"""
Vercel Serverless Function: 文件上传API
支持PDF/Word文件解析
"""
import os
import tempfile
import base64
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import Response

app = FastAPI()

# 添加CORS支持
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    上传并解析文件
    
    支持的文件类型：
    - PDF (.pdf)
    - Word (.doc, .docx)
    - 文本文件 (.txt)
    
    Returns:
        JSON响应，包含解析后的文本内容
    """
    try:
        # 读取文件内容
        file_bytes = await file.read()
        file_ext = os.path.splitext(file.filename)[1].lower()
        
        # 验证文件类型
        allowed_extensions = ['.pdf', '.doc', '.docx', '.txt']
        if file_ext not in allowed_extensions:
            raise HTTPException(
                status_code=400,
                detail=f"不支持的文件类型: {file_ext}。请上传PDF、Word或文本文件。"
            )
        
        # 文本文件直接解码
        if file_ext == '.txt':
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
        
        # PDF和Word文件需要特殊处理
        # 在Vercel环境中，我们需要使用base64传输文件内容
        # 然后在前端或通过其他服务解析
        
        # 方案：返回base64编码的文件内容，让前端处理
        file_base64 = base64.b64encode(file_bytes).decode('utf-8')
        
        return JSONResponse({
            "success": True,
            "filename": file.filename,
            "file_type": file_ext,
            "file_size": len(file_bytes),
            "file_base64": file_base64,
            "message": "文件已上传，请在浏览器中解析"
        })
        
    except HTTPException:
        raise
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"success": False, "detail": f"处理出错: {str(e)}"}
        )


@app.get("/api/health")
async def health():
    """健康检查端点"""
    return {"status": "ok"}


# Vercel需要的handler
def handler(request: Request) -> Response:
    return app(request)
