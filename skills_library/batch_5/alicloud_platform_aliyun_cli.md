---
title: alicloud-platform-aliyun-cli
url: https://skills.sh/cinience/alicloud-skills/alicloud-platform-aliyun-cli
---

# alicloud-platform-aliyun-cli

skills/cinience/alicloud-skills/alicloud-platform-aliyun-cli
alicloud-platform-aliyun-cli
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill alicloud-platform-aliyun-cli
SKILL.md

Category: tool

Alibaba Cloud Generic CLI (aliyun) Skill
Validation
mkdir -p output/alicloud-platform-aliyun-cli
python skills/platform/cli/alicloud-platform-aliyun-cli/scripts/ensure_aliyun_cli.py --help > output/alicloud-platform-aliyun-cli/validate-help.txt


Pass criteria: command exits 0 and output/alicloud-platform-aliyun-cli/validate-help.txt is generated.

Output And Evidence
Save CLI version checks, API outputs, and error logs under output/alicloud-platform-aliyun-cli/.
For each mutating action, keep request parameters and result summaries.
Goals
Use official aliyun CLI to execute Alibaba Cloud OpenAPI operations.
Provide a standard flow for install, configuration, API discovery, execution, and troubleshooting.
Quick Flow
Run the version guard script first (check first, then decide whether to upgrade).
If not installed or check interval reached, the script downloads and installs the latest official package.
Configure credentials and default region (recommend default profile).
Use aliyun <product> --help / aliyun <product> <ApiName> --help to confirm parameters.
Run read-only queries first, then mutating operations.
Version Guard (Practical)

Prefer the bundled script to avoid unnecessary downloads on every run:

python skills/platform/cli/alicloud-platform-aliyun-cli/scripts/ensure_aliyun_cli.py


Default behavior:

Check interval: 24 hours (configurable via environment variable).
Within interval and version is sufficient: skip download.
Exceeded interval / not installed / below minimum version: auto-download and install latest official package.

Optional controls (environment variables):

ALIYUN_CLI_CHECK_INTERVAL_HOURS=24：check interval.
ALIYUN_CLI_FORCE_UPDATE=1：force update (ignore interval).
ALIYUN_CLI_MIN_VERSION=3.2.9：minimum acceptable version.
ALIYUN_CLI_INSTALL_DIR=~/.local/bin：installation directory.

Manual parameter examples:

python skills/platform/cli/alicloud-platform-aliyun-cli/scripts/ensure_aliyun_cli.py \
  --interval-hours 24 \
  --min-version 3.2.9

Install (Linux example)
curl -fsSL https://aliyuncli.alicdn.com/aliyun-cli-linux-latest-amd64.tgz -o /tmp/aliyun-cli.tgz
mkdir -p ~/.local/bin
tar -xzf /tmp/aliyun-cli.tgz -C /tmp
mv /tmp/aliyun ~/.local/bin/aliyun
chmod +x ~/.local/bin/aliyun
~/.local/bin/aliyun version

Configure Credentials
aliyun configure set \
  --profile default \
  --mode AK \
  --access-key-id <AK> \
  --access-key-secret <SK> \
  --region cn-hangzhou


View configured profiles:

aliyun configure list

Command structure
Generic form:aliyun <product> <ApiName> --Param1 value1 --Param2 value2
REST form:aliyun <product> [GET|POST|PUT|DELETE] <PathPattern> --body '...json...'
API Discovery and Parameter Validation
aliyun help
aliyun ecs --help
aliyun ecs DescribeRegions --help

Common Read-Only Examples
# ECS: list regions
aliyun ecs DescribeRegions

# ECS: list instances by region
aliyun ecs DescribeInstances --RegionId cn-hangzhou

# SLS: list projects by endpoint
aliyun sls ListProject --endpoint cn-hangzhou.log.aliyuncs.com --size 100

Common Issues
InvalidAccessKeyId.NotFound / SignatureDoesNotMatch：check AK/SK and profile.
MissingRegionId：add --region or configure default region in profile.
for SLS endpoint errors, explicitly pass --endpoint <region>.log.aliyuncs.com.
Execution Recommendations
Run ensure_aliyun_cli.py before starting tasks.
If resource scope is unclear, query first then mutate.
Before delete/overwrite operations, output the target resource list first.
For batch operations, validate one item in a small scope first.
References
Official source list:references/sources.md
Prerequisites
Configure least-privilege Alibaba Cloud credentials before execution.
Prefer environment variables: ALICLOUD_ACCESS_KEY_ID, ALICLOUD_ACCESS_KEY_SECRET, optional ALICLOUD_REGION_ID.
If region is unclear, ask the user before running mutating operations.
Workflow
Confirm user intent, region, identifiers, and whether the operation is read-only or mutating.
Run one minimal read-only query first to verify connectivity and permissions.
Execute the target operation with explicit parameters and bounded scope.
Verify results and save output/evidence files.
Weekly Installs
278
Repository
cinience/alicloud-skills
GitHub Stars
383
First Seen
Mar 2, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail