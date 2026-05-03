---
rating: ⭐⭐⭐
title: srt-title-generator
url: https://skills.sh/crazynomad/skills/srt-title-generator
---

# srt-title-generator

skills/crazynomad/skills/srt-title-generator
srt-title-generator
Installation
$ npx skills add https://github.com/crazynomad/skills --skill srt-title-generator
SKILL.md
SRT Title Generator

Generate engaging, viral-potential video titles from SRT subtitle files.

Description

A skill that analyzes SRT subtitle/transcript files and generates compelling video titles optimized for YouTube, Xiaohongshu (小红书), and other platforms. Uses AI to identify key hooks, emotional triggers, and viral elements from the content.

When to Use

Use this skill when users:

Provide an SRT file and want to generate video titles
Mention "生成标题", "创建标题", "视频标题", "title from transcript"
Want to create YouTube/小红书/Bilibili titles from transcripts
Need multiple title variations for A/B testing
Want platform-specific title optimization
Features
Multi-Platform Support: YouTube, 小红书, Bilibili, 抖音 optimized titles
AI-Powered Analysis: Deep content analysis for hook identification
Viral Optimization: Emotional triggers, power words, curiosity gaps
Character Limits: Respects platform-specific length requirements
Bilingual: Chinese and English title generation
Multiple Variations: Generate 3-5 title options per request
Usage
Basic Workflow
Read the SRT file to get the transcript content
Apply the analysis prompt to identify key elements
Generate titles based on platform requirements
Platform Specifications
Platform	Max Length	Style
YouTube	60 chars	Hook + Keywords, 数字/问句/大胆声明
小红书	20 chars	简短爆点 + emoji
Bilibili	80 chars	详细 + B站风格
抖音	55 chars	悬念 + 口语化
Title Generation Prompt

When generating titles, use this analysis framework:

<scratchpad>
1. 主题识别: 从字幕中提取核心主题和关键点
2. 钩子发现: 找出最吸引人的角度或故事
3. 点击欲望: 什么会让观众想要点击
4. 草拟标题: 列出 3-5 个候选标题
5. 最优选择: 根据以下标准选出最佳:
   - 吸引眼球、制造好奇
   - 简洁 (YouTube ≤60字符)
   - 包含相关关键词
   - 准确反映内容
   - 使用情绪触发词
   - 避免标题党
</scratchpad>

Title Formulas (标题公式)
Hook Patterns (钩子模式)
数字法: "3个方法让你..."、"99%的人不知道的..."
问句法: "为什么...？"、"如何...？"
反差法: "我曾以为...直到..."
时效法: "2024最新..."、"刚刚发布..."
悬念法: "结果让我震惊..."、"最后一个太绝了"
共情法: "打工人必看"、"学生党福音"
权威法: "专家揭秘"、"官方确认"
Power Words (力量词汇)

中文:

紧迫: 必看、速看、刚刚、最新、限时
好奇: 真相、揭秘、原来、竟然、居然
价值: 干货、攻略、避坑、省钱、效率
情绪: 炸裂、绝了、太强了、神级、王炸

English:

Urgency: NOW, FINALLY, BREAKING, NEW
Curiosity: SECRET, TRUTH, REVEALED, HIDDEN
Value: FREE, EASY, ULTIMATE, COMPLETE
Emotion: INSANE, MIND-BLOWING, GAME-CHANGER
Output Format

Generate output in this structure:

## 分析过程

### 核心主题
[从字幕提取的1-2句主题总结]

### 关键钩子
- 钩子1: [描述]
- 钩子2: [描述]

### 目标受众
[谁会对这个内容感兴趣]

---

## 推荐标题

### YouTube (≤60字符)
1. **首选**: [标题]
2. **备选**: [标题]
3. **备选**: [标题]

### 小红书 (≤20字符)
1. [标题 + emoji]
2. [标题 + emoji]

### Bilibili (≤80字符)
1. [标题]
2. [标题]

---

## 标题解析
[解释为什么首选标题最有效]

Example
Input SRT Content (excerpt):
本期节目我们将进行一个Vibe Coding的极限挑战
你将看到我们如何用两句大白话就让Claude徒手写出一个下载播客的Skills

Generated Titles:

YouTube:

首选: 两句话让AI写出完整程序！Vibe Coding极限挑战
备选: 不会编程也能开发？我用Claude徒手造了个下载器
备选: AI编程有多强？2分钟写完专业程序员3天的活

小红书:

两句话让AI写程序🤯
不会代码也能开发✨

Bilibili:

【实测】只用大白话就能让Claude写出完整程序？Vibe Coding极限挑战全记录
零基础编程时代来了！手把手教你用AI造自己的工具
Claude Integration

When user provides an SRT file for title generation:

Read the SRT file:

cat "path/to/file.srt"


Extract text content (remove timestamps):

Strip SRT formatting (numbers, timestamps)
Concatenate dialogue/narration text

Analyze and generate using the prompt framework above

Present titles in the structured format

Tips for Best Results
Provide context: Tell Claude the target platform
Specify tone: 专业/轻松/搞笑/悬疑
Include keywords: 如果有特定SEO关键词
Mention competitors: 参考哪些成功标题
Limitations
Title quality depends on transcript content richness
Cultural/platform-specific nuances may need human review
SEO keyword research should supplement AI suggestions
A/B testing recommended for final selection
Version History

v1.0 (Current)

Initial release
Multi-platform title generation
Chinese and English support
Analysis framework and power words library
Weekly Installs
22
Repository
crazynomad/skills
GitHub Stars
15
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass