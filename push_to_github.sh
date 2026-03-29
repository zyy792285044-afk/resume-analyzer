#!/bin/bash

# GitHub推送脚本
# 使用Personal Access Token进行认证

echo "=== GitHub 推送指南 ==="
echo ""
echo "步骤1: 创建Personal Access Token"
echo "  访问: https://github.com/settings/tokens/new"
echo "  勾选: repo (所有repo相关权限)"
echo "  点击: Generate token"
echo "  复制生成的token"
echo ""
echo "步骤2: 在IDE终端执行推送命令"
echo "  cd /workspace/projects"
echo "  git push https://YOUR_TOKEN@github.com/zyy792285044-afk/resume-analyzer.git main"
echo ""
echo "注意: 将 YOUR_TOKEN 替换为您的实际token"
echo ""
