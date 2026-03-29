# 简历战斗力分析 Agent

专业的简历分析助手，提供战斗力评分、问题诊断和优化建议，支持PDF上传解析和报告下载。

## ✨ 功能特性

- 📄 **简历分析** - 战斗力评分、四维拆解、三大致命问题诊断
- 📎 **文件上传** - 支持PDF/Word文件上传和自动解析
- 📊 **报告下载** - 支持PDF/Word格式报告下载
- 💬 **对话交互** - 流式输出，类微信聊天体验
- 📱 **移动适配** - 完美适配PC和移动端

## 🚀 快速开始

### 方式一：本地运行

```bash
# 启动服务
bash scripts/local_run.sh -m flow

# 启动HTTP服务
bash scripts/http_run.sh -p 5000
```

### 方式二：在线访问

- **GitHub Pages**: [在线体验](https://zyy792285044-afk.github.io/resume-analyzer/)
- **本地前端**: 启动服务后访问 `http://localhost:5000`

## 📚 使用指南

- [快速开始指南](docs/guides/QUICK_START_GUIDE.md)
- [Coze平台部署](docs/guides/COZE_PLATFORM_GUIDE.md)
- [Coze Bot配置](docs/guides/COZE_BOT_SIMPLE_PROMPT.md)

## 🛠️ 技术栈

- **后端**: Python 3.12 + LangChain + LangGraph + FastAPI
- **前端**: HTML5 + CSS3 + Vanilla JavaScript
- **模型**: 豆包·Seed 2.0 Pro
- **SDK**: coze-coding-dev-sdk

## 📁 项目结构

```
.
├── api/              # Vercel API端点
├── docs/             # 文档和前端页面
├── src/              # 源代码
│   ├── agents/       # Agent核心逻辑
│   ├── tools/        # 工具函数
│   └── api/          # API接口
├── config/           # 配置文件
└── scripts/          # 脚本文件
```

## 📝 使用方式

1. **上传简历** - 点击📎按钮上传PDF/Word文件
2. **粘贴简历** - 直接粘贴简历文本
3. **获取分析** - AI自动分析并生成报告
4. **下载报告** - 点击"生成PDF报告"按钮

## 🔗 相关链接

- [GitHub仓库](https://github.com/zyy792285044-afk/resume-analyzer)
- [在线演示](https://zyy792285044-afk.github.io/resume-analyzer/)

## 📄 License

MIT License
