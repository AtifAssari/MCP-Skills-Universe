---
title: cdp domain knowledge
url: https://skills.sh/danhvb/my-ba-skills/cdp-domain-knowledge
---

# cdp domain knowledge

skills/danhvb/my-ba-skills/CDP Domain Knowledge
CDP Domain Knowledge
Installation
$ npx skills add https://github.com/danhvb/my-ba-skills --skill 'CDP Domain Knowledge'
SKILL.md
CDP Domain Knowledge Skill
Purpose

Provide comprehensive CDP domain knowledge for analyzing requirements in customer data unification, segmentation, and marketing activation.

What is a CDP?

A Customer Data Platform (CDP) is a packaged software that:

Collects customer data from multiple sources
Creates unified customer profiles (360-degree view)
Enables segmentation and audience building
Activates data to marketing channels
CDP vs DMP vs CRM
Capability	CDP	DMP	CRM
Data Type	First-party + Third-party	Third-party cookies	First-party
Identity	Known + Anonymous	Mostly anonymous	Known customers
Data Persistence	Long-term	Short-term (90 days)	Long-term
Primary Use	Personalization, Analytics	Advertising	Sales/Service
User Management	Individuals	Segments/Audiences	Accounts/Contacts
CDP Architecture
Data Flow
Data Sources → Ingestion → Identity Resolution → Profile Unification → 
Segmentation → Audience Building → Channel Activation

Core Components

1. Data Collection:

Website/app events (page views, clicks, transactions)
CRM data (contacts, accounts, opportunities)
Transaction data (orders, returns, support tickets)
Marketing data (email opens, campaign responses)
Offline data (in-store purchases, call center)
Third-party data (demographics, intent)

2. Identity Resolution:

Deterministic matching (email, phone, customer ID)
Probabilistic matching (device fingerprinting, behavior)
Cross-device stitching
Household linkage
Anonymous to known conversion

3. Profile Unification:

Golden record creation
Attribute standardization
Conflict resolution (which source wins?)
Profile enrichment
Historical event storage

4. Segmentation:

Rule-based segments
AI/ML-based segments
Dynamic vs. static segments
Lookalike audiences
Predictive segments

5. Activation:

Real-time personalization
Email/SMS marketing
Advertising platforms
Customer service systems
Analytics/BI tools
Key CDP Concepts
Identity Resolution

Matching Keys:

Email address (primary)
Phone number (hashed)
Customer ID / Loyalty ID
Device IDs (IDFA, GAID, cookie)
Address + Name combination

Identity Graph:

            Cookie_A
               ↓
Email_1 ← Customer_123 → Device_B
               ↓
          Phone_555


Confidence Levels:

High: Email match, customer ID
Medium: Phone + first name
Low: Cookie + behavior patterns
Customer Profile

Profile Attributes:

## John Smith - Customer Profile

### Identity
- Customer ID: CUST-123456
- Email: john.smith@email.com
- Phone: +1-555-123-4567
- Device IDs: [device_a, device_b]

### Demographics
- Age: 35
- Gender: Male
- Location: San Francisco, CA
- Household Income: $100-150K

### Behavioral
- First Purchase: 2024-01-15
- Last Purchase: 2026-01-10
- Total Orders: 12
- LTV: $1,245
- Average Order Value: $103.75
- Favorite Category: Electronics
- Last Page Viewed: Laptops
- Email Engagement: High (45% open rate)

### Segments
- VIP Customer
- Tech Enthusiast
- High Email Engager
- Likely to Churn (ML score: 0.65)

### Consent
- Email Marketing: Opted In
- SMS: Opted Out
- Third-party Sharing: Opted Out
- Last Updated: 2026-01-01

Segmentation

Segment Types:

Static Segments: Fixed list, doesn't update automatically

Customers who purchased in Black Friday 2025


Dynamic Segments: Updates as data changes

Customers who purchased in last 30 days
AND total spend > $500
AND category = "Electronics"


Predictive Segments: ML-based predictions

Customers with churn risk > 70%
Customers likely to purchase in next 7 days


Lookalike Segments: Similar to seed audience

Customers similar to "VIP Customers" segment

Data Activation

Activation Channels:

Email: Personalized campaigns, triggered emails
SMS/Push: Time-sensitive notifications
Advertising: Facebook, Google, programmatic
Website: Real-time personalization
Customer Service: Agent context
Analytics: Reporting and insights

Real-time vs Batch:

Real-time: Website personalization, triggered emails
Batch: Daily email campaigns, weekly reports
Privacy & Consent
Consent Management

Consent Types:

Marketing email opt-in/out
SMS opt-in/out
Third-party data sharing
Cookie consent
Cross-site tracking

Consent Requirements:

GDPR (EU): Explicit opt-in required
CCPA (California): Opt-out right
LGPD (Brazil): Consent required
PDPA (Thailand/Singapore): Consent required
Data Rights

User Rights (GDPR/CCPA):

Right to access (what data do you have?)
Right to rectification (fix incorrect data)
Right to erasure (delete my data)
Right to portability (give me my data)
Right to opt-out (don't sell my data)
Key Metrics
Data Quality
Profile completeness (% fields populated)
Identity match rate
Data freshness (recency of updates)
Duplicate rate
Engagement
Segment size and growth
Activation success rate
Channel reach
Personalization lift
Business Impact
Revenue influenced by CDP
Customer lifetime value improvement
Campaign ROI improvement
Reduced customer acquisition cost
Common CDP Requirements
Data Collection
REQ-001: System shall collect website events including page views, product views, add-to-cart, and purchases
REQ-002: System shall ingest CRM data via API daily
REQ-003: System shall capture email engagement events in real-time

Identity Resolution
REQ-010: System shall match profiles using email as primary key
REQ-011: System shall stitch anonymous cookie to known profile on login
REQ-012: System shall maintain identity graph with confidence scores

Segmentation
REQ-020: System shall support dynamic segment creation using AND/OR logic
REQ-021: System shall recalculate segment membership daily at minimum
REQ-022: System shall support audience size estimation before creation

Activation
REQ-030: System shall sync audiences to Facebook in near real-time
REQ-031: System shall trigger email via Klaviyo when user enters segment
REQ-032: System shall provide personalization API for website with < 100ms latency

Questions for Stakeholders
What data sources need to be connected?
How do you identify customers today?
What segments do you need?
Which marketing channels for activation?
What personalization use cases?
Privacy/consent requirements?
Real-time vs batch needs?
Popular CDP Platforms
Segment: Developer-friendly, data infrastructure
mParticle: Mobile-focused, SDK expertise
Treasure Data: Enterprise, data lake integration
Tealium: Tag management heritage
Adobe Experience Platform: Adobe ecosystem
Salesforce CDP: Salesforce ecosystem
References
CDP Institute Resources
First-party Data Strategy
Privacy Regulations (GDPR, CCPA)
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