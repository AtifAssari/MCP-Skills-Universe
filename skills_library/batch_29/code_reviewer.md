---
title: code-reviewer
url: https://skills.sh/alirezarezvani/claude-code-tresor/code-reviewer
---

# code-reviewer

skills/alirezarezvani/claude-code-tresor/code-reviewer
code-reviewer
Installation
$ npx skills add https://github.com/alirezarezvani/claude-code-tresor --skill code-reviewer
SKILL.md
Code Reviewer Skill

Lightweight automatic code quality checks while you code.

When I Activate
✅ Files modified or saved
✅ Git diff run
✅ Code mentioned in conversation
✅ User asks about code quality
✅ Before commits
What I Check
Quick Wins
Code style and formatting issues
Common anti-patterns
Obvious bugs (null checks, undefined references)
Basic security patterns (hardcoded secrets)
Import/export issues
Unused variables and functions
What I Don't Do
Deep architectural review → Use @code-reviewer sub-agent
Comprehensive security audit → Use security-auditor skill
Performance profiling → Use @architect sub-agent
Full refactoring plans → Use @code-reviewer sub-agent
Relationship with @code-reviewer Sub-Agent

Me (Skill): Fast, lightweight, real-time feedback @code-reviewer (Sub-Agent): Deep analysis with examples and strategy

Workflow
You write code
I auto-analyze (instant feedback)
I flag: "⚠️ Potential issue on line 42"
You want details → Invoke @code-reviewer sub-agent
Sub-agent provides comprehensive analysis
Analysis Examples
JavaScript/TypeScript
// You write this code:
function getUser(id) {
  return db.query(`SELECT * FROM users WHERE id = ${id}`);
}

// I immediately flag:
// 🚨 Line 2: SQL injection vulnerability
// 💡 Use parameterized queries

React
// You write:
function UserList({ users }) {
  return users.map(user => <User data={user} />);
}

// I flag:
// ⚠️ Missing key prop in list rendering (line 2)
// 💡 Add key={user.id} to User component

Python
# You write:
def process_data(data):
    return data['user']['profile']['name']

# I flag:
# ⚠️ Potential KeyError - no safety checks (line 2)
# 💡 Use .get() or add try/except

Check Categories
Code Style
Inconsistent naming conventions
Missing semicolons (JavaScript)
Improper indentation
Long functions (>50 lines)
Magic numbers
Potential Bugs
Null/undefined access without checks
Array access without bounds checking
Type mismatches (TypeScript)
Unreachable code
Infinite loops
Basic Security
Hardcoded API keys or secrets
SQL injection patterns
eval() or exec() usage
Insecure random number generation
Missing input validation
Best Practices
Missing error handling
Console.log in production code
Commented-out code blocks
TODO comments without context
Overly complex conditions
Output Format
🤖 code-reviewer skill:
  [Severity] Issue description (file:line)
  💡 Quick fix suggestion
  📖 Reference: [link to learn more]

Severity Levels
🚨 CRITICAL: Must fix (security, data loss)
⚠️ HIGH: Should fix (bugs, performance)
📋 MEDIUM: Consider fixing (maintainability)
💡 LOW: Nice to have (style, readability)
When to Invoke Sub-Agent

After I flag issues, invoke @code-reviewer sub-agent for:

Detailed explanation of the issue
Multiple fix alternatives with pros/cons
Architectural recommendations
Refactoring strategies
Best practice guidelines

Example:

Me: "⚠️ Potential N+1 query detected"
You: "@code-reviewer explain the N+1 issue and show optimal solution"
Sub-agent: [Provides comprehensive analysis with examples]

Sandboxing Compatibility

Works without sandboxing: ✅ Yes (default, recommended for learning) Works with sandboxing: ✅ Yes (no special configuration needed)

Filesystem: Read-only access to project files
Network: None required
Configuration: None required
Customization

Want different checks or patterns?

Copy this skill:

cp -r ~/.claude/skills/development/code-reviewer ~/.claude/skills/development/my-code-reviewer


Edit SKILL.md:

Modify description to adjust triggers
Customize check categories
Add language-specific patterns

Restart Claude Code:

claude --restart


See ../../TEMPLATES.md for customization guide.

Examples in Action
TypeScript Function
// Before:
async function fetchUsers(ids) {
  const users = [];
  for (let id of ids) {
    const user = await User.findById(id);  // N+1 query!
    users.push(user);
  }
  return users;
}

// I flag:
// ⚠️ N+1 query pattern detected (line 4)
// 💡 Use User.findByIds(ids) for batch loading

// After fix:
async function fetchUsers(ids) {
  return await User.findByIds(ids);
}

React Component
// Before:
function UserCard({ user }) {
  const [data, setData] = useState();

  useEffect(() => {
    fetch(`/api/users/${user.id}`)
      .then(res => res.json())
      .then(setData);
  }, []);  // Missing dependency!

  return <div>{data?.name}</div>;
}

// I flag:
// ⚠️ useEffect dependency array incomplete (line 6)
// 💡 Add user.id to dependencies: [user.id]

// After fix:
useEffect(() => {
  fetch(`/api/users/${user.id}`)
    .then(res => res.json())
    .then(setData);
}, [user.id]);

Integration with /review Command

The /review command aggregates my findings with deep sub-agent analysis:

/review --scope staged --checks all

# Command workflow:
# 1. Collects my automatic findings
# 2. Invokes @code-reviewer sub-agent for deep analysis
# 3. Invokes @security-auditor sub-agent
# 4. Generates comprehensive report with priorities

Performance Impact
Activation time: < 100ms
Analysis time: < 1 second per file
Memory usage: Minimal (read-only)
Background operation: Non-blocking

This skill operates asynchronously and won't slow down your coding workflow.

Language Support
Fully Supported
JavaScript/TypeScript (ES6+, React, Node.js)
Python (3.8+, Django, FastAPI)
Java (Spring Boot patterns)
Go (standard patterns)
Partial Support
Ruby, PHP, C#, Rust
Framework-agnostic patterns apply

Want to add language-specific patterns? See customization guide above.

Tips for Best Results
Write code first, then review - Let me catch issues as you go
Don't ignore warnings - Each flagged issue is worth reviewing
Use sub-agent for learning - Invoke @code-reviewer to understand "why"
Customize for your stack - Add project-specific patterns
Combine with /review - Use command for comprehensive pre-commit checks
Related Tools
security-auditor skill: Deeper security vulnerability scanning
test-generator skill: Auto-suggest tests for your code
@code-reviewer sub-agent: Comprehensive code review with examples
/review command: Full workflow with multiple agents
Learn More
Architecture: ../../../ARCHITECTURE.md
Templates: ../../TEMPLATES.md
Sub-agents: ../../../agents/README.md
Weekly Installs
16
Repository
alirezarezvani/…e-tresor
GitHub Stars
701
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass