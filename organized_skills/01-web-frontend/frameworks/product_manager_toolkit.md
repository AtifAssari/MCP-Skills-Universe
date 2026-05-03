---
rating: ⭐⭐⭐
title: product-manager-toolkit
url: https://skills.sh/davila7/claude-code-templates/product-manager-toolkit
---

# product-manager-toolkit

skills/davila7/claude-code-templates/product-manager-toolkit
product-manager-toolkit
Originally fromsickn33/antigravity-awesome-skills
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill product-manager-toolkit
Summary

RICE prioritization, customer interview analysis, PRD templates, and discovery frameworks for product strategy.

Includes automated RICE scoring with portfolio balance analysis, quarterly capacity planning, and roadmap generation from feature datasets
NLP-based interview analyzer extracts pain points, feature requests, jobs-to-be-done patterns, sentiment, and key themes from transcripts
Provides four PRD templates (standard, one-page, agile epic, feature brief) plus discovery frameworks including hypothesis templates and opportunity solution trees
Covers metrics frameworks (north star, funnel analysis, feature success metrics) and best practices for stakeholder management, discovery, and avoiding common product pitfalls
SKILL.md
Product Manager Toolkit

Essential tools and frameworks for modern product management, from discovery to delivery.

Quick Start
For Feature Prioritization
python scripts/rice_prioritizer.py sample  # Create sample CSV
python scripts/rice_prioritizer.py sample_features.csv --capacity 15

For Interview Analysis
python scripts/customer_interview_analyzer.py interview_transcript.txt

For PRD Creation
Choose template from references/prd_templates.md
Fill in sections based on discovery work
Review with stakeholders
Version control in your PM tool
Core Workflows
Feature Prioritization Process

Gather Feature Requests

Customer feedback
Sales requests
Technical debt
Strategic initiatives

Score with RICE

# Create CSV with: name,reach,impact,confidence,effort
python scripts/rice_prioritizer.py features.csv

Reach: Users affected per quarter
Impact: massive/high/medium/low/minimal
Confidence: high/medium/low
Effort: xl/l/m/s/xs (person-months)

Analyze Portfolio

Review quick wins vs big bets
Check effort distribution
Validate against strategy

Generate Roadmap

Quarterly capacity planning
Dependency mapping
Stakeholder alignment
Customer Discovery Process

Conduct Interviews

Use semi-structured format
Focus on problems, not solutions
Record with permission

Analyze Insights

python scripts/customer_interview_analyzer.py transcript.txt


Extracts:

Pain points with severity
Feature requests with priority
Jobs to be done
Sentiment analysis
Key themes and quotes

Synthesize Findings

Group similar pain points
Identify patterns across interviews
Map to opportunity areas

Validate Solutions

Create solution hypotheses
Test with prototypes
Measure actual vs expected behavior
PRD Development Process

Choose Template

Standard PRD: Complex features (6-8 weeks)
One-Page PRD: Simple features (2-4 weeks)
Feature Brief: Exploration phase (1 week)
Agile Epic: Sprint-based delivery

Structure Content

Problem → Solution → Success Metrics
Always include out-of-scope
Clear acceptance criteria

Collaborate

Engineering for feasibility
Design for experience
Sales for market validation
Support for operational impact
Key Scripts
rice_prioritizer.py

Advanced RICE framework implementation with portfolio analysis.

Features:

RICE score calculation
Portfolio balance analysis (quick wins vs big bets)
Quarterly roadmap generation
Team capacity planning
Multiple output formats (text/json/csv)

Usage Examples:

# Basic prioritization
python scripts/rice_prioritizer.py features.csv

# With custom team capacity (person-months per quarter)
python scripts/rice_prioritizer.py features.csv --capacity 20

# Output as JSON for integration
python scripts/rice_prioritizer.py features.csv --output json

customer_interview_analyzer.py

NLP-based interview analysis for extracting actionable insights.

Capabilities:

Pain point extraction with severity assessment
Feature request identification and classification
Jobs-to-be-done pattern recognition
Sentiment analysis
Theme extraction
Competitor mentions
Key quotes identification

Usage Examples:

# Analyze single interview
python scripts/customer_interview_analyzer.py interview.txt

# Output as JSON for aggregation
python scripts/customer_interview_analyzer.py interview.txt json

Reference Documents
prd_templates.md

Multiple PRD formats for different contexts:

Standard PRD Template

Comprehensive 11-section format
Best for major features
Includes technical specs

One-Page PRD

Concise format for quick alignment
Focus on problem/solution/metrics
Good for smaller features

Agile Epic Template

Sprint-based delivery
User story mapping
Acceptance criteria focus

Feature Brief

Lightweight exploration
Hypothesis-driven
Pre-PRD phase
Prioritization Frameworks
RICE Framework
Score = (Reach × Impact × Confidence) / Effort

Reach: # of users/quarter
Impact: 
  - Massive = 3x
  - High = 2x
  - Medium = 1x
  - Low = 0.5x
  - Minimal = 0.25x
Confidence:
  - High = 100%
  - Medium = 80%
  - Low = 50%
Effort: Person-months

Value vs Effort Matrix
         Low Effort    High Effort
         
High     QUICK WINS    BIG BETS
Value    [Prioritize]   [Strategic]
         
Low      FILL-INS      TIME SINKS
Value    [Maybe]       [Avoid]

MoSCoW Method
Must Have: Critical for launch
Should Have: Important but not critical
Could Have: Nice to have
Won't Have: Out of scope
Discovery Frameworks
Customer Interview Guide
1. Context Questions (5 min)
   - Role and responsibilities
   - Current workflow
   - Tools used

2. Problem Exploration (15 min)
   - Pain points
   - Frequency and impact
   - Current workarounds

3. Solution Validation (10 min)
   - Reaction to concepts
   - Value perception
   - Willingness to pay

4. Wrap-up (5 min)
   - Other thoughts
   - Referrals
   - Follow-up permission

Hypothesis Template
We believe that [building this feature]
For [these users]
Will [achieve this outcome]
We'll know we're right when [metric]

Opportunity Solution Tree
Outcome
├── Opportunity 1
│   ├── Solution A
│   └── Solution B
└── Opportunity 2
    ├── Solution C
    └── Solution D

Metrics & Analytics
North Star Metric Framework
Identify Core Value: What's the #1 value to users?
Make it Measurable: Quantifiable and trackable
Ensure It's Actionable: Teams can influence it
Check Leading Indicator: Predicts business success
Funnel Analysis Template
Acquisition → Activation → Retention → Revenue → Referral

Key Metrics:
- Conversion rate at each step
- Drop-off points
- Time between steps
- Cohort variations

Feature Success Metrics
Adoption: % of users using feature
Frequency: Usage per user per time period
Depth: % of feature capability used
Retention: Continued usage over time
Satisfaction: NPS/CSAT for feature
Best Practices
Writing Great PRDs
Start with the problem, not solution
Include clear success metrics upfront
Explicitly state what's out of scope
Use visuals (wireframes, flows)
Keep technical details in appendix
Version control changes
Effective Prioritization
Mix quick wins with strategic bets
Consider opportunity cost
Account for dependencies
Buffer for unexpected work (20%)
Revisit quarterly
Communicate decisions clearly
Customer Discovery Tips
Ask "why" 5 times
Focus on past behavior, not future intentions
Avoid leading questions
Interview in their environment
Look for emotional reactions
Validate with data
Stakeholder Management
Identify RACI for decisions
Regular async updates
Demo over documentation
Address concerns early
Celebrate wins publicly
Learn from failures openly
Common Pitfalls to Avoid
Solution-First Thinking: Jumping to features before understanding problems
Analysis Paralysis: Over-researching without shipping
Feature Factory: Shipping features without measuring impact
Ignoring Technical Debt: Not allocating time for platform health
Stakeholder Surprise: Not communicating early and often
Metric Theater: Optimizing vanity metrics over real value
Integration Points

This toolkit integrates with:

Analytics: Amplitude, Mixpanel, Google Analytics
Roadmapping: ProductBoard, Aha!, Roadmunk
Design: Figma, Sketch, Miro
Development: Jira, Linear, GitHub
Research: Dovetail, UserVoice, Pendo
Communication: Slack, Notion, Confluence
Quick Commands Cheat Sheet
# Prioritization
python scripts/rice_prioritizer.py features.csv --capacity 15

# Interview Analysis
python scripts/customer_interview_analyzer.py interview.txt

# Create sample data
python scripts/rice_prioritizer.py sample

# JSON outputs for integration
python scripts/rice_prioritizer.py features.csv --output json
python scripts/customer_interview_analyzer.py interview.txt json

Weekly Installs
463
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass