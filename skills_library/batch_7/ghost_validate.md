---
title: ghost-validate
url: https://skills.sh/ghostsecurity/skills/ghost-validate
---

# ghost-validate

skills/ghostsecurity/skills/ghost-validate
ghost-validate
Installation
$ npx skills add https://github.com/ghostsecurity/skills --skill ghost-validate
Summary

Validate security findings by analyzing code flows, testing exploit conditions, and confirming true vs. false positives.

Traces request flows from route registration through middleware to handler logic, identifying indirect protections scanners may miss
Performs live validation against accessible application instances using proxy-based request replay and response comparison
Classifies findings into True Positive, True Positive (Confirmed), False Positive, or Inconclusive with supporting evidence and confidence levels
Outputs structured validation reports with code analysis, live test results, and specific remediation recommendations
Optionally appends validation details back to the original finding file for persistent documentation
SKILL.md
Security Finding Validation

Determine whether a security finding is a true positive or false positive. Produce a determination with supporting evidence.

Input

The user provides a finding as a file path or pasted text. If neither is provided, ask for one.

Extract: vulnerability class, specific claim, affected endpoint, code location, and any existing validation evidence.

Validation Workflow
Step 1: Understand the Finding

Identify:

The vulnerability class (BFLA, BOLA, XSS, SQLi, SSRF, etc.)
The specific claim being made (what authorization check is missing, what input is unsanitized, etc.)
The affected endpoint and HTTP method
The code location
Step 2: Analyze the Source Code
Read the vulnerable file at the specified line number and all supporting files
Trace the request flow from route registration through middleware to the handler
Verify the specific claim — does the code actually lack the described check?
Look for indirect protections (middleware, helpers, ORM constraints) the scanner may have missed
Confirm the vulnerable code path is reachable under the described conditions
Step 3: Live Validation (When Available)

If a live instance of the application is accessible and the vulnerability can be confirmed through live interaction, use the proxy skill to confirm exploitability:

Start reaper proxy scoped to the target domain
Authenticate (or have the user authenticate) as a legitimate user and capture a valid request to the vulnerable endpoint
Replay or modify the request to attempt the exploit described in the finding
Compare the response to expected behavior:
Does the unauthorized action succeed? (true positive)
Does the server reject it with 401/403/404? (false positive)
Capture the request/response pair as evidence using reaper get <id>
Step 4: Make Determination

Classify the finding as one of:

True Positive: The vulnerability exists and is exploitable. The code lacks the described protection and the endpoint is reachable.
True Positive (Confirmed): Same as above, plus live testing demonstrated successful exploitation.
False Positive: The vulnerability does not exist. Provide the specific reason (indirect protection found, code path unreachable, etc.).
Inconclusive: Cannot determine without additional information. Specify what is needed.
Step 5: Report

Output a summary in the following format:

Determination: True Positive, False Positive, or Inconclusive
Confidence: High, Medium, or Low
Evidence Summary: Key findings from code review and/or live testing
Code Analysis: Specific lines and logic that support the determination
Live Test Results (if performed): Request/response pairs demonstrating the behavior
Recommendation: Fix if true positive, close if false positive, gather more info if inconclusive

Example:

## Validation Result
- **Determination**: True Positive
- **Confidence**: High
- **Evidence**: Handler at routes/transfers.go:142 queries transfers by ID without checking ownership. No middleware or ORM-level constraint enforces user scoping.
- **Recommendation**: Add ownership check — include user_id in the WHERE clause.

Step 6: Persist Results

If the finding was provided as a file path, ask the user if they would like to append the validation details to the original finding file. If they agree, append a ## Validation section to the file containing the determination, confidence, evidence summary, and recommendation.

Vulnerability Class Reference

See VULNERABILITY_PATTERNS.md in this skill directory for patterns to look for when validating authorization flaws (BFLA/BOLA/IDOR), injection (SQLi/XSS), and authentication flaws.

Weekly Installs
1.2K
Repository
ghostsecurity/skills
GitHub Stars
400
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail