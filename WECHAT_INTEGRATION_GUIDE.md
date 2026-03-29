# 微信公众号/小程序集成指南

## 📱 方案概述

本指南帮助您将简历分析Agent集成到微信公众号或小程序中，让用户无需登录即可使用。

---

## 🎯 方案一：微信公众号（推荐，最简单）

### 步骤1：访问已部署的网页

**✅ 已为您生成移动端对话式网页：**

```
https://coze-coding-project.tos.coze.site/coze_storage_7621796462938161204/resume-chat_b4abb61d.html?sign=1777348563-1ba69a8cfc-0-5b4441e50219af3fb7931a05949440b18ce8eaabdee0b938c36b45648aec903e
```

**功能特性：**
- ✅ 完美适配手机屏幕
- ✅ 对话式交互，流式输出
- ✅ 支持文本输入
- ✅ 支持PDF文件上传（显示提示）
- ✅ 自动询问是否需要PDF版本
- ✅ 一键生成PDF下载链接

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
   - 网页地址：填入上面的访问链接
   - 点击"保存并发布"

3. **用户使用流程**
   ```
   用户打开公众号
       ↓
   点击底部菜单"简历分析"
       ↓
   进入对话界面
       ↓
   粘贴简历内容
       ↓
   AI流式输出分析报告
       ↓
   AI询问是否需要PDF
       ↓
   用户回复"需要PDF"
       ↓
   AI生成PDF下载链接
   ```

#### 方式2：文章中插入链接

1. **编辑图文消息**
   - 在文章中插入超链接
   - 链接地址：访问链接
   - 文字提示：点击这里免费分析简历

2. **或使用小程序卡片**
   - 如果有小程序，可以使用web-view组件
   - 跳转到HTML页面

---

## 📱 网页界面展示

### 主要特点

**1. 对话式交互**
- 类似微信聊天界面
- 流式输出，打字机效果
- 实时显示AI回复

**2. 移动端完美适配**
- 响应式设计
- 适配各种手机屏幕
- 流畅的触摸交互

**3. 智能功能**
- 支持文本粘贴
- 支持PDF文件上传提示
- 自动询问PDF需求
- 一键生成下载链接

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

1. **复制访问链接**
   ```
   https://coze-coding-project.tos.coze.site/coze_storage_7621796462938161204/resume-chat_b4abb61d.html
   ```

2. **配置到微信公众号**
   - 公众号后台 → 自定义菜单 → 添加菜单
   - 菜单名称：简历分析
   - 跳转网页：填入上面的链接

3. **完成！**
   - 用户点击菜单即可使用
   - 无需登录
   - 手机端完美适配
   - 对话式交互

---

## 💡 使用流程示例

### 用户端操作流程

```
1. 打开微信公众号
2. 点击底部菜单"简历分析"
3. 在对话框中粘贴简历内容
4. 点击发送按钮
5. AI流式输出分析报告
6. 阅读完整报告后
7. 回复"需要PDF"或"下载报告"
8. AI生成PDF下载链接
9. 点击链接下载PDF文件
```

---

## 📊 方案对比

| 方案 | 难度 | 优势 | 劣势 |
|------|------|------|------|
| **公众号菜单+网页** | ⭐ 简单 | 快速上线，对话式交互 | 需要HTML托管 |
| **公众号文章链接** | ⭐ 简单 | 灵活，可随时发布 | 用户需要点击链接 |
| **微信小程序** | ⭐⭐⭐ 中等 | 体验好，功能强 | 需要开发、审核 |

---

## ✅ 下一步操作

1. 使用手机打开访问链接，测试完整流程
2. 配置微信公众号菜单
3. 发布文章宣传
4. 收集用户反馈并优化

---

## 🆘 常见问题

**Q: 网页链接有效期多久？**
A: 当前链接有效期30天，到期后需要重新生成。

**Q: 用户需要登录吗？**
A: 不需要，直接打开网页就能使用。

**Q: 手机端体验如何？**
A: 已做移动端适配，完美适配各种手机屏幕，对话式交互体验流畅。

**Q: 如何获取PDF报告？**
A: AI分析完成后会自动询问是否需要PDF，用户回复"需要PDF"即可获得下载链接。

**Q: PDF下载链接有效期多久？**
A: PDF下载链接有效期24小时。

**Q: 如何查看使用数据？**
A: 可以在HTML中集成统计代码（如百度统计、友盟等）。

**Q: API地址变了怎么办？**
A: 修改HTML文件中的API_URL配置，重新上传即可。

---

## 📝 技术说明

### 前端技术栈
- HTML5 + CSS3 + Vanilla JavaScript
- 响应式设计
- 流式响应处理
- Markdown格式化

### 后端API
- 基于Coze平台的智能体API
- 支持流式输出
- 自动调用PDF生成工具

### 部署方式
- 对象存储（S3）
- 静态HTML文件
- CDN加速
