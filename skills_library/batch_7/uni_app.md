---
title: uni-app
url: https://skills.sh/uni-helper/skills/uni-app
---

# uni-app

skills/uni-helper/skills/uni-app
uni-app
Installation
$ npx skills add https://github.com/uni-helper/skills --skill uni-app
Summary

Vue.js cross-platform framework for building apps across iOS, Android, HarmonyOS, Web, and 10+ mini-program platforms.

Provides 50+ built-in components covering views, forms, media, navigation, and UI feedback patterns
Includes APIs for networking, storage, geolocation, file operations, device info, and lifecycle management
Supports platform-specific code via condition compilation directives; most APIs return Promises for async workflows
Configured through pages.json (routing, tabs, sub-packages) and manifest.json (permissions, platform settings)
Covers 13 deployment targets with full support, including WeChat, Alipay, Baidu, Douyin, and HarmonyOS ecosystems
SKILL.md

The skill is based on uni-app documentation, generated at 2026-01-30.

uni-app is a Vue.js-based cross-platform framework for developing applications that run on iOS, Android, HarmonyOS, Web (responsive), and various mini-program platforms (WeChat/Alipay/Baidu/Douyin/Feishu/QQ/Kuaishou/DingTalk/Taobao/Jingdong/Xiaohongshu).

Core
Topic	Description	Reference
Core Framework	Project structure, platform support, condition compilation	core-framework
View Components	view, scroll-view, swiper, movable-area, cover-view	core-view-components
Form Components	input, textarea, picker, checkbox, radio, switch, slider	core-form-components
Features
UI Components
Topic	Description	Reference
Media Components	image, video, camera, live-player, map	feature-media-components
Navigation	navigator, routing, page navigation	feature-navigation
UI Feedback	toast, modal, loading, action sheet, pull refresh	feature-ui-feedback
APIs
Topic	Description	Reference
Network	HTTP requests, file upload/download, WebSocket	feature-network
Storage	Local storage, file system, caching	feature-storage
System Info	Device info, network status, screen, vibration	feature-system-info
File Operations	Image/video selection, file system operations	feature-file-operations
Location	Geolocation, map component, address selection	feature-location
Lifecycle	App and page lifecycle hooks	feature-lifecycle
Configuration
Topic	Description	Reference
pages.json	Page routing, tab bar, global styles, sub-packages	config-pages
manifest.json	App config, permissions, platform settings	config-manifest
Platform Support
Platform	Support Level
iOS App	Full support
Android App	Full support
HarmonyOS Next	Full support
H5/Web	Full support
WeChat Mini Program	Full support
Alipay Mini Program	Full support
Baidu Smart Program	Full support
Douyin Mini Program	Full support
QQ Mini Program	Full support
Kuaishou Mini Program	Full support
Feishu Mini Program	Full support
JD Mini Program	Full support
HarmonyOS Meta Service	Full support
Key Concepts
Condition Compilation

Use special comments to write platform-specific code:

<!-- #ifdef APP-PLUS -->
<view>App only</view>
<!-- #endif -->

<!-- #ifdef MP-WEIXIN -->
<view>WeChat only</view>
<!-- #endif -->

API Promise Support

Most uni-app APIs support Promise when no callback is provided:

const res = await uni.request({ url: 'https://api.example.com' })

Cross-Platform Best Practices
Use uni-app components and APIs instead of platform-specific ones
Use condition compilation for platform-specific features
Test on all target platforms
Use rpx for responsive layouts
Handle platform differences in manifest.json
must use uni-helper tools
MCP扩展

当需要查询 uni-app 官方文档时，优先调用 search-docs-by-Uniapp-official MCP 工具搜索相关 API 文档和使用示例。

使用场景：

用户询问特定 API 的详细用法
需要官方文档中的代码示例
查询组件的属性和事件
了解 API 的平台兼容性

工具安装： 如果检测到该 MCP 工具不可用，引导用户访问 https://github.com/uni-helper/mcp 进行安装。

Weekly Installs
966
Repository
uni-helper/skills
GitHub Stars
58
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass