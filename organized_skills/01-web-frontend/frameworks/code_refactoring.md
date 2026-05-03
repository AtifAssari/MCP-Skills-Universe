---
rating: ⭐⭐
title: code-refactoring
url: https://skills.sh/skillcreatorai/ai-agent-skills/code-refactoring
---

# code-refactoring

skills/skillcreatorai/ai-agent-skills/code-refactoring
code-refactoring
Installation
$ npx skills add https://github.com/skillcreatorai/ai-agent-skills --skill code-refactoring
Summary

Structured patterns and techniques for improving code quality through safe, behavior-preserving refactoring.

Covers common code smells including long methods, deeply nested conditionals, primitive obsession, and feature envy with before/after examples
Provides core refactoring techniques: extract method, replace conditional with polymorphism, introduce parameter objects, and replace magic numbers with constants
Emphasizes safe refactoring workflow: ensure test coverage first, make small focused changes, run tests after each step, and commit frequently
Includes decision framework for when to refactor (before features, after tests pass, during code review) and when to avoid it (without tests, under tight deadlines, on code being replaced)
SKILL.md
Code Refactoring
Refactoring Principles
When to Refactor
Before adding new features (make change easy, then make easy change)
After getting tests passing (red-green-refactor)
When you see code smells
During code review feedback
When NOT to Refactor
Without tests covering the code
Under tight deadlines with no safety net
Code that will be replaced soon
When you don't understand what the code does
Common Code Smells
Long Methods
// BEFORE: Method doing too much
function processOrder(order: Order) {
  // 100 lines of validation, calculation, notification, logging...
}

// AFTER: Extract into focused methods
function processOrder(order: Order) {
  validateOrder(order);
  const total = calculateTotal(order);
  saveOrder(order, total);
  notifyCustomer(order);
}

Deeply Nested Conditionals
// BEFORE: Arrow code
function getDiscount(user: User, order: Order) {
  if (user) {
    if (user.isPremium) {
      if (order.total > 100) {
        if (order.items.length > 5) {
          return 0.2;
        }
      }
    }
  }
  return 0;
}

// AFTER: Early returns (guard clauses)
function getDiscount(user: User, order: Order) {
  if (!user) return 0;
  if (!user.isPremium) return 0;
  if (order.total <= 100) return 0;
  if (order.items.length <= 5) return 0;
  return 0.2;
}

Primitive Obsession
// BEFORE: Primitives everywhere
function createUser(name: string, email: string, phone: string) {
  if (!email.includes('@')) throw new Error('Invalid email');
  // more validation...
}

// AFTER: Value objects
class Email {
  constructor(private value: string) {
    if (!value.includes('@')) throw new Error('Invalid email');
  }
  toString() { return this.value; }
}

function createUser(name: string, email: Email, phone: Phone) {
  // Email is already validated
}

Feature Envy
// BEFORE: Method uses another object's data extensively
function calculateShipping(order: Order) {
  const address = order.customer.address;
  const weight = order.items.reduce((sum, i) => sum + i.weight, 0);
  const distance = calculateDistance(address.zip);
  return weight * distance * 0.01;
}

// AFTER: Move method to where the data is
class Order {
  calculateShipping() {
    return this.totalWeight * this.customer.shippingDistance * 0.01;
  }
}

Refactoring Techniques
Extract Method
// Identify a code block that does one thing
// Move it to a new method with a descriptive name
// Replace original code with method call

function printReport(data: ReportData) {
  // Extract this block...
  const header = `Report: ${data.title}\nDate: ${data.date}\n${'='.repeat(40)}`;
  console.log(header);

  // ...into a method
  printHeader(data);
}

Replace Conditional with Polymorphism
// BEFORE: Switch on type
function getArea(shape: Shape) {
  switch (shape.type) {
    case 'circle': return Math.PI * shape.radius ** 2;
    case 'rectangle': return shape.width * shape.height;
    case 'triangle': return shape.base * shape.height / 2;
  }
}

// AFTER: Polymorphic classes
interface Shape {
  getArea(): number;
}

class Circle implements Shape {
  constructor(private radius: number) {}
  getArea() { return Math.PI * this.radius ** 2; }
}

class Rectangle implements Shape {
  constructor(private width: number, private height: number) {}
  getArea() { return this.width * this.height; }
}

Introduce Parameter Object
// BEFORE: Too many parameters
function searchProducts(
  query: string,
  minPrice: number,
  maxPrice: number,
  category: string,
  inStock: boolean,
  sortBy: string,
  sortOrder: string
) { ... }

// AFTER: Parameter object
interface SearchParams {
  query: string;
  priceRange: { min: number; max: number };
  category?: string;
  inStock?: boolean;
  sort?: { by: string; order: 'asc' | 'desc' };
}

function searchProducts(params: SearchParams) { ... }

Replace Magic Numbers with Constants
// BEFORE
if (user.age >= 18 && order.total >= 50) {
  applyDiscount(order, 0.1);
}

// AFTER
const MINIMUM_AGE = 18;
const DISCOUNT_THRESHOLD = 50;
const STANDARD_DISCOUNT = 0.1;

if (user.age >= MINIMUM_AGE && order.total >= DISCOUNT_THRESHOLD) {
  applyDiscount(order, STANDARD_DISCOUNT);
}

Safe Refactoring Process
Ensure tests exist - Write tests if they don't
Make small changes - One refactoring at a time
Run tests after each change - Catch regressions immediately
Commit frequently - Easy to revert if something breaks
Review the diff - Make sure behavior hasn't changed
Refactoring Checklist
 Tests pass before starting
 Each change is small and focused
 Tests pass after each change
 No behavior changes (only structure)
 Code is more readable than before
 Commit message explains the refactoring
Weekly Installs
583
Repository
skillcreatorai/…t-skills
GitHub Stars
1.0K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass