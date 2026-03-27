#!/usr/bin/env python3
"""测试脚本：直接调用简历分析Agent"""
import json
import sys
sys.path.insert(0, '/workspace/projects/src')

from agents.agent import ResumeAnalysisAgent

# 创建Agent实例
agent = ResumeAnalysisAgent()

# 准备测试数据
test_input = {
    "resume_text": """
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
    """.strip(),
    "target_role": "AI产品经理",
    "candidate_level": "中级"
}

# 测试invoke方法
print("测试 invoke 方法...")
result = agent.invoke(test_input)
print("\n=== 结果 ===")
print(result.content)

# 测试stream方法
print("\n\n测试 stream 方法...")
full_content = ""
for chunk in agent.stream(test_input):
    if chunk.content:
        print(chunk.content, end="", flush=True)
        full_content += chunk.content

print("\n\n=== 流式输出完成 ===")
