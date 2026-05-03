---
title: zerone-cli
url: https://skills.sh/giikin/skills/zerone-cli
---

# zerone-cli

skills/giikin/skills/zerone-cli
zerone-cli
Installation
$ npx skills add https://github.com/giikin/skills --skill zerone-cli
SKILL.md
Zerone CLI 工具集

Zerone CLI (@zeronejs/cli) 是团队内部的前端工程化工具，提供四大核心功能。

功能索引（按使用频率排序）

根据用户意图匹配对应功能，阅读对应的 references 文档后执行操作。

1. API 后端接口生成（最常用）

触发词：生成接口、更新接口、pnpm api、新增 API 模块、生成 API 模块 xxx

两种场景：

场景	用户说	操作
更新已有模块	"更新 mcp 的接口"	直接执行 pnpm api:mcp
创建新模块	"生成 API 模块 gstore"	创建整套文件（request.ts、swagger.config.json、.env、package.json script）

详细文档 → api-generation.md

2. 字体图标管理

触发词：图标、iconfont、pnpm font、更新图标、icon、at.alicdn.com 链接

三种场景：

场景	用户说	操作
更新图标	发了一个 //at.alicdn.com/... 链接	更新 config.json → 执行 pnpm font
首次创建	"添加 iconfont"	确保 package.json 有 font 脚本 → 创建 config → 执行 pnpm font → 引入 main.ts
图标使用	"怎么用图标"	class 格式：acore-font icon-{图标名}

详细文档 → font-grabber.md

3. 创建前端项目

触发词：创建项目、新建项目、pnpm create zerone、脚手架、初始化项目

执行 pnpm create zerone 进入交互式选择，用户自行选择模板（giime-ts、tailwind-ts、admin-ts 等）。

详细文档 → create-project.md

4. 工作日志

触发词：日报、周报、月报、工作日志、zerone log

使用 zerone log 基于 Git 提交记录生成日报/周报/月报。

详细文档 → zerone-log.md

Weekly Installs
59
Repository
giikin/skills
GitHub Stars
2
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn