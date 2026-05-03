---
title: agent-browser-cli
url: https://skills.sh/site/skills.volces.com/agent-browser-cli
---

# agent-browser-cli

skills/skills.volces.com/agent-browser
agent-browser
$ npx skills add https://skills.volces.com/c/arkclaw-personal/skills/clawhub/joshhuang123
SKILL.md
Agent Browser

Vercel 出品的浏览器自动化 CLI，基于 Playwright，比标准浏览器工具更快更灵活。

快速开始
agent-browser open <url>     # 打开网页
agent-browser snapshot       # 获取页面可访问性树
agent-browser click @<ref>   # 点击元素（用ref引用）
agent-browser fill @<ref> "内容"  # 填入内容
agent-browser close         # 关闭浏览器

常用命令
导航
agent-browser open <url>      # 打开URL（别名：goto, navigate）
agent-browser back            # 后退
agent-browser forward         # 前进
agent-browser reload          # 刷新

交互
agent-browser click <sel>                    # 点击
agent-browser dblclick <sel>                  # 双击
agent-browser fill <sel> "text"               # 填入（清空后填）
agent-browser type <sel> "text"               # 输入（追加）
agent-browser select <sel> <value>             # 选择下拉选项
agent-browser check <sel>                      # 勾选复选框
agent-browser uncheck <sel>                   # 取消勾选
agent-browser press <key>                      # 按键（Enter, Tab, Escape等）

获取信息
agent-browser snapshot              # 获取可访问性树（推荐）
agent-browser get text <sel>        # 获取文本
agent-browser get html <sel>        # 获取HTML
agent-browser get value <sel>       # 获取输入值
agent-browser get title             # 获取页面标题
agent-browser get url               # 获取当前URL
agent-browser screenshot [path]     # 截图
agent-browser screenshot --annotate  # 带标注的截图

元素定位

通过 snapshot 输出的 ref（如 @e14）直接引用：

agent-browser click @e14
agent-browser fill @e13 "hello"


或使用 CSS 选择器：

agent-browser click "#submit"
agent-browser fill "input[name='email']" "test@test.com"


或使用 ARIA 角色查找：

agent-browser find role button click --name "Submit"
agent-browser find text "Sign In" click
agent-browser find label "Email" fill "test@test.com"
agent-browser find placeholder "Search" type "query"

典型工作流
1. 签到任务
# 打开登录页
agent-browser open <签到页面URL>

# 获取页面结构
agent-browser snapshot

# 点击登录/签到按钮（用实际ref替换 @eXX）
agent-browser click @eXX

# 等待页面加载
sleep 2
agent-browser snapshot

2. 填表任务
agent-browser open <表单URL>
agent-browser snapshot

# 填入各字段
agent-browser find label "用户名" fill "myuser"
agent-browser find label "密码" fill "mypassword"
agent-browser find role button click --name "提交"

3. 定时签到（配合cron）

创建脚本 ~/.openclaw/scripts/daily-checkin.sh：

#!/bin/bash
agent-browser open <签到URL>
sleep 2
agent-browser find role button click --name "签到"
agent-browser screenshot /tmp/checkin_$(date +%Y%m%d).png
agent-browser close

注意事项
先 snapshot 再操作 - 每次页面变化后重新获取 ref
添加等待 - 页面加载需要时间，用 sleep 2 或等待
保持浏览器开启 - 多个操作可以在同一浏览器会话中完成
完成后关闭 - 用 agent-browser close 释放资源
依赖安装

如果 agent-browser 未安装：

npm install -g agent-browser
agent-browser install

Weekly Installs
301
Source
skills.volces.c…huang123
First Seen
4 days ago