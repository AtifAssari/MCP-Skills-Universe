---
title: ms365-tenant-manager
url: https://skills.sh/questnova502/claude-skills-sync/ms365-tenant-manager
---

# ms365-tenant-manager

skills/questnova502/claude-skills-sync/ms365-tenant-manager
ms365-tenant-manager
Installation
$ npx skills add https://github.com/questnova502/claude-skills-sync --skill ms365-tenant-manager
SKILL.md
Microsoft 365 Tenant Manager

This skill provides expert guidance and automation for Microsoft 365 Global Administrators managing tenant setup, configuration, user lifecycle, security policies, and organizational optimization.

Capabilities
Tenant Setup & Configuration: Initial tenant setup, domain configuration, DNS records, service provisioning
User & Group Management: User lifecycle (create, modify, disable, delete), group creation, license assignment
Security & Compliance: Conditional Access policies, MFA setup, DLP policies, retention policies, security baselines
SharePoint & OneDrive: Site provisioning, permissions management, storage quotas, sharing policies
Teams Administration: Team creation, policy management, guest access, compliance settings
Exchange Online: Mailbox management, distribution groups, mail flow rules, anti-spam/malware policies
License Management: License allocation, optimization, cost analysis, usage reporting
Reporting & Auditing: Activity reports, audit logs, compliance reporting, usage analytics
Automation Scripts: PowerShell script generation for bulk operations and recurring tasks
Best Practices: Microsoft recommended configurations, security hardening, governance frameworks
Input Requirements

Tenant management tasks require:

Action type: setup, configure, create, modify, delete, report, audit
Resource details: User info, group names, policy settings, service configurations
Organizational context: Company size, industry, compliance requirements (GDPR, HIPAA, etc.)
Current state: Existing configurations, licenses, user count
Desired outcome: Specific goals, requirements, or changes needed

Formats accepted:

Text descriptions of administrative tasks
JSON with structured configuration data
CSV for bulk user/group operations
Existing PowerShell scripts to review or modify
Output Formats

Results include:

Step-by-step instructions: Detailed guidance for manual configuration via Admin Center
PowerShell scripts: Ready-to-use scripts for automation (with safety checks)
Configuration recommendations: Security and governance best practices
Validation checklists: Pre/post-implementation verification steps
Documentation: Markdown documentation of changes and configurations
Rollback procedures: Instructions to undo changes if needed
Compliance reports: Security posture and compliance status
How to Use

"Set up a new Microsoft 365 tenant for a 50-person company with security best practices" "Create a PowerShell script to provision 100 users from a CSV file with appropriate licenses" "Configure Conditional Access policy requiring MFA for all admin accounts" "Generate a report of all inactive users in the past 90 days" "Set up Teams policies for external collaboration with security controls"

Scripts
tenant_setup.py: Initial tenant configuration and service provisioning automation
user_management.py: User lifecycle operations and bulk provisioning
security_policies.py: Security policy configuration and compliance checks
reporting.py: Analytics, audit logs, and compliance reporting
powershell_generator.py: Generates PowerShell scripts for Microsoft Graph API and admin modules
Best Practices
Tenant Setup
Enable MFA first - Before adding users, enforce multi-factor authentication
Configure named locations - Define trusted IP ranges for Conditional Access
Set up privileged access - Use separate admin accounts, enable PIM (Privileged Identity Management)
Domain verification - Add and verify custom domains before bulk user creation
Baseline security - Apply Microsoft Secure Score recommendations immediately
User Management
License assignment - Use group-based licensing for scalability
Naming conventions - Establish consistent user principal names (UPNs) and display names
Lifecycle management - Implement automated onboarding/offboarding workflows
Guest access - Enable only when necessary, set expiration policies
Shared mailboxes - Use for department emails instead of assigning licenses
Security & Compliance
Zero Trust approach - Verify explicitly, use least privilege access, assume breach
Conditional Access - Start with report-only mode, then enforce gradually
Data Loss Prevention - Define sensitive information types, test policies before enforcement
Retention policies - Balance compliance requirements with storage costs
Regular audits - Review permissions, licenses, and security settings quarterly
SharePoint & Teams
Site provisioning - Use templates and governance policies
External sharing - Restrict to specific domains, require authentication
Storage management - Set quotas, enable auto-cleanup of old content
Teams templates - Create standardized team structures for consistency
Guest lifecycle - Set expiration and regular recertification
PowerShell Automation
Use Microsoft Graph - Prefer Graph API over legacy MSOnline modules
Error handling - Include try/catch blocks and validation checks
Dry-run mode - Test scripts with -WhatIf before executing
Logging - Capture all operations for audit trails
Credential management - Use Azure Key Vault or managed identities, never hardcode
Common Tasks
Initial Tenant Setup
Configure company branding
Add and verify custom domains
Set up DNS records (MX, SPF, DKIM, DMARC)
Enable required services (Teams, SharePoint, Exchange)
Create organizational structure (departments, locations)
Set default user settings and policies
User Onboarding
Create user accounts (single or bulk)
Assign appropriate licenses
Add to security and distribution groups
Configure mailbox and OneDrive
Set up multi-factor authentication
Provision Teams access
Security Hardening
Enable Security Defaults or Conditional Access
Configure MFA enforcement
Set up admin role assignments
Enable audit logging
Configure anti-phishing policies
Set up DLP and retention policies
Reporting & Monitoring
Active users and license utilization
Security incidents and alerts
Mailbox usage and storage
SharePoint site activity
Teams usage and adoption
Compliance and audit logs
Limitations
Permissions required: Global Administrator or specific role-based permissions
API rate limits: Microsoft Graph API has throttling limits for bulk operations
License dependencies: Some features require specific license tiers (E3, E5)
Delegation constraints: Some tasks cannot be delegated to service principals
Regional variations: Compliance features may vary by geographic region
Hybrid scenarios: On-premises Active Directory integration requires additional configuration
Third-party integrations: External apps may require separate authentication and permissions
PowerShell prerequisites: Requires appropriate modules installed (Microsoft.Graph, ExchangeOnlineManagement, etc.)
Security Considerations
Authentication
Never store credentials in scripts or configuration files
Use Azure Key Vault for credential management
Implement certificate-based authentication for automation
Enable Conditional Access for admin accounts
Use Privileged Identity Management (PIM) for JIT access
Authorization
Follow principle of least privilege
Use custom admin roles instead of Global Admin when possible
Regularly review and audit admin role assignments
Enable PIM for temporary elevated access
Separate user accounts from admin accounts
Compliance
Enable audit logging for all activities
Retain logs according to compliance requirements
Configure data residency for regulated industries
Implement information barriers where needed
Regular compliance assessments and reporting
PowerShell Modules Required

To execute generated scripts, ensure these modules are installed:

Microsoft.Graph (recommended, modern Graph API)
ExchangeOnlineManagement (Exchange Online management)
MicrosoftTeams (Teams administration)
SharePointPnPPowerShellOnline (SharePoint management)
AzureAD or AzureADPreview (Azure AD management - being deprecated)
MSOnline (Legacy, being deprecated - avoid when possible)
Updates & Maintenance
Microsoft 365 features and APIs evolve rapidly
Review Microsoft 365 Roadmap regularly for upcoming changes
Test scripts in non-production tenant before production deployment
Subscribe to Microsoft 365 Admin Center message center for updates
Keep PowerShell modules updated to latest versions
Regular security baseline reviews (quarterly recommended)
Helpful Resources
Microsoft 365 Admin Center: https://admin.microsoft.com
Microsoft Graph Explorer: https://developer.microsoft.com/graph/graph-explorer
PowerShell Gallery: https://www.powershellgallery.com
Microsoft Secure Score: Security posture assessment in Admin Center
Microsoft 365 Compliance Center: https://compliance.microsoft.com
Azure AD Conditional Access: Identity and access management policies
Weekly Installs
10
Repository
questnova502/cl…lls-sync
GitHub Stars
3
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass