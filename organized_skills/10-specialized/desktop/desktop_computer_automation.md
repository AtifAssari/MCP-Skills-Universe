---
rating: ⭐⭐⭐
title: desktop-computer-automation
url: https://skills.sh/web-infra-dev/midscene-skills/desktop-computer-automation
---

# desktop-computer-automation

skills/web-infra-dev/midscene-skills/desktop-computer-automation
desktop-computer-automation
Installation
$ npx skills add https://github.com/web-infra-dev/midscene-skills --skill desktop-computer-automation
Summary

Vision-driven desktop automation for native apps using natural language commands and screenshots.

Controls macOS, Windows, and Linux desktops entirely from visual input; no DOM or accessibility labels required
Operates synchronously with a screenshot-analyze-act loop: connect, observe screen state, execute high-level actions via natural language prompts, then disconnect
Requires a vision-capable AI model (Gemini, Qwen, Doubao, or similar) configured via environment variables; supports multiple model providers and OpenRouter
Takes over the user's mouse and keyboard during execution; best suited for desktop-native apps (Electron, Qt, native UIs) that cannot run headless; web apps should use Browser Automation instead
SKILL.md
Desktop Computer Automation

CRITICAL RULES — VIOLATIONS WILL BREAK THE WORKFLOW:

Never run midscene commands in the background. Each command must run synchronously so you can read its output (especially screenshots) before deciding the next action. Background execution breaks the screenshot-analyze-act loop.
Run only one midscene command at a time. Wait for the previous command to finish, read the screenshot, then decide the next action. Never chain multiple commands together.
Allow enough time for each command to complete. Midscene commands involve AI inference and screen interaction, which can take longer than typical shell commands. A typical command needs about 1 minute; complex act commands may need even longer.
Always report task results before finishing. After completing the automation task, you MUST proactively summarize the results to the user — including key data found, actions completed, screenshots taken, and any relevant findings. Never silently end after the last automation step; the user expects a complete response in a single interaction.
Only minimize windows, never close them unless explicitly asked. When you need to dismiss or get a window out of the way, minimize it instead of closing it. Do not close any app or window unless the user explicitly asks you to do so.

Control your desktop (macOS, Windows, Linux) using npx -y @midscene/computer@1. Each CLI command maps directly to an MCP tool — you (the AI agent) act as the brain, deciding which actions to take based on screenshots.

What act Can Do

Inside a single act call on desktop, Midscene can move the mouse, click, double-click, right-click, drag items, type or clear text, scroll, press single keys or keyboard shortcuts, and work through multi-step interactions on whatever is visible on the selected display.

Prerequisites

Midscene requires models with strong visual grounding capabilities. The following environment variables must be configured — either as system environment variables or in a .env file in the current working directory (Midscene loads .env automatically):

MIDSCENE_MODEL_API_KEY="your-api-key"
MIDSCENE_MODEL_NAME="model-name"
MIDSCENE_MODEL_BASE_URL="https://..."
MIDSCENE_MODEL_FAMILY="family-identifier"


Example: Gemini (Gemini-3-Flash)

MIDSCENE_MODEL_API_KEY="your-google-api-key"
MIDSCENE_MODEL_NAME="gemini-3-flash"
MIDSCENE_MODEL_BASE_URL="https://generativelanguage.googleapis.com/v1beta/openai/"
MIDSCENE_MODEL_FAMILY="gemini"


Example: Qwen 3.5

MIDSCENE_MODEL_API_KEY="your-aliyun-api-key"
MIDSCENE_MODEL_NAME="qwen3.5-plus"
MIDSCENE_MODEL_BASE_URL="https://dashscope.aliyuncs.com/compatible-mode/v1"
MIDSCENE_MODEL_FAMILY="qwen3.5"
MIDSCENE_MODEL_REASONING_ENABLED="false"
# If using OpenRouter, set:
# MIDSCENE_MODEL_API_KEY="your-openrouter-api-key"
# MIDSCENE_MODEL_NAME="qwen/qwen3.5-plus"
# MIDSCENE_MODEL_BASE_URL="https://openrouter.ai/api/v1"


Example: Doubao Seed 2.0 Lite

MIDSCENE_MODEL_API_KEY="your-doubao-api-key"
MIDSCENE_MODEL_NAME="doubao-seed-2-0-lite"
MIDSCENE_MODEL_BASE_URL="https://ark.cn-beijing.volces.com/api/v3"
MIDSCENE_MODEL_FAMILY="doubao-seed"


Commonly used models: Doubao Seed 2.0 Lite, Qwen 3.5, Zhipu GLM-4.6V, Gemini-3-Pro, Gemini-3-Flash.

If the model is not configured, ask the user to set it up. See Model Configuration for supported providers.

Commands
Connect to Desktop
npx -y @midscene/computer@1 connect
npx -y @midscene/computer@1 connect --displayId <id>

List Displays
npx -y @midscene/computer@1 list_displays

Take Screenshot
npx -y @midscene/computer@1 take_screenshot


After taking a screenshot, read the saved image file to understand the current screen state before deciding the next action.

Perform Action

Use act to interact with the computer and get the result. It autonomously handles all UI interactions internally — clicking, typing, scrolling, waiting, and navigating — so you should give it complex, high-level tasks as a whole rather than breaking them into small steps. Describe what you want to do and the desired effect in natural language:

# specific instructions
npx -y @midscene/computer@1 act --prompt "type hello world in the search field and press Enter"
npx -y @midscene/computer@1 act --prompt "drag the file icon to the Trash"

# or target-driven instructions
npx -y @midscene/computer@1 act --prompt "search for the weather in Shanghai using the Chrome browser, tell me the result"

Assert Current Screen State

Use assert to verify that the current screen satisfies a natural language condition. It does not perform UI actions; it checks the visible screen state and passes only when the assertion is true. Use this for validation, QA checks, and final state verification after act.

npx -y @midscene/computer@1 assert --prompt "there is a login button visible"
npx -y @midscene/computer@1 assert --prompt "the active window shows a saved confirmation message"
npx -y @midscene/computer@1 assert --displayId 1 --prompt "the file picker is open"

Use a Reference Image for Precise Targeting

When the user provides a screenshot, icon, logo, or reference image and wants an exact visual match, prefer tap --locate instead of a generic act --prompt. Pass --locate as JSON. The prompt describes the target, images supplies named reference images, and convertHttpImage2Base64: true is useful when the image URL may not be directly accessible to the model.

npx -y @midscene/computer@1 tap --locate '{
  "prompt": "tap the area contains the image",
  "images": [
    {
      "name": "target image",
      "url": "https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png"
    }
  ],
  "convertHttpImage2Base64": true
}'


The same locate JSON shape also works for other commands that accept a locate parameter.

Disconnect
npx -y @midscene/computer@1 disconnect

Consume Report Files

The generated HTML report is recommended for human reading first. It includes step-by-step execution details and replay videos for each operation, which makes it much easier to understand what happened and troubleshoot problems.

If another skill or tool needs to consume the report, first convert it with report-tool from the same platform CLI package. Prefer Markdown for LLM-based workflows. Use JSON when the report needs to be processed programmatically.

npx -y @midscene/computer@1 report-tool --action to-markdown --htmlPath ./midscene_run/report/.../index.html --outputDir ./output-markdown
npx -y @midscene/computer@1 report-tool --action split --htmlPath ./midscene_run/report/.../index.html --outputDir ./output-data

Workflow Pattern

Since CLI commands are stateless between invocations, follow this pattern:

Connect to establish a session
Health check — observe the output of the connect command. If connect already performed a health check (screenshot and mouse movement test), no additional check is needed. If connect did not perform a health check, do one manually: take a screenshot and verify it succeeds, then move the mouse to a random position (act --prompt "move the mouse to a random position") and verify it succeeds. If either step fails, stop and troubleshoot before continuing. Only proceed to the next steps after both checks pass without errors.
Launch the target app and take screenshot to see the current state, make sure the app is launched and visible on the screen.
Execute action using act to perform the desired action or target-driven instructions, and use assert when you need to verify the resulting screen state.
Disconnect when done
Report results — summarize what was accomplished, present key findings and data extracted during the task, and list any generated files (screenshots, logs, etc.) with their paths
Best Practices
Always run a health check first: After connecting, observe the output of the connect command. If connect already performed a health check (screenshot and mouse movement test), no additional check is needed. If it did not, do one manually: take a screenshot and move the mouse to a random position. Both must succeed (no errors) before proceeding with any further operations. This catches environment issues early.
Bring the target app to the foreground before using this skill: For best efficiency, bring the app to the foreground using other means (e.g., open -a <AppName> on macOS, start <AppName> on Windows) before invoking any midscene commands. Then take a screenshot to confirm the app is actually in the foreground. Only after visual confirmation should you proceed with UI automation using this skill. Avoid using Spotlight, Start menu search, or other launcher-based approaches through midscene — they involve transient UI, multiple AI inference steps, and are significantly slower.
Be specific about UI elements: Instead of vague descriptions, provide clear, specific details. Say "the yellow minimize button in the top-left corner of the Safari window" instead of "the button".
Describe locations when possible: Help target elements by describing their position (e.g., "the icon in the top-right corner of the menu bar", "the third item in the left sidebar").
Never run in background: Every midscene command must run synchronously — background execution breaks the screenshot-analyze-act loop.
Check for multiple displays: If you launched an app but cannot see it on the screenshot, the app window may have opened on a different display. Use list_displays to check available displays. You have two options: either move the app window to the current display, or use connect --displayId <id> to switch to the display where the app is.
Batch related operations into a single act command: When performing consecutive operations within the same app, combine them into one act prompt instead of splitting them into separate commands. For example, "search for X, click the first result, and scroll down to see more details" should be a single act call, not three. This reduces round-trips, avoids unnecessary screenshot-analyze cycles, and is significantly faster.
Set up PATH before running (macOS): On macOS, some commands (e.g., system_profiler) may not be found if the PATH is incomplete. Before running any midscene commands, ensure the PATH includes the standard system directories:
export PATH="/usr/sbin:/usr/bin:/bin:/sbin:$PATH"

This prevents screenshot failures caused by missing system utilities.
Use assert for verification: When the goal is to confirm that a screen state is true, use assert --prompt "..." instead of an act prompt. Keep assertions observable and specific, such as "the Save dialog is open" or "the export completed message is visible".
Always report results after completion: After finishing the automation task, you MUST proactively present the results to the user without waiting for them to ask. This includes: (1) the answer to the user's original question or the outcome of the requested task, (2) key data extracted or observed during execution, (3) screenshots and other generated files with their paths, (4) a brief summary of steps taken. Do NOT silently finish after the last automation command — the user expects complete results in a single interaction.
Prefer tap --locate when a reference image is provided: If the user shares a screenshot, icon, or logo and wants that exact visual target, use tap --locate with a multimodal locate JSON object such as { "prompt": "...", "images": [...] } instead of relying only on act --prompt.

Example — Context menu interaction:

npx -y @midscene/computer@1 act --prompt "right-click the file icon and select Delete from the context menu"
npx -y @midscene/computer@1 take_screenshot


Example — Dropdown menu:

npx -y @midscene/computer@1 act --prompt "open the File menu and click New Window"
npx -y @midscene/computer@1 take_screenshot

Troubleshooting
macOS: Accessibility Permission Denied

Your terminal app does not have Accessibility access:

Open System Settings > Privacy & Security > Accessibility
Add your terminal app and enable it
Restart your terminal app after granting permission
macOS: Xcode Command Line Tools Not Found
xcode-select --install

API Key Not Set

Check .env file contains MIDSCENE_MODEL_API_KEY=<your-key>.

macOS: Screenshot Fails with system_profiler Not Found

If take_screenshot fails with an error like system_profiler: command not found, the PATH environment variable is likely incomplete. Fix it by running:

export PATH="/usr/sbin:/usr/bin:/bin:/sbin:$PATH"


Then retry the screenshot command.

macOS: Screenshot Returns a Black Screen

If take_screenshot returns a completely black image, the Mac is likely locked (e.g. screen is at the login/lock window). This is a system-level restriction — macOS prohibits capturing the screen contents while the session is locked, so there is no workaround at the application level.

Recommended fix: Use a screensaver instead of locking the screen. A screensaver keeps the user session active and unlocked, allowing screenshots to capture normally.

Open System Settings > Lock Screen
Set "Require password after screen saver begins or display is turned off" to a longer delay (or turn it off during automation)
Optionally configure a screensaver under System Settings > Screen Saver so the display still dims after inactivity without locking
AI Cannot Find the Element
Take a screenshot to verify the element is actually visible
Use more specific descriptions (include color, position, surrounding text)
Ensure the element is not hidden behind another window
@midscene/* Dependency Version Outdated
Check local versions: npm ls @midscene/computer @midscene/core @midscene/shared (or pnpm why @midscene/computer).
Check latest versions: npm view @midscene/computer version, npm view @midscene/core version, npm view @midscene/shared version.
Upgrade dependencies: npm i @midscene/computer@latest @midscene/core@latest @midscene/shared@latest.
Weekly Installs
2.6K
Repository
web-infra-dev/m…e-skills
GitHub Stars
201
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn