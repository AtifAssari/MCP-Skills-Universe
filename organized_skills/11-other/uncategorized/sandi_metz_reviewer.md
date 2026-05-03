---
rating: ⭐⭐⭐
title: sandi-metz-reviewer
url: https://skills.sh/el-feo/ai-context/sandi-metz-reviewer
---

# sandi-metz-reviewer

skills/el-feo/ai-context/sandi-metz-reviewer
sandi-metz-reviewer
Installation
$ npx skills add https://github.com/el-feo/ai-context --skill sandi-metz-reviewer
SKILL.md
Sandi Metz Code Reviewer

Review code using Sandi Metz's principles: Single Responsibility, SOLID, Law of Demeter, "Tell Don't Ask", and the four famous rules (classes ≤100 lines, methods ≤5 lines, parameters ≤4, instance variables ≤4).

Quick Start

For code review requests, follow this workflow:

Parse the code - Understand structure: classes, methods, dependencies
Apply checks - Run through all principle categories
Provide feedback - Clear issues with actionable suggestions
Format output - Organized by principle with severity levels
Review Checks
1. Sandi Metz's Four Rules

Check every class and method:

Classes: Max 100 lines
Methods: Max 5 lines (excluding blank lines and end statements)
Parameters: Max 4 per method
Instance Variables: Max 4 per class

Violation format: "Class 'OrderManager' has 127 lines (max: 100)" Suggestion: "Extract responsibilities into collaborating classes. Ask: Can this class be described in one sentence?"

2. Single Responsibility Principle (SRP)

Indicators of violations:

Class has >7 public methods → Too many responsibilities
Method name contains "and" → Doing multiple things
Method doesn't use any instance variables → Feature Envy, belongs elsewhere
Hard to describe class in one sentence → Multiple responsibilities

Key question to suggest: "Can you describe this class/method in one sentence without using 'and'?"

3. Dependency Management

Check for:

Explicit instantiation (ClassName.new) → Suggest dependency injection
Message chains (object.property.method.value) → Law of Demeter violation
Inappropriate intimacy (accessing internals of other objects) → Use proper interfaces

Law of Demeter: "Only talk to immediate friends"

✅ self.method
✅ method_parameter.method
✅ @instance_variable.method
❌ object.attribute.another_attribute.method
4. Tell, Don't Ask

Anti-pattern:

if user.admin?
  user.delete_all
end


Better:

user.perform_admin_action(:delete_all)


Principle: Objects should make their own decisions, not have their state queried and then acted upon.

5. Open/Closed Principle

Identify candidates for polymorphism:

Case statements on type → Create subclasses with polymorphic behavior
If-elsif chains based on type → Replace with strategy pattern
Type checking (if object.is_a?(Type)) → Use duck typing or polymorphism

Pattern from 99 Bottles: Replace conditionals with polymorphic message sends to objects that know their own behavior.

6. Code Smells (18 types)

Structural:

Long Method (>5 lines)
Large Class (>100 lines)
Long Parameter List (>4 params)
Data Clump (same params together repeatedly)

Coupling:

Feature Envy (method uses data from another class more than own)
Message Chains (Law of Demeter violations)
Inappropriate Intimacy (classes too tightly coupled)

Conditional Logic:

Conditional Complexity (nested if-elsif)
Case Statements (candidate for polymorphism)
Speculative Generality (code added "just in case")

Naming:

Vague names (Manager, Handler, Processor, Data)
Methods with "and" (doing multiple things)
Flag parameters (boolean params that change behavior)

Comments:

Comments explaining "what" code does → Code should be self-documenting
Keep comments that explain "why" decisions were made
7. Naming Conventions

Poor names that indicate design problems:

Classes: Manager, Handler, Processor, Controller, Helper, Util
Methods: process, handle, manage, do, data, info
With "and": save_and_send → Should be two methods

Principle: Names should reveal intent. If you can't name it clearly, it probably has unclear responsibilities.

Output Format

Structure feedback by principle area:

📏 SANDI METZ'S FOUR RULES
✓ Pass: Class 'Order' size good (45 lines)
⚠️  Warning: Method 'process' has 12 lines (max: 5) [line 23]
    💡 Extract smaller methods with intention-revealing names

🎯 SINGLE RESPONSIBILITY
ℹ️  Info: Class 'OrderManager' has 9 public methods [line 1]
    💡 Ask: Can this class be described in one sentence?

🔗 DEPENDENCIES
❌ Error: Message chain detected: customer.address.street.name [line 45]
    💡 Use delegation. Add customer.street_name method

💬 TELL, DON'T ASK  
⚠️  Warning: Conditional based on object query [line 67]
    💡 Let objects make their own decisions

📊 SUMMARY
✓ Passes: 12
ℹ️  Info: 5
⚠️  Warnings: 8
❌ Errors: 2

Severity Levels
❌ Error: Serious violations (accessing internals, tight coupling)
⚠️ Warning: Rule violations, should be fixed
ℹ️ Info: Suggestions, best practices
✓ Pass: Correctly following principles
Shameless Green Philosophy

From 99 Bottles of OOP - encourage this refactoring approach:

Start with Shameless Green - Write simplest code that works
Wait for duplication - Don't abstract too early
Follow Flocking Rules:
Find things that are most alike
Find smallest difference between them
Make simplest change to remove difference
Converge on abstractions - Let patterns emerge

Key wisdom: "Make the change easy, then make the easy change"

Refactoring Patterns

Suggest these when appropriate:

Extract Method: When methods too long

# Before: 15-line method
# After: 3-line method calling 3 extracted methods (each ≤5 lines)


Extract Class: When classes have too many responsibilities

# Before: OrderManager with 8 instance variables
# After: Order + Payment + Shipping (each with ≤4 instance variables)


Replace Conditional with Polymorphism: For case/if-elsif on type

# Before: case type when 'book'... when 'electronics'...
# After: Book.price, Electronics.price (each knows own behavior)


Introduce Parameter Object: For long parameter lists

# Before: create_order(name, email, street, city, state, zip)
# After: create_order(customer_info)

Code Examples

When showing before/after examples, keep them concise:

Before (violations):

class OrderManager
  def process(name, email, address, phone, items, discount, method)
    # 20 lines of nested conditionals
  end
end


After (principles applied):

class Order
  def total
    items.sum(&:price) - discount.amount
  end
end

class Discount
  def amount
    # polymorphic behavior
  end
end

When Breaking Rules is OK

Sandi Metz: "Break them only if you have a good reason and you've tried not to."

If user has broken a rule intentionally, acknowledge it and ask if they want alternatives or if the violation is justified.

References

For deeper understanding, the skill is based on:

Practical Object-Oriented Design in Ruby (POODR) by Sandi Metz
99 Bottles of OOP by Sandi Metz, Katrina Owen, TJ Stankus

Key talks (available online):

"Nothing is Something" - RailsConf 2015
"All the Little Things" - RailsConf 2014
Execution Notes
Focus on one principle area at a time
Provide specific line numbers when possible
Always include actionable suggestions, not just criticism
Celebrate what's done well (✓ Pass messages)
Keep feedback encouraging - design is about making code easier to change, not achieving perfection
Weekly Installs
13
Repository
el-feo/ai-context
GitHub Stars
9
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn