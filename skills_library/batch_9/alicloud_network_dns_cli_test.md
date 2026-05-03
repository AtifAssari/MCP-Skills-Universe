---
title: alicloud-network-dns-cli-test
url: https://skills.sh/cinience/alicloud-skills/alicloud-network-dns-cli-test
---

# alicloud-network-dns-cli-test

skills/cinience/alicloud-skills/alicloud-network-dns-cli-test
alicloud-network-dns-cli-test
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill alicloud-network-dns-cli-test
SKILL.md

Category: test

DNS CLI Minimal Viable Test
Prerequisites
aliyun CLI is installed and configured.
AK/SK is configured.
GoalsSkill: skills/network/dns/alicloud-network-dns-cli/。
Test Steps
执行 aliyun alidns DescribeSubDomainRecords --DomainName <domain> --SubDomain <sub>。
若无记录，再执行一次空返回验证。
记录 request id 和返回条目数。
Expected Results
命令可执行，返回 JSON 或明确权限错误。
Weekly Installs
292
Repository
cinience/alicloud-skills
GitHub Stars
383
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass