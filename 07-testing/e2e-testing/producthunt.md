---
title: producthunt
url: https://skills.sh/manojbajaj95/gtm-skills/producthunt
---

# producthunt

skills/manojbajaj95/gtm-skills/producthunt
producthunt
Installation
$ npx skills add https://github.com/manojbajaj95/gtm-skills --skill producthunt
SKILL.md
Product Hunt Skill
Overview

Automates Product Hunt operations including discovering products, upvoting, commenting, and tracking launches through browser automation.

Quick Install
curl -sSL https://canifi.com/skills/producthunt/install.sh | bash


Or manually:

cp -r skills/producthunt ~/.canifi/skills/

Setup

Configure via canifi-env:

# First, ensure canifi-env is installed:
# curl -sSL https://canifi.com/install.sh | bash

canifi-env set PRODUCTHUNT_EMAIL "your-email@example.com"
canifi-env set PRODUCTHUNT_PASSWORD "your-password"

Privacy & Authentication

Your credentials, your choice. Canifi LifeOS respects your privacy.

Option 1: Manual Browser Login (Recommended)

If you prefer not to share credentials with Claude Code:

Complete the Browser Automation Setup using CDP mode
Login to the service manually in the Playwright-controlled Chrome window
Claude will use your authenticated session without ever seeing your password
Option 2: Environment Variables

If you're comfortable sharing credentials, you can store them locally:

canifi-env set SERVICE_EMAIL "your-email"
canifi-env set SERVICE_PASSWORD "your-password"


Note: Credentials stored in canifi-env are only accessible locally on your machine and are never transmitted.

Capabilities
Browse daily product launches
Upvote products
Comment on launches
Follow makers and topics
Search products
View collections
Access upcoming launches
Track product rankings
Usage Examples
Example 1: Browse Today's Products
User: "Show me today's top products on Product Hunt"
Claude: I'll check today's launches.
- Navigate to producthunt.com
- View today's products
- Sort by upvotes
- Present top launches

Example 2: Upvote Product
User: "Upvote that new AI tool on Product Hunt"
Claude: I'll upvote that product.
- Find the product listing
- Click upvote button
- Confirm upvote registered
- Note current ranking

Example 3: Comment on Launch
User: "Leave a supportive comment on this launch"
Claude: I'll add that comment.
- Navigate to product page
- Click comment section
- Write supportive message
- Post comment

Example 4: Search Products
User: "Find productivity tools on Product Hunt"
Claude: I'll search for those.
- Navigate to search
- Search "productivity"
- Filter by category
- Present top results

Authentication Flow
Navigate to producthunt.com via Playwright MCP
Click login and select email option
Enter email and password from canifi-env
Handle 2FA if enabled (notify user via iMessage)
Verify feed access
Maintain session cookies
Error Handling
Login Failed: Clear cookies, verify credentials
Session Expired: Re-authenticate automatically
2FA Required: iMessage for verification code
Already Upvoted: Cannot upvote twice
Rate Limited: Wait before continuing
Product Not Found: Search with alternative terms
Comment Failed: Check community guidelines
Launch Not Live: Product may be scheduled
Self-Improvement Instructions

When encountering new Product Hunt features:

Document new UI elements
Add support for new interaction types
Log successful engagement patterns
Update for platform changes
Notes
Daily product rankings reset at midnight PT
Upvotes from accounts with history carry more weight
Makers can answer comments
Collections curate themed products
Golden Kitty Awards annual event
Upcoming section for pre-launch products
Maker profiles build credibility
Weekly Installs
9
Repository
manojbajaj95/gtm-skills
GitHub Stars
40
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubFail
SocketFail
SnykFail