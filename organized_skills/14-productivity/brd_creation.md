---
title: brd creation
url: https://skills.sh/danhvb/my-ba-skills/brd-creation
---

# brd creation

skills/danhvb/my-ba-skills/BRD Creation
BRD Creation
Installation
$ npx skills add https://github.com/danhvb/my-ba-skills --skill 'BRD Creation'
SKILL.md
BRD Creation Skill
Purpose

This skill enables AI assistants to create comprehensive, professional Business Requirement Documents (BRDs) that clearly communicate business needs, objectives, and high-level requirements to stakeholders and development teams.

When to Use This Skill
After completing requirements elicitation
At the start of a new project or major initiative
When seeking executive approval and funding
To establish project scope and boundaries
Before creating detailed FRS documents
What is a BRD?

A Business Requirement Document (BRD) is a formal document that:

Describes the business problem or opportunity
Defines business objectives and success criteria
Outlines high-level business requirements
Establishes project scope (in-scope and out-of-scope)
Identifies stakeholders and their needs
Documents assumptions, constraints, and dependencies

BRD vs. FRS:

BRD: WHAT the business needs and WHY (business perspective)
FRS: HOW the system will meet those needs (technical perspective)
BRD Structure
1. Executive Summary

Purpose: Provide a concise overview for busy executives

Contents:

Project name and brief description
Business problem or opportunity (2-3 sentences)
Proposed solution overview (2-3 sentences)
Expected business benefits
High-level timeline and budget
Key success metrics

Length: 1 page maximum

Writing Tips:

Write this section LAST (after completing the rest of the BRD)
Use business language, not technical jargon
Focus on business value and ROI
Make it compelling - this may be all executives read

Example:

Project: Mobile App Development for Customer Self-Service

Business Problem: Customers currently must call our support center for account inquiries, order tracking, and returns, resulting in 15,000+ monthly support calls and $450K annual support costs. Customer satisfaction scores for support are 3.2/5.

Proposed Solution: Develop a mobile application (iOS and Android) enabling customers to self-serve for common inquiries, track orders in real-time, and initiate returns without agent assistance.

Expected Benefits: Reduce support call volume by 60% (9,000 calls/month), save $270K annually in support costs, improve customer satisfaction to 4.5/5, and increase customer retention by 15%.

Investment: $180K development cost, 4-month timeline

ROI: Payback in 8 months, $540K savings over 2 years

2. Business Objectives

Purpose: Define what the business wants to achieve

Contents:

Primary business objective
Secondary objectives
Alignment with company strategy
Success criteria (measurable)

Format: Use SMART criteria (Specific, Measurable, Achievable, Relevant, Time-bound)

Example:

Primary Objective: Reduce customer support costs by 60% within 6 months of mobile app launch

Secondary Objectives:

Improve customer satisfaction score from 3.2 to 4.5 within 3 months of launch
Increase customer retention rate by 15% within 12 months
Enable 24/7 customer self-service capabilities

Strategic Alignment: Supports company's digital transformation initiative and customer-first strategy

Success Criteria:

70% of customers download and activate the app within 6 months
60% reduction in support call volume
4.5+ app store rating
80% of users complete tasks without contacting support
3. Background & Context

Purpose: Provide context for why this project is needed

Contents:

Current situation description
History and evolution of the problem
Previous attempts to solve (if any)
Market or competitive drivers
Regulatory or compliance drivers (if applicable)

Example:

Our customer support center currently handles 15,000 calls per month, with 70% being routine inquiries (order status, account balance, return requests) that don't require human expertise. Industry benchmarks show that companies with self-service mobile apps reduce support costs by 50-70% while improving customer satisfaction.

Our main competitors (CompanyX and CompanyY) launched mobile apps in 2024 and have seen significant improvements in customer satisfaction and retention. Customer surveys indicate that 65% of our customers prefer mobile self-service over calling support.

Previous attempts to address this through a web portal in 2023 achieved only 15% adoption due to poor mobile experience and lack of push notifications for order updates.

4. Stakeholder Analysis

Purpose: Identify who is impacted and their needs

Format: Table with stakeholder roles, interests, and requirements

Stakeholder Group	Key Representatives	Interest/Concern	Key Requirements
Customers	End users	Easy access to account info, order tracking	Intuitive UI, fast performance, offline access
Customer Support	Support Manager	Reduced call volume, better tools	Integration with support system, escalation path
IT Operations	IT Director	System stability, security	Secure authentication, API performance, monitoring
Marketing	Marketing VP	Customer engagement, retention	Push notifications, personalization, analytics
Executive Team	CEO, CFO	ROI, strategic alignment	Cost savings, customer satisfaction improvement
5. Scope Definition
5.1 In-Scope

Purpose: Clearly define what WILL be included

Format: Categorized list of features/capabilities

Example for E-commerce Mobile App:

Account Management:

User registration and login
Profile management
Password reset
Biometric authentication (Face ID, Touch ID)

Order Management:

Order history viewing
Real-time order tracking
Order details and invoice download
Reorder functionality

Product Browsing:

Product catalog browsing
Product search and filtering
Product details and images
Wishlist management

Customer Support:

FAQ and help center
Live chat integration
Support ticket submission
Call-back request

Notifications:

Order status push notifications
Promotional notifications
Delivery updates
5.2 Out-of-Scope

Purpose: Explicitly state what will NOT be included (manage expectations)

Example:

In-app purchasing (Phase 2)
Augmented reality product preview (Phase 2)
Social media integration (Future consideration)
Loyalty program management (Separate project)
International shipping (Q3 2026 expansion)
6. Business Requirements

Format: Organized by category with clear, business-focused language

6.1 Functional Requirements (High-Level)

BR-001: User Authentication

Requirement: System shall provide secure user authentication
Business Value: Protect customer data and ensure privacy
Priority: Must Have
Success Criteria: 99.9% successful authentication rate, < 3 seconds login time

BR-002: Order Tracking

Requirement: System shall provide real-time order status and tracking
Business Value: Reduce "where is my order" support calls (currently 35% of call volume)
Priority: Must Have
Success Criteria: Real-time updates within 5 minutes of status change

BR-003: Push Notifications

Requirement: System shall send push notifications for order updates
Business Value: Proactive communication reduces customer anxiety and support calls
Priority: Must Have
Success Criteria: 90% notification delivery rate, opt-in rate > 60%
6.2 Non-Functional Requirements (High-Level)

BR-NFR-001: Performance

App shall load within 3 seconds on 4G connection
API response time < 2 seconds for 95% of requests
Support 50,000 concurrent users

BR-NFR-002: Availability

99.9% uptime during business hours (6 AM - 11 PM)
Planned maintenance windows outside business hours

BR-NFR-003: Security

Comply with PCI DSS for payment data
Encrypt all data in transit (TLS 1.3)
Support biometric authentication
Session timeout after 15 minutes of inactivity

BR-NFR-004: Usability

Support iOS 15+ and Android 12+
Comply with WCAG 2.1 Level AA accessibility standards
Support English and Spanish languages
Intuitive UI requiring no training

BR-NFR-005: Compliance

GDPR compliance for EU customers
CCPA compliance for California customers
SOC 2 Type II compliance
7. Assumptions

Purpose: Document what we're assuming to be true

Example:

Customers have smartphones with iOS 15+ or Android 12+
Existing backend APIs can support mobile app requirements with minor enhancements
Customer support team will be trained on new escalation process
Marketing will drive app adoption through email and social campaigns
IT infrastructure can handle projected user load
Third-party services (push notifications, analytics) will remain available
8. Constraints

Purpose: Document limitations and restrictions

Categories:

Technical: Must use existing AWS infrastructure, must integrate with legacy order management system
Budget: $180K total budget (development, testing, deployment)
Timeline: Must launch by Q2 2026 for seasonal campaign
Resource: 2 mobile developers, 1 QA, 1 BA available
Regulatory: Must comply with app store guidelines (Apple, Google)
Business: Cannot disrupt current web experience during development
9. Dependencies

Purpose: Identify what this project depends on

Example:

Dependency	Description	Owner	Status	Risk
Backend API Enhancement	Order tracking API needs real-time updates	IT Team	In Progress	Medium
Push Notification Service	Need to procure service (OneSignal or Firebase)	IT Team	Not Started	Low
App Store Accounts	Apple Developer and Google Play accounts	Marketing	Pending	Low
Customer Data Migration	Clean customer data for app migration	Data Team	Planned	Medium
Support System Integration	Integrate with Zendesk for ticket creation	IT Team	Not Started	High
10. Risks & Mitigation
Risk	Impact	Probability	Mitigation Strategy
Low app adoption rate	High	Medium	Comprehensive marketing campaign, in-app incentives, email promotion
Backend API performance issues	High	Medium	Load testing, performance optimization, caching strategy
App store rejection	Medium	Low	Early review of guidelines, compliance checklist, beta testing
Integration delays with legacy systems	High	High	Early technical spike, parallel development, fallback plan
Security vulnerabilities	Critical	Low	Security audit, penetration testing, code review
11. Success Metrics & KPIs

Adoption Metrics:

App downloads: 70% of active customers within 6 months
Monthly active users (MAU): 60% of downloads
Daily active users (DAU): 25% of MAU

Business Impact Metrics:

Support call reduction: 60% decrease within 3 months
Cost savings: $270K annually
Customer satisfaction: Increase from 3.2 to 4.5
Customer retention: 15% improvement

Technical Metrics:

App store rating: 4.5+ stars
Crash rate: < 1%
App load time: < 3 seconds
API response time: < 2 seconds (95th percentile)

Engagement Metrics:

Average session duration: > 3 minutes
Feature usage: 80% use order tracking, 60% use account management
Push notification opt-in: > 60%
12. Timeline & Milestones
Phase	Milestone	Duration	Target Date
Planning	BRD Approval	2 weeks	Feb 1, 2026
Design	UX/UI Design Complete	3 weeks	Feb 22, 2026
Development	iOS App Development	8 weeks	Apr 19, 2026
Development	Android App Development	8 weeks	Apr 19, 2026
Testing	QA and UAT	3 weeks	May 10, 2026
Deployment	App Store Submission	1 week	May 17, 2026
Launch	Public Launch	-	May 24, 2026
13. Budget Estimate
Category	Cost	Notes
Development (iOS & Android)	$120,000	2 developers x 3 months
UX/UI Design	$25,000	Design agency
QA & Testing	$15,000	QA engineer + device testing
Project Management	$10,000	BA + PM time
Third-party Services (Year 1)	$5,000	Push notifications, analytics
App Store Fees	$200	Apple ($99) + Google ($25) + buffer
Contingency (10%)	$17,520	Risk buffer
Total	$192,720	
14. Approval & Sign-off
Role	Name	Signature	Date
Business Sponsor			
Product Owner			
IT Director			
Finance			
Business Analyst			
Domain-Specific BRD Considerations
E-commerce BRDs

Focus Areas:

Customer journey and conversion optimization
Payment and security requirements
Inventory and order management integration
Multi-channel consistency
Seasonal traffic and scalability

Key Metrics: Conversion rate, cart abandonment, average order value, customer lifetime value

ERP BRDs

Focus Areas:

Business process transformation
Change management and training
Data migration and cleansing
Integration with existing systems
Compliance and audit requirements

Key Metrics: Process efficiency, cost reduction, data accuracy, user adoption

CRM BRDs

Focus Areas:

Sales process optimization
Lead management and conversion
Customer 360-degree view
Marketing and sales alignment
Reporting and analytics

Key Metrics: Lead conversion rate, sales cycle time, customer satisfaction, pipeline value

CDP BRDs

Focus Areas:

Data unification strategy
Privacy and consent management
Segmentation and personalization
Marketing activation channels
Data governance

Key Metrics: Data completeness, segment accuracy, campaign performance, ROI

Mobile/Web BRDs

Focus Areas:

User experience and engagement
Performance and responsiveness
Cross-platform consistency
Offline capabilities
App store optimization

Key Metrics: User engagement, session duration, retention rate, app store rating

BRD Best Practices
Writing Style

✅ Do:

Use clear, concise business language
Write for your audience (executives, not developers)
Focus on business value and outcomes
Use active voice
Be specific and measurable
Include visual aids (diagrams, charts)

❌ Don't:

Use technical jargon or acronyms without explanation
Include implementation details (save for FRS)
Make vague statements ("improve efficiency")
Assume prior knowledge
Write overly long sentences
Structure & Format
Use consistent formatting and numbering
Include table of contents for documents > 10 pages
Use tables for structured information
Include page numbers and version control
Use headers and white space for readability
Collaboration
Involve stakeholders early and often
Review drafts with business owners
Get technical feasibility validation
Iterate based on feedback
Maintain version history
Quality Checks
 Executive summary is compelling and concise
 Business objectives are SMART
 Scope is clearly defined (in and out)
 Requirements are business-focused, not technical
 Success metrics are measurable
 Assumptions and constraints are documented
 Dependencies and risks are identified
 Budget and timeline are realistic
 Document is well-formatted and professional
 All stakeholders have reviewed and approved
Tools for BRD Creation
Lark
Use Lark Docs for collaborative BRD writing
Use comments for stakeholder feedback
Use version history to track changes
Share with stakeholders for review and approval
Notion
Create BRD template in Notion
Use database properties for metadata (version, status, owner)
Link to related requirements and user stories
Embed diagrams and mockups
Figma
Create process flow diagrams
Design user journey maps
Build wireframes to illustrate concepts
Embed Figma links in BRD
Next Steps After BRD Approval
Create detailed Functional Requirements Specification (FRS) - see frs-creation skill
Develop use cases - see use-case-documentation skill
Create user stories for Agile development - see user-story-writing skill
Design process maps - see process-mapping skill
Plan UAT - see uat-planning skill
References
BABOK® Guide - Business requirements documentation standards
IIBA Standards - Professional BA documentation practices
PMI PMBOK® Guide - Project charter and business case development
IEEE 29148 - Requirements engineering and documentation standards
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