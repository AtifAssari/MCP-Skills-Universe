---
title: alicloud-platform-aliyun-cli-test
url: https://skills.sh/cinience/alicloud-skills/alicloud-platform-aliyun-cli-test
---

# alicloud-platform-aliyun-cli-test

skills/cinience/alicloud-skills/alicloud-platform-aliyun-cli-test
alicloud-platform-aliyun-cli-test
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill alicloud-platform-aliyun-cli-test
SKILL.md

Category: test

通用 aliyun CLI Minimal Viable Test
Prerequisites
aliyun CLI is installed.
A valid profile is configured (default default).
GoalsSkill: skills/platform/cli/alicloud-platform-aliyun-cli/。
Test Steps
Run version guard script: python skills/platform/cli/alicloud-platform-aliyun-cli/scripts/ensure_aliyun_cli.py --interval-hours 24。
执行 aliyun version。
执行 aliyun configure list。
Run one read-only API (example): aliyun ecs DescribeRegions。
Expected Results
CLI executes and returns version information.
configure list shows valid credential/profile info (or explicit missing hints).
Read-only API returns JSON (or explicit permission error).
Weekly Installs
240
Repository
cinience/alicloud-skills
GitHub Stars
383
First Seen
Mar 2, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass