---
rating: ⭐⭐⭐
title: customer-persona-framer
url: https://skills.sh/timlai666/skills/customer-persona-framer
---

# customer-persona-framer

skills/timlai666/skills/customer-persona-framer
customer-persona-framer
Installation
$ npx skills add https://github.com/timlai666/skills --skill customer-persona-framer
SKILL.md
Customer Persona Framer
Overview

Create persona-first outputs in Traditional Chinese. Stop at a reusable persona when the task is only about customer definition, or expand into a journey-framing brief that can be handed to customer-journey-mapper. Use this skill first when someone wants customer-journey-mapper output but no completed persona exists yet.

Default output is structured Markdown. If the user explicitly asks for 簡報、投影片、教學圖、slides、deck, keep the same information architecture but rewrite each section as presentation-ready bullets.

Mode Policy

Use mode: auto | persona-only | journey-framing. If the user wants customer-journey-mapper output but no persona is available yet, choose journey-framing first so the result can be handed off downstream.

auto rules:

If the user asks for persona、人物誌、顧客輪廓、使用者輪廓、目標客群分析、輪廓建模, choose persona-only.
If the user asks for 5W1H、顧客旅程、接觸點、情緒、階段、旅程地圖前置, choose journey-framing.
If the user clearly says 只要 persona、先不要旅程, lock to persona-only even if journey words also appear.
Input Contract

Need at least one of:

產品或服務
目標客群
初步 persona 線索

Optional:

使用情境
品牌/產業背景
既有接觸點
輸出用途
mode

Default assumptions:

produce one core persona, not multiple persona variants
infer the most likely decision and usage context from the available clues
keep the persona grounded in plausible behavior, not decorative storytelling
Data Sufficiency Gate

If the available input is enough to define one coherent persona, generate directly.

If critical information is missing and the user did not ask for speed:

ask concise follow-up questions first
do not fabricate a final persona or journey frame

If the user asks for a quick draft, for example:

先做一版
快速版
可先假設
直接幫我整理

Then:

list 3-5 assumptions first
generate the requested output after the assumptions
keep every assumption observable and business-relevant
Output Contract

Always answer in Traditional Chinese.

persona-only

Output sections in this order:

Persona 卡
核心特徵與限制
需求/痛點/期望
persona_block

Recommended Persona 卡 fields:

角色代稱
年齡層/人生階段
背景與生活型態
主要目標
決策線索
使用情境

persona_block must be compact and reusable. Use this shape:

### persona_block
- 顧客輪廓: ...
- 角色背景: ...
- 核心需求: ...
- 主要痛點: ...
- 使用情境: ...
- 決策線索: ...


Do not add handoff_to_customer_journey_mapper in persona-only.

journey-framing

Output sections in this order:

Persona 卡
5W1H 摘要
旅程五元素摘要
階段定義
handoff_to_customer_journey_mapper

5W1H 摘要 must cover:

Who
What
When
Where
Why
How

旅程五元素摘要 must cover:

persona
stages
touchpoints
emotions
metrics

Default stage names must align with customer-journey-mapper:

認知
考慮/研究
決策/購買
使用
關係建立

metrics stay in this summary only. Do not copy metrics into the mapper handoff block.

Use this handoff shape:

### handoff_to_customer_journey_mapper
- 顧客輪廓: ...
- 產品或服務: ...
- 品牌/產業背景: ...
- 目標市場: ...
- 目前接觸點: ...
- 輸出用途: ...


When information is unknown:

omit the field if it is truly unavailable, or
mark it as a short assumption if the user requested a quick draft
Workflow
Read the product, audience clue, and context.
Choose persona-only or journey-framing.
Build the persona from the customer's point of view.
Separate stable traits, real constraints, needs, pain points, and expectations.
Only in journey-framing, convert the persona into 5W1H, five journey elements, and stage definitions.
If journey-framing, produce handoff_to_customer_journey_mapper as the final section.
Quality Rules
do not stereotype with invented demographics, income, or family details unless the prompt supports them
distinguish 需求, 痛點, and 期望; do not collapse them into one vague list
make constraints operational, for example time pressure, knowledge gaps, approval needs, or device habits
keep 接觸點 concrete, such as search, LINE, store visit, DM, app push, or friend referral
make 情緒 a real state or transition, not a marketing adjective
make metrics observable, such as click-through, consultation rate, trial start, repeat use, or support resolution
slide-ready mode should shorten phrasing, not change the substance
Suggested Prompts
Use $customer-persona-framer to create a Traditional Chinese persona profile from 產品或服務 and 目標客群.
Use $customer-persona-framer to create a Traditional Chinese journey-framing brief with persona, 5W1H, and a handoff block for customer-journey-mapper.
Weekly Installs
12
Repository
timlai666/skills
First Seen
Mar 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass