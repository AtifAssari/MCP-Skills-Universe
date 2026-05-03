---
title: fp-types-ref
url: https://skills.sh/sickn33/antigravity-awesome-skills/fp-types-ref
---

# fp-types-ref

skills/sickn33/antigravity-awesome-skills/fp-types-ref
fp-types-ref
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill fp-types-ref
SKILL.md
fp-ts Quick Reference
Which Type Should I Use?
Is the operation async?
├─ NO: Does it involve errors?
│   ├─ YES → Either<Error, Value>
│   └─ NO: Might value be missing?
│       ├─ YES → Option<Value>
│       └─ NO → Just use the value
└─ YES: Does it involve errors?
    ├─ YES → TaskEither<Error, Value>
    └─ NO: Might value be missing?
        ├─ YES → TaskOption<Value>
        └─ NO → Task<Value>

Common Imports
// Core
import { pipe, flow } from 'fp-ts/function'

// Types
import * as O from 'fp-ts/Option'      // Maybe exists
import * as E from 'fp-ts/Either'      // Success or failure
import * as TE from 'fp-ts/TaskEither' // Async + failure
import * as T from 'fp-ts/Task'        // Async (no failure)
import * as A from 'fp-ts/Array'       // Array utilities

One-Line Patterns
Need	Code
Wrap nullable	O.fromNullable(value)
Default value	O.getOrElse(() => default)
Transform if exists	O.map(fn)
Chain optionals	O.flatMap(fn)
Wrap try/catch	E.tryCatch(() => risky(), toError)
Wrap async	TE.tryCatch(() => fetch(url), toError)
Run pipe	pipe(value, fn1, fn2, fn3)
Pattern Match
// Option
pipe(maybe, O.match(
  () => 'nothing',
  (val) => `got ${val}`
))

// Either
pipe(result, E.match(
  (err) => `error: ${err}`,
  (val) => `success: ${val}`
))

Weekly Installs
20
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