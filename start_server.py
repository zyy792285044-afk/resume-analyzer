#!/usr/bin/env python3
"""
本地服务器 - 用于测试简历分析网页
"""

import http.server
import socketserver
import os
import webbrowser
from functools import partial

PORT = 8080
DIRECTORY = os.path.join(os.path.dirname(__file__), "assets")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        # 添加CORS头
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}/resume-chat.html"
        print(f"\n{'='*60}")
        print(f"🚀 本地服务器已启动！")
        print(f"{'='*60}")
        print(f"\n📱 访问地址：")
        print(f"   PC端: {url}")
        print(f"   手机: 在手机浏览器输入 http://你的IP地址:{PORT}/resume-chat.html")
        print(f"\n💡 提示：")
        print(f"   - 按 Ctrl+C 停止服务器")
        print(f"   - 支持PC和移动端自适应显示")
        print(f"{'='*60}\n")
        
        # 自动打开浏览器
        webbrowser.open(url)
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n👋 服务器已停止")
