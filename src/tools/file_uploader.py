"""
文件上传工具
支持前端上传PDF/Word文件，后端解析内容
"""
import os
import base64
import tempfile
from langchain.tools import tool
from coze_coding_dev_sdk.s3 import S3SyncStorage
from coze_coding_dev_sdk.fetch import FetchClient
from coze_coding_utils.runtime_ctx.context import new_context
from coze_coding_utils.log.write_log import request_context


@tool
def upload_and_parse_file(file_base64: str, file_name: str) -> str:
    """
    上传并解析文件内容。
    
    前端将文件转为Base64后调用此工具。
    支持PDF、Word等格式的文档解析。
    
    Args:
        file_base64: Base64编码的文件内容
        file_name: 原始文件名
    
    Returns:
        解析后的文件文本内容
    """
    try:
        # 获取上下文
        ctx = request_context.get() or new_context(method="upload_parse_file")
        
        # 解码Base64
        file_bytes = base64.b64decode(file_base64)
        
        # 判断文件类型
        file_ext = os.path.splitext(file_name)[1].lower()
        
        # 如果是PDF或Word，使用FetchClient解析
        if file_ext in ['.pdf', '.doc', '.docx']:
            # 保存为临时文件
            with tempfile.NamedTemporaryFile(delete=False, suffix=file_ext) as tmp:
                tmp.write(file_bytes)
                tmp_path = tmp.name
            
            try:
                # 使用FetchClient解析
                client = FetchClient(ctx=ctx)
                response = client.fetch(url=f"file://{tmp_path}")
                
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
                file_text = "\n\n".join(text_parts)
                
                return f"文件解析成功:\n\n{file_text}"
                
            finally:
                # 删除临时文件
                if os.path.exists(tmp_path):
                    os.unlink(tmp_path)
        
        else:
            # 其他文件类型，尝试解码为文本
            try:
                text = file_bytes.decode('utf-8')
                return f"文件内容:\n\n{text}"
            except:
                return "不支持的文件类型，请上传PDF或Word文档"
    
    except Exception as e:
        return f"处理出错: {str(e)}"


@tool
def upload_file_to_storage(file_base64: str, file_name: str, content_type: str = "application/pdf") -> str:
    """
    上传文件到对象存储并返回URL。
    
    Args:
        file_base64: Base64编码的文件内容
        file_name: 原始文件名
        content_type: 文件MIME类型
    
    Returns:
        文件的访问URL
    """
    try:
        # 获取上下文
        ctx = request_context.get() or new_context(method="upload_file")
        
        # 解码Base64
        file_bytes = base64.b64decode(file_base64)
        
        # 初始化存储
        storage = S3SyncStorage(
            endpoint_url=os.getenv("COZE_BUCKET_ENDPOINT_URL"),
            access_key="",
            secret_key="",
            bucket_name=os.getenv("COZE_BUCKET_NAME"),
            region="cn-beijing",
        )
        
        # 上传文件
        key = storage.upload_file(
            file_content=file_bytes,
            file_name=f"resumes/{file_name}",
            content_type=content_type,
        )
        
        # 生成访问URL（有效期24小时）
        url = storage.generate_presigned_url(
            key=key,
            expire_time=86400,
        )
        
        return f"文件上传成功，访问地址: {url}"
    
    except Exception as e:
        return f"上传失败: {str(e)}"
