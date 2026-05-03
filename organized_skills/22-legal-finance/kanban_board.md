---
rating: ⭐⭐
title: kanban-board
url: https://skills.sh/nexu-io/open-design/kanban-board
---

# kanban-board

skills/nexu-io/open-design/kanban-board
kanban-board
Installation
$ npx skills add https://github.com/nexu-io/open-design --skill kanban-board
SKILL.md
Kanban Board Skill

Produce a single-screen kanban board.

Workflow
Read the active DESIGN.md.
Identify squad name, sprint number, columns, and member roster from the brief.
Layout:
Top bar: project crumb, sprint chip, filter row (members, labels, status), search.
4 columns: Backlog, In progress, In review, Done. Each column has a count chip and an "+ add" affordance.
3–6 cards per column. Each card: tag chip, title, assignee avatar, point estimate, progress (if applicable).
Sidebar (collapsible feel): "Sprint pulse" with progress bar, top assignees, blocked-tickets callout.
One inline <style>, semantic HTML.
Output contract
<artifact identifier="kanban-board" type="text/html" title="Sprint Board">
<!doctype html>...</artifact>

Weekly Installs
65
Repository
nexu-io/open-design
GitHub Stars
14.2K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass