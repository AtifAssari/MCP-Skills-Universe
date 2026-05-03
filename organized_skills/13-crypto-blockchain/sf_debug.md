---
rating: ⭐⭐
title: sf-debug
url: https://skills.sh/jaganpro/sf-skills/sf-debug
---

# sf-debug

skills/jaganpro/sf-skills/sf-debug
sf-debug
Installation
$ npx skills add https://github.com/jaganpro/sf-skills --skill sf-debug
SKILL.md
sf-debug: Salesforce Debug Log Analysis & Troubleshooting

Use this skill when the user needs root-cause analysis from debug logs: governor-limit diagnosis, stack-trace interpretation, slow-query investigation, heap / CPU pressure analysis, or a reproduction-to-fix loop based on log evidence.

When This Skill Owns the Task

Use sf-debug when the work involves:

.log files from Salesforce
stack traces and exception analysis
governor limits
SOQL / DML / CPU / heap troubleshooting
query-plan or performance evidence extracted from logs

Delegate elsewhere when the user is:

running or repairing Apex tests → sf-testing
implementing the code fix → sf-apex
debugging Agentforce session traces / parquet telemetry → sf-ai-agentforce-observability
Required Context to Gather First

Ask for or infer:

org alias
failing transaction / user flow / test name
approximate timestamp or transaction window
user / record / request ID if known
whether the goal is diagnosis only or diagnosis + fix loop
Recommended Workflow
1. Retrieve logs
sf apex list log --target-org <alias> --json
sf apex get log --log-id <id> --target-org <alias>
sf apex tail log --target-org <alias> --color

2. Analyze in this order
entry point and transaction type
exceptions / fatal errors
governor limits
repeated SOQL / DML patterns
CPU / heap hotspots
callout timing and external failures
3. Classify severity
Critical — runtime failure, hard limit, corruption risk
Warning — near-limit, non-selective query, slow path
Info — optimization opportunity or hygiene issue
4. Recommend the smallest correct fix

Prefer fixes that are:

root-cause oriented
bulk-safe
testable
easy to verify with a rerun

Expanded workflow: references/analysis-playbook.md

High-Signal Issue Patterns
Issue	Primary signal	Default fix direction
SOQL in loop	repeating SOQL_EXECUTE_BEGIN in a repeated call path	query once, use maps / grouped collections
DML in loop	repeated DML_BEGIN patterns	collect rows, bulk DML once
Non-selective query	high rows scanned / poor selectivity	add indexed filters, reduce scope
CPU pressure	CPU usage approaching sync limit	reduce algorithmic complexity, cache, async where valid
Heap pressure	heap usage approaching sync limit	stream with SOQL for-loops, reduce in-memory data
Null pointer / fatal error	EXCEPTION_THROWN / FATAL_ERROR	guard null assumptions, fix empty-query handling

Expanded examples: references/common-issues.md

Output Format

When finishing analysis, report in this order:

What failed
Where it failed (class / method / line / transaction stage)
Why it failed (root cause, not just symptom)
How severe it is
Recommended fix
Verification step

Suggested shape:

Issue: <summary>
Location: <class / line / transaction>
Root cause: <explanation>
Severity: Critical | Warning | Info
Fix: <specific action>
Verify: <test or rerun step>

Cross-Skill Integration
Need	Delegate to	Reason
Implement Apex fix	sf-apex	code change generation / review
Reproduce via tests	sf-testing	test execution and coverage loop
Deploy fix	sf-deploy	deployment orchestration
Create debugging data	sf-data	targeted seed / repro data
Reference Map
Start here
references/analysis-playbook.md
references/common-issues.md
references/cli-commands.md
Deep references
references/debug-log-reference.md
references/log-analysis-tools.md
references/benchmarking-guide.md
Rubric
references/scoring-rubric.md
Score Guide
Score	Meaning
90+	Expert analysis with strong fix guidance
80–89	Good analysis with minor gaps
70–79	Acceptable but may miss secondary issues
60–69	Partial diagnosis only
< 60	Incomplete analysis
Weekly Installs
1.1K
Repository
jaganpro/sf-skills
GitHub Stars
404
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass