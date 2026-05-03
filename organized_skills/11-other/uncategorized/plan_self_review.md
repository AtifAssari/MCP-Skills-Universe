---
rating: ⭐⭐
title: plan-self-review
url: https://skills.sh/hrdtbs/agent-skills/plan-self-review
---

# plan-self-review

skills/hrdtbs/agent-skills/plan-self-review
plan-self-review
Installation
$ npx skills add https://github.com/hrdtbs/agent-skills --skill plan-self-review
SKILL.md
Plan Self-Review

Use this skill immediately after creating or updating a plan. Catching logical gaps, ambiguous steps, or missing dependencies early prevents cascading failures during execution. Self-reviewing your plan helps you approach the problem methodically and reduces the likelihood of needing major revisions later.

Review Steps
Score Plan (100pt): Evaluate the plan based on the following criteria:
Clarity (25): Are the steps clear and easy to follow? Do they specify which files and tools will be used?
Comprehensiveness (25): Does the plan cover all necessary aspects of the task? Are there any unaddressed edge cases?
Feasibility (25): Are the steps achievable with the available tools and context? Do you have enough information to execute them?
Consistency (25): Are there any logical contradictions or missing elements? Do the steps follow a logical sequence?
List Deficiencies: Create a prioritized task list (- [ ]) of any gaps, omissions, or ambiguities found in the plan.
Improve: Edit the plan to resolve the identified deficiencies. Update the plan using the appropriate tool.
Final Check: Perform a final check to confirm no logical contradictions or missing elements remain.
Output Format

Present your review using the following structure:

Self-Evaluation Score: [Score]/100
Clarity: [Score]/25
Comprehensiveness: [Score]/25
Feasibility: [Score]/25
Consistency: [Score]/25
Deficiencies
 [Deficiency 1]
 [Deficiency 2]
Improvements Made
[Briefly describe the improvements made to the plan]
Final Check
[Confirm that the plan is now logically sound and complete]
Examples

Example 1: Reviewing a plan for adding a new API endpoint

Initial Plan:

Create new endpoint.
Update tests.

Self-Review Output:

Self-Evaluation Score: 40/100
Clarity: 10/25 (Missing details on which file to edit and what the endpoint does)
Comprehensiveness: 10/25 (Missing documentation update, error handling details)
Feasibility: 10/25 (Too vague to execute without further clarification)
Consistency: 10/25 (Logically sound but lacks concrete steps)
Deficiencies
 Specify the exact file and route for the new endpoint
 Add error handling requirements
 Identify which test file needs to be updated and what test cases to add
 Include a step to update the API documentation
Improvements Made
Updated the plan to specify the target file (src/api/users.js) and route (POST /users).
Added a sub-step for implementing input validation and error handling.
Specified the test file (tests/api/users.test.js) and explicitly required testing the error cases.
Added a step to update docs/api.md.
Final Check
The revised plan is now clear, comprehensive, and specifies exact files and actions. It is logically sound and ready for execution.
Weekly Installs
42
Repository
hrdtbs/agent-skills
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass