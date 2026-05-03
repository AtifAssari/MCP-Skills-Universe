---
title: clean-codejs-objects
url: https://skills.sh/damianwrooby/javascript-clean-code-skills/clean-codejs-objects
---

# clean-codejs-objects

skills/damianwrooby/javascript-clean-code-skills/clean-codejs-objects
clean-codejs-objects
Installation
$ npx skills add https://github.com/damianwrooby/javascript-clean-code-skills --skill clean-codejs-objects
SKILL.md
Clean Code JavaScript – Object & Class Patterns
Table of Contents
Encapsulation
Immutability
Cohesion
Encapsulation
// ❌ Bad
user.name = 'John';

// ✅ Good
user.rename('John');

Immutability
// ❌ Bad
user.age++;

// ✅ Good
const updatedUser = user.withAge(user.age + 1);

Cohesion
// ❌ Bad
class User {
  calculateTax() {}
}

// ✅ Good
class TaxCalculator {
  calculate(user) {}
}

Weekly Installs
72
Repository
damianwrooby/ja…e-skills
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass