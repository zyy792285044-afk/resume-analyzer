#!/bin/bash

# 一键部署脚本 - 将简历分析网页发布到GitHub Pages
# 使用前提：已安装git并配置好GitHub账号

set -e

echo "================================================"
echo "🚀 简历分析网页 - 一键部署到GitHub Pages"
echo "================================================"
echo ""

# 检查git是否安装
if ! command -v git &> /dev/null; then
    echo "❌ 错误：未检测到git，请先安装git"
    echo "   macOS: brew install git"
    echo "   Windows: https://git-scm.com/download/win"
    exit 1
fi

# 配置信息
read -p "请输入您的GitHub用户名: " GITHUB_USER
read -p "请输入仓库名称（默认: resume-analyzer）: " REPO_NAME
REPO_NAME=${REPO_NAME:-resume-analyzer}

echo ""
echo "📝 部署配置："
echo "   GitHub用户: $GITHUB_USER"
echo "   仓库名称: $REPO_NAME"
echo "   访问地址: https://$GITHUB_USER.github.io/$REPO_NAME/resume-chat.html"
echo ""

read -p "确认部署？(y/n): " CONFIRM
if [ "$CONFIRM" != "y" ]; then
    echo "已取消部署"
    exit 0
fi

# 创建临时目录
TEMP_DIR=$(mktemp -d)
cd "$TEMP_DIR"

echo ""
echo "📦 正在初始化仓库..."

# 初始化git仓库
git init
git config user.email "noreply@example.com"
git config user.name "Resume Analyzer"

# 复制HTML文件
cp "$WORKSPACE_PATH/assets/resume-chat.html" .
cp "$WORKSPACE_PATH/assets/resume-chat.html" index.html

# 创建README
cat > README.md << 'EOF'
# 简历战斗力分析器

## 使用方法

1. 打开网页链接
2. 粘贴您的简历内容
3. 点击发送，等待AI分析
4. 回复"需要PDF"获取下载链接

## 功能特点

- 📊 战斗力评分（0-100分）
- 🎯 四维能力拆解
- ⚠️ 三大致命问题诊断
- ✨ 改前VS改后优化建议
- 🚀 行动优先级建议
- 📄 PDF报告下载

## 技术支持

由Coze AI提供支持
EOF

# 提交代码
git add .
git commit -m "feat: 初始化简历分析网页"

# 创建GitHub仓库（需要gh命令行工具）
if command -v gh &> /dev/null; then
    echo "🔧 正在创建GitHub仓库..."
    gh repo create "$REPO_NAME" --public --source=. --remote=origin
    git push -u origin main
else
    echo ""
    echo "⚠️  未检测到gh命令行工具，请手动创建仓库："
    echo ""
    echo "1. 访问 https://github.com/new"
    echo "2. 创建名为 '$REPO_NAME' 的公开仓库"
    echo "3. 不要勾选 'Add a README file'"
    echo "4. 创建后执行以下命令："
    echo ""
    echo "   git remote add origin https://github.com/$GITHUB_USER/$REPO_NAME.git"
    echo "   git branch -M main"
    echo "   git push -u origin main"
    echo ""
    echo "5. 进入仓库 Settings → Pages"
    echo "   Source: Deploy from a branch"
    echo "   Branch: main / (root)"
    echo "   点击 Save"
    echo ""
    echo "6. 等待1-2分钟后访问："
    echo "   https://$GITHUB_USER.github.io/$REPO_NAME/resume-chat.html"
fi

# 清理临时目录
echo ""
echo "✅ 部署完成！"
echo ""
echo "📱 访问地址："
echo "   https://$GITHUB_USER.github.io/$REPO_NAME/resume-chat.html"
echo ""
echo "💡 提示："
echo "   - 首次访问可能需要等待1-2分钟"
echo "   - 该链接永久有效，可直接分享给用户"
echo "   - 可在小红书/公众号文章中嵌入此链接"
echo ""
