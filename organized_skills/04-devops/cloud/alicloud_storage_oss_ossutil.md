---
rating: ⭐⭐
title: alicloud-storage-oss-ossutil
url: https://skills.sh/cinience/alicloud-skills/alicloud-storage-oss-ossutil
---

# alicloud-storage-oss-ossutil

skills/cinience/alicloud-skills/alicloud-storage-oss-ossutil
alicloud-storage-oss-ossutil
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill alicloud-storage-oss-ossutil
SKILL.md

Category: tool

OSS (ossutil 2.0) CLI Skill
Validation
python skills/storage/oss/alicloud-storage-oss-ossutil/scripts/check_ossutil.py --output output/alicloud-storage-oss-ossutil/validate.txt


Pass criteria: command exits 0 and output/alicloud-storage-oss-ossutil/validate.txt is generated.

Output And Evidence
Save command outputs, object listings, and sync logs under output/alicloud-storage-oss-ossutil/.
Keep at least one upload or listing result as evidence.
Goals
Use ossutil 2.0 to manage OSS: upload, download, sync, and resource management.
Provide a unified CLI flow for install, config, credentials, and region/endpoint handling.
Quick Start Flow
Install ossutil 2.0.
Configure AK/SK and default region (ossutil config or config file).
Run ossutil ls to list buckets, then list objects using the bucket region.
Execute upload/download/sync or API-level commands.
Install ossutil 2.0
See references/install.md for platform-specific install steps.
Configure ossutil
Interactive configuration:
ossutil config

Default config file paths:
Linux/macOS：~/.ossutilconfig
Windows：C:\Users\issuser\.ossutilconfig

Main configuration fields include:

AccessKey ID
AccessKey Secret
Region（example default cn-hangzhou; ask the user if the best region is unclear）
Endpoint（optional; auto-derived from region if omitted）
AccessKey configuration notes

Use RAM users/roles with least privilege and avoid passing AK in plain text on command line.

Recommended method (environment variables):

export ALICLOUD_ACCESS_KEY_ID="<your-ak>"
export ALICLOUD_ACCESS_KEY_SECRET="<your-sk>"
export ALICLOUD_REGION_ID="cn-beijing"


ALICLOUD_REGION_ID can be used as default region; if unset choose the most reasonable region, ask user if unclear.

Or use the standard shared credentials file:

~/.alibabacloud/credentials

[default]
type = access_key
access_key_id = <your-ak>
access_key_secret = <your-sk>

Command structure (2.0)
High-level command example:ossutil config
API-level command example:ossutil api put-bucket-acl
Common command examples
ossutil ls
ossutil ls oss://your-bucket -r --short-format --region cn-shanghai -e https://oss-cn-shanghai.aliyuncs.com
ossutil cp ./local.txt oss://your-bucket/path/local.txt
ossutil cp oss://your-bucket/path/remote.txt ./remote.txt
ossutil sync ./local-dir oss://your-bucket/path/ --delete

Recommended execution flow (list buckets first, then objects)
List all buckets
ossutil ls


Get target bucket region from output (e.g. oss-cn-shanghai) and convert it to --region format (cn-shanghai).

When listing objects, explicitly set --region and -e to avoid cross-region signature/endpoint errors.

ossutil ls oss://your-bucket \
  -r --short-format \
  --region cn-shanghai \
  -e https://oss-cn-shanghai.aliyuncs.com

For very large buckets, limit output size first.
ossutil ls oss://your-bucket --limited-num 100
ossutil ls oss://your-bucket/some-prefix/ -r --short-format --region cn-shanghai -e https://oss-cn-shanghai.aliyuncs.com

Common errors and handling

Error: region must be set in sign version 4.

Cause: missing region configuration.
Fix: add region in config file, or pass --region cn-xxx.

The bucket you are attempting to access must be addressed using the specified endpoint

Cause: request endpoint does not match bucket region.
Fix: use endpoint of the bucket region, e.g. -e https://oss-cn-hongkong.aliyuncs.com.

Invalid signing region in Authorization header

Cause: signature region does not match bucket region.
Fix: correct both --region and -e; both must match bucket region.
Credential and security guidance
Prefer RAM user AK for access control.
CLI options can override config file, but passing secrets on command line has leakage risk.
In production, manage secrets via config files or environment variables.
Clarifying questions (ask when uncertain)
Is your target a Bucket or an Object?
Do you need upload/download/sync, or management actions like ACL/lifecycle/CORS?
What are the target region and endpoint?
Are you accessing OSS from ECS in the same region (intranet endpoint may be preferred)?
References

OSSUTIL 2.0 overview and install/config:

https://help.aliyun.com/zh/oss/developer-reference/ossutil-overview

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
283
Repository
cinience/alicloud-skills
GitHub Stars
383
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass