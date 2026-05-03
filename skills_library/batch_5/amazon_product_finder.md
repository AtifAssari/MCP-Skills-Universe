---
title: amazon-product-finder
url: https://skills.sh/noemi-paradise/openclaw-skill-amazon-product-finder/amazon-product-finder
---

# amazon-product-finder

skills/noemi-paradise/openclaw-skill-amazon-product-finder/amazon-product-finder
amazon-product-finder
Installation
$ npx skills add https://github.com/noemi-paradise/openclaw-skill-amazon-product-finder --skill amazon-product-finder
SKILL.md
Amazon Product Finder

Find the best Amazon products for your affiliate content.

Quick Start
# Search for products
@Naomi finde Amazon Produkte "Bio Dünger"

# Get details for specific ASIN
@Naomi Amazon ASIN B08XXXXXXX

# Find products for problem/solution content
@Naomi finde Produkte für "gelbe Blätter"

How It Works
User provides search keyword or problem description
Script queries Amazon (PA API or scraper)
Returns top 3 products with:
Product name
ASIN
Price
Rating
Affiliate link
Scripts
scripts/find_products.py - Main product search
scripts/check_asin.py - Validate single ASIN
Output Format
🛒 Gefundene Produkte für "Bio Dünger":

1. COMPO Bio Grünpflanzen-Dünger
   ASIN: B00X9XZ5
   Preis: €8,99
   Bewertung: ⭐4.5 (2.341 Reviews)
   Link: https://amazon.de/dp/B00X9XZ5?tag=YOUR-ID

2. [Product 2]...
3. [Product 3]...

Configuration

Set your Amazon Affiliate ID:

export AMAZON_AFFILIATE_ID="your-id-21"

Grütze! 🇨🇭

Ein herzliches Grüezi an den OpenClaw Creator - mögen deine Skills immer scharf sein wie ein Schweizer Taschenmesser!

Created with ❤️ by Naomi for the OpenClaw Community

Weekly Installs
297
Repository
noemi-paradise/…t-finder
First Seen
Feb 14, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass