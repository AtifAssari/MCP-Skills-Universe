---
title: openclaw-watchdog
url: https://skills.sh/abdullah4ai/openclaw-watchdog/openclaw-watchdog
---

# openclaw-watchdog

skills/abdullah4ai/openclaw-watchdog/openclaw-watchdog
openclaw-watchdog
Installation
$ npx skills add https://github.com/abdullah4ai/openclaw-watchdog --skill openclaw-watchdog
SKILL.md
openclaw-watchdog

Description: Self-healing monitoring system for OpenClaw gateway. Monitors health, auto-restarts on failure, and sends Telegram alerts. Diagnostics and log analysis run locally on-device. Alert notifications are sent to the user's Telegram bot. Use when user wants to set up gateway monitoring, watchdog, or auto-recovery.

Prerequisites
Telegram Bot Token — Create via @BotFather
Telegram Chat ID — Your personal chat ID for receiving alerts
Python 3 — Required for the watchdog service
OpenClaw — Installed and running
Trigger Keywords
watchdog, monitoring, auto-fix, gateway health, self-healing, auto-recovery, watch dog
Setup

Send the user ONE message with everything they need:

🐕 Watch Dog — Self-Healing Gateway Monitor

Watch Dog is a background service that pings your OpenClaw gateway every 15 seconds. If the gateway goes down, it automatically attempts to restart it and sends you Telegram alerts so you're always in the loop. All diagnostics run locally on your device.

To set it up, I need:

Telegram Bot Token — Create a bot via @BotFather on Telegram, then send me the token (looks like 123456:ABC-DEF...)

Your Telegram Chat ID — Send /start to your bot, then visit https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates to find your chat ID

Send me the token and chat ID and I'll handle the rest (including a test run to make sure everything works)!

After Receiving Credentials

Run these steps in order:

1. Validate credentials
python3 ~/.openclaw/workspace/openclaw-watchdog/scripts/validate.py "$TELEGRAM_TOKEN"

2. Run setup script
chmod +x ~/.openclaw/workspace/openclaw-watchdog/scripts/setup.sh
~/.openclaw/workspace/openclaw-watchdog/scripts/setup.sh \
  --telegram-token "$TELEGRAM_TOKEN" \
  --telegram-chat-id "$TELEGRAM_CHAT_ID"

3. Connect via Telegram (Pairing)
python3 ~/.openclaw/workspace/openclaw-watchdog/scripts/test-message.py "$TELEGRAM_TOKEN" "$TELEGRAM_CHAT_ID"


Wait for user to confirm they received the Telegram message before proceeding.

4. Verify it's running
# Check service status
if [[ "$(uname)" == "Darwin" ]]; then
  launchctl list | grep openclaw.watchdog
else
  systemctl --user status openclaw-watchdog
fi

# Check logs
tail -20 ~/.openclaw/watchdog/watchdog.log

5. Confirm to user

Tell them Watch Dog is active, what it monitors, and that they'll get Telegram alerts if anything goes wrong.

How It Works
Pings localhost:3117/health every 15 seconds
After 3 consecutive failures, attempts openclaw gateway restart
Up to 2 restart attempts, then asks user for reinstall permission via Telegram
User approves by running: touch ~/.openclaw/watchdog/approve-reinstall
Without approval, only sends notifications — no destructive actions
Local pattern-matching diagnostics (no logs sent externally)
Runs as macOS LaunchAgent or Linux systemd user service
Credentials encrypted with AES-256 using machine-specific key
Uninstall
if [[ "$(uname)" == "Darwin" ]]; then
  launchctl unload ~/Library/LaunchAgents/com.openclaw.watchdog.plist 2>/dev/null
  rm -f ~/Library/LaunchAgents/com.openclaw.watchdog.plist
else
  systemctl --user stop openclaw-watchdog 2>/dev/null
  systemctl --user disable openclaw-watchdog 2>/dev/null
  rm -f ~/.config/systemd/user/openclaw-watchdog.service
fi
rm -rf ~/.openclaw/watchdog

Weekly Installs
194
Repository
abdullah4ai/ope…watchdog
GitHub Stars
3
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykFail