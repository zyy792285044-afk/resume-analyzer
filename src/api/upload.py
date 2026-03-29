"""
文件上传API端点
用于处理前端上传的PDF/Word文件
"""
import os
import base64
import tempfile
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from coze_coding_dev_sdk.fetch import FetchClient
from coze_coding_utils.runtime_ctx.context import new_context
from coze_coding_utils.log.write_log import request_context

router = APIRouter()


@router.post("/upload_file")
async def upload_file(file: UploadFile = File(...)):
    """
    上传并解析文件
    
    Args:
        file: 上传的文件
    
    Returns:
        解析后的文本内容
    """
    try:
        # 获取上下文
        ctx = request_context.get() or new_context(method="upload_file")
        
        # 读取文件内容
        file_bytes = await file.read()
        
        # 获取文件扩展名
        file_ext = os.path.splitext(file.filename)[1].lower()
        
        # 支持的文件类型
        allowed_extensions = ['.pdf', '.doc', '.docx', '.txt']
        if file_ext not in allowed_extensions:
            raise HTTPException(
                status_code=400,
                detail=f"不支持的文件类型: {file_ext}。请上传PDF、Word或文本文件。"
            )
        
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
                    raise HTTPException(
                        status_code=500,
                        detail=f"解析失败: {response.status_message}"
                    )
                
                # 提取文本内容
                text_parts = []
                for item in response.content:
                    if item.type == "text" and hasattr(item, 'text') and item.text:
                        text_parts.append(item.text)
                
                if not text_parts:
                    raise HTTPException(
                        status_code=500,
                        detail="解析失败: 未找到文本内容"
                    )
                
                # 合并所有文本
                file_text = "\n\n".join(text_parts)
                
                return JSONResponse({
                    "success": True,
                    "filename": file.filename,
                    "content": file_text
                })
                
            finally:
                # 删除临时文件
                if os.path.exists(tmp_path):
                    os.unlink(tmp_path)
        
        else:
            # 文本文件，直接解码
            try:
                text = file_bytes.decode('utf-8')
                return JSONResponse({
                    "success": True,
                    "filename": file.filename,
                    "content": text
                })
            except:
                raise HTTPException(
                    status_code=400,
                    detail="无法解码文本文件，请确保是UTF-8编码"
                )
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"处理出错: {str(e)}")
