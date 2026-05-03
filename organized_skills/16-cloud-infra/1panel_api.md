---
rating: ⭐⭐⭐
title: 1panel-api
url: https://skills.sh/breadbot86/1panel-skills/1panel-api
---

# 1panel-api

skills/breadbot86/1panel-skills/1panel-api
1panel-api
Installation
$ npx skills add https://github.com/breadbot86/1panel-skills --skill 1panel-api
SKILL.md
1Panel API Skills

🎯 一键管理你的 1Panel 服务器

快速开始
首次配置

首次使用本 Skill 时，请提供以下信息：

信息	说明	示例
1Panel 地址	服务器 IP 或域名 + 端口	http://192.168.1.100:8888
API Key	在面板「设置」→「API 密钥」中生成	你的密钥
获取 API Key
登录 1Panel 面板
进入「设置」→「API 密钥」
点击「创建」生成新密钥
复制生成的密钥
功能模块
模块	说明
Apps	应用商店、已安装应用管理
Websites	网站创建、配置、反向代理、SSL
Containers	Docker 容器管理
Databases	MySQL、PostgreSQL、Redis、MongoDB
Files	文件上传、下载、压缩、解压
Backups	备份与恢复
Cronjobs	定时任务
Runtimes	PHP、Node、Python、Go、Java 运行环境
Hosts	主机监控、防火墙、SSH、磁盘管理
Settings	系统配置、用户管理
认证方式
# Token 计算方式
api_key="你的API密钥"
timestamp=$(date +%s)
token=$(echo -n "1panel${api_key}${timestamp}" | openssl md5 | awk '{print $2}')

# 请求示例
curl -X GET "http://你的地址:8888/api/v2/containers/list" \
  -H "1Panel-Token: $token" \
  -H "1Panel-Timestamp: $timestamp" \
  -H "Content-Type: application/json"

了解更多
📖 完整 API 文档：见 docs 目录
❓ 常见问题：见 README.md
🔧 1Panel 官网：https://1panel.cn/
Weekly Installs
33
Repository
breadbot86/1panel-skills
GitHub Stars
6
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail