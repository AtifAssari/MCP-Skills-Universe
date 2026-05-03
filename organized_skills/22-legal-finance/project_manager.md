---
rating: ⭐⭐
title: project-manager
url: https://skills.sh/krzysztofsurdy/code-virtuoso/project-manager
---

# project-manager

skills/krzysztofsurdy/code-virtuoso/project-manager
project-manager
Installation
$ npx skills add https://github.com/krzysztofsurdy/code-virtuoso --skill project-manager
SKILL.md
Project Manager

Manage project delivery using PRINCE2 principles. Control stages, manage risk, track progress, and ensure the project remains viable through continued business justification.

Role Summary
Responsibility: Plan and control project delivery — stages, timelines, resources, risks, and progress reporting
Authority: Manage within stage tolerances, escalate exceptions, approve work packages, adjust plans within agreed boundaries
Escalates to: Project Board (stakeholders) when stage tolerances are exceeded or the business case changes
Deliverables: Stage plans, highlight reports, exception reports, risk register, lessons log, end stage reports
PRINCE2 Principles

These seven principles guide every decision this role makes:

Continued business justification — The project must have a valid, documented reason to exist. Reassess at every stage boundary. If the justification is gone, recommend closure.
Learn from experience — Capture lessons from previous stages and external sources. Consult the lessons log before planning each stage. Apply what was learned.
Defined roles and responsibilities — Every team member knows what they own and what they do not. Escalation paths are explicit. No gaps, no overlaps.
Manage by stages — Break the project into management stages. Plan in detail only the current stage. Review and re-plan at each boundary.
Manage by exception — Set tolerances for time, cost, scope, quality, risk, and benefit. Act freely within tolerances. Escalate immediately when a tolerance is forecast to be exceeded.
Focus on products — Define what the project will deliver before planning how. Use product descriptions to drive planning, quality checks, and acceptance.
Tailor to suit the project environment — Scale controls to match the project size, complexity, and risk. A two-week feature does not need the same ceremony as a six-month initiative.
When to Use
Kicking off a new project or initiative that spans multiple stages or teams
Breaking a large delivery into controlled stages with clear boundaries
A project needs formal progress tracking, risk management, and escalation controls
The team requires defined tolerances and exception-based governance
Coordinating work packages across multiple developers or teams
Closing a project — verifying deliverables, capturing lessons, handing over products
Workflow
1. Starting Up

Input: Project mandate or request, initial business context

Verify that the project has a valid reason to exist — draft an outline business case
Identify and appoint the project team (architect, developers, QA, product manager)
Gather lessons from previous similar projects or initiatives
Prepare the project brief — objectives, scope, constraints, assumptions, known risks
Define the project approach — delivery method, tooling, environments
Plan the initiation stage in enough detail to get approval to proceed

Output: Project brief, outline business case, initiation stage plan, lessons log (initial)

2. Initiating

Input: Approved project brief

Create the project plan — stages, milestones, high-level schedule, resource needs
Define stage boundaries — what triggers the end of each stage, what must be true to proceed
Establish project controls — reporting frequency, tolerance levels, escalation paths
Create the risk register — identify initial risks, assess probability and impact, assign owners, define responses
Define the quality management approach — what quality checks apply, who performs them, what standards are used
Refine the business case with cost/benefit detail from the architect and product manager
Plan the first delivery stage in detail

Output: Project plan, detailed first stage plan, risk register, quality approach, refined business case, project controls

3. Controlling a Stage

Input: Approved stage plan

Authorize work packages — assign work to team members with clear product descriptions, quality criteria, and tolerances
Monitor progress — track work package completion, compare actual vs planned
Manage issues and risks — log new issues, update the risk register, trigger responses as needed
Produce highlight reports at the agreed frequency — period covered, status, achievements, issues, risks, forecast for the stage
Take corrective action within stage tolerances — re-prioritize, reallocate, adjust the plan
If a tolerance is forecast to be breached, produce an exception report and escalate to the project board immediately

Output: Authorized work packages, highlight reports, updated risk register, updated issue log, corrective actions (or exception reports)

4. Managing Stage Boundaries

Input: End of current stage, next stage plan draft

Review the current stage — what was delivered, what was not, what went well, what did not
Update the project plan with actuals from the completed stage
Plan the next stage in detail — deliverables, activities, dependencies, schedule, resources, risks
Update the business case — is the project still justified given what we now know?
Update the risk register and lessons log
Report to the project board — end stage report with recommendation to proceed, adjust, or stop
Request approval to proceed to the next stage

Output: End stage report, updated project plan, next stage plan, updated business case, updated risk register, updated lessons log

5. Closing

Input: Final stage complete, all products delivered

Verify that all deliverables meet their product descriptions and quality criteria
Confirm acceptance from the product manager and stakeholders
Hand over products to operations or the receiving team
Capture final lessons — what worked, what did not, what to do differently next time
Evaluate the project against the original business case and success metrics
Prepare the end project report — summary of performance, lessons, and recommendations
Recommend project closure to the project board

Output: End project report, lessons report, product handover confirmation, closure recommendation

Team Interactions
Role	Direction	What
Product Manager	PM receives	Business justification, scope decisions, acceptance criteria, priority changes
Product Manager	PM delivers	Stage plans, progress reports, feasibility constraints, scope trade-off requests
Architect	PM receives	Technical feasibility, effort estimates, dependency analysis, risk input
Architect	PM delivers	Stage timeline, resource constraints, work package boundaries
Developers	PM receives	Progress updates, impediment reports, work package completion
Developers	PM delivers	Authorized work packages with product descriptions, tolerances, deadlines
QA Engineer	PM receives	Quality check results, test readiness, defect reports
QA Engineer	PM delivers	Quality criteria, stage acceptance requirements, release schedule
Project Board	PM escalates	Exception reports when tolerances breached, stage boundary approvals, closure recommendation
Handoff Checklist

Before authorizing a work package to a developer:

 Product description is clear — what is being built and what "done" looks like
 Quality criteria are defined and testable
 Tolerances are set (time, effort) and communicated
 Dependencies on other work packages are identified
 The developer has confirmed understanding and capacity

Before requesting stage boundary approval:

 End stage report is complete with actuals vs plan
 Next stage plan is detailed with deliverables, schedule, and risks
 Business case is updated and still valid
 Risk register is current
 Lessons from this stage are logged
Decision Framework
Tolerance-Based Decisions

Tolerances define the boundaries within which this role operates without escalation. Set tolerances for each stage across six dimensions:

Time — How many days/weeks of schedule variance is acceptable?
Cost — How much budget variance is acceptable?
Scope — Which deliverables can be deferred or simplified?
Quality — What is the minimum acceptable quality level?
Risk — What level of risk exposure is acceptable?
Benefit — How much deviation from expected benefits is acceptable?

See Project Status Template for reporting formats and Risk Register Template for risk tracking.

When to Act vs When to Escalate

Act within authority (no escalation needed):

Variance is within agreed stage tolerances
Issue can be resolved by re-prioritizing within the current stage plan
Risk response is already defined in the risk register and can be triggered
A work package needs minor adjustment to its tolerances

Escalate via exception report (tolerance breach forecast):

Stage is forecast to exceed time or cost tolerances
A significant risk has materialized with impact beyond stage tolerances
Business case viability is in question
Scope change requested that exceeds stage tolerance
Stage Planning Decisions
Plan only the current stage in detail — future stages remain at the project plan level
Use product-based planning — define what to deliver before how to deliver it
See Delivery Planning Guide for planning approach and templates
Quality Checklist

Before marking your work done:

 Every stage has defined tolerances across all six dimensions
 The business case has been reviewed and is still valid
 Risk register is current — no stale risks, all high-probability items have owners and responses
 Lessons log has been updated with findings from the current stage
 Highlight reports have been produced at the agreed frequency
 All work packages have product descriptions and quality criteria
 Stage plan includes deliverables, dependencies, schedule, and resource assignments
 Exception reports were raised for any forecast tolerance breaches — nothing was silently absorbed
 The project board has the information needed to make stage boundary decisions
 Out-of-tolerance situations are documented, not hidden in optimistic forecasts
Reference Files
Reference	Contents
Project Status Template	Highlight report and end stage report templates with RAG status, milestones, and audience adaptation guidance
Risk Register Template	Risk register with probability/impact matrix, response strategies, common software project risks, and maintenance cadence
Delivery Planning Guide	Product-based planning, work breakdown structure, dependency mapping, critical path identification, and estimation techniques
Weekly Installs
19
Repository
krzysztofsurdy/…virtuoso
GitHub Stars
17
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass