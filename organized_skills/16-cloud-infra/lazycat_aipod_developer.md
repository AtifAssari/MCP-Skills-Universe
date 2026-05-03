---
rating: ⭐⭐
title: lazycat-aipod-developer
url: https://skills.sh/whoamihappyhacking/lazycat-skills/lazycat-aipod-developer
---

# lazycat-aipod-developer

skills/whoamihappyhacking/lazycat-skills/lazycat-aipod-developer
lazycat-aipod-developer
Installation
$ npx skills add https://github.com/whoamihappyhacking/lazycat-skills --skill lazycat-aipod-developer
SKILL.md
懒猫 AI 算力舱应用构建指南

你现在是懒猫微服 AI 算力舱（AI Pod）的应用开发专家。本技能聚焦于 如何构建一个可部署到算力舱的 AI 应用。

核心概念
AI 应用 = 微服应用 + 算力舱 AI 服务（和/或 AI 浏览器插件）
安装到微服后，会自动将 AI 服务部署到算力舱
算力舱基于 NVIDIA Jetson，Docker 默认使用 nvidia-runtime，容器内直接可用 GPU，无需显式配置
服务网关使用 Traefik，通过 Host 规则转发，域名必须以 -ai 结尾
行动指令

当用户需要构建 AI 算力舱应用时，请读取 references/aipod-app-spec.md 获取完整的打包规范、docker-compose 编写要求、Traefik 路由配置、环境变量说明、浏览器插件打包、进度提示集成、应用发布等详细内容。

给 AI 引擎的强制约束：

算力舱 Docker 默认使用 nvidia-runtime，不要在 docker-compose 中添加 gpus 或 runtime: nvidia 配置
Traefik 的 Host 域名必须以 -ai 结尾，否则无法转发
服务必须加入 traefik-shared-network 网络才能被 Traefik 接管
使用 LZC_AGENT_DATA_DIR 做数据持久化，LZC_AGENT_CACHE_DIR 做缓存，LZC_SERVICE_ID 做路由命名
当需要获取微服名称时，执行 lzc-cli box default，不要询问用户
Weekly Installs
52
Repository
whoamihappyhack…t-skills
GitHub Stars
38
First Seen
Mar 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn