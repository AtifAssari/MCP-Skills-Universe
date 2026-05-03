---
title: requirements prioritization
url: https://skills.sh/danhvb/my-ba-skills/requirements-prioritization
---

# requirements prioritization

skills/danhvb/my-ba-skills/Requirements Prioritization
Requirements Prioritization
Installation
$ npx skills add https://github.com/danhvb/my-ba-skills --skill 'Requirements Prioritization'
SKILL.md
Requirements Prioritization Skill
Purpose

Systematically prioritize requirements to ensure the most valuable features are delivered first, managing scope and stakeholder expectations effectively.

When to Use
Managing product backlog
Planning releases or sprints
Resolving conflicting stakeholder needs
Allocating limited resources
Defining MVP (Minimum Viable Product)
Prioritization Frameworks
1. MoSCoW Method

Best for: Fixed deadlines, scope negotiation

Must Have (M): Critical for success. Non-negotiable. If missed, launch fails.
Should Have (S): Important but not vital. Can be worked around painfully.
Could Have (C): Desirable/Nice-to-have. Low impact if left out.
Won't Have (W): Agreed to leave out of this release (maybe later).

Example: E-commerce Checkout

Must: Guest checkout, Credit card payment.
Should: PayPal integration, Address autocomplete.
Could: Gift wrapping options, Crypto payment.
Won't: Voice-activated checkout (for now).
2. RICE Scoring

Best for: Data-driven decision making, comparing disparate features.

$$ RICE Score = \frac{Reach \times Impact \times Confidence}{Effort} $$

Reach: Number of people/events per period (e.g., 1000 users/month).
Impact:
3 (Massive)
2 (High)
1 (Medium)
0.5 (Low)
0.25 (Minimal)
Confidence:
100% (High - have data)
80% (Medium - some data/intuition)
50% (Low - wild guess)
Effort: Person-months (e.g., 2 months).
3. Kano Model

Best for: Customer satisfaction and differentiation.

Basic (Threshold): Must be present. Customer neutral if there, dissatisfied if absent. (e.g., Car brakes).
Performance (Linear): The more, the better. (e.g., Car gas mileage).
Excitement (Delighters): Surprise features. High satisfaction if present, neutral if absent. (e.g., Free sunroof).
4. WSJF (Weighted Shortest Job First)

Best for: Agile/SAFe environments, maximizing economic flow.

$$ WSJF = \frac{Cost of Delay (CoD)}{Job Size (Duration)} $$

Cost of Delay components:

User-Business Value (Value to user/business)
Time Criticality (Is there a deadline/decay?)
Risk Reduction/Opportunity Enablement (Does it reduce risk/unlock future value?)
Facilitating Prioritization Workshops
Preparation
List Requirements: Ensure all requirements are gathered and clear.
Invite Stakeholders: Decision makers, technical leads, business owners.
Define Criteria: Agree on the framework (e.g., "We will use MoSCoW").
Process (e.g., Buy a Feature)
Give stakeholders "play money" budget (e.g., $100).
Assign "prices" to requirements based on effort/cost.
Ask stakeholders to "buy" the features they want.
Discuss results: What was bought? What was ignored?
Process (e.g., $100 Test)
Give each stakeholder 100 points.
Ask them to distribute points across requirements based on importance.
Sum up points to see group consensus.
Common Challenges & Solutions
Challenge	Solution
Everything is a "Must"	Force ranking (1 to N). Use "Buy a Feature" with limited budget.
HIPPO (Highest Paid Person's Opinion)	Use data-driven methods (RICE). Visualize trade-offs.
Conflicting priorities	Link back to business goals/KPIs. Facilitate negotiation.
Dependencies ignored	Technical team must review to identify dependency chains (A must be done before B).
Business Value vs. Technical Necessity
Business Priority: Value provided to the customer/business.
Technical Priority: Architectural needs, dependencies, debt reduction.
Final Priority: Start where Business Value is high AND Technical Risk is managed.
Output
Prioritized Backlog: Ordered list of requirements.
Release Map: What goes into Release 1, 2, 3.
Descope List: Explicit list of what is NOT being done.
Reference
Wiegers, K. & Beatty, J. (2013). Software Requirements.
Intercom on Product Management (RICE).
SAFe Framework (WSJF).
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