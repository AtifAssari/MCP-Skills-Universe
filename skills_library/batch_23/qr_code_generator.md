---
title: qr-code-generator
url: https://skills.sh/dkyazzentwatwa/chatgpt-skills/qr-code-generator
---

# qr-code-generator

skills/dkyazzentwatwa/chatgpt-skills/qr-code-generator
qr-code-generator
Installation
$ npx skills add https://github.com/dkyazzentwatwa/chatgpt-skills --skill qr-code-generator
SKILL.md
QR Code Generator

Create QR assets that are safe to print, easy to scan, and explicit about the encoded destination.

Workflow
Validate the target URL and prefer HTTPS.
Add UTM parameters only when the campaign needs them.
Generate single codes with scripts/generate_qr.py or batches with scripts/batch_generate.py.
Prefer SVG and higher error correction for print uses.
Guardrails
Do not generate QR codes for suspicious or deceptive destinations.
Return the final encoded URL alongside the output files.
Explain when PNG is fine and when SVG is the better choice.
Weekly Installs
116
Repository
dkyazzentwatwa/…t-skills
GitHub Stars
53
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass