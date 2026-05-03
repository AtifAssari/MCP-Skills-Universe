---
rating: ⭐⭐
title: serper-scholar
url: https://skills.sh/fanzhidongyzby/openclaw-serper/serper-scholar
---

# serper-scholar

skills/fanzhidongyzby/openclaw-serper/serper-scholar
serper-scholar
Installation
$ npx skills add https://github.com/fanzhidongyzby/openclaw-serper --skill serper-scholar
SKILL.md
Google Scholar Search Tool

基于 Google Scholar API 的学术文献搜索工具，提供学术论文、研究报告、技术文献的专业搜索能力。

When to Activate

当用户提到以下内容时自动激活：

学术搜索关键词
"论文"、"学术"、"文献"、"研究"
"搜索论文"、"查找文献"、"学术研究"
"谷歌学术"、"Scholar"
特定场景
需要查找学术论文或研究报告
需要了解某领域的学术进展
需要查找特定作者的作品
需要获取引用信息和发表刊物
需要研究技术领域的理论依据
示例问题
"帮我搜索关于机器学习的论文"
"查找一下深度学习在 NLP 中的应用"
"研究一下 Transformer 架构的学术论文"
"找一些关于大模型训练方法的文献"
"搜索一下 Attention mechanism 的相关论文"
Tools
serper_scholar

用途： 执行学术文献搜索，返回论文详细信息

参数：

query (必选，string)：搜索关键词
num (可选，number)：返回结果数量，默认 10，最大 20
gl (可选，string)：国家代码，默认 cn
推荐值： cn（中国）、us（美国）、uk（英国）
hl (可选，string)：语言代码，默认 zh-CN
推荐值： zh-CN（简体中文）、en（英文）

返回字段：

title：论文标题
url：论文链接
snippet：摘要
type：文献类型（PDF、HTML 等）
year：发表年份
authors：作者列表
publication：发表刊物/会议
citationCount：引用次数
Best Practices
1. 搜索技巧

使用专业术语和技术关键词：

示例：

✅ "Attention mechanism neural machine translation"
✅ "Transformer large language models"
✅ "Reinforcement learning robotics"
❌ "机器学习"（太宽泛，结果太多）
2. 添加领域限定

明确研究领域和方法：

示例：

✅ "BERT semantic analysis NLP"
✅ "CNN image classification computer vision"
✅ "GPT text generation natural language"
✅ "Q-learning reinforcement learning agent"
3. 时间范围搜索

关注最新研究进展：

示例：

✅ "Large language models 2024 2025"
✅ "Transformer architecture recent advances"
✅ "Diffusion models 2023 2024"
4. 作者和机构搜索

查找特定研究者或机构的工作：

示例：

✅ "Geoffrey Hinton deep learning"
✅ "Yann LeCun CNN papers"
✅ "Andrew Ng machine learning"
✅ "OpenAI research papers"
5. 论文类型筛选

关注特定类型的文献：

示例：

✅ "Survey deep learning"
✅ "Review transformer models"
✅ "Tutorial reinforcement learning"
✅ "Benchmark NLP models"
6. 结果数量选择

根据需求调整：

快速浏览： num=5（核心文献）
全面了解： num=10（主流研究）
深度调研： num=20（全面覆盖）
7. 引用信息分析

关注高引用论文和经典文献：

关注点：

引用次数：citationCount 高的论文通常是领域经典
发表年份：较新的论文代表最新进展
发表刊物：顶级会议（NeurIPS、ICML、ACL）质量高
Example Scenarios
场景 1：技术调研

用户提问： "研究一下 Transformer 架构的论文"

AI 行为：

// 搜索核心论文
serper_scholar({
  query: "Transformer architecture attention is all you need",
  num: 5
})

// 搜索后续研究
serper_scholar({
  query: "BERT transformer NLP 2018 2019",
  num: 8
})


回复示例：

核心论文：

1. **Attention Is All You Need** (2017)
   - 作者：Vaswani et al.
   - 引用：100,000+
   - 📄 [PDF]
   
后续研究：

2. **BERT: Pre-training of Deep Bidirectional Transformers** (2019)
   - 作者：Devlin et al.
   - 引用：80,000+
   - 发表：NAACL 2019
   
3. **Improving Language Understanding with Generative Pre-Training** (2018)
   - 作者：Radford et al. (OpenAI)
   - 引用：50,000+

场景 2：领域综述

用户提问： "找一些关于强化学习的综述论文"

AI 行为：

serper_scholar({
  query: "Survey review reinforcement learning",
  num: 8
})


回复示例：

强化学习综述论文：

1. **Reinforcement Learning: A Survey** (2021)
   - 引用：5,000+
   - 类型：综述
   
2. **Deep Reinforcement Learning: An Overview** (2020)
   - 引用：8,000+
   - 类型：综述
   
3. **Recent Advances in Deep Reinforcement Learning** (2022)
   - 引用：2,000+
   - 类型：综述

场景 3：作者研究

用户提问： "查找 Geoffrey Hinton 的深度学习论文"

AI 行为：

serper_scholar({
  query: "Geoffrey Hinton deep learning backpropagation",
  num: 10
})


回复示例：

Geoffrey Hinton 的经典论文：

1. **Deep Learning** (2015)
   - 合作：LeCun, Bengio
   - 发表：Nature
   - 引用：50,000+
   
2. **Backpropagation Applied to Handwritten Zip Code Recognition** (1989)
   - 引用：10,000+
   
3. **Reducing the Dimensionality of Data with Neural Networks** (2006)
   - 引用：30,000+

场景 4：最新进展

用户提问： "2024-2025 年大模型有什么新进展"

AI 行为：

serper_scholar({
  query: "Large language models 2024 2025 advances",
  num: 10
})


回复示例：

2024-2025 大模型研究进展：

1. **Scaling Laws for Neural Language Models** (2024)
   - 持续探索模型规模与性能关系
   
2. **Instruction Tuning for Large Language Models** (2024)
   - 指令微调方法改进
   
3. **Chain-of-Thought Prompting** (2024)
   - 推理链提示技术

场景 5：跨学科搜索

用户提问： "搜索机器学习在医疗诊断中的应用论文"

AI 行为：

serper_scholar({
  query: "Machine learning medical diagnosis healthcare",
  num: 8
})


回复示例：

医疗诊断中的机器学习：

1. **Deep Learning for Medical Image Analysis** (2021)
   - 引用：8,000+
   - 应用：影像诊断
   
2. **Machine Learning in Clinical Diagnosis** (2022)
   - 引用：3,000+
   - 应用：辅助诊断
   
3. **AI in Healthcare: A Survey** (2023)
   - 引用：2,000+
   - 类型：综述

Limitations
搜索结果来源： Google Scholar，可能受地区影响
访问限制： 某些论文需要订阅或付费访问
结果数量： 最多 20 条
更新延迟： 最新论文可能需要一段时间才会被收录
语言偏好： 英文论文数量远多于中文
Configuration
环境变量配置

编辑 ~/.openclaw/gateway.env：

SERPER_API_KEY=your-api-key-here

获取 API Key

访问 https://serper.dev/ 注册并获取 API Key。

免费额度：每月 2,500 次调用（Web 和 Scholar 共享）。

Related Tools
serper_search： 普通网页搜索
web_fetch： 获取单个网页的详细内容
Tips
混合使用： 先用 serper_search 了解概念，再用 serper_scholar 深入研究
引用优先： 优先阅读高引用论文（通常是领域经典）
关注年份： 平衡经典文献和最新研究
追踪作者： 找到重要作者后，搜索其全部作品
PDF 访问： 尝试访问论文页面，寻找免费版本
Version History
v1.0 (2026-02-06)：初始版本，基础学术搜索功能
支持 Google Scholar API
提供论文详细信息（作者、年份、引用等）
集成 OpenClaw Skill 系统

💡 提示： 学术搜索时，尽量使用英文关键词，英文论文数量和质量通常更高。

Weekly Installs
240
Repository
fanzhidongyzby/…w-serper
GitHub Stars
4
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn