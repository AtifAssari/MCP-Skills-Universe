---
title: gap analysis
url: https://skills.sh/danhvb/my-ba-skills/gap-analysis
---

# gap analysis

skills/danhvb/my-ba-skills/Gap Analysis
Gap Analysis
Installation
$ npx skills add https://github.com/danhvb/my-ba-skills --skill 'Gap Analysis'
SKILL.md
Gap Analysis Skill
Purpose

Identify the difference (gap) between the current state (As-Is) and the desired future state (To-Be) to determine what actions, processes, or technologies are needed to bridge that gap.

When to Use
Strategic planning
Software migration/upgrades
Process improvement initiatives
Compliance audits
Feature parity analysis (e.g., moving from Legacy to New System)
The Gap Analysis Process
1. Identify Current State (As-Is)
What: How things work today.
Sources: Documentation, interviews, observation, system data.
Artifacts: Current process maps, system architecture diagrams, SWOT strengths/weaknesses.
Questions:
What is the current manual process?
What are the pain points?
What metrics are we hitting/missing?
2. Define Future State (To-Be)
What: Where we want to be.
Sources: Strategic goals, industry benchmarks, stakeholder vision.
Artifacts: Future process maps, target architecture, KPIs.
Questions:
What does "good" look like?
What are the automation targets?
What functionality is mandatory?
3. Analyze the Gap
Compare As-Is and To-Be directly.
Characterize the gap:
Process Gap: Missing steps, inefficient workflows.
Technology Gap: System limitations, missing features, integration needs.
Skill/People Gap: Training needs, resource shortages.
Data Gap: Missing data fields, poor data quality.
4. Bridge the Gap (Action Plan)
Define solutions to close each gap.
Prioritize solutions.
Estimate effort and impact.
Gap Analysis Matrix Template
#	Category	Current State (As-Is)	Future State (To-Be)	Gap Description	Action / Solution	Priority
1	Process	Orders manually entered from email to ERP.	Orders automatically synced from Web to ERP.	No integration exists. Manual entry takes 15 mins/order.	Implement ERP API integration.	High
2	Data	Customer phone numbers stored in free text.	Customer phone numbers validated and standardized (E.164).	Data quality issue, unable to use SMS gateway.	Data cleansing script + Validation on frontend.	Medium
3	Feature	No guest checkout available.	Guest checkout supported.	Missing functionality causing 20% drop-off.	Build guest checkout flow.	High
4	Skill	Support team knows Tier 1 issues only.	Support team handles Tier 2 issues.	Knowledge gap.	Train Lead Support agents on Tier 2 troubleshooting.	Low
Comparison Frameworks
1. SWOT Analysis (Current State Focus)
Strengths: Internal positives.
Weaknesses: Internal negatives (GAPS).
Opportunities: External positives (Future State potential).
Threats: External negatives.
2. McKinsey 7S Framework

Analyze gaps across:

Hard Elements: Strategy, Structure, Systems.
Soft Elements: Shared Values, Style, Staff, Skills.
3. Nadler-Tushman Congruence Model

Checks fit between Work, People, Structure, and Culture.

Output Artifacts
Gap Analysis Document: Detailed report.
Action Plan / Roadmap: Timeline of projects to close gaps.
Business Case: Justification for the investment.
Tips for Success
Be quantified: "Slow processing" is bad. "Processing takes 4 days vs target of 4 hours" is good.
Focus on root causes: Don't just list symptoms.
Validate: Confirm As-Is with users who do the work, not just managers.
References
BABOK Guide - Strategy Analysis
Business Capability Mapping
Weekly Installs
–
Repository
danhvb/my-ba-skills
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass