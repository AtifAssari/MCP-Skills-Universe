---
title: email-best-practices
url: https://skills.sh/resend/email-best-practices/email-best-practices
---

# email-best-practices

skills/resend/email-best-practices/email-best-practices
email-best-practices
Installation
$ npx skills add https://github.com/resend/email-best-practices --skill email-best-practices
Summary

Comprehensive guidance for building deliverable, compliant, and user-friendly email systems.

Covers authentication setup (SPF/DKIM/DMARC), spam troubleshooting, and deliverability best practices to prevent emails from landing in spam
Includes templates and patterns for transactional emails (password resets, OTPs, confirmations) and marketing emails with proper consent workflows
Provides compliance frameworks for CAN-SPAM, GDPR, and CASL regulations, plus double opt-in and suppression list management
Addresses production reliability through idempotent sending, retry logic, webhook event handling, and bounce/complaint tracking
SKILL.md
Email Best Practices

Guidance for building deliverable, compliant, user-friendly emails.

Architecture Overview
[User] → [Email Form] → [Validation] → [Double Opt-In]
                                              ↓
                                    [Consent Recorded]
                                              ↓
[Suppression Check] ←──────────────[Ready to Send]
        ↓
[Idempotent Send + Retry] ──────→ [Email API]
                                       ↓
                              [Webhook Events]
                                       ↓
              ┌────────┬────────┬─────────────┐
              ↓        ↓        ↓             ↓
         Delivered  Bounced  Complained  Opened/Clicked
                       ↓        ↓
              [Suppression List Updated]
                       ↓
              [List Hygiene Jobs]

Quick Reference
Need to...	See
Set up SPF/DKIM/DMARC, fix spam issues	Deliverability
Build password reset, OTP, confirmations	Transactional Emails
Plan which emails your app needs	Transactional Email Catalog
Build newsletter signup, validate emails	Email Capture
Send newsletters, promotions	Marketing Emails
Ensure CAN-SPAM/GDPR/CASL compliance	Compliance
Decide transactional vs marketing	Email Types
Handle retries, idempotency, errors	Sending Reliability
Process delivery events, set up webhooks	Webhooks & Events
Manage bounces, complaints, suppression	List Management
Start Here

New app? Start with the Catalog to plan which emails your app needs (password reset, verification, etc.), then set up Deliverability (DNS authentication) before sending your first email.

Spam issues? Check Deliverability first—authentication problems are the most common cause. Gmail/Yahoo reject unauthenticated emails.

Marketing emails? Follow this path: Email Capture (collect consent) → Compliance (legal requirements) → Marketing Emails (best practices).

Production-ready sending? Add reliability: Sending Reliability (retry + idempotency) → Webhooks & Events (track delivery) → List Management (handle bounces).

Weekly Installs
5.1K
Repository
resend/email-be…ractices
GitHub Stars
128
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass