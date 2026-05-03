---
rating: ⭐⭐⭐
title: uniapp
url: https://skills.sh/hairyf/skills/uniapp
---

# uniapp

skills/hairyf/skills/uniapp
uniapp
Installation
$ npx skills add https://github.com/hairyf/skills --skill uniapp
SKILL.md
uni-app

本 skill 基于 uni-app 文档生成，生成日期 2026-01-29。

uni-app 是基于 Vue 的跨平台应用开发框架，一套代码可编译到 App、H5、微信/支付宝/百度等小程序。适用于需要为 Agent 提供「如何用 uni-app 配置项目、写页面与组件、使用路由与 API、注意跨端差异」等能力说明的场景。

核心参考
主题	说明	参考
入口 main.js/uts	入口文件、代码时序、插件与路由	core-main
App.vue	应用生命周期、globalData、全局样式	core-app
pages.json	页面路由、globalStyle、tabBar、easycom	core-pages
页面生命周期	onLoad、onShow、onReady、onHide、onUnload	core-lifecycle
manifest.json	应用配置、版本、超时、各端配置	core-manifest
条件编译	#ifdef/#ifndef、平台标识、多端差异化	core-conditional-compilation
样式与布局	rpx/px 单位、预处理器、nvue 差异	core-syntax-css
分包配置	subPackages、preloadRule、主包与分包	core-subpackages
能力参考
主题	说明	参考
API 概述	uni API、Promise 化、各端特色 API、canIUse	features-api-overview
路由与跳转	navigateTo/redirectTo/reLaunch/switchTab、传参、EventChannel、窗口动画	features-router
组件概述	基础组件分类、公共属性、easycom、扩展组件	features-component-overview
自定义组件	slot、ref、父子通信、defineExpose	features-vue-components
Vue 基础	单文件结构、数据绑定、事件、列表与条件渲染	features-vue-basics
页面栈与通讯	getCurrentPages、uni.$emit/$on/$off	features-window-communication
下拉与触底	onPullDownRefresh、onReachBottom、start/stopPullDownRefresh	features-pulldown
定时器	setTimeout、setInterval、clearTimeout、clearInterval、销毁时清理	features-timer
网络请求	uni.request、上传下载、超时与中断	features-request
网络状态	getNetworkType、onNetworkStatusChange、offNetworkStatusChange	features-network
上传与下载	uploadFile、downloadFile、formData、多文件	features-upload-download
WebSocket	connectSocket、SocketTask、onOpen/onMessage/send/close	features-websocket
数据缓存	setStorage/getStorage、本地持久化	features-storage
剪贴板	setClipboardData、getClipboardData	features-clipboard
键盘	hideKeyboard、onKeyboardHeightChange、offKeyboardHeightChange	features-keyboard
启动参数	getLaunchOptionsSync、getEnterOptionsSync、path/query/scene	features-launch-options
授权与设置	authorize、getSetting、openSetting、scope 列表	features-authorize
交互反馈	showToast、showLoading、showModal、showActionSheet	features-ui-prompt
拦截器	addInterceptor、removeInterceptor、回调与返回值改写	features-interceptor
节点信息	createSelectorQuery、boundingClientRect、scrollOffset、in(component)	features-nodes-info
节点相交	createIntersectionObserver、relativeTo、observe、disconnect	features-intersection-observer
表单	form 组件、report-submit、@submit、@reset、form-type	features-form
图片	chooseImage、previewImage、getImageInfo、saveImageToPhotosAlbum	features-media-image
视频与音频	chooseVideo、createVideoContext、getRecorderManager、createInnerAudioContext、getBackgroundAudioManager	features-media-video-audio
文件	saveFile、getSavedFileList、openDocument、getFileSystemManager	features-file
位置与地图	getLocation、chooseLocation、openLocation、位置更新、createMapContext	features-location
画布	createCanvasContext、CanvasContext、canvasToTempFilePath	features-canvas
导航栏与 TabBar	setNavigationBarTitle、setTabBarItem、hideTabBar、setTabBarBadge	features-navigation-tabbar
媒体查询与胶囊按钮	createMediaQueryObserver、getMenuButtonBoundingClientRect、setBackgroundColor	features-ui-extras
动画	createAnimation、animation.export、组件 animation 属性、pageScrollTo	features-ui-animation
字体与单位	loadFontFace、rpx2px、upx2px	features-font
语言与主题	getLocale、setLocale、onLocaleChange、onThemeChange	features-locale-theme
系统信息	getSystemInfo、getDeviceInfo、getWindowInfo、getAppBaseInfo	features-system-info
设备能力	振动、scanCode、makePhoneCall、getBatteryInfo、onMemoryWarning	features-system-device
应用级事件	onPageNotFound、onError、onAppShow、onAppHide	features-application-events
页面预加载	preloadPage、unPreloadPage（App-nvue、H5）	features-preload-page
登录/支付/分享/推送	login、getUserInfo、requestPayment、share、getProvider、push 概述	features-plugins-overview
其它 API	getAccountInfoSync、getEnvInfoSync、getUpdateManager、navigateToMiniProgram、exit、nextTick、base64	features-other-apis
H5 宽屏适配	topWindow、leftWindow、rightWindow、getTopWindowStyle、setTopWindowStyle	features-h5-adapt
进阶参考
主题	说明	参考
nvue	原生渲染、与 vue 差异、requireNativePlugin	advanced-nvue
renderjs	视图层 JS、App 端操作 DOM、echarts 等	advanced-renderjs
subNVues	App 原生子窗体、getSubNVueById、getCurrentSubNVue	advanced-subnvue
Worker	多线程、各端实现差异	advanced-worker
最佳实践
主题	说明	参考
跨端注意	标签与样式、JS/API 差异、工程与配置、常见异常	best-practices-cross-platform
Weekly Installs
160
Repository
hairyf/skills
GitHub Stars
15
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn