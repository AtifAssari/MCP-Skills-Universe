---
rating: ⭐⭐
title: sf-ai-agentforce-testing
url: https://skills.sh/jaganpro/sf-skills/sf-ai-agentforce-testing
---

# sf-ai-agentforce-testing

skills/jaganpro/sf-skills/sf-ai-agentforce-testing
sf-ai-agentforce-testing
Installation
$ npx skills add https://github.com/jaganpro/sf-skills --skill sf-ai-agentforce-testing
SKILL.md
sf-ai-agentforce-testing: Agentforce Test Execution & Coverage Analysis

Use this skill when the user needs formal Agentforce testing: multi-turn conversation validation, CLI Testing Center specs, topic/action coverage analysis, preview checks, or a structured test-fix loop after publish.

When This Skill Owns the Task

Use sf-ai-agentforce-testing when the work involves:

sf agent test workflows
multi-turn Agent Runtime API testing
topic routing, action invocation, context preservation, guardrail, or escalation validation
test-spec generation and coverage analysis
post-publish / post-activate test-fix loops

Delegate elsewhere when the user is:

building or editing the agent itself → sf-ai-agentforce or sf-ai-agentscript
running Apex unit tests → sf-testing
creating seed data for actions → sf-data
analyzing session telemetry / STDM traces → sf-ai-agentforce-observability
Core Operating Rules
Testing comes after deploy / publish / activate.
Use multi-turn API testing as the primary path when conversation continuity matters.
Use CLI Testing Center as the secondary path for single-utterance and org-supported test-center workflows.
Interactive and programmatic CLI preview use standard sf org login web authentication; ECA is only required for Agent Runtime API testing, not for live preview.
Fixes to the agent should be delegated to sf-ai-agentscript when Agent Script changes are needed.
Do not use raw curl for OAuth token validation in the ECA flow; use the provided credential tooling.
Script path rule

Use the existing scripts under:

~/.claude/skills/sf-ai-agentforce-testing/hooks/scripts/

These scripts are pre-approved. Do not recreate them.

Required Context to Gather First

Ask for or infer:

agent API name / developer name
target org alias
testing goal: smoke test, regression, coverage expansion, or bug reproduction
whether the agent is already published and activated
whether the org has Agent Testing Center available
whether ECA credentials are available for Agent Runtime API testing

Preflight checks:

discover the agent
confirm publish / activation state
verify dependencies (Flows, Apex, data)
choose testing track
Dual-Track Workflow
Track A — Multi-turn API testing (primary)

Use when you need:

multi-turn conversation testing
topic re-matching validation
context preservation checks
escalation or action-chain analysis across turns

Requires:

ECA / auth setup
agent runtime access
Track B — CLI Testing Center (secondary)

Use when you need:

org-native sf agent test workflows
test spec YAML execution
quick single-utterance validation
CLI-centered CI/CD usage where Testing Center is available
Quick manual path

For manual validation without full formal testing, use preview workflows first, then escalate to Track A or B as needed.

Recommended Workflow
1. Discover and verify
locate the agent in the target org
confirm it is published and activated
confirm required actions / Flows / Apex exist
decide whether Track A or Track B fits the request
2. Plan tests

Cover at least:

main topics
expected actions
guardrails / off-topic handling
escalation behavior
phrasing variation
3. Execute the right track
Track A
validate ECA credentials with the provided tooling
retrieve metadata needed for scenario generation
run multi-turn scenarios with the provided Python scripts
analyze per-turn failures and coverage
Track B
generate or refine a flat YAML test spec
run sf agent test commands
inspect structured results and verbose action output
4. Classify failures

Typical failure buckets:

topic not matched
wrong topic matched
action not invoked
wrong action selected
action invocation failed
context preservation failure
guardrail failure
escalation failure
5. Run fix loop

When failures imply agent-authoring issues:

delegate fixes to sf-ai-agentscript
re-publish / re-activate if needed
re-run focused tests before full regression
Testing Guardrails

Never skip these:

test only after publish/activate
include harmful / off-topic / refusal scenarios
use multiple phrasings per important topic
clean up sessions after API tests
keep swarm execution small and controlled

Avoid these anti-patterns:

testing unpublished agents
treating one happy-path utterance as coverage
storing ECA secrets in repo files
debugging auth with brittle shell-expanded curl commands
changing both tests and agent simultaneously without isolating the cause
Output Format

When finishing a run, report in this order:

Test track used
What was executed
Pass/fail summary
Coverage gaps
Root-cause themes
Recommended fix loop / next test step

Suggested shape:

Agent: <name>
Track: Multi-turn API | CLI Testing Center | Preview
Executed: <specs / scenarios / turns>
Result: <passed / partial / failed>
Coverage: <topics, actions, guardrails, context>
Issues: <highest-signal failures>
Next step: <fix, republish, rerun, or expand coverage>

Cross-Skill Integration
Need	Delegate to	Reason
fix Agent Script logic	sf-ai-agentscript	authoring and deterministic fix loops
create test data	sf-data	action-ready data setup
fix Flow-backed actions	sf-flow	Flow repair
fix Apex-backed actions	sf-apex	Apex repair
set up ECA / OAuth for Agent Runtime API	sf-connected-apps	auth and app configuration
analyze session telemetry	sf-ai-agentforce-observability	STDM / trace analysis
Reference Map
Start here
references/interview-wizard.md
references/multi-turn-testing.md
references/cli-commands.md
references/test-spec-reference.md
Execution / auth
references/execution-protocol.md
references/multi-turn-execution.md
references/eca-setup-guide.md
references/credential-convention.md
references/connected-app-setup.md
Coverage / fix loops
references/coverage-analysis.md
references/agentic-fix-loops.md
references/results-scoring.md
references/known-issues.md
Advanced / specialized
references/agentscript-agents.md
references/agentscript-testing-patterns.md
references/cli-testing-details.md
references/deep-conversation-history-patterns.md
references/swarm-execution.md
references/trace-analysis.md
references/agent-api-reference.md
Templates / assets
references/test-templates.md
references/test-plan-format.md
assets/
Score Guide
Score	Meaning
90+	production-ready test confidence
80–89	strong coverage with minor gaps
70–79	acceptable but coverage expansion recommended
60–69	partial validation only
< 60	insufficient confidence; block release
Weekly Installs
1.0K
Repository
jaganpro/sf-skills
GitHub Stars
404
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass