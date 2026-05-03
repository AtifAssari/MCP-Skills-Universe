---
title: voice-call
url: https://skills.sh/steipete/clawdis/voice-call
---

# voice-call

skills/steipete/clawdis/voice-call
voice-call
Installation
$ npx skills add https://github.com/steipete/clawdis --skill voice-call
SKILL.md
Voice Call

Use the voice-call plugin to start or inspect calls (Twilio, Telnyx, Plivo, or mock).

CLI
openclaw voicecall call --to "+15555550123" --message "Hello from OpenClaw"
openclaw voicecall status --call-id <id>

Tool

Use voice_call for agent-initiated calls.

Actions:

initiate_call (message, to?, mode?)
continue_call (callId, message)
speak_to_user (callId, message)
end_call (callId)
get_status (callId)

Notes:

Requires the voice-call plugin to be enabled.
Plugin config lives under plugins.entries.voice-call.config.
Twilio config: provider: "twilio" + twilio.accountSid/authToken + fromNumber.
Telnyx config: provider: "telnyx" + telnyx.apiKey/connectionId + fromNumber.
Plivo config: provider: "plivo" + plivo.authId/authToken + fromNumber.
Dev fallback: provider: "mock" (no network).
Weekly Installs
1.1K
Repository
steipete/clawdis
GitHub Stars
367.2K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass