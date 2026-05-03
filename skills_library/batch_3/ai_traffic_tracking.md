---
title: ai-traffic-tracking
url: https://skills.sh/kostja94/marketing-skills/ai-traffic-tracking
---

# ai-traffic-tracking

skills/kostja94/marketing-skills/ai-traffic-tracking
ai-traffic-tracking
Installation
$ npx skills add https://github.com/kostja94/marketing-skills --skill ai-traffic-tracking
SKILL.md
Analytics: AI Traffic

Guides tracking of AI-driven search traffic in Google Analytics 4 and Google Search Console.

When invoking: On first use, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On subsequent use or when the user asks to skip, go directly to the main output.

Scope
AI search traffic: Track in GA4 and GSC; separate AI sources from organic referral
Google AI Overviews: AI summary box in Google search (formerly SGE)
AI-driven search: Traffic from ChatGPT, Perplexity, Gemini, Claude, Copilot, etc.
Why Track Separately
AI traffic is growing but GA4 often groups it as Referral, Organic, or Direct
AI visitors may have stronger intent and higher conversion
Separating AI Overviews from organic helps assess AI impact
GA4: AI-Driven Search
Option 1: Exploration Report (Recommended)
Explore →Free form
Dimensions: Session source (or Session source / medium)
Metrics: Sessions, Engagement rate, Event count, etc.
Filters: Add filter →Session source Matches regex →use regex below
Configure table, save report

Regex (common AI sources):

chatgpt\.com|openai\.com|openai|perplexity\.ai|perplexity|doubao\.com|chat\.qwen\.ai|copilot\.microsoft\.com|copilot\.com|(business\.)?gemini\.google|chat\.deepseek\.com|deepseek\.com|poe\.com|anthropic\.com|claude\.ai|bard\.google\.com|edgeservices\.bing\.com

Option 2: Custom Channel Group
Admin →Data Display →Channel Groups
Copy default group, name e.g. "Default and AI Chatbots"
Add channel "AI Chatbots": Source Matches regex (same regex)
Important: Place "AI Chatbots" above "Referral" so it matches first
Save and use in Traffic Acquisition
Option 3: Custom Report
Reports →Library →Create Detail Report
Use Traffic Acquisition template
Add filter: Session source Matches regex (same regex)
Save and add to menu
Common AI Source Domains
Platform	GA4 Source examples
ChatGPT	chatgpt.com, openai
Perplexity	perplexity.ai, perplexity
Copilot	copilot.com, copilot.microsoft.com
Gemini	business.gemini.google, gemini.google
Claude	claude.ai, anthropic.com
Bing Chat	edgeservices.bing.com
Google AI Overviews
GA4 + URL fragment: Some AI Overview clicks add URL fragments; can use GTM (partial coverage)
GSC: For AI Overviews analysis in GSC (filter, limitations), see google-search-console
Checklist
 AI sources identified in GA4 (Session Source)
 AI traffic Exploration report created
 Channel group updated with AI above Referral (if used)
 Custom report added to Library (optional)
 GTM + URL fragment for AI Overviews (optional)
 GSC AI-oriented query filter (optional; see google-search-console)
Output Format
GA4 setup: Exploration, channel group, or custom report
Regex: Adapted to user's observed sources
Related Skills
generative-engine-optimization: GEO strategy; AI traffic tracking measures GEO impact
traffic-analysis: Traffic sources, attribution, UTM
analytics-tracking: GA4 events and conversions
google-search-console: GSC AI traffic analysis
robots-txt: AI crawler allow/block strategy
Weekly Installs
540
Repository
kostja94/market…g-skills
GitHub Stars
413
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass