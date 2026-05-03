---
rating: ⭐⭐
title: alicloud-storage-oss-ossutil-test
url: https://skills.sh/cinience/alicloud-skills/alicloud-storage-oss-ossutil-test
---

# alicloud-storage-oss-ossutil-test

skills/cinience/alicloud-skills/alicloud-storage-oss-ossutil-test
alicloud-storage-oss-ossutil-test
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill alicloud-storage-oss-ossutil-test
SKILL.md

Category: test

OSSUTIL 2.0 Minimal Viable Test
Goals
验证 AK/Region 配置正确。
验证 OSS 访问（列桶、上传、下载）。
Prerequisites
已配置 AK（推荐环境变量或 ~/.alibabacloud/credentials）。
已准备一个可读写的 OSS Bucket。
Test Steps (Minimal)
查看配置
ossutil config get region

列出 Bucket
ossutil ls

选择一个 bucket，按该 bucket 地域列对象（显式 region + endpoint）
# 示例（按实际 bucket 地域替换）
ossutil ls oss://<bucket> -r --short-format --region cn-shanghai -e https://oss-cn-shanghai.aliyuncs.com --limited-num 20

上传小文件
echo "ossutil-test" > /tmp/ossutil-test.txt
ossutil cp /tmp/ossutil-test.txt oss://<bucket>/tests/ossutil-test.txt --region cn-shanghai -e https://oss-cn-shanghai.aliyuncs.com

下载并校验
ossutil cp oss://<bucket>/tests/ossutil-test.txt /tmp/ossutil-test-down.txt --region cn-shanghai -e https://oss-cn-shanghai.aliyuncs.com
cat /tmp/ossutil-test-down.txt

Expected Results
ossutil ls 能返回至少一个 bucket 或无权限说明。
指定 --region + -e 后，列对象可正常返回。
上传/下载成功，文件内容一致。
常见失败
Region 不匹配：确认 ALIBABACLOUD_REGION_ID 或配置文件中的 region。
AK 无权限：确认 RAM 策略允许 oss:* 或最小读写权限。
Weekly Installs
297
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