---
rating: ⭐⭐⭐
title: navigation
url: https://skills.sh/site/cbskills.xcloudzen.com/navigation
---

# navigation

skills/cbskills.xcloudzen.com/navigation
navigation
$ npx skills add https://cbskills.xcloudzen.com
SKILL.md
Navigation — Loading URLs and Managing Tabs

Covers navigate, navigate_back, navigate_forward, tabs_*, and the wait-for-ready patterns every other skill depends on. Read chrome-bridge first if you haven't.

Single-tab loads
navigate(url='https://example.com')            # uses the active tab
navigate(url='https://example.com', tab_id=N)  # targets a specific tab


navigate returns once Chrome has dispatched the load — not once the DOM is ready. Always confirm before interacting:

execute_script(code="(()=>({url:location.href, title:document.title}))()")
# → check .url for redirects/consent walls/geo-rewrites; .title to confirm you got the page you asked for
# Or, if you have the tab id: tabs_get(tab_id).url / .title

Wait for ready

No sleep tool exists. Poll document.readyState:

execute_script(code="(function(){ return document.readyState; })()")
# Repeat until it returns "complete". Most pages get there in <3s.


For SPAs where readyState=complete fires before hydration, poll for a known element instead:

execute_script(code="(function(){ return !!document.querySelector('main [data-loaded=true]'); })()")


Rough ceilings if you must guess: simple HTML 2–3s, typical SPA 5–6s, heavy SPA (Google Scholar, LinkedIn feed, Anthropic docs) 8–10s.

Back / forward
navigate_back(tab_id?)     # history.back()
navigate_forward(tab_id?)  # history.forward()


Useful for OAuth callbacks, pagination that uses pushState, wizard flows that retain state on back. If the page was loaded via navigate then submitted a form, navigate_back returns to the pre-submit form with field values preserved (in most cases).

Multi-tab orchestration

Parallelism in chrome-bridge is per-tab: requests to different tabs run concurrently, requests to the same tab are queued. Use tabs to parallelize.

a = tabs_create(url='https://news.ycombinator.com').id
b = tabs_create(url='https://lobste.rs').id
c = tabs_create(url='https://techmeme.com').id
# Wait until all three are ready (poll readyState on each, or just sleep ~4s)

page_markdown(tab_id=a)   # these three run in parallel
page_markdown(tab_id=b)
page_markdown(tab_id=c)

tabs_close(a); tabs_close(b); tabs_close(c)


Rules of thumb

Keep concurrency at 3–5 tabs. Beyond that Chrome swaps and everything slows.
Close each tab as soon as you're done with it, not at the end of the session.
The bridge always keeps at least one about:blank tab alive — don't worry about closing "the last" tab.
Background tabs may not fully render

Tabs created with active=false (or that were never foregrounded) can return empty title, empty url, and unrendered DOM. If dom_query or page_* calls come back suspiciously empty:

action('tabs.update', { tabId: N, active: true })
# wait ~2–3s for the page to finish painting


Then retry the extraction.

Common patterns

Confirm you actually landed on the page you asked for:

navigate(url='https://example.com/article')
# ... wait for ready ...
current = execute_script(code="(()=>location.href)()")
if current != 'https://example.com/article':
    # maybe a consent redirect or geo block — investigate


Reload when content is stale:

tabs_reload(tab_id=N)
# wait for ready, then re-extract


Open a sibling tab from the current one (preserves history if useful):

tabs_duplicate(tab_id=N)
# then navigate the duplicate somewhere else

Common failures
Signal	Cause	Fix
URL after navigate differs from what you asked for	Redirect, consent wall, geo-block, login gate	Inspect execute_script("(()=>document.title)()") and page_text(); for consent walls see search skill
Navigation returns but DOM is empty	SPA still hydrating	Poll for a specific element, not just readyState
Many parallel tabs all slow	Opened too many at once	Stick to 3–5; close finished ones before opening new ones
Empty DOM after tabs_create with active=false	Background rendering suspended	action('tabs.update', ...) to activate, wait, retry
Weekly Installs
9
Source
cbskills.xcloudzen.com
First Seen
8 days ago