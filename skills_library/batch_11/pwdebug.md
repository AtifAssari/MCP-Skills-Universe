---
title: pwdebug
url: https://skills.sh/dcjanus/prompts/pwdebug
---

# pwdebug

skills/dcjanus/prompts/pwdebug
pwdebug
Installation
$ npx skills add https://github.com/dcjanus/prompts --skill pwdebug
SKILL.md
Playwright 浏览器调试 CLI
概览

该技能提供一个基于 Playwright 的命令行工具，用于启动浏览器服务并执行导航、评估 JS、截图、元素拾取与日志监听等调试操作。当前仅支持 Chromium（通过 CDP 连接）。

快速开始

工作目录应为本文件所在目录，示例命令默认从该目录执行。 说明：必须直接执行脚本，不要用 uv run python 或 python。

脚本调用方式示例：

cd skills/pwdebug && ./scripts/pwdebug.py start


错误示例：

uv run python skills/pwdebug/scripts/pwdebug.py start
python skills/pwdebug/scripts/pwdebug.py start

启动浏览器服务（常驻进程）：
./scripts/pwdebug.py start

在新标签页打开页面：
./scripts/pwdebug.py nav https://example.com --new

执行 JS 表达式：
./scripts/pwdebug.py evaluate "document.title"

截图：
./scripts/pwdebug.py screenshot --full

交互式拾取元素：
./scripts/pwdebug.py pick "点击登录按钮"

监听控制台日志：
./scripts/pwdebug.py watch-logs

查看最近日志：
./scripts/pwdebug.py logs 100

说明
CLI 入口：./scripts/pwdebug.py
日志路径：~/.cache/pwdebug/console.log.jsonl
状态路径：~/.cache/pwdebug/server.json
依赖与安装
脚本依赖通过 uv --script 管理。
Weekly Installs
22
Repository
dcjanus/prompts
GitHub Stars
19
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn