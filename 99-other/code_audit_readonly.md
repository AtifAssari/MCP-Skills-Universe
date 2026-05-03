---
title: code-audit-readonly
url: https://skills.sh/jpkovas/code-audit-readonly/code-audit-readonly
---

# code-audit-readonly

skills/jpkovas/code-audit-readonly/code-audit-readonly
code-audit-readonly
Installation
$ npx skills add https://github.com/jpkovas/code-audit-readonly --skill code-audit-readonly
SKILL.md
Code Audit Readonly

Run a full technical repository audit in read-only mode and record everything in improvements.md.

Mandatory rules
Operate in read-only mode for the audited project.
Do not edit source code, configs, or tests in the audited project.
Do not run automatic refactors, formatters that write to disk, or destructive commands.
Allow only the creation/update of improvements.md as the final audit output.
Do not ask for confirmation to proceed with the audit; execute the plan end to end.
Record every validated finding; do not impose arbitrary limits.
If multiple locations share the same issue pattern, still register every location with explicit file and line references.
This audit is intentionally slow: prioritize depth, evidence quality, and completeness over speed.
Do not optimize for fast turnaround if that reduces analysis coverage or confidence.
Never reproduce secrets or raw credential material in improvements.md, tool output, or final responses.
For secret-related findings, record only the file path, line range, secret class, and sanitized context needed to explain the risk.
Do not quote full offending lines when they contain tokens, keys, passwords, cookies, connection strings, private keys, or other sensitive values.
Sensitive data handling

Apply these rules whenever the audit touches credentials, secrets, or other sensitive material:

Treat any suspected secret as high-risk content that must stay redacted.
Confirm the issue via read-only inspection, but never echo the literal value back to the user.
Describe the finding with neutral placeholders such as <redacted-api-key> or <redacted-private-key> only when a placeholder is necessary.
Prefer descriptions like hardcoded API credential in config bootstrap over copying the surrounding source line.
If a log, error, or telemetry path leaks sensitive data, describe the leaked data class and exposure path without reproducing payload contents.
Keep traceability through file paths and line ranges, not through verbatim secret material.
Mandatory analysis scope
Correctness and logic
Detect obvious and subtle bugs.
Check for race conditions, inconsistent states, and incorrect async/concurrency usage.
Evaluate error/exception handling, nullability, typing, and unsafe conversions.
Cover edge flows and extreme scenarios.
Performance
Find unnecessary allocations, expensive loops, N+1 patterns, excessive I/O, and repeated work.
Check for caching opportunities and inappropriate data structures.
Correlate bottlenecks across modules.
Duplication and maintainability
Detect literal duplication and logical duplication.
Identify long functions, mixed responsibilities, and excessive coupling.
Flag confusing internal APIs, ambiguous names, and outdated comments.
Security (mandatory, thorough)
Hardcoded secrets (tokens, keys, passwords, sensitive endpoints), reported with redacted descriptions only.
Injection vectors (SQL/NoSQL/command/template).
XSS, CSRF, SSRF, open redirect, path traversal.
Insecure uploads (insufficient type/size/validation checks).
Authentication/authorization issues (bypass, missing checks, privilege escalation).
Insufficient validation/sanitization.
Weak cryptography and inadequate hashing.
Insecure configurations (overly broad CORS, missing headers, debug in production).
Vulnerable dependencies and problematic versions.
Sensitive data leakage in logs, errors, and telemetry.
Observability and reliability
Validate log quality without exposing secrets.
Verify metrics/tracing where applicable.
Evaluate consistency and actionability of error messages.
Tests and quality
Identify coverage gaps in critical areas.
Detect brittle tests and missing integration coverage.
Map untested edge cases.
Execution method
Map the repository tree and list all relevant files:
Application code, internal libraries, configs, scripts, CI, Docker, IaC, migrations, and tests.
Initialize improvements.md with:
A short system summary inferred from the structure.
A "Progress Tracking" section with all relevant files marked as pending.
Severity and category conventions.
Review each file sequentially and deterministically:
Read the entire file.
Record specific findings and correlate with related imports/calls/contracts.
Update progress tracking.
Explicitly record: File fully reviewed: <path/to/file>.
Before moving to the next file, run a quick self-check for missed edge cases, security vectors, and cross-file impacts.
Run read-only auxiliary checks when useful:
Static analysis, linter, and typecheck in read-only mode.
Run tests without writing to disk.
Dependency/CVE audit.
Close improvements.md with:
A complete finding inventory (all findings captured during the audit).
A prioritized backlog that references finding IDs and contains no artificial cap.
A detailed phased remediation plan (see "Detailed planning requirements").
A brief completeness checkpoint describing what was verified to ensure no relevant area was rushed or skipped.
Progress tracking

Apply these rules to keep progress tracking clear and stable:

Build a canonical file list once:
Normalize paths (./ removed, no trailing slash, consistent case as seen on disk).
Sort the list before writing "Progress Tracking".
Keep exactly one progress row per canonical file path.
Update progress in-place:
Change the existing row status (pending -> in_progress -> reviewed).
Never append a second row for the same file.
Write File fully reviewed: <path/to/file> exactly once per file.
If a file is revisited, add notes under the same file entry; do not create a new checklist row or a second File fully reviewed line.
Before finishing, validate:
Number of reviewed rows == number of unique relevant files.
"Progress Tracking" appears exactly once in the report.
Every finding location appears in at least one reviewed file entry.
Example report structure

Use this high-level structure to keep the report consistent and to ensure a single "Progress Tracking" section:

# improvements.md

## 1. System summary
- Inferred architecture and main modules.
- Main risk surfaces.

## 2. Conventions
- Categories and severity scale used in the audit.
- Finding ID convention (`A001`, `A002`, ...).

## 3. Progress Tracking
- [ ] path/to/file-a.ext
- [ ] path/to/file-b.ext
- [ ] path/to/file-c.ext

## 4. Complete finding inventory
### A001
Category: ...
Severity: ...
Location: ...
Problem: ...
Impact: ...
Suggestion: ...
Correlation notes: ...
Security (if applicable): ...

### A002
...

## 5. Prioritized backlog (all findings)
- Priority 1: A00X, A00Y...
- Priority 2: A00Z...

## 6. Detailed phased remediation plan
### Phase 1
- Objective
- Findings included
- Dependencies
- Validation gates
- Exit criteria

### Phase 2
...

### Phase 3
...

Categories and severity

Use only these categories:

Bug
Performance
Security
Duplication
Code Quality
Architecture
Maintainability
Observability
Tests
Dependencies

Use only these severity levels:

Critical
High
Medium
Low
Mandatory format for each finding

Use unique sequential IDs (A001, A002, ...).

A0XX
Category: <...>
Severity: <Critical|High|Medium|Low>
Location: <file>:<start line>-<end line>
Problem: <objective description>
Impact: <real or potential impact>
Suggestion: <high-level fix, without editing code>
Correlation notes: <related files/flows>
Security (if applicable): <plausible abuse scenario + mitigation>


For secret-related findings, keep the same structure but never include the raw secret value or paste the full source line. Use file and line references plus sanitized descriptions only.

Detailed planning requirements

The planning phase in improvements.md must be explicit and implementation-oriented. Use this structure:

Planning assumptions and constraints:
Confirm read-only audit boundaries.
List unknowns that may affect remediation sequencing.
Prioritized backlog (complete):
Include all findings (A001...A0XX) with:
Priority order.
Estimated effort (S, M, L) with a short rationale.
Primary risk type (Correctness, Security, Performance, Reliability, Maintainability).
Phase plan with objective and controls:
For each phase, include:
Objective.
Findings included (explicit ID list).
Dependencies and ordering constraints.
Validation gates (tests/checks/evidence expected after fixes).
Exit criteria (what must be true to close the phase).
Sequencing rules:
Resolve Critical and exploitable High security/correctness findings first.
Schedule performance and maintainability work after risk containment unless blocking.
Call out parallelizable workstreams and non-parallelizable bottlenecks.
Delivery roadmap:
Provide a suggested execution order by batch/wave.
For each batch, list expected risk reduction and verification focus.
Traceability requirements
Make every finding traceable to file and line/section.
Avoid generic recommendations without evidence.
Register all validated findings found during the audit, including low-severity and repeated-location findings.
Explicitly record uncertainties when evidence is partial.
For sensitive findings, preserve traceability with file and line references while keeping all credential material redacted.
Completion criteria

Finish only when:

All relevant files are marked as reviewed in Progress Tracking.
Each reviewed file has the line File fully reviewed: ....
improvements.md contains the complete finding inventory, a prioritized backlog, and a detailed phased plan.
The audited project remains intact, with only improvements.md as the audit output artifact.
Weekly Installs
16
Repository
jpkovas/code-au…readonly
GitHub Stars
2
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail