---
title: code-review-excellence
url: https://skills.sh/wshobson/agents/code-review-excellence
---

# code-review-excellence

skills/wshobson/agents/code-review-excellence
code-review-excellence
Installation
$ npx skills add https://github.com/wshobson/agents --skill code-review-excellence
Summary

Systematic code review practices for constructive feedback, bug detection, and team knowledge sharing.

Covers the complete review workflow: context gathering, high-level architecture assessment, line-by-line analysis, and decision-making with clear severity labeling (blocking, important, nit, suggestion)
Includes language-specific patterns for Python, TypeScript, and JavaScript, plus specialized review techniques for security, testing, and architectural changes
Provides templates, checklists, and communication strategies to balance quality standards with team morale, emphasizing collaborative feedback over gatekeeping
Addresses difficult feedback scenarios, disagreement resolution, and common pitfalls like perfectionism, scope creep, and delayed reviews
SKILL.md
Code Review Excellence

Transform code reviews from gatekeeping to knowledge sharing through constructive feedback, systematic analysis, and collaborative improvement.

When to Use This Skill
Reviewing pull requests and code changes
Establishing code review standards for teams
Mentoring junior developers through reviews
Conducting architecture reviews
Creating review checklists and guidelines
Improving team collaboration
Reducing code review cycle time
Maintaining code quality standards
Core Principles
1. The Review Mindset

Goals of Code Review:

Catch bugs and edge cases
Ensure code maintainability
Share knowledge across team
Enforce coding standards
Improve design and architecture
Build team culture

Not the Goals:

Show off knowledge
Nitpick formatting (use linters)
Block progress unnecessarily
Rewrite to your preference
2. Effective Feedback

Good Feedback is:

Specific and actionable
Educational, not judgmental
Focused on the code, not the person
Balanced (praise good work too)
Prioritized (critical vs nice-to-have)
❌ Bad: "This is wrong."
✅ Good: "This could cause a race condition when multiple users
access simultaneously. Consider using a mutex here."

❌ Bad: "Why didn't you use X pattern?"
✅ Good: "Have you considered the Repository pattern? It would
make this easier to test. Here's an example: [link]"

❌ Bad: "Rename this variable."
✅ Good: "[nit] Consider `userCount` instead of `uc` for
clarity. Not blocking if you prefer to keep it."

3. Review Scope

What to Review:

Logic correctness and edge cases
Security vulnerabilities
Performance implications
Test coverage and quality
Error handling
Documentation and comments
API design and naming
Architectural fit

What Not to Review Manually:

Code formatting (use Prettier, Black, etc.)
Import organization
Linting violations
Simple typos
Review Process
Phase 1: Context Gathering (2-3 minutes)
Before diving into code, understand:

1. Read PR description and linked issue
2. Check PR size (>400 lines? Ask to split)
3. Review CI/CD status (tests passing?)
4. Understand the business requirement
5. Note any relevant architectural decisions

Phase 2: High-Level Review (5-10 minutes)
1. **Architecture & Design**
   - Does the solution fit the problem?
   - Are there simpler approaches?
   - Is it consistent with existing patterns?
   - Will it scale?

2. **File Organization**
   - Are new files in the right places?
   - Is code grouped logically?
   - Are there duplicate files?

3. **Testing Strategy**
   - Are there tests?
   - Do tests cover edge cases?
   - Are tests readable?

Phase 3: Line-by-Line Review (10-20 minutes)
For each file:

1. **Logic & Correctness**
   - Edge cases handled?
   - Off-by-one errors?
   - Null/undefined checks?
   - Race conditions?

2. **Security**
   - Input validation?
   - SQL injection risks?
   - XSS vulnerabilities?
   - Sensitive data exposure?

3. **Performance**
   - N+1 queries?
   - Unnecessary loops?
   - Memory leaks?
   - Blocking operations?

4. **Maintainability**
   - Clear variable names?
   - Functions doing one thing?
   - Complex code commented?
   - Magic numbers extracted?

Phase 4: Summary & Decision (2-3 minutes)
1. Summarize key concerns
2. Highlight what you liked
3. Make clear decision:
   - ✅ Approve
   - 💬 Comment (minor suggestions)
   - 🔄 Request Changes (must address)
4. Offer to pair if complex

Review Techniques
Technique 1: The Checklist Method
## Security Checklist

- [ ] User input validated and sanitized
- [ ] SQL queries use parameterization
- [ ] Authentication/authorization checked
- [ ] Secrets not hardcoded
- [ ] Error messages don't leak info

## Performance Checklist

- [ ] No N+1 queries
- [ ] Database queries indexed
- [ ] Large lists paginated
- [ ] Expensive operations cached
- [ ] No blocking I/O in hot paths

## Testing Checklist

- [ ] Happy path tested
- [ ] Edge cases covered
- [ ] Error cases tested
- [ ] Test names are descriptive
- [ ] Tests are deterministic

Technique 2: The Question Approach

Instead of stating problems, ask questions to encourage thinking:

❌ "This will fail if the list is empty."
✅ "What happens if `items` is an empty array?"

❌ "You need error handling here."
✅ "How should this behave if the API call fails?"

❌ "This is inefficient."
✅ "I see this loops through all users. Have we considered
the performance impact with 100k users?"

Technique 3: Suggest, Don't Command
## Use Collaborative Language

❌ "You must change this to use async/await"
✅ "Suggestion: async/await might make this more readable:
`typescript
    async function fetchUser(id: string) {
        const user = await db.query('SELECT * FROM users WHERE id = ?', id);
        return user;
    }
    `
What do you think?"

❌ "Extract this into a function"
✅ "This logic appears in 3 places. Would it make sense to
extract it into a shared utility function?"

Technique 4: Differentiate Severity
Use labels to indicate priority:

🔴 [blocking] - Must fix before merge
🟡 [important] - Should fix, discuss if disagree
🟢 [nit] - Nice to have, not blocking
💡 [suggestion] - Alternative approach to consider
📚 [learning] - Educational comment, no action needed
🎉 [praise] - Good work, keep it up!

Example:
"🔴 [blocking] This SQL query is vulnerable to injection.
Please use parameterized queries."

"🟢 [nit] Consider renaming `data` to `userData` for clarity."

"🎉 [praise] Excellent test coverage! This will catch edge cases."

Language-Specific Patterns
Python Code Review
# Check for Python-specific issues

# ❌ Mutable default arguments
def add_item(item, items=[]):  # Bug! Shared across calls
    items.append(item)
    return items

# ✅ Use None as default
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

# ❌ Catching too broad
try:
    result = risky_operation()
except:  # Catches everything, even KeyboardInterrupt!
    pass

# ✅ Catch specific exceptions
try:
    result = risky_operation()
except ValueError as e:
    logger.error(f"Invalid value: {e}")
    raise

# ❌ Using mutable class attributes
class User:
    permissions = []  # Shared across all instances!

# ✅ Initialize in __init__
class User:
    def __init__(self):
        self.permissions = []

TypeScript/JavaScript Code Review
// Check for TypeScript-specific issues

// ❌ Using any defeats type safety
function processData(data: any) {  // Avoid any
    return data.value;
}

// ✅ Use proper types
interface DataPayload {
    value: string;
}
function processData(data: DataPayload) {
    return data.value;
}

// ❌ Not handling async errors
async function fetchUser(id: string) {
    const response = await fetch(`/api/users/${id}`);
    return response.json();  // What if network fails?
}

// ✅ Handle errors properly
async function fetchUser(id: string): Promise<User> {
    try {
        const response = await fetch(`/api/users/${id}`);
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error('Failed to fetch user:', error);
        throw error;
    }
}

// ❌ Mutation of props
function UserProfile({ user }: Props) {
    user.lastViewed = new Date();  // Mutating prop!
    return <div>{user.name}</div>;
}

// ✅ Don't mutate props
function UserProfile({ user, onView }: Props) {
    useEffect(() => {
        onView(user.id);  // Notify parent to update
    }, [user.id]);
    return <div>{user.name}</div>;
}

Advanced Review Patterns
Pattern 1: Architectural Review
When reviewing significant changes:

1. **Design Document First**
   - For large features, request design doc before code
   - Review design with team before implementation
   - Agree on approach to avoid rework

2. **Review in Stages**
   - First PR: Core abstractions and interfaces
   - Second PR: Implementation
   - Third PR: Integration and tests
   - Easier to review, faster to iterate

3. **Consider Alternatives**
   - "Have we considered using [pattern/library]?"
   - "What's the tradeoff vs. the simpler approach?"
   - "How will this evolve as requirements change?"

Pattern 2: Test Quality Review
// ❌ Poor test: Implementation detail testing
test('increments counter variable', () => {
    const component = render(<Counter />);
    const button = component.getByRole('button');
    fireEvent.click(button);
    expect(component.state.counter).toBe(1);  // Testing internal state
});

// ✅ Good test: Behavior testing
test('displays incremented count when clicked', () => {
    render(<Counter />);
    const button = screen.getByRole('button', { name: /increment/i });
    fireEvent.click(button);
    expect(screen.getByText('Count: 1')).toBeInTheDocument();
});

// Review questions for tests:
// - Do tests describe behavior, not implementation?
// - Are test names clear and descriptive?
// - Do tests cover edge cases?
// - Are tests independent (no shared state)?
// - Can tests run in any order?

Pattern 3: Security Review
## Security Review Checklist

### Authentication & Authorization

- [ ] Is authentication required where needed?
- [ ] Are authorization checks before every action?
- [ ] Is JWT validation proper (signature, expiry)?
- [ ] Are API keys/secrets properly secured?

### Input Validation

- [ ] All user inputs validated?
- [ ] File uploads restricted (size, type)?
- [ ] SQL queries parameterized?
- [ ] XSS protection (escape output)?

### Data Protection

- [ ] Passwords hashed (bcrypt/argon2)?
- [ ] Sensitive data encrypted at rest?
- [ ] HTTPS enforced for sensitive data?
- [ ] PII handled according to regulations?

### Common Vulnerabilities

- [ ] No eval() or similar dynamic execution?
- [ ] No hardcoded secrets?
- [ ] CSRF protection for state-changing operations?
- [ ] Rate limiting on public endpoints?

Giving Difficult Feedback
Pattern: The Sandwich Method (Modified)
Traditional: Praise + Criticism + Praise (feels fake)

Better: Context + Specific Issue + Helpful Solution

Example:
"I noticed the payment processing logic is inline in the
controller. This makes it harder to test and reuse.

[Specific Issue]
The calculateTotal() function mixes tax calculation,
discount logic, and database queries, making it difficult
to unit test and reason about.

[Helpful Solution]
Could we extract this into a PaymentService class? That
would make it testable and reusable. I can pair with you
on this if helpful."

Handling Disagreements
When author disagrees with your feedback:

1. **Seek to Understand**
   "Help me understand your approach. What led you to
   choose this pattern?"

2. **Acknowledge Valid Points**
   "That's a good point about X. I hadn't considered that."

3. **Provide Data**
   "I'm concerned about performance. Can we add a benchmark
   to validate the approach?"

4. **Escalate if Needed**
   "Let's get [architect/senior dev] to weigh in on this."

5. **Know When to Let Go**
   If it's working and not a critical issue, approve it.
   Perfection is the enemy of progress.

Best Practices
Review Promptly: Within 24 hours, ideally same day
Limit PR Size: 200-400 lines max for effective review
Review in Time Blocks: 60 minutes max, take breaks
Use Review Tools: GitHub, GitLab, or dedicated tools
Automate What You Can: Linters, formatters, security scans
Build Rapport: Emoji, praise, and empathy matter
Be Available: Offer to pair on complex issues
Learn from Others: Review others' review comments
Common Pitfalls
Perfectionism: Blocking PRs for minor style preferences
Scope Creep: "While you're at it, can you also..."
Inconsistency: Different standards for different people
Delayed Reviews: Letting PRs sit for days
Ghosting: Requesting changes then disappearing
Rubber Stamping: Approving without actually reviewing
Bike Shedding: Debating trivial details extensively
Templates
PR Review Comment Template
## Summary

[Brief overview of what was reviewed]

## Strengths

- [What was done well]
- [Good patterns or approaches]

## Required Changes

🔴 [Blocking issue 1]
🔴 [Blocking issue 2]

## Suggestions

💡 [Improvement 1]
💡 [Improvement 2]

## Questions

❓ [Clarification needed on X]
❓ [Alternative approach consideration]

## Verdict

✅ Approve after addressing required changes

Weekly Installs
14.9K
Repository
wshobson/agents
GitHub Stars
34.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass