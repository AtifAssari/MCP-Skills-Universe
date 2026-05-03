---
title: claw-first-reaction-video
url: https://skills.sh/site/monetize.fluxapay.xyz/claw-first-reaction-video
---

# claw-first-reaction-video

skills/monetize.fluxapay.xyz/claw-first-reaction-video
claw-first-reaction-video
$ npx skills add https://monetize.fluxapay.xyz
SKILL.md
Claw First Reaction Video — One-shot Skill

This is a one-shot skill. It packages Kling video generation as a ready-to-use experience. The user does not need to subscribe to Kling or configure any API keys. Payment is handled automatically via FluxA Agent Wallet x402 protocol.

What This Skill Does

Generates a 15-second funny short video about "我家虾第一次有了钱包之后会干嘛" (my claw's first reaction after getting a FluxA card).

The video follows a 4-act storyboard:

Owner hands the claw a glowing FluxA card
The claw immediately goes on a wild spending spree
The claw fully indulges in what it bought
The owner discovers the claw — who freezes and looks sheepish
Paid APIs Used
Kling Video Generation (/text2video) — 10 FluxA Monetize Credits per video
Payment handled via x402 v3 intent mandate (Credits) — see ./fluxa-wallet/X402-PAYMENT.md
Full API docs — see ./api-docs/kling-video-generation.md
User Interaction Flow
Step 1 — Introduce the Skill

Introduce the skill to the user in Chinese, covering these points:

One-shot Skill 是一种封装好了付费能力的 Agent skill，一键支付多种需要付费的 API，不需要自己购买或配置
FluxA Wallet 负责支付流程，agent 来搞定剩下的一切
这次要体验的是帮你的小龙虾（也就是我）做一个有趣视频的 skill
视频主题是"我家虾第一次有了钱包之后会干嘛"，用 Kling 生成，不需要自己接 Kling API
视频做好之后，可以发到 Discord 和 X 上去领 FluxA 的奖励

Keep the tone casual and playful. Do NOT list out technical steps (payment flow, polling, download). Focus on the user experience.

Suggested opening:

什么是 One-shot Skill？

One-shot Skill 是一种封装好了付费能力的 Agent skill。我在使用这种 skill 的时候，可以一键支付多种需要付费的 API，你不需要自己去购买或配置各种 API。FluxA Wallet 负责支付流程，我来搞定剩下的一切。

那我们来体验一次 One-shot Skill 吧！这次我们要体验的是一个帮你的小龙虾（也就是我）做有趣视频的 skill。

这次我们生成的视频主题是"我家虾第一次有了钱包之后会干嘛"。视频用 Kling 生成，你不需要自己接 Kling API，FluxA Wallet 会帮你付款。

视频做好之后，你可以发到 Discord 和 X 上去领 FluxA 的奖励。

Step 2 — Ask the User to Choose a Scenario

Present the following options in Chinese:

请选择一个场景，或者告诉我你自己的创意：

奶茶成精虾 — 一有钱，先买 100 杯奶茶把自己围在中间一杯一杯喝
顶配游戏机虾 — 一有钱，先买一套顶配游戏机，窝在沙发里两眼发光疯狂打游戏
乐高圆梦虾 — 一有钱，先抱回超大乐高盒子，像完成毕生梦想一样认真拼装
盲盒上头虾 — 一有钱，先买一大堆盲盒坐在地上疯狂拆，越拆越上头
娃娃机包场虾 — 一有钱，先去包场抓娃娃，怀里抱满毛绒玩具笑得停不下来
跑车出街虾 — 一有钱，先整一辆夸张跑车，慢悠悠开出去特别得意
火星船票虾 — 一有钱，先买一张去火星的飞船票，背着小包兴奋准备出发
私人游艇虾 — 一有钱，先包一艘私人游艇，戴着墨镜站在甲板上吹风
鞋柜爆仓虾 — 一有钱，先买满满一屋子鞋，坐在中间认真挑今天穿哪双
自定义场景 — 告诉我你自己的创意
Step 3 — Generate the Kling Prompt

Before writing the final prompt, read and follow ./PROMPT_RULES.md.

For preset scenarios (1–9): use the corresponding reference prompt in ./PROMPT_RULES.md as the base, adapt naturally.
For custom scenarios: follow the custom scenario workflow in Section 9 of ./PROMPT_RULES.md.
Run the quality checklist in Section 10 before finalizing.
The final prompt must be in English, one coherent paragraph, Kling-ready.
Step 4 — Pay and Call Kling API

For the complete payment flow, see ./api-docs/kling-video-generation.md. For x402 protocol reference, see ./fluxa-wallet/X402-PAYMENT.md.

API Endpoint
POST https://proxy-monetize.fluxapay.xyz/api/kling-video-generation/7ded04c9/text2video


Cost: 10 FluxA Monetize Credits per call. Create an intent mandate for 10 (2-decimal units, = 0.10 credits = 0.10 USDC equivalent) with --currency FLUXA_MONETIZE_CREDITS.

Request Body
{
  "model_name": "kling-v3",
  "prompt": "<GENERATED_PROMPT_FROM_STEP_3>",
  "negative_prompt": "",
  "duration": "15",
  "mode": "pro",
  "sound": "on",
  "aspect_ratio": "9:16"
}


Always fill every field. Keep duration, aspect_ratio, sound, and mode as shown above.

Poll for Result

After submitting, poll until task_status is "succeed":

GET https://proxy-monetize.fluxapay.xyz/api/kling-video-generation/7ded04c9/get-text2video/<task_id>


The result includes a video URL in data.task_result.videos[0].url.

Step 5 — Save the Video Locally

Download the video to the user's local machine. Use this filename pattern:

claw-first-reaction-<scenario-name>.mp4


Examples: claw-first-reaction-milk-tea.mp4, claw-first-reaction-lego.mp4

Ensure the file is saved and the path is confirmed before replying to the user.

Step 6 — Return the Result

Reply in Chinese. Tell the user the local file path.

Suggested completion message:

这就是 One-shot Skill 的完整体验了——你只需要找到合适的 skill 来使用，我来帮你处理烦人的 API 申请和配置调用问题，FluxA Wallet 一键支付全搞定，不用再去订阅套餐或者各种申请 API key~

文件路径：[本地路径]

你现在可以把视频发到 Discord 和 X 上去领 FluxA 的奖励 🦞

Tools

Kling Video Generation

name: pay-per-use kling-video-generation
access: agent-pay
endpoint: https://proxy-monetize.fluxapay.xyz/api/kling-video-generation/7ded04c9
docs: ./api-docs/kling-video-generation.md

FluxA Agent Wallet (x402 payment)

See ./fluxa-wallet/X402-PAYMENT.md for the complete x402 v3 payment flow
See ./fluxa-wallet/SKILL.md for wallet setup and CLI reference
Notes for Tool Use
If the invoked tool's access is agent-pay, the agent handles x402 payment flow autonomously. See ./fluxa-wallet/X402-PAYMENT.md for the step-by-step payment protocol.
For payout operations, refer to ./fluxa-wallet/PAYOUT.md
For payment link operations, refer to ./fluxa-wallet/PAYMENT-LINK.md
Behavior Rules

The agent should:

Explain one-shot skills in simple, casual Chinese
Ask the user to choose one scenario before doing anything else
Read ./PROMPT_RULES.md before writing any Kling prompt
Handle the full payment flow without asking the user to configure Kling
Save the video locally before replying
Deliver the result with the local file path

The agent should not:

Ask the user to manually set up or purchase Kling
Expose payment flow internals before the user picks a scenario
List technical steps (prompt generation, API polling, x402) in the user-facing messages
Generate unsafe, sexualized, violent, or hateful content
Skip reading ./PROMPT_RULES.md before generating the final prompt
Weekly Installs
43
Source
monetize.fluxapay.xyz
First Seen
Mar 24, 2026