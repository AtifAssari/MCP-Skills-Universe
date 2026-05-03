---
rating: ⭐⭐
title: qr-code-generator
url: https://skills.sh/manojbajaj95/claude-gtm-plugin/qr-code-generator
---

# qr-code-generator

skills/manojbajaj95/claude-gtm-plugin/qr-code-generator
qr-code-generator
Installation
$ npx skills add https://github.com/manojbajaj95/claude-gtm-plugin --skill qr-code-generator
SKILL.md
QR Code Generator
What this skill does

Given a URL, this skill generates:

a QR code that encodes the URL
optional captions (human-readable URL or short label)
exports in PNG and/or SVG
optional batch runs from a CSV
Guardrails
Don’t generate QR codes for suspicious links (phishing, credential prompts, malware). If unsure, ask for confirmation or suggest a safer destination page.
Prefer HTTPS URLs.
If the QR is for print, prefer SVG (scales cleanly) and high error correction.
Inputs

Required:

URL

Optional:

label/caption text (e.g., “Scan to book a call”)
whether to show the URL under the QR (yes/no)
output formats: PNG, SVG
UTM params (source, medium, campaign, content, term)
size intent: screen / print / sticker
Workflow
Validate the URL (scheme + domain).
Optionally append UTM parameters (using assets/templates/utm_template.json).
Generate QR:
Error correction: M (default), H for print/complex usage
Border: 4 (default)
Export:
PNG (good for web)
SVG (best for print)
If caption enabled:
PNG: add label and/or URL under the QR
SVG: add a text element under the QR
Return links + a quick “usage notes” block (recommended minimum size, print tips).
Output format (required)
Encoded URL (final URL after UTM, if used)
Files generated (with links)
Recommendations (error correction, min size, when to use SVG vs PNG)
Scripts in this pack
scripts/generate_qr.py — single QR (PNG/SVG, optional caption)
scripts/batch_generate.py — batch from CSV (id,url,label)
Templates
assets/templates/utm_template.json
assets/templates/print_notes.md
assets/templates/prompt_snippets.md
Weekly Installs
162
Repository
manojbajaj95/cl…m-plugin
GitHub Stars
43
First Seen
Mar 11, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass