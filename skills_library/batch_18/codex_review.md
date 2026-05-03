---
title: codex-review
url: https://skills.sh/jrajasekera/claude-skills/codex-review
---

# codex-review

skills/jrajasekera/claude-skills/codex-review
codex-review
Installation
$ npx skills add https://github.com/jrajasekera/claude-skills --skill codex-review
SKILL.md
Codex Review
Overview

Cross-agent review workflow: After creating a design doc or implementation plan, invoke Codex to review it, then address the feedback before implementation.

Core principle: Two agents catch more issues than one. Codex reviews with fresh eyes while Claude addresses feedback.

When to Use
digraph trigger_decision {
    "Plan/design doc created" [shape=box];
    "Is change trivial?" [shape=diamond];
    "Ask user: use codex-review?" [shape=box];
    "Auto-trigger codex-review" [shape=box];
    "User says yes?" [shape=diamond];
    "Skip review" [shape=box];
    "Run review" [shape=box];

    "Plan/design doc created" -> "Is change trivial?";
    "Is change trivial?" -> "Ask user: use codex-review?" [label="yes"];
    "Is change trivial?" -> "Auto-trigger codex-review" [label="no"];
    "Ask user: use codex-review?" -> "User says yes?" ;
    "User says yes?" -> "Run review" [label="yes"];
    "User says yes?" -> "Skip review" [label="no"];
    "Auto-trigger codex-review" -> "Run review";
}


Trivial changes: Single-file edits, typo fixes, config changes, adding a simple function. Ask before reviewing.

Non-trivial (auto-trigger): Multi-file changes, new features, architectural decisions, refactors, anything with design choices.

Also use when: User explicitly requests codex-review (e.g., "use codex-review", "get Codex feedback").

Invoking Codex

Run from the project root directory:

CRITICAL: You MUST set the Bash tool timeout parameter to 600000 (10 minutes) to prevent hangs. Run in foreground only — never background.

codex exec -C /absolute/path/to/project/root \
    --sandbox read-only \
    --full-auto \
    --skip-git-repo-check \
    "Read relative/path/to/plan.md, do research on the codebase, and then provide feedback on the plan. Point out any issues, flaws, or concerns with the plan. In your final response, provide only the feedback. Don't offer to do anything else or ask follow-up questions." 2>/dev/null


Parameters:

Bash tool timeout: Set timeout: 600000 on the Bash tool call to kill the process after 10 minutes if it hangs. This replaces the old timeout/gtimeout shell wrapper which had zsh compatibility issues.
-C: Absolute path to project root
--sandbox read-only: Codex can read but not modify
--full-auto: No interactive prompts
--skip-git-repo-check: Works in any directory
2>/dev/null: Suppress stderr noise

Capture stdout directly - do not write feedback to a file.

CRITICAL: Run in foreground only. Do NOT run codex exec as a background process (no &, no nohup, no subshell backgrounding). Always run it synchronously so that the command fully completes and exits before you proceed. Running it in the background can cause the process to linger and produce confusing duplicate output later when it eventually exits.

Path handling:

Plan inside project: Use relative path from project root (e.g., docs/plan.md)
Plan outside project: Use absolute path (e.g., /tmp/scratch/plan.md)
The -C flag always takes the absolute project root path regardless of where the plan file lives
What Codex Reviews Well (and Doesn't)

Codex excels at:

Checking if plan matches actual codebase structure (file paths, frameworks, patterns)
Identifying missing dependencies or incompatible libraries
Spotting architectural mismatches (e.g., Express patterns in a Next.js app)
Finding references to non-existent code (routes, models, functions)

Codex may struggle with:

Plans referencing external systems Codex can't access (APIs, databases, third-party services)
Very high-level or abstract plans with few concrete file/code references
Plans for greenfield projects where there's no existing code to compare against

If Codex feedback seems shallow: The plan may lack enough concrete details for meaningful review. Consider adding specific file paths, function names, or code snippets before re-running.

Processing Feedback

After receiving Codex's feedback, categorize each item:

Category	Action
Critical issues	Address immediately without asking. These are bugs, security issues, logical flaws, missing error handling, or architectural problems that would cause failures.
Minor concerns	Present to user and ask which to address. These are style suggestions, optional improvements, alternative approaches, or "nice to have" items.

Presenting minor concerns:

Handle each minor concern individually using AskUserQuestion. For each concern, present multiple ways to address it so the user can pick the best approach.

Call AskUserQuestion once per minor concern with options representing different ways to resolve it:

AskUserQuestion:
  question: "Codex suggests: [concern summary]. How should I address this?"
  header: "[short label]"
  options:
    - label: "[Approach A]", description: "[what this approach does]"
    - label: "[Approach B]", description: "[what this approach does]"
    - label: "Skip this", description: "Don't address this concern"
  multiSelect: false


Guidelines:

Each concern gets its own AskUserQuestion call — do not batch multiple concerns into one question
Always include a "Skip this" option so the user can dismiss concerns they don't care about
Present 2-3 concrete resolution approaches per concern, plus the skip option
If there are many minor concerns (5+), you may batch multiple AskUserQuestion calls in parallel (up to 4 per message) to avoid excessive back-and-forth
Review Rounds

Auto-continue on critical issues, capped at 3 rounds.

digraph review_rounds {
    "Round N" [shape=box];
    "Process feedback" [shape=box];
    "Had critical issues?" [shape=diamond];
    "N < 3?" [shape=diamond];
    "Update plan, run round N+1" [shape=box];
    "Proceed to implementation" [shape=box];

    "Round N" -> "Process feedback";
    "Process feedback" -> "Had critical issues?";
    "Had critical issues?" -> "Proceed to implementation" [label="no"];
    "Had critical issues?" -> "N < 3?" [label="yes"];
    "N < 3?" -> "Update plan, run round N+1" [label="yes"];
    "N < 3?" -> "Proceed to implementation" [label="no (max reached)"];
    "Update plan, run round N+1" -> "Round N" [style=dashed];
}


Rules:

After each round, if any critical issues were found and addressed, automatically run another round to verify the fixes
If a round produces only minor concerns (or no feedback), stop — no further rounds needed
Maximum 3 rounds total. If round 3 still has critical issues, proceed to implementation anyway and note the unresolved concerns
The user can still request a specific number of rounds (e.g., "do 2 rounds"), which overrides the auto-continue logic but is still capped at 3

After each round:

Address critical issues and update the plan/design doc
Present minor concerns to the user (per the feedback processing rules above)
If critical issues were addressed and rounds remain, invoke Codex again on the updated doc
After final round, proceed to implementation
Error Handling
digraph error_handling {
    "Run codex exec" [shape=box];
    "Success?" [shape=diamond];
    "Process feedback" [shape=box];
    "Retry once" [shape=box];
    "Success on retry?" [shape=diamond];
    "Ask user how to proceed" [shape=box];

    "Run codex exec" -> "Success?";
    "Success?" -> "Process feedback" [label="yes"];
    "Success?" -> "Retry once" [label="no (timeout/error)"];
    "Retry once" -> "Success on retry?";
    "Success on retry?" -> "Process feedback" [label="yes"];
    "Success on retry?" -> "Ask user how to proceed" [label="no"];
}


Note: Bash tool timeout errors may surface as a tool-level timeout message rather than exit code 124 (which shell timeout/gtimeout would return). The retry logic still applies either way.

On persistent failure, ask:

Codex review failed after retry. How would you like to proceed?
1. Skip review and continue to implementation
2. Try again
3. I'll review the plan manually

Common Mistakes
Mistake	Fix
Forgetting to set Bash tool timeout	Always set timeout: 600000 on the Bash tool call to prevent codex from hanging indefinitely
Running codex from wrong directory	Always use -C /absolute/path/to/project/root
Running codex in background	Always run synchronously (no &). Background processes cause duplicate output later
Writing feedback to file	Capture stdout directly, don't create feedback files
Running extra rounds when only minor concerns remain	Only auto-continue if critical issues were found
Exceeding 3 rounds	Cap at 3 rounds max, even if critical issues persist
Addressing all feedback equally	Categorize: critical = auto-fix, minor = ask user
Forgetting to update plan between rounds	Always update the doc before next round
Using relative path for plan outside project	Use absolute path for files not in project root
Running review on vague/abstract plans	Ensure plan has concrete file paths and code references
Quick Reference
# Review flow (auto-continues on critical issues, max 3 rounds)
[Create plan] → codex-review round 1 → address feedback →
  critical issues found? → yes → update plan → round 2 → ...
  no critical issues?    → proceed to implementation

# Feedback handling
Critical issues  → Address immediately, triggers another round
Minor concerns   → AskUserQuestion per concern with resolution options

Weekly Installs
9
Repository
jrajasekera/cla…e-skills
GitHub Stars
1
First Seen
Feb 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass