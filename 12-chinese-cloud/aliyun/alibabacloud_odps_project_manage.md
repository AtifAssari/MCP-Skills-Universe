---
title: alibabacloud-odps-project-manage
url: https://skills.sh/aliyun/alibabacloud-aiops-skills/alibabacloud-odps-project-manage
---

# alibabacloud-odps-project-manage

skills/aliyun/alibabacloud-aiops-skills/alibabacloud-odps-project-manage
alibabacloud-odps-project-manage
Installation
$ npx skills add https://github.com/aliyun/alibabacloud-aiops-skills --skill alibabacloud-odps-project-manage
SKILL.md
MaxCompute Project Management

Manage Alibaba Cloud MaxCompute (ODPS) Projects including creation, querying, and listing operations.

Prerequisites

Pre-check: Aliyun CLI >= 3.3.3 required

Run aliyun version to verify >= 3.3.3. If not installed or version too low, run curl -fsSL https://aliyuncli.alicdn.com/setup.sh | bash to update, or see references/cli-installation-guide.md for installation instructions.

Then [MUST] run aliyun plugin update to ensure that any existing plugins on your local machine are always up-to-date.

[MUST] CLI User-Agent — Every aliyun CLI command invocation must include: --user-agent AlibabaCloud-Agent-Skills/alibabacloud-odps-project-manage

[MUST] AI-Mode Commands — When using aliyun CLI, declare AI-Mode lifecycle:

Enable AI-Mode before commands:
aliyun configure ai-mode enable

Set User-Agent for AI-Mode:
aliyun configure ai-mode set-user-agent --user-agent "AlibabaCloud-Agent-Skills/alibabacloud-odps-project-manage"

Disable AI-Mode after workflow ends:
aliyun configure ai-mode disable

Quick Start

When user asks about MaxCompute projects, follow these steps:

Identify intent: create / list / get
Get RegionId: Ask user which region (e.g., cn-hangzhou, cn-shanghai)
Execute: Run the appropriate command with --region {REGION_ID} and --user-agent AlibabaCloud-Agent-Skills/alibabacloud-odps-project-manage
Verify: Confirm the result and report to user
Pre-flight Checklist (Execute BEFORE every command)

You MUST verify ALL of these before running any command:

 I have asked the user for RegionId (not using default)
 I have the actual RegionId value from user (not placeholder)
 My command includes --region {ACTUAL_REGION_ID}
 My command includes --user-agent AlibabaCloud-Agent-Skills/alibabacloud-odps-project-manage
 I am NOT reading or echoing any AK/SK values
 I am NOT using hardcoded values for user-provided parameters

If ANY check fails, STOP and fix before proceeding.

Task Completion Checklist

CRITICAL: You MUST complete ALL steps in order. Do NOT stop early.

For LIST Projects:
 Ask user: "Which region would you like to query? (e.g., cn-hangzhou, cn-shanghai)"
 Ask user: "Which quota nickname to filter by? (e.g., os_PayAsYouGoQuota, or press Enter for default)"
 MUST use quota-nick-name parameter:
If user specified a quota: Use --quota-nick-name={USER_QUOTA}
If user didn't specify: Use --quota-nick-name=os_PayAsYouGo
 Execute with REQUIRED parameters:
aliyun maxcompute list-projects --region {REGION_ID} --quota-nick-name={QUOTA_NICKNAME} --max-item=20 --user-agent AlibabaCloud-Agent-Skills/alibabacloud-odps-project-manage

 Wait for command output
 If 400 error (quota not found):
Call aliyun maxcompute list-quotas --billing-type ALL --region {REGION_ID} --user-agent AlibabaCloud-Agent-Skills/alibabacloud-odps-project-manage
Present available quotas to user for selection
Re-run list-projects with user-selected quota
 Parse response and present results
 Confirm task completion

FORBIDDEN:

❌ Use --marker for pagination
❌ Fetch all projects then filter locally with Python/jq
❌ Call API without --quota-nick-name parameter

REQUIRED:

✅ ALWAYS use --quota-nick-name with user's quota or default
✅ ALWAYS use --max-item=20
✅ Let API do server-side filtering
For GET Project:
 Ask user: "Which region? (e.g., cn-hangzhou)"
 Ask user: "What is the project name?"
 Execute: aliyun maxcompute get-project --region {REGION_ID} --project-name {PROJECT_NAME} --user-agent AlibabaCloud-Agent-Skills/alibabacloud-odps-project-manage
 Wait for command output
 Parse the JSON response - look for data.name, data.status, data.owner
 Present project details to user in a clear format
 Confirm task completion to user
For CREATE Project:
 Ask user: "Which region to create in? (e.g., cn-hangzhou)"
 Ask user: "What is the project name?"
 MANDATORY VALIDATION: If project name is empty or whitespace, STOP and ask user again: "Project name cannot be empty. Please provide a valid project name."
 CRITICAL: Store the user's exact project name - do NOT use placeholder text
 MUST call list-quotas: Execute: aliyun maxcompute list-quotas --billing-type ALL --region {REGION_ID} --user-agent AlibabaCloud-Agent-Skills/alibabacloud-odps-project-manage
 Wait for command output
 Parse list-quotas response: Find a quota with nickName and its secondary quotas (look in data.quotas[].subQuotas or similar)
 STRICT VALIDATION: Select a secondary quota's nickName from the list-quotas response (NOT the primary quota)
 TRIM WHITESPACE: Remove any leading/trailing spaces from the quota nickName. If nickName contains internal spaces, trim them or select a different quota
 PRE-FLIGHT CHECK: Verify you have actual values for REGION_ID, PROJECT_NAME, and SECONDARY_QUOTA_NICKNAME (trimmed, no spaces)
 Ask for typeSystem (optional): "Which typeSystem? (1=MaxCompute, 2=MaxCompute2, hive=Hive compatible; default: 2)"
 Validate typeSystem: Must be "1", "2", or "hive". If not specified or invalid, use default "2"
 Execute create command with ACTUAL values:
aliyun maxcompute create-project --region {ACTUAL_REGION} --body '{"name":"ACTUAL_PROJECT_NAME","defaultQuota":"SECONDARY_QUOTA_NICKNAME","productType":"payasyougo","typeSystem":"TYPE_SYSTEM_VALUE"}' --user-agent AlibabaCloud-Agent-Skills/alibabacloud-odps-project-manage

Example with real values:
aliyun maxcompute create-project --region cn-hangzhou --body '{"name":"my-project-123","defaultQuota":"os_PayAsYouGoQuota_sub","productType":"payasyougo","typeSystem":"2"}' --user-agent AlibabaCloud-Agent-Skills/alibabacloud-odps-project-manage

 Wait for command output
 CHECK CREATE RESPONSE: If create command returned error (non-2xx), STOP and report error to user. Do NOT proceed to verification.
 ONLY IF create succeeded: Verify by executing: aliyun maxcompute get-project --region {REGION_ID} --project-name {PROJECT_NAME} --user-agent AlibabaCloud-Agent-Skills/alibabacloud-odps-project-manage
 CRITICAL: Verify the response contains the CORRECT project name (the one user requested, not a different project)
 CHECK STATUS: Verify response contains "status":"AVAILABLE"
 If verification returns 403/Access Denied: Inform user about permission requirements and stop
 If project not found: Report "Project creation failed - project not found after creation"
 If wrong project returned: Report error - do not use a different project as substitute
 ONLY IF all checks pass: Confirm to user: "Project {PROJECT_NAME} created successfully with status AVAILABLE"
If User Requests Deletion:

Respond: "Project deletion is not supported by this skill. Please use the Alibaba Cloud Console or contact your administrator."

Common Errors & Solutions
Error	Cause	Solution
ProjectNotFound	Project doesn't exist	Check project name spelling and region
ProjectAlreadyExist	Name taken	Ask user for a different project name
get project default quota error	No valid quota	Run list-quotas first, ensure quota exists
InvalidProjectName	Bad naming format	Use only lowercase, numbers, underscores (3-28 chars)
NoPermission or 403 Access Denied	RAM permission issue	Inform user: "You need odps permissions for list-quotas, create-project and get-project. Please contact your administrator."
RegionId required	Missing --region	Always add --region {REGION_ID} to commands
ODPS-0420095: Access Denied	Missing read privilege	Inform user about required permissions and stop
Forbidden Actions

CRITICAL: Never do these:

NEVER read/echo AK/SK values (e.g., echo $ALIBABA_CLOUD_ACCESS_KEY_ID)
NEVER use hardcoded values — always ask user for parameters, then use their ACTUAL answer (not placeholder text)
NEVER use aliyun configure set with literal credential values
NEVER run aliyun ram commands
NEVER execute ANY command without --user-agent AlibabaCloud-Agent-Skills/alibabacloud-odps-project-manage
NEVER skip asking for RegionId — this is ALWAYS required
NEVER assume a default region — always ask the user
NEVER use uppercase API action format as CLI commands — ALWAYS use plugin format with lowercase and hyphens (e.g., create-project)
NEVER execute aliyun maxcompute delete-project — project deletion is NOT supported by this skill
Negative Examples
❌ WRONG	✅ CORRECT
Using uppercase API action names as CLI commands	aliyun maxcompute create-project (plugin format, lowercase with hyphens)
'{"name":"{PROJECT_NAME}"}' (placeholder)	'{"name":"actual-name"}' (actual value)
--region cn-hangzhou (hardcoded)	Ask user first, then use their answer
Missing --user-agent	Must include --user-agent AlibabaCloud-Agent-Skills/alibabacloud-odps-project-manage
echo $ALIBABA_CLOUD_ACCESS_KEY_ID	Never read/display credentials
aliyun ram ... commands	RAM commands are outside scope
aliyun maxcompute delete-project	Project deletion is NOT supported
Verify different project on failure	Report failure, don't substitute
Architecture
MaxCompute Service
    └── Project (Workspace)
          ├── defaultQuota (Compute Resource - MUST exist before project creation)
          ├── productType (payasyougo/subscription)
          └── typeSystem ("1", "2", or "hive"; default: "2")

Dependencies

Prerequisite: Quota must exist before creating a project.

Every MaxCompute project requires a compute quota (defaultQuota). The quota must already exist in your account — if it does not, the create-project call will fail with get project default quota error.

Use the alibabacloud-odps-quota-manage skill to create or query quotas:

Pay-as-you-go: aliyun maxcompute create-quota --charge-type payasyougo --commodity-code odps --region <region> --user-agent AlibabaCloud-Agent-Skills/alibabacloud-odps-project-manage
Subscription: See alibabacloud-odps-quota-manage skill for full parameters (partNickName, CU, ord_time, etc.)
List existing quotas: aliyun maxcompute list-quotas --billing-type ALL --region <region> --user-agent AlibabaCloud-Agent-Skills/alibabacloud-odps-project-manage

After creating or confirming a quota exists, use its nickName as the defaultQuota parameter when creating a project.

Installation

Pre-check: Aliyun CLI >= 3.3.3 required

Run aliyun version to verify >= 3.3.3. If not installed or version too low, run curl -fsSL https://aliyuncli.alicdn.com/setup.sh | bash to update, or see references/cli-installation-guide.md for installation instructions.

Pre-check: Aliyun CLI plugin update required

[MUST] run aliyun configure set --auto-plugin-install true to enable automatic plugin installation. [MUST] run aliyun plugin update to ensure that any existing plugins are always up-to-date.

# Install/Update Alibaba Cloud CLI
curl -fsSL https://aliyuncli.alicdn.com/setup.sh | bash

# Verify version (must be >= 3.3.3)
aliyun version

# Enable auto plugin installation
aliyun configure set --auto-plugin-install true

# Update plugins
aliyun plugin update

Environment Variables

No additional environment variables required beyond standard Alibaba Cloud credentials.

Authentication

CRITICAL: You MUST check credentials before ANY operation.

Allowed Credential Check (ONLY this command):
aliyun configure list


What to look for:

Output shows at least one profile with mode: AK or mode: StsToken
Profile shows access_key_id: ******** (masked is OK)

If NO valid profile:

Tell user: "Please run aliyun configure to set up credentials first."
STOP - Do not proceed with any MaxCompute commands

FORBIDDEN - NEVER do these:

❌ echo $ALIBABA_CLOUD_ACCESS_KEY_ID
❌ echo $ALIBABA_CLOUD_ACCESS_KEY_SECRET
❌ aliyun configure get | grep access-key
❌ Any command that displays actual credential values
RAM Policy

[MUST] RAM Permission Pre-check: Before executing the workflow, verify that the current user has the required permissions.

Required permissions are listed in references/ram-policies.md.

Note: You do NOT need to verify RAM permissions via CLI commands. The permissions listed in ram-policies.md are for user reference only. Proceed with the workflow assuming the user has configured appropriate permissions.

Parameters

Always ask user for these values — never assume defaults:

Parameter	Required	Description
RegionId	Yes	Region ID (cn-hangzhou, cn-shanghai, etc.)
projectName	Yes	Project name
quotaNickName	For create	Quota alias (get from list-quotas)
Example Conversation

LIST: User asks → Agent requests RegionId → Agent executes list-projects → Agent presents results

CREATE: User asks → Agent requests RegionId → Agent requests projectName → Agent calls list-quotas → Agent creates project → Agent verifies → Agent confirms success

Commands
List Projects
# Ask user for quota nickname first, then:
aliyun maxcompute list-projects --region {REGION_ID} --quota-nick-name={QUOTA_NICKNAME} --max-item=20 --user-agent AlibabaCloud-Agent-Skills/alibabacloud-odps-project-manage


MUST: Always use --quota-nick-name parameter (user-specified or default). Never fetch all and filter locally.

Get Project
aliyun maxcompute get-project --region {REGION_ID} --project-name {PROJECT_NAME} --user-agent AlibabaCloud-Agent-Skills/alibabacloud-odps-project-manage

Create Project
List quotas first:
aliyun maxcompute list-quotas --billing-type ALL --region {REGION_ID} --user-agent AlibabaCloud-Agent-Skills/alibabacloud-odps-project-manage

Create with quota nickName from response:
aliyun maxcompute create-project --region {REGION_ID} --body '{"name":"{PROJECT_NAME}","defaultQuota":"{QUOTA_NICKNAME}","productType":"payasyougo"}' --user-agent AlibabaCloud-Agent-Skills/alibabacloud-odps-project-manage

Success Verification Method

See references/verification-method.md for detailed verification steps.

Verification Command:

aliyun maxcompute get-project --region {REGION_ID} --project-name {PROJECT_NAME} --user-agent AlibabaCloud-Agent-Skills/alibabacloud-odps-project-manage


Success Criteria:

Response contains "status":"AVAILABLE"
Response contains correct "name" matching the created project
Response contains correct "defaultQuota" matching the specified quota

If verification fails:

Check error message for specific issue
Report failure reason to user
Suggest corrective action based on error type
Limitations

The following operations cannot be performed via CLI/API and require Console access:

Operation	Reason	Alternative
View billing details	Requires Console access	Use Billing Console
Manage IAM policies visually	Console-only feature	Use RAM CLI for policy management
Real-time resource monitoring	Requires Console dashboard	Use CloudMonitor APIs
API and Command Tables

See references/related-apis.md for complete API reference.

Operation	CLI Command (plugin mode)	API Action Name
Create Project	aliyun maxcompute create-project	create-project
Get Project	aliyun maxcompute get-project	get-project
List Projects	aliyun maxcompute list-projects	list-projects
List Quotas	aliyun maxcompute list-quotas	list-quotas
Skill Completion Criteria (REQUIRED for skill_pass)

For skill_pass_rate to be successful, ALL of these MUST be true:

Universal Requirements (ALL operations):
✅ User was asked for RegionId and provided an answer
✅ ALL commands used --region {USER_PROVIDED_VALUE} (not hardcoded)
✅ ALL commands included --user-agent AlibabaCloud-Agent-Skills/alibabacloud-odps-project-manage
✅ No forbidden actions were performed (no credential echoing, no ram commands)
✅ Task result was reported to user clearly
Operation-Specific Requirements:

LIST:

Command executed: aliyun maxcompute list-projects --region {REGION} --quota-nick-name=os_PayAsYouGo --max-item=20 --user-agent AlibabaCloud-Agent-Skills/alibabacloud-odps-project-manage
MUST include --quota-nick-name=os_PayAsYouGo parameter for first attempt
MUST include --max-item=20 parameter
If first attempt fails with 400 error, retry with --quota-nick-name=os_PayAsYouGoQuota
Results presented to user (list of projects or "no projects found")

GET:

Command executed: aliyun maxcompute get-project --region {REGION} --project-name {NAME} --user-agent AlibabaCloud-Agent-Skills/alibabacloud-odps-project-manage
Project details presented to user

CREATE:

User was asked for RegionId and projectName (actual values obtained)

Quota was listed first: aliyun maxcompute list-quotas --billing-type ALL --region {REGION} --user-agent AlibabaCloud-Agent-Skills/alibabacloud-odps-project-manage

MUST use actual values in body - NOT placeholders like {PROJECT_NAME}

Create command format: --body '{"name":"ACTUAL_NAME","defaultQuota":"ACTUAL_QUOTA","productType":"payasyougo"}'

MUST check create response for errors before proceeding

Verification command executed: aliyun maxcompute get-project --region {REGION} --project-name {NAME} --user-agent AlibabaCloud-Agent-Skills/alibabacloud-odps-project-manage

MUST verify the project name in response matches the requested project

MUST verify status is AVAILABLE

If verification fails due to permissions (403), inform user and stop

If project not found or wrong project returned, report failure

If verification succeeds (status=AVAILABLE), confirm success to user

If user requests deletion, inform them to use Alibaba Cloud Console

Final Skill Pass Check:
Before responding to user, verify:
□ I followed the correct workflow for the operation type
□ I asked for ALL required parameters from user
□ I used user's actual values in commands (not placeholders or defaults)
□ I included --user-agent AlibabaCloud-Agent-Skills/alibabacloud-odps-project-manage in EVERY command
□ I did NOT perform any forbidden actions
□ I reported the final result to user

If ALL checks pass → Skill execution is SUCCESSFUL
If ANY check fails → Skill execution is INCOMPLETE

Final Verification (Before Marking Task Complete)

You MUST verify ALL of these before telling user the task is done:

For LIST:
 I asked for RegionId and got user's answer
 I executed list-projects with --region {USER_ANSWER} and --user-agent AlibabaCloud-Agent-Skills/alibabacloud-odps-project-manage
 I presented the results to user clearly
For GET:
 I asked for RegionId and got user's answer
 I asked for projectName and got user's answer
 I executed get-project with user's values and --user-agent AlibabaCloud-Agent-Skills/alibabacloud-odps-project-manage
 I presented project details to user clearly
For CREATE:
 I asked for RegionId and got user's answer
 I asked for projectName and got user's answer
 I executed list-quotas to get a valid quota
 I executed create-project with user's values and --user-agent AlibabaCloud-Agent-Skills/alibabacloud-odps-project-manage
 I verified creation by calling get-project
 I confirmed success to user
For DELETE:
 Inform user that deletion is not supported and suggest using Alibaba Cloud Console

If ANY check fails, the task is NOT complete.

Best Practices
Naming Convention: Use lowercase letters, numbers, and underscores for project names
Quota Selection: Choose appropriate quota based on workload requirements
Product Type: Use payasyougo for development/testing, subscription for production with predictable workloads
Type System: Use 2 (MaxCompute) for new projects unless Hive compatibility is required
Resource Cleanup: Always clean up test projects to avoid unnecessary costs
Reference Links
Document	Description
references/related-apis.md	Complete API reference
references/ram-policies.md	Required RAM permissions
references/verification-method.md	Verification steps
references/cli-installation-guide.md	CLI installation guide
MaxCompute Product Page	Official product documentation
create-project API	API reference
get-project API	API reference
list-projects API	API reference
Weekly Installs
157
Repository
aliyun/alibabac…s-skills
GitHub Stars
80
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn