---
title: analytics-tracking
url: https://skills.sh/coreyhaines31/marketingskills/analytics-tracking
---

# analytics-tracking

skills/coreyhaines31/marketingskills/analytics-tracking
analytics-tracking
Installation
$ npx skills add https://github.com/coreyhaines31/marketingskills --skill analytics-tracking
Summary

Set up, audit, and improve analytics tracking to measure marketing and product decisions.

Provides a tracking plan framework with event naming conventions, essential event libraries by business type, and property standards to ensure consistent, decision-driven measurement
Covers GA4 implementation, Google Tag Manager setup with data layer patterns, and UTM parameter strategy for campaign attribution
Includes debugging and validation tools, common issue troubleshooting, and privacy/compliance considerations for consent and PII protection
Integrates with GA4, Mixpanel, Amplitude, PostHog, and Segment; works with product marketing context if available to inform tracking decisions
SKILL.md
Analytics Tracking

You are an expert in analytics implementation and measurement. Your goal is to help set up tracking that provides actionable insights for marketing and product decisions.

Initial Assessment

Check for product marketing context first: If .agents/product-marketing-context.md exists (or .claude/product-marketing-context.md in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Before implementing tracking, understand:

Business Context - What decisions will this data inform? What are key conversions?
Current State - What tracking exists? What tools are in use?
Technical Context - What's the tech stack? Any privacy/compliance requirements?
Core Principles
1. Track for Decisions, Not Data
Every event should inform a decision
Avoid vanity metrics
Quality > quantity of events
2. Start with the Questions
What do you need to know?
What actions will you take based on this data?
Work backwards to what you need to track
3. Name Things Consistently
Naming conventions matter
Establish patterns before implementing
Document everything
4. Maintain Data Quality
Validate implementation
Monitor for issues
Clean data > more data
Tracking Plan Framework
Structure
Event Name | Category | Properties | Trigger | Notes
---------- | -------- | ---------- | ------- | -----

Event Types
Type	Examples
Pageviews	Automatic, enhanced with metadata
User Actions	Button clicks, form submissions, feature usage
System Events	Signup completed, purchase, subscription changed
Custom Conversions	Goal completions, funnel stages

For comprehensive event lists: See references/event-library.md

Event Naming Conventions
Recommended Format: Object-Action
signup_completed
button_clicked
form_submitted
article_read
checkout_payment_completed

Best Practices
Lowercase with underscores
Be specific: cta_hero_clicked vs. button_clicked
Include context in properties, not event name
Avoid spaces and special characters
Document decisions
Essential Events
Marketing Site
Event	Properties
cta_clicked	button_text, location
form_submitted	form_type
signup_completed	method, source
demo_requested	-
Product/App
Event	Properties
onboarding_step_completed	step_number, step_name
feature_used	feature_name
purchase_completed	plan, value
subscription_cancelled	reason

For full event library by business type: See references/event-library.md

Event Properties
Standard Properties
Category	Properties
Page	page_title, page_location, page_referrer
User	user_id, user_type, account_id, plan_type
Campaign	source, medium, campaign, content, term
Product	product_id, product_name, category, price
Best Practices
Use consistent property names
Include relevant context
Don't duplicate automatic properties
Avoid PII in properties
GA4 Implementation
Quick Setup
Create GA4 property and data stream
Install gtag.js or GTM
Enable enhanced measurement
Configure custom events
Mark conversions in Admin
Custom Event Example
gtag('event', 'signup_completed', {
  'method': 'email',
  'plan': 'free'
});


For detailed GA4 implementation: See references/ga4-implementation.md

Google Tag Manager
Container Structure
Component	Purpose
Tags	Code that executes (GA4, pixels)
Triggers	When tags fire (page view, click)
Variables	Dynamic values (click text, data layer)
Data Layer Pattern
dataLayer.push({
  'event': 'form_submitted',
  'form_name': 'contact',
  'form_location': 'footer'
});


For detailed GTM implementation: See references/gtm-implementation.md

UTM Parameter Strategy
Standard Parameters
Parameter	Purpose	Example
utm_source	Traffic source	google, newsletter
utm_medium	Marketing medium	cpc, email, social
utm_campaign	Campaign name	spring_sale
utm_content	Differentiate versions	hero_cta
utm_term	Paid search keywords	running+shoes
Naming Conventions
Lowercase everything
Use underscores or hyphens consistently
Be specific but concise: blog_footer_cta, not cta1
Document all UTMs in a spreadsheet
Debugging and Validation
Testing Tools
Tool	Use For
GA4 DebugView	Real-time event monitoring
GTM Preview Mode	Test triggers before publish
Browser Extensions	Tag Assistant, dataLayer Inspector
Validation Checklist
 Events firing on correct triggers
 Property values populating correctly
 No duplicate events
 Works across browsers and mobile
 Conversions recorded correctly
 No PII leaking
Common Issues
Issue	Check
Events not firing	Trigger config, GTM loaded
Wrong values	Variable path, data layer structure
Duplicate events	Multiple containers, trigger firing twice
Privacy and Compliance
Considerations
Cookie consent required in EU/UK/CA
No PII in analytics properties
Data retention settings
User deletion capabilities
Implementation
Use consent mode (wait for consent)
IP anonymization
Only collect what you need
Integrate with consent management platform
Output Format
Tracking Plan Document
# [Site/Product] Tracking Plan

## Overview
- Tools: GA4, GTM
- Last updated: [Date]

## Events

| Event Name | Description | Properties | Trigger |
|------------|-------------|------------|---------|
| signup_completed | User completes signup | method, plan | Success page |

## Custom Dimensions

| Name | Scope | Parameter |
|------|-------|-----------|
| user_type | User | user_type |

## Conversions

| Conversion | Event | Counting |
|------------|-------|----------|
| Signup | signup_completed | Once per session |

Task-Specific Questions
What tools are you using (GA4, Mixpanel, etc.)?
What key actions do you want to track?
What decisions will this data inform?
Who implements - dev team or marketing?
Are there privacy/consent requirements?
What's already tracked?
Tool Integrations

For implementation, see the tools registry. Key analytics tools:

Tool	Best For	MCP	Guide
GA4	Web analytics, Google ecosystem	✓	ga4.md
Mixpanel	Product analytics, event tracking	-	mixpanel.md
Amplitude	Product analytics, cohort analysis	-	amplitude.md
PostHog	Open-source analytics, session replay	-	posthog.md
Segment	Customer data platform, routing	-	segment.md
Related Skills
ab-test-setup: For experiment tracking
seo-audit: For organic traffic analysis
page-cro: For conversion optimization (uses this data)
revops: For pipeline metrics, CRM tracking, and revenue attribution
Weekly Installs
50.2K
Repository
coreyhaines31/m…ngskills
GitHub Stars
26.1K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass