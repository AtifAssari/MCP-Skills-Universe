---
rating: ⭐⭐
title: upgrade-stripe
url: https://skills.sh/stripe/ai/upgrade-stripe
---

# upgrade-stripe

skills/stripe/ai/upgrade-stripe
upgrade-stripe
Installation
$ npx skills add https://github.com/stripe/ai --skill upgrade-stripe
Summary

Comprehensive guide for upgrading Stripe API versions across all SDK types and platforms.

Covers server-side SDKs (dynamically-typed languages like Python, Node.js, Ruby allow per-request or global version overrides; strongly-typed languages like Java, Go, .NET require SDK updates instead)
Stripe.js uses an evergreen model with biannual major releases (Acacia, Basil, Clover) that automatically pair with corresponding API versions; v3 continues to be supported indefinitely
Mobile SDKs (iOS, Android) use semantic versioning; React Native uses a 0.x.y schema where minor version changes include breaking changes
Includes testing strategies using the Stripe-Version header and a nine-step upgrade checklist covering changelog review, SDK updates, webhook handler changes, and database schema considerations
SKILL.md

The latest Stripe API version is 2026-04-22.dahlia - use this version when upgrading unless the user specifies a different target version.

Upgrading Stripe Versions

This guide covers upgrading Stripe API versions, server-side SDKs, Stripe.js, and mobile SDKs.

Understanding Stripe API Versioning

Stripe uses date-based API versions (e.g., 2026-04-22.dahlia, 2025-08-27.basil, 2024-12-18.acacia). Your account’s API version determines request/response behavior.

Types of Changes

Backward-Compatible Changes (don’t require code updates):

New API resources
New optional request parameters
New properties in existing responses
Changes to opaque string lengths (e.g., object IDs)
New webhook event types

Breaking Changes (require code updates):

Field renames or removals
Behavioral modifications
Removed endpoints or parameters

Review the API Changelog for all changes between versions.

Server-Side SDK Versioning

See SDK Version Management for details.

Dynamically-Typed Languages (Ruby, Python, PHP, Node.js)

These SDKs offer flexible version control:

Global Configuration:

import stripe
stripe.api_version = '2026-04-22.dahlia'

Stripe.api_version = '2026-04-22.dahlia'

const stripe = require('stripe')('sk_test_xxx', {
  apiVersion: '2026-04-22.dahlia'
});


Per-Request Override:

stripe.Customer.create(
  email="customer@example.com",
  stripe_version='2026-04-22.dahlia'
)

Strongly-Typed Languages (Java, Go, .NET)

These use a fixed API version matching the SDK release date. Don’t set a different API version for strongly-typed languages because response objects might not match the strong types in the SDK. Instead, update the SDK to target a new API version.

Best Practice

Always specify the API version you’re integrating against in your code instead of relying on your account’s default API version:

// Good: Explicit version
const stripe = require('stripe')('sk_test_xxx', {
  apiVersion: '2026-04-22.dahlia'
});

// Avoid: Relying on account default
const stripe = require('stripe')('sk_test_xxx');

Stripe.js Versioning

See Stripe.js Versioning for details.

Stripe.js uses an evergreen model with major releases (Acacia, Basil, Clover, Dahlia) on a biannual basis.

Loading Versioned Stripe.js

Via Script Tag:

<script src="https://js.stripe.com/dahlia/stripe.js"></script>


Via npm:

npm install @stripe/stripe-js


Major npm versions correspond to specific Stripe.js versions.

API Version Pairing

Each Stripe.js version automatically pairs with its corresponding API version. For instance:

Dahlia Stripe.js uses 2026-04-22.dahlia API
Acacia Stripe.js uses 2024-12-18.acacia API

You can’t override this association.

Migrating from v3
Identify your current API version in code
Review the changelog for relevant changes
Consider gradually updating your API version before switching Stripe.js versions
Stripe continues supporting v3 indefinitely
Mobile SDK Versioning

See Mobile SDK Versioning for details.

iOS and Android SDKs

Both platforms follow semantic versioning (MAJOR.MINOR.PATCH):

MAJOR: Breaking API changes
MINOR: New functionality (backward-compatible)
PATCH: Bug fixes (backward-compatible)

New features and fixes release only on the latest major version. Upgrade regularly to access improvements.

React Native SDK

Uses a different model (0.x.y schema):

Minor version changes (x): Breaking changes AND new features
Patch updates (y): Critical bug fixes only
Backend Compatibility

All mobile SDKs work with any Stripe API version you use on your backend unless documentation specifies otherwise.

Upgrade Checklist
Review the API Changelog for changes between your current and target versions
Check Upgrades Guide for migration guidance
Update server-side SDK package version (e.g., npm update stripe, pip install --upgrade stripe)
Update the apiVersion parameter in your Stripe client initialization
Test your integration against the new API version using the Stripe-Version header
Update webhook handlers to handle new event structures
Update Stripe.js script tag or npm package version if needed
Update mobile SDK versions in your package manager if needed
Store Stripe object IDs in databases that accommodate up to 255 characters (case-sensitive collation)
Testing API Version Changes

Use the Stripe-Version header to test your code against a new version without changing your default:

curl https://api.stripe.com/v1/customers \
  -u sk_test_xxx: \
  -H "Stripe-Version: 2026-04-22.dahlia"


Or in code:

const stripe = require('stripe')('sk_test_xxx', {
  apiVersion: '2026-04-22.dahlia'  // Test with new version
});

Important Notes
Your webhook listener should handle unfamiliar event types gracefully
Test webhooks with the new version structure before upgrading
Breaking changes are tagged by affected product areas (Payments, Billing, Connect, etc.)
Multiple API versions coexist simultaneously, enabling staged adoption
Weekly Installs
3.4K
Repository
stripe/ai
GitHub Stars
1.5K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail