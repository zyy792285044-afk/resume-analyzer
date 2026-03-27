# 部署到 Coze 平台指南

## 方式一：Git 推送部署（推荐）

### 1. 创建 Git 仓库

你可以选择以下任一平台：
- GitHub (https://github.com)
- GitLab (https://gitlab.com)
- Gitee (https://gitee.com) - 国内速度快

### 2. 推送代码到仓库

```bash
# 初始化 Git（如果还没有）
git init

# 添加所有文件
git add .

# 提交
git commit -m "初始化简历分析Agent项目"

# 添加远程仓库（以GitHub为例）
git remote add origin https://github.com/你的用户名/resume-analyzer.git

# 推送代码
git push -u origin main
```

### 3. 在 Coze 平台导入项目

1. 登录 Coze 平台：https://www.coze.cn
2. 点击右上角 "创建" → "创建项目"
3. 选择 "从 Git 导入"
4. 输入你的 Git 仓库地址
5. 点击 "导入"

### 4. 配置环境变量

在 Coze 项目设置中，添加以下环境变量：

```
COZE_WORKLOAD_IDENTITY_API_KEY=你的API密钥
COZE_INTEGRATION_MODEL_BASE_URL=https://api.coze.cn
```

### 5. 构建和部署

1. 点击 "构建" 按钮
2. 等待构建完成
3. 点击 "部署" 按钮
4. 部署成功后，获得访问链接

---

## 方式二：直接上传代码包

### 1. 打包项目

```bash
# 在项目根目录执行
tar -czf resume-analyzer.tar.gz \
  --exclude='.git' \
  --exclude='.venv' \
  --exclude='__pycache__' \
  --exclude='*.pyc' \
  .
```

### 2. 在 Coze 平台上传

1. 登录 Coze 平台
2. 点击 "创建项目"
3. 选择 "上传代码包"
4. 选择打包好的 `resume-analyzer.tar.gz`
5. 点击 "上传"

---

## 方式三：使用 Coze CLI 工具

### 1. 安装 Coze CLI

```bash
npm install -g @coze/cli
```

### 2. 登录 Coze

```bash
coze login
```

### 3. 部署项目

```bash
cd /workspace/projects
coze deploy
```

---

## 📱 部署后的访问方式

部署成功后，你会获得以下访问方式：

### 1. Web 界面访问

Coze 会自动生成一个网页界面，用户可以直接访问：

```
https://www.coze.cn/space/你的空间ID/agent/你的AgentID
```

### 2. API 接口访问

```bash
# 调用接口
curl -X POST https://api.coze.cn/v1/chat \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "bot_id": "YOUR_BOT_ID",
    "user_id": "user_123",
    "stream": false,
    "additional_messages": [{
      "role": "user",
      "content": "请帮我分析简历..."
    }]
  }'
```

### 3. 嵌入到你的网站

在你的网站中嵌入：

```html
<iframe 
  src="https://www.coze.cn/space/xxx/agent/xxx" 
  width="100%" 
  height="800px">
</iframe>
```

---

## ✅ 验证部署是否成功

### 1. 检查服务状态

```bash
# 如果部署成功，可以通过健康检查接口验证
curl https://你的部署地址/health
```

### 2. 测试 Agent

发送测试请求：

```bash
curl -X POST https://你的部署地址/run \
  -H "Content-Type: application/json" \
  -d '{
    "resume_input": "张三，5年产品经验...",
    "target_role": "AI产品经理",
    "candidate_level": "中级"
  }'
```

---

## 🔧 常见问题

### Q1: 部署失败，提示依赖安装错误

**解决方案：**
- 检查 `requirements.txt` 是否完整
- 确保所有依赖包都兼容 Python 3.12
- 查看 Coze 平台的构建日志

### Q2: 环境变量配置错误

**解决方案：**
- 在 Coze 项目设置中正确配置环境变量
- 确保 API Key 有效
- 检查 BASE_URL 是否正确

### Q3: 部署成功但无法访问

**解决方案：**
- 检查端口配置（默认 5000）
- 确认 `src/main.py` 中的路由正确
- 查看 Coze 平台的运行日志

---

## 💰 部署成本

### Coze 平台计费

**免费版：**
- 每月 5000 次调用
- 基础模型使用
- 基础功能

**专业版（99元/月）：**
- 无限次调用
- 高级模型
- 优先技术支持

---

## 🎯 推荐流程

1. **先本地测试**（已完成✅）
2. **推送到 Git 仓库**
3. **在 Coze 导入项目**
4. **配置环境变量**
5. **构建并部署**
6. **测试访问**
7. **分享链接给用户**

---

## 📞 需要帮助？

如果你遇到任何问题：
1. 查看 Coze 官方文档
2. 检查构建/运行日志
3. 在社区提问
4. 联系技术支持
