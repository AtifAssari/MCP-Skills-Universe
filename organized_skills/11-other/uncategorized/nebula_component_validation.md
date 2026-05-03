---
rating: ⭐⭐
title: nebula-component-validation
url: https://skills.sh/acquia/nebula/nebula-component-validation
---

# nebula-component-validation

skills/acquia/nebula/nebula-component-validation
nebula-component-validation
Installation
$ npx skills add https://github.com/acquia/nebula --skill nebula-component-validation
SKILL.md
Validate

Before running validation, confirm every new component has a matching src/stories/<component-name>.stories.jsx file (see nebula-storybook-stories).

After creating or modifying components, always validate your code by running the code:fix script. Make sure to use the right package manager. For example, if using npm, run the following command:

npm run code:fix


This runs Prettier and ESLint with auto-fix, ensuring:

Consistent formatting
Common issue detection
Drupal Canvas Code Component requirements

If errors remain after auto-fix, address them manually and re-run until passing.

Weekly Installs
8
Repository
acquia/nebula
GitHub Stars
7
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass