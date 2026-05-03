---
rating: ⭐⭐⭐
title: amazon-shopping
url: https://skills.sh/jlave-dev/agent-skills/amazon-shopping
---

# amazon-shopping

skills/jlave-dev/agent-skills/amazon-shopping
amazon-shopping
Installation
$ npx skills add https://github.com/jlave-dev/agent-skills --skill amazon-shopping
SKILL.md
Amazon Shopping

Search Amazon and recommend products based on user preferences.

MANDATORY FIRST STEP - REQUIREMENTS GATHERING

YOU MUST ASK CLARIFYING QUESTIONS BEFORE ANY BROWSER AUTOMATION.

DO NOT proceed to search until you understand:

Budget: Price range they're comfortable with
Usage: Who/what it's for (personal, gift, professional)
Deal-breakers: Features they must have or avoid

Use AskUserQuestion to gather this information. Only after receiving answers should you proceed to Step 2.

Example questions for any product:

Budget range (under $25, $25-50, $50-100, $100+)
Primary use case (personal, gift, professional)
Key preferences (brand, features, quality vs value)
Quick Start (After Requirements Gathered)
Gather requirements: Ask about budget, usage, deal-breakers → DONE in mandatory step above
Search Amazon: Navigate to search results and capture snapshot
Extract data: Identify products with ASINs, prices, ratings, review counts
Verify: Visit product pages to confirm accuracy
Present recommendations: Ranked by user's criteria
Prerequisites
Chrome DevTools MCP server connected
Internet access to Amazon.com
Search Workflow
Step 1: Navigate to Amazon Search Results

Go directly to the search URL (simplest approach):

navigate_page type="url" url="https://www.amazon.com/s?k=<encoded search query>"


Alternative - Interactive search (if direct URL doesn't work):

Navigate to https://www.amazon.com
take_snapshot to find the search box UID
fill the search box with your query
click the search button or press_key with key="Enter"
Step 2: Capture Results
take_snapshot


The snapshot returns the full accessibility tree with UIDs for every element. Each element includes its role, name, and URL where applicable.

Step 3: Extract Products WITH Their ASINs

CRITICAL: Extract product names AND their ASINs from THE SAME container element to prevent mismatches.

In the accessibility tree, each product is typically a listitem containing:

A heading with the product name
A link with the ASIN in the URL (e.g., /dp/B0XXXXXXXXX)

Read the snapshot and pair each heading with the link in the same container. Use the UID hierarchy and indentation to identify which elements belong to the same product.

WRONG - Causes ASIN/Product Mismatches:

Extracting all ASINs separately and pairing them with product names
Amazon pages contain ASINs for ads, sponsored products, and footer links that will mix with real results
Step 4: MANDATORY Product Page Verification

For EVERY product before presenting it to the user, you MUST verify by visiting its actual product page.

For each product:

navigate_page to https://www.amazon.com/dp/<ASIN>
take_snapshot to read the page content
Verify:
Title matches the product you're recommending
Price is current from the product page (for example Buy new: $XX.XX, One-time purchase: $XX.XX, or the main price block)
Rating and review count are present

MANDATORY VERIFICATION RULES:

If ASIN redirects to different product → DISCARD
If page title doesn't match expected product → DISCARD
If price cannot be found → DISCARD
Only present VERIFIED products with a checkmark

NEVER extract prices from search results pages - they often don't match actual product page prices due to variants, promotions, or different sellers.

See reference/asin-extraction.md for detailed patterns.

Common Issues
Issue	Solution
CAPTCHA	Wait 60s, retry from amazon.com
Rate limited	Wait 2-3 min
No results	Broaden search
Slow page load	Use wait_for with expected visible text, then retake take_snapshot

See reference/common-errors.md for complete troubleshooting.

Output Format

ALL presented products MUST be verified on their actual product pages.

## Amazon Shortlist - [Category]

### 1. [Product] - $XX.XX (verified)
**ASIN**: [ASIN]
**Rating**: X.X/5 (X,XXX reviews)
**Amazon**: https://www.amazon.com/dp/[ASIN]
**Why this**: [Reason]
**Key specs**: [Specs]


Do NOT present unverified products. The verified marker confirms that:

The ASIN link goes to the actual product (not a redirect)
The price is current from the product page
The title matches what was recommended

See reference/output-formats.md for templates.

Ranking Priority

When ratings are similar (within 0.5), prioritize review count.

Example: 4.0 with 10,000 reviews > 5.0 with 100 reviews

Weekly Installs
65
Repository
jlave-dev/agent-skills
GitHub Stars
1
First Seen
Feb 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn