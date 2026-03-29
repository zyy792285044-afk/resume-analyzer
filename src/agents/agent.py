"""
简历战斗力分析Agent
功能：单次输入简历文本或PDF，输出完整的战斗力分析报告
"""
import os
import json
from typing import Annotated, Optional, Dict, Any
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langgraph.graph import MessagesState
from langgraph.graph.message import add_messages
from langchain_core.messages import AnyMessage
from coze_coding_utils.runtime_ctx.context import default_headers
from storage.memory import get_memory_saver
from tools.resume_parser import parse_resume_from_url, parse_resume_from_text
from tools.pdf_generator import generate_pdf_report, generate_docx_report

LLM_CONFIG = "config/agent_llm_config.json"

# 默认保留最近 20 轮对话 (40 条消息)
MAX_MESSAGES = 40


def _windowed_messages(old, new):
    """滑动窗口: 只保留最近 MAX_MESSAGES 条消息"""
    return add_messages(old, new)[-MAX_MESSAGES:]  # type: ignore


class AgentState(MessagesState):
    """Agent状态，包含消息历史"""
    messages: Annotated[list[AnyMessage], _windowed_messages]


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


def build_agent(ctx=None):
    """
    构建Agent实例（遵循规范要求的build_agent函数）
    
    Args:
        ctx: 运行时上下文（可选）
    
    Returns:
        Agent实例
    """
    workspace_path = os.getenv("COZE_WORKSPACE_PATH", "/workspace/projects")
    config_path = os.path.join(workspace_path, LLM_CONFIG)

    with open(config_path, 'r', encoding='utf-8') as f:
        cfg = json.load(f)

    api_key = os.getenv("COZE_WORKLOAD_IDENTITY_API_KEY")
    base_url = os.getenv("COZE_INTEGRATION_MODEL_BASE_URL")

    llm = ChatOpenAI(
        model=cfg['config'].get("model"),
        api_key=api_key,
        base_url=base_url,
        temperature=cfg['config'].get('temperature', 0.7),
        streaming=True,
        timeout=cfg['config'].get('timeout', 600),
        extra_body={
            "thinking": {
                "type": cfg['config'].get('thinking', 'disabled')
            }
        },
        default_headers=default_headers(ctx) if ctx else {}
    )

    return create_agent(
        model=llm,
        system_prompt=cfg.get("sp"),
        tools=[parse_resume_from_url, parse_resume_from_text, generate_pdf_report, generate_docx_report],
        checkpointer=get_memory_saver(),
        state_schema=AgentState,
    )
