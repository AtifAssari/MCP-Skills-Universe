---
title: aptx-api-plugin-auth
url: https://skills.sh/haibaraaiaptx/aptx-skill/aptx-api-plugin-auth
---

# aptx-api-plugin-auth

skills/haibaraaiaptx/aptx-skill/aptx-api-plugin-auth
aptx-api-plugin-auth
Installation
$ npx skills add https://github.com/haibaraaiaptx/aptx-skill --skill aptx-api-plugin-auth
SKILL.md
aptx-api-plugin-auth
目录
工作流程
TokenStore 接口
中间件模式（推荐）
控制器模式（手动 token 管理）
配置选项
错误处理
关键约束
高级主题
工作流程

在接入认证插件时，执行以下流程：

强制使用 TokenStore 抽象，不直接在业务代码里散落 token 读写。
创建 createAuthMiddleware({ store, refreshToken, ... }) 并挂到 RequestClient.use(...)。
refreshToken 返回 { token, expiresAt } 或 string，优先返回 expiresAt 以便存储层同步过期时间。
使用 shouldRefresh 定义触发刷新条件；默认仅在 HttpError(401) 时刷新。
配置 onRefreshFailed 处理刷新失败后的业务动作（例如清理会话或跳转登录）。

默认推荐搭配：

@aptx/token-store（TokenStore 接口定义）
@aptx/token-store-cookie（浏览器 cookie 实现）
SSR：@aptx/token-store-ssr-cookie（Node/SSR request-scoped cookie 实现）
TokenStore 接口

store 参数支持三种形式（TokenStoreResolver 类型）：

type TokenStoreResolver =
  | TokenStore                    // 直接实例（向后兼容）
  | (() => TokenStore)            // 同步工厂函数
  | (() => Promise<TokenStore>);  // 异步工厂函数（SSR）


TokenStore 接口（由 @aptx/token-store 提供）：

interface TokenStore {
  // 获取存储的 token
  getToken(): string | undefined | Promise<string | undefined>;

  // 存储 token（可选 meta 用于支持过期时间和其他元数据）
  setToken(token: string, meta?: { expiresAt?: number; [key: string]: unknown }): void | Promise<void>;

  // 清除 token
  clearToken(): void | Promise<void>;

  // --- 可选扩展方法 ---

  // 获取元数据（用于读取 expiresAt）
  getMeta?(): Promise<{ expiresAt?: number } | undefined>;

  // 获取完整记录（token + meta）
  getRecord?(): Promise<{ token: string; meta?: { expiresAt?: number } } | undefined>;
}

使用场景
形式	场景	说明
直接实例	浏览器端	单例模式，所有请求共享同一 store
同步工厂函数	浏览器端（推荐）	保持 API 一致性
异步工厂函数	SSR 端	每请求独立 store，从请求上下文读取 cookie

推荐实现：

@aptx/token-store-cookie - 浏览器 cookie 存储（自动跨标签页同步）
@aptx/token-store-ssr-cookie - SSR cookie 存储（每请求独立）
自定义实现（如 localStorage、sessionStorage、IndexedDB）
中间件模式（推荐）
浏览器端

最小模板：

import { createAuthMiddleware } from "@aptx/api-plugin-auth";
import { createCookieTokenStore } from "@aptx/token-store-cookie";

const store = createCookieTokenStore({
  tokenKey: "aptx_token",
  metaKey: "aptx_token_meta",
  syncExpiryFromMeta: true,
});

const auth = createAuthMiddleware({
  store, // 或使用工厂函数: store: () => store
  refreshLeewayMs: 60_000,
  refreshToken: async () => {
    return { token: "new-token", expiresAt: Date.now() + 30 * 60 * 1000 };
  },
});

SSR 端（Next.js App Router）

SSR 环境需要为每个请求创建独立的 store，因为 cookie 需要从请求上下文读取。

重要：服务端默认不处理 token 刷新，刷新由客户端处理。

import { cookies } from "next/headers";
import { createAuthMiddleware } from "@aptx/api-plugin-auth";
import { createSsrCookieTokenStore } from "@aptx/token-store-ssr-cookie";

// 创建请求级别的 API 客户端
export async function createServerApiClient() {
  const cookieStore = await cookies();

  const auth = createAuthMiddleware({
    // 异步工厂函数：每次请求创建独立 store
    store: async () => createSsrCookieTokenStore({
      tokenKey: "aptx_token",
      metaKey: "aptx_token_meta",
      getCookieHeader: () => cookieStore.toString(),
      setCookie: (value) => {
        // 解析 Set-Cookie 并调用 cookieStore.set()
      },
    }),
    // 注意：服务端不需要 refreshToken，刷新由客户端处理
    // refreshToken 会被忽略
  });

  return createApiClient().use(auth);
}


关键点：

使用异步工厂函数 async () => store
每次调用中间件都会执行工厂函数，获取该请求的 store 实例
不同请求的 store 实例完全隔离，避免 token 串用
服务端不处理刷新：收到 401 直接抛出错误，由客户端处理跳转登录
控制器模式（手动 token 管理）

对于需要手动控制 token 的场景（如手动刷新、预加载 token）：

import { createAuthController } from "@aptx/api-plugin-auth";

const controller = createAuthController({
  store,
  refreshToken: async () => ({ token: "...", expiresAt: Date.now() + 30000 }),
});

// 手动触发刷新并返回新 token
const token = await controller.refresh();

// 确保返回有效 token（接近过期时自动刷新）
const validToken = await controller.ensureValidToken();


AuthController 方法：

refresh(): Promise<string> - 强制刷新 token 并返回新 token
ensureValidToken(): Promise<string> - 返回有效 token，接近过期时自动刷新
配置选项
AuthPluginOptions
选项	类型	必填	默认值	说明
store	TokenStoreResolver	✅	-	Token 持久化抽象（支持直接实例、同步工厂、异步工厂）
refreshToken	Promise<{token, expiresAt?} | string>	✅	-	刷新 token 的异步函数（仅客户端生效）
refreshLeewayMs	number	❌	60_000	提前刷新的时间窗口（毫秒）
shouldRefresh	(error, req, ctx) => boolean	❌	401 检查	判断是否需要刷新的条件（仅客户端生效）
onRefreshFailed	(error) => void	❌	-	刷新失败回调（仅客户端生效）
headerName	string	❌	"Authorization"	自定义 header 名称
tokenPrefix	string	❌	"Bearer "	Token 前缀
maxRetry	number	❌	1	刷新失败后重试次数（仅客户端生效）

注意：服务端（SSR）环境下，refreshToken、shouldRefresh、onRefreshFailed、maxRetry 会被忽略，因为服务端默认不处理 token 刷新。

refreshToken 返回值

refreshToken 可以返回两种格式：

推荐格式（包含过期时间）：
return {
  token: "new-token",
  expiresAt: Date.now() + 30 * 60 * 1000, // 30 分钟后过期
};

简单格式（仅 token）：
return "new-token"; // 适用于不需要过期时间的场景


优先返回包含 expiresAt 的对象，便于存储层（如 @aptx/token-store-cookie）同步过期时间。

自定义 header 配置

对于非标准认证方案（如自定义 header 或无 Bearer 前缀）：

const auth = createAuthMiddleware({
  store,
  refreshToken: async () => ({ token: "custom-token" }),
  headerName: "X-Auth-Token",      // 自定义 header 名称
  tokenPrefix: "",                  // 移除 Bearer 前缀
  maxRetry: 2,                      // 增加重试次数
});

自定义 shouldRefresh 条件

默认仅在 401 状态码时触发刷新。如需自定义逻辑：

const auth = createAuthMiddleware({
  store,
  refreshToken: async () => ({ token: "..." }),
  shouldRefresh: (error, req, ctx) => {
    // error: { status?: number, message?: string, code?: string }
    return error.status === 401 || error.code === "TOKEN_EXPIRED";
  },
});


参数说明：

error: 错误对象，包含 status（HTTP状态码）、message（错误消息）、code（业务错误码）
req: 原始请求对象
ctx: 上下文对象
重试策略

maxRetry 控制刷新失败后的重试次数：

maxRetry: 0 - 刷新失败后立即抛出错误
maxRetry: 1 (默认) - 刷新失败后重试一次
maxRetry: 2 - 刷新失败后重试两次

刷新失败时会自动调用 store.clearToken() 清除本地 token。

导出常量
SKIP_AUTH_REFRESH_META_KEY

用于标记请求跳过 auth 刷新逻辑，避免 refreshToken 请求本身返回 401 时触发死锁。

import { SKIP_AUTH_REFRESH_META_KEY } from "@aptx/api-plugin-auth";

// 在 refreshToken 请求的 spec 中添加此标记
const refreshTokenSpec = {
  method: "POST",
  path: "/api/refresh-token",
  meta: { [SKIP_AUTH_REFRESH_META_KEY]: true },
};


使用场景：当 refreshToken 回调使用同一个 apiClient 发起刷新请求时，必须添加此标记。

错误处理
const auth = createAuthMiddleware({
  store,
  refreshToken: async () => {
    const res = await fetch("/api/refresh");
    if (!res.ok) throw new Error("Refresh failed");
    return await res.json();
  },
  onRefreshFailed: (error) => {
    // 刷新失败后的业务动作（仅客户端执行）
    console.error("Auth refresh failed:", error);
    // 例如：跳转登录页、清除用户状态、显示登录弹窗
    window.location.href = "/login";
  },
});


注意：onRefreshFailed 仅在客户端执行。服务端收到 401 时会直接抛出错误，不调用此回调。

关键约束
store 必填且是唯一 token 持久化入口，必须实现 TokenStore 接口。
refreshToken 尽量返回 expiresAt，便于存储层处理过期时间。
若刷新失败，必须由 onRefreshFailed 统一处理业务动作（仅客户端生效）。
shouldRefresh 默认仅在 HttpError(401) 时触发刷新，其他错误不会刷新（仅客户端生效）。
服务端默认不处理 token 刷新：服务端收到 401 直接抛出错误，刷新由客户端处理。
何时不使用
静态 API 调用：无需用户认证的公开接口不需要使用此插件
服务端到服务端认证：应使用 API Key 或应用级凭证，而非用户 token
仅需一次性认证：如果只需在应用启动时获取一次 token，无需自动刷新，可直接使用 createAuthController 而不挂载中间件
高级主题
刷新请求死锁保护

重要：如果 refreshToken 回调使用同一个 apiClient 发起请求，必须使用 SKIP_AUTH_REFRESH_META_KEY 标记刷新请求。

问题场景：

1. 请求 A → 401
2. auth 中间件调用 refreshToken()
3. refreshToken 请求经过 auth 中间件 → 401
4. auth 中间件再次调用 refreshToken() → 死锁！


解决方案：

import { SKIP_AUTH_REFRESH_META_KEY } from "@aptx/api-plugin-auth";

// refreshToken 请求的 spec 必须添加跳过标记
export function buildRefreshTokenSpec(): RequestSpec {
  return {
    method: "POST",
    path: "/api/refresh-token",
    meta: { [SKIP_AUTH_REFRESH_META_KEY]: true },  // 关键！
  };
}

边缘情况处理

详见 edge-cases.md，包含：

并发刷新防止
Token 验证
网络错误重试
跨标签页 Token 同步
无限刷新与死锁保护
Weekly Installs
23
Repository
haibaraaiaptx/aptx-skill
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass