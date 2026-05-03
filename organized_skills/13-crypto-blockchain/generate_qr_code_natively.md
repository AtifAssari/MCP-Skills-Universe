---
rating: ⭐⭐⭐
title: generate-qr-code-natively
url: https://skills.sh/besoeasy/open-skills/generate-qr-code-natively
---

# generate-qr-code-natively

skills/besoeasy/open-skills/generate-qr-code-natively
generate-qr-code-natively
Installation
$ npx skills add https://github.com/besoeasy/open-skills --skill generate-qr-code-natively
SKILL.md
Generate QR Code Natively

Create QR codes fully offline on the local machine (no third-party QR API calls).

When to use
User asks to generate a QR code from text, URL, wallet address, or payload
Privacy-sensitive workflows where data should stay local
Fast automation pipelines that should not depend on external services
Required tools / APIs
No external API required
Bash CLI option: qrencode
Node.js option: qrcode package

Install options:

# Ubuntu/Debian
sudo apt-get update && sudo apt-get install -y qrencode

# Node.js
npm install qrcode

Skills
generate_qr_with_bash

Generate PNG and terminal QR directly from shell.

# Encode text into PNG
DATA="https://example.com/report?id=123"
qrencode -o qrcode.png -s 8 -m 2 "$DATA"

# Print QR in terminal (UTF-8 block mode)
qrencode -t UTF8 "$DATA"

# SVG output
qrencode -t SVG -o qrcode.svg "$DATA"

generate_qr_with_nodejs
import QRCode from 'qrcode';

const data = process.argv[2] || 'https://example.com';

async function main() {
  await QRCode.toFile('qrcode.png', data, {
    errorCorrectionLevel: 'M',
    margin: 2,
    width: 512
  });

  const svg = await QRCode.toString(data, { type: 'svg', margin: 2 });
  await import('node:fs/promises').then(fs => fs.writeFile('qrcode.svg', svg));

  const terminal = await QRCode.toString(data, { type: 'terminal' });
  console.log(terminal);
  console.log('Saved: qrcode.png, qrcode.svg');
}

main().catch(err => {
  console.error('QR generation failed:', err.message);
  process.exit(1);
});


Run:

node generate-qr.js "https://example.com/invoice/abc"

Agent prompt
You are generating QR codes locally without calling external QR APIs.
Use Bash (qrencode) for quick CLI generation or Node.js (qrcode package) for programmatic control.
Return:
1) command/code used,
2) output filenames (png/svg),
3) brief validation note (e.g., "scan test recommended").
If dependency is missing, provide the install command and retry.

Best practices
Keep payload concise for better scan reliability
Use at least error correction level M for general use
Export PNG for compatibility and SVG for scalable print/web usage
Validate with a scanner after generation
Troubleshooting
qrencode: command not found → install qrencode via package manager
Node import error → ensure npm install qrcode completed
Dense/unclear QR image → increase image size/box size and reduce payload length
See also
pdf-manipulation.md — combine generated QR images into documents
Weekly Installs
11
Repository
besoeasy/open-skills
GitHub Stars
111
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass