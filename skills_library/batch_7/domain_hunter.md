---
title: domain-hunter
url: https://skills.sh/resciencelab/opc-skills/domain-hunter
---

# domain-hunter

skills/resciencelab/opc-skills/domain-hunter
domain-hunter
Installation
$ npx skills add https://github.com/resciencelab/opc-skills --skill domain-hunter
Summary

Find and purchase domain names at the best price with availability checks and registrar comparison.

Generates 5-10 creative, brandable domain suggestions based on project description, then verifies availability via WHOIS or registrar search before presenting options
Compares prices across major registrars (Spaceship, Cloudflare, Namecheap, Porkbun, Dynadot) and surfaces renewal costs alongside registration fees
Searches Twitter and Reddit for active promo codes from registrar accounts and domain communities
Highlights key registrar differences: Cloudflare's at-cost pricing, free WHOIS privacy availability, and premium TLD requirements like .ai's 2-year minimum registration
SKILL.md
Domain Hunter Skill

Help users find and purchase domain names at the best price.

Workflow
Step 1: Generate Domain Ideas & Check Availability

Based on the user's project description, generate 5-10 creative domain name suggestions.

Guidelines:

Keep names short (under 15 characters)
Make them memorable and brandable
Consider: {action}{noun}, {noun}{suffix}, {prefix}{keyword}
Common suffixes: app, io, hq, ly, ify, now, hub

CRITICAL: Always check availability before presenting domains to user!

Use one of these methods to verify availability:

Method 1: WHOIS check (most reliable)

# Check if domain is available via whois
whois {domain}.{tld} 2>/dev/null | grep -i "no match\|not found\|available\|no data found" && echo "AVAILABLE" || echo "TAKEN"


Method 2: Registrar search page Open the registrar's domain search in browser to verify:

open "https://www.spaceship.com/domains/?search={domain}.{tld}"


Method 3: Bulk check via Namecheap/Dynadot

https://www.namecheap.com/domains/registration/results/?domain={domain}
https://www.dynadot.com/domain/search?domain={domain}

IMPORTANT:

Only present domains that are confirmed AVAILABLE
Mark any uncertain domains with "(unverified)"
Present suggestions to user and wait for confirmation before proceeding
Ask user to pick their preferred options or provide feedback
Only move to Step 2 after user approves domain name(s)
Step 2: Compare Prices

Use WebSearch to find current prices:

WebSearch: "cheapest .{tld} domain registrar 2026 site:tld-list.com"
WebSearch: ".{tld} domain price comparison tldes.com"


Key price comparison sites:

tld-list.com/tld/{tld}
tldes.com/{tld}
domaintyper.com/{tld}-domain
Step 3: Find Promo Codes

Use Twitter skill to search registrar accounts:

cd <twitter_skill_directory>
python3 scripts/search_tweets.py "from:{registrar} promo code" --type Latest --limit 15
python3 scripts/search_tweets.py "{registrar} promo code coupon" --type Latest --limit 15


Use Reddit skill to search domain communities:

cd <reddit_skill_directory>
python3 scripts/search_posts.py "{registrar} promo code" --limit 15
python3 scripts/search_posts.py "{registrar} coupon discount" --subreddit Domains --limit 10


Major registrar Twitter handles:

@spaceship, @Dynadot, @Namecheap, @Porkbun, @namesilo, @Cloudflare
Step 4: Recommend

Present final recommendation in this format:

## Recommendation

**Domain:** example.ai
**Best Registrar:** Spaceship
**Price:** $68.98/year (2-year minimum = $137.96)
**Promo Code:** None available for .ai
**Purchase Link:** https://www.spaceship.com/

### Price Comparison
| Registrar | Year 1 | Renewal | 2-Year Total |
|-----------|--------|---------|--------------|
| Spaceship | $68.98 | $68.98  | $137.96      |
| Cloudflare| $70.00 | $70.00  | $140.00      |
| Porkbun   | $71.40 | $72.40  | $143.80      |

Important Notes
Premium TLDs (.ai, .io) rarely have promo codes - wholesale costs are too high
.ai domains require 2-year minimum registration
Cloudflare offers at-cost pricing with no markup
Renewal prices often differ from registration - always check both
WHOIS privacy is free at most registrars (Cloudflare, Namecheap, Porkbun)
References
references/registrars.md - Detailed registrar comparison
references/spaceship-api.md - Spaceship API for automated domain operations
Weekly Installs
1.2K
Repository
resciencelab/opc-skills
GitHub Stars
828
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn