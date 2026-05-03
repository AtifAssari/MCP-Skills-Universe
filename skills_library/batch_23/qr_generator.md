---
title: qr-generator
url: https://skills.sh/winsorllc/upgraded-carnival/qr-generator
---

# qr-generator

skills/winsorllc/upgraded-carnival/qr-generator
qr-generator
Installation
$ npx skills add https://github.com/winsorllc/upgraded-carnival --skill qr-generator
SKILL.md
QR Code Generator Skill

Generate QR codes for various data types using Python's qrcode library.

When to Use

✅ USE this skill when:

"Generate a QR code for this URL"
"Create QR code for WiFi credentials"
"Make a QR code for contact info"
"Generate QR for this text"
When NOT to Use

❌ DON'T use this skill when:

Reading/scanning QR codes → use mobile device or dedicated scanner
Creating barcodes (non-QR) → use barcode libraries
Setup

Install required package:

pip install qrcode pillow

Commands
Basic QR Code
{baseDir}/qr.sh "https://example.com"
{baseDir}/qr.sh "Hello, World!" --out /tmp/qr.png

WiFi QR Code
{baseDir}/qr-wifi.sh --ssid "MyNetwork" --password "secret123"
{baseDir}/qr-wifi.sh --ssid "MyNetwork" --password "secret123" --security WPA3

vCard QR Code
{baseDir}/qr-vcard.sh --name "John Doe" --phone "+1234567890" --email "john@example.com"
{basedir}/qr-vcard.sh --name "Jane Doe" --phone "+1234567890" --org "Company" --url "https://example.com"

Email QR Code
{baseDir}/qr-email.sh --to "user@example.com" --subject "Hello" --body "Check this out"

Customize Options
{baseDir}/qr.sh "data" --size 20 --border 4 --color black --bg white
{baseDir}/qr.sh "data" --out /tmp/custom.png --size 30 --border 2

Options
--out <path>: Output file path (default: qr.png)
--size <N>: Module size in pixels (default: 10)
--border <N>: Border size in modules (default: 4)
--color <color>: QR code color (default: black)
--bg <color>: Background color (default: white)
--format <fmt>: Output format: PNG, SVG (default: PNG)
Output Formats
PNG

Binary image file, widely compatible.

SVG

Vector format, scalable without quality loss.

Examples

URL QR Code:

{baseDir}/qr.sh "https://mywebsite.com/page?id=123" --out website.png


WiFi QR Code (guests can scan to connect):

{baseDir}/qr-wifi.sh --ssid "GuestNetwork" --password "guestpass" --security WPA


Contact QR Code (scan to add to contacts):

{baseDir}/qr-vcard.sh --name "Alice Smith" --phone "+15551234567" --email "alice@example.com"

Notes
QR codes can store up to ~4KB of data
Larger data = denser QR = harder to scan
Use URL shorteners for very long URLs
Error correction allows partial damage recovery
Weekly Installs
8
Repository
winsorllc/upgra…carnival
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail