---
rating: ⭐⭐
title: fp-pipe-ref
url: https://skills.sh/sickn33/antigravity-awesome-skills/fp-pipe-ref
---

# fp-pipe-ref

skills/sickn33/antigravity-awesome-skills/fp-pipe-ref
fp-pipe-ref
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill fp-pipe-ref
SKILL.md
pipe & flow Quick Reference
pipe - Transform a Value
import { pipe } from 'fp-ts/function'

// pipe(startValue, fn1, fn2, fn3)
// = fn3(fn2(fn1(startValue)))

const result = pipe(
  '  hello world  ',
  s => s.trim(),
  s => s.toUpperCase(),
  s => s.split(' ')
)
// ['HELLO', 'WORLD']

flow - Create Reusable Pipeline
import { flow } from 'fp-ts/function'

// flow(fn1, fn2, fn3) returns a new function
const process = flow(
  (s: string) => s.trim(),
  s => s.toUpperCase(),
  s => s.split(' ')
)

process('  hello world  ') // ['HELLO', 'WORLD']
process('  foo bar  ')     // ['FOO', 'BAR']

When to Use
Use	When
pipe	Transform a specific value now
flow	Create reusable transformation
With fp-ts Types
import * as O from 'fp-ts/Option'
import * as A from 'fp-ts/Array'

// Option chain
pipe(
  O.fromNullable(user),
  O.map(u => u.email),
  O.getOrElse(() => 'no email')
)

// Array chain
pipe(
  users,
  A.filter(u => u.active),
  A.map(u => u.name)
)

Common Pattern
// Data last enables partial application
const getActiveNames = flow(
  A.filter((u: User) => u.active),
  A.map(u => u.name)
)

// Reuse anywhere
getActiveNames(users1)
getActiveNames(users2)

Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
18
Repository
sickn33/antigra…e-skills
GitHub Stars
36.1K
First Seen
Mar 15, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass