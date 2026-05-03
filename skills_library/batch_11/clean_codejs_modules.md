---
title: clean-codejs-modules
url: https://skills.sh/damianwrooby/javascript-clean-code-skills/clean-codejs-modules
---

# clean-codejs-modules

skills/damianwrooby/javascript-clean-code-skills/clean-codejs-modules
clean-codejs-modules
Installation
$ npx skills add https://github.com/damianwrooby/javascript-clean-code-skills --skill clean-codejs-modules
SKILL.md
Clean Code JavaScript – Module Patterns
Table of Contents
One Responsibility per Module
Export Patterns
Folder Structure
One Responsibility per Module
// ❌ Bad
// user.js
export function createUser() {}
export function connectToDb() {}

// ✅ Good
// user.service.js
export function createUser() {}

Export Patterns
// ✅ Prefer named exports
export function parseDate() {}
export function formatDate() {}

Folder Structure
/users
  user.service.js
  user.repository.js
  user.controller.js

Weekly Installs
81
Repository
damianwrooby/ja…e-skills
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass