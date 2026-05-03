---
rating: ⭐⭐⭐
title: base64-tools
url: https://skills.sh/winsorllc/upgraded-carnival/base64-tools
---

# base64-tools

skills/winsorllc/upgraded-carnival/base64-tools
base64-tools
Installation
$ npx skills add https://github.com/winsorllc/upgraded-carnival --skill base64-tools
SKILL.md
Base64 Tools Skill

Encode and decode data using Base64 encoding.

When to Use

Γ£à USE this skill when:

"Encode this to base64"
"Decode this base64"
"Convert file to base64"
"Decode base64 to file"
"URL-safe base64 encoding"
When NOT to Use

Γ¥î DON'T use this skill when:

Cryptographic operations ΓåÆ use encryption tools
Hash/generate signature ΓåÆ use hash-tools
Compress data ΓåÆ use compression tools
Commands
Encode String
{baseDir}/base64.sh encode "Hello World"
{baseDir}/base64.sh encode "Hello World" --url-safe
{baseDir}/base64.sh encode --string "Hello World"

Decode String
{baseDir}/base64.sh decode "SGVsbG8gV29ybGQ="
{baseDir}/base64.sh decode "SGVsbG8gV29ybGQ" --url-safe
{baseDir}/base64.sh decode --string "SGVsbG8gV29ybGQ="

Encode File
{baseDir}/base64.sh encode --file image.png
{baseDir}/base64.sh encode --file document.pdf --output encoded.txt

Decode to File
{baseDir}/base64.sh decode --string "SGVsbG8gV29ybGQ=" --output output.txt
{baseDir}/base64.sh decode --file encoded.txt --output original.png

From Stdin
echo "Hello World" | {baseDir}/base64.sh encode
cat file.txt | {baseDir}/base64.sh encode --output encoded.txt

Check if Valid Base64
{baseDir}/base64.sh validate "SGVsbG8gV29ybGQ="
{baseDir}/base64.sh validate "not-valid-base64!"

Options
Option	Description	Default
--url-safe	Use URL-safe variant (-_ instead of +/)	false
--file FILE	Read from/write to file	stdin/stdout
--string STR	Direct string input	None
--output FILE	Output to file	stdout
--wrap COLS	Wrap encoded output at N columns	76
--no-wrap	Don't wrap encoded output	false
--ignore-garbage	Ignore non-base64 characters	false
--validate	Just validate, don't decode	false
--json	Output as JSON	false
URL-Safe Base64

Standard Base64 uses + and / which aren't URL-safe. The URL-safe variant replaces:

+ ΓåÆ -
/ ΓåÆ _
Removes padding =
# Standard: SGVsbG8gV29ybGQ/==
# URL-safe: SGVsbG8gV29ybGQ_
{baseDir}/base64.sh encode "Hello?" --url-safe

Examples

Encode a string:

{baseDir}/base64.sh encode "Hello World"
# SGVsbG8gV29ybGQ=


Decode a string:

{baseDir}/base64.sh decode "SGVsbG8gV29ybGQ="
# Hello World


Encode a file:

{baseDir}/base64.sh encode --file image.png
# iVBORw0KGgoAAAANSUhEUgAA...


Decode to file:

{baseDir}/base64.sh decode --file encoded.txt --output image.png


URL-safe encoding:

{baseDir}/base64.sh encode "user@example.com" --url-safe
# dXNlckBleGFtcGxlLmNvbQ


Validate base64:

{baseDir}/base64.sh validate "SGVsbG8gV29ybGQ="
# Valid base64


JSON output:

{baseDir}/base64.sh encode "Hello" --json
# {"input": "Hello", "encoded": "SGVsbG8="}


Encode from stdin:

echo "secret data" | {baseDir}/base64.sh encode
# c2VjcmV0IGRhdGE=

Use Cases

Embed images in HTML/CSS:

ENCODED=$({baseDir}/base64.sh encode --file logo.png --no-wrap)
echo "background: url('data:image/png;base64,$ENCODED');"


Store binary in JSON:

# Encode binary file to base64, store in JSON field
{baseDir}/base64.sh encode --file binary.dat --json


API authentication:

# Create Basic Auth header
CREDS="user:pass"
ENCODED=$({baseDir}/base64.sh encode "$CREDS")
echo "Authorization: Basic $ENCODED"


Data URLs:

# Create data URL for image
{baseDir}/base64.sh encode --file icon.svg --output - | \
  sed 's/^/data:image\/svg+xml;base64,/'

Exit Codes
0: Success
1: Invalid base64 input (decode mode)
2: File not found
3: Permission denied
Notes
Uses built-in base64 command (available on most systems)
Wraps at 76 columns by default (MIME standard)
Use --no-wrap for single-line output
Binary files are handled correctly
URL-safe encoding follows RFC 4648
Weekly Installs
8
Repository
winsorllc/upgra…carnival
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass