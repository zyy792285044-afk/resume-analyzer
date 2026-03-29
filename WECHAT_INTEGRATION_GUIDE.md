# 微信公众号/小程序集成指南

## 📱 方案概述

本指南帮助您将简历分析Agent集成到微信公众号或小程序中，让用户无需登录即可使用。

---

## 🎯 方案一：微信公众号（推荐，最简单）

### 步骤1：部署网页文件

#### 方法A：使用Coze对象存储（推荐）

1. **准备HTML文件**
   - 已创建文件：`assets/resume-analyzer.html`
   - 位置：项目根目录下的 assets 文件夹

2. **上传到对象存储**
   
   **方式1：通过Coze平台上传**
   - 登录 Coze 平台
   - 进入【对象存储】功能
   - 创建存储桶（如果还没有）
   - 上传 `assets/resume-analyzer.html` 文件
   - 设置为公开访问
   - 复制文件访问URL

   **方式2：使用代码上传**
   ```bash
   cd /workspace/projects
   
   # 上传文件到对象存储
   python3 << 'EOF'
   from coze_coding_dev_sdk import StorageClient
   from coze_coding_utils.runtime_ctx.context import new_context
   
   ctx = new_context(method="upload_html")
   client = StorageClient(ctx=ctx)
   
   # 读取HTML文件
   with open('assets/resume-analyzer.html', 'r', encoding='utf-8') as f:
       html_content = f.read()
   
   # 上传到对象存储
   url = client.upload_object(
       key="resume-analyzer.html",
       data=html_content.encode('utf-8'),
       content_type="text/html"
   )
   
   print(f"上传成功！访问地址：{url}")
   EOF
   ```

#### 方法B：使用GitHub Pages（免费）

1. **创建GitHub仓库**
   - 登录 https://github.com
   - 创建新仓库（例如：`resume-analyzer-web`）

2. **上传HTML文件**
   ```bash
   # 在项目根目录执行
   cd /workspace/projects/assets
   
   # 初始化Git仓库（如果还没有）
   git init
   git add resume-analyzer.html
   git commit -m "Add resume analyzer web page"
   
   # 推送到GitHub
   git remote add origin https://github.com/你的用户名/resume-analyzer-web.git
   git push -u origin main
   ```

3. **启用GitHub Pages**
   - 进入仓库 Settings → Pages
   - Source 选择 `main` 分支
   - 保存后获得访问链接：
     ```
     https://你的用户名.github.io/resume-analyzer-web/resume-analyzer.html
     ```

---

### 步骤2：配置微信公众号

#### 方式1：添加到公众号菜单（推荐）

1. **登录微信公众号后台**
   - 网址：https://mp.weixin.qq.com

2. **设置自定义菜单**
   - 左侧菜单：功能 → 自定义菜单
   - 点击"添加菜单"
   - 菜单名称：`简历分析`
   - 菜单内容：选择"跳转网页"
   - 网页地址：填入步骤1获取的HTML文件URL
   - 点击"保存并发布"

3. **用户使用流程**
   - 用户打开公众号
   - 点击底部菜单"简历分析"
   - 进入网页，粘贴简历内容
   - 获得分析报告

#### 方式2：文章中插入链接

1. **编辑图文消息**
   - 在文章中插入超链接
   - 链接地址：HTML文件URL
   - 文字提示：点击这里免费分析简历

2. **或使用小程序卡片**
   - 如果有小程序，可以使用web-view组件
   - 跳转到HTML页面

---

## 🎯 方案二：微信小程序

### 步骤1：创建小程序项目

1. **注册小程序**
   - 登录 https://mp.weixin.qq.com
   - 注册小程序账号

2. **下载开发工具**
   - 微信开发者工具下载地址：
     https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html

### 步骤2：开发小程序页面

创建以下文件：

**pages/index/index.wxml**
```xml
<view class="container">
  <view class="header">
    <text class="title">简历战斗力分析</text>
    <text class="subtitle">专业评估 · 精准诊断</text>
  </view>
  
  <view class="form">
    <textarea 
      class="resume-input"
      placeholder="请粘贴简历内容..."
      bindinput="onResumeInput"
    />
    
    <radio-group class="format-group" bindchange="onFormatChange">
      <radio value="text" checked>文本格式</radio>
      <radio value="pdf">PDF格式</radio>
      <radio value="word">Word格式</radio>
    </radio-group>
    
    <button class="submit-btn" bindtap="analyzeResume" loading="{{loading}}">
      开始分析
    </button>
  </view>
  
  <view class="result" wx:if="{{result}}">
    <text class="result-title">分析报告</text>
    <text class="result-content">{{result}}</text>
  </view>
</view>
```

**pages/index/index.js**
```javascript
Page({
  data: {
    resumeText: '',
    format: 'text',
    result: '',
    loading: false
  },
  
  onResumeInput(e) {
    this.setData({ resumeText: e.detail.value })
  },
  
  onFormatChange(e) {
    this.setData({ format: e.detail.value })
  },
  
  async analyzeResume() {
    if (!this.data.resumeText) {
      wx.showToast({ title: '请输入简历内容', icon: 'none' })
      return
    }
    
    this.setData({ loading: true })
    
    try {
      // 调用您的API
      const res = await wx.request({
        url: 'https://2m6zxztjxq.coze.site/stream_run',
        method: 'POST',
        data: {
          messages: [{
            role: 'user',
            content: `请分析我的简历。\n\n${this.data.resumeText}${this.data.format !== 'text' ? '\n\n请输出' + this.data.format.toUpperCase() + '格式的报告。' : ''}`
          }]
        }
      })
      
      // 处理响应并显示结果
      this.setData({ result: res.data })
      
    } catch (error) {
      wx.showToast({ title: '分析失败', icon: 'none' })
    } finally {
      this.setData({ loading: false })
    }
  }
})
```

### 步骤3：配置域名

1. **登录小程序后台**
   - 开发 → 开发管理 → 开发设置 → 服务器域名

2. **添加合法域名**
   - request合法域名：`https://2m6zxztjxq.coze.site`

3. **提交审核发布**
   - 开发完成后提交审核
   - 审核通过后发布

---

## 🚀 快速开始（推荐路径）

### 最简单的方式（5分钟上线）

1. **上传HTML文件**
   ```bash
   cd /workspace/projects/assets
   # 将 resume-analyzer.html 上传到任意对象存储或静态托管服务
   ```

2. **获取访问链接**
   - 例如：`https://your-domain.com/resume-analyzer.html`

3. **配置到微信公众号**
   - 公众号后台 → 自定义菜单 → 添加菜单
   - 菜单名称：简历分析
   - 跳转网页：填入上面的链接

4. **完成！**
   - 用户点击菜单即可使用
   - 无需登录
   - 手机端完美适配

---

## 💡 重要提示

### 1. API地址配置

在HTML文件中，已配置API地址：
```javascript
const API_URL = 'https://2m6zxztjxq.coze.site/stream_run';
```

如果您的API地址发生变化，需要修改这个配置。

### 2. 跨域问题

如果遇到跨域问题，有几种解决方案：

**方案A：在Coze平台配置CORS**
- 在API服务的响应头中添加：
  ```
  Access-Control-Allow-Origin: *
  Access-Control-Allow-Methods: GET, POST, OPTIONS
  Access-Control-Allow-Headers: Content-Type
  ```

**方案B：使用代理**
- 通过您的服务器代理API请求
- 或使用Nginx反向代理

**方案C：使用微信小程序**
- 小程序的request请求不受跨域限制
- 但需要配置合法域名

### 3. 安全性考虑

- API接口建议添加访问频率限制
- 可以考虑添加简单的验证机制
- 监控API调用量，防止滥用

---

## 📊 方案对比

| 方案 | 难度 | 优势 | 劣势 |
|------|------|------|------|
| **公众号菜单+网页** | ⭐ 简单 | 快速上线，无需开发 | 需要HTML托管 |
| **公众号文章链接** | ⭐ 简单 | 灵活，可随时发布 | 用户需要点击链接 |
| **微信小程序** | ⭐⭐⭐ 中等 | 体验好，功能强 | 需要开发、审核 |

---

## ✅ 下一步操作

1. 选择一个部署方案（推荐：公众号菜单+网页）
2. 上传HTML文件到对象存储
3. 配置微信公众号菜单
4. 测试完整流程
5. 收集用户反馈并优化

---

## 🆘 常见问题

**Q: HTML文件放到哪里？**
A: 任何支持静态文件托管的地方都可以，推荐Coze对象存储或GitHub Pages。

**Q: 用户需要登录吗？**
A: 不需要，直接打开网页就能使用。

**Q: 手机端体验如何？**
A: 已做移动端适配，在微信中打开体验良好。

**Q: 如何查看使用数据？**
A: 可以在HTML中集成统计代码（如百度统计、友盟等）。

**Q: API地址变了怎么办？**
A: 修改HTML文件中的API_URL配置，重新上传即可。
