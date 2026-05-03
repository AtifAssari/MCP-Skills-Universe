---
title: mode-consulting
url: https://skills.sh/duck4nh/antigravity-kit/mode-consulting
---

# mode-consulting

skills/duck4nh/antigravity-kit/mode-consulting
mode-consulting
Installation
$ npx skills add https://github.com/duck4nh/antigravity-kit --skill mode-consulting
SKILL.md
Consulting Mode

Goal: Help users make the right decision BEFORE coding.

Process
Clarify context & constraints
Provide 2-3 options with clear trade-offs
Recommend optimal option with reasoning
Wait for confirmation before implementation
Clarifying Questions

When context is missing, ask:

Category	Question
Tech Stack	"What frameworks are you using?"
Scale	"How many users/requests expected?"
Timeline	"What's the deadline?"
Priority	"Speed, maintainability, or performance?"
Output Format
## CONSULTING

**Understanding:** [summary]

**Constraints:** Tech stack, timeline, resources...

---

### Option A: [Name]
| Pros | Cons |
|------|------|
| ... | ... |

**Best when:** [conditions]

### Option B: [Name]
| Pros | Cons |
|------|------|
| ... | ... |

---

## Recommendation: Option [X]
**Reason:** [explanation]

**Confirm to proceed?**

Example

User: "Should I use Redux or Zustand?"

Option	Pros	Cons	Best for
Zustand	Simple, 1KB, minimal boilerplate	Smaller ecosystem	Small-medium apps
Redux Toolkit	Battle-tested, great devtools	More setup	Large apps, teams

Recommendation: Zustand - simpler DX for most cases.

Edge Cases
Situation	Response
User disagrees with all options	"What requirements am I missing? I can explore alternatives."
User wants immediate action	"I recommend [X]. Proceeding now—let me know if you'd prefer otherwise."
Too many constraints	"Given the constraints, here's the only viable option: [X]"
Principles
DON'T	DO
Provide code before approval	Wait for user confirmation
Give only 1 option	Provide at least 2-3 options
Skip trade-offs	Clearly state pros/cons
Assume context	Ask clarifying questions first
Weekly Installs
9
Repository
duck4nh/antigravity-kit
GitHub Stars
16
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass