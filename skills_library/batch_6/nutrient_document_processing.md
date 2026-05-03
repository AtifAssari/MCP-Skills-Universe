---
title: nutrient-document-processing
url: https://skills.sh/affaan-m/everything-claude-code/nutrient-document-processing
---

# nutrient-document-processing

skills/affaan-m/everything-claude-code/nutrient-document-processing
nutrient-document-processing
Installation
$ npx skills add https://github.com/affaan-m/everything-claude-code --skill nutrient-document-processing
Summary

Document conversion, extraction, OCR, redaction, signing, and form-filling via the Nutrient DWS API.

Converts between 15+ formats including PDF, DOCX, XLSX, PPTX, HTML, and images (JPG, PNG, TIFF, WebP, SVG, and more)
Extracts plain text and tables from documents; OCR supports 100+ languages for scanned PDFs and images
Redacts PII using preset patterns (SSN, email, credit card, phone, date, URL, IP, MAC address, ZIP code, VIN) or custom regex
Adds watermarks, applies digital CMS signatures, and fills PDF form fields programmatically
Available as REST API or MCP server for native tool integration
SKILL.md
Nutrient Document Processing

Note: This skill integrates with the Nutrient commercial API. Review their terms before use.

Process documents with the Nutrient DWS Processor API. Convert formats, extract text and tables, OCR scanned documents, redact PII, add watermarks, digitally sign, and fill PDF forms.

Setup

Get a free API key at nutrient.io

export NUTRIENT_API_KEY="pdf_live_..."


All requests go to https://api.nutrient.io/build as multipart POST with an instructions JSON field.

Operations
Convert Documents
# DOCX to PDF
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F "document.docx=@document.docx" \
  -F 'instructions={"parts":[{"file":"document.docx"}]}' \
  -o output.pdf

# PDF to DOCX
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F "document.pdf=@document.pdf" \
  -F 'instructions={"parts":[{"file":"document.pdf"}],"output":{"type":"docx"}}' \
  -o output.docx

# HTML to PDF
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F "index.html=@index.html" \
  -F 'instructions={"parts":[{"html":"index.html"}]}' \
  -o output.pdf


Supported inputs: PDF, DOCX, XLSX, PPTX, DOC, XLS, PPT, PPS, PPSX, ODT, RTF, HTML, JPG, PNG, TIFF, HEIC, GIF, WebP, SVG, TGA, EPS.

Extract Text and Data
# Extract plain text
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F "document.pdf=@document.pdf" \
  -F 'instructions={"parts":[{"file":"document.pdf"}],"output":{"type":"text"}}' \
  -o output.txt

# Extract tables as Excel
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F "document.pdf=@document.pdf" \
  -F 'instructions={"parts":[{"file":"document.pdf"}],"output":{"type":"xlsx"}}' \
  -o tables.xlsx

OCR Scanned Documents
# OCR to searchable PDF (supports 100+ languages)
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F "scanned.pdf=@scanned.pdf" \
  -F 'instructions={"parts":[{"file":"scanned.pdf"}],"actions":[{"type":"ocr","language":"english"}]}' \
  -o searchable.pdf


Languages: Supports 100+ languages via ISO 639-2 codes (e.g., eng, deu, fra, spa, jpn, kor, chi_sim, chi_tra, ara, hin, rus). Full language names like english or german also work. See the complete OCR language table for all supported codes.

Redact Sensitive Information
# Pattern-based (SSN, email)
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F "document.pdf=@document.pdf" \
  -F 'instructions={"parts":[{"file":"document.pdf"}],"actions":[{"type":"redaction","strategy":"preset","strategyOptions":{"preset":"social-security-number"}},{"type":"redaction","strategy":"preset","strategyOptions":{"preset":"email-address"}}]}' \
  -o redacted.pdf

# Regex-based
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F "document.pdf=@document.pdf" \
  -F 'instructions={"parts":[{"file":"document.pdf"}],"actions":[{"type":"redaction","strategy":"regex","strategyOptions":{"regex":"\\b[A-Z]{2}\\d{6}\\b"}}]}' \
  -o redacted.pdf


Presets: social-security-number, email-address, credit-card-number, international-phone-number, north-american-phone-number, date, time, url, ipv4, ipv6, mac-address, us-zip-code, vin.

Add Watermarks
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F "document.pdf=@document.pdf" \
  -F 'instructions={"parts":[{"file":"document.pdf"}],"actions":[{"type":"watermark","text":"CONFIDENTIAL","fontSize":72,"opacity":0.3,"rotation":-45}]}' \
  -o watermarked.pdf

Digital Signatures
# Self-signed CMS signature
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F "document.pdf=@document.pdf" \
  -F 'instructions={"parts":[{"file":"document.pdf"}],"actions":[{"type":"sign","signatureType":"cms"}]}' \
  -o signed.pdf

Fill PDF Forms
curl -X POST https://api.nutrient.io/build \
  -H "Authorization: Bearer $NUTRIENT_API_KEY" \
  -F "form.pdf=@form.pdf" \
  -F 'instructions={"parts":[{"file":"form.pdf"}],"actions":[{"type":"fillForm","formFields":{"name":"Jane Smith","email":"jane@example.com","date":"2026-02-06"}}]}' \
  -o filled.pdf

MCP Server (Alternative)

For native tool integration, use the MCP server instead of curl:

{
  "mcpServers": {
    "nutrient-dws": {
      "command": "npx",
      "args": ["-y", "@nutrient-sdk/dws-mcp-server"],
      "env": {
        "NUTRIENT_DWS_API_KEY": "YOUR_API_KEY",
        "SANDBOX_PATH": "/path/to/working/directory"
      }
    }
  }
}

When to Use
Converting documents between formats (PDF, DOCX, XLSX, PPTX, HTML, images)
Extracting text, tables, or key-value pairs from PDFs
OCR on scanned documents or images
Redacting PII before sharing documents
Adding watermarks to drafts or confidential documents
Digitally signing contracts or agreements
Filling PDF forms programmatically
Links
API Playground
Full API Docs
npm MCP Server
Weekly Installs
3.2K
Repository
affaan-m/everyt…ude-code
GitHub Stars
171.6K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass