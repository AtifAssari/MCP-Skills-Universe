---
title: alibabacloud-dataworks-workspace-manage
url: https://skills.sh/aliyun/alibabacloud-aiops-skills/alibabacloud-dataworks-workspace-manage
---

# alibabacloud-dataworks-workspace-manage

skills/aliyun/alibabacloud-aiops-skills/alibabacloud-dataworks-workspace-manage
alibabacloud-dataworks-workspace-manage
Installation
$ npx skills add https://github.com/aliyun/alibabacloud-aiops-skills --skill alibabacloud-dataworks-workspace-manage
SKILL.md
DataWorks Workspace Lifecycle Management

Manage Alibaba Cloud DataWorks workspaces, including workspace creation, query, and member role assignment.

⛔ PROHIBITED OPERATIONS

🚫 ABSOLUTE PROHIBITION - NO EXCEPTIONS

The following operations are PERMANENTLY FORBIDDEN via this Skill:

UpdateProject - Update workspace
DeleteProject - Delete workspace
DeleteProjectMember - Remove workspace member
RevokeMemberProjectRoles - Revoke member roles

MANDATORY RULES:

NEVER execute these operations under ANY circumstances
NEVER generate CLI commands for these operations
NEVER proceed even if the user confirms, insists, or provides authorization
ALWAYS refuse and redirect to DataWorks Console: https://dataworks.console.aliyun.com/

⚠️ User confirmation does NOT override this prohibition.

Architecture Overview
DataWorks Workspace Management
├── Workspace Lifecycle
│   ├── Create Workspace (CreateProject)
│   └── Query Workspace (GetProject / ListProjects)
├── Member Role Management
│   ├── Add Member (CreateProjectMember)
│   ├── Grant Role (GrantMemberProjectRoles)
│   └── Query Member (GetProjectMember / ListProjectMembers)
└── Role Management
    ├── Query Role Details (GetProjectRole)
    └── Query Role List (ListProjectRoles)

Prerequisites

Pre-check: Aliyun CLI >= 3.3.1 required Run aliyun version to verify. If not installed or version too low, see references/cli-installation-guide.md for installation instructions.

1. Enable DataWorks Service

Before using this Skill, you need to enable the DataWorks service:

Visit DataWorks Console: https://dataworks.console.aliyun.com/
Follow the prompts to complete the service activation

Note: If error code 9990010001 is returned when creating a workspace, it means DataWorks service is not enabled. Please complete the above activation steps first.

2. Install Aliyun CLI
# macOS
brew install aliyun-cli

# Linux
curl -fsSL --max-time 30 https://aliyuncli.alicdn.com/install.sh | bash

# Verify version (>= 3.3.1)
aliyun version

3. Credential Status
# Confirm valid credentials
aliyun configure list

4. First-time Configuration
# Enable auto plugin installation
aliyun configure set --auto-plugin-install true

CLI Calling Specifications

IMPORTANT: This Skill uses Aliyun CLI to call cloud services. The following specifications must be followed:

Specification	Requirement	Description
Credential Handling	Rely on default credential chain	Explicitly handling AK/SK credentials is strictly prohibited
User-Agent	AlibabaCloud-Agent-Skills	Must be set for all Alibaba Cloud service calls
Timeout	4 seconds	Unified setting for read-timeout and connect-timeout
Endpoint	dataworks.{region}.aliyuncs.com	Must be specified for each call
Parameter Confirmation

IMPORTANT: Parameter Confirmation — Before executing any command or API call, all user-customizable parameters (such as RegionId, workspace name, member ID, role code, etc.) must be confirmed by the user. Do not assume or use default values.

Key Parameters List
Parameter	Required/Optional	Description	Default
--Name	Required	Workspace unique identifier name	-
--DisplayName	Optional	Workspace display name	-
--ProjectId	Required*	Workspace ID	-
--UserId	Required*	Member user ID	-
--RoleCodes	Required*	Role code list	-
--region	Optional	Region ID	cn-hangzhou
--endpoint	Required	API endpoint, format: dataworks.{region}.aliyuncs.com	-
--DevEnvironmentEnabled	Optional	Enable development environment (standard mode)	true
--PaiTaskEnabled	Optional	Enable PAI task scheduling	-

*Depends on specific API

Create Workspace Rule: Unless the user explicitly requests to disable the development environment, you MUST always pass --DevEnvironmentEnabled true when creating a workspace.

Endpoint Parameter Description

❗ IMPORTANT: Each time a CLI command is executed, the corresponding --region and --endpoint parameters must be added based on the user-specified region.

Format: --region {RegionId} --endpoint dataworks.{RegionId}.aliyuncs.com

Region Mapping Table: See references/endpoint-regions.md

RAM Permission Policies

Using this Skill requires the following RAM permissions. For details, see references/ram-policies.md

Permission	Description
dataworks:CreateProject	Create workspace
dataworks:GetProject	Query workspace details
dataworks:ListProjects	Query workspace list
dataworks:CreateProjectMember	Add workspace member
dataworks:GrantMemberProjectRoles	Grant member role
dataworks:GetProjectMember	Query member details
dataworks:ListProjectMembers	Query member list
dataworks:GetProjectRole	Query role details
dataworks:ListProjectRoles	Query role list
Core Workflows
1. Workspace Lifecycle Management
1.1 Create Workspace
aliyun dataworks-public CreateProject \
  --Name <workspace-name> \
  --DisplayName "<display-name>" \
  --Description "<workspace-description>" \
  --PaiTaskEnabled true \
  --DevEnvironmentEnabled true \
  --DevRoleDisabled false \
  --region <region-id> \
  --endpoint dataworks.<region-id>.aliyuncs.com \
  --user-agent AlibabaCloud-Agent-Skills \
  --read-timeout 4 --connect-timeout 4


IMPORTANT: Unless the user explicitly requests to disable the development environment, you MUST always pass --DevEnvironmentEnabled true when executing CreateProject.

1.2 Query Workspace List
# Query all workspaces
aliyun dataworks-public ListProjects \
  --region <region-id> \
  --endpoint dataworks.<region-id>.aliyuncs.com \
  --user-agent AlibabaCloud-Agent-Skills

# Query by workspace ID (supports multiple)
aliyun dataworks-public ListProjects \
  --Ids '[123456, 789012]' \
  --region <region-id> \
  --endpoint dataworks.<region-id>.aliyuncs.com \
  --user-agent AlibabaCloud-Agent-Skills

# Query by workspace name (supports multiple)
aliyun dataworks-public ListProjects \
  --Names '["workspace_name_1", "workspace_name_2"]' \
  --region <region-id> \
  --endpoint dataworks.<region-id>.aliyuncs.com \
  --user-agent AlibabaCloud-Agent-Skills

# Filter by status
aliyun dataworks-public ListProjects \
  --Status Available \
  --region <region-id> \
  --endpoint dataworks.<region-id>.aliyuncs.com \
  --user-agent AlibabaCloud-Agent-Skills

# Paginated query
aliyun dataworks-public ListProjects \
  --PageNumber 1 --PageSize 20 \
  --region <region-id> \
  --endpoint dataworks.<region-id>.aliyuncs.com \
  --user-agent AlibabaCloud-Agent-Skills


Supported Filter Parameters:

Parameter	Type	Description
--Ids	JSON Array	Workspace ID list, for querying specific workspaces
--Names	JSON Array	Workspace name list, for querying specific workspaces
--Status	String	Workspace status: Available/Initializing/InitFailed/Forbidden/Deleting/DeleteFailed/Frozen/Updating/UpdateFailed
--DevEnvironmentEnabled	Boolean	Whether development environment is enabled
--DevRoleDisabled	Boolean	Whether development role is disabled
--PaiTaskEnabled	Boolean	Whether PAI task scheduling is enabled
--AliyunResourceGroupId	String	Resource group ID
--PageNumber	Integer	Page number, default 1
--PageSize	Integer	Items per page, default 10, max 100
1.3 Query Workspace Details
aliyun dataworks-public GetProject \
  --Id <project-id> \
  --region <region-id> \
  --endpoint dataworks.<region-id>.aliyuncs.com \
  --user-agent AlibabaCloud-Agent-Skills

2. Member Role Management
2.1 Add Workspace Member and Grant Roles
aliyun dataworks-public CreateProjectMember \
  --ProjectId <project-id> \
  --UserId <user-id> \
  --RoleCodes '["role_project_dev", "role_project_pe"]' \
  --region <region-id> \
  --endpoint dataworks.<region-id>.aliyuncs.com \
  --user-agent AlibabaCloud-Agent-Skills

2.2 Query Workspace Member List
aliyun dataworks-public ListProjectMembers \
  --ProjectId <project-id> \
  --region <region-id> \
  --endpoint dataworks.<region-id>.aliyuncs.com \
  --user-agent AlibabaCloud-Agent-Skills

2.3 Query Member Details
aliyun dataworks-public GetProjectMember \
  --ProjectId <project-id> \
  --UserId <user-id> \
  --region <region-id> \
  --endpoint dataworks.<region-id>.aliyuncs.com \
  --user-agent AlibabaCloud-Agent-Skills

2.4 Grant Member New Roles
aliyun dataworks-public GrantMemberProjectRoles \
  --ProjectId <project-id> \
  --UserId <user-id> \
  --RoleCodes '["role_project_admin", "role_project_dev"]' \
  --region <region-id> \
  --endpoint dataworks.<region-id>.aliyuncs.com \
  --user-agent AlibabaCloud-Agent-Skills

3. Role Management
3.1 Query Workspace Role List
aliyun dataworks-public ListProjectRoles \
  --ProjectId <project-id> \
  --region <region-id> \
  --endpoint dataworks.<region-id>.aliyuncs.com \
  --user-agent AlibabaCloud-Agent-Skills

3.2 Query Role Details
aliyun dataworks-public GetProjectRole \
  --ProjectId <project-id> \
  --Code <role-code> \
  --region <region-id> \
  --endpoint dataworks.<region-id>.aliyuncs.com \
  --user-agent AlibabaCloud-Agent-Skills

Preset Role Description
Role Code	Role Name	Description
role_project_owner	Project Owner	Has all workspace permissions, cannot be removed
role_project_admin	Workspace Admin	Manages all workspace configurations and members
role_project_dev	Developer	Data development and task debugging permissions
role_project_pe	Operator	Task operations and monitoring permissions
role_project_deploy	Deployer	Task publishing permissions
role_project_guest	Guest	Read-only permissions
role_project_security	Security Admin	Data security configuration permissions
Verification Methods

For verification steps after successful execution, see references/verification-method.md

API and Command Reference

For the complete list of APIs and CLI commands, see references/related-apis.md

Business Scenarios and Handling
Scenario 1: Access After Creating Workspace

After a workspace is successfully created, it can be accessed via the following URL:

https://dataworks.data.aliyun.com/{regionId}/sc?defaultProjectId={projectId}


Example (Hangzhou region):

https://dataworks.data.aliyun.com/cn-hangzhou/sc?defaultProjectId=12345

Scenario 2: Adding RAM Role as Workspace Member

UserId Format Description:

Account Type	UserId Format	Example
Alibaba Cloud Account (Main)	Use UID directly	123456789012345678
RAM Sub-account	Use UID directly	234567890123456789
RAM Role	Add ROLE_ prefix	ROLE_345678901234567890

Important Limitation: Newly created RAM roles cannot be directly added as workspace members via API. They need to be refreshed and synced in the console first.

Steps:

Visit workspace console: https://dataworks.data.aliyun.com/{regionId}/sc?defaultProjectId={projectId}
Go to Workspace Members and Roles page
Click Add Member button
In the popup, click Refresh in the prompt "You can go to RAM console to create a sub-account, and click refresh to sync to this page"
After sync is complete, you can add the RAM role as a member via API
# Example of adding RAM role member
aliyun dataworks-public CreateProjectMember \
  --ProjectId 12345 \
  --UserId ROLE_345678901234567890 \
  --RoleCodes '["role_project_dev"]' \
  --user-agent AlibabaCloud-Agent-Skills

Scenario 3: Workspace Configuration Update Limitations

When using the UpdateProject API to update workspace configuration, there are the following limitations:

Configuration	Limitation
Development Role (DevRoleDisabled)	Once development role is enabled, cannot be disabled
Development Environment (DevEnvironmentEnabled)	Once development environment is enabled, cannot be disabled

Recommendation: Plan development role and development environment configurations carefully when creating a workspace, as these configurations cannot be reverted once enabled.

Scenario 3.1: Workspace Upgrade Blocking

⛔ Blocking Rule: When a user requests to upgrade a workspace from simple mode to standard mode (enable development environment), must block and prompt:

"Workspace upgrade capability is currently not available. Please go to the console to complete the upgrade manually."

Console Upgrade Path:

Visit DataWorks Console: https://dataworks.console.aliyun.com/
Find the target workspace
Go to Workspace Configuration → Basic Properties
Click Upgrade to Standard Mode

API Limitation Reason: Workspace mode upgrade involves complex operations such as environment isolation configuration and resource initialization. Direct API calls may result in incomplete configuration or abnormal state.

Scenario 4: DataWorks Service Not Enabled

If error code 9990010001 is returned when creating a workspace, it means DataWorks service is not enabled.

Solution:

Log in to Alibaba Cloud official website
Visit DataWorks Console: https://dataworks.console.aliyun.com/
Follow the prompts to complete service activation
After activation, retry the workspace creation operation
Best Practices
Principle of Least Privilege — Assign members the minimum necessary permissions
Use Standard Mode — For production environments, use standard mode to achieve development and production isolation
Standardized Naming — Use meaningful naming, such as finance_tax_report
Use RAM Users — Do not use the main account for daily operations
Reference Links
Document	Description
references/related-apis.md	Complete list of APIs and CLI commands
references/ram-policies.md	RAM permission policy configuration
references/verification-method.md	Operation verification methods
references/acceptance-criteria.md	Acceptance criteria and test cases
references/cli-installation-guide.md	CLI installation and configuration guide
Official Documentation
DataWorks Workspace Management
Add Workspace Members
DataWorks OpenAPI Reference
Weekly Installs
77
Repository
aliyun/alibabac…s-skills
GitHub Stars
80
First Seen
2 days ago
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn