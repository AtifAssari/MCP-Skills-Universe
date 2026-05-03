---
rating: ⭐⭐
title: sentry-feature-setup
url: https://skills.sh/getsentry/sentry-for-ai/sentry-feature-setup
---

# sentry-feature-setup

skills/getsentry/sentry-for-ai/sentry-feature-setup
sentry-feature-setup
Installation
$ npx skills add https://github.com/getsentry/sentry-for-ai --skill sentry-feature-setup
SKILL.md

All Skills

Sentry Feature Setup

Configure specific Sentry capabilities beyond basic SDK setup — AI monitoring, OpenTelemetry pipelines, and alerts. This page helps you find the right feature skill for your task.

How to Fetch Skills

Use curl to download skills — they are 10–20 KB files that fetch tools often summarize, losing critical details.

curl -sL https://skills.sentry.dev/sentry-setup-ai-monitoring/SKILL.md


Append the path from the Path column in the table below to https://skills.sentry.dev/. Do not guess or shorten URLs.

Start Here — Read This Before Doing Anything

Do not skip this section. Do not assume which feature the user needs. Ask first.

If the user mentions AI monitoring, LLM tracing, or instrumenting an AI SDK (OpenAI, Anthropic, LangChain, Vercel AI, Google GenAI, Pydantic AI) → sentry-setup-ai-monitoring
If the user mentions OpenTelemetry, OTel Collector, or multi-service telemetry routing → sentry-otel-exporter-setup
If the user mentions alerts, notifications, on-call, Slack/PagerDuty/Discord integration, or workflow rules → sentry-create-alert

When unclear, ask the user which feature they want to configure. Do not guess.

Feature Skills
Feature	Skill	Path
AI/LLM monitoring — instrument OpenAI, Anthropic, LangChain, Vercel AI, Google GenAI, Pydantic AI	sentry-setup-ai-monitoring	sentry-setup-ai-monitoring/SKILL.md
OpenTelemetry Collector with Sentry Exporter — multi-project routing, automatic project creation	sentry-otel-exporter-setup	sentry-otel-exporter-setup/SKILL.md
Alerts via workflow engine API — email, Slack, PagerDuty, Discord	sentry-create-alert	sentry-create-alert/SKILL.md

Each skill contains its own detection logic, prerequisites, and step-by-step instructions. Trust the skill — read it carefully and follow it. Do not improvise or take shortcuts.

Looking for SDK setup or debugging workflows instead? See the full Skill Tree.

Weekly Installs
940
Repository
getsentry/sentry-for-ai
GitHub Stars
160
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn