---
title: uview-pro
url: https://skills.sh/uview-pro/skills/uview-pro
---

# uview-pro

skills/uview-pro/skills/uview-pro
uview-pro
Installation
$ npx skills add https://github.com/uview-pro/skills --skill uview-pro
SKILL.md
uView Pro 组件库技能
触发条件

在以下场景中自动调用此技能：

开发 uni-app 页面时
使用 u- 前缀的组件时（如 u-button, u-input, u-form 等）
需要表单、按钮、弹窗、提示、导航等 UI 组件时
需要使用工具函数（防抖、节流、深拷贝等）时
需要使用组合式 API 钩子（useToast, useModal, useTheme 等）时
需要 uView Pro 相关的布局模板时
组件快速索引
基础组件
组件	说明	文档
button	按钮组件	button
icon	图标组件	icon
image	图片组件	image
text	文本组件	text
tag	标签组件	tag
badge	徽章组件	badge
link	链接组件	link
avatar	头像组件	avatar
表单组件
组件	说明	文档
form	表单组件	form
input	输入框组件	input
field	表单字段组件	field
textarea	文本域组件	textarea
checkbox	复选框组件	checkbox
radio	单选框组件	radio
switch	开关组件	switch
slider	滑块组件	slider
rate	评分组件	rate
numberBox	数字输入框组件	numberBox
upload	上传组件	upload
picker	选择器组件	picker
select	选择器组件	select
keyboard	键盘组件	keyboard
数据展示组件
组件	说明	文档
card	卡片组件	card
grid	宫格组件	grid
cell	单元格组件	cell
collapse	折叠面板组件	collapse
table	表格组件	table
list	列表组件	indexList
skeleton	骨架屏组件	skeleton
empty	空状态组件	empty
loading	加载组件	loading
swiper	轮播组件	swiper
steps	步骤组件	steps
timeLine	时间轴组件	timeLine
反馈组件
组件	说明	文档
toast	提示组件	toast
modal	模态框组件	modal
popup	弹出层组件	popup
actionSheet	操作菜单组件	actionSheet
noticeBar	通知栏组件	noticeBar
alertTips	警告提示组件	alertTips
topTips	顶部提示组件	topTips
loadingPopup	加载弹窗组件	loadingPopup
导航组件
组件	说明	文档
navbar	导航栏组件	navbar
tabbar	标签栏组件	tabbar
tabs	标签页组件	tabs
subsection	分段器组件	subsection
pagination	分页组件	pagination
布局组件
组件	说明	文档
layout	布局组件	layout
gap	间距组件	gap
divider	分割线组件	divider
line	线条组件	line
section	区块组件	section
safeAreaInset	安全区域适配组件	safeAreaInset
功能组件
组件	说明	文档
calendar	日历组件	calendar
countDown	倒计时组件	countDown
countTo	数字滚动组件	countTo
backTop	返回顶部组件	backTop
lazyLoad	懒加载组件	lazyLoad
readMore	阅读更多组件	readMore
search	搜索组件	search
swipeAction	滑动操作组件	swipeAction
transition	过渡动画组件	transition
waterfall	瀑布流组件	waterfall
工具函数快速索引
工具	说明	文档
debounce	防抖工具	debounce
deepClone	深拷贝工具	deepClone
deepMerge	深度合并工具	deepMerge
route	路由工具	route
time	时间工具	time
test	测试工具（验证）	test
queryParams	查询参数工具	queryParams
guid	生成GUID工具	guid
random	随机数工具	random
trim	字符串修剪工具	trim
color	颜色值工具	color
colorSwitch	颜色转换工具	colorSwitch
组合式 API 钩子
钩子	说明	文档
useToast	提示钩子	useToast
useModal	模态框钩子	useModal
useTheme	主题管理钩子	useTheme
useLocale	国际化钩子	useLocale
useDebounce	防抖钩子	useDebounce
useThrottle	节流钩子	useThrottle
useColor	颜色管理钩子	useColor
布局模板
布局	说明	文档
login	登录布局	login
address	地址布局	address
citySelect	城市选择布局	citySelect
comment	评论布局	comment
coupon	优惠券布局	coupon
order	订单布局	order
submitBar	提交栏布局	submitBar
menu	菜单布局	menu
keyboardPay	键盘支付布局	keyboardPay
wxCenter	微信中心布局	wxCenter
指南文档
指南	说明	文档
design	设计指南	design
customTheme	自定义主题指南	customTheme
customStyle	自定义样式指南	customStyle
customIcon	自定义图标指南	customIcon
i18n	国际化指南	i18n
faq	常见问题指南	faq
note	注意事项指南	note
使用示例
按钮组件
<template>
  <u-button type="primary" @click="handleClick">主要按钮</u-button>
  <u-button type="success">成功按钮</u-button>
  <u-button type="warning" plain>镂空按钮</u-button>
</template>

表单组件
<template>
  <u-form :model="form" :rules="rules" ref="formRef">
    <u-form-item label="用户名" prop="username">
      <u-input v-model="form.username" placeholder="请输入用户名" />
    </u-form-item>
    <u-form-item label="密码" prop="password">
      <u-input v-model="form.password" type="password" placeholder="请输入密码" />
    </u-form-item>
  </u-form>
</template>

提示组件
<script setup>
import { useToast } from '@/uni_modules/uview-pro'

const toast = useToast()

const showToast = () => {
  toast.show({
    title: '操作成功',
    type: 'success'
  })
}
</script>

完整组件列表
指南类 Skills
codeHint - 代码提示指南
customIcon - 自定义图标指南
customStyle - 自定义样式指南
customTheme - 自定义主题指南
demo - 示例指南
design - 设计指南
faq - 常见问题指南
i18n - 国际化指南
note - 注意事项指南
theme - 主题指南
themeGenerate - 主题生成指南
组件类 Skills
actionSheet - 操作菜单组件
alertTips - 警告提示组件
avatar - 头像组件
avatarCropper - 头像裁剪组件
backTop - 返回顶部组件
badge - 徽章组件
button - 按钮组件
calendar - 日历组件
card - 卡片组件
cell - 单元格组件
checkbox - 复选框组件
circleProgress - 圆形进度条组件
collapse - 折叠面板组件
color - 颜色组件
common - 通用组件
configProvider - 配置提供者组件
countDown - 倒计时组件
countTo - 数字滚动组件
divider - 分割线组件
downloadSetting - 下载设置组件
dropdown - 下拉菜单组件
empty - 空状态组件
fab - 悬浮按钮组件
feature - 特性组件
field - 表单字段组件
form - 表单组件
fullScreen - 全屏组件
gap - 间距组件
grid - 宫格组件
icon - 图标组件
image - 图片组件
indexList - 索引列表组件
input - 输入框组件
install - 安装组件
keyboard - 键盘组件
layout - 布局组件
lazyLoad - 懒加载组件
line - 线条组件
lineProgress - 线性进度条组件
link - 链接组件
loading - 加载组件
loadingPopup - 加载弹窗组件
loadMore - 加载更多组件
mask - 遮罩组件
messageInput - 消息输入组件
modal - 模态框组件
navbar - 导航栏组件
noNetwork - 无网络组件
noticeBar - 通知栏组件
npmSetting - npm设置组件
numberBox - 数字输入框组件
nvue - nvue组件
pagination - 分页组件
picker - 选择器组件
popup - 弹出层组件
quickstart - 快速开始组件
radio - 单选框组件
rate - 评分组件
readMore - 阅读更多组件
safeAreaInset - 安全区域适配组件
search - 搜索组件
section - 区块组件
select - 选择器组件
skeleton - 骨架屏组件
slider - 滑块组件
steps - 步骤组件
sticky - 粘性组件
subsection - 分段器组件
swipeAction - 滑动操作组件
swiper - 轮播组件
switch - 开关组件
tabbar - 标签栏组件
table - 表格组件
tabs - 标签页组件
tabsSwiper - 标签轮播组件
tag - 标签组件
text - 文本组件
textarea - 文本域组件
timeLine - 时间轴组件
toast - 提示组件
topTips - 顶部提示组件
transition - 过渡动画组件
uniModulesSetting - uni_modules设置组件
upload - 上传组件
verificationCode - 验证码组件
vuexDetail - Vuex详情组件
waterfall - 瀑布流组件
工具类 Skills
color - 颜色值工具
colorSwitch - 颜色转换工具
debounce - 防抖工具
deepClone - 深拷贝工具
deepMerge - 深度合并工具
fastUse - 快速使用工具
getRect - 获取元素尺寸工具
guid - 生成GUID工具
md5 - MD5加密工具
mpShare - 小程序分享工具
queryParams - 查询参数工具
random - 随机数工具
randomArray - 随机数组工具
route - 路由工具
test - 测试工具
time - 时间工具
trim - 字符串修剪工具
钩子类 Skills
useColor - 颜色管理钩子
useDebounce - 防抖钩子
useLocale - 国际化钩子
useModal - 模态框钩子
useTheme - 主题管理钩子
useThrottle - 节流钩子
useToast - 提示钩子
布局类 Skills
address - 地址布局
citySelect - 城市选择布局
comment - 评论布局
coupon - 优惠券布局
keyboardPay - 键盘支付布局
login - 登录布局
menu - 菜单布局
order - 订单布局
submitBar - 提交栏布局
wxCenter - 微信中心布局
Weekly Installs
109
Repository
uview-pro/skills
GitHub Stars
7
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass