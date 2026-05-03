---
rating: ⭐⭐⭐
title: mdzilla
url: https://skills.sh/pi0/mdzilla/mdzilla
---

# mdzilla

skills/pi0/mdzilla/mdzilla
mdzilla
Installation
$ npx skills add https://github.com/pi0/mdzilla --skill mdzilla
SKILL.md
mdzilla

Markdown documentation browser for terminal and agents. Fetches and renders docs from local dirs, GitHub, npm, HTTP, and llms.txt.

CLI
npx mdzilla <source> [query] [options]

Sources
Source	Syntax	Notes
Local dir	mdzilla ./docs	Scan local docs directory
File	mdzilla README.md	Render single markdown file
GitHub	mdzilla gh:owner/repo	Looks for docs/ in repo
npm	mdzilla npm:package-name	Downloads package, reads docs
HTTP	mdzilla https://example.com	Tries /llms.txt, then markdown negotiation, then HTML→markdown
Options
--export <dir> — Export docs to flat .md files
--plain — Plain text output; auto-enabled for AI agents or non-TTY stdout
Smart Resolve

The second positional argument is smart-resolved:

If it matches a navigation path → renders that page
Otherwise → searches titles and content
Agent usage
npx mdzilla gh:unjs/h3 /guide/basics        # render a specific page
npx mdzilla gh:unjs/h3 router               # search for 'router'
npx mdzilla https://h3.unjs.io /guide       # render page from URL
npx mdzilla npm:consola --plain             # list all pages (plain)


Export docs for offline processing:

npx mdzilla <source> --export ./fetched-docs


Then read the exported .md files as needed.

Programmatic API
Export Docs
import { exportSource } from "mdzilla";

await exportSource("./docs", "./dist/docs");
await exportSource("gh:unjs/h3", "./dist/h3-docs");
await exportSource("npm:h3", "./dist/h3-docs", { plainText: true });
await exportSource("https://h3.unjs.io", "./dist/h3-docs");

Collection
import { Collection, resolveSource } from "mdzilla";

const docs = new Collection(resolveSource("./docs"));
await docs.load();

console.log(docs.tree); // NavEntry[] navigation tree
console.log(docs.flat); // FlatEntry[] flat list

const content = await docs.getContent(docs.flat[0]);
const results = docs.filter("query"); // fuzzy search

Weekly Installs
32
Repository
pi0/mdzilla
GitHub Stars
106
First Seen
Mar 8, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn