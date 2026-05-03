---
rating: ⭐⭐
title: pdf4me
url: https://skills.sh/vm0-ai/vm0-skills/pdf4me
---

# pdf4me

skills/vm0-ai/vm0-skills/pdf4me
pdf4me
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill pdf4me
SKILL.md
Troubleshooting

If requests fail, run zero doctor check-connector --env-name PDF4ME_TOKEN or zero doctor check-connector --url https://api.pdf4me.com/api/v2/ConvertToPdf --method POST

How to Use
1. Convert to PDF

Convert Word, Excel, PowerPoint, images to PDF:

# Convert a text file to PDF
echo "Hello, PDF4ME!" > /tmp/test.txt
BASE64_CONTENT=$(base64 < /tmp/test.txt)


Write to /tmp/pdf4me_request.json:

{
  "docContent": "${BASE64_CONTENT}",
  "docName": "test.txt"
}


Then run:

curl -s -X POST "https://api.pdf4me.com/api/v2/ConvertToPdf" --header "Authorization: $PDF4ME_TOKEN" --header "Content-Type: application/json" -d @/tmp/pdf4me_request.json | jq -r '.docContent' | base64 -d > /tmp/output.pdf

2. HTML to PDF

Convert HTML content to PDF:

HTML_CONTENT=$(echo '<html><body><h1>Hello World</h1><p>This is a test.</p></body></html>' | base64)


Write to /tmp/pdf4me_request.json:

{
  "docContent": "${HTML_CONTENT}",
  "docName": "test.html",
  "layout": "Portrait",
  "format": "A4"
}


Then run:

curl -s -X POST "https://api.pdf4me.com/api/v2/ConvertHtmlToPdf" --header "Authorization: $PDF4ME_TOKEN" --header "Content-Type: application/json" -d @/tmp/pdf4me_request.json --output /tmp/from-html.pdf

3. URL to PDF

Convert a webpage to PDF:

Write to /tmp/pdf4me_request.json:

{
  "webUrl": "https://example.com"
}


Then run:

curl -s -X POST "https://api.pdf4me.com/api/v2/ConvertUrlToPdf" --header "Authorization: $PDF4ME_TOKEN" --header "Content-Type: application/json" -d @/tmp/pdf4me_request.json > /tmp/webpage.pdf

4. Merge PDFs

Combine multiple PDFs into one:

PDF1_BASE64=$(base64 < file1.pdf)
PDF2_BASE64=$(base64 < file2.pdf)


Write to /tmp/pdf4me_request.json:

{
  "docContent": ["${PDF1_BASE64}", "${PDF2_BASE64}"],
  "docName": "merged.pdf"
}


Then run:

curl -s -X POST "https://api.pdf4me.com/api/v2/Merge" --header "Authorization: $PDF4ME_TOKEN" --header "Content-Type: application/json" -d @/tmp/pdf4me_request.json | jq -r '.docContent' | base64 -d > merged.pdf

5. Split PDF

Split PDF by page ranges:

PDF_BASE64=$(base64 < input.pdf)


Write to /tmp/pdf4me_request.json:

{
  "docContent": "${PDF_BASE64}",
  "docName": "input.pdf",
  "splitAction": "splitAfterPage",
  "splitAfterPage": 2
}


Then run:

curl -s -X POST "https://api.pdf4me.com/api/v2/Split" --header "Authorization: $PDF4ME_TOKEN" --header "Content-Type: application/json" -d @/tmp/pdf4me_request.json

6. Compress PDF

Reduce PDF file size:

PDF_BASE64=$(base64 < large.pdf)


Write to /tmp/pdf4me_request.json:

{
  "docContent": "${PDF_BASE64}",
  "docName": "large.pdf"
}


Then run:

curl -s -X POST "https://api.pdf4me.com/api/v2/Compress" --header "Authorization: $PDF4ME_TOKEN" --header "Content-Type: application/json" -d @/tmp/pdf4me_request.json | jq -r '.docContent' | base64 -d > compressed.pdf

7. PDF to Word

Convert PDF to editable Word document:

PDF_BASE64=$(base64 < input.pdf)


Write to /tmp/pdf4me_request.json:

{
  "docContent": "${PDF_BASE64}",
  "docName": "input.pdf"
}


Then run:

curl -s -X POST "https://api.pdf4me.com/api/v2/PdfToWord" --header "Authorization: $PDF4ME_TOKEN" --header "Content-Type: application/json" -d @/tmp/pdf4me_request.json | jq -r '.docContent' | base64 -d > output.docx

8. PDF to Images

Create thumbnails/images from PDF pages:

PDF_BASE64=$(base64 < input.pdf)


Write to /tmp/pdf4me_request.json:

{
  "docContent": "${PDF_BASE64}",
  "docName": "input.pdf",
  "imageFormat": "png",
  "width": 800
}


Then run:

curl -s -X POST "https://api.pdf4me.com/api/v2/CreateThumbnail" --header "Authorization: $PDF4ME_TOKEN" --header "Content-Type: application/json" -d @/tmp/pdf4me_request.json

9. Add Text Stamp/Watermark

Add text watermark to PDF:

PDF_BASE64=$(base64 < input.pdf)


Write to /tmp/pdf4me_request.json:

{
  "docContent": "${PDF_BASE64}",
  "docName": "input.pdf",
  "stampText": "CONFIDENTIAL",
  "pages": "all",
  "alignX": "center",
  "alignY": "middle",
  "alpha": 0.3
}


Then run:

curl -s -X POST "https://api.pdf4me.com/api/v2/TextStamp" --header "Authorization: $PDF4ME_TOKEN" --header "Content-Type: application/json" -d @/tmp/pdf4me_request.json | jq -r '.docContent' | base64 -d > stamped.pdf

10. OCR - Extract Text from Scanned PDF

Make scanned PDFs searchable:

PDF_BASE64=$(base64 < scanned.pdf)


Write to /tmp/pdf4me_request.json:

{
  "docContent": "${PDF_BASE64}",
  "docName": "scanned.pdf",
  "ocrLanguage": "eng"
}


Then run:

curl -s -X POST "https://api.pdf4me.com/api/v2/PdfOcr" --header "Authorization: $PDF4ME_TOKEN" --header "Content-Type: application/json" -d @/tmp/pdf4me_request.json | jq -r '.docContent' | base64 -d > searchable.pdf

11. Protect PDF with Password
PDF_BASE64=$(base64 < input.pdf)


Write to /tmp/pdf4me_request.json:

{
  "docContent": "${PDF_BASE64}",
  "docName": "input.pdf",
  "password": "secret123"
}


Then run:

curl -s -X POST "https://api.pdf4me.com/api/v2/ProtectDocument" --header "Authorization: $PDF4ME_TOKEN" --header "Content-Type: application/json" -d @/tmp/pdf4me_request.json | jq -r '.docContent' | base64 -d > protected.pdf

12. Extract Pages

Extract specific pages from PDF:

PDF_BASE64=$(base64 < input.pdf)


Write to /tmp/pdf4me_request.json:

{
  "docContent": "${PDF_BASE64}",
  "docName": "input.pdf",
  "pageNrs": [1, 3, 5]
}


Then run:

curl -s -X POST "https://api.pdf4me.com/api/v2/ExtractPages" --header "Authorization: $PDF4ME_TOKEN" --header "Content-Type: application/json" -d @/tmp/pdf4me_request.json | jq -r '.docContent' | base64 -d > extracted.pdf

API Endpoints
Category	Endpoint	Description
Convert	/api/v2/ConvertToPdf	Word/Excel/PPT/Image → PDF
	/api/v2/ConvertHtmlToPdf	HTML → PDF
	/api/v2/UrlToPdf	URL → PDF
	/api/v2/MarkdownToPdf	Markdown → PDF
	/api/v2/PdfToWord	PDF → Word
	/api/v2/PdfToExcel	PDF → Excel
	/api/v2/PdfToPowerpoint	PDF → PowerPoint
Merge/Split	/api/v2/Merge	Merge multiple PDFs
	/api/v2/Split	Split PDF
	/api/v2/ExtractPages	Extract specific pages
Optimize	/api/v2/Compress	Compress PDF
	/api/v2/Linearize	Optimize for web
Edit	/api/v2/TextStamp	Add text watermark
	/api/v2/ImageStamp	Add image watermark
	/api/v2/AddPageNumber	Add page numbers
	/api/v2/Rotate	Rotate pages
Extract	/api/v2/CreateThumbnail	PDF → Images
	/api/v2/ExtractResources	Extract images/fonts
	/api/v2/ExtractTable	Extract tables
OCR	/api/v2/PdfOcr	OCR scanned PDFs
Security	/api/v2/ProtectDocument	Password protect
	/api/v2/UnlockPdf	Remove password
Forms	/api/v2/FillPdfForm	Fill form fields
	/api/v2/ExtractFormData	Extract form data
Barcode	/api/v2/CreateBarcode	Generate barcode
	/api/v2/AddBarcodeToPdf	Add barcode to PDF
	/api/v2/ReadBarcodeFromPdf	Read barcode from PDF
Request Format

All endpoints use POST with JSON body:

Write to /tmp/pdf4me_request.json:

{
  "docContent": "base64-encoded-file",
  "docName": "filename.ext",
  "...other parameters": "..."
}


Then run:

curl -s -X POST "https://api.pdf4me.com/api/v2/{endpoint}" --header "Authorization: $PDF4ME_TOKEN" --header "Content-Type: application/json" -d @/tmp/pdf4me_request.json

Response Format
{
  "docContent": "base64-encoded-result",
  "docName": "output.pdf",
  "pageCount": 5
}

Guidelines
File Size: Max 20MB per file (varies by plan)
Base64: All file content must be base64 encoded
Formats: Supports PDF, Word, Excel, PowerPoint, HTML, images
OCR Languages: eng, deu, fra, spa, ita, por, etc.
Rate Limits: Check your plan at https://dev.pdf4me.com/pricing/
Free Tier: 50 API calls/month
Postman: Import from https://dev.pdf4me.com/apiv2/documentation/postman/
Resources
API Docs: https://dev.pdf4me.com/apiv2/documentation/
Code Samples: https://github.com/pdf4me/pdf4me-api-samples
Postman Collection: https://dev.pdf4me.com/apiv2/documentation/postman/
Dashboard: https://dev.pdf4me.com/dashboard/
Weekly Installs
106
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn