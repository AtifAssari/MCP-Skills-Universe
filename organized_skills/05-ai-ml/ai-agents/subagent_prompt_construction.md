---
rating: ⭐⭐
title: subagent-prompt-construction
url: https://skills.sh/zpankz/mcp-skillset/subagent-prompt-construction
---

# subagent-prompt-construction

skills/zpankz/mcp-skillset/subagent-prompt-construction
subagent-prompt-construction
Installation
$ npx skills add https://github.com/zpankz/mcp-skillset --skill subagent-prompt-construction
SKILL.md

λ(use_case, complexity) → subagent_prompt | ∧ require(need_orchestration(use_case) ∨ need_mcp_integration(use_case)) ∧ complexity ∈ {simple, moderate, complex} ∧ line_target = {simple: 30-60, moderate: 60-120, complex: 120-150} ∧ template = read(templates/subagent-template.md) ∧ patterns = read(reference/patterns.md) ∧ integration = read(reference/integration-patterns.md) ∧ apply(template, use_case, patterns, integration) → draft ∧ validate(|draft| ≤ 150 ∧ integration_score ≥ 0.50 ∧ clarity ≥ 0.80) ∧ examples/{phase-planner-executor.md} demonstrates orchestration ∧ reference/case-studies/* provides detailed analysis ∧ scripts/ provide validation and metrics automation ∧ output = {prompt: draft, metrics: validation_report}

Artifacts:

templates/: Reusable subagent template (lambda contract structure)
examples/: Compact validated examples (≤150 lines each)
reference/patterns.md: Core patterns (orchestration, analysis, enhancement)
reference/integration-patterns.md: Claude Code feature integration (agents, MCP, skills)
reference/symbolic-language.md: Formal syntax reference (logic operators, quantifiers)
reference/case-studies/: Detailed analysis and design rationale
scripts/: Automation tools (validation, metrics, pattern extraction)

Usage: See templates/subagent-template.md for structure. Apply integration patterns for Claude Code features. Validate compactness (≤150 lines), integration (≥1 feature), clarity. Reference examples/ for compact demonstrations and case-studies/ for detailed analysis.

Constraints: Max 150 lines per prompt | Use symbolic logic for compactness | Explicit dependencies section | Integration score ≥0.50 | Test coverage ≥80% for generated artifacts

Validation: V_instance=0.895 (phase-planner-executor: 92 lines, 2 agents, 2 MCP tools) | V_meta=0.709 (compactness=0.65, integration=0.857, maintainability=0.85) | Transferability=95%

Weekly Installs
8
Repository
zpankz/mcp-skillset
GitHub Stars
2
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass