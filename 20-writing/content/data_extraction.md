---
title: data-extraction
url: https://skills.sh/site/cbskills.xcloudzen.com/data-extraction
---

# data-extraction

skills/cbskills.xcloudzen.com/data-extraction
data-extraction
$ npx skills add https://cbskills.xcloudzen.com
SKILL.md
Data Extraction — Structured Data from Pages

Goal: turn a rendered page into clean JSON. Always try the lightest-weight tool first; escalate only when it returns empty or wrong data.

Priority order
page_schema(tab_id?) — JSON-LD + microdata. Products, recipes, events, articles, local-business listings usually embed complete structured data. One call, often zero parsing. Caveat: returns {"schemas": []} on plenty of pages — disambiguation / list pages (Wikipedia), Google search results, Instagram profile pages, most SPAs without server-side rendering. Don't assume schema exists; fall through to the next tool if empty.
page_article(tab_id?, max_wait=10000) — Mozilla Readability + SPA wait. Returns { title, author, date, image, content } for editorial pages. Use for anything you'd call "an article." Increase max_wait to 15000 for heavy SPAs.
page_headings(tab_id?) — h1–h6 outline. Cheap. Use to plan a targeted extraction before dumping the whole page.
execute_script — custom DOM extractor. Use when the data you want isn't in schema and isn't article prose (price badges, review counts, custom data attributes, tabular data).
page_markdown(tab_id?) — full-page Markdown dump. Includes nav/footer/sidebar. Last resort when page_article errors (dashboards, search results, listings).
page_source(tab_id?) / page_text(tab_id?) — raw HTML / plain text. Fallback when selectors misbehave or paywalls are CSS-only.
Reusable scripts

Each capability has a focused JS file under scripts/. To use one:

Read the script file to load it as a string.
Pass the contents as the code argument to mcp__chrome-bridge__execute_script.
The script returns a structured object — see the header comment at the top of each file for the exact return shape.
Task	Pre-condition	Script	Notes
Product DOM fallback	page_schema() returned [] or sparse Product	scripts/product_dom_fields.js	Adapt the right-hand selectors per site.
Tables	Page rendered	scripts/tables_extract.js	Returns every table as { headers, rows }. Use instead of page_markdown() — markdown mangles tables.
Listing links	On a listing/index page	scripts/listing_links.js	Scoped to article h2 a, article h3 a. Edit the selector for sites that use a different wrapper.
Pattern: schema-first
navigate(url='https://www.example.com/product/xyz')
# wait for ready
data = page_schema()
# If data contains a @type=Product entry with name/price/offers, you're done.


When schema is missing or sparse, fall through to the DOM fallback:

execute_script(code=<contents of scripts/product_dom_fields.js>)

Pattern: articles

For news, blogs, docs, Substack, Medium — try page_article first:

navigate(url='https://...')
# wait
article = page_article()
# → { title, author, date, image, content } (Markdown body)


If page_article returns { error: ... } (dashboards, listing pages, custom layouts), fall through to page_schema then page_markdown.

Pattern: tables
execute_script(code=<contents of scripts/tables_extract.js>)
# → [{ index, caption, headers, rows }, ...] one entry per <table>

Pattern: links / listings
execute_script(code=<contents of scripts/listing_links.js>)
# → [{ title, url }, ...]

Dynamic content

Content injected after load (infinite scroll, "Read more" expanders):

# trigger the load
execute_script(code="(function(){ window.scrollTo(0, document.body.scrollHeight); return 'scrolled'; })()")
# wait a few seconds, then re-extract
page_schema()   # or whichever tool


If content only appears after a click:

dom_click('button.expand-all')
# wait, re-extract

Return shape

Every extractor should return a plain JSON-serializable object. Good shapes:

{ source_url, captured_at, items: [{ title, url, price, ... }] }


Always include the source_url and a timestamp so downstream consumers can audit staleness. Don't return DOM nodes, HTML blobs, or images — extract the field you need and return that.

VERBATIM RULE — never summarize a body field

When the user asks for a body, description, content, full text, article, excerpt, or anything similar, the value MUST be the actual text returned by page_text / page_article().content / page_markdown — copied as-is (you may trim trailing site chrome like "RELATED NEWS", "Top Articles", "Follow Us", "Comments", footer links). You may NOT:

write a summary in your own words
paraphrase or condense
substitute a description like "Article covers Q1 results and analyst commentary"
substitute placeholder text like "Full article text can be fetched on request" or "Retrieved live content from source"
return only the title or only the first paragraph when the request was the body

Field names like full_text, body, content, description, excerpt are content slots, not metadata slots. If you don't have the verbatim text yet, navigate to the item and call page_text before answering.

Examples — body field
// ✓ CORRECT: the value is the actual returned text from page_text()
{
  "url": "https://news.site/q1-results",
  "full_text": "Acme Corp posted Q1 revenue of $4.2B, up 18% YoY, beating analyst consensus of $3.9B. CEO Jane Doe attributed the gain to enterprise contract renewals and a 12% lift in international bookings. Operating margin expanded to 23.4% from 21.1% a year ago, helped by lower customer-acquisition spend. The company guided FY revenue to $17–18B, in line with the Street. Shares rose 6% in after-hours trading. ..."
}

// ✗ WRONG: summary disguised as body
{
  "url": "https://news.site/q1-results",
  "full_text": "Article on Acme's Q1 earnings covering revenue beat, margin expansion, and full-year guidance."
}

// ✗ WRONG: placeholder
{
  "url": "https://news.site/q1-results",
  "full_text": "Q1 earnings article — full text available on the source page."
}

// ✗ WRONG: title repeated as body
{
  "url": "https://news.site/q1-results",
  "full_text": "Acme Corp Q1 Earnings"
}

Common failures
Signal	Cause	Fix
page_schema returns []	Site has no structured data	Skip to page_article or custom extractor
page_article returns { error }	Not an article page	Use page_schema / page_markdown / custom extractor instead
Selectors match nothing	Page not yet hydrated	Poll document.readyState or a known element; scroll to trigger lazy load
execute_script returns undefined	Bare return at top level	Wrap the code in (function(){ ... })() (the scripts in scripts/ already do this)
execute_script errors with Invalid \escape	JS regex backslashes not double-escaped for JSON	Pass scripts as file contents (no JSON encoding) — the scripts/ files don't need escaping. If you must inline regex, prefer indexOf() / includes().
execute_script times out (HTTP 504)	Script does something slow (image fetch, big loop)	Trim the logic; return fewer fields; avoid fetch() inside the script
Paywalled content hidden	Some paywalls only hide via CSS	Try page_text — the body text is often still in the DOM
Weekly Installs
9
Source
cbskills.xcloudzen.com
First Seen
8 days ago