---
title: batch-qr-generator
url: https://skills.sh/dkyazzentwatwa/chatgpt-skills/batch-qr-generator
---

# batch-qr-generator

skills/dkyazzentwatwa/chatgpt-skills/batch-qr-generator
batch-qr-generator
Installation
$ npx skills add https://github.com/dkyazzentwatwa/chatgpt-skills --skill batch-qr-generator
SKILL.md
Batch QR Generator

Generate bulk QR codes from CSV data with UTM tracking, logos, and customizable styling for events, products, and marketing.

Purpose

Bulk QR code generation for:

Event ticketing and check-in
Product inventory tracking
Marketing campaign tracking (UTM parameters)
Business card contact sharing
Bulk URL shortening with QR codes
Features
CSV Input: Generate from spreadsheet data
UTM Tracking: Auto-add campaign tracking parameters
Custom Styling: Colors, logos, error correction
Sequential Naming: Auto-generate filenames
Metadata Export: CSV with QR data and filenames
Format Options: PNG, SVG output
Quick Start
from batch_qr_generator import BatchQRGenerator

# Generate from CSV
generator = BatchQRGenerator()
generator.load_csv('products.csv', url_column='product_url')
generator.add_utm_params(source='catalog', medium='qr', campaign='2024Q1')
generator.generate_batch(output_dir='qr_codes/')

CLI Usage
# Generate QR codes from CSV
python batch_qr_generator.py --csv products.csv --url-column url --output-dir qr_codes/

# Add UTM tracking
python batch_qr_generator.py --csv products.csv --url-column url --utm-source catalog --utm-campaign 2024Q1 --output-dir qr_codes/

# Add logo
python batch_qr_generator.py --csv urls.csv --url-column link --logo logo.png --output-dir branded_qr/

Weekly Installs
56
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