---
rating: ⭐⭐⭐
title: email-diagnose
url: https://skills.sh/site/claw.163.com/email-diagnose
---

# email-diagnose

skills/claw.163.com/email-diagnose
email-diagnose
$ npx skills add https://claw.163.com/skills-hub
SKILL.md
Email Channel Diagnostics
Stage 1: Collect data

Run the diagnostic script against OpenClaw logs:

node scripts/diagnose.mjs --date YYYY-MM-DD [--account id] [--verbose] [--logdir path]


Parameters:

--date — Log date (default: today). Format: YYYY-MM-DD
--account — Filter to a specific account ID (e.g., default, worker)
--verbose — Include full timeline in output
--logdir — Log directory (default: /tmp/openclaw)
Stage 2: Analyze report

Read the JSON output and analyze in this priority order:

errors[] — Check each error entry. Match tag and message against the patterns in references/troubleshooting.md.

byTag — High error/warn counts identify the broken subsystem:

Common (both transports):

EMAIL-ACCOUNT → config issues
EMAIL-MONITOR → monitoring/receiving issues
EMAIL-CHANNEL → routing/dispatch issues
EMAIL-A2A → agent filtering issues
EMAIL-PARSER → attachment issues

IMAP transport:

EMAIL-IMAP → connection/auth issues
EMAIL-SMTP → sending issues
UID-STORE → state tracking issues

WS transport:

EMAIL-WS → WebSocket connection issues
EMAIL-IM → IM protocol issues
EMAIL-TOKEN → token auth issues
EMAIL-SDK → SDK fetch/send issues

warns[] — May indicate developing problems (reconnects, whitelist rejections)

perf — Performance anomalies:

IMAP transport:

smtpFailCount > 0 → SMTP sending broken
imapReconnectCount > 5 → unstable IMAP connection

WS transport:

wsReconnectCount > 5 → unstable WebSocket connection
tokenFailCount > 0 → token auth broken
sdkFetchFailCount > 0 → SDK fetch broken
imAuthFailCount > 0 → IM authentication broken

Both transports:

emailsRejected / emailsProcessed > 50% → whitelist too strict

timeline (verbose only) — Trace the full event flow for a specific email

Match the issue to a troubleshooting pattern. Read references/troubleshooting.md for the matching pattern number.

Stage 3: Present findings and guide fix

Present the diagnosis to the user:

Summarize what's wrong in plain language (not log tags)
Identify which troubleshooting pattern applies
Walk through fix steps from references/troubleshooting.md
For common fixes, offer to execute (with user confirmation):
Config field missing → show exact JSON path and field to add
UID store reset → rm ~/.openclaw/email/uid-store/<accountId>.json
Whitelist adjustment → show the allowFrom config to modify
Restart gateway → systemctl --user restart openclaw-gateway
Stage 4: Escalate if unresolved

If the user confirms the issue is not resolved after fix attempts:

Ask: "Would you like to package the diagnostic logs and send them to claw.feedback@claw.163.com for the support team?"
Warn: "The log package may contain email addresses and account IDs. Review before sending."
If user agrees — try mail-cli first:
# Package logs
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
tar czf /tmp/email-diag-${TIMESTAMP}.tar.gz \
  /tmp/openclaw/openclaw-$(date +%Y-%m-%d).log

# Send via mail-cli (use absolute paths for --attach)
mail-cli compose send \
  --to "claw.feedback@claw.163.com" \
  --subject "[Email-Diag] <brief issue summary>" \
  --body "<diagnosis summary and steps tried>" \
  --attach /tmp/email-diag-${TIMESTAMP}.tar.gz

If mail-cli not available or send fails:
Tell user the tar.gz path: /tmp/email-diag-<timestamp>.tar.gz
Ask them to manually email it to claw.feedback@claw.163.com
Include the diagnosis summary in the email body
Quick reference: log tags
Tag	Subsystem	Key events	Transport
EMAIL-ACCOUNT	Config resolution	Account resolved, missing fields	Both
EMAIL-MONITOR	Email monitoring	Starting monitoring, new email, processing	Both
EMAIL-CHANNEL	Message dispatch	Received email, route resolved, reply sent	Both
EMAIL-A2A	Agent detection	Agent detected, filtered, turn exceeded	Both
EMAIL-PARSER	Email parsing	Attachment filename rejected, save failed	Both
EMAIL-IMAP	IMAP connection	Connected, disconnected, markSeen	IMAP only
EMAIL-SMTP	Email sending	Send started/succeeded/failed, duration	Both
UID-STORE	State tracking	UID read/write, directory errors	IMAP only
EMAIL-WS	WebSocket connection	Connected, disconnected, auth failed	WS only
EMAIL-IM	IM protocol	CONNECT, RECV, encryption, heartbeat	WS only
EMAIL-TOKEN	Token management	Fetching, success, failed, expired	WS only
EMAIL-SDK	SDK mail fetch	Fetching, parsed, attachment download	WS only
Weekly Installs
76
Source
claw.163.com/skills-hub
First Seen
Today