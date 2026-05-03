---
title: code-refactoring
url: https://skills.sh/supercent-io/skills-template/code-refactoring
---

# code-refactoring

skills/supercent-io/skills-template/code-refactoring
code-refactoring
Installation
$ npx skills add https://github.com/supercent-io/skills-template --skill code-refactoring
Summary

Refactor code while preserving behavior, improving clarity, and reducing complexity.

Covers five core refactoring patterns: Extract Method, DRY principle removal, conditional-to-polymorphism conversion, parameter object introduction, and SOLID principle application
Includes behavior validation workflow with pre-refactoring analysis, post-refactoring testing (unit, type, lint, snapshot), and change documentation
Provides refactoring checklist covering function length, parameter count, nesting depth, magic numbers, and self-documentation
Enforces mandatory constraints: write tests first, change one thing at a time, preserve all functional behavior
Supports multi-agent workflows with role-based verification across orchestration, analysis, and test execution phases
SKILL.md
Code Refactoring
When to use this skill
Code review: Discovering complex or duplicated code
Before adding new features: Cleaning up existing code
After bug fixes: Removing root causes
Resolving technical debt: Regular refactoring
Instructions
Step 1: Extract Method

Before (long function):

function processOrder(order: Order) {
  // Validation
  if (!order.items || order.items.length === 0) {
    throw new Error('Order must have items');
  }
  if (!order.customerId) {
    throw new Error('Order must have customer');
  }

  // Price calculation
  let total = 0;
  for (const item of order.items) {
    total += item.price * item.quantity;
  }
  const tax = total * 0.1;
  const shipping = total > 100 ? 0 : 10;
  const finalTotal = total + tax + shipping;

  // Inventory check
  for (const item of order.items) {
    const product = await db.product.findUnique({ where: { id: item.productId } });
    if (product.stock < item.quantity) {
      throw new Error(`Insufficient stock for ${product.name}`);
    }
  }

  // Create order
  const newOrder = await db.order.create({
    data: {
      customerId: order.customerId,
      items: order.items,
      total: finalTotal,
      status: 'pending'
    }
  });

  return newOrder;
}


After (method extraction):

async function processOrder(order: Order) {
  validateOrder(order);
  const total = calculateTotal(order);
  await checkInventory(order);
  return await createOrder(order, total);
}

function validateOrder(order: Order) {
  if (!order.items || order.items.length === 0) {
    throw new Error('Order must have items');
  }
  if (!order.customerId) {
    throw new Error('Order must have customer');
  }
}

function calculateTotal(order: Order): number {
  const subtotal = order.items.reduce((sum, item) => sum + item.price * item.quantity, 0);
  const tax = subtotal * 0.1;
  const shipping = subtotal > 100 ? 0 : 10;
  return subtotal + tax + shipping;
}

async function checkInventory(order: Order) {
  for (const item of order.items) {
    const product = await db.product.findUnique({ where: { id: item.productId } });
    if (product.stock < item.quantity) {
      throw new Error(`Insufficient stock for ${product.name}`);
    }
  }
}

async function createOrder(order: Order, total: number) {
  return await db.order.create({
    data: {
      customerId: order.customerId,
      items: order.items,
      total,
      status: 'pending'
    }
  });
}

Step 2: Remove Duplication

Before (duplication):

async function getActiveUsers() {
  return await db.user.findMany({
    where: { status: 'active', deletedAt: null },
    select: { id: true, name: true, email: true }
  });
}

async function getActivePremiumUsers() {
  return await db.user.findMany({
    where: { status: 'active', deletedAt: null, plan: 'premium' },
    select: { id: true, name: true, email: true }
  });
}


After (extract common logic):

type UserFilter = {
  plan?: string;
};

async function getActiveUsers(filter: UserFilter = {}) {
  return await db.user.findMany({
    where: {
      status: 'active',
      deletedAt: null,
      ...filter
    },
    select: { id: true, name: true, email: true }
  });
}

// Usage
const allActiveUsers = await getActiveUsers();
const premiumUsers = await getActiveUsers({ plan: 'premium' });

Step 3: Replace Conditional with Polymorphism

Before (long if-else):

class PaymentProcessor {
  process(payment: Payment) {
    if (payment.method === 'credit_card') {
      // Credit card processing
      const cardToken = this.tokenizeCard(payment.card);
      const charge = this.chargeCreditCard(cardToken, payment.amount);
      return charge;
    } else if (payment.method === 'paypal') {
      // PayPal processing
      const paypalOrder = this.createPayPalOrder(payment.amount);
      const approval = this.getPayPalApproval(paypalOrder);
      return approval;
    } else if (payment.method === 'bank_transfer') {
      // Bank transfer processing
      const transfer = this.initiateBankTransfer(payment.account, payment.amount);
      return transfer;
    }
  }
}


After (polymorphism):

interface PaymentMethod {
  process(payment: Payment): Promise<PaymentResult>;
}

class CreditCardPayment implements PaymentMethod {
  async process(payment: Payment): Promise<PaymentResult> {
    const cardToken = await this.tokenizeCard(payment.card);
    return await this.chargeCreditCard(cardToken, payment.amount);
  }
}

class PayPalPayment implements PaymentMethod {
  async process(payment: Payment): Promise<PaymentResult> {
    const order = await this.createPayPalOrder(payment.amount);
    return await this.getPayPalApproval(order);
  }
}

class BankTransferPayment implements PaymentMethod {
  async process(payment: Payment): Promise<PaymentResult> {
    return await this.initiateBankTransfer(payment.account, payment.amount);
  }
}

class PaymentProcessor {
  private methods: Map<string, PaymentMethod> = new Map([
    ['credit_card', new CreditCardPayment()],
    ['paypal', new PayPalPayment()],
    ['bank_transfer', new BankTransferPayment()]
  ]);

  async process(payment: Payment): Promise<PaymentResult> {
    const method = this.methods.get(payment.method);
    if (!method) {
      throw new Error(`Unknown payment method: ${payment.method}`);
    }
    return await method.process(payment);
  }
}

Step 4: Introduce Parameter Object

Before (many parameters):

function createUser(
  name: string,
  email: string,
  password: string,
  age: number,
  country: string,
  city: string,
  postalCode: string,
  phoneNumber: string
) {
  // ...
}


After (grouped into object):

interface UserProfile {
  name: string;
  email: string;
  password: string;
  age: number;
}

interface Address {
  country: string;
  city: string;
  postalCode: string;
}

interface CreateUserParams {
  profile: UserProfile;
  address: Address;
  phoneNumber: string;
}

function createUser(params: CreateUserParams) {
  const { profile, address, phoneNumber } = params;
  // ...
}

// Usage
createUser({
  profile: { name: 'John', email: 'john@example.com', password: 'xxx', age: 30 },
  address: { country: 'US', city: 'NYC', postalCode: '10001' },
  phoneNumber: '+1234567890'
});

Step 5: Apply SOLID Principles

Single Responsibility:

// ❌ Bad example: multiple responsibilities
class User {
  constructor(public name: string, public email: string) {}

  save() {
    // Save to DB
  }

  sendEmail(subject: string, body: string) {
    // Send email
  }

  generateReport() {
    // Generate report
  }
}

// ✅ Good example: separated responsibilities
class User {
  constructor(public name: string, public email: string) {}
}

class UserRepository {
  save(user: User) {
    // Save to DB
  }
}

class EmailService {
  send(to: string, subject: string, body: string) {
    // Send email
  }
}

class UserReportGenerator {
  generate(user: User) {
    // Generate report
  }
}

Output format
Refactoring Checklist
- [ ] Function does one thing only (SRP)
- [ ] Function name clearly describes what it does
- [ ] Function is 20 lines or fewer (guideline)
- [ ] 3 or fewer parameters
- [ ] No duplicate code (DRY)
- [ ] if nesting is 2 levels or fewer
- [ ] No magic numbers (extract as constants)
- [ ] Understandable without comments (self-documenting)

Constraints
Mandatory Rules (MUST)
Test first: Write tests before refactoring
Small steps: Change one thing at a time
Behavior preservation: No functional changes
Prohibited (MUST NOT)
Multiple tasks simultaneously: No refactoring + feature addition at the same time
Refactoring without tests: Risk of regression
Best practices
Boy Scout Rule: Leave code cleaner than you found it
Refactoring timing: Red-Green-Refactor (TDD)
Incremental improvement: Consistency over perfection
Behavior preservation: Refactoring involves no functional changes
Small commits: Commit in focused units
Behavior Validation (Code Simplifier Integration)
Step A: Understand Current Behavior

Fully understand current behavior before refactoring:

## Behavior Analysis

### Inputs
- [list of input parameters]
- [types and constraints]

### Outputs
- [return values]
- [side effects]

### Invariants
- [conditions that must always be true]
- [edge cases]

### Dependencies
- [external dependencies]
- [state dependencies]

Step B: Validate After Refactoring
# 1. Run tests
npm test -- --coverage

# 2. Type check
npx tsc --noEmit

# 3. Lint check
npm run lint

# 4. Compare with previous behavior (snapshot tests)
npm test -- --updateSnapshot

Step C: Document Changes
## Refactoring Summary

### Changes Made
1. [Change 1]: [reason]
2. [Change 2]: [reason]

### Behavior Preserved
- [x] Same input → same output
- [x] Same side effects
- [x] Same error handling

### Risks & Follow-ups
- [potential risks]
- [follow-up tasks]

### Test Status
- [ ] Unit tests: passing
- [ ] Integration tests: passing
- [ ] E2E tests: passing

Troubleshooting
Issue: Tests fail after refactor

Cause: Behavior change occurred Solution: Revert and isolate the change, then retry

Issue: Code still complex

Cause: Multiple responsibilities mixed in one function Solution: Extract into smaller units with clear boundaries

Issue: Performance regression

Cause: Inefficient abstraction introduced Solution: Profile and optimize the hot path

Multi-Agent Workflow
Validation & Retrospectives
Round 1 (Orchestrator): Validate behavior preservation checklist
Round 2 (Analyst): Complexity and duplication analysis
Round 3 (Executor): Test or static analysis verification
Agent Roles
Agent	Role
Claude	Refactoring plan, code transformation
Gemini	Large-scale codebase analysis, pattern detection
Codex	Test execution, build verification
Workflow Example
# 1. Gemini: Codebase analysis
ask-gemini "@src/ extract list of high-complexity functions"

# 2. Claude: Refactoring plan and execution
# Work based on IMPLEMENTATION_PLAN.md

# 3. Codex: Verification
codex-cli shell "npm test && npm run lint"

References
Refactoring (Martin Fowler)
Clean Code (Robert C. Martin)
SOLID Principles
Metadata
Version
Current Version: 1.0.0
Last Updated: 2025-01-01
Compatible Platforms: Claude, ChatGPT, Gemini
Related Skills
code-review
backend-testing
Tags

#refactoring #code-quality #DRY #SOLID #design-patterns #clean-code

Examples
Example 1: Basic usage
Example 2: Advanced usage
Weekly Installs
11.9K
Repository
supercent-io/sk…template
GitHub Stars
88
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass