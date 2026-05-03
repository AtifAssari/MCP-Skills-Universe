---
rating: ⭐⭐
title: bambu-filament-tracker
url: https://skills.sh/mono0926/skills/bambu-filament-tracker
---

# bambu-filament-tracker

skills/mono0926/skills/bambu-filament-tracker
bambu-filament-tracker
Installation
$ npx skills add https://github.com/mono0926/skills --skill bambu-filament-tracker
SKILL.md
Bambu Lab Purchase Tracker

This skill automates the retrieval and summarization of Bambu Lab filament purchases by searching your Gmail history for order confirmations from bambulab.com, payment notifications from PayPal/PayPay, and relevant Amazon orders.

Capabilities
Search: Scans Gmail for keywords like "Bambu Lab", "filament", "JP" prefixed order numbers, and "Bambu Japan".
Extract: Parses order dates, items, quantities, and total spent from email snippets and bodies.
Summarize: Generates a clean table or list of purchases with a grand total.
Usage

Run the tracking script to see your purchase history:

dart bambu-filament-tracker/scripts/tracker.dart

Tool Dependencies
gws: Used to access Gmail messages and threads.
Permissions
Requires https://www.googleapis.com/auth/gmail.readonly or similar access provided by the gws tool configuration.
Weekly Installs
37
Repository
mono0926/skills
GitHub Stars
1
First Seen
Mar 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn