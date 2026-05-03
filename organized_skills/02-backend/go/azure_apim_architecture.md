---
rating: ⭐⭐⭐
title: azure-apim-architecture
url: https://skills.sh/thomast1906/github-copilot-agent-skills/azure-apim-architecture
---

# azure-apim-architecture

skills/thomast1906/github-copilot-agent-skills/azure-apim-architecture
azure-apim-architecture
Installation
$ npx skills add https://github.com/thomast1906/github-copilot-agent-skills --skill azure-apim-architecture
SKILL.md
Azure APIM Architecture Skill

Provides comprehensive guidance on Azure API Management architecture patterns for enterprise API marketplaces, including component selection, network topology, cost optimization, and design decision rationale.

When to Use This Skill

Activate this skill when users ask questions related to:

Component selection: "Should I use Azure Front Door or Application Gateway?"
Network architecture: "VNet Internal mode vs External mode?"
Multi-environment strategy: "Separate APIM instances or workspaces for dev/test/prod?"
Cost optimization: "How much will this cost in UK South?"
Authentication patterns: "OAuth vs subscription keys for public APIs?"
Design rationale: "Why did you choose X instead of Y?"
Core Knowledge
1. Azure Front Door Premium (Not Application Gateway)

Decision: Use Azure Front Door Premium as ingress layer

Rationale:

Built-in DDoS protection: Platform-level, included at no extra cost (saves £2,644/month vs separate Azure DDoS Standard)
Private Link support: Secure backend connectivity to APIM VNet Internal mode without public internet exposure
Global capabilities: Multi-POP network, future-proof for geographic expansion
WAF included: Managed OWASP rulesets for application security
Better for APIs: Optimized for HTTP/HTTPS routing, lower latency than App Gateway

Cost: £378/month (UK South) vs Application Gateway WAF v2 ~£350/month (similar cost, AFD offers more features)

Microsoft Docs: Azure Front Door Overview

Alternatives Rejected:

Application Gateway: No global capabilities, requires separate DDoS (£2,644/mo), less optimized for API workloads
Direct APIM exposure: Not secure, no DDoS protection layer
2. VNet Internal Mode (Not External)

Decision: Deploy all APIM instances in VNet Internal mode

Rationale:

Maximum security: No public IP exposure, gateway endpoints accessible only within VNet via internal load balancer
Zero-trust architecture: All external access via Front Door → Private Link → APIM internal endpoint (Azure backbone, no internet)
Simplified attack surface: Only Front Door is internet-facing (single point of defense)
Compliance: Meets data residency and security requirements (no data leaving Azure network)
Internal API security: Private APIs accessible only within VNet without separate APIM instance

Microsoft Guidance:

"Use the internal VNet mode when you want to expose your API Management instance only to clients within the VNet. This mode provides maximum security by ensuring the gateway and management endpoints are accessible only via private IPs." - APIM VNet Modes

Network Flow:

Internet User → Azure Front Door (WAF, DDoS)
    ↓ Private Link (Azure backbone, no internet)
APIM Internal Endpoint (10.1.1.4, no public IP)
    ↓ VNet connectivity
Backend APIs (within VNet or peered VNets)


Key Implications:

Gateway endpoint: 10.1.1.4 (internal IP only, not registered in public DNS)
Developer portal: Accessed via VNet or Front Door with Private Link
Management endpoint: Requires VPN/Bastion or Azure portal (no public access)
Private DNS zones: azure-api.net resolves to internal IP within VNet
Warning: Complexity: Requires proper VNet configuration, Private DNS setup, Private Link approval

External Mode Rejected:

Gateway has public IP (even if restricted by NSGs)
Larger attack surface
Cannot enforce 100% private traffic flow

Microsoft Docs: APIM VNet Integration

3. Separate APIM Instances per Environment (Not Workspaces)

Decision: Use 3 separate APIM instances for dev/test/prod, not workspaces within a single instance

Rationale:

Cost optimization: Developer tier for dev/test (£45/month) vs Premium shared cost (£648/workspace if conceptually split)
Blast radius isolation: Dev changes cannot impact production (separate compute, configuration, secrets, networking)
Independent scaling: Scale prod (3 units zone-redundant) separately from dev (1 unit)
Environment-specific configuration: Different backends, rate limits, policies, secrets per environment without risk of cross-contamination
Deployment safety: Test promotes confidence before prod (true replica environments, not logical separation)
Compliance: Some frameworks require physical separation of production from non-production

Microsoft Guidance:

"Workspaces provide logical isolation within a single API Management instance for organizing APIs, products, and subscriptions by team or project. They're ideal for multi-tenant scenarios within the same environment, but don't provide compute or infrastructure isolation." - APIM Workspaces

Cost Comparison:

Approach	Dev	Test	Prod	Total
Separate Instances (recommended)	£45	£45	£1,944	£2,034/mo
Workspaces in Single Premium	£648*	£648*	£648*	£1,944/mo

*Workspaces share same Premium instance cost (£1,944/month), lack infrastructure isolation

When to Use Workspaces:

Logical separation within an environment (e.g., Team A APIs vs Team B APIs in same prod APIM)
RBAC per workspace (Team A can't see Team B APIs)
NOT for dev/test/prod separation (no compute, network, or secret isolation)

Configuration:

Development:
- APIM: apim-api-marketplace-dev-uks (Developer tier, 1 unit)
- VNet: vnet-dev-uks (10.0.0.0/16)
- Cost: £45/month + supporting services (~£55) = ~£100/month total

Test:
- APIM: apim-api-marketplace-test-uks (Developer tier, 1 unit)
- VNet: vnet-test-uks (10.1.0.0/16)
- Cost: £45/month + supporting services (~£55) = ~£100/month total

Production:
- APIM: apim-api-marketplace-prod-uks (Premium tier, 3 units, zone-redundant)
- VNet: vnet-prod-uks (10.2.0.0/16)
- Cost: £1,944/month + Front Door £378 + monitoring £270 + API Center £135 + other = ~£3,230/month


Microsoft Docs: APIM Workspaces Overview

4. Hybrid Authentication (OAuth + Subscription Keys)

Decision: Use hybrid authentication strategy - OAuth 2.0 for sensitive/internal APIs, subscription keys for simple public APIs

Rationale:

Flexibility: Different API types have different security and UX needs
User experience: Public read-only APIs don't need complex OAuth flows (lower barrier to entry, faster onboarding)
Security: Sensitive data (PII, financial) protected by OAuth with proven user identity
Partner compatibility: Some B2B partners prefer traditional API keys over OAuth client credentials
Rate limiting options: Can limit per-user (OAuth sub claim) or per-subscription (shared keys)

Authentication Decision Matrix:

API Type	Auth Method	Justification	Example
Public Read-Only	Subscription Keys	Low security risk, easy onboarding, no PII	Weather API, Public Holidays
Internal Corporate	OAuth 2.0 (Entra ID)	User identity required, RBAC, audit trail	Employee Directory, HR Systems
Sensitive Public	OAuth 2.0 (Entra External ID B2C)	Handles PII/financial, user consent	Payment Processing, Health Records
Partner B2B	OAuth 2.0 Client Credentials	Machine-to-machine, mTLS optional	Order Management, Inventory Sync

Rate Limiting Strategy:

OAuth authenticated users: 1000 requests/hour per user (sub claim from JWT)
Subscription key users: 500 requests/hour per subscription (shared if multi-user app)
Rationale: OAuth users have proven identity (higher trust), subscription keys might be shared

Policy Implementation (abbreviated):

<choose>
    <when condition="@(context.Request.Headers.GetValueOrDefault('Authorization','').StartsWith('Bearer'))">
        <validate-jwt header-name="Authorization">
            <openid-config url="https://login.microsoftonline.com/{tenant}/v2.0/.well-known/openid-configuration" />
        </validate-jwt>
        <rate-limit-by-key calls="1000" renewal-period="3600" 
                           counter-key="@(context.Request.Headers.GetValueOrDefault('Authorization','').AsJwt()?.Subject)" />
    </when>
    <otherwise>
        <check-header name="Ocp-Apim-Subscription-Key" />
        <rate-limit-by-key calls="500" renewal-period="3600" 
                           counter-key="@(context.Subscription.Key)" />
    </otherwise>
</choose>


Microsoft Docs: Protect backend with Entra ID

5. Azure API Center Included

Decision: Deploy Azure API Center (Standard tier) at £135/month for centralized API governance

Rationale:

Multiple environments: Need visibility across dev/test/prod APIM instances (3 separate instances)
Scale: Expecting 50+ APIs at maturity across all environments
Governance: Centralized compliance checking, breaking change detection, API linting
Discovery: Developers need to find APIs across environments from single catalog
Cost: £135/month (4% of total prod budget) justified for governance value

Microsoft Guidance:

"Azure API Center enables organizations to develop and maintain a structured and standardized API inventory. API Center enables tracking all APIs in the organization, along with their versions, deployments, and dependencies." - API Center Overview

When API Center Adds Value:

50+ APIs: Manual tracking becomes unmanageable
Multiple teams: Different teams publishing APIs, need central registry
Multiple environments: 3 APIM instances (dev/test/prod) need unified view
Compliance requirements: Need audit trail of API changes, versions, owners
Breaking change detection: Auto-detect when API schemas change incompatibly

When You DON'T Need API Center:

<20 APIs: Manual tracking in spreadsheet is sufficient
Single team: Team knows all their APIs
No compliance requirements: No audit/governance needs

Key Features Used:

API Inventory: All APIs from dev/test/prod APIM instances registered
Metadata Management: Owner, domain, data classification per API
Compliance Checking: APIs tagged with frameworks (GDPR, PCI-DSS)
Version Tracking: All API versions visible (v1, v2, deprecated status)
Breaking Change Detection: Schema comparison between versions
API Linting: OpenAPI spec validation, naming convention enforcement

Cost: Standard tier £135/month UK South (includes unlimited APIs, compliance, linting)

Microsoft Docs: API Center Overview

6. UK South Single-Region

Decision: Deploy all resources in UK South only, no multi-region/DR to other regions

Rationale:

Data residency: UK data must stay in UK (regulatory requirement)
Simplicity: No cross-region replication complexity or latency
Cost optimization: Multi-region APIM Premium would be £1,944 × 2 = £3,888/month
Zone redundancy sufficient: APIM Premium with 3 units across 3 availability zones in UK South provides 99.99% SLA (4.38 minutes downtime/month)
Business requirement: All consumers in UK/Europe, low latency from UK South sufficient

High Availability Strategy (Single-Region):

APIM Premium: 3 units across 3 availability zones → 99.99% SLA
Azure Front Door: Multi-POP global network (but origin in UK South only)
Zone failure: Auto-failover within UK South zones (no manual intervention)
Backups: Geo-redundant storage (GRS) to UK West (disaster recovery)

When Multi-Region WOULD Be Needed:

Global user base (US, Asia) requiring <100ms latency globally
Business continuity requires < 1 hour RTO (single-region outage)
Compliance requires active-active across geographies
Traffic > 10,000 requests/second (need geo-distribution)

DR Strategy (Without Multi-Region Active-Active):

Backups: Nightly APIM backup to Storage (GRS to UK West)
IaC: All infrastructure in Bicep/Terraform (can redeploy to UK West in ~2 hours)
APIOps: All API configs in Git (restore from source control)
RTO/RPO: RTO 4 hours, RPO 24 hours (acceptable for business)

Cost Avoidance: Saves ~£2,100/month by staying single-region

Microsoft Docs: APIM High Availability

Total Cost Summary
All Environments (GBP UK South)
Environment	APIM Tier	Monthly Cost
Development	Developer	~£100
Test	Developer	~£100
Production	Premium (3u)	~£3,230
TOTAL		~£3,430/month (~£41,160/year)
Production Environment Breakdown (£3,230/month)
Component	Configuration	Monthly Cost
API Management (Premium)	3 units (zone-redundant)	£1,944
Azure Front Door (Premium)	100GB, 1M requests	£378
Microsoft Entra ID (P2)	100 users	£270
Entra External ID (B2C)	50k MAU	£0 (free tier)
Azure Monitor + App Insights	100GB logs	£270
Azure API Center	Standard	£135
VNet + Private Link	10 endpoints	£90
Key Vault + Misc		£143
Cost Optimization Decisions
Developer tier for dev/test: Saves £1,206/month vs Premium (93% savings)
No separate DDoS Standard: Front Door includes platform DDoS (saves £2,644/month)
Single region: No multi-region replication (saves £1,944/month)
Entra External ID: First 50k MAU free (saves £1,000+/month vs paid auth solution)

Total Architectural Savings: ~£5,850/month through design optimization

Steps to Apply This Skill
Step 1: Understand Current Architecture Question

Ask yourself:

Is user asking about component selection? (Front Door vs App Gateway, VNet mode, etc.)
Is user asking about cost? (How much will this cost?)
Is user asking for rationale? (Why did you choose X?)
Is user comparing alternatives? (Workspaces or separate instances?)
Step 2: Reference Knowledge Base

Match question to relevant section above:

Front Door vs App Gateway → Section 1
VNet Internal vs External → Section 2
Workspaces vs Instances → Section 3
OAuth vs Subscription Keys → Section 4
API Center justification → Section 5
Single-region strategy → Section 6
Cost breakdown → Total Cost Summary
Step 3: Structure Response

Format response with:

Decision or Recommendation (clear statement)
Rationale (3-5 bullet points)
Microsoft Documentation Link (with quote if applicable)
Cost Implications (in GBP UK South)
Alternatives Considered (with reasons for rejection)
Reference to Documentation (which document section for details)
Step 4: Cite Sources

Always reference:

Primary source: DESIGN_DECISIONS_REFERENCE.md (for "why" with alternatives)
Secondary source: ARCHITECTURE_DESIGN.md (for "how" with technical details)
Microsoft documentation: Official Azure docs with links
Step 5: Include Cost Context

When discussing any component, always mention:

Monthly cost in GBP for UK South region
How it fits into total budget (£3,430/month all environments)
Any cost optimization decisions made
Example Usage
Example 1: Component Selection

User: "Should I use Azure Front Door or Application Gateway?"

Response using this skill:

## Recommendation: Azure Front Door Premium

**Decision**: Use Azure Front Door Premium as ingress layer

**Rationale**:
- Built-in DDoS protection (platform-level, saves £2,644/month vs separate Azure DDoS Standard)
- Private Link support to APIM (secure backend connectivity without public internet)
- Global load balancing capabilities (future-proof for expansion)
- WAF with managed OWASP rulesets
- Better optimized for API workloads (lower latency)

**Cost Comparison**:
- Azure Front Door Premium: £378/month
- Application Gateway WAF v2: ~£350/month
- Similar cost, but AFD offers more features for API workloads

**Microsoft Documentation**:
[Azure Front Door Overview](https://learn.microsoft.com/azure/frontdoor/front-door-overview)

**Alternatives Considered**:
- Application Gateway: No global capabilities, requires separate DDoS (£2,644/mo), less suitable for API workloads
- Direct APIM exposure: Not secure, no DDoS layer

**Architecture Flow**:
Internet Users → Front Door (WAF, DDoS) → Private Link → APIM (VNet Internal) → Backends

**Documentation**: See DESIGN_DECISIONS_REFERENCE.md Section 1.1 for complete analysis

Example 2: Cost Inquiry

User: "What's the total cost for all three environments?"

Response using this skill:

## Total Cost: All Environments (GBP UK South)

| Environment | APIM Tier | Monthly Cost |
|-------------|-----------|--------------|
| Development | Developer | ~£100 |
| Test | Developer | ~£100 |
| Production | Premium (3u) | ~£3,230 |
| **TOTAL** | | **~£3,430/month** (~£41,160/year) |

### Production Environment Detail (£3,230/month)

APIM Premium (3u): £1,944  
Azure Front Door: £378  
Entra ID P2: £270  
Monitoring: £270  
API Center: £135  
VNet + Private Link: £90  
Misc: £143

### Cost Optimization Highlights

- Developer tier for dev/test: **Saves £1,206/month** (93% vs Premium)
- No separate DDoS: **Saves £2,644/month** (Front Door includes platform DDoS)
- Single region: **Saves £1,944/month** (no multi-region APIM)
- Entra External ID free tier: **Saves £1,000+/month** (vs paid auth solution)

**Total Architectural Savings**: ~£5,850/month through design optimization

**Documentation**: See ARCHITECTURE_DESIGN.md Section 9.1 for detailed cost breakdown

Related Skills
apim-policy-authoring - Use after architecture decisions to implement policies
api-security-review - Use to validate security of chosen architecture
apiops-deployment - Use to deploy the architecture with IaC
Microsoft Documentation Quick Links
APIM: https://learn.microsoft.com/azure/api-management/
VNet Internal: https://learn.microsoft.com/azure/api-management/api-management-using-with-vnet?tabs=stv2#virtual-network-modes
Front Door: https://learn.microsoft.com/azure/frontdoor/front-door-overview
Private Link: https://learn.microsoft.com/azure/frontdoor/private-link
API Center: https://learn.microsoft.com/azure/api-center/overview
Entra External ID: https://learn.microsoft.com/entra/external-id/customers/overview-customers-ciam
APIM Workspaces: https://learn.microsoft.com/azure/api-management/workspaces-overview
Well-Architected: https://learn.microsoft.com/azure/well-architected/service-guides/azure-api-management

Skill Version: 1.0
Last Updated: 29 January 2026
Primary Documents: DESIGN_DECISIONS_REFERENCE.md, ARCHITECTURE_DESIGN.md
Related MCP Tools: azure_documental search, azure_bestpractices

Weekly Installs
11
Repository
thomast1906/git…t-skills
GitHub Stars
162
First Seen
Mar 2, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass