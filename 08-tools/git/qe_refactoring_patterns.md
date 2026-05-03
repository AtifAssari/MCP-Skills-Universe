---
title: qe-refactoring-patterns
url: https://skills.sh/proffesor-for-testing/agentic-qe/qe-refactoring-patterns
---

# qe-refactoring-patterns

skills/proffesor-for-testing/agentic-qe/qe-refactoring-patterns
qe-refactoring-patterns
Installation
$ npx skills add https://github.com/proffesor-for-testing/agentic-qe --skill qe-refactoring-patterns
SKILL.md
Refactoring Patterns

<default_to_action> When refactoring:

ENSURE tests pass (never refactor without tests)
MAKE small change (one refactoring at a time)
RUN tests (must stay green)
COMMIT (save progress)
REPEAT

Safe Refactoring Cycle:

npm test               # Green ✅
# Make ONE small change
npm test               # Still green ✅
git commit -m "refactor: extract calculateTotal"
# Repeat


Code Smells → Refactoring:

Smell	Refactoring
Long method (>20 lines)	Extract Method
Large class	Extract Class
Long parameter list (>3)	Introduce Parameter Object
Duplicated code	Extract Method/Class
Complex conditional	Decompose Conditional
Magic numbers	Named Constants
Nested loops	Replace Loop with Pipeline

NEVER REFACTOR:

Without tests (write tests first)
When deadline is tomorrow
Code you don't understand
Code that works and won't be touched </default_to_action>
Quick Reference Card
Common Refactorings
Pattern	Before	After
Extract Method	50-line function	5 small functions
Extract Class	Class doing 5 things	5 single-purpose classes
Parameter Object	fn(a,b,c,d,e,f)	fn(options)
Replace Conditional	if (type === 'a') {...}	Polymorphism
Pipeline	Nested loops	.filter().map().reduce()
The Rule of Three
First time → Just do it
Second time → Wince and duplicate
Third time → Refactor
Key Patterns
Extract Method
// Before: Long method
function processOrder(order) {
  // 50 lines of validation, calculation, saving, emailing...
}

// After: Clear responsibilities
function processOrder(order) {
  validateOrder(order);
  const pricing = calculatePricing(order);
  const saved = saveOrder(order, pricing);
  sendConfirmationEmail(saved);
  return saved;
}

Replace Loop with Pipeline
// Before
let results = [];
for (let item of items) {
  if (item.inStock) {
    results.push(item.name.toUpperCase());
  }
}

// After
const results = items
  .filter(item => item.inStock)
  .map(item => item.name.toUpperCase());

Decompose Conditional
// Before
if (order.total > 1000 && customer.isPremium && allInStock(order)) {
  return 'FREE_SHIPPING';
}

// After
function isEligibleForFreeShipping(order, customer) {
  return isLargeOrder(order) &&
         isPremiumCustomer(customer) &&
         allInStock(order);
}

Refactoring Anti-Patterns
❌ Anti-Pattern	Problem	✅ Better
Without tests	No safety net	Write tests first
Big bang	Rewrite everything	Small incremental steps
For perfection	Endless tweaking	Good enough, move on
Premature abstraction	Pattern not clear yet	Wait for Rule of Three
During feature work	Mixed changes	Separate commits
Agent Integration
// Detect code smells
const smells = await Task("Detect Code Smells", {
  source: 'src/services/',
  patterns: ['long-method', 'large-class', 'duplicate-code']
}, "qe-quality-analyzer");

// Safe refactoring with test verification
await Task("Verify Refactoring", {
  beforeCommit: 'abc123',
  afterCommit: 'def456',
  expectSameBehavior: true
}, "qe-test-executor");

Agent Coordination Hints
Memory Namespace
aqe/refactoring/
├── smells/*          - Detected code smells
├── suggestions/*     - Refactoring recommendations
├── verifications/*   - Behavior preservation checks
└── history/*         - Refactoring log

Fleet Coordination
const refactoringFleet = await FleetManager.coordinate({
  strategy: 'refactoring',
  agents: [
    'qe-quality-analyzer',   // Identify targets
    'qe-test-generator',     // Add safety tests
    'qe-test-executor',      // Verify behavior
    'qe-test-refactorer'     // TDD refactor phase
  ],
  topology: 'sequential'
});

Related Skills
tdd-london-chicago - TDD refactor phase
code-review-quality - Review refactored code
xp-practices - Collective ownership
Remember

Refactoring is NOT:

Adding features
Fixing bugs
Performance optimization
Rewriting from scratch

Refactoring IS:

Improving structure
Making code clearer
Reducing complexity
Removing duplication
Without changing behavior

Always have tests. Always take small steps. Always keep tests green.

Weekly Installs
42
Repository
proffesor-for-t…entic-qe
GitHub Stars
334
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass