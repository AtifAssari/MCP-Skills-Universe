---
rating: ⭐⭐
title: amazon-fba-calculator
url: https://skills.sh/nexscope-ai/amazon-skills/amazon-fba-calculator
---

# amazon-fba-calculator

skills/nexscope-ai/amazon-skills/amazon-fba-calculator
amazon-fba-calculator
Installation
$ npx skills add https://github.com/nexscope-ai/amazon-skills --skill amazon-fba-calculator
SKILL.md
Amazon FBA Calculator (Lite)

Precise FBA fee calculation based on product dimensions and weight.

Features
Size Tier Detection - Automatic classification
FBA Fulfillment Fee - 2024 rates
Monthly Storage Fee - Standard & Peak season
Long-term Storage Fee - 271+ days aging
Referral Fee - By category
Profit Analysis - Gross/Net margin, ROI
Optimization Tips - Size, weight, inventory
Size Tiers (2024)
Tier	Max Weight	Max Dimensions
Small Standard	1 lb	15"×12"×0.75"
Large Standard	20 lb	18"×14"×8"
Small Oversize	70 lb	60"×30"
Medium Oversize	150 lb	L+Girth ≤108"
Large Oversize	150 lb	L+Girth ≤165"
Special Oversize	>150 lb	>165"
Input
{
  "length": 10.0,
  "width": 6.0,
  "height": 3.0,
  "weight": 1.2,
  "selling_price": 29.99,
  "product_cost": 8.00,
  "inbound_shipping_cost": 1.50,
  "category": "kitchen"
}

Output
Size tier classification
Fee breakdown table
Profit metrics (margin, ROI)
Optimization suggestions
Usage
python3 scripts/calculator.py
python3 scripts/calculator.py '{"length": 10, "width": 6, ...}' --zh


Version 1.0.0 | Platform: Amazon | Variant: Lite

Part of Nexscope AI — AI tools for e-commerce sellers.

Weekly Installs
83
Repository
nexscope-ai/ama…n-skills
GitHub Stars
143
First Seen
Mar 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass