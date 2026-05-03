---
title: idea
url: https://skills.sh/ppx123-web/claude-config/idea
---

# idea

skills/ppx123-web/claude-config/idea
idea
Installation
$ npx skills add https://github.com/ppx123-web/claude-config --skill idea
SKILL.md
Idea - Record Thoughts and Problems
Overview

Quickly capture ideas and questions, structure them into Obsidian vault with problem analysis and tags. Focuses on problems only, not solutions.

Core Features
💡 Quick Capture: Capture fleeting thoughts and problems
📁 Auto-Archive: Organize by date into idea/ directory
🏷️ Tag Management: Auto-add relevant tags
📋 Index Update: Auto-update Ideas-Index.md
🧠 Problem-Focused: Only record problems, no solutions
When to Use

Trigger this skill when user:

Captures sudden inspiration during work/learning
Questions technical approaches or architectures
Discovers problems worth researching
Has doubts about current solutions
Example Triggers
"记录一个关于错误处理的 idea"
"我有个关于性能优化的想法"
"对当前的架构有一些疑问，帮我记录"
"发现一个值得研究的问题"
"有个想法，关于..."
Basic Usage
Simple Idea
记录想法: 为什么错误信息不能包含更多上下文？

Specify Topic
记录一个关于 LLM 的想法: 如何让错误信息更机器友好

Problem Analysis Format
记录想法:
核心问题: [问题陈述]
背景: [为什么是问题]
疑问: [待探索的点]

Workflow
Step 1: Understand Idea

Extract from user's description:

Core Problem: What's the essence?
Background: Why did this idea occur?
Value: Is it worth exploring?
Step 2: Create Note

Create file in Obsidian vault:

Path: idea/YYYY-MM-DD-[title].md
Format: Markdown template
Title: Concise description of idea topic
Step 3: Structure Content

Use standard template (see references/templates.md for full templates):

# idea: [Title]

## 核心问题

**[Problem Statement]**

[Problem description]

---

## 问题分析

### 现状
- [Point 1]
- [Point 2]

### 疑问
- [Question 1]
- [Question 2]

---

## 延伸思考

1. [Thought 1]
2. [Thought 2]
3. [Thought 3]

---

*创建时间: YYYY-MM-DD*
*标签: #idea #tag1 #tag2*

Step 4: Update Index

Add entry to idea/Ideas-Index.md:

### YYYY-MM-DD - [[idea/YYYY-MM-DD-[title]]]
**主题**: [Brief description]
**核心问题**: [Core problem]
**标签**: #tag1 #tag2

Naming Conventions
File Naming

Format: idea/YYYY-MM-DD-[slug].md

Date: Current date
Slug: Short English description, hyphen-separated
Examples:
idea/2026-01-13-LLM-Error-Messages.md
idea/2026-01-15-Cache-Strategy.md
idea/2026-01-20-API-Design.md
Tag Standards

Auto-add tags:

#idea - Universal tag for all ideas
Specific tags based on content:
#LLM
#architecture
#performance
#debugging
Best Practices
Content Principles
Problems Only: Don't include solutions
Keep Concise: Focus on core problem
Value Judgment: Verify problem is worth exploring
Traceable: Record time and tags
Quality Standards

Good idea notes should:

✅ Have clear, specific problems
✅ Include concrete analysis
✅ Raise thoughtful questions
✅ Contain problem verification
❌ NOT include specific solutions
❌ NOT over-expand details
Common Mistakes
❌ "我有个想法，应该用 Redis 做缓存"
   → This is a solution, not a problem

✅ "如何在高并发场景下优化数据访问性能？"
   → This is a problem, worth recording

Technical Implementation

Uses Obsidian MCP tools:

obsidian_append_content - Create/append content
obsidian_delete_file - Delete old files
obsidian_get_file_contents - Read existing content
obsidian_list_files_in_vault - List files

See references/implementation.md for complete technical details.

Templates

See references/templates.md for:

Technical problem template
Architecture design template
Research question template
Examples

See examples/ for complete dialogues:

inspiration-capture.md - Sudden inspiration capture
research-question.md - Recording research questions
architecture-tradeoff.md - Architecture decision questions
Common Questions

Q: How to view all ideas? Open idea/Ideas-Index.md for complete list.

Q: Can I edit existing ideas? Yes, edit directly in Obsidian or tell me what needs changing.

Q: What's the difference between idea note and regular note?

Idea note: Only problems, no solutions
Regular note: Can contain anything

Q: How to turn idea into implementation plan? When ready to implement, create new note referencing it, or add solution section to original.

Note: This skill focuses on problem recording. Understand the problem first, then seek solutions.

Weekly Installs
12
Repository
ppx123-web/claude-config
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass