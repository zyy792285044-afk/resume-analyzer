# 🚀 Gitee Pages 部署指南（国内用户推荐）

## 为什么选择Gitee？

| 对比项 | Gitee Pages | GitHub Pages |
|--------|------------|--------------|
| 国内访问速度 | ⭐⭐⭐⭐⭐ 秒开 | ⭐⭐ 慢/打不开 |
| 稳定性 | ⭐⭐⭐⭐⭐ 不被墙 | ⭐⭐⭐ 可能被墙 |
| 费用 | 免费 | 免费 |
| 推荐度（国内用户） | ⭐⭐⭐⭐⭐ | ⭐⭐ |

---

## 📝 部署步骤（5分钟完成）

### 第1步：注册Gitee账号

**访问：** https://gitee.com/signup

填写：
- 用户名
- 邮箱
- 密码

点击「注册」→ 验证邮箱

---

### 第2步：创建仓库

1. 登录后点击右上角「**+**」→「**新建仓库**」

2. 填写信息：
   ```
   仓库名称：resume-analyzer
   路径：resume-analyzer（自动填充）
   仓库介绍：简历战斗力分析工具
   是否开源：公开
   ```

3. ❌ **不要勾选**：
   - 添加README.md
   - 添加.gitignore
   - 添加开源许可证

4. 点击「**创建**」

---

### 第3步：创建文件

1. 进入仓库页面

2. 点击「**+**」→「**新建文件**」

3. 在文件路径输入：
   ```
   docs/index.html
   ```
   （输入 `docs/` 后会自动创建文件夹）

4. 复制粘贴HTML代码（见下方）

5. 填写提交信息：
   ```
   feat: 部署简历分析网页
   ```

6. 点击「**提交**」

---

### 第4步：启用Gitee Pages

1. 进入仓库页面

2. 点击顶部菜单「**服务**」→「**Gitee Pages**」

3. 配置：
   ```
   部署分支：master（或main）
   部署目录：/docs
   ```

4. 点击「**启动**」

5. 等待几秒钟，页面会显示：
   ```
   你的网站已发布
   https://您的用户名.gitee.io/resume-analyzer/
   ```

---

### 第5步：访问测试

**访问地址：**
```
https://您的用户名.gitee.io/resume-analyzer/
```

**示例：**
```
如果用户名是 zhangsan
访问：https://zhangsan.gitee.io/resume-analyzer/
```

---

## 📋 完整HTML代码

复制以下代码粘贴到 `docs/index.html`：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>简历战斗力分析</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'PingFang SC', 'Microsoft YaHei', sans-serif;
            background: #f5f5f5;
            height: 100vh;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }
        
        @media (min-width: 769px) {
            body {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            }
            .header {
                max-width: 800px;
                margin: 20px auto 0;
                border-radius: 16px 16px 0 0;
            }
            .chat-container {
                max-width: 800px;
                margin: 0 auto;
                background: white;
                box-shadow: 0 0 30px rgba(0,0,0,0.2);
            }
            .input-container {
                max-width: 800px;
                margin: 0 auto 20px;
                border-radius: 0 0 16px 16px;
            }
        }
        
        @media (max-width: 768px) {
            body {
                background: #f5f5f5;
            }
        }
        
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .header-title {
            font-size: 18px;
            font-weight: 600;
        }
        
        .header-subtitle {
            font-size: 12px;
            opacity: 0.9;
        }
        
        .chat-container {
            flex: 1;
            overflow-y: auto;
            padding: 15px;
            display: flex;
            flex-direction: column;
            gap: 15px;
        }
        
        .message {
            max-width: 85%;
            animation: fadeIn 0.3s ease-in-out;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .message-user { align-self: flex-end; }
        .message-ai { align-self: flex-start; }
        
        .message-content {
            padding: 12px 15px;
            border-radius: 15px;
            font-size: 15px;
            line-height: 1.6;
        }
        
        .message-user .message-content {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-bottom-right-radius: 5px;
        }
        
        .message-ai .message-content {
            background: white;
            color: #333;
            border-bottom-left-radius: 5px;
            box-shadow: 0 1px 5px rgba(0,0,0,0.1);
        }
        
        .message-ai .message-content h2 {
            font-size: 18px;
            margin: 15px 0 10px 0;
            color: #667eea;
        }
        
        .message-ai .message-content h3 {
            font-size: 16px;
            margin: 12px 0 8px 0;
            color: #333;
        }
        
        .message-ai .message-content ul, .message-ai .message-content ol {
            padding-left: 20px;
            margin: 10px 0;
        }
        
        .message-ai .message-content li { margin: 5px 0; }
        
        .message-ai .message-content strong {
            color: #667eea;
            font-weight: 600;
        }
        
        .message-ai .message-content hr {
            border: none;
            border-top: 1px solid #e0e0e0;
            margin: 15px 0;
        }
        
        .input-container {
            background: white;
            padding: 10px 15px;
            box-shadow: 0 -2px 10px rgba(0,0,0,0.05);
        }
        
        .input-main {
            display: flex;
            align-items: flex-end;
            gap: 10px;
        }
        
        .input-wrapper {
            flex: 1;
            display: flex;
            background: #f5f5f5;
            border-radius: 20px;
            padding: 5px;
        }
        
        .text-input {
            flex: 1;
            border: none;
            background: transparent;
            padding: 8px 12px;
            font-size: 15px;
            outline: none;
            resize: none;
            max-height: 100px;
            min-height: 36px;
        }
        
        .send-btn {
            width: 40px;
            height: 40px;
            border: none;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 50%;
            font-size: 18px;
            cursor: pointer;
            transition: transform 0.2s;
        }
        
        .send-btn:hover {
            transform: scale(1.05);
        }
        
        .send-btn:disabled {
            background: #ccc;
            cursor: not-allowed;
        }
        
        .welcome-message {
            text-align: center;
            padding: 40px 20px;
            color: #666;
        }
        
        .welcome-icon {
            font-size: 48px;
            margin-bottom: 15px;
        }
        
        .welcome-title {
            font-size: 20px;
            font-weight: 600;
            color: #333;
            margin-bottom: 10px;
        }
        
        .welcome-desc {
            font-size: 14px;
            line-height: 1.8;
            color: #999;
        }
        
        .typing-indicator {
            display: flex;
            gap: 4px;
            padding: 15px;
            background: white;
            border-radius: 15px;
            box-shadow: 0 1px 5px rgba(0,0,0,0.1);
        }
        
        .typing-dot {
            width: 8px;
            height: 8px;
            background: #667eea;
            border-radius: 50%;
            animation: typing 1.4s infinite;
        }
        
        .typing-dot:nth-child(1) { animation-delay: 0s; }
        .typing-dot:nth-child(2) { animation-delay: 0.2s; }
        .typing-dot:nth-child(3) { animation-delay: 0.4s; }
        
        @keyframes typing {
            0%, 60%, 100% { transform: translateY(0); }
            30% { transform: translateY(-10px); }
        }
    </style>
</head>
<body>
    <div class="header">
        <div>
            <div class="header-title">简历战斗力分析</div>
            <div class="header-subtitle">专业评估 · 精准诊断</div>
        </div>
    </div>
    
    <div class="chat-container" id="chatContainer">
        <div class="welcome-message">
            <div class="welcome-icon">📄</div>
            <div class="welcome-title">欢迎使用简历分析助手</div>
            <div class="welcome-desc">
                请粘贴您的简历内容<br>
                我将为您提供专业的战斗力分析和优化建议
            </div>
        </div>
    </div>
    
    <div class="input-container">
        <div class="input-main">
            <div class="input-wrapper">
                <textarea class="text-input" id="textInput" placeholder="粘贴简历内容..." rows="1" onkeydown="handleKeyDown(event)"></textarea>
            </div>
            <button class="send-btn" id="sendBtn" onclick="sendMessage()">➤</button>
        </div>
    </div>
    
    <script>
        const API_URL = 'https://4925fcc2-b204-42d1-b939-4f2b318b1d14.dev.coze.site/stream_run';
        let isLoading = false;
        
        function handleKeyDown(event) {
            if (event.key === 'Enter' && !event.shiftKey) {
                event.preventDefault();
                sendMessage();
            }
        }
        
        async function sendMessage() {
            const input = document.getElementById('textInput');
            const message = input.value.trim();
            
            if (!message || isLoading) return;
            
            isLoading = true;
            document.getElementById('sendBtn').disabled = true;
            
            addMessage(message, 'user');
            input.value = '';
            input.style.height = 'auto';
            
            const loadingId = showTypingIndicator();
            
            try {
                const sessionId = 'session_' + Date.now();
                
                const response = await fetch(API_URL, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        type: "query",
                        session_id: sessionId,
                        content: {
                            query: {
                                prompt: [{
                                    type: "text",
                                    content: { text: message }
                                }]
                            }
                        }
                    })
                });
                
                if (!response.ok) throw new Error(`API请求失败: ${response.status}`);
                
                removeTypingIndicator(loadingId);
                
                const reader = response.body.getReader();
                const decoder = new TextDecoder();
                let aiMessage = '';
                let messageId = null;
                
                while (true) {
                    const { done, value } = await reader.read();
                    if (done) break;
                    
                    const chunk = decoder.decode(value, { stream: true });
                    const lines = chunk.split('\n');
                    
                    for (const line of lines) {
                        if (line.startsWith('data: ')) {
                            try {
                                const data = JSON.parse(line.slice(6));
                                if (data.type === 'answer' && data.content) {
                                    if (!messageId) messageId = addMessage('', 'ai', true);
                                    aiMessage += data.content;
                                    updateMessage(messageId, aiMessage);
                                } else if (data.content) {
                                    if (!messageId) messageId = addMessage('', 'ai', true);
                                    aiMessage += data.content;
                                    updateMessage(messageId, aiMessage);
                                }
                            } catch (e) {}
                        }
                    }
                }
            } catch (error) {
                removeTypingIndicator(loadingId);
                addMessage('抱歉，分析过程中出现错误：' + error.message, 'ai');
            } finally {
                isLoading = false;
                document.getElementById('sendBtn').disabled = false;
            }
        }
        
        function addMessage(content, type) {
            const container = document.getElementById('chatContainer');
            const messageDiv = document.createElement('div');
            const messageId = 'msg_' + Date.now();
            
            messageDiv.id = messageId;
            messageDiv.className = `message message-${type}`;
            
            const contentDiv = document.createElement('div');
            contentDiv.className = 'message-content';
            contentDiv.innerHTML = formatMessage(content);
            
            messageDiv.appendChild(contentDiv);
            container.appendChild(messageDiv);
            container.scrollTop = container.scrollHeight;
            
            return messageId;
        }
        
        function updateMessage(messageId, content) {
            const messageDiv = document.getElementById(messageId);
            if (messageDiv) {
                const contentDiv = messageDiv.querySelector('.message-content');
                contentDiv.innerHTML = formatMessage(content);
                document.getElementById('chatContainer').scrollTop = document.getElementById('chatContainer').scrollHeight;
            }
        }
        
        function formatMessage(text) {
            if (!text) return '';
            let formatted = text
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;');
            formatted = formatted.replace(/^### (.*$)/gim, '<h3>$1</h3>');
            formatted = formatted.replace(/^## (.*$)/gim, '<h2>$1</h2>');
            formatted = formatted.replace(/^# (.*$)/gim, '<h2>$1</h2>');
            formatted = formatted.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
            formatted = formatted.replace(/^\- (.*$)/gim, '<li>$1</li>');
            formatted = formatted.replace(/^\d+\. (.*$)/gim, '<li>$1</li>');
            formatted = formatted.replace(/\n/g, '<br>');
            formatted = formatted.replace(/---/g, '<hr>');
            return formatted;
        }
        
        function showTypingIndicator() {
            const container = document.getElementById('chatContainer');
            const loadingDiv = document.createElement('div');
            const loadingId = 'loading_' + Date.now();
            
            loadingDiv.id = loadingId;
            loadingDiv.className = 'message message-ai';
            loadingDiv.innerHTML = '<div class="typing-indicator"><div class="typing-dot"></div><div class="typing-dot"></div><div class="typing-dot"></div></div>';
            
            container.appendChild(loadingDiv);
            container.scrollTop = container.scrollHeight;
            
            return loadingId;
        }
        
        function removeTypingIndicator(loadingId) {
            const loadingDiv = document.getElementById(loadingId);
            if (loadingDiv) loadingDiv.remove();
        }
        
        const textInput = document.getElementById('textInput');
        textInput.addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = Math.min(this.scrollHeight, 100) + 'px';
        });
    </script>
</body>
</html>
```

---

## ✅ 部署成功后

**访问地址：**
```
https://您的用户名.gitee.io/resume-analyzer/
```

**特点：**
- ✅ 国内秒开
- ✅ 稳定不挂
- ✅ 永久免费
- ✅ HTTPS安全

---

## 📱 分享示例

**小红书：**
```
姐妹们！发现一个超实用的简历分析工具！

🔗 链接：https://您的用户名.gitee.io/resume-analyzer/

只需3步：
1️⃣ 打开链接
2️⃣ 粘贴简历
3️⃣ 获得专业分析

完全免费！秒开！
#简历 #求职 #面试技巧
```

---

## 💡 总结

**国内用户 → Gitee Pages**（推荐）
**国外用户 → GitHub Pages**

现在就去Gitee创建吧！🚀
