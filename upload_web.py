import os
from coze_coding_dev_sdk.s3 import S3SyncStorage

# 初始化存储客户端
storage = S3SyncStorage(
    endpoint_url=os.getenv("COZE_BUCKET_ENDPOINT_URL"),
    access_key="",
    secret_key="",
    bucket_name=os.getenv("COZE_BUCKET_NAME"),
    region="cn-beijing",
)

# 读取HTML文件
with open('assets/resume-chat.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# 上传文件
file_key = storage.upload_file(
    file_content=html_content.encode('utf-8'),
    file_name="resume-chat.html",
    content_type="text/html",
)

# 生成访问链接（有效期30天）
access_url = storage.generate_presigned_url(
    key=file_key,
    expire_time=2592000,  # 30天
)

print(f"✅ 上传成功！")
print(f"文件Key: {file_key}")
print(f"访问链接: {access_url}")
print(f"\n用户可以直接访问这个链接使用简历分析功能！")
print(f"有效期: 30天")
