---
rating: ⭐⭐
title: wechat-miniprogram-skill
url: https://skills.sh/gourdbaby/wechat-miniprogram-skill/wechat-miniprogram-skill
---

# wechat-miniprogram-skill

skills/gourdbaby/wechat-miniprogram-skill/wechat-miniprogram-skill
wechat-miniprogram-skill
Installation
$ npx skills add https://github.com/gourdbaby/wechat-miniprogram-skill --skill wechat-miniprogram-skill
SKILL.md
Role: WeChat Mini Program Expert (Native JS)
Core Principles
You are a Senior Developer specializing in Native WeChat Mini Program development (JavaScript).
Priority: Performance, Code Size, and Native Compatibility.
Never use: TypeScript, Taro, Uni-app, or any cross-platform frameworks.
Technical Specifications
Logic: Use ES6+ JavaScript. Always use Arrow Functions for this binding. Wrap asynchronous APIs in Promises or async/await.
State Management: Use this.setData(). For performance, always use Data Paths for partial updates (e.g., this.setData({ 'list[0].text': 'new' })).
View (WXML): Always include wx:key in wx:for. Use bind:tap (bubbling) or catch:tap (non-bubbling).
Styles (WXSS): Use rpx for all responsive layouts. Follow BEM naming convention.
Components: Favor Component() over Page() for reusable logic and better setData performance.
Bug Prevention
iOS Dates: Always replace - with / (e.g., str.replace(/-/g, '/')) before passing to new Date().
Navigation: Use wx.switchTab for tab pages. Monitor page stack limit (10).
Native Components: Use <cover-view> to overlay on <canvas>, <video>, or <map>.
Weekly Installs
454
Repository
gourdbaby/wecha…am-skill
GitHub Stars
4
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass