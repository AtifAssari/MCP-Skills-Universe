---
title: subagent-driven-development
url: https://skills.sh/hjewkes/agent-skills/subagent-driven-development
---

# subagent-driven-development

skills/hjewkes/agent-skills/subagent-driven-development
subagent-driven-development
Installation
$ npx skills add https://github.com/hjewkes/agent-skills --skill subagent-driven-development
SKILL.md
Subagent-Driven Development

Execute plan by dispatching fresh subagent per task, with two-stage review after each: spec compliance review first, then code quality review.

Core principle: Fresh subagent per task + two-stage review (spec then quality) = high quality, fast iteration

When to Use
Have an implementation plan with mostly independent tasks
Want to stay in the current session (otherwise use executing-plans)
See references/process-detail.md for decision tree and full process flow diagrams
The Process
Load plan — Read plan.md + manifest.json. Note task IDs and waves. Do NOT read briefing files into your context.
Dispatch per task — Send implementer a 2-3 sentence summary + briefing file path. Agent reads its own briefing from disk.
Two-stage review — Spec compliance first, then code quality. Both must pass before marking complete.
Wave boundaries — Re-read manifest.json to recover state after context compaction.
Prompt Templates
./implementer-prompt.md — ./spec-reviewer-prompt.md — ./code-quality-reviewer-prompt.md
Red Flags

Never: skip reviews, proceed with unfixed issues, dispatch parallel implementers, paste full briefing text inline instead of pointing to briefing file, skip reading the manifest at wave boundaries, start code quality review before spec compliance passes.

Dispatch prompts missing key sections (see skills-management/references/dispatch-prompt-template.md for the canonical 6-section structure)

If subagent asks questions: Answer before proceeding. If reviewer finds issues: Implementer fixes, re-review until approved.

Cleanup

After all tasks complete and final review passes, before calling git-workflow stack:

Optionally write .claude/plans/<plan-id>/summary.md with execution notes
Delete the plan directory: rm -rf .claude/plans/<plan-id>/
If deletion fails, warn but do not block
References
references/workflow-example.md — full walkthrough
references/advantages-and-costs.md — comparison vs manual/executing plans

Required skills: git-workflow, writing-plans, code-review, test-driven-development

Weekly Installs
9
Repository
hjewkes/agent-skills
GitHub Stars
3
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass