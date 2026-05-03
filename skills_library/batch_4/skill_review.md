---
title: skill-review
url: https://skills.sh/jezweb/claude-skills/skill-review
---

# skill-review

skills/jezweb/claude-skills/skill-review
skill-review
Installation
$ npx skills add https://github.com/jezweb/claude-skills --skill skill-review
Summary

Systematic 9-phase audit for claude-skills covering standards, docs verification, code accuracy, and version drift.

Validates YAML structure, keywords, third-person style, and directory organization against skill standards
Verifies API patterns, imports, and code examples against official documentation, GitHub repos, and npm packages
Cross-checks consistency between SKILL.md and README.md, detects stale dependencies (>90 days), and identifies breaking changes
Categorizes issues by severity (Critical/High/Medium/Low) with evidence links, auto-fixes unambiguous problems, and bumps versions appropriately
Prevents 10 common issues including fake API adapters, outdated method signatures, schema inconsistencies, and broken links
SKILL.md
Skill Review Skill
Process

Invoke: /review-skill <skill-name> or use this skill when detecting outdated patterns

Production evidence: better-auth audit (2025-11-08) - found 6 critical issues including non-existent API imports, removed 665 lines incorrect code, implemented v2.0.0

9-Phase Audit
Pre-Review: Install skill, check version/date, test discovery
Standards: Validate YAML, keywords, third-person style, directory structure
Official Docs: WebFetch/Context7 verify API patterns, GitHub updates, npm versions, production repos
Code Examples: Verify imports exist, API signatures match, schema consistency, templates work
Cross-File Consistency: Compare SKILL.md vs README.md, bundled resources match files
Dependencies: Run ./scripts/check-versions.sh, check breaking changes, verify "Last Verified"
Categorize: Severity (🔴 Critical / 🟡 High / 🟠 Medium / 🟢 Low) with evidence (GitHub/docs/npm)
Fix: Auto-fix unambiguous, ask user for architectural, update all files, bump version
Verify: Test discovery, templates work, no contradictions, commit with changelog

Automated (via ./scripts/review-skill.sh): YAML syntax, package versions, broken links, TODOs, file org, staleness

Manual (AI): API methods vs docs, GitHub issues, production comparisons, code correctness, schema consistency

Severity Classification

🔴 CRITICAL: Non-existent API/imports, invalid config, missing dependencies

🟡 HIGH: Contradictory examples, inconsistent patterns, outdated major versions

🟠 MEDIUM: Stale minors (>90d), missing docs sections, incomplete errors

🟢 LOW: Typos, formatting, missing optional metadata

Fix Decision

Auto-fix: Unambiguous (correct import from docs), clear evidence, no architectural impact

Ask user: Multiple valid approaches, breaking changes, architectural choices

Version Bumps
Major (v1→v2): API patterns change
Minor (v1.0→v1.1): New features, backward compatible
Patch (v1.0.0→v1.0.1): Bug fixes only
Example: better-auth Audit (2025-11-08)

🔴 CRITICAL #1: Non-existent d1Adapter import from 'better-auth/adapters/d1'

Evidence: Official docs show drizzleAdapter, GitHub has no d1Adapter export, 4 production repos use Drizzle/Kysely
Fix: Replaced with drizzleAdapter from 'better-auth/adapters/drizzle'

Result: 3 files deleted (obsolete), 3 created (correct patterns), +1,266 lines, v1.0→v2.0, 3.5 hours

Issues Prevented (10)
Fake API adapters - Non-existent imports
Stale API methods - Changed signatures
Schema inconsistency - Different table names
Outdated scripts - Deprecated approaches
Version drift - Packages >90 days old
Contradictory examples - Multiple conflicting patterns
Broken links - 404 URLs
YAML errors - Invalid frontmatter
Missing keywords - Poor discoverability
Incomplete bundled resources - Listed files don't exist
Bundled Resources

Planning: ~/.claude/skills/../planning/SKILL_REVIEW_PROCESS.md or repo planning/SKILL_REVIEW_PROCESS.md (complete 9-phase guide)

Scripts: Repo root scripts/review-skill.sh (automated validation)

Commands: Repo root commands/review-skill.md (slash command, symlinked to ~/.claude/commands/)

References: references/audit-report-template.md (output template)

Last Verified: 2026-01-09 | Version: 1.0.1

Weekly Installs
358
Repository
jezweb/claude-skills
GitHub Stars
759
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn