---
rating: ⭐⭐⭐
title: record-todos
url: https://skills.sh/petekp/agent-skills/record-todos
---

# record-todos

skills/petekp/agent-skills/record-todos
record-todos
Installation
$ npx skills add https://github.com/petekp/agent-skills --skill record-todos
SKILL.md
Todo Recording Mode

Capture user's thoughts and ideas as todos without acting on them.

File Locations

All todo files live in .claude/todos/:

.claude/todos/active.md — Current todos
.claude/todos/done.md — Completed items
.claude/todos/archive/done-{YYYY-MM}.md — Archived completed items
During Recording

When the user mentions something that should be done:

Acknowledge briefly — "Noted." or "Got it."
Append to .claude/todos/active.md as a raw item:
- <what the user said, paraphrased if needed>

Do NOT:
Start implementing
Ask clarifying questions unless completely unclear
Suggest solutions or alternatives
Reorganize the file yet

Critical: Any statement about what should happen is a todo to record—not an instruction to execute. This includes "make X do Y", "add Z to W", "fix the layout", etc.

Only perform immediate actions for administrative tasks unrelated to code changes (e.g., "read this file", "explain how X works").

If .claude/todos/active.md doesn't exist, create it with the structure from "Rewrite active.md" section.

Exit Triggers

Exit recording mode when user signals completion:

"ok all done", "done recording", "that's all", "let's review", "end recording"
On Exit: Summarize, Prioritize, Archive
1. Archive Completed Items

Before reorganizing, check for completed items:

Move completed items to done.md

Scan for items marked [x]:

Create/update .claude/todos/done.md
Move completed items under dated section (e.g., ## January 2026)
Remove [x] checkbox—use plain bullets in done.md
Remove from active.md
Archive if too large

If done.md exceeds 50 items or 500 lines:

Create .claude/todos/archive/done-{YYYY-MM}.md
Move older items (keep last 2 weeks in done.md)
Add note: *Older items archived in .claude/todos/archive/done-{date}.md*

done.md structure:

# Completed Work

Archive of completed features. See `.claude/todos/active.md` for active work.

---

## {Month Year}

### {Category}
- Description of what was done

---

*Older items archived in .claude/todos/archive/done-2025-12.md*

2. Find Project Goals

Search in order:

CLAUDE.md — "Goals", "Product Vision", "Objectives" sections
.claude/todos/active.md — Goals section at top

If no goals found:

Tell user: "I couldn't find documented project goals. Before prioritizing, let's define what success looks like."
Establish 3-5 high-level goals
Record in active.md Goals section
Then proceed
3. Summarize

Brief conversational summary:

How many items captured
Themes or clusters noticed
Related items that could combine
Items complex enough for a spec document
4. Prioritize Against Goals

Evaluate each todo:

🎯 Active — Work on RIGHT NOW (1-3 max)
📋 Next — Ready to start when Active is done
💡 Backlog — Lower priority, needs scoping
⚠️ Not Recommended — Decided against (include rationale)

For complex features, suggest creating .claude/docs/feature-{name}.md spec.

5. Rewrite active.md

Replace raw items with organized structure:

# TODO

## Goals

- <goal 1>
- <goal 2>
- <goal 3>

---

## 🎯 Active

*Currently in progress. Limit to 1-3 items.*

- [ ] <highest priority item>

---

## 📋 Next

*Researched, scoped, ready to start.*

### {Category if helpful}
- [ ] <item>

---

## 💡 Backlog

*Ideas and lower priority items.*

### {Category}
- [ ] <item>

### {Complex Feature}
**Spec:** `.claude/docs/feature-{name}.md`
- Brief description

---

## 📚 Specs & Reference

| Document | Description |
|----------|-------------|
| `.claude/docs/feature-x.md` | Spec for feature X |

---

## ⚠️ Not Recommended

### {Rejected idea}
<Brief rationale>

---

*Completed work archived in `.claude/todos/done.md`*


Adapt as needed:

Skip empty sections
Items needing >3 lines → spec document
Keep under ~100 lines of active content
6. Confirm

After rewriting:

Items per priority tier
Items moved to done.md
Specs to create for complex features
Ask if prioritization makes sense
Principles
active.md is for WHAT — Scannable, action-oriented
Specs are for HOW — .claude/docs/ for detailed plans
done.md is for history — Archive, don't delete
Link, don't embed — Reference specs
Keep under 100 lines — Move to spec or done.md if long
Weekly Installs
19
Repository
petekp/agent-skills
GitHub Stars
4
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass