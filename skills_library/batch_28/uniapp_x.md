---
title: uniapp-x
url: https://skills.sh/hairyf/skills/uniapp-x
---

# uniapp-x

skills/hairyf/skills/uniapp-x
uniapp-x
Installation
$ npx skills add https://github.com/hairyf/skills --skill uniapp-x
SKILL.md
uni-app x

本 skill 基于 uni-app x 文档生成，生成日期 2026-01-29。

uni-app x 是下一代 uni-app，跨平台应用开发引擎。包含 UTS 语言、uvue 渲染引擎、uni 组件与 API 及扩展机制。适用于需要为 Agent 提供「如何用 uni-app x 写页面、组件、API、UTS、样式与工程配置」等能力说明的场景。

核心参考
主题	说明	参考
项目结构	新建项目、目录结构、运行与发行	core-project
页面与 uvue	页面文件、构成、pages.json	core-page
页面生命周期	onLoad、onShow、onReady、onBackPress 等	core-lifecycle
App.uvue	应用入口、应用生命周期、globalData、全局样式	core-app
manifest.json	应用配置、appid、版本、图标、uni-app-x 标识	core-manifest
编译器与静态资源	条件编译、static、编译缓存	core-compiler
UTS 语言
主题	说明	参考
UTS 概述	类型声明、变量/常量、与 TS 的差异	uts-overview
数据类型	boolean、number、string、Array、UTSJSONObject、type	uts-data-type
与 JS 开发差别	强类型、data 类型、事件参数类型	features-codegap
条件编译	#ifdef APP-ANDROID、平台与项目类型判断	uts-conditional
函数与模块	函数定义、异常 try-catch、export/import	uts-function-module
Vue / uvue
主题	说明	参考
uvue 概述	SFC、template/script/style、组合式与选项式	vue-uvue
组件	创建、easycom、手动引用、ref 与 defineExpose	vue-component
内置指令	v-if、v-for、v-show、v-model、v-bind、v-html 等	features-vue-directives
组件标志	id、ref、UniElement、getElementById、createXXXContext	features-idref
组合式 API	ref、computed、watch、reactive、readonly、watchEffect	vue-composition-api
数据绑定与修饰符	响应式状态、事件修饰符、v-model 修饰符	vue-data-bind-modifier
样式 (CSS/ucss)
主题	说明	参考
uvue CSS	flex 布局、样式不继承、选择器与优先级	css-ucss
组件与 API
主题	说明	参考
组件概述	内置组件、自定义组件、easycom、uts 组件	features-component-overview
API 概述	uni API、全局 API、原生 API 调用	features-api-overview
路由与跳转	navigateTo、redirectTo、reLaunch、switchTab、navigateBack、参数传递	features-navigation
本地存储	setStorageSync、getStorageSync、key-value、对象需 as UTSJSONObject	features-storage
页面栈与当前页	getCurrentPages、UniPage、this.$page、getDialogPages	features-get-current-pages
dialogPage	弹窗页、openDialogPage、closeDialogPage、与主 page 区别	features-dialog-page
全局状态	globalData、专用 store 模块（reactive）	features-global-state
长列表与滚动	scroll-view、list-view、吸顶、嵌套滚动、sticky-header	features-list-scroll
request 与网络	流式响应、cookie、拦截器、泛型与 Task 释放	features-api-request
事件与系统信息	uni.$on/$emit、getLaunchOptionsSync、getSystemInfo	features-api-event-system-info
DOM 与 UniElement	getElementById、ref、样式与 draw API、跟手动效	features-dom
表单 form	submit/reset、form-type、子组件与数据提交	features-form
宽屏适配	leftWindow/rightWindow、页面作组件、窗体通信	features-adapt
国际化	多语言、lime-i18n、vue-i18n(Web)、uni.getLocale	features-i18n
主题与暗黑	theme.json、setAppTheme、onAppThemeChange、pages.json 样式	features-theme-dark
编译到 Web	SPA、与 App 差异、refs 类型、SSR 简述	features-web
教程与最佳实践
主题	说明	参考
request 联网	UTSJSONObject 与 type 泛型处理接口数据	best-practices-request
选项式转组合式	改造要点、生命周期与 ref 类型	best-practices-options-to-composition
性能优化	DOM 数量、动画用 transform、长列表与分批加载	best-practices-performance
语言服务与 AI	语言服务插件、Cursor/VSCode、AI Rules、MCP、AI 修复	tutorial-ls-ai-rules
进阶
主题	说明	参考
原生 SDK 与混合开发	嵌入原生工程、导出应用原生资源、集成文档	advanced-native-sdk
Weekly Installs
59
Repository
hairyf/skills
GitHub Stars
15
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass