---
title: fp-option-ref
url: https://skills.sh/sickn33/antigravity-awesome-skills/fp-option-ref
---

# fp-option-ref

skills/sickn33/antigravity-awesome-skills/fp-option-ref
fp-option-ref
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill fp-option-ref
SKILL.md
Option Quick Reference

Option = value that might not exist. Some(value) or None.

When to Use
You need a quick fp-ts reference for nullable or optional values.
The task involves eliminating null checks, safe property access, or optional chaining with Option.
You want a short reference card rather than a full migration guide.
Create
import * as O from 'fp-ts/Option'

O.some(5)              // Some(5)
O.none                 // None
O.fromNullable(x)      // null/undefined → None, else Some(x)
O.fromPredicate(x > 0)(x) // false → None, true → Some(x)

Transform
O.map(fn)              // Transform inner value
O.flatMap(fn)          // Chain Options (fn returns Option)
O.filter(predicate)    // None if predicate false

Extract
O.getOrElse(() => default)  // Get value or default
O.toNullable(opt)           // Back to T | null
O.toUndefined(opt)          // Back to T | undefined
O.match(onNone, onSome)     // Pattern match

Common Patterns
import { pipe } from 'fp-ts/function'
import * as O from 'fp-ts/Option'

// Safe property access
pipe(
  O.fromNullable(user),
  O.map(u => u.profile),
  O.flatMap(p => O.fromNullable(p.avatar)),
  O.getOrElse(() => '/default-avatar.png')
)

// Array first element
import * as A from 'fp-ts/Array'
pipe(
  users,
  A.head,  // Option<User>
  O.map(u => u.name),
  O.getOrElse(() => 'No users')
)

vs Nullable
// ❌ Nullable - easy to forget checks
const name = user?.profile?.name ?? 'Guest'

// ✅ Option - explicit, composable
pipe(
  O.fromNullable(user),
  O.flatMap(u => O.fromNullable(u.profile)),
  O.map(p => p.name),
  O.getOrElse(() => 'Guest')
)


Use Option when you need to chain operations on optional values.

Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
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