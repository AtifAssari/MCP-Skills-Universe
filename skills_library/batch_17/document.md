---
title: document
url: https://skills.sh/webriq/claude-skills/document
---

# document

skills/webriq/claude-skills/document
document
Installation
$ npx skills add https://github.com/webriq/claude-skills --skill document
SKILL.md
/document - Documentation Agent
Workflow
/document {ID}
       ↓
1. Resolve task ID → find task document
2. Read task document + test report (pipeline audit)
3. Run git diff — identify pipeline gaps
4. Create/update feature doc (docs/features/{feature}.md)
5. Create/update user guide if user-facing (docs/guides/{feature}.md)
6. Update CLAUDE.md if structural changes detected
7. Write retrospective → update LEARNINGS.md
8. Move task to "Approved" in TASKS.md
       ↓
┌─── Automation Mode? ───┐
│                        │
▼ Manual                 ▼ Auto
Notify user              Output SIGNAL, exit
Ready for /ship

Auto Mode Behavior

When task document has Automation: auto:

≡ SIGNAL
STAGE: document
STATUS: DONE
TASK: {ID}
SUMMARY: Feature doc created
REFERENCE: docs/features/{feature}.md
≡ END


Manual mode: Run /clear then /ship {ID}.

Step 1: Pre-Documentation Checklist — Full Pipeline Audit
Step 1A: Read primary sources
docs/task/{ID}-{task-name}.md        - What was planned + Implementation Notes from /simplify
docs/testing/{ID}-{task-name}.md     - Test results, failures, retry cycles

Step 1B: Get the actual file diff
git diff --name-only main...HEAD


Cross-reference against task doc's ## File Changes. Anything in diff but NOT in the task doc was added by /simplify or a /test retry — these are pipeline gaps to capture.

Step 1C: Classify pipeline gaps
File in diff but not in task doc	Likely source	Action
Same file, significantly refactored	/simplify quality fixes	Note pattern changes in CLAUDE.md if new convention emerged
New helper/utility extracted	/simplify single-responsibility fix	Add to CLAUDE.md Important File Locations if reusable
New test fixture or seed file	/test setup	Note in LEARNINGS.md if it reveals a testing pattern
Additional files changed in retry	/test → /implement re-run	Document deviation; check if CLAUDE.md needs updating
Migration file added mid-cycle	Any step	Always add to CLAUDE.md — migrations are critical context

Do NOT do broad codebase exploration. Only open files in the gap list or explicitly needed to verify accuracy.

Step 1D: Read /simplify's Implementation Notes

In the task doc ## Implementation Notes:

"What was built" — may differ from original plan
"Deviations from plan" — medium or major deviations surface in documentation
"Standards check" — fixes may have introduced new patterns worth recording in CLAUDE.md
Step 1E: Check /test retry count

In docs/testing/{ID}-{task-name}.md:

0 retries → note what worked well in LEARNINGS.md
1+ retries → root cause of failure is a lesson; always capture in LEARNINGS.md
Multiple retries on same issue → add "Do Not" entry to CLAUDE.md
Step 2: Identify Documentation Needs
Change Type	Documentation Needed
New feature	Feature doc + User guide
Enhancement	Update existing docs
Bug fix	Update troubleshooting sections
API change	Update API reference
Pipeline gap (simplify/test added files)	CLAUDE.md + LEARNINGS.md
Step 3: Documentation Output

Feature doc: docs/features/{FEATURE}.md — technical implementation details for developers. Include overview, user journey, architecture (file structure, schema, API endpoints), key components, technical notes.

User guide: docs/guides/{feature}.md — how to use the feature for end users. Include quick start, step-by-step instructions, tips, FAQ, troubleshooting.

Step 4: CLAUDE.md — Living Project Brain

Read → prune → update (in that order). Never just append.

Bar for an entry: A future agent would make a mistake without it, waste time discovering it, or re-open a decision already made.

Triggers for update after this task:

What happened	What to update
New directory created	Project Structure
File moved or renamed	Important File Locations
Database migration ran	Stack section, schema notes
New package installed	Stack section
/simplify caught a repeated violation	Do Not
Architecture debate resolved	Architecture Decisions
Convention violated and then fixed	Key Conventions
Old pattern replaced	Remove old entry, add new

Skip entirely if: pure logic fix, copy change, or styling tweak with no new files, directories, migrations, routes, or packages.

Never skip if: migration added, new directory created, file moved/renamed, new API route, new env variable required, or pattern replaced.

/implement should have already captured these — verify and fill any gaps.

Step 5: Retrospective & LEARNINGS.md

Task retrospective: docs/learnings/{ID}-{task-name}.md

Covers the entire pipeline — plan vs reality, quality gate findings, test failures, decisions made. Include:

Plan vs Reality (what was planned, what was committed, deviations, files outside plan)
What /simplify caught (patterns flagged and fixed)
What /test revealed (failures and root causes)
Key lessons (specific and actionable)

LEARNINGS.md (project root): Extract the most reusable insight and append to the relevant section.

Where the lesson came from	LEARNINGS.md section
/simplify caught a coding pattern violation	Common Mistakes to Avoid
/simplify extracted a reusable helper	Established Coding Patterns
/test failed due to system behavior not in plan	Tech Stack Notes
/test retry revealed an integration gap	Common Mistakes to Avoid
Files in diff not in plan	Tech Stack Notes or Established Coding Patterns
Architecture decision made during pipeline	Architecture & Decisions

Rules for LEARNINGS.md entries:

One entry = one actionable lesson
Credit the pipeline step that caught it
Bold the key phrase, explain in one sentence
Never duplicate — check before appending
If LEARNINGS.md missing, create with sections: Architecture & Decisions, Established Coding Patterns, Common Mistakes to Avoid, Testing Patterns, Tech Stack Notes
Documentation Checklist
 git diff --name-only main...HEAD run — full file list captured
 Pipeline gaps identified and classified
 /simplify Implementation Notes read — deviations noted
 /test retry count checked — root cause of failures identified
 Feature doc created/updated with accurate file paths
 User guide created/updated (if user-facing)
 CLAUDE.md read → pruned → updated (or skipped if no structural changes)
 docs/learnings/{ID}-{task-name}.md written
 Key lesson(s) appended to LEARNINGS.md
 No duplicate entries in LEARNINGS.md
 Task moved to "Approved" in TASKS.md
Update TASKS.md

Move task to "Approved":

ID	Task	Task Doc	Feature Doc	Test Report	Approved
Handoff to /ship

Manual mode: Output summary of updated files, task moved to "Approved", next step /ship {ID}. Auto mode: Output SIGNAL and exit. The orchestrator handles routing. Do not spawn the next skill.

Weekly Installs
32
Repository
webriq/claude-skills
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass