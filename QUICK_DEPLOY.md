# ⚡ 5分钟部署到GitHub Pages

## 📝 只需3步

### 第1步：创建GitHub仓库（1分钟）

1. 打开 https://github.com
2. 点击右上角「+」→「New repository」
3. 填写：
   - Repository name: `resume-analyzer`
   - 选择 **Public**
   - ❌ **不要勾选**任何初始化选项
4. 点击「Create repository」

---

### 第2步：推送代码（2分钟）

在IDE终端复制粘贴以下命令：

```bash
cd /workspace/projects

git init
git config user.email "resume@example.com"
git config user.name "Resume Analyzer"
git add docs/
git commit -m "feat: 部署简历分析网页"
git remote add origin https://github.com/您的用户名/resume-analyzer.git
git branch -M main
git push -u origin main
```

**注意：** 把 `您的用户名` 替换成您的GitHub用户名

---

### 第3步：启用Pages（2分钟）

1. 打开您的仓库页面
2. 点击「Settings」
3. 左侧菜单点击「Pages」
4. 配置：
   - Source: Deploy from a branch
   - Branch: main
   - Folder: /docs
5. 点击「Save」
6. 等待1-2分钟

---

## ✅ 完成！

**访问地址：**
```
https://您的用户名.github.io/resume-analyzer/
```

**立即分享给用户！**

---

## 🎯 详细指南

如果遇到问题，请查看：
- **GITHUB_PAGES_DEPLOY_GUIDE.md** - 完整部署指南
- **deploy_github_pages.sh** - 一键部署脚本
