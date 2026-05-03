---
title: intel-agent
url: https://skills.sh/yfe404/intel-agent/intel-agent
---

# intel-agent

skills/yfe404/intel-agent/intel-agent
intel-agent
Installation
$ npx skills add https://github.com/yfe404/intel-agent --skill intel-agent
SKILL.md
Intel Agent: Data Point Reconnaissance
When This Skill Activates

Activate when user requests:

"recon [URL]"
"intel report for [URL]"
"find how to extract [data] from [URL]"
"discover data from [URL]"
"what's the best way to get [data] from [site]"
"how would I scrape [data points] from [URL]"

This skill does NOT implement scrapers. It discovers extraction methods and outputs a structured intelligence report. For implementation, hand off to the web-scraper skill.

References (loaded on demand):

reference/tool-reference.md — Tool signatures, known limitations, important rules
reference/data-point-types.md — Type classification and search strategies per type
reference/report-schema.md — Report output format
strategies/cheerio-vs-browser-test.md — Cheerio vs Browser extraction test procedure
strategies/proxy-escalation.md — Three-tier protection testing procedure
Input Parsing

Extract from the user's request: Target URL and Data points to extract.

Normalize each data point into a type (text / numeric / boolean / list / nested) with search terms. See reference/data-point-types.md for type classification and search strategies.

If data points are NOT specified, ask the user before proceeding.

The Workflow

Six steps, executed sequentially. Each step builds on the previous.

Step 1: Initialize & Capture Baseline Traffic

Start the MITM proxy with full-body persistence (required — the default ring buffer caps bodies at 4 KB, which truncates __NEXT_DATA__, JSON-LD, and most API responses). Then launch the stealth browser and capture the baseline.

proxy_start(persistence_enabled: true, capture_profile: "full", session_name: "recon-[domain]-[YYYYMMDD]", max_disk_mb: 2048)
interceptor_browser_launch(url: "[target URL]")
interceptor_browser_screenshot(target_id)


Note: proxy_start with persistence_enabled: true auto-starts a session. A subsequent proxy_session_start() will return the existing session (not error), but the cleaner pattern is to pass session_name directly to proxy_start. Capture the returned session_id — every body-search and HAR-export call needs it.

Console signal for site profiling: interceptor_browser_list_console(target_id) — React/hydration warnings → CSR SPA, network errors on /api/* → API-driven, clean console → static SSR.

Record: Session name/ID, page load status, loading behavior (SSR vs SPA), interstitials, framework indicators.

Dismiss interstitials: prefer locator-based clicks over CSS selectors — humanizer_click auto-waits for visible + enabled + stable + in-view. Try in this order:

humanizer_click(target_id, role: "button", name: "Accept all")
humanizer_click(target_id, text: "I agree")
humanizer_click(target_id, selector: ".cookie-accept")   # fallback


Multiple popups may appear sequentially (e.g., Cloudflare challenge then cookie consent) — repeat until the page is clean.

Step 2: Scan Response Bodies for Data Points

For each data point, search three locations to determine extraction methods.

2a. Raw HTML body (Cheerio method)

Use the session-backed full-body path — the ring buffer preview (proxy_get_exchange) truncates at 4 KB and will miss embedded JSON blobs.

proxy_search_session_bodies(session_id, query: "[data point search term]", hostname_contains: "[target domain]")
proxy_list_traffic(url_filter: "[target domain]", method_filter: "GET")   # locate main HTML exchange id
proxy_get_session_exchange(session_id, exchange_id: "[main HTML exchange id]", include_body: true)


If the search term is found in the raw HTML body → Cheerio works.

2b. JSON blobs in HTML (JSON-in-HTML method)

Search the raw HTML body (or use proxy_search_session_bodies directly) for: application/ld+json, __NEXT_DATA__, __INITIAL_STATE__, __NUXT__, __APOLLO_STATE__, __RELAY_STORE__. Parse and search for data points. If found → JSON-in-HTML works (preferred over Cheerio).

2c. Rendered DOM (Browser method)
interceptor_browser_snapshot(target_id)
# scoped (token-saver):
interceptor_browser_snapshot(target_id, selector: "main, article, [itemtype*='Product']")
# with refs (lets later humanizer_click reuse the locator):
interceptor_browser_snapshot(target_id, mode: "ai")


Output is YAML with role, name, text fields — match data-point search terms against those. If found in rendered DOM but NOT in raw HTML / JSON blobs / web storage → Browser extraction required.

2d. Web storage scan (often overlooked — SPAs hydrate from here)
interceptor_browser_list_storage_keys(target_id, storage_type: "local")
interceptor_browser_list_storage_keys(target_id, storage_type: "session")
interceptor_browser_get_storage_value(target_id, storage_type: "local", item_id: "[item_id]")


If a search term is found in a storage value → Browser extraction required, but the data is stable + parseable from storage keys (record the key name).

2e. Decision matrix
Raw HTML?	JSON Blob?	Web Storage?	Rendered DOM?	Method
Yes	—	—	—	Cheerio
—	Yes	—	—	JSON-in-HTML (preferred)
Yes	Yes	—	—	JSON-in-HTML (preferred) or Cheerio
No	No	Yes	—	Browser required; parseable from storage
No	No	No	Yes	Browser required (DOM scrape)
No	No	No	No	Requires interaction → Step 2f

See strategies/cheerio-vs-browser-test.md for the detailed procedure.

2f. Trigger interactions for missing data points

For data points not found: proxy_clear_traffic(), interact (locator-based humanizer_click, humanizer_scroll), then re-check DOM + traffic. humanizer_click auto-waits for stability — no explicit idle needed before reading traffic.

2g. Full-page scroll capture (MANDATORY)

Scroll the entire page before API sniffing to capture lazy-loaded API calls:

proxy_clear_traffic()
Scroll 2-3x: humanizer_scroll(target_id, delta_y: 800)
Mid-scroll visual check: interceptor_browser_screenshot(target_id) + interceptor_browser_snapshot(target_id) — inspect for interstitials (CAPTCHA, cookie consent, modals). Dismiss via humanizer_click(role + name / text). If a hard block (CAPTCHA) is detected, stop scrolling and proceed to Step 3 with traffic captured so far.
Scroll 2-3x more: humanizer_scroll(target_id, delta_y: 800)
interceptor_browser_screenshot(target_id) + interceptor_browser_snapshot(target_id) — final state
proxy_list_traffic() — review newly triggered API calls

MANDATORY even if all data points already found — lazy APIs often provide better-structured data.

Step 3: Sniff APIs
3a. Filter existing traffic

The MITM proxy is the single source of truth — it sees strictly more than any in-browser network view (3rd-party domains, CONNECT tunnels, every TLS handshake):

proxy_list_traffic(url_filter: "/api/")
proxy_list_traffic(url_filter: "/graphql")
proxy_list_traffic(url_filter: "/_next/data/")
proxy_list_traffic(url_filter: "/wp-json/")
proxy_list_traffic(url_filter: ".json")
proxy_search_traffic(query: "application/json")
proxy_search_session_bodies(session_id, query: "__typename", content_type_contains: "application/json")

3b. Trigger more traffic via interactions

proxy_clear_traffic() → interact (pagination, search, filters, detail click, load more, sort) via locator-based humanizer_click → proxy_list_traffic(). No explicit idle — humanizer_click auto-waits for stability.

3c. Inspect each discovered endpoint

Pull full request + response body from the session (not the 4 KB preview): proxy_get_session_exchange(session_id, exchange_id, include_body: true). Record: URL, method, headers, auth, body, response structure, pagination, data points covered, rate limits. See reference/report-schema.md Section 4 for the full endpoint template.

Step 4: Test Protection Levels

See strategies/proxy-escalation.md for the detailed procedure.

Tier 1 (Direct): Already tested. Check cookies, status codes, challenges:

interceptor_browser_list_cookies(target_id)
proxy_search_traffic(query: "403")
proxy_search_traffic(query: "challenge")


TLS verification: proxy_list_tls_fingerprints(hostname_filter: "[target domain]"). JA3 varies + JA4 stable = browser ClientHello passthrough (cloakbrowser presents authentic Chrome fingerprint). JA3 identical = proxy re-terminates. See strategies/proxy-escalation.md for interpretation matrix.

Tier 2 (Datacenter): proxy_set_upstream("[dc proxy]") → interceptor_browser_navigate(target_id, url, wait_until: "networkidle") → compare to baseline. For country-specific proxies, also relaunch the browser with matching timezone + locale (IP/browser geo mismatch is a bot signal).

Tier 3 (Residential): proxy_set_upstream("[res proxy]") → interceptor_browser_navigate(target_id, url, wait_until: "networkidle") → compare.

Clean up: proxy_clear_upstream().

Direct	Datacenter	Residential	Minimum Required
OK	OK	OK	Direct
Blocked	OK	OK	Datacenter proxy
Blocked	Blocked	OK	Residential proxy
Blocked	Blocked	Blocked	Residential + stealth + CAPTCHA solving
Step 5: Rank Extraction Methods

For each data point, rank available methods. Priority: API > JSON-in-HTML > Cheerio > Browser.

Per method include: source details (endpoint/selector/JSON path), required proxy level, confidence (High/Medium/Low).

Step 6: Generate Intelligence Report

Compile findings into the report format. See reference/report-schema.md for the complete structure.

6a. Export session evidence:

proxy_get_session_handshakes(session_id)   # JA3/JA4 coverage for section 2
proxy_session_stop()
proxy_export_har(session_id: "[session_id]", file_path: "recon-[domain]-[YYYYMMDD].har", include_bodies: true)


Include session name, ID, HAR path, and handshake coverage in Section 6 of the report (all REQUIRED).

What This Skill Does NOT Do

This skill is pure discovery. It does NOT write scraping code, create Actors, implement pagination, or deploy anything.

Handoff: After generating the report:

Intelligence report complete. To implement a scraper based on these findings,
use the web-scraper skill:
  "scrape [data points] from [URL] using the intel report above"

Weekly Installs
14
Repository
yfe404/intel-agent
First Seen
Mar 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykFail