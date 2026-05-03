---
rating: ⭐⭐
title: sgds-pattern-page-templates
url: https://skills.sh/govtechsg/sgds-web-component/sgds-pattern-page-templates
---

# sgds-pattern-page-templates

skills/govtechsg/sgds-web-component/sgds-pattern-page-templates
sgds-pattern-page-templates
Installation
$ npx skills add https://github.com/govtechsg/sgds-web-component --skill sgds-pattern-page-templates
SKILL.md
SGDS Page Templates

Ready-to-use full-page templates using SGDS components and utilities — adapted from the visual patterns of shadcn Blocks. Each template gives a beautiful starting point without writing layout code from scratch.

Prerequisites

Every page must include the Application Shell. Read sgds-pattern-block-templates → reference/application-shell.md before generating any page. The shell provides mandatory <sgds-masthead>, <sgds-mainnav>, and <sgds-footer> on every page, plus container class selection (.sgds-container vs .sgds-container-sidebar) and sticky-header conventions. Never generate a page template without all three shell components.

import "@govtechsg/sgds-web-component/themes/day.css";
import "@govtechsg/sgds-web-component/css/sgds.css";
import "@govtechsg/sgds-web-component/css/utility.css";


See sgds-getting-started and sgds-components for full installation.

For container width and max-width utilities used in these templates, see sgds-utilities.

Quick Decision Guide
What you're building	Template to use
Internal tool, admin portal, dashboard	Dashboard
Login / sign-in page	Login
Multi-field settings or data-entry form	Form Page
Data list with search, filters, pagination	List Page
Company/agency profile, team intro, achievements	About Us
→ Read reference/dashboard.md

Sidebar navigation + stat cards row + data table. Use for dashboards, admin portals, internal tools.

Note: The dashboard template uses sgds-sidebar (RC component). Load the CDN script before other SGDS imports — see sgds-components sidebar reference for the CDN tag and framework setup.

→ Read reference/login.md

Centered card with email/password form. Use for authentication, sign-in, sign-up pages.

→ Read reference/form-page.md

Two-column settings layout with labelled form sections. Use for settings pages, profile pages, multi-section data entry.

→ Read reference/list-page.md

Search + filter bar + table + pagination. Use for record lists, search results, data management pages.

→ Read reference/about-us.md

Two-column headline + image grid + logo strip + achievements stats panel. Use for agency profiles, product about pages, team introductions.

Visual Hierarchy Principles (apply to all templates)

These are the rules that make SGDS UIs look polished — the same principles shadcn/Mantine use:

1. Layer backgrounds to create depth

Page background: sgds:bg-surface-default (the base canvas)
Cards / panels: sgds:bg-surface-raised (lifts content off the page)
Nested content areas: sgds:bg-surface-overlay sparingly

2. Use semantic spacing, not raw numbers Prefer sgds:p-layout-md, sgds:gap-layout-md, sgds:p-component-md over sgds:p-4. Semantic tokens are responsive and encode intent. Always apply whitespace between sections and elements — never render blocks without spacing. See sgds-utilities-spacing for the full defaults table.

3. Consistent card anatomy Every card: padding inside (sgds:p-component-lg), gap between card rows (sgds:gap-layout-md), border-radius (sgds:rounded-lg), subtle shadow (sgds:shadow-card).

4. Action hierarchy in forms Primary action → <sgds-button variant="primary">. Secondary / cancel → <sgds-button variant="outline">. Destructive → <sgds-button variant="ghost" tone="danger">.

5. Muted labels, prominent values In stat cards and description lists: label in sgds:text-muted sgds:text-sm, value in sgds:text-default sgds:text-2xl sgds:font-semibold.

Weekly Installs
38
Repository
govtechsg/sgds-…omponent
GitHub Stars
12
First Seen
Mar 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass