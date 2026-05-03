---
rating: ⭐⭐
title: windows-infra-admin
url: https://skills.sh/404kidwiz/claude-supercode-skills/windows-infra-admin
---

# windows-infra-admin

skills/404kidwiz/claude-supercode-skills/windows-infra-admin
windows-infra-admin
Installation
$ npx skills add https://github.com/404kidwiz/claude-supercode-skills --skill windows-infra-admin
SKILL.md
Windows Infrastructure Admin
Purpose

Provides Windows Server and enterprise administration expertise specializing in Active Directory, Hybrid Identity, and PowerShell automation. Manages enterprise Windows environments with Group Policy, Intune, and comprehensive infrastructure administration.

When to Use
Designing or troubleshooting Active Directory topology (Forests, Domains, Sites)
Implementing Group Policy Objects (GPO) for security hardening (CIS Benchmarks)
Automating administrative tasks with PowerShell (User creation, Reporting)
Configuring Hybrid Identity (Azure AD Connect / Cloud Sync)
Managing Windows Server roles (DNS, DHCP, IIS, NPS, WSUS)
Deploying endpoints via Intune / Autopilot
Disaster Recovery planning for AD (Forest Recovery)
Examples
Example 1: AD Migration to Hybrid Identity

Scenario: Migrating on-premises AD to hybrid identity with Azure AD.

Implementation:

Designed Azure AD Connect sync topology
Implemented password hash synchronization
Configured seamless single sign-on
Set up conditional access policies
Created hybrid join certificates

Results:

Seamless authentication for cloud apps
99% reduction in password-related support tickets
Improved security posture with MFA
Foundation for Microsoft 365 migration
Example 2: GPO Security Hardening

Scenario: Hardening Windows endpoints to CIS Benchmarks.

Implementation:

Analyzed current GPO landscape
Created security baseline GPO
Implemented password policies (NIST guidelines)
Configured firewall and BitLocker policies
Set up audit logging

Results:

95% compliance with CIS Benchmarks
Security incidents reduced by 70%
Passed external security audit
Clear audit trail for compliance
Example 3: Intune Enrollment Automation

Scenario: Automating Windows device onboarding for remote workforce.

Implementation:

Configured Autopilot for zero-touch deployment
Created enrollment status screen policies
Imployed configuration profiles for security settings
Set up conditional access policies
Created self-service BitLocker recovery

Results:

Devices ready for use within 30 minutes
80% reduction in IT support calls
Consistent security configuration across devices
Improved user satisfaction
Best Practices
Active Directory
Health Monitoring: Regular dcdiag and repadmin checks
Backup: Daily system state backups with tested restores
Least Privilege: Separate admin from regular accounts
Cleanup: Regular stale object removal
Group Policy
Testing: Always test GPO in pilot first
Documentation: Document GPO purpose and settings
Security: Use security filtering appropriately
Review: Annual GPO review and cleanup
PowerShell Automation
Error Handling: Comprehensive try/catch/finally
Modules: Create reusable modules
Logging: Log all automation activities
Testing: Test scripts before production use
Security
Patching: Rapid patch deployment (within 30 days)
MFA: Enforce MFA for all admin access
Auditing: Enable advanced audit logging
LAPS: Use for local administrator passwords
Hybrid Identity
Sync Health: Monitor Azure AD Connect
Conditional Access: Enforce policies for cloud access
Password Protection: Enable banned password lists
Access Reviews: Regular access reviews

Do NOT invoke when:

Troubleshooting physical hardware failure → Use network-engineer (if network) or vendor support
Managing Linux servers → Use linux-admin (if available) or devops-engineer
Developing .NET applications → Use csharp-developer
Configuring cloud-native Azure resources (VMs, VNets) → Use azure-infra-engineer
Core Capabilities
Active Directory Management
Managing AD forests, domains, and trusts
Implementing user and group lifecycle management
Configuring organizational units and delegation
Troubleshooting authentication and replication issues
Group Policy Administration
Creating and managing GPOs for security settings
Implementing security baselines and CIS benchmarks
Troubleshooting policy application issues
Managing policy preferences and filtering
PowerShell Automation
Writing PowerShell scripts for administration
Automating user provisioning and reporting
Managing Active Directory with modules
Implementing error handling and logging
Hybrid Identity
Configuring Entra ID Connect for synchronization
Managing hybrid identity scenarios
Implementing conditional access policies
Managing device enrollment with Intune
Workflow 2: Hybrid Identity Setup (Entra ID Connect)

Goal: Sync on-prem users to Azure AD for Office 365 access.

Steps:

Prerequisites

Clean up AD (IdFix tool).
Verified domain in Azure portal.

Install Azure AD Connect

Select Password Hash Sync (PHS) (Most robust).
Enable SSO (Single Sign-On).

Filtering

Filter by OU (Sync only User_OU, exclude Admin_OU and Service_Accounts).

Verification

Check Synchronization Service Manager.
Verify user appears in Azure Portal as "Directory Synced: Yes".
4. Patterns & Templates
Pattern 1: Tiered Administration (Security)

Use case: Preventing credential theft (Pass-the-Hash).

Tier 0 (Identity): Domain Admins. Can only log into DCs. (Red Card/Token).
Tier 1 (Servers): Server Admins. Can log into Application Servers.
Tier 2 (Workstations): Helpdesk. Can log into Workstations.
Rule: Lower tiers CANNOT log into higher tier assets.
Pattern 2: DFS Namespaces (File Sharing)

Use case: Abstracting file server names.

Bad: Mapping \\Server01\Share. If Server01 dies, links break.
Good: Mapping \\corp.com\Data\Share.
\\corp.com\Data is the DFS Namespace.
It points to \\Server01\Share (Target).
Migration to \\Server02 is invisible to users.
Pattern 3: JEA (Just Enough Administration)

Use case: Allowing Helpdesk to reset passwords without being Domain Admins.

# Role Capability File (.psrc)
VisibleCmdlets = @{
    'Set-ADAccountPassword' = @{ Parameters = @{ Name = 'Identity' } }
    'Unlock-ADAccount' = @{ Parameters = @{ Name = 'Identity' } }
}

6. Integration Patterns
azure-infra-engineer:
Handoff: Windows Admin manages on-prem AD → Azure Engineer sets up Entra ID Connect.
Collaboration: Extending AD to Azure via VPN (IaaS DCs).
Tools: Azure Active Directory.
security-auditor:
Handoff: Auditor requests "User Access Review" → Windows Admin runs PowerShell report on Group Membership.
Collaboration: Enforcing Password Policies and MFA.
Tools: AD Audit Plus, Splunk.
network-engineer:
Handoff: Network Engineer sets up VLANs → Windows Admin configures DHCP Scopes/IP Helpers.
Collaboration: DNS resolution (Split-brain DNS).
Tools: IPAM.
Weekly Installs
139
Repository
404kidwiz/claud…e-skills
GitHub Stars
76
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn