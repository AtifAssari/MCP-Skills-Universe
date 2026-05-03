---
rating: ⭐⭐
title: jina-web-fetch
url: https://skills.sh/xiaojiongqian/skills-hub/jina-web-fetch
---

# jina-web-fetch

skills/xiaojiongqian/skills-hub/jina-web-fetch
jina-web-fetch
Installation
$ npx skills add https://github.com/xiaojiongqian/skills-hub --skill jina-web-fetch
SKILL.md
Jina Web Fetch

Use this skill to capture content from hard-to-fetch pages while keeping a deterministic workflow:

Try direct fetch first.
If direct fetch fails or looks blocked, retry via jina.ai.
Quick Start
bash "<path-to-skill>/scripts/fetch_with_jina_fallback.sh" "<url>" "<output_file>"


Example:

bash "<path-to-skill>/scripts/fetch_with_jina_fallback.sh" \
  "https://x.com/trq212/status/2027463795355095314" \
  "raw/x-status.txt"


The script prints source=direct or source=jina to stderr so you can see which path was used.

If output_file is omitted, content is printed to stdout.

Default Workflow
Run the script with the target URL.
Save raw output under a traceable path like raw/<slug>.txt.
Parse extracted text/markdown for:
main body
media links (images/videos)
referenced URLs
Keep original URL + raw capture together for auditability.
Blocking Heuristics

The script auto-falls back to jina.ai when direct content looks like:

login wall / sign-up prompt
JS-required page
anti-bot / captcha / access denied page
very small shell-like HTML page (default threshold < 800 bytes)
Environment Knobs
FETCH_TIMEOUT (default 25)
FETCH_CONNECT_TIMEOUT (default 10)
FETCH_MIN_BYTES (default 800)
JINA_FORCE=1 to skip direct fetch and always use jina.ai
URL Format Note

Fallback URL is built as: https://r.jina.ai/http://<original-host-and-path>

Weekly Installs
49
Repository
xiaojiongqian/skills-hub
GitHub Stars
2
First Seen
Mar 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn