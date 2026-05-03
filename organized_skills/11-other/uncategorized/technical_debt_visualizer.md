---
rating: ⭐⭐
title: technical-debt-visualizer
url: https://skills.sh/jorgealves/agent_skills/technical-debt-visualizer
---

# technical-debt-visualizer

skills/jorgealves/agent_skills/technical-debt-visualizer
technical-debt-visualizer
Installation
$ npx skills add https://github.com/jorgealves/agent_skills --skill technical-debt-visualizer
SKILL.md
Technical Debt Visualizer
Purpose and Intent

The technical-debt-visualizer provides a data-driven view of software quality. It helps engineering leaders and developers prioritize refactoring work by identifying files that are both complex and frequently changed—the "high-interest" technical debt.

When to Use
Sprint Planning: Run this before a dedicated refactoring sprint to identify the best "ROI" targets.
Architectural Reviews: Use to visualize the impact of legacy systems on the overall codebase health.
Due Diligence: Quickly assess the health of a new or acquired repository.
When NOT to Use
Performance Benchmarking: This tool measures code structure and maintainability, not runtime performance.
Absolute Complexity Rating: Metrics like cyclomatic complexity are indicators, not absolute rules; some complex logic is unavoidable.
Input and Output Examples
Input
source_path: "./src"
output_format: "markdown"

Output

A markdown report highlighting "Hotspots"—files that have high complexity and low test coverage.

Error Conditions and Edge Cases
No Git History: If run on a non-git directory, the "change frequency" metric will be unavailable.
Unsupported Languages: Complexity analysis is language-dependent; unknown extensions will be reported with a lower confidence score.
Security and Data-Handling Considerations
Local Scan: The analysis is performed entirely in memory on the local machine.
No Execution: The tool uses static analysis; it never runs the code it is analyzing.
Weekly Installs
84
Repository
jorgealves/agent_skills
GitHub Stars
1
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass