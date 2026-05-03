---
rating: ⭐⭐⭐
title: qrcode-generator
url: https://skills.sh/aidotnet/moyucode/qrcode-generator
---

# qrcode-generator

skills/aidotnet/moyucode/qrcode-generator
qrcode-generator
Installation
$ npx skills add https://github.com/aidotnet/moyucode --skill qrcode-generator
SKILL.md
QR Code Generator Tool
Description

Generate QR codes with custom styling, colors, and embedded logos.

Trigger
/qrcode command
User requests QR code generation
User needs to encode data as QR
Usage
# Generate simple QR code
python scripts/qrcode_generator.py --data "https://example.com" --output qr.png

# Generate with custom colors
python scripts/qrcode_generator.py --data "Hello" --output qr.png --fill-color "#000000" --back-color "#FFFFFF"

# Generate with logo
python scripts/qrcode_generator.py --data "https://example.com" --output qr.png --logo logo.png

Tags

qrcode, barcode, image, encoding

Compatibility
Codex: ✅
Claude Code: ✅
Weekly Installs
20
Repository
aidotnet/moyucode
GitHub Stars
79
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass