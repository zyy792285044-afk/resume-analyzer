"""
PDF报告生成工具
将Markdown格式的简历分析报告转换为PDF文档
"""
from langchain.tools import tool
from coze_coding_dev_sdk import DocumentGenerationClient, PDFConfig


@tool
def generate_pdf_report(markdown_content: str, title: str = "resume_analysis_report") -> str:
    """
    将Markdown格式的简历分析报告转换为PDF文档。
    
    当用户要求输出PDF格式时使用此工具。
    会生成一份专业排版的PDF报告，包含完整的分析内容。
    
    Args:
        markdown_content: Markdown格式的报告内容
        title: PDF文档标题（英文，用于文件名生成，默认"resume_analysis_report"）
    
    Returns:
        PDF文档的下载链接（有效期24小时）
    """
    try:
        # 配置PDF参数（A4纸张，适合简历报告）
        pdf_config = PDFConfig(
            page_size="A4",
            left_margin=72,
            right_margin=72,
            top_margin=72,
            bottom_margin=72
        )
        
        # 创建客户端（不传ctx参数）
        client = DocumentGenerationClient(pdf_config=pdf_config)
        
        # 生成PDF
        pdf_url = client.create_pdf_from_markdown(markdown_content, title)
        
        return f"PDF报告已生成成功！\n\n下载链接：{pdf_url}\n\n（链接有效期24小时，请及时下载）"
        
    except Exception as e:
        return f"PDF生成失败: {str(e)}"


@tool
def generate_docx_report(markdown_content: str, title: str = "resume_analysis_report") -> str:
    """
    将Markdown格式的简历分析报告转换为Word文档。
    
    当用户要求输出Word格式时使用此工具。
    会生成一份可编辑的Word文档，方便用户后续修改。
    
    Args:
        markdown_content: Markdown格式的报告内容
        title: Word文档标题（英文，用于文件名生成，默认"resume_analysis_report"）
    
    Returns:
        Word文档的下载链接（有效期24小时）
    """
    try:
        # 创建客户端（不传ctx参数）
        client = DocumentGenerationClient()
        
        # 生成Word文档
        docx_url = client.create_docx_from_markdown(markdown_content, title)
        
        return f"Word报告已生成成功！\n\n下载链接：{docx_url}\n\n（链接有效期24小时，请及时下载）"
        
    except Exception as e:
        return f"Word文档生成失败: {str(e)}"
