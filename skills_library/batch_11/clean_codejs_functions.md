---
title: clean-codejs-functions
url: https://skills.sh/damianwrooby/javascript-clean-code-skills/clean-codejs-functions
---

# clean-codejs-functions

skills/damianwrooby/javascript-clean-code-skills/clean-codejs-functions
clean-codejs-functions
Installation
$ npx skills add https://github.com/damianwrooby/javascript-clean-code-skills --skill clean-codejs-functions
SKILL.md
Clean Code JavaScript – Function Patterns
Table of Contents
Single Responsibility
Function Size
Parameters
Side Effects
Single Responsibility
// ❌ Bad
function handleUser(user) {
  saveUser(user);
  sendEmail(user);
}

// ✅ Good
function saveUser(user) {}
function notifyUser(user) {}

Function Size

Keep functions small (ideally < 20 lines).

Parameters
// ❌ Bad
function createUser(name, age, city, zip) {}

// ✅ Good
function createUser({ name, age, address }) {}

Side Effects
// ❌ Bad
let total = 0;
function add(value) {
  total += value;
}

// ✅ Good
function add(total, value) {
  return total + value;
}

Weekly Installs
96
Repository
damianwrooby/ja…e-skills
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass