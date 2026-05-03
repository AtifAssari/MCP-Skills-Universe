---
rating: ⭐⭐
title: aptx-token-store-cookie
url: https://skills.sh/haibaraaiaptx/aptx-skill/aptx-token-store-cookie
---

# aptx-token-store-cookie

skills/haibaraaiaptx/aptx-skill/aptx-token-store-cookie
aptx-token-store-cookie
Installation
$ npx skills add https://github.com/haibaraaiaptx/aptx-skill --skill aptx-token-store-cookie
SKILL.md
aptx-token-store-cookie
Quick Start

Create store with default configuration:

import { createCookieTokenStore } from "@aptx/token-store-cookie";

const store = createCookieTokenStore({
  tokenKey: "aptx_token",
  metaKey: "aptx_token_meta",
  syncExpiryFromMeta: true,
  cookie: {
    path: "/",
    sameSite: "lax",
    secure: true,
  },
});

进阶：使用 CookieTokenStore 类

除了 createCookieTokenStore 工厂函数，还可以直接使用 CookieTokenStore 类：

import { CookieTokenStore, CookieTokenStoreOptions } from "@aptx/token-store-cookie";

const options: CookieTokenStoreOptions = {
  tokenKey: "aptx_token",
  metaKey: "aptx_token_meta",
  syncExpiryFromMeta: true,
  cookie: {
    path: "/",
    sameSite: "lax",
    secure: true,
  },
};

// 直接实例化
const store = new CookieTokenStore(options);


适用于需要更多控制权的场景。

SSR / Node 环境说明

@aptx/token-store-cookie 基于 js-cookie，属于浏览器实现，不适用于 SSR/Node。

SSR 场景推荐：

每个 SSR request 创建自己的 TokenStore（request-scoped），从入站 Cookie 读取 token，并通过 Set-Cookie 写回响应。
可使用 @aptx/token-store-ssr-cookie（本仓库新增）作为 SSR cookie store。
Implementation Workflow

When integrating cookie token storage:

Create store using createCookieTokenStore({ tokenKey, metaKey, cookie, syncExpiryFromMeta })
Keep syncExpiryFromMeta: true (default) to auto-sync meta.expiresAt → cookie expires
Set syncExpiryFromMeta: false only if gateway controls cookie expiration independently
Inject store into @aptx/api-plugin-auth's store field
Test: token/meta I/O, clear, expiry sync, and disabled sync scenarios
Documentation
API Reference - Method signatures and descriptions
Configuration - All options and expiry sync rules
Testing - Mock patterns, validation examples, and test coverage checklist
Extensions - Custom fields and type imports
Weekly Installs
23
Repository
haibaraaiaptx/aptx-skill
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass