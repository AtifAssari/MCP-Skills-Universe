---
title: crm domain knowledge
url: https://skills.sh/danhvb/my-ba-skills/crm-domain-knowledge
---

# crm domain knowledge

skills/danhvb/my-ba-skills/CRM Domain Knowledge
CRM Domain Knowledge
Installation
$ npx skills add https://github.com/danhvb/my-ba-skills --skill 'CRM Domain Knowledge'
SKILL.md
CRM Domain Knowledge Skill
Purpose

Provide comprehensive CRM domain knowledge for analyzing requirements in customer relationship management systems across sales, marketing, and service functions.

CRM Core Modules
1. Sales Module

Lead Management:

Lead capture (web forms, imports, manual entry)
Lead scoring and grading
Lead assignment (round-robin, territory-based)
Lead qualification (MQL → SQL)
Lead nurturing campaigns
Lead conversion to opportunity

Opportunity Management:

Opportunity creation and tracking
Sales stages (Prospecting → Qualification → Proposal → Negotiation → Closed Won/Lost)
Probability weighting
Expected close date
Opportunity amount
Competitor tracking
Win/loss analysis

Account & Contact Management:

Account hierarchy (parent-child relationships)
Contact roles (decision maker, influencer, user)
Account teams
Contact history and interactions
360-degree customer view

Sales Pipeline:

Visual pipeline (kanban view)
Pipeline stages
Stage conversion rates
Pipeline velocity
Weighted pipeline value
Forecast accuracy

Quote & Proposal:

Quote generation
Product catalog integration
Pricing rules (discounts, bundles)
Quote approval workflows
E-signature integration
Quote-to-cash process

Key Metrics:

Lead conversion rate: (SQLs / Total Leads) × 100
Opportunity win rate: (Closed Won / Total Opportunities) × 100
Average deal size: Total Revenue / Number of Deals
Sales cycle length: Average days from opportunity creation to close
Pipeline coverage: Pipeline Value / Quota
2. Marketing Module

Campaign Management:

Campaign planning and execution
Multi-channel campaigns (email, social, events, webinars)
Campaign budgets and ROI tracking
A/B testing
Campaign performance analytics

Marketing Automation:

Email marketing workflows
Drip campaigns
Trigger-based emails (behavior, time, score)
Landing pages
Forms and lead capture
Progressive profiling

Lead Nurturing:

Nurture streams
Content mapping to buyer journey
Lead scoring adjustments
Engagement tracking
Automated follow-ups

Segmentation:

Demographic segmentation
Behavioral segmentation
Firmographic segmentation (B2B)
Dynamic lists
Static lists

Key Metrics:

Email open rate: (Emails Opened / Emails Sent) × 100
Click-through rate: (Clicks / Emails Sent) × 100
Conversion rate: (Conversions / Visitors) × 100
Cost per lead: Marketing Spend / Leads Generated
Marketing ROI: (Revenue - Marketing Cost) / Marketing Cost × 100
3. Customer Service Module

Case Management:

Case creation (email, phone, chat, portal)
Case assignment and routing
Case prioritization (severity, SLA)
Case escalation rules
Case resolution and closure
Case history

Knowledge Base:

Article creation and management
Article categories and tags
Search functionality
Article ratings and feedback
Internal vs. customer-facing articles

Service Level Agreements (SLA):

Response time SLA
Resolution time SLA
SLA tracking and alerts
SLA breach notifications
SLA reporting

Omnichannel Support:

Email support
Phone integration (CTI)
Live chat
Social media support
Self-service portal
Mobile app support

Key Metrics:

First response time: Time to first agent response
Average resolution time: Average time to close case
Customer satisfaction (CSAT): Survey score after resolution
First contact resolution: Cases resolved on first contact
SLA compliance: (Cases Meeting SLA / Total Cases) × 100
CRM Data Model
Core Entities

Lead:

Lead source (web, referral, event, cold call)
Lead status (new, contacted, qualified, unqualified)
Lead score (0-100)
Company information
Contact information
Lead owner

Account:

Account name
Industry
Company size (employees, revenue)
Account type (prospect, customer, partner)
Parent account (for hierarchies)
Account owner
Account team

Contact:

Name, title, email, phone
Account relationship
Contact role (decision maker, influencer)
Reporting structure
Preferred communication method
Contact owner

Opportunity:

Opportunity name
Account and primary contact
Amount
Close date
Stage
Probability
Competitors
Opportunity owner

Activity:

Task (to-do item)
Event (meeting, call)
Email
Note
Activity date and time
Related to (lead, contact, opportunity, account)
Common CRM Requirements
Lead Scoring Example
Demographic Scoring:
- Job Title: C-Level (20), VP/Director (15), Manager (10), IC (5)
- Company Size: Enterprise 1000+ (15), Mid-market 100-999 (10), SMB (5)
- Industry: Target industries (5), Others (0)

Behavioral Scoring:
- Pricing page visit (15)
- Whitepaper download (10)
- Webinar attendance (15)
- Demo request (25)
- Email open (2)
- Email click (5)

Negative Scoring:
- Personal email (-10)
- Competitor (-50)
- Student (-15)
- No activity 90 days (-20)

Thresholds:
- MQL: 60 points
- SQL: 75 points

Sales Process Stages
1. Prospecting (10% probability)
2. Qualification (20%)
3. Needs Analysis (40%)
4. Proposal (60%)
5. Negotiation (80%)
6. Closed Won (100%) / Closed Lost (0%)

Integration Requirements

Marketing Automation (HubSpot, Marketo, Pardot):

Bi-directional lead sync
Campaign member sync
Lead scoring sync
Form submission capture

Email (Gmail, Outlook):

Email tracking
Calendar sync
Contact sync
Email templates

Phone (RingCentral, Aircall):

Click-to-dial
Call logging
Call recording
Screen pop on incoming calls

E-signature (DocuSign, Adobe Sign):

Send documents for signature
Track signature status
Store signed documents

Accounting (QuickBooks, Xero):

Customer sync
Invoice sync
Payment tracking
CRM Best Practices
Data Quality
Mandatory fields for key data
Validation rules (email format, phone format)
Duplicate detection and prevention
Data enrichment (Clearbit, ZoomInfo)
Regular data cleanup
User Adoption
Intuitive UI/UX
Mobile access
Minimal data entry (automation)
Integration with daily tools (email, calendar)
Training and support
Process Automation
Lead assignment automation
Email alerts and notifications
Workflow automation
Approval processes
Scheduled reports
Questions for Stakeholders

Sales Process:

What are your sales stages?
What's your average sales cycle?
How do you qualify leads?
What's your territory structure?

Lead Management:

What are your lead sources?
How do you score leads?
What defines MQL vs. SQL?
How are leads assigned?

Integration:

What marketing automation tool?
What email system?
What phone system?
What other systems to integrate?

Reporting:

What KPIs do you track?
Who needs dashboards?
What reports are critical?
References
Salesforce Trailhead
HubSpot Academy
CRM Best Practices Guides
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