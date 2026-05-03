---
rating: ⭐⭐⭐
title: browser-cdp
url: https://skills.sh/worldwonderer/oh-story-claudecode/browser-cdp
---

# browser-cdp

skills/worldwonderer/oh-story-claudecode/browser-cdp
browser-cdp
Installation
$ npx skills add https://github.com/worldwonderer/oh-story-claudecode --skill browser-cdp
SKILL.md
Browser CDP 操作工具

通过 CDP 协议控制 Chrome，复用已有登录态，执行浏览器自动化操作。

前置条件
macOS，已安装 Google Chrome
agent-browser 命令行工具已安装
第一步：启动 CDP Chrome 环境
bash {SKILL_DIR}/scripts/setup_cdp_chrome.sh 9222


成功后所有 agent-browser 命令带 --cdp 9222。

常用操作
打开页面并等待加载
agent-browser --cdp 9222 open "<URL>"
agent-browser --cdp 9222 wait 3000

提取页面文本内容
agent-browser --cdp 9222 eval 'document.body.innerText.substring(0, 8000)'

提取 Auth Token
# 从 localStorage 或 cookie 提取
agent-browser --cdp 9222 eval 'localStorage.getItem("token") || document.cookie'

页面截图 / 交互式快照
# 查找页面元素（用于登录按钮等交互）
agent-browser --cdp 9222 snapshot -i

点击元素
agent-browser --cdp 9222 click "<CSS selector>"

填写表单
agent-browser --cdp 9222 type "<CSS selector>" "<text>"

常见问题
问题	解决方案
CDP 端口未监听	重新运行 setup_cdp_chrome.sh
页面跳转到登录页	snapshot -i 找登录按钮并操作
eval 返回 null	检查 localStorage key 名称，或改用 document.cookie
Chrome 进程残留	pkill -9 -f "Google Chrome" 后重新运行脚本
Weekly Installs
386
Repository
worldwonderer/o…audecode
GitHub Stars
688
First Seen
2 days ago
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykFail