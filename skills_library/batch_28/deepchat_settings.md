---
title: deepchat-settings
url: https://skills.sh/thinkinaixyz/deepchat/deepchat-settings
---

# deepchat-settings

skills/thinkinaixyz/deepchat/deepchat-settings
deepchat-settings
Installation
$ npx skills add https://github.com/thinkinaixyz/deepchat --skill deepchat-settings
SKILL.md
DeepChat Settings Modification Skill

Use this skill to safely change DeepChat application settings during a conversation.

Core rules
Only change settings when the user is asking to change DeepChat settings.
Use the dedicated settings tools; never attempt arbitrary key/value writes.
These tools are intended to be available only when this skill is active; if they are missing, activate this skill via skill_control.
If the request is ambiguous, ask a clarifying question before applying.
For unsupported or high-risk settings (MCP, prompts, providers, API keys, paths): do not apply changes; instead explain where to change it and open Settings.
After completing the settings task, deactivate this skill via skill_control to keep context small.
Supported settings (initial allowlist)

Toggles:

soundEnabled: enable/disable sound effects.
copyWithCotEnabled: enable/disable copying COT details.

Enums:

language: DeepChat locale, including system, zh-CN, en-US, zh-TW, zh-HK, ko-KR, ru-RU, ja-JP, fr-FR, fa-IR, pt-BR, da-DK, he-IL.
theme: dark | light | system.
fontSizeLevel: integer level within supported range.

Settings navigation (open-only):

Use deepchat_settings_open only when the request cannot be fulfilled by the settings tools, and avoid calling it if the change is already applied.
section hints: common, display, provider, mcp, prompt, acp, skills, knowledge-base, database, shortcut, about.
Workflow
Confirm the user is requesting a DeepChat settings change.
Determine the target setting and the intended value.
If the setting is supported, call the matching tool:
toggles: deepchat_settings_toggle
language: deepchat_settings_set_language
theme: deepchat_settings_set_theme
font size: deepchat_settings_set_font_size
Confirm back to the user what changed (include the final value).
If the setting is unsupported, call deepchat_settings_open (with section) and provide a short pointer to the correct Settings section. Do not call it if the requested change has already been applied.
Deactivate this skill via skill_control.
Examples (activate this skill)
"把主题改成深色"
"Turn off sound effects"
"语言改成英文"
"复制时不要带 COT"
"Open the MCP settings page"
"Edit my prompts"
Examples (do NOT activate this skill)
"把 Windows 的系统代理改成..."
"帮我改 VS Code 的字体"
"把电脑的声音关掉"
Weekly Installs
34
Repository
thinkinaixyz/deepchat
GitHub Stars
5.6K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass