---
title: shopware-admin-crud-module
url: https://skills.sh/friendsofshopware/agent-skills/shopware-admin-crud-module
---

# shopware-admin-crud-module

skills/friendsofshopware/agent-skills/shopware-admin-crud-module
shopware-admin-crud-module
Installation
$ npx skills add https://github.com/friendsofshopware/agent-skills --skill shopware-admin-crud-module
SKILL.md
Shopware Administration CRUD Module
When to Apply
Creating a new admin module for a Shopware DAL entity
Adding list, detail, and create pages for an entity in the administration
Setting up ACL privileges for an admin module
Adding search, filters, and inline editing for entity listings
Scaffolding administration i18n snippets for a new module
Rule Categories by Priority
Priority	Category	Prefix	Description
CRITICAL	Module Setup	module-	Module registration, file structure, naming conventions
CRITICAL	Pages	page-	List page and detail/create page patterns
HIGH	ACL & Search	acl-	ACL privilege mapping and search configuration
MEDIUM	Snippets & Filters	snippet-	i18n snippet structure and filter setup
How to Use

When the user invokes this skill, ask them for:

The entity name (DAL entity, e.g. webhook) -- if not provided as argument
Which fields to show in the list and detail (or read from the EntityDefinition PHP class automatically)
The module prefix to use (default: frosh-tools-<entity>)

Then read the relevant reference files from the references/ directory and generate all files following the patterns described there. The admin source root is src/Resources/app/administration/src/.

Naming Conventions
Module name: frosh-tools-<entity> (hyphenated)
Route prefix: frosh.tools.<entity> (dotted) -- derived from module name by replacing hyphens with dots
ACL key: frosh_tools_<entity> (underscored)
File Structure
module/<module-name>/
  index.js                          # Module registration + search type + lazy component loading
  default-search-configuration.js   # Search ranking config
  acl/
    index.js                        # ACL privilege mapping
  snippet/
    en-GB.json
    de-DE.json
  page/
    <module-name>-list/
      index.js
      template.html.twig
    <module-name>-detail/
      index.js
      template.html.twig


Also add import './module/<module-name>'; to main.js.

External References
Shopware Developer Documentation - Admin Module
Weekly Installs
24
Repository
friendsofshopwa…t-skills
GitHub Stars
9
First Seen
Mar 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketFail
SnykPass