---
title: alicloud-security-kms-test
url: https://skills.sh/cinience/alicloud-skills/alicloud-security-kms-test
---

# alicloud-security-kms-test

skills/cinience/alicloud-skills/alicloud-security-kms-test
alicloud-security-kms-test
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill alicloud-security-kms-test
SKILL.md

Category: test

KMS Minimal Viable Test
Prerequisites
AK/SK and region are configured.
GoalsSkill: skills/security/key-management/alicloud-security-kms/。
Test Steps
通过 OpenAPI 元数据确认 KMS 常用读取 API。
执行一个只读查询（如 ListKeys 或产品支持的等价读接口）。
记录 request id、返回数量、错误码（若有）。
Expected Results
只读查询成功或返回明确权限错误。
Weekly Installs
295
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