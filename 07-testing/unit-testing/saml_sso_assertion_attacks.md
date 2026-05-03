---
rating: ⭐⭐
title: saml-sso-assertion-attacks
url: https://skills.sh/yaklang/hack-skills/saml-sso-assertion-attacks
---

# saml-sso-assertion-attacks

skills/yaklang/hack-skills/saml-sso-assertion-attacks
saml-sso-assertion-attacks
Installation
$ npx skills add https://github.com/yaklang/hack-skills --skill saml-sso-assertion-attacks
SKILL.md
SKILL: SAML SSO and Assertion Attacks — Signature Validation, Binding, and Trust Confusion

AI LOAD INSTRUCTION: Use this skill when the target uses SAML-based SSO and you need to validate assertion trust: signature coverage, audience and recipient checks, ACS handling, XML parsing weaknesses, and IdP/SP confusion.

1. WHEN TO LOAD THIS SKILL

Load when:

Enterprise SSO uses SAML requests or responses
You see SAMLRequest, SAMLResponse, XML assertions, or ACS endpoints
Login flows involve an external IdP and browser POST/redirect binding
2. HIGH-VALUE MISCONFIGURATION CHECKS
Theme	What to Check
signature validation	unsigned assertion accepted, wrong node signed, signature wrapping
audience and recipient	weak Audience, Recipient, Destination, or ACS validation
issuer trust	wrong IdP accepted or multi-tenant issuer confusion
replay and freshness	missing InResponseTo, weak NotBefore / NotOnOrAfter enforcement
account mapping	email-only binding, case folding, unverified attributes
XML parser behavior	XXE-like parser issues or unsafe transforms around SAML documents
3. QUICK TRIAGE
Capture one full login round trip.
Inspect which XML nodes are signed and which attributes drive account binding.
Compare SP-initiated and IdP-initiated flows.
Test replay, altered attributes, and assertion placement confusion.
4. RELATED ROUTES
XML parser attack depth: xxe xml external entity
OAuth or OIDC SSO alternatives: oauth oidc misconfiguration
Auth boundary issues after SSO: authbypass authentication flaws
Weekly Installs
317
Repository
yaklang/hack-skills
GitHub Stars
368
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass