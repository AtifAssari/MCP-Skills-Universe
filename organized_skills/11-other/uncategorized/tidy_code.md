---
rating: ⭐⭐⭐⭐⭐
title: tidy-code
url: https://skills.sh/ggwicz/skills/tidy-code
---

# tidy-code

skills/ggwicz/skills/tidy-code
tidy-code
Installation
$ npx skills add https://github.com/ggwicz/skills --skill tidy-code
SKILL.md
tidy-code Review

Review source code against 10 language-agnostic structural quality principles and produce a findings report with concrete refactoring suggestions.

Important: This skill produces a report. Do not modify any reviewed files.

Review Workflow
Select files — Use the user's specified files. If none specified, run scripts/scan-source-files.sh <project-directory> to discover source files. The <project-directory> argument is required — it must be the root of the user's project, NOT the skill's own directory.
Load rules — Read references/principles-quick-ref.md for the full checklist with detection signals and thresholds.
Review files in parallel — Spawn parallel sub-agents (via the Task tool, model sonnet, effort medium) to review files concurrently. Batch files into groups of 3–5 per sub-agent, grouping related files (same module or directory) together when possible so sub-agents can detect cross-file violations within their batch. Each sub-agent receives: its file list, the principles from references/principles-quick-ref.md, and instructions to produce findings in the Output Format below, loading detailed reference files on demand as violations are detected. Run up to 5 sub-agents concurrently. Once all complete, collect their findings. If a sub-agent fails, log the error and continue — do not block the rest of the review.
Collect and deduplicate findings — Gather findings from all sub-agents. Remove exact duplicates if file batches shared related files. Check for cross-file violations that individual sub-agents may have missed (e.g., a dependency injected in one file but hardcoded in another within a different batch).
Classify severity — Use references/severity-rubric.md to assign high/medium/low.
Verify suggestions — For each suggested rewrite, confirm it resolves the flagged violation, does not introduce a new violation of any other principle, and preserves the original behavior. If a suggestion introduces a new violation, revise it before including it.
Assemble report — Write findings to .agents/tidy/code/tidy-code-findings-YYYYMMDD.md (create the directory if it doesn't exist; use today's date). Group findings by file, then by severity (high first). End with the summary block.
Model & Effort Guidance

This skill does not require frontier-class reasoning for typical codebases. The 10 principles have concrete detection signals and named refactorings that reduce the task to structured pattern matching. Use a mid-tier model (e.g., Claude Sonnet) at high effort for orchestration, and the same model at medium effort for file-review sub-agents. For very large or architecturally complex codebases, upgrading the orchestrator to a frontier model (e.g., Claude Opus) may surface subtler cross-file violations.

Output Format

Use this exact structure for each finding:

## [file path]

### Finding [N] — [Smell name] [ID] (severity: [high|medium|low])
- **Line [N]:** `[original code snippet]`
- **Principle:** [One-sentence explanation of the violated principle]
- **Refactoring:** [Named refactoring technique]
- **Suggested:**
  [concrete rewrite as a fenced code block]


Example:

## src/services/order_service.py

### Finding 1 — Hidden Dependency TC-02 (severity: high)
- **Line 8:** `self.db = PostgresConnection("prod:5432")`
- **Principle:** Dependencies created internally are invisible, untestable, and tightly coupled to a specific implementation.
- **Refactoring:** Inject via constructor parameter
- **Suggested:**
  ```python
  class OrderService:
      def __init__(self, db, mailer):
          self.db = db
          self.mailer = mailer
  ```

### Finding 2 — Nested Pyramid TC-03 (severity: medium)
- **Line 34:** 3 levels of nesting in `process_order()`
- **Principle:** Each nesting level forces the reader to maintain a mental stack. Guard clauses flatten the logic.
- **Refactoring:** Replace Nested Conditional with Guard Clauses
- **Suggested:**
  ```python
  def process_order(order):
      if not order:
          return None
      if not order.items:
          return None
      if not order.payment:
          raise ValueError("Missing payment")
      # happy path — no nesting
  ```


If a file has no findings, omit it from the report entirely.

End the report with:

## Summary
- **Files reviewed:** [N]
- **Total findings:** [N] ([N] high, [N] medium, [N] low)
- **Top issues:** [List the 2-3 most frequent violations]
- **Highest-leverage fix:** [The single change that would most improve the codebase]

When to Load Reference Files

Load references on demand to conserve context:

File	When to load
references/principles-quick-ref.md	Always — load at start of every review
references/severity-rubric.md	When classifying findings
references/composition-over-inheritance.md	Inheritance depth > 1 or base class used only for code reuse
references/dependency-injection.md	import + instantiate inside business logic
references/guard-clauses.md	Nesting depth > 2 or pyramid-shaped conditionals
references/single-responsibility.md	Function > 25 lines or class name contains "Manager", "Handler", "Utils"
references/fail-fast.md	Bare except:/catch {}, silent None returns, or swallowed errors
references/least-surprise.md	get_* function has side effects, or boolean params at call sites
references/tell-dont-ask.md	External code reads 2+ fields from an object to make a decision
references/immutability.md	var, let (JS) where const works, argument mutation, shared mutable state
references/naming.md	Vague names (data, info, result) or abbreviations (usr, mgr)
references/functional-core-imperative-shell.md	Business logic contains I/O calls (db, http, file, print)
Scope Rules
Review: application source code — functions, classes, modules, components
Skip: test fixtures/factories, generated code, migration files, configuration files (JSON/YAML/TOML), vendor/third-party code, single-use scripts under 20 lines, type declaration files (.d.ts)
Light touch: test files — apply naming (TC-09) and guard clauses (TC-03) but do not enforce DI (TC-02) or functional core (TC-10), since test setup is inherently side-effectful
Do not modify reviewed files — produce recommendations only
Weekly Installs
8
Repository
ggwicz/skills
GitHub Stars
1
First Seen
11 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail