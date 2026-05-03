---
title: alicloud-observability-sls-log-query-test
url: https://skills.sh/cinience/alicloud-skills/alicloud-observability-sls-log-query-test
---

# alicloud-observability-sls-log-query-test

skills/cinience/alicloud-skills/alicloud-observability-sls-log-query-test
alicloud-observability-sls-log-query-test
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill alicloud-observability-sls-log-query-test
SKILL.md

Category: test

SLS 日志查询Minimal Viable Test
Prerequisites
配置 ALIBABACLOUD_ACCESS_KEY_ID、ALIBABACLOUD_ACCESS_KEY_SECRET。
配置 SLS_ENDPOINT、SLS_PROJECT、SLS_LOGSTORE。
GoalsSkill: skills/observability/sls/alicloud-observability-sls-log-query/。
Test Steps
执行 5 分钟窗口的基础查询（如 * | select count(*)）。
记录耗时与返回行数。
若失败，记录完整错误码。
Expected Results
查询成功返回统计结果，或返回可诊断错误。
Weekly Installs
294
Repository
cinience/alicloud-skills
GitHub Stars
383
First Seen
8 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass