"""
简历战斗力分析Agent
功能：单次输入简历文本，输出完整的战斗力分析报告
"""
import os
import json
from typing import Optional, Dict, Any, Iterator
from coze_coding_dev_sdk import LLMClient
from coze_coding_utils.runtime_ctx.context import new_context
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, AIMessageChunk

LLM_CONFIG = "config/agent_llm_config.json"


def get_text_content(content) -> str:
    """安全提取AIMessage中的文本内容"""
    if isinstance(content, str):
        return content
    elif isinstance(content, list):
        if content and isinstance(content[0], str):
            return " ".join(content)
        else:
            text_parts = []
            for item in content:
                if isinstance(item, dict) and item.get("type") == "text":
                    text_parts.append(item.get("text", ""))
            return " ".join(text_parts)
    else:
        return str(content)


class ResumeAnalysisAgent:
    """简历战斗力分析Agent"""
    
    def __init__(self):
        """初始化Agent"""
        self.workspace_path = os.getenv("COZE_WORKSPACE_PATH", "/workspace/projects")
        self.config_path = os.path.join(self.workspace_path, LLM_CONFIG)
        
        # 加载配置
        with open(self.config_path, 'r', encoding='utf-8') as f:
            self.config = json.load(f)
    
    def stream(
        self,
        input_data: Dict[str, Any],
        config: Optional[Dict[str, Any]] = None,
        **kwargs
    ) -> Iterator[AIMessageChunk]:
        """
        流式分析简历并生成战斗力报告
        
        Args:
            input_data: 输入数据，包含以下字段：
                - resume_text: 简历文本内容
                - target_role: 目标岗位
                - candidate_level: 候选人级别（可选）
            config: 配置参数（可选）
            **kwargs: 其他参数（如stream_mode等，会被忽略）
        
        Yields:
            AIMessageChunk: 流式输出的消息块
        """
        # 提取参数
        resume_text = input_data.get("resume_text", "")
        target_role = input_data.get("target_role", "产品经理")
        candidate_level = input_data.get("candidate_level", "中级")
        
        # 构建用户输入
        user_input = {
            "resume_text": resume_text,
            "target_role": target_role,
            "candidate_level": candidate_level
        }
        
        # 创建LLM客户端
        ctx = new_context(method="resume_analysis")
        client = LLMClient(ctx=ctx)
        
        # 构建消息
        messages = [
            SystemMessage(content=self.config["sp"]),
            HumanMessage(content=json.dumps(user_input, ensure_ascii=False, indent=2))
        ]
        
        # 流式调用LLM
        for chunk in client.stream(
            messages=messages,
            model=self.config["config"]["model"],
            temperature=self.config["config"]["temperature"],
            top_p=self.config["config"]["top_p"],
            max_completion_tokens=self.config["config"]["max_completion_tokens"],
            thinking=self.config["config"]["thinking"]
        ):
            if chunk.content:
                yield AIMessageChunk(content=chunk.content)
    
    def invoke(
        self,
        input_data: Dict[str, Any],
        config: Optional[Dict[str, Any]] = None
    ) -> AIMessage:
        """
        同步分析简历并生成战斗力报告
        
        Args:
            input_data: 输入数据，包含以下字段：
                - resume_text: 简历文本内容
                - target_role: 目标岗位
                - candidate_level: 候选人级别（可选）
            config: 配置参数（可选）
        
        Returns:
            AIMessage: 分析结果
        """
        # 提取参数
        resume_text = input_data.get("resume_text", "")
        target_role = input_data.get("target_role", "产品经理")
        candidate_level = input_data.get("candidate_level", "中级")
        
        # 构建用户输入
        user_input = {
            "resume_text": resume_text,
            "target_role": target_role,
            "candidate_level": candidate_level
        }
        
        # 创建LLM客户端
        ctx = new_context(method="resume_analysis")
        client = LLMClient(ctx=ctx)
        
        # 构建消息
        messages = [
            SystemMessage(content=self.config["sp"]),
            HumanMessage(content=json.dumps(user_input, ensure_ascii=False, indent=2))
        ]
        
        # 调用LLM
        response = client.invoke(
            messages=messages,
            model=self.config["config"]["model"],
            temperature=self.config["config"]["temperature"],
            top_p=self.config["config"]["top_p"],
            max_completion_tokens=self.config["config"]["max_completion_tokens"],
            thinking=self.config["config"]["thinking"]
        )
        
        # 提取响应文本
        response_text = get_text_content(response.content)
        
        # 清理markdown代码块标记
        cleaned_text = response_text.strip()
        if cleaned_text.startswith("```json"):
            cleaned_text = cleaned_text[7:]  # 移除 ```json
            if cleaned_text.endswith("```"):
                cleaned_text = cleaned_text[:-3]  # 移除结尾的 ```
        elif cleaned_text.startswith("```"):
            cleaned_text = cleaned_text[3:]  # 移除 ```
            if cleaned_text.endswith("```"):
                cleaned_text = cleaned_text[:-3]  # 移除结尾的 ```
        
        cleaned_text = cleaned_text.strip()
        
        # 尝试解析JSON
        try:
            result = json.loads(cleaned_text)
            return AIMessage(content=json.dumps(result, ensure_ascii=False, indent=2))
        except json.JSONDecodeError as e:
            # 如果解析失败，尝试提取JSON部分
            import re
            json_match = re.search(r'\{[\s\S]*\}', cleaned_text)
            if json_match:
                try:
                    result = json.loads(json_match.group())
                    return AIMessage(content=json.dumps(result, ensure_ascii=False, indent=2))
                except json.JSONDecodeError:
                    pass
            
            # 如果仍然失败，返回原始文本
            return AIMessage(content=response_text)


def build_agent(ctx=None):
    """
    构建Agent实例（遵循规范要求的build_agent函数）
    
    Args:
        ctx: 运行时上下文（可选）
    
    Returns:
        ResumeAnalysisAgent实例
    """
    return ResumeAnalysisAgent()
