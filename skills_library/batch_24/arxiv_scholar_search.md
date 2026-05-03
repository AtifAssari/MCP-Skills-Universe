---
title: arxiv-scholar-search
url: https://skills.sh/site/skills.volces.com/arxiv-scholar-search
---

# arxiv-scholar-search

skills/skills.volces.com/arxiv-scholar-search
arxiv-scholar-search
$ npx skills add https://skills.volces.com/skills/clawhub/xxxxxxxxxxxxxxxxxxx20gex
SKILL.md
Scholar Search Workflow

This skill only uses arXiv as the data source. The workflow is fixed:

Read user input and parse the search intent.
Call the arXiv API (via arxiv_search).
Evaluate result quality and decide whether another search round is needed.
Output results using the required template.
0) File Layout (Overview)
File Path	Purpose	When to Check
SKILL.md	Main entry: task parsing, query syntax, calling conventions, quality control	Check first at the beginning of every task
1) Parse User Search Requirements

Extract the following constraints first:

Topic keywords (Chinese or English).
Time preference (for example: "latest", "this year", "last three years").
Number of results (for example: 5, 10, 20).
Output goal (paper discovery, comparison, or brief survey).
Output language (Chinese or English).

Keyword strategy:

Use a broad query in round one (topic terms only).
Add constraint terms in round two (method terms, task terms, category terms).
If results are too few, switch to synonyms or broader terms.
2) arXiv API Guide (Built-in)
2.1 API Endpoint
Base endpoint: https://export.arxiv.org/api/query
Request methods: GET (common), POST (optional when parameters are very long)
2.2 Core Parameters
search_query: query expression
id_list: comma-separated list of arXiv IDs
start: pagination offset (0-based)
max_results: number of returned entries
sortBy: relevance / lastUpdatedDate / submittedDate
sortOrder: ascending / descending
2.3 search_query Syntax

Common field prefixes:

ti (title)
au (author)
abs (abstract)
cat (category)
all (all fields)

Boolean operators:

AND
OR
ANDNOT

Time syntax (submittedDate):

Range: submittedDate:[200701*+TO+200712*]
Specific day: submittedDate:20101225
2.4 Direct URL Examples
Topic query: https://export.arxiv.org/api/query?search_query=all:electron
Combined query: https://export.arxiv.org/api/query?search_query=au:del_maestro+AND+ti:checkerboard
Paginated query: https://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=10
Sorted query: https://export.arxiv.org/api/query?search_query=ti:%22electron+thermal+conductivity%22&sortBy=lastUpdatedDate&sortOrder=descending
2.5 Rate Limits and Stability (Must Follow)
Keep request frequency at no more than one request every 3 seconds.
Use only one active connection at a time.
Avoid high-frequency repeated queries; reuse existing results whenever possible.
3) Calling Conventions (Must Match Actual Use)

Standard call example:

curl -s "https://export.arxiv.org/api/query?search_query=all:multimodal+AND+cat:cs.CL&start=0&max_results=10&sortBy=submittedDate&sortOrder=descending"


Parameter notes:

search_query: arXiv query expression (supports field prefixes and boolean operators).
start: pagination offset (0-based).
max_results: number of returned entries; recommend 5-20.
sortBy: recommend submittedDate or lastUpdatedDate.
sortOrder: recommend descending.
4) Decide Whether to Continue Searching

Run one more search round if any condition below is met:

Too few papers are returned (for example, < 3).
Results are clearly off-topic.
Key fields are frequently missing (title, link, abstract).

Stop searching when:

Result count reaches the target or an acceptable range.
Topic relevance is high.
Additional search rounds provide low value.
5) Output Requirements

Each paper must use the following structure:

-----------
# {Index}. **{Paper Title}**

**Paper Info**: **Venue/Source**: {journal, conference, or source} | **Publication Date**: {yyyy-mm-dd or unknown} | **Source**: [{source name}]({entry link or paper link}) | **PDF**: [PDF link]({pdf link})

### Research Content
{1-2 objective sentences based on the paper content}

### Main Contributions
- {Contribution 1}
- {Contribution 2}
- {Contribution 3}


Must follow:

Add a standalone line ----------- before every paper title.
Keep the title as a standalone level-1 header line.
Keep "Paper Info" in a single line, separated by |.
Keep the PDF field:
If a PDF exists: provide a direct link.
If no PDF exists: remove the PDF field.
Content must be based only on source metadata, abstract, or TLDR. No speculation.
Do not add conclusions not explicitly supported by the source.
All links must come from tool output. Do not fabricate or guess links.
Do not fabricate venue, date, or citation count.
Write "Research Content" and "Main Contributions" only from returned fields.
6) Failure Handling
API failure: state the reason and the strategies already attempted.
No results: provide actionable keyword rewrite suggestions.
Missing fields: explicitly mark as "unknown/missing"; do not fill with inferred data.
Weekly Installs
17
Source
skills.volces.c…xxx20gex
First Seen
Mar 19, 2026