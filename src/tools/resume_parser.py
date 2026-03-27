"""
简历解析工具
支持从PDF URL或文本解析简历内容
"""
from langchain.tools import tool
from coze_coding_dev_sdk.fetch import FetchClient
from coze_coding_utils.runtime_ctx.context import new_context


@tool
def parse_resume_from_url(resume_url: str) -> str:
    """
    从PDF URL解析简历内容。
    
    当用户提供简历PDF的下载链接时使用此工具。
    支持PDF、Word等格式的文档解析。
    
    Args:
        resume_url: 简历文档的URL链接（PDF/Word等）
    
    Returns:
        解析后的简历文本内容
    """
    try:
        # 获取上下文
        ctx = new_context(method="parse_resume_url")
        
        # 创建FetchClient
        client = FetchClient(ctx=ctx)
        
        # 解析URL内容
        response = client.fetch(url=resume_url)
        
        # 检查解析状态
        if response.status_code != 0:
            return f"解析失败: {response.status_message}"
        
        # 提取文本内容
        text_parts = []
        for item in response.content:
            if item.type == "text" and hasattr(item, 'text') and item.text:
                text_parts.append(item.text)
        
        if not text_parts:
            return "解析失败: 未找到文本内容"
        
        # 合并所有文本
        resume_text = "\n\n".join(text_parts)
        
        return f"简历解析成功:\n\n{resume_text}"
        
    except Exception as e:
        return f"解析出错: {str(e)}"


@tool
def parse_resume_from_text(resume_text: str) -> str:
    """
    处理用户直接粘贴的简历文本。
    
    当用户直接输入或粘贴简历文本内容时使用此工具。
    会自动清理和格式化文本。
    
    Args:
        resume_text: 用户粘贴的简历文本
    
    Returns:
        格式化后的简历文本
    """
    try:
        # 清理文本
        cleaned_text = resume_text.strip()
        
        # 移除多余的空行
        lines = cleaned_text.split('\n')
        cleaned_lines = []
        prev_empty = False
        
        for line in lines:
            is_empty = not line.strip()
            if is_empty:
                if not prev_empty:
                    cleaned_lines.append('')
                prev_empty = True
            else:
                cleaned_lines.append(line.strip())
                prev_empty = False
        
        result = '\n'.join(cleaned_lines)
        
        return f"简历文本处理完成:\n\n{result}"
        
    except Exception as e:
        return f"处理出错: {str(e)}"
