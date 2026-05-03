---
rating: ⭐⭐⭐
title: base64-encoder
url: https://skills.sh/aidotnet/moyucode/base64-encoder
---

# base64-encoder

skills/aidotnet/moyucode/base64-encoder
base64-encoder
Installation
$ npx skills add https://github.com/aidotnet/moyucode --skill base64-encoder
SKILL.md
Base64 Encoder Tool
Description

Encode and decode Base64, URL-safe Base64, and hexadecimal strings with support for files.

Trigger
/base64 command
User needs to encode/decode data
User wants to convert binary to text
Usage
# Encode text
python scripts/base64_encoder.py encode "Hello World"

# Decode Base64
python scripts/base64_encoder.py decode "SGVsbG8gV29ybGQ="

# Encode file
python scripts/base64_encoder.py encode --file image.png --output image.b64

# URL-safe encoding
python scripts/base64_encoder.py encode "data" --url-safe

Tags

base64, encode, decode, binary, text

Compatibility
Codex: ✅
Claude Code: ✅
Weekly Installs
25
Repository
aidotnet/moyucode
GitHub Stars
79
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass