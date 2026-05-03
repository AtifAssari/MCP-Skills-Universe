---
rating: ⭐⭐
title: ieee-search-mcp
url: https://skills.sh/duruii/scientific-skills/ieee-search-mcp
---

# ieee-search-mcp

skills/duruii/scientific-skills/ieee-search-mcp
ieee-search-mcp
Installation
$ npx skills add https://github.com/duruii/scientific-skills --skill ieee-search-mcp
SKILL.md
ieee-search-mcp

Use this skill when user requires IEEE Xplore search through school library access (proxy/SSO session), not direct public IEEE entry.

Preconditions
Browser MCP (for example chrome-devtools or equivalent) is already installed and available.
The agent has permission to control a browser.
If either condition is missing, stop and explicitly say this workflow cannot be executed in-browser.
For relative time filters (for example "近2年"), use local time/date tool first and compute explicit year range before filtering.
School Profiles (pluggable)
Load school profile from assets/school_profiles.example.json.
If school is not provided, ask user first.
Treat these as pluggable fields per school:
library_home
proxy_ieee_home
db_keyword_candidates
Optional: known_database_detail_url
Demo/default profile is wust (Wuhan University of Science and Technology).
Common User Intent Paths
Path A: Login + Keyword search + recent years
Open library_home, verify login state.
If login required, ask user to complete SSO/QR and wait.
Search DB by db_keyword_candidates in order (for WUST try IEL before IEEE if needed).
Enter IEEE from library entry and verify institutional session.
Run keyword search.
Apply explicit year range (for example if current year is 2026, "近2年" means 2025-2026).
Return results using requested format.
Path B: Continue from existing proxy IEEE page
If user provides/opened proxy URL (for example metaersp-2.../ieeexplore/...), continue in the same page/session.
Do not open https://ieeexplore.ieee.org/ directly unless user confirms fallback.
Re-verify Access provided by: or proxy host before searching.
Path C: Advanced search / Journal search
Confirm mode with user (keyword / advanced / journal).
Ask for missing constraints (query fields, journal name, years, document type).
Execute search and return structured results.
Failure Branches From Real WUST Flow
DB alias mismatch: searching IEEE may fail, retry IEL.
Click timeout on DB row: refresh snapshot and retry once.
Still cannot click: navigate to known detail URL (known_database_detail_url) if profile has it.
Session drift: if jumped to public ieeexplore.ieee.org, immediately restore proxy route via proxy_ieee_home.
Page/tool argument error: re-check tool parameter type/naming before retry (for example pageId must be number).
Mandatory user checkpoints

Ask user instead of guessing at these points:

School or library profile not confirmed.
Login step requires human action (captcha/QR/2FA).
Multiple near-identical database entries appear and click target is ambiguous.
User requests conflicting constraints (for example "only proxy session" and "jump to public site").
Output schema not specified but user asks for "整理成表格/导出".
Optional CCF Post-Filter (with ccf-rank skill)

If user asks for "只要 CCF-A/CCF-B" or similar:

Collect venue/journal from IEEE results.
Use sibling skill script: node ../ccf-rank/scripts/query_ccf_rank.mjs "<venue or journal>" --top 3
Keep only rows matching requested rank (for example A).
In output, include both IEEE fields and CCF fields (type, rank, area).
Output Rules
Honor user-specified format first.
If user requests a table, output Markdown table with requested columns.
If user does not specify columns, default columns: title | year | venue/journal | authors | access_path | ieee_url | ccf_rank(optional).
Always include access_path so user can confirm proxy route is used.
For time-based filters, include explicit year range in response text.
Minimal run summary

For each run, report these 5 items:

Access path used (library_home -> db alias -> IEEE proxy page).
Institutional access preserved or not.
Query mode + query + filters.
Result list (or table).
Next action options (advanced search / journal search / CCF filter / open full text).
Weekly Installs
15
Repository
duruii/scientific-skills
First Seen
Mar 7, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn