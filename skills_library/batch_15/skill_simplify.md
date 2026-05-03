---
title: skill-simplify
url: https://skills.sh/catlog22/claude-code-workflow/skill-simplify
---

# skill-simplify

skills/catlog22/claude-code-workflow/skill-simplify
skill-simplify
Installation
$ npx skills add https://github.com/catlog22/claude-code-workflow --skill skill-simplify
SKILL.md
Skill Simplify

Three-phase pipeline: analyze functional inventory, apply optimization rules, verify integrity.

Phase Reference Documents (read on-demand):

Phase	Document	Purpose
1	phases/01-analysis.md	Extract functional inventory, identify redundancy, validate pseudo-code format
2	phases/02-optimize.md	Apply simplification rules, fix format issues
3	phases/03-check.md	Verify functional integrity, validate format
Input Processing
const targetPath = input.trim()
const targetFile = targetPath.endsWith('.md') ? targetPath : `${targetPath}/SKILL.md`
const originalContent = Read(targetFile)
const originalLineCount = originalContent.split('\n').length

TodoWrite Pattern
TodoWrite({ todos: [
  { content: `Phase 1: Analyzing ${targetFile}`, status: "in_progress", activeForm: "Extracting functional inventory" },
  { content: "Phase 2: Optimize", status: "pending" },
  { content: "Phase 3: Integrity Check", status: "pending" }
]})

Core Rules
Preserve ALL functional elements: Code blocks with logic, agent calls, data structures, routing, error handling, input/output specs
Only reduce descriptive content: Flowcharts, verbose comments, duplicate sections, examples that repeat logic
Never summarize algorithm logic: If-else branches, function bodies, schemas must remain verbatim
Classify code blocks: Distinguish functional (logic, routing, schemas) from descriptive (ASCII art, examples, display templates) — only descriptive blocks may be deleted
Merge equivalent variants: Single/multi-perspective templates differing only by a parameter → one template with variant comment
Fix format issues: Nested backtick template literals in code fences → convert to prose; hardcoded option lists → flag for dynamic generation; workflow handoff references → ensure execution steps present
Validate pseudo-code: Check bracket matching, variable consistency, structural completeness
Quantitative verification: Phase 3 counts must match Phase 1 counts for functional categories; descriptive block decreases are expected
Error Handling
Error	Resolution
Target file not found	Report error, stop
Check FAIL (missing functional elements)	Show delta, revert to original, report which elements lost
Check WARN (descriptive decrease or merge)	Show delta with justification
Format issues found	Report in check, fix in Phase 2
Weekly Installs
16
Repository
catlog22/claude…workflow
GitHub Stars
1.9K
First Seen
Mar 8, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass