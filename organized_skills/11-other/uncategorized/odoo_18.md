---
rating: ⭐⭐⭐
title: odoo-18
url: https://skills.sh/unclecatvn/agent-skills/odoo-18
---

# odoo-18

skills/unclecatvn/agent-skills/odoo-18
odoo-18
Installation
$ npx skills add https://github.com/unclecatvn/agent-skills --skill odoo-18
SKILL.md
Odoo 18 Skill - Master Index

Master index for all Odoo 18 development guides. Read the appropriate guide from references/ based on your task.

Quick Reference
Topic	File	When to Use
Actions	references/odoo-18-actions-guide.md	Creating actions, menus, scheduled jobs, server actions
API Decorators	references/odoo-18-decorator-guide.md	Using @api decorators, compute fields, validation
Controllers	references/odoo-18-controller-guide.md	Writing HTTP endpoints, routes, web controllers
Data Files	references/odoo-18-data-guide.md	XML/CSV data files, records, shortcuts
Development	references/odoo-18-development-guide.md	Creating modules, manifest, reports, security, wizards
Field Types	references/odoo-18-field-guide.md	Defining model fields, choosing field types
Manifest	references/odoo-18-manifest-guide.md	manifest.py configuration, dependencies, hooks
Migration	references/odoo-18-migration-guide.md	Upgrading modules, data migration, version changes
Mixins	references/odoo-18-mixins-guide.md	mail.thread, activities, email aliases, tracking
Model Methods	references/odoo-18-model-guide.md	Writing ORM queries, CRUD operations, domain filters
OWL Components	references/odoo-18-owl-guide.md	Building OWL UI components, hooks, services
Performance	references/odoo-18-performance-guide.md	Optimizing queries, fixing slow code, preventing N+1
Reports	references/odoo-18-reports-guide.md	QWeb reports, PDF/HTML, templates, paper formats
Security	references/odoo-18-security-guide.md	Access rights, record rules, field permissions
Testing	references/odoo-18-testing-guide.md	Writing tests, mocking, assertions, browser testing
Transactions	references/odoo-18-transaction-guide.md	Handling database errors, savepoints, UniqueViolation
Translation	references/odoo-18-translation-guide.md	Adding translations, localization, i18n
Views & XML	references/odoo-18-view-guide.md	Writing XML views, actions, menus, QWeb templates
File Structure
skills/odoo-18.0/
├── SKILL.md                          # This file - master index
└── references/                       # Development guides
    ├── odoo-18-actions-guide.md
    ├── odoo-18-controller-guide.md
    ├── odoo-18-data-guide.md
    ├── odoo-18-decorator-guide.md
    ├── odoo-18-development-guide.md
    ├── odoo-18-field-guide.md
    ├── odoo-18-manifest-guide.md
    ├── odoo-18-migration-guide.md
    ├── odoo-18-mixins-guide.md
    ├── odoo-18-model-guide.md
    ├── odoo-18-owl-guide.md
    ├── odoo-18-performance-guide.md
    ├── odoo-18-reports-guide.md
    ├── odoo-18-security-guide.md
    ├── odoo-18-testing-guide.md
    ├── odoo-18-transaction-guide.md
    ├── odoo-18-translation-guide.md
    └── odoo-18-view-guide.md

Base Code Reference (Odoo 18)

All guides are based on analysis of Odoo 18 source code:

odoo/models.py - ORM implementation
odoo/fields.py - Field types
odoo/api.py - Decorators
odoo/http.py - HTTP layer
odoo/exceptions.py - Exception types
odoo/tools/translate.py - Translation system
odoo/addons/base/models/res_lang.py - Language model
addons/web/static/src/core/l10n/translation.js - JS translations
External Documentation
Odoo 18 Official Documentation
Odoo 18 Developer Reference
Weekly Installs
649
Repository
unclecatvn/agent-skills
GitHub Stars
60
First Seen
Today