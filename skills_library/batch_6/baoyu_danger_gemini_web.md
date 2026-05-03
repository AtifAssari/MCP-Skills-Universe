---
title: baoyu-danger-gemini-web
url: https://skills.sh/jimliu/baoyu-skills/baoyu-danger-gemini-web
---

# baoyu-danger-gemini-web

skills/jimliu/baoyu-skills/baoyu-danger-gemini-web
baoyu-danger-gemini-web
Installation
$ npx skills add https://github.com/jimliu/baoyu-skills --skill baoyu-danger-gemini-web
Summary

Reverse-engineered Gemini Web API for text and image generation with multi-turn conversation support.

Supports text generation, image generation from prompts, and vision input via reference images for analysis or variation
Includes four model options: gemini-3-pro (default), gemini-3-flash, gemini-3-flash-thinking, and gemini-3.1-pro-preview
Multi-turn conversation via session IDs with automatic cookie caching and browser-based Google authentication
Requires user consent before first use; supports custom configuration via EXTEND.md for model defaults, proxy settings, and data directory paths
SKILL.md
Gemini Web Client

Text/image generation via Gemini Web API. Supports reference images and multi-turn conversations.

User Input Tools

When this skill prompts the user, follow this tool-selection rule (priority order):

Prefer built-in user-input tools exposed by the current agent runtime — e.g., AskUserQuestion, request_user_input, clarify, ask_user, or any equivalent.
Fallback: if no such tool exists, emit a numbered plain-text message and ask the user to reply with the chosen number/answer for each question.
Batching: if the tool supports multiple questions per call, combine all applicable questions into a single call; if only single-question, ask them one at a time in priority order.

Concrete AskUserQuestion references below are examples — substitute the local equivalent in other runtimes.

Script Directory

Important: All scripts are located in the scripts/ subdirectory of this skill.

Agent Execution Instructions:

Determine this SKILL.md file's directory path as {baseDir}
Script path = {baseDir}/scripts/<script-name>.ts
Resolve ${BUN_X} runtime: if bun installed → bun; if npx available → npx -y bun; else suggest installing bun
Replace all {baseDir} and ${BUN_X} in this document with actual values

Script Reference:

Script	Purpose
scripts/main.ts	CLI entry point for text/image generation
scripts/gemini-webapi/*	TypeScript port of gemini_webapi (GeminiClient, types, utils)
Consent Check (REQUIRED)

Before first use, verify user consent for reverse-engineered API usage.

Consent file locations:

macOS: ~/Library/Application Support/baoyu-skills/gemini-web/consent.json
Linux: ~/.local/share/baoyu-skills/gemini-web/consent.json
Windows: %APPDATA%\baoyu-skills\gemini-web\consent.json

Flow:

Check if consent file exists with accepted: true and disclaimerVersion: "1.0"
If valid consent exists → print warning with acceptedAt date, proceed
If no consent → show disclaimer, ask user via AskUserQuestion:
"Yes, I accept" → create consent file with ISO timestamp, proceed
"No, I decline" → output decline message, stop
Consent file format: {"version":1,"accepted":true,"acceptedAt":"<ISO>","disclaimerVersion":"1.0"}
Preferences (EXTEND.md)

Check EXTEND.md in priority order — the first one found wins:

Priority	Path	Scope
1	.baoyu-skills/baoyu-danger-gemini-web/EXTEND.md	Project
2	${XDG_CONFIG_HOME:-$HOME/.config}/baoyu-skills/baoyu-danger-gemini-web/EXTEND.md	XDG
3	$HOME/.baoyu-skills/baoyu-danger-gemini-web/EXTEND.md	User home

If none found, use defaults.

EXTEND.md supports: Default model, proxy settings, custom data directory.

Usage
# Text generation
${BUN_X} {baseDir}/scripts/main.ts "Your prompt"
${BUN_X} {baseDir}/scripts/main.ts --prompt "Your prompt" --model gemini-3-flash

# Image generation
${BUN_X} {baseDir}/scripts/main.ts --prompt "A cute cat" --image cat.png
${BUN_X} {baseDir}/scripts/main.ts --promptfiles system.md content.md --image out.png

# Vision input (reference images)
${BUN_X} {baseDir}/scripts/main.ts --prompt "Describe this" --reference image.png
${BUN_X} {baseDir}/scripts/main.ts --prompt "Create variation" --reference a.png --image out.png

# Multi-turn conversation
${BUN_X} {baseDir}/scripts/main.ts "Remember: 42" --sessionId session-abc
${BUN_X} {baseDir}/scripts/main.ts "What number?" --sessionId session-abc

# JSON output
${BUN_X} {baseDir}/scripts/main.ts "Hello" --json

Options
Option	Description
--prompt, -p	Prompt text
--promptfiles	Read prompt from files (concatenated)
--model, -m	Model: gemini-3-pro (default), gemini-3-flash, gemini-3-flash-thinking, gemini-3.1-pro-preview
--image [path]	Generate image (default: generated.png)
--reference, --ref	Reference images for vision input
--sessionId	Session ID for multi-turn conversation
--list-sessions	List saved sessions
--json	Output as JSON
--login	Refresh cookies, then exit
--cookie-path	Custom cookie file path
--profile-dir	Chrome profile directory
Models
Model	Description
gemini-3-pro	Default, latest 3.0 Pro
gemini-3-flash	Fast, lightweight 3.0 Flash
gemini-3-flash-thinking	3.0 Flash with thinking
gemini-3.1-pro-preview	3.1 Pro preview (empty header, auto-routed)
Authentication

First run opens browser for Google auth. Cookies cached automatically.

When no explicit profile dir is set, cookie refresh may reuse an already-running local Chrome/Chromium debugging session tied to a standard user-data dir. Set --profile-dir or GEMINI_WEB_CHROME_PROFILE_DIR to force a dedicated profile and skip existing-session reuse. This is a best-effort CDP session reuse path, not the Chrome DevTools MCP prompt-based --autoConnect flow described in Chrome's official docs.

Supported browsers (auto-detected): Chrome, Chrome Canary/Beta, Chromium, Edge.

Force refresh: --login flag. Override browser: GEMINI_WEB_CHROME_PATH env var.

Environment Variables
Variable	Description
GEMINI_WEB_DATA_DIR	Data directory
GEMINI_WEB_COOKIE_PATH	Cookie file path
GEMINI_WEB_CHROME_PROFILE_DIR	Chrome profile directory
GEMINI_WEB_CHROME_PATH	Chrome executable path
HTTP_PROXY, HTTPS_PROXY	Proxy for Google access (set inline with command)
Sessions

Session files stored in data directory under sessions/<id>.json.

Contains: id, metadata (Gemini chat state), messages array, timestamps.

Extension Support

Custom configurations via EXTEND.md. See Preferences section for paths and supported options.

Weekly Installs
16.7K
Repository
jimliu/baoyu-skills
GitHub Stars
16.9K
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn