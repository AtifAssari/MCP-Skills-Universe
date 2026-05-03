---
title: alibabacloud-rds-copilot
url: https://skills.sh/aliyun/alibabacloud-aiops-skills/alibabacloud-rds-copilot
---

# alibabacloud-rds-copilot

skills/aliyun/alibabacloud-aiops-skills/alibabacloud-rds-copilot
alibabacloud-rds-copilot
Installation
$ npx skills add https://github.com/aliyun/alibabacloud-aiops-skills --skill alibabacloud-rds-copilot
SKILL.md
Alibaba Cloud RDS Copilot Intelligent Operations Assistant

This skill serves as an intelligent agent for Alibaba Cloud RDS Copilot in conversations, helping users with RDS-related intelligent Q&A, SQL optimization, instance operations, and troubleshooting.

Scenario Description

Architecture: Alibaba Cloud CLI + RdsAi OpenAPI

Main features:

Understand user's natural language requests (Chinese or English), identify if related to RDS Copilot
Directly call Alibaba Cloud CLI to execute aliyun rdsai chat-messages command for real-time RDS Copilot queries
When receiving results or user-pasted error messages, further explain, diagnose, and provide recommendations
Installation

Pre-check: Alibaba Cloud CLI must be installed

This skill uses Alibaba Cloud CLI to call RdsAi OpenAPI. You need to install and configure Alibaba Cloud CLI first.

Pre-check: Aliyun CLI >= 3.3.3 required

Run aliyun version to verify >= 3.3.3. If not installed or version too low, run curl -fsSL https://aliyuncli.alicdn.com/setup.sh | bash to update, or see references/cli-installation-guide.md for installation instructions.

Pre-check: Aliyun CLI plugin update required

[MUST] run aliyun configure set --auto-plugin-install true to enable automatic plugin installation. [MUST] run aliyun plugin update to ensure that any existing plugins are always up-to-date.

[MUST] CLI User-Agent — Every aliyun CLI command invocation must include: --user-agent AlibabaCloud-Agent-Skills/alibabacloud-rds-copilot

macOS Installation
# Option 1: Install via Homebrew (recommended)
brew install aliyun-cli

# Option 2: Install via PKG package
curl -O https://aliyuncli.alicdn.com/aliyun-cli-latest.pkg
sudo installer -pkg aliyun-cli-latest.pkg -target /

# Option 3: Install via one-click script
/bin/bash -c "$(curl -fsSL https://aliyuncli.alicdn.com/install.sh)"

Linux Installation
# Install via one-click script
/bin/bash -c "$(curl -fsSL https://aliyuncli.alicdn.com/install.sh)"

# Or download TGZ package for manual installation
curl https://aliyuncli.alicdn.com/aliyun-cli-linux-latest-amd64.tgz -o aliyun-cli.tgz
tar xzvf aliyun-cli.tgz
sudo mv aliyun /usr/local/bin/

Verify Installation
aliyun version

Credential Configuration
Option 1: Interactive Configuration (Recommended)
aliyun configure --profile rdsai


Follow the prompts to enter:

Access Key Id: Your AccessKey ID
Access Key Secret: Your AccessKey Secret
Default Region Id: cn-hangzhou (or other regions)
Option 2: Non-interactive Configuration
aliyun configure set \
  --profile rdsai \
  --mode AK \
  --access-key-id <yourAccessKeyID> \
  --access-key-secret <yourAccessKeySecret> \
  --region cn-hangzhou

Command Format
Basic Command Structure
aliyun rdsai chat-messages \
  --query '<query content>' \
  --inputs RegionId=<region ID> Language=<language> Timezone=<timezone> [CustomAgentId=<custom agent ID>] \
  --event-mode separate \
  --endpoint rdsai.aliyuncs.com \
  --user-agent 'AlibabaCloud-Agent-Skills/alibabacloud-rds-copilot' \
  [--conversation-id '<conversation ID>']

Parameter Description

IMPORTANT: Parameter Confirmation — Before executing any command, Determine user intent: SQL writing/optimization, SQL diagnosis, instance parameter tuning, troubleshooting, performance analysis, query instance list, etc. Collect necessary parameters (use default values if not specified).

Parameter	Required/Optional	Description	Default
--query	Required	User query content	-
--inputs RegionId=	Optional	Alibaba Cloud region ID	cn-hangzhou
--inputs Language=	Optional	Language	zh-CN
--inputs Timezone=	Optional	Timezone	Asia/Shanghai
--inputs CustomAgentId=	Optional	Custom Agent ID	None
--event-mode	Optional	Event mode	separate
--endpoint	Required	API endpoint	rdsai.aliyuncs.com
--conversation-id	Optional	Conversation ID for multi-turn dialogue	None
--region	Optional	Region for API call	Credential default region
--profile	Optional	Specify credential profile name	Default profile
--user-agent	Required	Custom User-Agent	AlibabaCloud-Agent-Skills/alibabacloud-rds-copilot
RAM Permissions

This skill requires the following RAM permissions. See references/ram-policies.md for details.

Permission	Description
rdsai:ChatMessages	Call RDS AI Assistant API
Core Workflow
0. Enable AI-Mode (Before Executing Any CLI Command)

Before executing any aliyun CLI command, you must enable AI-Mode and set the User-Agent:

# [MUST] Enable AI-Mode before any CLI command execution
aliyun configure ai-mode enable

# [MUST] Set User-Agent for AI-Mode
aliyun configure ai-mode set-user-agent --user-agent "AlibabaCloud-Agent-Skills/alibabacloud-rds-copilot"

1. Confirm Task Type and Parameters

Determine user intent: SQL writing/optimization, SQL diagnosis, instance parameter tuning, troubleshooting, performance analysis, query instance list, etc.

Collect necessary parameters (use default values if not specified):

RegionId: Region ID (default cn-hangzhou)
Language: Language (default zh-CN)
Timezone: Timezone (default Asia/Shanghai)
CustomAgentId: Custom Agent ID (optional)
--conversation-id: Conversation ID for multi-turn dialogue (optional)
2. Construct Command and Call CLI
# Basic query
aliyun rdsai chat-messages \
  --query 'List RDS MySQL instances in Hangzhou region' \
  --inputs RegionId=cn-hangzhou Language=zh-CN Timezone=Asia/Shanghai \
  --event-mode separate \
  --endpoint rdsai.aliyuncs.com \
  --user-agent 'AlibabaCloud-Agent-Skills/alibabacloud-rds-copilot'

# Troubleshooting example
aliyun rdsai chat-messages \
  --query 'RDS instance rm-bp1xxx connection timeout, error Too many connections, please help troubleshoot. Instance is in Hangzhou region.' \
  --inputs RegionId=cn-hangzhou Language=zh-CN Timezone=Asia/Shanghai \
  --event-mode separate \
  --endpoint rdsai.aliyuncs.com \
  --user-agent 'AlibabaCloud-Agent-Skills/alibabacloud-rds-copilot'

# Query with Beijing region
aliyun rdsai chat-messages \
  --query 'Optimize this SQL: SELECT * FROM users WHERE name LIKE "%test%"' \
  --inputs RegionId=cn-beijing Language=zh-CN Timezone=Asia/Shanghai \
  --event-mode separate \
  --endpoint rdsai.aliyuncs.com \
  --user-agent 'AlibabaCloud-Agent-Skills/alibabacloud-rds-copilot'

# Multi-turn dialogue (using ConversationId from previous response)
aliyun rdsai chat-messages \
  --query 'Continue analyzing the above issue' \
  --conversation-id '<ConversationId from previous response>' \
  --inputs RegionId=cn-hangzhou Language=zh-CN Timezone=Asia/Shanghai \
  --event-mode separate \
  --endpoint rdsai.aliyuncs.com \
  --user-agent 'AlibabaCloud-Agent-Skills/alibabacloud-rds-copilot'

# Using custom Agent
aliyun rdsai chat-messages \
  --query 'Analyze database performance' \
  --inputs RegionId=cn-hangzhou Language=zh-CN Timezone=Asia/Shanghai CustomAgentId=your-custom-agent-id \
  --event-mode separate \
  --endpoint rdsai.aliyuncs.com \
  --user-agent 'AlibabaCloud-Agent-Skills/alibabacloud-rds-copilot'

3. Parse Results and Follow-up Processing
Explain RDS Copilot's response to the user in natural language
If the response contains SQL or operational steps, assess risks and warn:
Avoid executing high-risk statements directly in production (e.g., large table DELETE / UPDATE / schema changes)
Recommend validating in test environment or adding backup/condition restrictions
If continuing the conversation, record the ConversationId from the response for the next query
4. Disable AI-Mode (After Workflow Ends)

After the workflow is complete, you must disable AI-Mode:

# [MUST] Disable AI-Mode after workflow ends
aliyun configure ai-mode disable

Output Format

Alibaba Cloud CLI returns JSON format responses (streaming multiple JSON events):

{"data":{"ConversationId":"8227be22-xxxx-xxxx-xxxx-xxxxxxxxxxxx","Event":"workflow_started","MessageId":"a79c881c-xxxx-xxxx-xxxx-xxxxxxxxxxxx",...}}
{"data":{"Answer":"<partial answer content>","Event":"message",...}}
{"data":{"Event":"workflow_finished",...}}


Key fields:

ConversationId: Conversation ID (for multi-turn dialogue)
Answer: AI assistant's response content
Event: Event type (workflow_started, message, workflow_finished)
Success Verification
CLI installation successful: aliyun version shows version number
Credential configured correctly: aliyun configure list shows configured credentials
API call successful: Response contains ConversationId and Answer in JSON format
Response content valid: Answer is relevant to the query content

See references/verification-method.md for detailed verification steps.

Cleanup

This skill only performs read-only query operations, does not create any cloud resources, no cleanup required.

API and Command List

See references/related-apis.md for details.

Product	API Action	CLI Command	Description
RdsAi	ChatMessages	aliyun rdsai chat-messages	RDS AI Assistant dialogue API
Best Practices
Use multi-turn dialogue: For complex issues, use --conversation-id for context-aware multi-turn conversations
Specify correct region: Set RegionId parameter based on the RDS instance's region
Be cautious in production: SQL recommendations from RDS Copilot should be validated in test environment first
Save conversation ID: Save the returned ConversationId if you need to follow up or continue analysis
Use configuration file: Recommend using aliyun configure to configure credentials, avoid exposing sensitive information in command line
Use --profile: You can configure multiple credential profiles and switch between accounts using --profile
Reference Links
Reference Document	Description
Alibaba Cloud CLI Documentation	Alibaba Cloud CLI User Guide
references/related-apis.md	API and Command List
references/ram-policies.md	RAM Policy Configuration
references/verification-method.md	Verification Methods
references/acceptance-criteria.md	Acceptance Criteria
Weekly Installs
119
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