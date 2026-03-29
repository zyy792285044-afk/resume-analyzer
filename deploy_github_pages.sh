#!/bin/bash

# 一键部署到GitHub Pages
# 使用方法：bash deploy_github_pages.sh

set -e

echo "================================================"
echo "🚀 简历分析网页 - 一键部署到GitHub Pages"
echo "================================================"
echo ""

# 检查git是否安装
if ! command -v git &> /dev/null; then
    echo "❌ 错误：未检测到git"
    echo "   请先安装git后再运行此脚本"
    exit 1
fi

# 获取用户输入
read -p "请输入您的GitHub用户名: " GITHUB_USER
read -p "请输入仓库名称（默认: resume-analyzer）: " REPO_NAME
REPO_NAME=${REPO_NAME:-resume-analyzer}

echo ""
echo "📝 部署配置："
echo "   GitHub用户: $GITHUB_USER"
echo "   仓库名称: $REPO_NAME"
echo "   访问地址: https://$GITHUB_USER.github.io/$REPO_NAME/"
echo ""

read -p "确认部署？(y/n): " CONFIRM
if [ "$CONFIRM" != "y" ]; then
    echo "已取消部署"
    exit 0
fi

echo ""
echo "📦 正在准备部署..."

# 初始化git（如果需要）
if [ ! -d ".git" ]; then
    echo "初始化Git仓库..."
    git init
    git config user.email "resume-analyzer@example.com"
    git config user.name "Resume Analyzer Bot"
fi

# 确保docs目录存在
if [ ! -d "docs" ]; then
    echo "❌ 错误：docs目录不存在"
    exit 1
fi

# 创建README
cat > docs/README.md << 'EOF'
# 简历战斗力分析

## 使用方法

1. 打开网页链接
2. 粘贴您的简历内容
3. 点击发送，等待AI分析
4. 查看专业的战斗力评估报告

## 功能特点

- 📊 战斗力评分（0-100分）
- 🎯 四维能力拆解
- ⚠️ 三大致命问题诊断
- ✨ 改前VS改后优化建议
- 🚀 行动优先级建议

## 技术支持

由Coze AI提供支持
EOF

# 添加文件
echo "添加文件到Git..."
git add docs/
git add .gitignore 2>/dev/null || true

# 提交
if git diff --staged --quiet; then
    echo "没有需要提交的更改"
else
    echo "提交更改..."
    git commit -m "feat: 部署简历分析网页到GitHub Pages"
fi

# 添加远程仓库
if ! git remote | grep -q "origin"; then
    echo ""
    echo "⚠️  未检测到远程仓库，请按以下步骤操作："
    echo ""
    echo "1. 访问 https://github.com/new 创建新仓库"
    echo "   仓库名称: $REPO_NAME"
    echo "   设置为: Public（公开）"
    echo "   不要勾选 'Add a README file'"
    echo ""
    echo "2. 创建后，执行以下命令："
    echo ""
    echo "   git remote add origin https://github.com/$GITHUB_USER/$REPO_NAME.git"
    echo "   git branch -M main"
    echo "   git push -u origin main"
    echo ""
    echo "3. 启用GitHub Pages："
    echo "   - 进入仓库 Settings → Pages"
    echo "   - Source: Deploy from a branch"
    echo "   - Branch: main"
    echo "   - Folder: /docs"
    echo "   - 点击 Save"
    echo ""
    echo "4. 等待1-2分钟后访问："
    echo "   https://$GITHUB_USER.github.io/$REPO_NAME/"
    echo ""
else
    echo "推送代码到GitHub..."
    git branch -M main
    git push -u origin main --force
fi

echo ""
echo "✅ 部署准备完成！"
echo ""
echo "📱 访问地址："
echo "   https://$GITHUB_USER.github.io/$REPO_NAME/"
echo ""
echo "💡 提示："
echo "   - 首次访问可能需要等待1-2分钟"
echo "   - 该链接永久有效，可直接分享给用户"
echo "   - 可在小红书/公众号文章中嵌入此链接"
echo ""
