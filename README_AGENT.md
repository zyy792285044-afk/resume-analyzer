# 简历战斗力分析Agent

## 功能介绍

这是一个专业的简历分析Agent，能够帮助求职者快速识别简历的致命问题，并给出具体可执行的改进建议。

**核心能力：**
- 🎯 **简历结构化分析**：将非结构化简历文本转换为标准JSON格式
- 📊 **岗位画像构建**：根据目标岗位生成标准能力模型
- ⚖️ **多维度评分**：从技能匹配、业务理解、项目质量、表达清晰度4个维度量化评估
- ⚠️ **问题诊断**：识别简历中影响面试决策的3个致命问题
- ✍️ **简历优化**：提供3组改前/改后的具体优化建议
- 📝 **完整报告**：生成结构化的求职战斗力报告

## 使用方法

### 输入格式

Agent接受JSON格式的输入：

```json
{
  "resume_text": "简历文本内容...",
  "target_role": "AI产品经理",
  "candidate_level": "中级"
}
```

**参数说明：**
- `resume_text`（必需）：简历文本内容
- `target_role`（必需）：目标岗位名称
- `candidate_level`（可选）：候选人级别，可选值：初级/中级/高级

### 输出格式

Agent返回一个完整的JSON对象，包含6个步骤的中间结果和最终报告：

```json
{
  "step1_resume_structured": {
    "basic_info": {"name": "张三", "work_experience": "5年"},
    "education": [...],
    "work_experience": [...],
    "project_experience": [...],
    "skills": [...],
    "awards": [],
    "certificates": [],
    "gaps_or_risks": [...]
  },
  "step2_job_profile": {
    "role_name": "中级AI产品经理",
    "key_skills": [...],
    "business_capability": [...],
    "expected_project_type": [...],
    "common_red_flags": [...],
    "evaluation_weights": {...}
  },
  "step3_score_result": {
    "total_score": 72,
    "skill_match": 80,
    "business_understanding": 42,
    "project_quality": 55,
    "expression_clarity": 48,
    "interview_probability": "低",
    "overall_comment": "经历不算差，但对目标岗位缺乏足够说服力。"
  },
  "step4_fatal_issues": [
    {
      "issue": "项目经历缺少结果指标",
      "reason": "招聘方无法判断你做过的事到底有没有业务价值。"
    },
    ...
  ],
  "step5_rewrite_suggestions": [
    {
      "before": "负责数据分析工作",
      "after": "负责核心业务数据分析与指标体系搭建，支持运营策略优化，推动关键转化指标提升。"
    },
    ...
  ],
  "final_report_markdown": "# 求职战斗力报告\n\n## 1. 总评\n..."
}
```

## 分析流程

Agent内部按照以下6个步骤进行分析：

1. **简历结构化**：解析简历文本，提取关键信息
2. **岗位画像解析**：根据目标岗位生成标准能力模型
3. **匹配评分**：从4个维度量化评估简历质量
4. **提炼致命问题**：识别3个最影响面试决策的问题
5. **经历改写**：提供3组具体的优化建议
6. **生成最终报告**：输出完整的求职战斗力报告

## 使用示例

### Python调用

```python
from agents.agent import ResumeAnalysisAgent

# 创建Agent实例
agent = ResumeAnalysisAgent()

# 准备输入数据
input_data = {
    "resume_text": """
张三，5年产品经验

工作经历：
2020-2023 某科技公司 产品经理
- 负责数据分析平台的产品设计
- 参与AI项目推进
    """,
    "target_role": "AI产品经理",
    "candidate_level": "中级"
}

# 调用Agent
result = agent.invoke(input_data)
print(result.content)
```

### HTTP API调用

```bash
POST /run
Content-Type: application/json

{
  "resume_text": "简历内容...",
  "target_role": "AI产品经理",
  "candidate_level": "中级"
}
```

## 特色功能

### 1. 极其严格的评分标准
- 不鼓励式表达，不灌鸡汤
- 问题要打狠，建议要具体
- 所有评价基于简历事实

### 2. 量化评估体系
- 总分：0-100分
- 4个维度评分：技能匹配、业务理解、项目质量、表达清晰度
- 面试概率判断：高/中/低

### 3. 可操作的优化建议
- 每个建议都包含"原句"和"优化后"
- 优化建议贴近目标岗位
- 突出结果、影响、指标

## 技术架构

- **模型**：doubao-seed-2-0-pro-260215（支持深度推理）
- **框架**：LangChain + Coze SDK
- **输出格式**：JSON + Markdown

## 适用场景

✅ **适合：**
- 求职者快速了解简历问题
- 简历优化参考
- 面试准备自查

❌ **不适合：**
- 完全替代人工简历修改
- 保证面试成功的承诺

## 注意事项

1. Agent的分析基于输入的简历文本，请确保内容真实完整
2. 评分标准较为严格，这是为了帮助发现真实问题
3. 优化建议仅供参考，请根据实际情况调整
4. 建议结合具体岗位要求使用，效果更佳

## 更新日志

### v1.0.0 (2026-03-27)
- ✨ 初始版本发布
- ✨ 支持6步分析流程
- ✨ 输出完整JSON报告
- ✨ 支持流式和同步两种调用方式
