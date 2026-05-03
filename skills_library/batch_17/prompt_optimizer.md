---
title: prompt-optimizer
url: https://skills.sh/chujianyun/skills/prompt-optimizer
---

# prompt-optimizer

skills/chujianyun/skills/prompt-optimizer
prompt-optimizer
Installation
$ npx skills add https://github.com/chujianyun/skills --skill prompt-optimizer
SKILL.md
Prompt Optimizer

帮助用户基于具体任务场景，选择合适的提示词框架，并生成更清晰、更可执行的 prompt。

设计模式

本 skill 主要采用：

Reviewer：先判断用户现有 prompt 或任务描述的问题
Inversion：信息不足时，先追问目标、受众、约束和格式
Generator：基于选定框架生成优化后的 prompt
Gotchas
不要一上来就套框架，先判断任务是否真的需要复杂框架
不要为了显得专业而过度设计简单 prompt
如果用户只想快速润色一句 prompt，不要强行输出一整套长模板
如果目标、受众、输出格式不清楚，先补最小必要问题
说明为什么选这个框架，比堆很多框架名更重要
Workflow

Copy this checklist and track your progress:

 Step 1: Analyze User Input
 Step 2: Match Scenario and Select Framework
 Step 3: Load Framework Details
 Step 4: Clarify Ambiguities
 Step 5: Generate Optimized Prompt
 Step 6: Present and Iterate

When a user requests create or prompt optimization, follow these steps:

Step 1: Analyze User Input

Receive the user's request, which may be:

A raw prompt that needs optimization
A task description or requirement
A vague idea that needs to be turned into a prompt
Step 2: Match Scenario and Select Framework

Read the references/Frameworks_Summary.md file to:

Identify the user's scenario from the application scenarios listed
Match the most suitable framework(s) based on:
Application scenario alignment
Task complexity (simple/medium/complex)
Domain category (marketing, decision analysis, education, etc.)

Framework Selection Guide by Complexity:

Complexity	Recommended Frameworks
Simple (≤3 elements)	APE, ERA, TAG, RTF, BAB, PEE, ELI5
Medium (4-5 elements)	RACE, CIDI, SPEAR, SPAR, FOCUS, SMART, GOPA, ORID, CARE, ROSE, PAUSE, TRACE, GRADE, TRACI, RODES
Complex (6+ elements)	RACEF, CRISPE, SCAMPER, Six Thinking Hats, ROSES, PROMPT, RISEN, RASCEF, Atomic Prompting

Framework Selection Guide by Domain:

Domain	Recommended Frameworks
Marketing Content	BAB, SPEAR, Challenge-Solution-Benefit, BLOG, PROMPT, RHODES
Decision Analysis	RICE, Pros and Cons, Six Thinking Hats, Tree of Thought, PAUSE, What If
Education & Training	Bloom's Taxonomy, ELI5, Socratic Method, PEE, Hamburger Model
Product Development	SCAMPER, HMW, CIDI, RELIC, 3Cs Model
AI Dialogue/Assistant	COAST, ROSES, TRACE, RACE, RASCEF
Writing & Creation	BLOG, 4S Method, Hamburger Model, Few-shot, RHODES, Chain of Destiny
Image Generation	Atomic Prompting
Quick Simple Tasks	Zero-shot, ERA, TAG, APE, RTF
Complex Reasoning	Chain of Thought, Tree of Thought
Step 3: Load Framework Details

Once the best framework is identified, read the corresponding framework file from the references/frameworks/ directory:

File naming pattern: XX_FrameworkName_Framework.md
Example: For RACEF framework, read references/frameworks/01_RACEF_Framework.md

The framework file contains:

Framework overview and components
Detailed explanation of each element
Pros and cons
Best practice examples
Step 4: Clarify Ambiguities

Before generating the final prompt, verify with the user:

Goal Clarity: Is the intended outcome clear?
Target Audience: Who will receive the AI's response?
Context Completeness: Is sufficient background information provided?
Format Requirements: Are there specific output format needs?
Constraints: Are there any limitations or restrictions?

Ask clarifying questions if any information is:

Missing
Ambiguous
Incomplete
Contradictory

Example clarifying questions:

"What specific outcome are you hoping to achieve?"
"Who is the target audience for this content?"
"Are there any format or length requirements?"
"What context should the AI consider?"
Step 5: Generate Optimized Prompt

Apply the selected framework to create the final prompt:

Structure the prompt according to framework components
Incorporate all clarified information
Ensure clarity and specificity
Include relevant examples if the framework requires
Add any necessary constraints or guidelines
Step 6: Present and Iterate

Present the optimized prompt to the user with:

The selected framework name and why it was chosen
The complete optimized prompt
Explanation of how each framework element was applied
Suggestions for potential variations or improvements

If the user requests changes, iterate on the prompt while maintaining framework structure.

Framework Reference Files

All framework details are stored in the references/frameworks/ directory. Each file contains:

Application scenarios
Framework components with explanations
Advantages and disadvantages
Multiple practical examples
Quick Framework Selection

For users unsure which framework to use:

User Says	Recommended Framework
"I need a simple prompt"	APE, ERA, TAG
"I want to persuade/sell"	BAB, SPEAR, Challenge-Solution-Benefit
"I need to analyze/decide"	RICE, Pros and Cons, Chain of Thought
"I want to teach/explain"	ELI5, Bloom's Taxonomy, Socratic Method
"I need creative ideas"	SCAMPER, HMW, SPARK, Imagine
"I want structured writing"	BLOG, 4S Method, Hamburger Model
"I need step-by-step reasoning"	Chain of Thought, Tree of Thought
"I'm generating images"	Atomic Prompting
"I need a detailed plan"	RISEN, RASCEF, CRISPE
Weekly Installs
113
Repository
chujianyun/skills
GitHub Stars
539
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass