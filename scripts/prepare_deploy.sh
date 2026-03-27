#!/bin/bash
# 部署准备脚本

echo "=== 开始准备部署 ==="

# 1. 检查必要的文件
echo "检查必要文件..."
required_files=(
    ".coze"
    "src/main.py"
    "src/agents/agent.py"
    "config/agent_llm_config.json"
    "requirements.txt"
)

for file in "${required_files[@]}"; do
    if [ ! -f "$file" ] && [ ! -d "$file" ]; then
        echo "错误: 缺少文件 $file"
        exit 1
    fi
done

echo "✓ 所有必需文件存在"

# 2. 初始化 Git（如果需要）
if [ ! -d ".git" ]; then
    echo "初始化 Git..."
    git init
    git add .
    git commit -m "初始化简历分析Agent项目"
    echo "✓ Git 初始化完成"
else
    echo "✓ Git 已存在"
fi

# 3. 检查环境变量
echo ""
echo "=== 下一步操作 ==="
echo ""
echo "1. 在 GitHub 或 Gitee 创建新仓库"
echo "   GitHub: https://github.com/new"
echo "   Gitee: https://gitee.com/projects/new"
echo ""
echo "2. 添加远程仓库："
echo "   git remote add origin https://gitee.com/你的用户名/resume-analyzer.git"
echo ""
echo "3. 推送代码："
echo "   git push -u origin master"
echo ""
echo "4. 在 Coze 平台导入："
echo "   https://www.coze.cn → 创建项目 → 从 Git 导入"
echo ""
echo "5. 配置环境变量："
echo "   COZE_WORKLOAD_IDENTITY_API_KEY=你的密钥"
echo "   COZE_INTEGRATION_MODEL_BASE_URL=https://api.coze.cn"
echo ""
echo "6. 点击构建和部署"
echo ""
echo "完成！"
