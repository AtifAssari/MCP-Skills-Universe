---
title: code-style
url: https://skills.sh/bumgeunsong/daily-writing-friends/code-style
---

# code-style

skills/bumgeunsong/daily-writing-friends/code-style
code-style
Installation
$ npx skills add https://github.com/bumgeunsong/daily-writing-friends --skill code-style
SKILL.md
Code Style
Core Philosophy

Code should be self-explanatory. Comments explain WHY, not WHAT.

Function Design
Small and Focused

Each function should do one thing well. Split larger functions into smaller, independent methods.

Either Call Or Pass

A function should either:

Call other methods (high-level orchestration), OR
Pass data / perform low-level operations

Never mix abstraction levels in one function body. This is the Single Level of Abstraction (SLA) principle.

// BAD - mixed abstraction levels
function processOrder(order: Order) {
  validateOrder(order);                    // high-level call
  const tax = order.total * 0.1;           // low-level calculation
  await sendConfirmation(order);           // high-level call
  db.insert('orders', { ...order, tax });  // low-level operation
}

// GOOD - consistent abstraction
function processOrder(order: Order) {
  validateOrder(order);
  const enrichedOrder = calculateTaxes(order);
  await persistOrder(enrichedOrder);
  await sendConfirmation(enrichedOrder);
}

Never Use If With Else

Prefer guard clauses or polymorphism over if-else blocks.

// BAD
function getDiscount(user: User) {
  if (user.isPremium) {
    return 0.2;
  } else {
    return 0;
  }
}

// GOOD - guard clause
function getDiscount(user: User) {
  if (!user.isPremium) return 0;
  return 0.2;
}

Avoid Flag Arguments

Flag arguments indicate a function is doing more than one thing.

// BAD
function createUser(data: UserData, sendEmail: boolean) { ... }

// GOOD
function createUser(data: UserData) { ... }
function createUserAndNotify(data: UserData) { ... }

Naming
Expressive Over Comments
// BAD
const d = 7; // days in recovery period

// GOOD
const daysInRecoveryPeriod = 7;

No Abbreviations
// BAD
getUserCmt(), calcRecReq()

// GOOD
getUserComment(), calculateRecoveryRequirement()

Booleans Read Like Questions
// BAD
eligible, recovery

// GOOD
isEligible, isRecovering, hasPassedDeadline

Collections Use Plurals
// BAD
const post = getPosts();

// GOOD
const posts = getPosts();

Use Intermediate Variables
const hasRequiredPostCount = posts.length >= 2;
const isWithinRecoveryWindow = new Date() <= recoveryDeadline;
const canStartRecovery = hasRequiredPostCount && isWithinRecoveryWindow;

Constants
No Magic Numbers
// BAD
if (streak >= 21) { ... }

// GOOD
const GOLD_BADGE_STREAK_THRESHOLD = 21;
if (streak >= GOLD_BADGE_STREAK_THRESHOLD) { ... }

Comments
Sparingly and Meaningful
Code tells HOW, comments tell WHY
If you need a comment, first try better naming
Use TODO: for known limitations
Delete obsolete comments
Weekly Installs
28
Repository
bumgeunsong/dai…-friends
GitHub Stars
9
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass