---
rating: ⭐⭐
title: doctor
url: https://skills.sh/jasonharmongit/jh-skills/doctor
---

# doctor

skills/jasonharmongit/jh-skills/doctor
doctor
Installation
$ npx skills add https://github.com/jasonharmongit/jh-skills --skill doctor
SKILL.md
Per-step execution loop

For every step, follow this exact order:

Announce the step.
Run the step and fix failures until it passes.
Give a very brief report of changes made in that step.
If any changes were made, call AskQuestion so the user can click instead of typing. If they choose No, stop the doctor sequence (do not run later steps). If they choose Yes, continue. If no changes were made during the step, continue automatically to the next step.

AskQuestion arguments for the gate after step N (where N is 1, 2, or 3):

title: Doctor: Step {N} completed
questions: one question with id doctor_proceed, prompt Proceed to step {N+1}?, and two options: id yes / label Yes, and id no / label No

Example announce line:

Doctor: Step 3/4 - mix check

Example report line:

Step 3 report: lib/surge/foo.ex - removed unused alias; wrapped side effect in after callback.

Step 1 - Organize functions

Read and apply the organize-elixir-functions skill from ~/.agents/skills/organize-elixir-functions. Unless the user specifies otherwise (rare), you should apply it in branch mode.

When determining which files changed on the branch for that step, use the same baseline as Step 4: git merge-base HEAD origin/main (not local main), so candidate detection matches the remote default branch.

If changes were made, call AskQuestion (after step 1 gate above). If No, stop.

Step 2 - Format
mix format


One mix format run applies all formatting the tool can do; a second pass is only needed if the first run failed (for example syntax errors) or you changed files after formatting.

If changes were made, call AskQuestion (after step 2 gate: title Doctor: Step 2 completed, prompt Proceed to step 3?). If No, stop.

Step 3 - mix check
mix check


If changes were made, call AskQuestion (after step 3 gate: title Doctor: Step 3 completed, prompt Proceed to step 4?). If No, stop.

Step 4 - Compile and tests

!!!ABSOLUTELY CRITICAL RULE!!!: bare mix test is never allowed under any circumstances whatsoever.

Scope only: branch-changed paths from git diff --name-only "$(git merge-base HEAD origin/main)"...HEAD + git status --short.

Test run shape: only explicit *_test.exs file args. No directory args. No repo-wide runs. No "extra confidence" runs.

Allowed files only: test file in branch diff, or direct counterpart of changed lib/... module (same path stem). No sibling or neighbor tests.

Empty allowed list: skip this step.

CRITICAL - Fix scope is per test case, not per file: only fix a failing case when it is DIRECTLY related to branch application-code changes. Other failures in same file: ignore, leave red.

No out-of-scope edits: no changes to unrelated test cases, unrelated test files, or production code for unrelated failures.

Pre-edit gate (required): before any test file change, announce the exact test-case edit you plan to make and cite the specific app-code path + branch diff hunk that directly justifies touching that case. If you cannot cite that evidence first, do not edit.

Final report requirement for any file change: include strong evidence for each changed test case - exact failing case, exact changed app-code path, and exact direct relationship. If you cannot prove that, do not edit.

mix compile --warnings-as-errors

# optional:
mix test <file path>

Notes
If you get stuck in any loops or complex problems that you are having to make large or risky changes for, stop and ask the user for help.
Doctor is not a green-the-whole-repo pass: it is compile + only branch-tied test files + only edits to branch-related test cases inside those files (other cases in the same file can stay red). Anything broader is a mistake.
REMINDER - bare mix test is never allowed under any circumstances whatsoever.
Weekly Installs
23
Repository
jasonharmongit/jh-skills
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass