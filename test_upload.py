import os
from coze_coding_dev_sdk.s3 import S3SyncStorage

print("=== 开始上传网页文件 ===")

# 初始化存储客户端
storage = S3SyncStorage(
    endpoint_url=os.getenv("COZE_BUCKET_ENDPOINT_URL"),
    access_key="",
    secret_key="",
    bucket_name=os.getenv("COZE_BUCKET_NAME"),
    region="cn-beijing",
)

print(f"存储桶: {os.getenv('COZE_BUCKET_NAME')}")
print(f"Endpoint: {os.getenv('COZE_BUCKET_ENDPOINT_URL')}")

# 读取HTML文件
with open('assets/resume-chat.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

print(f"\n文件大小: {len(html_content)} 字符")

# 上传文件
file_key = storage.upload_file(
    file_content=html_content.encode('utf-8'),
    file_name="index.html",
    content_type="text/html; charset=utf-8",
)

print(f"\n上传成功!")
print(f"文件Key: {file_key}")

# 生成访问链接
print("\n正在生成访问链接...")
access_url = storage.generate_presigned_url(
    key=file_key,
    expire_time=2592000,  # 30天
)

print(f"\n✅ 访问链接: {access_url}")
print(f"有效期: 30天")

# 验证文件是否存在
exists = storage.file_exists(file_key)
print(f"\n文件存在验证: {exists}")
