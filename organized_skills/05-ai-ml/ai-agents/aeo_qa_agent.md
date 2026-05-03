---
rating: ⭐⭐⭐⭐⭐
title: aeo-qa-agent
url: https://skills.sh/ivzc07/aeo-skills/aeo-qa-agent
---

# aeo-qa-agent

skills/ivzc07/aeo-skills/aeo-qa-agent
aeo-qa-agent
Installation
$ npx skills add https://github.com/ivzc07/aeo-skills --skill aeo-qa-agent
SKILL.md
AEO QA Agent

Purpose: Internal code reviewer with veto power. Reviews all changes before commit and blocks if critical issues found.

When to Review
After logical work unit complete - Feature implemented, bug fixed
Before suggesting completion - Before saying "task is done"
Before git commit - Final gate before committing changes
Review Categories
1. Security Issues (VETO POWER)

Automatic Veto - Block and fix immediately:

SQL Injection:

// ❌ VULNERABLE
const query = `SELECT * FROM users WHERE id = ${userId}`

// ✅ SECURE
const query = 'SELECT * FROM users WHERE id = $1'
await db.query(query, [userId])


XSS (Cross-Site Scripting):

// ❌ VULNERABLE
<div>{userInput}</div>

// ✅ SECURE
<div>{escape(userInput)}</div>
// or
<div dangerouslySetInnerHTML={{__html: DOMPurify.sanitize(userInput)}} />


CSRF (Cross-Site Request Forgery):

// ❌ VULNERABLE - No CSRF protection
app.post('/api/update', (req, res) => { ... })

// ✅ SECURE
import csrf from 'csurf'
const csrfProtection = csrf({ cookie: true })
app.post('/api/update', csrfProtection, (req, res) => { ... })


Hardcoded Credentials:

// ❌ VULNERABLE
const apiKey = "sk_live_1234567890"

// ✅ SECURE
const apiKey = process.env.API_KEY


Missing Input Validation:

// ❌ VULNERABLE
app.post('/api/users', (req, res) => {
  db.query(`INSERT INTO users (email) VALUES ('${req.body.email}')`)
})

// ✅ SECURE
import { body, validationResult } from 'express-validator'

app.post('/api/users',
  body('email').isEmail().normalizeEmail(),
  (req, res) => {
    const errors = validationResult(req)
    if (!errors.isEmpty()) return res.status(400).json({ errors })
    db.query('INSERT INTO users (email) VALUES ($1)', [req.body.email])
  }
)


Insecure Cryptography:

// ❌ VULNERABLE - MD5 is broken
const hash = md5(password)

// ✅ SECURE
import bcrypt from 'bcrypt'
const hash = await bcrypt.hash(password, 10)


Auth Bypasses:

// ❌ VULNERABLE
if (user.apiKey === userProvidedKey) { /* No rate limiting */ }

// ✅ SECURE
import rateLimit from 'express-rate-limit'
const limiter = rateLimit({ windowMs: 60000, max: 10 })
app.use('/api/auth', limiter)

2. Code Smells (Auto-Fix)

Remove immediately without asking:

Console Logs:

// ❌ REMOVE
console.log('debug:', variable)
console.error('error:', error)

// ✅ Use proper logging
import logger from './logger.js'
logger.info({ variable })
logger.error({ error })


Debugger Statements:

// ❌ REMOVE
debugger;


Unused Imports:

// ❌ REMOVE
import React, { useState, useEffect } from 'react'
// useEffect never used


TODO/FIXME without Tickets:

// ❌ FLAG - Needs ticket reference
// TODO: Refactor this
// FIXME: This is buggy

// ✅ ACCEPTABLE
// TODO: Refactor this - Ticket #1234
// FIXME: Bug in production - https://github.com/org/repo/issues/567


Inconsistent Naming:

// ❌ INCONSISTENT
const userData = getUser()
const user_data = getUserById()
const USER_DATA = getUserByEmail()

// ✅ CONSISTENT (pick one style)
const userData = getUser()
const userDataById = getUserById()
const userDataByEmail = getUserByEmail()


Magic Numbers:

// ❌ MAGIC NUMBER
if (user.age > 13) { /* ... */ }

// ✅ EXTRACT CONSTANT
const MINIMUM_AGE = 13
if (user.age > MINIMUM_AGE) { /* ... */ }


Duplicate Code:

// ❌ DUPLICATE
function getUserData(id) {
  const user = db.query('SELECT * FROM users WHERE id = $1', [id])
  return { id: user.id, name: user.name, email: user.email }
}

function getUserProfile(id) {
  const user = db.query('SELECT * FROM users WHERE id = $1', [id])
  return { id: user.id, name: user.name, email: user.email }
}

// ✅ EXTRACT FUNCTION
function formatUser(user) {
  return { id: user.id, name: user.name, email: user.email }
}

function getUserData(id) {
  const user = db.query('SELECT * FROM users WHERE id = $1', [id])
  return formatUser(user)
}

function getUserProfile(id) {
  const user = db.query('SELECT * FROM users WHERE id = $1', [id])
  return formatUser(user)
}

3. Test Coverage

Flag if missing:

New Features Without Tests:

❌ New component but no test file
Component: /components/UserForm.tsx
Expected: /components/__tests__/UserForm.test.tsx

Action: Add test file before commit


Edge Cases Not Covered:

❌ Tests don't cover edge cases
Function: validateEmail(email)
Tests: ✓ Valid email
       ✗ Invalid format
       ✗ Null/undefined
       ✗ Edge cases (+ alias, unicode)

Action: Add edge case tests

4. Architecture Violations

Detect and flag:

Circular Dependencies:

// ❌ CIRCULAR
// fileA.js imports from fileB.js
// fileB.js imports from fileA.js

Action: Break cycle by extracting shared code


Layer Violations:

// ❌ PRESENTATION LAYER CALLING DATABASE
// /components/UserList.tsx
import db from './database.js'
const users = db.query('SELECT * FROM users')

// ✅ CORRECT
// /components/UserList.tsx
import { getUsers } from './api/users.js'
const users = await getUsers()

// /api/users.js
import db from './database.js'
export function getUsers() {
  return db.query('SELECT * FROM users')
}


Breaking Encapsulation:

// ❌ ACCESSING PRIVATE STATE
class User {
  #passwordHash  // Private field
}
user.#passwordHash = 'new'  // ❌

// ✅ USE PUBLIC API
class User {
  #passwordHash
  setPassword(newPassword) {
    this.#passwordHash = hash(newPassword)
  }
}
user.setPassword('new')

Review Process
Step 1: Scan for VETO Issues

Check all changed files for security issues. If found:

🚨 VETO - SECURITY ISSUE DETECTED

File: path/to/file.js:Line
Issue: SQL Injection vulnerability

Current Code:
```javascript
const query = `SELECT * FROM users WHERE id = ${userId}`


Required Fix:

const query = 'SELECT * FROM users WHERE id = $1'
await db.query(query, [userId])


Action: BLOCKED - Fix required before commit


**Stop execution and wait for fix.**

### Step 2: Check for Auto-Fix Issues

Scan for code smells. Apply fixes automatically:

- Remove console.log statements
- Remove debugger statements
- Remove unused imports
- Extract magic numbers

**Report fixes applied:**


🔧 AUTO-FIXES APPLIED

• Removed 3 console.log statements (auth.js:45,47,52) • Removed 1 debugger statement (utils.js:123) • Extracted constant MAX_RETRY_COUNT (api.js:78)


### Step 3: Check Test Coverage

Verify tests exist and cover edge cases:



⚠️ TEST COVERAGE ISSUES

Missing Tests: • /components/UserForm.tsx - No test file • /utils/validation.ts - Edge cases not covered

Action: Add tests before proceeding


### Step 4: Check Architecture

If architecture violations found, invoke aeo-architecture skill for detailed analysis.

### Step 5: Final Report

If all checks pass:



✅ QA REVIEW PASSED

Changed Files: 5 Security Issues: 0 Code Smells: 0 (2 auto-fixed) Test Coverage: ✓ Architecture: ✓

Ready to commit.


## Veto Process

When a VETO issue is found:

1. **Stop execution immediately**
2. **Output issue with location**
3. **Show current code vs required fix**
4. **Block until resolved**
5. **Re-review after fix**

## Auto-Fix Rules

**Apply without asking:**
- Remove console.log, console.error, console.warn
- Remove debugger statements
- Remove obviously unused imports
- Extract simple magic numbers (integers, common values)

**Flag for review:**
- Complex refactoring (duplicate code extraction)
- Architectural changes
- Test additions

## Review Timing

**Mandatory Reviews:**
- After feature implementation
- Before saying "done"
- Before git commit

**Skip Review:**
- Reading files
- Gathering information
- Planning

## Integration

Called by aeo-core after task execution completes.

If QA veto occurs:
1. Inform human of issue
2. Wait for fix
3. Re-review
4. Only pass if clean

## Example Session



[Task implementation completes]

AEO: [Invoking aeo-qa-agent]

QA: Scanning files...

🔧 AUTO-FIXES APPLIED
• Removed 2 console.log statements
• Extracted constant MAX_ATTEMPTS

✅ QA REVIEW PASSED

Changed Files: 3
Security Issues: 0
Code Smells: 0
Test Coverage: ✓
Architecture: ✓


AEO: Ready to commit changes.

Human: Yes

AEO: [Commits changes]

Weekly Installs
15
Repository
ivzc07/aeo-skills
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail