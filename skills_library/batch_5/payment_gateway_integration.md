---
title: payment-gateway-integration
url: https://skills.sh/aj-geddes/useful-ai-prompts/payment-gateway-integration
---

# payment-gateway-integration

skills/aj-geddes/useful-ai-prompts/payment-gateway-integration
payment-gateway-integration
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill payment-gateway-integration
SKILL.md
Payment Gateway Integration
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Build secure payment processing systems with major payment providers (Stripe, PayPal, Square), handling transactions, subscriptions, webhooks, PCI compliance, and error scenarios across different backend frameworks.

When to Use
Processing customer payments
Implementing subscription billing
Building e-commerce platforms
Handling refunds and disputes
Managing recurring charges
Integrating payment webhooks
Quick Start

Minimal working example:

# config.py
import os

class StripeConfig:
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
    STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY')
    STRIPE_WEBHOOK_SECRET = os.getenv('STRIPE_WEBHOOK_SECRET')

# stripe_service.py
import stripe
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

class StripePaymentService:
    @staticmethod
    def create_payment_intent(amount, currency='usd', description=None, metadata=None):
        """Create a payment intent"""
        try:
            intent = stripe.PaymentIntent.create(
                amount=int(amount * 100),  # Convert to cents
                currency=currency,
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Stripe Integration with Python/Flask	Stripe Integration with Python/Flask
Node.js/Express Stripe Integration	Node.js/Express Stripe Integration
PayPal Integration	PayPal Integration
Subscription Management	Subscription Management
Best Practices
✅ DO
Use official payment SDK libraries
Verify webhook signatures
Store minimal payment information
Never store full credit card numbers
Use HTTPS for all payment routes
Implement proper error handling
Test with sandbox environments
Handle payment failures gracefully
Implement PCI compliance
Log all payment transactions
Use idempotency keys
Implement retry logic
❌ DON'T
Handle raw card data
Store sensitive payment information
Log sensitive details
Trust client-side validation only
Ignore webhook events
Hardcode API keys
Use test keys in production
Skip SSL/TLS verification
Forget to validate amounts
Store payment tokens without encryption
Weekly Installs
317
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn