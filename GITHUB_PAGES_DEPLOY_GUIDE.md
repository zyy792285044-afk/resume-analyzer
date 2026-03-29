# 🚀 GitHub Pages 部署指南

## 📋 准备工作

确保您有：
- ✅ GitHub账号（没有的话去 https://github.com 注册）
- ✅ Git已安装（大多数电脑已自带）

---

## 🎯 方式一：手动部署（推荐新手）

### 第一步：创建GitHub仓库

1. **打开GitHub**
   ```
   https://github.com
   ```

2. **登录您的账号**

3. **点击右上角「+」→「New repository」**

4. **填写仓库信息**
   - Repository name: `resume-analyzer`
   - Description: `简历战斗力分析工具`
   - 选择 **Public**（公开）
   - ❌ **不要勾选** "Add a README file"
   - ❌ **不要勾选** "Add .gitignore"
   - 点击「Create repository」

---

### 第二步：在IDE中推送代码

在Coze Coding IDE的终端中执行：

```bash
# 1. 进入项目目录
cd /workspace/projects

# 2. 初始化Git（如果还没有）
git init

# 3. 配置Git用户信息
git config user.email "your-email@example.com"
git config user.name "Your Name"

# 4. 添加文件
git add docs/

# 5. 提交
git commit -m "feat: 初始化简历分析网页"

# 6. 添加远程仓库（替换成您的GitHub用户名）
git remote add origin https://github.com/您的用户名/resume-analyzer.git

# 7. 推送代码
git branch -M main
git push -u origin main
```

---

### 第三步：启用GitHub Pages

1. **进入仓库设置**
   - 打开您的仓库页面
   - 点击「Settings」标签

2. **找到Pages设置**
   - 左侧菜单找到「Pages」
   - 点击进入

3. **配置部署源**
   - Source: 选择「Deploy from a branch」
   - Branch: 选择「main」
   - Folder: 选择「/docs」
   - 点击「Save」

4. **等待部署**
   - 页面会显示 "Your site is ready to be published"
   - 等待1-2分钟
   - 刷新页面，会显示绿色提示和访问链接

---

### 第四步：访问您的网页

**访问地址：**
```
https://您的用户名.github.io/resume-analyzer/
```

**示例：**
```
如果您的用户名是 zhangsan
访问地址就是：https://zhangsan.github.io/resume-analyzer/
```

---

## 🎯 方式二：使用部署脚本（快速）

### 执行脚本

在IDE终端中运行：

```bash
cd /workspace/projects
bash deploy_github_pages.sh
```

按照提示输入：
- GitHub用户名
- 仓库名称（默认：resume-analyzer）

脚本会自动完成：
- ✅ 初始化Git
- ✅ 创建提交
- ✅ 提示后续步骤

---

## 📱 部署成功后

### 分享到小红书

**标题：**
```
🔥 免费AI简历分析工具，5分钟找出你的简历致命问题！
```

**内容：**
```
姐妹们！发现一个超实用的简历分析工具！

只需3步：
1️⃣ 打开链接：https://您的用户名.github.io/resume-analyzer/
2️⃣ 粘贴简历内容
3️⃣ 获得专业分析

✨ 包含：
• 战斗力评分（0-100分）
• 四维能力拆解
• 三大致命问题诊断
• 改前VS改后优化建议

完全免费！亲测好用！
#简历 #求职 #面试技巧 #AI工具
```

---

### 分享到公众号

**方式1：菜单栏添加**
```
公众号后台 → 自定义菜单 → 新建菜单
菜单名称：简历分析
跳转链接：https://您的用户名.github.io/resume-analyzer/
```

**方式2：文章内嵌**
```
直接在文章中插入链接
用户点击即可使用
```

---

## ⚠️ 常见问题

### Q1: 推送代码失败，提示"fatal: 'origin' already exists"

**解决方案：**
```bash
git remote remove origin
git remote add origin https://github.com/您的用户名/resume-analyzer.git
git push -u origin main
```

---

### Q2: GitHub Pages显示404

**可能原因：**
- 文件夹选择错误（应该选择 `/docs`）
- 还在部署中（等待1-2分钟）
- 文件名错误（应该是 `index.html`）

**解决方案：**
- 检查 Settings → Pages 配置
- 确保 Branch 是 `main`，Folder 是 `/docs`
- 等待几分钟再访问

---

### Q3: 需要更新网页内容

**步骤：**
```bash
# 修改 docs/index.html 后
git add docs/
git commit -m "update: 更新网页内容"
git push

# GitHub Pages会自动重新部署
# 等待1-2分钟后刷新页面
```

---

### Q4: 网页加载慢

**原因：** GitHub Pages在国外服务器

**解决方案：**
- 使用国内CDN加速（如jsdelivr）
- 或部署到Gitee Pages（国内访问更快）

---

## 🎯 方式三：部署到Gitee Pages（国内更快）

### 步骤：

1. **创建Gitee账号**
   ```
   https://gitee.com
   ```

2. **创建仓库**
   - 点击右上角「+」→「新建仓库」
   - 仓库名称：`resume-analyzer`
   - 设置为公开

3. **推送代码**
   ```bash
   git remote add gitee https://gitee.com/您的用户名/resume-analyzer.git
   git push gitee main
   ```

4. **启用Gitee Pages**
   - 进入仓库「服务」→「Gitee Pages」
   - 选择分支：main
   - 选择目录：/docs
   - 点击「启动」

5. **访问地址**
   ```
   https://您的用户名.gitee.io/resume-analyzer/
   ```

---

## ✅ 部署检查清单

- [ ] 已创建GitHub/Gitee仓库
- [ ] 已推送代码到仓库
- [ ] 已启用Pages服务
- [ ] 已选择正确的分支和文件夹
- [ ] 访问链接可以正常打开
- [ ] 测试简历分析功能正常

---

## 🎉 部署成功后

您将获得：
- ✅ 永久有效的访问链接
- ✅ 免费托管服务
- ✅ 支持HTTPS安全访问
- ✅ 全球CDN加速
- ✅ 可直接分享给用户

---

## 💡 优势对比

| 平台 | 访问速度 | 稳定性 | 费用 | 推荐度 |
|------|---------|--------|------|--------|
| **GitHub Pages** | 国内较慢 | ⭐⭐⭐⭐⭐ | 免费 | ⭐⭐⭐⭐ |
| **Gitee Pages** | 国内快 | ⭐⭐⭐⭐ | 免费 | ⭐⭐⭐⭐⭐ |
| **Vercel** | 全球快 | ⭐⭐⭐⭐⭐ | 免费 | ⭐⭐⭐⭐ |

---

## 📞 需要帮助？

如果遇到问题：
1. 检查网络连接
2. 确认仓库设置正确
3. 查看GitHub Pages部署日志
4. 或联系我获取帮助

**现在就开始部署吧！** 🚀
