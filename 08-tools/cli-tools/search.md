---
title: search
url: https://skills.sh/site/cbskills.xcloudzen.com/search
---

# search

skills/cbskills.xcloudzen.com/search
search
$ npx skills add https://cbskills.xcloudzen.com
SKILL.md
Search — Run a Query, Return Structured Results

For any task that needs "the top N results for X." Read chrome-bridge first.

Why not a search API

The chrome-bridge gives you a real logged-in Chrome session with full cookies, so queries return personalized / region-appropriate results and aren't rate-limited the way a raw API key would be. No API signup, no tokens.

How this skill is laid out

Each capability has a focused JS file under scripts/. To use one:

Read the script file to load it as a string.
Pass the contents as the code argument to mcp__chrome-bridge__execute_script.
The script returns a structured object — the header comment at the top of each file documents pre-conditions and return shape.
Capability map
Task	Pre-condition	Script	Notes
Google SERP — primary extractor	navigate('https://www.google.com/search?q=' + encodeURIComponent(query)) + 3s	scripts/google_results.js	Returns up to 10 { title, url, snippet }. Snippet may be empty for text-fragment cards — fall back to the next row.
Google SERP — text-fragment fallback	same as above, used when primary returns empty snippets	scripts/google_results_fallback.js	Reconstructs snippet from card.innerText minus title.
EU consent wall click-through	location.href contains consent.google.com	scripts/consent_click.js	Prefers "Reject all". Try dom_click('button[aria-label*="Reject all" i]') first; fall through to this script if that fails.
DuckDuckGo HTML — fast fallback	navigate('https://html.duckduckgo.com/html/?q=' + encodeURIComponent(query)) + 2s	scripts/ddg_results.js	URLs are wrapped through //duckduckgo.com/l/?uddg=... — use the decode variant if you need real URLs.
DuckDuckGo HTML — with URL decode	same as above	scripts/ddg_results_decode.js	Same shape as ddg_results.js but decodes uddg to the real destination.
Bing SERP	navigate('https://www.bing.com/search?q=' + encodeURIComponent(query)) + 3s	scripts/bing_results.js	Last-resort fallback when Google + DuckDuckGo both fail.
Workflow
Primary: Google
navigate(url='https://www.google.com/search?q=' + urlencode(query))
# wait ~3s

# Detect & clear EU consent wall if present:
u = execute_script(code="(()=>location.href)()")
if 'consent.google.com' in u:
    dom_click('button[aria-label*="Reject all" i]')   # try the dedicated button first
    # fall through to the text-matching script if that did nothing:
    execute_script(code=<contents of scripts/consent_click.js>)
    # wait ~3s for redirect back to /search

results = execute_script(code=<contents of scripts/google_results.js>)
# If any result has empty snippet and you need them all populated:
results = execute_script(code=<contents of scripts/google_results_fallback.js>)


If Google's primary extractor still returns empty:

Fall back to page_markdown and pick out result-looking links heuristically
Fall back to DuckDuckGo (below)
Google search operators

Pass operators in the query string:

site:example.com — restrict to a domain
filetype:pdf — restrict to a file type
"exact phrase" — exact match
after:2025-01-01 — recency filter
-word — exclude a term
Fallback: DuckDuckGo HTML endpoint

Useful when Google shows CAPTCHA, consent loops, or you need a no-JS path:

navigate(url='https://html.duckduckgo.com/html/?q=' + urlencode(query))
# wait ~2s
results = execute_script(code=<contents of scripts/ddg_results.js>)
# Or if you need real URLs (not the //duckduckgo.com/l/?uddg= wrapper):
results = execute_script(code=<contents of scripts/ddg_results_decode.js>)

Fallback: Bing
navigate(url='https://www.bing.com/search?q=' + urlencode(query))
# wait ~3s
results = execute_script(code=<contents of scripts/bing_results.js>)

Specialty searches
Academic: https://scholar.google.com/scholar?q=... — results under .gs_ri, title at .gs_rt a, metadata at .gs_a, snippet at .gs_rs.
News: https://news.google.com/search?q=... — SPA, may need 5+ seconds to render.
Images: https://www.google.com/search?q=...&tbm=isch — extract img[src^="http"] with alt text.
Return shape
[
  { "title": "...", "url": "https://...", "snippet": "..." }
]


Always include a snippet even if short — it's what lets the caller rank without re-fetching.

Common failures
Signal	Cause	Fix
Empty results from Google	DOM changed, or consent wall blocking	Run the fallback extractor; handle consent; fall back to DuckDuckGo
CAPTCHA on Google	Detected automation	Stop and tell the user — never bypass
Results have title but no url	Selector picked an h3 without an anchor	The scripts already require a.href.startsWith('http') — if it still happens, the SERP layout changed
DuckDuckGo URLs are duckduckgo.com/l/?uddg=...	Redirect wrapper	Use ddg_results_decode.js instead of ddg_results.js
Only 2–3 results	Page not fully loaded, or personalized to a narrow result set	Wait longer; retry with a broader query
Weekly Installs
9
Source
cbskills.xcloudzen.com
First Seen
8 days ago