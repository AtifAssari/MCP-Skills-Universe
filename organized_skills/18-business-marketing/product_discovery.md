---
rating: ⭐⭐
title: product-discovery
url: https://skills.sh/ncklrs/startup-os-skills/product-discovery
---

# product-discovery

skills/ncklrs/startup-os-skills/product-discovery
product-discovery
Installation
$ npx skills add https://github.com/ncklrs/startup-os-skills --skill product-discovery
SKILL.md
Product Discovery

Strategic user research and problem validation expertise — from interview techniques and JTBD to opportunity sizing and insight synthesis.

Philosophy

Great products start with great problems. Discovery is how you find problems worth solving for people who will pay.

The best product discovery:

Talk to users, not stakeholders — Customers know their problems, not solutions
Validate problems before solutions — Build the right thing, then build it right
Quantify and qualify — Numbers tell you what, conversations tell you why
Continuous over batched — Weekly habits beat quarterly projects
How This Skill Works

When invoked, apply the guidelines in rules/ organized by:

research-* — User interview techniques, survey design, research ops
discovery-* — Problem discovery, JTBD framework, validation
analysis-* — Synthesis, segmentation, competitive analysis
testing-* — Prototype testing, usability testing
Core Frameworks
Discovery Process
Phase	Activities	Outputs
Explore	Interviews, observation, data mining	Problem space map
Validate	Problem interviews, surveys, experiments	Validated problems
Prioritize	Opportunity scoring, segmentation	Prioritized roadmap
Test	Prototype testing, usability studies	Solution validation
Jobs-to-be-Done Framework
                    ┌─────────────────────┐
                    │    FUNCTIONAL JOB   │
                    │   (What they do)    │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
       ┌──────────┐     ┌──────────┐     ┌──────────┐
       │ EMOTIONAL│     │  SOCIAL  │     │ CONTEXT  │
       │   JOB    │     │   JOB    │     │ (When/   │
       │ (Feel)   │     │ (Appear) │     │  Where)  │
       └──────────┘     └──────────┘     └──────────┘

Opportunity Scoring (OST)
Factor	Weight	Description
Importance	40%	How important is this job to the customer?
Satisfaction	30%	How satisfied are they with current solutions?
Frequency	20%	How often do they encounter this problem?
Willingness to Pay	10%	Will they pay to solve this?

Opportunity Score = Importance + max(Importance - Satisfaction, 0)

Research Method Selection
┌─────────────────────────────────────────────────────────────┐
│                   GENERATIVE RESEARCH                       │
│              (Discover unknown unknowns)                    │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐               │
│  │Contextual │  │ Discovery │  │ Diary    │               │
│  │ Inquiry   │  │ Interviews│  │ Studies  │               │
│  └───────────┘  └───────────┘  └───────────┘               │
├─────────────────────────────────────────────────────────────┤
│                   EVALUATIVE RESEARCH                       │
│              (Validate known hypotheses)                    │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐               │
│  │ Usability │  │  A/B      │  │ Prototype │               │
│  │ Testing   │  │  Testing  │  │ Testing   │               │
│  └───────────┘  └───────────┘  └───────────┘               │
├─────────────────────────────────────────────────────────────┤
│                   QUANTITATIVE RESEARCH                     │
│              (Measure and prioritize)                       │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐               │
│  │  Surveys  │  │ Analytics │  │ Card      │               │
│  │           │  │  Review   │  │ Sorting   │               │
│  └───────────┘  └───────────┘  └───────────┘               │
└─────────────────────────────────────────────────────────────┘

Customer Segmentation Matrix
Dimension	Consumer (B2C)	Business (B2B)
Demographics	Age, income, location	Company size, industry, revenue
Behavior	Usage patterns, purchase history	Buying process, tech stack
Psychographics	Values, lifestyle, attitudes	Company culture, risk tolerance
Needs	Problems, goals, aspirations	Business outcomes, KPIs
Continuous Discovery Cadence
Weekly:
├── 2-3 customer interviews
├── Review analytics/feedback
└── Update opportunity backlog

Monthly:
├── Synthesis session
├── Prioritization review
└── Stakeholder alignment

Quarterly:
├── Deep-dive research sprint
├── Competitive analysis refresh
└── Segment review

Interview Quick Reference
Interview Type	When to Use	Key Questions
Discovery	Exploring problem space	"Tell me about the last time..."
Problem	Validating specific pain	"How painful is this 1-10? Why?"
Solution	Testing concepts	"Would this solve your problem?"
JTBD	Understanding motivation	"What were you trying to accomplish?"
Usability	Testing interfaces	"What do you expect to happen?"
Anti-Patterns
Solution-first discovery — Falling in love with solutions before validating problems
Leading the witness — Asking questions that suggest desired answers
Confirmation bias — Only hearing what supports your hypothesis
Sample of one — Making decisions from a single interview
Proxy research — Asking salespeople instead of customers
Feature requests as research — Users ask for features, not problems
Analysis paralysis — Researching forever, never deciding
HiPPO-driven — Highest Paid Person's Opinion overriding data
Weekly Installs
76
Repository
ncklrs/startup-os-skills
GitHub Stars
18
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass