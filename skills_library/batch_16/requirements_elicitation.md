---
title: requirements elicitation
url: https://skills.sh/danhvb/my-ba-skills/requirements-elicitation
---

# requirements elicitation

skills/danhvb/my-ba-skills/Requirements Elicitation
Requirements Elicitation
Installation
$ npx skills add https://github.com/danhvb/my-ba-skills --skill 'Requirements Elicitation'
SKILL.md
Requirements Elicitation Skill
Purpose

This skill enables AI assistants to conduct professional requirements elicitation sessions, gathering comprehensive business requirements from stakeholders across various project types (Web, Mobile, ERP, CRM, CDP, E-commerce) using industry-standard techniques.

When to Use This Skill
Starting a new project or feature development
Conducting discovery or inception phases
Gathering requirements for system enhancements
Understanding business problems and opportunities
Preparing for BRD/FRS documentation
Core Elicitation Techniques
1. Stakeholder Interviews

Best for: Deep dive into individual perspectives, sensitive topics, executive input

Approach:

Preparation: Research stakeholder background, role, and pain points
Structure: Use semi-structured format (prepared questions + flexibility)
Duration: 45-60 minutes per session
Question Framework: Use 5W1H (Who, What, When, Where, Why, How)

Question Types:

Open-ended: "Can you walk me through your current process for...?"
Probing: "Why is that important to your team?"
Clarifying: "When you say 'real-time', what timeframe do you mean?"
Hypothetical: "If you could change one thing about the current system, what would it be?"

STAR Technique (for process understanding):

Situation: "Describe a typical scenario when you..."
Task: "What are you trying to accomplish?"
Action: "What steps do you take?"
Result: "What's the outcome? What could be better?"
2. Requirements Workshops

Best for: Cross-functional alignment, brainstorming, consensus building

Approach:

Participants: 6-12 stakeholders from different departments
Duration: 2-4 hours
Facilitation: Use visual aids (whiteboards, Figma, Miro)
Techniques:
Brainstorming sessions
Affinity mapping (group similar ideas)
Dot voting (prioritization)
Process walkthroughs

Workshop Agenda Template:

Introduction & objectives (10 min)
Current state review (30 min)
Pain points identification (30 min)
Future state visioning (45 min)
Requirements brainstorming (45 min)
Prioritization exercise (30 min)
Next steps & action items (10 min)
3. Document Analysis

Best for: Understanding existing systems, compliance requirements, historical context

Documents to Review:

Existing system documentation
Business process manuals
User guides and training materials
Compliance and regulatory documents
Analytics reports and dashboards
Support tickets and bug reports
Competitive analysis reports

Analysis Approach:

Identify gaps between documented and actual processes
Extract business rules and constraints
Understand data structures and relationships
Note assumptions and dependencies
4. Observation & Job Shadowing

Best for: Understanding actual workflows, identifying undocumented processes

Approach:

Shadow users in their work environment
Observe without interrupting (take notes)
Note workarounds and pain points
Follow up with clarifying questions
Document the "as-is" process flow

Focus Areas:

Frequency of tasks
Time spent on activities
Tools and systems used
Handoffs between teams
Error-prone steps
5. Surveys & Questionnaires

Best for: Gathering input from large user groups, quantitative data

Best Practices:

Keep surveys short (10-15 questions max)
Use mix of question types (multiple choice, rating scales, open-ended)
Ensure anonymity when appropriate
Set clear deadline for responses
Analyze and share results

Question Examples:

Rating: "On a scale of 1-5, how satisfied are you with the current checkout process?"
Multiple choice: "Which payment methods do you use most frequently?"
Open-ended: "What's the biggest challenge you face when processing orders?"
6. Prototyping & Mockups

Best for: Validating UI/UX requirements, visual requirements

Approach:

Create low-fidelity wireframes (Figma, sketches)
Present to stakeholders for feedback
Iterate based on input
Use clickable prototypes for user testing
Document feedback and requirements
Requirements Categorization
Functional Requirements

Definition: What the system should do

Examples by Domain:

E-commerce: "System shall allow users to add products to cart", "System shall calculate shipping costs based on destination"
ERP: "System shall generate purchase orders from approved requisitions", "System shall support multi-currency transactions"
CRM: "System shall track lead sources and conversion rates", "System shall send automated follow-up emails"
CDP: "System shall unify customer data from web, mobile, and CRM", "System shall create audience segments based on behavior"
Mobile/Web: "App shall work offline and sync when connected", "Website shall load in under 3 seconds"
Non-Functional Requirements

Categories:

Performance: Response time, throughput, scalability
Security: Authentication, authorization, data encryption
Usability: User experience, accessibility (WCAG compliance)
Reliability: Uptime, error handling, disaster recovery
Compatibility: Browser support, device support, integrations
Compliance: GDPR, CCPA, SOX, industry regulations

Examples:

"System shall support 10,000 concurrent users"
"All sensitive data shall be encrypted at rest and in transit"
"System shall achieve 99.9% uptime"
"Mobile app shall support iOS 15+ and Android 12+"
Constraints

Types:

Technical: Must use existing infrastructure, specific technology stack
Business: Budget limitations, timeline constraints
Regulatory: Must comply with specific regulations
Organizational: Must integrate with existing systems
Domain-Specific Considerations
E-commerce Projects

Key Areas to Explore:

Product catalog management (variants, attributes, inventory)
Shopping cart and checkout flow
Payment gateway integration and security
Order management and fulfillment
Customer accounts and profiles
Promotions and discount rules
Search and filtering capabilities
Product recommendations
Multi-channel selling (web, mobile, marketplace)

Critical Questions:

"How do you handle inventory across multiple warehouses?"
"What payment methods must be supported?"
"How should abandoned carts be handled?"
"What's the return and refund process?"
ERP Projects

Key Areas to Explore:

Module scope (Finance, HR, Supply Chain, Manufacturing, etc.)
Master data management strategy
Inter-module workflows and integration
Approval hierarchies and workflows
Reporting and analytics requirements
Multi-company/multi-currency needs
Role-based access control
Compliance requirements

Critical Questions:

"What approval levels are required for purchase orders?"
"How do you handle inter-company transactions?"
"What financial reports are required for compliance?"
"How should employee data be structured?"
CRM Projects

Key Areas to Explore:

Lead capture and qualification process
Sales pipeline stages and criteria
Contact and account hierarchies
Marketing campaign management
Customer service ticketing
Integration with email, phone, marketing tools
Sales forecasting methodology
Reporting and dashboards

Critical Questions:

"What defines a qualified lead?"
"What's your sales process from lead to close?"
"How do you measure customer satisfaction?"
"What integrations are needed with existing tools?"
CDP Projects

Key Areas to Explore:

Data sources (web, mobile, CRM, e-commerce, offline)
Customer identity resolution strategy
Data governance and privacy compliance
Segmentation and audience building
Real-time vs. batch processing
Data activation channels
Analytics and reporting needs
Integration with marketing tools

Critical Questions:

"How do you identify the same customer across channels?"
"What customer attributes are most important?"
"What marketing channels will consume this data?"
"How will you handle consent management?"
Mobile/Web Projects

Key Areas to Explore:

Platform requirements (iOS, Android, Web, PWA)
Responsive design needs
Offline functionality requirements
Performance expectations
Push notification strategy
Deep linking and app navigation
Authentication and security
App store requirements
Analytics and tracking

Critical Questions:

"What features must work offline?"
"What devices and OS versions must be supported?"
"How will users authenticate?"
"What analytics events need to be tracked?"
Elicitation Best Practices
1. Prepare Thoroughly
Research the business domain
Review existing documentation
Prepare questions in advance
Identify right stakeholders
Schedule adequate time
2. Listen Actively
Don't interrupt
Take detailed notes
Ask clarifying questions
Paraphrase to confirm understanding
Watch for non-verbal cues
3. Ask the Right Questions
Start broad, then drill down
Use open-ended questions
Avoid leading questions
Challenge assumptions
Ask "why" multiple times (5 Whys technique)
4. Document Immediately
Capture requirements in real-time
Use templates for consistency
Record decisions and rationale
Note assumptions and dependencies
Share notes for validation
5. Validate and Confirm
Review requirements with stakeholders
Check for completeness and clarity
Resolve conflicts and ambiguities
Get formal sign-off
Maintain traceability
6. Handle Conflicts
Acknowledge different perspectives
Focus on business objectives
Use data to support decisions
Escalate when necessary
Document trade-offs
Common Pitfalls to Avoid

❌ Assuming you understand the domain - Always verify your understanding ❌ Accepting vague requirements - Push for specificity and measurability ❌ Skipping non-functional requirements - They're critical for success ❌ Ignoring edge cases - Ask "what if" questions ❌ Not documenting assumptions - Make implicit knowledge explicit ❌ Talking more than listening - 80/20 rule: listen 80%, talk 20% ❌ Jumping to solutions - Understand the problem first ❌ Not validating requirements - Always confirm understanding

Tools for Hybrid Methodology
Lark
Use Docs for interview notes and requirements documentation
Use Base for requirements tracking and traceability
Use Meetings for recording sessions
Use Tasks for action items
Notion
Create requirements database with properties (priority, status, owner)
Use templates for consistency
Link requirements to user stories and test cases
Create stakeholder directory
Figma
Create wireframes and mockups during elicitation
Use FigJam for workshop collaboration
Prototype user flows for validation
Share designs for feedback
Output Artifacts

After requirements elicitation, you should produce:

Requirements Register: Comprehensive list of all requirements
Interview Notes: Detailed notes from stakeholder sessions
Workshop Outputs: Diagrams, prioritization results, decisions
Process Maps: Current state and future state flows
Assumptions Log: Documented assumptions and constraints
Stakeholder Matrix: Who provided which requirements
Open Questions List: Items requiring follow-up
Next Steps

After completing requirements elicitation:

Organize and categorize requirements
Prioritize using MoSCoW or RICE (see requirements-prioritization skill)
Validate requirements with stakeholders
Create BRD (see brd-creation skill)
Develop detailed FRS (see frs-creation skill)
References
BABOK® Guide (Business Analysis Body of Knowledge) - Requirements elicitation techniques
IIBA Standards - Professional BA practices
Agile Extension to BABOK® Guide - Elicitation in Agile contexts
IEEE 29148 - Requirements engineering standard
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