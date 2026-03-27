#!/usr/bin/env python3
"""测试脚本：直接调用简历分析Agent"""
import json
import sys
import os

# 设置环境变量
os.environ['COZE_WORKSPACE_PATH'] = '/workspace/projects'

sys.path.insert(0, '/workspace/projects/src')

from agents.agent import build_agent
from langchain_core.messages import HumanMessage

# 创建Agent实例
agent = build_agent()

# 准备测试数据
resume_text = """
张三，5年产品经验

工作经历：
2020-2023 某科技公司 产品经理
- 负责数据分析平台的产品设计
- 参与AI项目推进
- 协调开发和运营团队

2018-2020 某互联网公司 产品助理
- 协助产品经理完成需求文档
- 参与用户调研

项目经历：
- 数据分析平台：负责产品规划，提升用户留存
- AI推荐系统：参与需求梳理

技能：
- 产品设计
- 数据分析
- 团队协作

教育背景：
2014-2018 某大学 计算机科学 本科
""".strip()

# 构建输入
user_input = {
    "resume_text": resume_text,
    "target_role": "AI产品经理",
    "candidate_level": "中级"
}

# 创建消息
messages = [
    HumanMessage(content=json.dumps(user_input, ensure_ascii=False, indent=2))
]

# 测试invoke方法
print("=" * 80)
print("测试 invoke 方法...")
print("=" * 80)

result = agent.invoke(
    {"messages": messages},
    config={"configurable": {"thread_id": "test_session_1"}}
)

# 提取最后一条AI消息
last_message = result["messages"][-1]
print("\n=== 分析结果 ===")
print(last_message.content)

# 解析JSON
try:
    if "```json" in last_message.content:
        content = last_message.content.split("```json")[1].split("```")[0].strip()
    elif "```" in last_message.content:
        content = last_message.content.split("```")[1].split("```")[0].strip()
    else:
        content = last_message.content
    
    result_json = json.loads(content)
    print("\n=== 总分 ===")
    print(f"总分: {result_json['step3_score_result']['total_score']}/100")
    print(f"面试概率: {result_json['step3_score_result']['interview_probability']}")
    
    print("\n=== 3个致命问题 ===")
    for i, issue in enumerate(result_json['step4_fatal_issues'], 1):
        print(f"{i}. {issue['issue']}")
        print(f"   原因: {issue['reason']}")
    
    print("\n=== 测试成功! ===")
except Exception as e:
    print(f"\n解析结果失败: {e}")
    print("原始内容已输出")
