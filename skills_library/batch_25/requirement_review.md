---
title: requirement-review
url: https://skills.sh/dauquangthanh/hanoi-rainbow/requirement-review
---

# requirement-review

skills/dauquangthanh/hanoi-rainbow/requirement-review
requirement-review
Installation
$ npx skills add https://github.com/dauquangthanh/hanoi-rainbow --skill requirement-review
SKILL.md
Requirement Review

Systematically review requirements to validate quality and identify issues before design and development begins. Ensure requirements are complete, clear, consistent, testable, and traceable.

Review Workflow
1. Preparation

Gather all relevant documentation:

Requirements documents (BRD, SRS, user stories)
Non-functional requirements and constraints
Requirements Traceability Matrix (if available)
Project context (charter, goals)
Existing acceptance criteria
2. Quality Assessment

Evaluate each requirement using six quality attributes:

Completeness: All needs captured, no missing details or TBDs, dependencies identified
Clarity: Unambiguous, specific, no vague terms ("user-friendly", "fast", "easy")
Consistency: No conflicts, consistent terminology and priorities
Testability: Verifiable with measurable acceptance criteria and clear pass/fail
Traceability: Links to business goals, design, and tests
Feasibility: Technically achievable within constraints (budget, timeline, capability)

See quality-checklists.md for detailed assessment criteria and document-specific checklists

3. Issue Identification

Identify common requirement problems:

Ambiguous: "system shall be fast" → Specify measurable criteria: "< 2s response for 95% of requests"

Untestable: "system shall be secure" → Define specific controls: password complexity, encryption standards, audit logging

Incomplete: "system shall send notifications" → Specify channel, timing, content, recipients

Conflicting: REQ-012 "phone required" vs REQ-089 "phone optional" → Flag for stakeholder resolution

See examples.md for extensive before/after examples

4. Quality Scoring

Calculate scores for each quality attribute (0-100%):

90-100%: Excellent - minimal issues
75-89%: Good - minor improvements needed
60-74%: Fair - notable gaps exist
Below 60%: Poor - major rework required

Overall Quality = Average of all six attributes
Target: ≥ 90% for production-readiness

5. Report Generation

Create structured review report with:

Executive Summary: Quality rating, recommendation, key strengths (2-3), critical issues (2-3), top actions

Detailed Findings: Quality scores, issues by severity (Critical/Major/Minor), specific examples with requirement IDs

Action Items: Prioritized list with owners, due dates, effort estimates, approval conditions

See report-templates.md for complete report structure and templates

6. Recommendations

Provide clear decision:

Approve: Requirements ≥ 90% quality threshold
Approve with Conditions: Critical issues must be resolved before design
Major Revision: 60-74% quality - substantial rework required
Reject: < 60% quality or fundamental issues - complete redesign needed
Document-Specific Focus
Business Requirements Documents (BRD)

Focus on business objectives, stakeholder needs, scope definition, business case, constraints

Software Requirements Specifications (SRS)

Focus on functional requirements, non-functional requirements (performance, security, scalability), system behaviors, integration points, IEEE 830 compliance

User Story Backlogs

Focus on INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable), acceptance criteria format (Given-When-Then), story format, prioritization

See quality-checklists.md for document-specific assessment criteria

Severity Definitions
Critical: Blocks progress, must fix immediately (security gaps, fundamental conflicts, missing scope)
Major: Significant quality impact, should fix before approval (ambiguous criteria, missing acceptance criteria)
Minor: Quality improvements, nice to have (formatting, examples, enhancements)
Common Anti-Patterns to Flag
Gold Plating: Adding unrequested features
Solution-Focused: Specifying "how" instead of "what" (requirements should be technology-agnostic)
Scope Creep: Accepting changes without change control
Analysis Paralysis: Over-perfecting requirements indefinitely
Weak Acceptance Criteria: Vague or missing test conditions
No Traceability: Requirements disconnected from business goals
Vague Terms to Replace

Always replace with measurable criteria:

"user-friendly", "intuitive", "easy" → Define usability metrics
"fast", "quick", "responsive" → Specify response time targets
"secure" → Define specific security controls
"scalable" → Define capacity and load targets
"reliable" → Define uptime percentage and recovery time
Standards Compliance
IEEE 830: SRS structure and content standards
INVEST: User story quality criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable)
ISO/IEC 25010: Systems and software quality models
Industry-Specific: HIPAA (healthcare), PCI-DSS (payments), SOC 2 (SaaS), FDA (medical devices)

See quality-checklists.md for standards compliance details

Report Format

Generate review reports in this structure:

Executive Summary (1 page): Overall assessment, key findings, recommendation
Quality Metrics (0.5 page): Scores by attribute with targets
Detailed Findings (2-5 pages): Issues grouped by attribute with examples and recommendations
Action Items (1 page): Prioritized list with owners and due dates
Approval Decision (0.5 page): Recommendation with rationale and next steps

Keep reports factual, specific, and actionable. Always cite specific requirement IDs when identifying issues.

See report-templates.md for complete report templates

Weekly Installs
51
Repository
dauquangthanh/h…-rainbow
GitHub Stars
10
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass