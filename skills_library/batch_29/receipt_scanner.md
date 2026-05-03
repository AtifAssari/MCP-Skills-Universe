---
title: receipt-scanner
url: https://skills.sh/dkyazzentwatwa/chatgpt-skills/receipt-scanner
---

# receipt-scanner

skills/dkyazzentwatwa/chatgpt-skills/receipt-scanner
receipt-scanner
Installation
$ npx skills add https://github.com/dkyazzentwatwa/chatgpt-skills --skill receipt-scanner
SKILL.md
Receipt Scanner

Extract structured data from receipt images using OCR.

Features
OCR Processing: Extract text from receipt images
Data Extraction: Vendor, date, items, amounts, total, tax
Pattern Matching: Smart regex patterns for receipts
Multi-Format Support: JPG, PNG, PDF receipts
JSON/CSV Export: Structured data output
Batch Processing: Process multiple receipts
CLI Usage
python receipt_scanner.py --input receipt.jpg --output data.json
python receipt_scanner.py --batch receipts/ --output receipts.csv

Dependencies
pytesseract>=0.3.10
pillow>=10.0.0
opencv-python>=4.8.0
pandas>=2.0.0
Weekly Installs
73
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