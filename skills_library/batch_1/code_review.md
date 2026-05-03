---
title: code-review
url: https://skills.sh/supercent-io/skills-template/code-review
---

# code-review

skills/supercent-io/skills-template/code-review
code-review
Installation
$ npx skills add https://github.com/supercent-io/skills-template --skill code-review
Summary

Structured code review framework covering quality, security, performance, and testing standards.

Provides eight-step review methodology: context understanding, high-level architecture assessment, detailed code inspection, security audit, performance analysis, testing validation, documentation check, and constructive feedback delivery
Covers SOLID principles, naming conventions, error handling, input validation, authentication/authorization, SQL injection and XSS prevention, and resource management
Includes comprehensive checklists for functionality, code quality, security, performance, testing, and documentation with prioritization guidance (critical, important, nice-to-have)
Identifies common anti-patterns (god classes, magic numbers, deep nesting) and security vulnerabilities with corrected code examples across multiple languages
SKILL.md
Code Review
When to use this skill
Reviewing pull requests
Checking code quality
Providing feedback on implementations
Identifying potential bugs
Suggesting improvements
Security audits
Performance analysis
Instructions
Step 1: Understand the context

Read the PR description:

What is the goal of this change?
Which issues does it address?
Are there any special considerations?

Check the scope:

How many files changed?
What type of changes? (feature, bugfix, refactor)
Are tests included?
Step 2: High-level review

Architecture and design:

Does the approach make sense?
Is it consistent with existing patterns?
Are there simpler alternatives?
Is the code in the right place?

Code organization:

Clear separation of concerns?
Appropriate abstraction levels?
Logical file/folder structure?
Step 3: Detailed code review

Naming:

 Variables: descriptive, meaningful names
 Functions: verb-based, clear purpose
 Classes: noun-based, single responsibility
 Constants: UPPER_CASE for true constants
 Avoid abbreviations unless widely known

Functions:

 Single responsibility
 Reasonable length (< 50 lines ideally)
 Clear inputs and outputs
 Minimal side effects
 Proper error handling

Classes and objects:

 Single responsibility principle
 Open/closed principle
 Liskov substitution principle
 Interface segregation
 Dependency inversion

Error handling:

 All errors caught and handled
 Meaningful error messages
 Proper logging
 No silent failures
 User-friendly errors for UI

Code quality:

 No code duplication (DRY)
 No dead code
 No commented-out code
 No magic numbers
 Consistent formatting
Step 4: Security review

Input validation:

 All user inputs validated
 Type checking
 Range checking
 Format validation

Authentication & Authorization:

 Proper authentication checks
 Authorization for sensitive operations
 Session management
 Password handling (hashing, salting)

Data protection:

 No hardcoded secrets
 Sensitive data encrypted
 SQL injection prevention
 XSS prevention
 CSRF protection

Dependencies:

 No vulnerable packages
 Dependencies up-to-date
 Minimal dependency usage
Step 5: Performance review

Algorithms:

 Appropriate algorithm choice
 Reasonable time complexity
 Reasonable space complexity
 No unnecessary loops

Database:

 Efficient queries
 Proper indexing
 N+1 query prevention
 Connection pooling

Caching:

 Appropriate caching strategy
 Cache invalidation handled
 Memory usage reasonable

Resource management:

 Files properly closed
 Connections released
 Memory leaks prevented
Step 6: Testing review

Test coverage:

 Unit tests for new code
 Integration tests if needed
 Edge cases covered
 Error cases tested

Test quality:

 Tests are readable
 Tests are maintainable
 Tests are deterministic
 No test interdependencies
 Proper test data setup/teardown

Test naming:

# Good
def test_user_creation_with_valid_data_succeeds():
    pass

# Bad
def test1():
    pass

Step 7: Documentation review

Code comments:

 Complex logic explained
 No obvious comments
 TODOs have tickets
 Comments are accurate

Function documentation:

def calculate_total(items: List[Item], tax_rate: float) -> Decimal:
    """
    Calculate the total price including tax.

    Args:
        items: List of items to calculate total for
        tax_rate: Tax rate as decimal (e.g., 0.1 for 10%)

    Returns:
        Total price including tax

    Raises:
        ValueError: If tax_rate is negative
    """
    pass


README/docs:

 README updated if needed
 API docs updated
 Migration guide if breaking changes
Step 8: Provide feedback

Be constructive:

✅ Good:
"Consider extracting this logic into a separate function for better
testability and reusability:

def validate_email(email: str) -> bool:
    return '@' in email and '.' in email.split('@')[1]

This would make it easier to test and reuse across the codebase."

❌ Bad:
"This is wrong. Rewrite it."


Be specific:

✅ Good:
"On line 45, this query could cause N+1 problem. Consider using
.select_related('author') to fetch related objects in a single query."

❌ Bad:
"Performance issues here."


Prioritize issues:

🔴 Critical: Security, data loss, major bugs
🟡 Important: Performance, maintainability
🟢 Nice-to-have: Style, minor improvements

Acknowledge good work:

"Nice use of the strategy pattern here! This makes it easy to add
new payment methods in the future."

Review checklist
Functionality
 Code does what it's supposed to do
 Edge cases handled
 Error cases handled
 No obvious bugs
Code Quality
 Clear, descriptive naming
 Functions are small and focused
 No code duplication
 Consistent with codebase style
 No code smells
Security
 Input validation
 No hardcoded secrets
 Authentication/authorization
 No SQL injection vulnerabilities
 No XSS vulnerabilities
Performance
 No obvious bottlenecks
 Efficient algorithms
 Proper database queries
 Resource management
Testing
 Tests included
 Good test coverage
 Tests are maintainable
 Edge cases tested
Documentation
 Code is self-documenting
 Comments where needed
 Docs updated
 Breaking changes documented
Common issues
Anti-patterns

God class:

# Bad: One class doing everything
class UserManager:
    def create_user(self): pass
    def send_email(self): pass
    def process_payment(self): pass
    def generate_report(self): pass


Magic numbers:

# Bad
if user.age > 18:
    pass

# Good
MINIMUM_AGE = 18
if user.age > MINIMUM_AGE:
    pass


Deep nesting:

# Bad
if condition1:
    if condition2:
        if condition3:
            if condition4:
                # deeply nested code

# Good (early returns)
if not condition1:
    return
if not condition2:
    return
if not condition3:
    return
if not condition4:
    return
# flat code

Security vulnerabilities

SQL Injection:

# Bad
query = f"SELECT * FROM users WHERE id = {user_id}"

# Good
query = "SELECT * FROM users WHERE id = %s"
cursor.execute(query, (user_id,))


XSS:

// Bad
element.innerHTML = userInput;

// Good
element.textContent = userInput;


Hardcoded secrets:

# Bad
API_KEY = "sk-1234567890abcdef"

# Good
API_KEY = os.environ.get("API_KEY")

Best practices
Review promptly: Don't make authors wait
Be respectful: Focus on code, not the person
Explain why: Don't just say what's wrong
Suggest alternatives: Show better approaches
Use examples: Code examples clarify feedback
Pick your battles: Focus on important issues
Acknowledge good work: Positive feedback matters
Review your own code first: Catch obvious issues
Use automated tools: Let tools catch style issues
Be consistent: Apply same standards to all code
Tools to use

Linters:

Python: pylint, flake8, black
JavaScript: eslint, prettier
Go: golint, gofmt
Rust: clippy, rustfmt

Security:

Bandit (Python)
npm audit (Node.js)
OWASP Dependency-Check

Code quality:

SonarQube
CodeClimate
Codacy
References
Google Code Review Guidelines
OWASP Top 10
Clean Code by Robert C. Martin
Examples
Example 1: Basic usage
Example 2: Advanced usage
Weekly Installs
12.5K
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