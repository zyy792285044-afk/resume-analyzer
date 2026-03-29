# 如何使用GitHub Pages部署简历分析网页

## 步骤1：创建GitHub仓库

1. 登录 https://github.com
2. 点击右上角 "+" → "New repository"
3. 仓库名称：`resume-analyzer`（或任意名称）
4. 选择 "Public"
5. 点击 "Create repository"

## 步骤2：上传HTML文件

### 方式1：网页上传（最简单）

1. 在仓库页面点击 "Add file" → "Upload files"
2. 将 `assets/resume-chat.html` 拖拽上传
3. 重命名为 `index.html`
4. 点击 "Commit changes"

### 方式2：命令行上传

```bash
cd /workspace/projects/assets

# 复制文件并重命名
cp resume-chat.html index.html

# 如果你的项目有git
git add index.html
git commit -m "Add resume analyzer page"
git push
```

## 步骤3：启用GitHub Pages

1. 进入仓库 Settings
2. 左侧菜单找到 "Pages"
3. Source 选择 "Deploy from a branch"
4. Branch 选择 "main" 或 "master"
5. 点击 "Save"

## 步骤4：获取访问链接

等待1-2分钟后，访问链接：
```
https://你的用户名.github.io/resume-analyzer/
```

## 优势

- ✅ 永久免费
- ✅ 无需签名
- ✅ 全球CDN加速
- ✅ 支持自定义域名
- ✅ 链接永久有效

## 注意事项

- GitHub Pages 是公开的，任何人都可以访问
- 如果需要私有部署，可以考虑其他静态托管服务
