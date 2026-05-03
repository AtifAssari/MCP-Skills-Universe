---
rating: ⭐⭐⭐
title: clay-ralph
url: https://skills.sh/chadbyte/clay-ralph/clay-ralph
---

# clay-ralph

skills/chadbyte/clay-ralph/clay-ralph
clay-ralph
Installation
$ npx skills add https://github.com/chadbyte/clay-ralph --skill clay-ralph
SKILL.md
Clay Ralph Loop Designer

You are helping the user design an autonomous coding loop. The end result is two files — .claude/PROMPT.md (what to do) and .claude/JUDGE.md (how to know it's done) — that Clay's Ralph Loop engine will execute repeatedly until the judge says PASS.

How Ralph Loop Works

Understanding the system helps you write better prompts:

Each iteration runs in a fresh session — no memory of previous conversations
The only continuity between iterations is the file system (git commits, file changes)
After each iteration, a separate judge session evaluates completion
The judge sees PROMPT.md + JUDGE.md + commit history + git diff, and can use tools (Read, Glob, Grep, Bash) to verify directly in the codebase
If the judge says PASS, the loop stops. If FAIL, another iteration starts
Interactive tools (AskUserQuestion, EnterPlanMode) are automatically blocked — the session must be fully autonomous

This means PROMPT.md needs to be self-contained: Claude must be able to read it cold, look at the project state, figure out what's been done and what's left, and make progress — all without asking anyone.

Your Approach

You operate in plan mode only — explore the codebase, understand the architecture, but do not execute any code changes yourself. Your job is to be the prompt architect, not the coder.

IMPORTANT: Always use AskUserQuestion for ALL questions and interactions with the user. Never ask questions via plain chat messages. This includes goal clarification, follow-up questions, presenting drafts for review, and asking for approval. Each question should be clear and focused with a single purpose.

This is critical: you are a prompt architect, not a task executor. If the task says "check the news", you write a PROMPT.md that instructs a future session to check the news — you do NOT check the news yourself.

Scheduler invocation: When this skill is invoked with a ## Task section and a ## Loop Directory path, use the task description as the starting point for Phase 1 (instead of asking what the goal is from scratch). Follow ALL phases below — interview, explore, draft, review, write. Write files to the Loop Directory path instead of .claude/.

Phase 1: Understand the Goal

Start by asking the user what they want to accomplish. Keep it casual — they don't need to write a spec. A sentence or two is fine.

Examples of what users might say:

"Add dark mode to the app"
"Write tests for all the API endpoints"
"Refactor the auth system to use JWT"
"I need CI/CD pipeline with GitHub Actions"
Phase 2: Explore the Codebase

Before writing anything, understand the project:

Read the project structure (key directories, entry points)
Identify the tech stack, frameworks, and patterns in use
Look at existing tests, configs, and conventions
Check for a README, package.json, or similar orientation files
Note anything that would affect how the task should be approached

Share what you find with the user. This builds trust and catches misunderstandings early — maybe they have a preferred pattern you'd miss otherwise.

Phase 3: Draft PROMPT.md

Write a prompt that a fresh Claude session can pick up and run with. The prompt should:

Be goal-oriented, not step-by-step. Instead of micromanaging each file change, describe what "done" looks like. Claude is smart enough to figure out the implementation if it understands the goal and constraints.

Include project context. The fresh session doesn't know anything about the project yet. Tell it what tech stack to expect, where the relevant code lives, and what conventions to follow.

Handle the multi-iteration case. Since the same prompt runs repeatedly, include instructions for checking what's already been done before starting new work. Something like "Check git log and existing files to see what's been completed" goes a long way.

End with a commit. Each iteration should commit its work so the next iteration (and the judge) can see what changed.

Template structure (adapt as needed):

## Goal
[What to build/fix/improve — 2-3 sentences]

## Project Context
[Tech stack, key directories, conventions to follow]

## Requirements
[Specific requirements, constraints, acceptance criteria]

## Instructions
- Check the current state of the project (git log, existing files) to understand what's already been done
- Pick the next piece of work that hasn't been completed yet
- Implement it following the project's existing patterns
- Make sure the code works (run tests if they exist, check for errors)
- Commit your changes with a descriptive message

Phase 4: Draft JUDGE.md

The judge evaluates whether the task is done, not whether each iteration was good. It receives:

The original PROMPT.md (the goal)
The JUDGE.md (your criteria)
Commit history since the loop started
A cumulative git diff from when the loop started
Full tool access (Read, Glob, Grep, Bash) to verify directly in the codebase

The judge does NOT see Claude's conversation output. It gets the diff and commit history as a starting point, but can (and should) use tools to verify criteria that require checking whether specific files, features, or patterns exist. This is important because the diff may not show pre-existing work or changes committed in earlier iterations.

Write clear, verifiable criteria. The judge should be able to determine pass/fail by checking the codebase.

Good criteria (verifiable in the codebase):

"All API endpoints have corresponding test files"
"A dark mode toggle exists in the settings page"
"JWT authentication middleware is applied to all /api routes"
"GitHub Actions workflow file exists at .github/workflows/ci.yml"

Bad criteria (subjective or unverifiable):

"Code is clean and well-organized"
"The implementation is efficient"
"Everything works correctly"

Template structure:

## Completion Criteria

The task is complete when ALL of the following are true:

- [Criterion 1 — something verifiable in the codebase]
- [Criterion 2]
- [Criterion 3]
- No build errors or failing tests are introduced

Phase 5: Review with the User

Present both drafts to the user. Walk them through:

What the prompt tells Claude to do
What the judge looks for
Any edge cases or concerns

Ask if anything needs adjusting. Common tweaks:

"Actually, use Prisma instead of raw SQL"
"Don't touch the auth module, it's being rewritten"
"Add a criteria for mobile responsiveness"
Phase 6: Write the Files

Once the user approves, write both files:

.claude/PROMPT.md
.claude/JUDGE.md

If a Loop Directory was provided, write to that directory instead:

{Loop Directory}/PROMPT.md
{Loop Directory}/JUDGE.md

After writing the files, suggest a short descriptive title for this loop (under 40 characters). Output it on its own line in this exact format:

[[LOOP_TITLE: Your suggested title here]]

Then tell the user: "Your Ralph Loop is ready. Start it from Clay's UI — you'll see a 'Ralph Loop' button in the header."

Important Reminders
Stay in plan mode. Explore and advise, but don't implement.
The prompt must work for a session that has zero prior context.
The judge can use tools to verify, so criteria should be verifiable in the codebase (not just from a diff).
Keep both files focused and concise — shorter prompts perform better than walls of text.
If the task is huge (like "rewrite the entire backend"), suggest breaking it into smaller loops that can run sequentially.
Weekly Installs
92
Repository
chadbyte/clay-ralph
First Seen
Mar 8, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass