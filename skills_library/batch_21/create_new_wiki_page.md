---
title: create-new-wiki-page
url: https://skills.sh/jim60105/copilot-prompt/create-new-wiki-page
---

# create-new-wiki-page

skills/jim60105/copilot-prompt/create-new-wiki-page
create-new-wiki-page
Installation
$ npx skills add https://github.com/jim60105/copilot-prompt --skill create-new-wiki-page
SKILL.md
Create New Wiki Page

Create a new Azure DevOps wiki page with proper structure and formatting.

Steps

Execute tree . /f in pwsh to get all the page lists.

Read all docs under 設計文件, 功能需求, 標準規範 or other documents to get the full view of the project.

Plan the content for the wiki page about the user's specified topic. ${input:what-to-write-in-this-page}.

Include a mermaid diagram on the page if there is suitable content for it.

If the user doesn't specify a location, find an appropriate category and path for this page.

Write the page in 正體中文.

Add this page to the .order file in the same directory.

Add this page to the category's markdown file (e.g., if under 標準規範/, update 標準規範.md).

Review whether the Azure DevOps Wiki page is well-written; refine it to improve quality.

Git commit with a good message body.

Summarize what was done.

Wiki Writing Guidelines
Write in simple, concise language.
Follow a consistent format across all pages.
Break up sections with headlines, subheads, and text boxes.
Enrich pages with mermaid diagrams and links.
Include a list of FAQs in each section.
Weekly Installs
11
Repository
jim60105/copilot-prompt
GitHub Stars
18
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass