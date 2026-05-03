---
title: abc-backend-guide
url: https://skills.sh/abcfed/claude-marketplace/abc-backend-guide
---

# abc-backend-guide

skills/abcfed/claude-marketplace/abc-backend-guide
abc-backend-guide
Installation
$ npx skills add https://github.com/abcfed/claude-marketplace --skill abc-backend-guide
SKILL.md
ABC 后端开发指南

ABC 后端开发规范参考，涵盖开发、调试、运维等常见场景。

场景路由

根据用户的意图，读取对应的场景文件：

用户意图	场景文件	关键词
后端编码规范与基础	coding-guide.md	Java、Spring Boot、注解、Lombok、分层架构、编码规范、Controller、Service、Entity、DTO、CRUD、增删改查
RPC 服务（提供/调用）	rpc-guide.md	RPC、Feign、微服务调用、服务间通信、AbcServiceResponseBody
数据库表结构变更	db-migration.md	建表、加字段、加索引、改表、数据库变更、DDL
后端问题排查调试	debug-guide.md	调试、排查、报错、traceId、SLS、链路追踪
日志打印规范	logging.md	日志、log、打日志、message-index、AbcLogMarker、@LogReqAndRsp
异常处理规范	exception.md	异常、Exception、抛异常、错误码、NotFoundException、CisCustomException
启动后端项目	local-dev.md	启动、运行、端口、本地开发、环境配置、Gradle
Git 分支管理（通用）	使用 abc-git-flow SKILL（如果安装了）	分支、feature、hotfix、发布、提测、合并、灰度
Git 分支管理（后端特有）	backend-git-flow.md	dev-join、dev-joint、test-join、test-joint、联合分支、后端发布
Instructions
先判断用户的意图属于哪个场景
读取对应的场景文件（可以同时读取多个相关文件）
如果用户是学习目的，用通俗易懂的语言解释概念
如果用户是编码目的，严格按照场景文件中的规范生成代码
如果意图不明确，先问用户想做什么，再路由到对应场景
项目级差异：各项目可在 .claude/skills/ 中创建同名 SKILL 覆盖或补充本指南
Weekly Installs
16
Repository
abcfed/claude-m…ketplace
GitHub Stars
19
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass