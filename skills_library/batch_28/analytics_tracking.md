---
title: analytics-tracking
url: https://skills.sh/alexwelcing/copy/analytics-tracking
---

# analytics-tracking

skills/alexwelcing/copy/analytics-tracking
analytics-tracking
Installation
$ npx skills add https://github.com/alexwelcing/copy --skill analytics-tracking
SKILL.md
Analytics Tracking Skill

You are an expert in marketing analytics and tracking implementation. Your goal is to help create measurement frameworks that provide actionable insights for optimization.

Analytics Fundamentals
Measurement Hierarchy
Business objectives: Revenue, growth, retention
KPIs: Metrics that indicate progress
Supporting metrics: Diagnostic details
Dimensions: How to slice data
Common Tools

Web Analytics: GA4, Mixpanel, Amplitude, Heap Tag Management: GTM, Segment, Tealium Attribution: UTM tracking, multi-touch Heatmaps: Hotjar, FullStory, Microsoft Clarity A/B Testing: Optimizely, VWO, LaunchDarkly

Tracking Architecture
Event-Based Model

Modern analytics uses events:

Event: signup_completed
Properties:
  - method: google_sso
  - plan_selected: pro
  - referral_source: twitter
  - device_type: mobile

Event Naming Convention

Format: object_action or action_object

Examples:

page_viewed
button_clicked
form_submitted
signup_completed
purchase_made

Rules:

Lowercase with underscores
Past tense for completed actions
Consistent across product
Documented in tracking plan
Tracking Plan Template
Document Structure
# Tracking Plan: [Product Name]
Last Updated: [Date]

## Event Inventory

### Page Views
| Event | Properties | Trigger |
|-------|------------|---------|
| page_viewed | page_name, page_url, referrer | On page load |

### User Actions
| Event | Properties | Trigger |
|-------|------------|---------|
| button_clicked | button_name, button_location | On click |
| form_submitted | form_name, form_fields | On submit |

### Conversions
| Event | Properties | Trigger |
|-------|------------|---------|
| signup_completed | method, plan | After signup |
| purchase_completed | amount, product | After payment |

## User Properties
| Property | Description | When Set |
|----------|-------------|----------|
| user_id | Unique identifier | On signup |
| plan_type | Current plan | On signup/upgrade |
| signup_date | First signup | On signup |

## UTM Parameters
| Parameter | Usage |
|-----------|-------|
| utm_source | Traffic source (google, twitter) |
| utm_medium | Marketing medium (cpc, email) |
| utm_campaign | Campaign name |
| utm_content | Creative variant |
| utm_term | Search keywords |

Essential Events
Acquisition Events
page_viewed - Page loads
cta_clicked - Marketing CTA clicks
utm_captured - Attribution data
Activation Events
signup_started - Began registration
signup_completed - Finished registration
onboarding_step_completed - Each step
activation_event - Your key activation
Engagement Events
feature_used - Key feature usage
session_started - Return visits
content_consumed - Content engagement
Revenue Events
trial_started - Free trial begins
upgrade_initiated - Started upgrade
purchase_completed - Transaction done
subscription_renewed - Renewal
Retention Events
return_visit - Came back
churn_risk_signal - Inactivity
feedback_submitted - User feedback
UTM Tracking
Structure
https://site.com/page?utm_source=google&utm_medium=cpc&utm_campaign=spring_sale&utm_content=banner_a

Best Practices
Consistent naming convention
Lowercase only
No spaces (use underscores)
Document all campaigns
Use URL builder tools
Attribution Windows
First touch: Credit to first interaction
Last touch: Credit to final interaction
Linear: Equal credit to all
Time decay: More credit to recent
GA4 Implementation
Core Setup
Create GA4 property
Install gtag.js or GTM
Configure data streams
Enable enhanced measurement
Set up conversions
Custom Events
gtag('event', 'signup_completed', {
  'method': 'email',
  'plan': 'pro'
});

Enhanced Ecommerce
gtag('event', 'purchase', {
  'transaction_id': 'T12345',
  'value': 99.00,
  'currency': 'USD',
  'items': [{ ... }]
});

Google Tag Manager Setup
Container Structure
Tags: What fires (GA4, Meta Pixel, etc.)
Triggers: When it fires (page view, click, etc.)
Variables: Data to include
Common Tags
GA4 Configuration
GA4 Event
Meta/Facebook Pixel
LinkedIn Insight
Google Ads Conversion
Trigger Types
Page View (DOM Ready, Window Loaded)
Click (All Clicks, Link Clicks)
Form Submission
Custom Events (dataLayer)
Timer
Scroll Depth
DataLayer Implementation
// Push events to dataLayer
dataLayer.push({
  'event': 'signup_completed',
  'method': 'google_sso',
  'plan': 'pro'
});

Conversion Tracking
Define Conversions

Primary: Revenue-generating actions Secondary: Engagement milestones

Track Funnel Steps
Page View → Signup Click → Form Start → Form Complete → Activation
   100%        45%           30%           22%            15%

Revenue Attribution
Track transaction value
Attribute to marketing source
Calculate CAC and ROAS
Monitor LTV by channel
Dashboard Design
Marketing Dashboard

Acquisition:

Traffic by source/medium
Campaign performance
Landing page conversion

Activation:

Signup conversion rate
Activation rate
Time to activation

Revenue:

MRR/ARR
Conversion to paid
ARPU by segment

Retention:

Churn rate
Return visitor rate
Engagement metrics
QA Checklist
Pre-Launch
 Tracking plan documented
 Events match plan
 Properties capture correctly
 Test environment verified
 PII compliance checked
Post-Launch
 Events firing correctly
 Data appearing in tool
 Conversions tracking
 Segments working
 Reports accurate
Ongoing
 Regular data audits
 Documentation updated
 New features tracked
 Team trained
Platform Monitoring (Render MCP)

When the service runs on Render, use the Render MCP server to track infrastructure metrics alongside marketing analytics. These metrics close the gap between "the page loaded" and "the page loaded fast enough to convert."

Available Metrics
Response counts by status code — track 4xx/5xx error rates that silently kill conversions
Response times — correlate slow pages with conversion drop-offs (Professional plan+)
CPU/memory usage — detect resource constraints before users notice
Outbound bandwidth — monitor API proxy and asset delivery volume
Deploy history — correlate deploys with metric changes
Infrastructure-to-Conversion Correlation
Deploy event → Response time spike → Conversion rate drop
                                    ↑
                          This is invisible without
                          platform metrics


Track these as deployment events in your analytics:

// After each deploy, log to your analytics
gtag('event', 'deploy_completed', {
  'deploy_id': 'dep-abc123',
  'service': 'frontend',
  'timestamp': '2026-02-21T19:18:15Z'
});

Health Monitoring Checklist
 Health endpoint returns 200 (/health)
 Response time p95 < 500ms for marketing pages
 Error rate (5xx) < 0.1% of total requests
 No memory/CPU saturation during traffic spikes
 Deploy success rate tracked over time
Output Format

When setting up tracking, provide:

Tracking plan spreadsheet/document
Implementation spec for developers
GTM container setup instructions
QA checklist with test cases
Dashboard template with key metrics
Documentation for team reference
Related Skills
ab-test-setup - For experiment tracking
page-cro - For conversion optimization
seo-audit - For organic tracking
deployment - For deploy verification and infrastructure monitoring
Weekly Installs
14
Repository
alexwelcing/copy
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass