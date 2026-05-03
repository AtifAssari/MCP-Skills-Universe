---
rating: ⭐⭐
title: sf-testing
url: https://skills.sh/jaganpro/sf-skills/sf-testing
---

# sf-testing

skills/jaganpro/sf-skills/sf-testing
sf-testing
Installation
$ npx skills add https://github.com/jaganpro/sf-skills --skill sf-testing
SKILL.md
sf-testing: Salesforce Test Execution & Coverage Analysis

Use this skill when the user needs Apex test execution and failure analysis: running tests, checking coverage, interpreting failures, improving coverage, and managing a disciplined test-fix loop for Salesforce code.

When This Skill Owns the Task

Use sf-testing when the work involves:

sf apex run test workflows
Apex unit-test failures
code coverage analysis
identifying uncovered lines and missing test scenarios
structured test-fix loops for Apex code

Delegate elsewhere when the user is:

writing or refactoring production Apex → sf-apex
testing Agentforce agents → sf-ai-agentforce-testing
testing LWC with Jest → sf-lwc
Required Context to Gather First

Ask for or infer:

target org alias
desired test scope: single class, specific methods, suite, or local tests
coverage threshold expectation
whether the user wants diagnosis only or a test-fix loop
whether related test data factories already exist
Recommended Workflow
1. Discover test scope

Identify:

existing test classes
target production classes
test data factories / setup helpers
2. Run the smallest useful test set first

Start narrow when debugging a failure; widen only after the fix is stable.

3. Analyze results

Focus on:

failing methods
exception types and stack traces
uncovered lines / weak coverage areas
whether failures indicate bad test data, brittle assertions, or broken production logic
4. Run a disciplined fix loop

When the issue is code or test quality:

delegate code fixes to sf-apex when needed
add or improve tests
rerun focused tests before broader regression
5. Improve coverage intentionally

Cover:

positive path
negative / exception path
bulk path (251+ records where appropriate)
callout or async path when relevant
High-Signal Rules
default to SeeAllData=false
every test should assert meaningful outcomes
test bulk behavior, not just single-record happy paths
use factories / @TestSetup when they improve clarity and speed
pair Test.startTest() with Test.stopTest() when async behavior matters
do not hide flaky org dependencies inside tests
Output Format

When finishing, report in this order:

What tests were run
Pass/fail summary
Coverage result
Root-cause findings
Fix or next-run recommendation

Suggested shape:

Test run: <scope>
Org: <alias>
Result: <passed / partial / failed>
Coverage: <percent / key classes>
Issues: <highest-signal failures>
Next step: <fix class, add test, rerun scope, or widen regression>

Cross-Skill Integration
Need	Delegate to	Reason
fix production code or author tests	sf-apex	code generation and repair
create bulk / edge-case data	sf-data	realistic test datasets
deploy updated tests	sf-deploy	rollout
inspect detailed runtime logs	sf-debug	deeper failure analysis
Reference Map
Start here
references/cli-commands.md
references/test-patterns.md
references/testing-best-practices.md
references/test-fix-loop.md
Specialized guidance
references/mocking-patterns.md
references/performance-optimization.md
assets/
Score Guide
Score	Meaning
108+	strong production-grade test confidence
96–107	good test suite with minor gaps
84–95	acceptable but strengthen coverage / assertions
< 84	below standard; revise before relying on it
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