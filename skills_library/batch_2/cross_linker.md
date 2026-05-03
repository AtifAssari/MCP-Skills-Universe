---
title: cross-linker
url: https://skills.sh/ar9av/obsidian-wiki/cross-linker
---

# cross-linker

skills/ar9av/obsidian-wiki/cross-linker
cross-linker
Installation
$ npx skills add https://github.com/ar9av/obsidian-wiki --skill cross-linker
SKILL.md
Cross-Linker — Automated Wiki Cross-Referencing

You are weaving the wiki's knowledge graph tighter by finding and inserting missing [[wikilinks]] between pages that should reference each other but currently don't.

Follow the Retrieval Primitives table in llm-wiki/SKILL.md. Build the registry in Step 1 by grepping frontmatter only (not full pages). Reserve full Read for the unlinked-mention detection pass, and even there, only read pages whose summaries/titles make them plausible link targets. Blind full-vault reads are what this framework exists to avoid.

Before You Start
Read ~/.obsidian-wiki/config (preferred) or .env (fallback) to get OBSIDIAN_VAULT_PATH and OBSIDIAN_LINK_FORMAT (default: wikilink)
Read index.md to get the full inventory of pages and their one-line descriptions
Skim log.md to see what was recently ingested (focus linking effort on new pages)

When inserting links in Step 4, apply the link format from llm-wiki/SKILL.md (Link Format section) using the OBSIDIAN_LINK_FORMAT value. When OBSIDIAN_LINK_FORMAT=markdown, compute the relative .md path from the file being edited to the target page.

Step 1: Build the Page Registry

Glob all .md files in the vault (excluding _archives/, .obsidian/). For each page, extract:

Filename (without .md) — this is the wikilink target
Title from frontmatter
Aliases from frontmatter (if any)
Tags from frontmatter
Category from frontmatter or directory inference
One-line summary — first sentence or title field

Build a lookup table:

page_name → { path, title, aliases, tags, summary }


This is your "vocabulary" — every entry in this table is a valid wikilink target.

Step 2: Scan for Missing Links

For each page in the vault:

Read the full content

Extract existing wikilinks — find all [[...]] references already present

Search for unlinked mentions — check if the page's text contains any of these, without being wrapped in [[...]]:

Page filenames (e.g., the word "MyProject" appears but [[projects/my-project/my-project]] is missing)
Page titles from frontmatter
Aliases from frontmatter
Entity names, project names, concept names from the registry

Check for semantic connections — pages that share multiple tags or are in the same project directory but don't link to each other

Matching Rules
Case-insensitive matching for names (e.g., "my-project" matches page MyProject)
Diacritic-insensitive matching — normalize both the page name and the body text with Unicode NFKD (decompose accented characters to base + combining marks, strip combining marks) before comparing. This ensures body text "Muller" matches page [[entities/müller]] and vice versa.
Skip self-references — a page shouldn't link to itself
Skip common words — don't link "the", "and", generic terms. Only match on distinctive names
Prefer the shortest unambiguous wikilink path — use [[page-name]] not [[full/path/to/page-name]] when the name is unique across the vault
Don't link inside code blocks or frontmatter
Don't double-link — if [[foo]] already appears on the page, don't add another
Step 3: Score and Rank Suggestions

Not every possible link is worth adding. Score each candidate using a composite signal, then tag it with a confidence label.

Scoring
Signal	Points	Example
Exact name match in text	+4	"MyProject" appears in body text → link to my-project.md
Shared tags (2+)	+2	Both tagged #ai #agent but no link between them
Same project, no link	+2	Both under projects/my-project/ but don't reference each other
Mentioned entity/concept	+2	Page mentions "knowledge graphs" → link to [[concepts/knowledge-graphs]]
Cross-category connection	+2	Source is in concepts/, target is in entities/ (or skills/ ↔ synthesis/) — different knowledge layers make this link more architecturally valuable
Peripheral→hub reach	+2	Source page has ≤ 2 total links (peripheral) but target has ≥ 8 (hub) — connecting a loose page to a load-bearing concept
Partial name match	+1	"graph" appears but page is knowledge-graphs — plausible but ambiguous
Confidence labels

Tag each candidate with a confidence label based on its score:

Score	Label	Action
≥ 6	EXTRACTED	Link is effectively certain — exact mention or very strong match. Apply inline.
3–5	INFERRED	Link is a reasonable inference — shared context, cross-category, peripheral→hub. Apply inline or as Related section.
1–2	AMBIGUOUS	Weak or partial match. Skip unless user specifically asks to connect loose pages.

Only act on EXTRACTED and INFERRED candidates. Include the confidence label in the Cross-Link Report so the user can review INFERRED links before trusting them.

Step 4: Apply Links

For each page with missing links:

4a: Inline linking (preferred)

Find the first natural mention of the term in the body text and wrap it in wikilinks:

Before:

This project uses knowledge graphs to connect entities.


After:

This project uses [[concepts/knowledge-graphs|knowledge graphs]] to connect entities.


Use the [[path|display text]] format when the wikilink path differs from the display text.

4b: Related section (fallback)

If the term isn't mentioned naturally in the body but the pages are semantically related (shared tags, same project), add a ## Related section at the bottom of the page:

## Related

- [[projects/my-project/my-project]] — Also uses AI agents for research automation
- [[concepts/knowledge-graphs]] — Core technique used in this project


If a ## Related section already exists, append to it. Don't duplicate existing entries.

Step 5: Score Misc Page Affinity

After the main linking pass, update affinity scores for all pages in misc/ (pages with promotion_status: misc in their frontmatter, or located under the misc/ directory).

For each misc page:

Collect outgoing links — all [[wikilinks]] in the page body
Collect incoming links — grep the vault for [[misc/<slug>]] and [[<slug>]] references
For each linked page (both directions), check if it belongs to a project:
Lives under projects/<project-name>/
Has a project: frontmatter field matching a project name
Group by project name and sum: outgoing_links + incoming_links
Update the affinity frontmatter block on the misc page:
affinity:
  obsidian-wiki: 3
  another-project: 1

If any project's score ≥ 3: flag this page as a promotion candidate and record it for the report

Efficiency note: only read the full body of misc pages — other pages only need a frontmatter grep to determine their project membership.

Step 6: Report

Present a summary:

## Cross-Link Report

### Links Added: 23 across 12 pages

| Page | Links Added | Confidence | Type |
|---|---|---|---|
| `projects/my-project/my-project.md` | 3 | EXTRACTED | 2 inline, 1 related |
| `entities/jane-doe.md` | 5 | INFERRED | 3 inline, 2 related |
| ... | | | |

### Orphan Pages Remaining: 2
- `references/foo.md` — no incoming or outgoing links found
- `concepts/bar.md` — could not find related pages

### Misc Promotion Candidates: N
Pages in misc/ that have ≥ 3 connections to a single project — ready to be promoted:

| Page | Top Project | Score |
|---|---|---|
| `misc/web-martinfowler-articles-microservices.md` | `obsidian-wiki` | 4 |

To promote: move the page to `projects/<project-name>/references/` and update all backlinks.

### Pages Skipped: 3
- `index.md`, `log.md` — special files
- `_archives/*` — archived content

Step 7: Update Log and Hot Cache

Append to log.md:

- [TIMESTAMP] CROSS_LINK pages_scanned=N links_added=M pages_modified=P orphans_remaining=Q misc_affinity_updated=R promotion_candidates=S


hot.md — Read $OBSIDIAN_VAULT_PATH/hot.md (create from the template in wiki-ingest if missing). Update Recent Activity with a one-line summary of what was linked — e.g. "Cross-linked 23 mentions across 12 pages; 2 orphans remain." Keep the last 3 operations. Update updated timestamp.

Tips
Run after every ingest. New pages are almost always poorly connected. This is the fix.
Be conservative with inline links. Only link the first natural mention, not every occurrence.
Don't touch pages in _archives/. Those are frozen snapshots.
Respect existing structure. If a page carefully curates its links in a ## Key Concepts section, add to that section rather than creating a separate ## Related.
Entity pages are link magnets. An entity like jane-doe should be linked from almost every project page. Prioritize these.
Weekly Installs
918
Repository
ar9av/obsidian-wiki
GitHub Stars
893
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass