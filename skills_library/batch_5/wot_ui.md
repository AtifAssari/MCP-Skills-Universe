---
title: wot-ui
url: https://skills.sh/wot-ui/wot-starter/wot-ui
---

# wot-ui

skills/wot-ui/wot-starter/wot-ui
wot-ui
Installation
$ npx skills add https://github.com/wot-ui/wot-starter --skill wot-ui
SKILL.md
wot-ui

此技能提供使用 wot-ui 组件库开发应用程序的专业知识。

何时使用

当用户需要以下帮助时使用此技能：

实现特定的 wot-ui 组件（例如，“如何使用 Calendar 日历组件？”）
配置全局 Provider 或主题
排查组件行为问题
查找 props、events 和 slots 的 API 参考
组件参考

references/ 目录包含每个组件的详细文档。当用户询问特定组件时，请检查 references/ 中对应的 markdown 文件。

基础 (Basic)
introduction.md, quick-use.md, common-problems.md, custom-theme.md
button.md, cell.md, config-provider.md, icon.md, img.md, layout.md, popup.md, resize.md, transition.md
表单 (Form)
calendar.md, calendar-view.md
checkbox.md
col-picker.md
datetime-picker.md, datetime-picker-view.md
form.md
input.md, input-number.md, password-input.md, textarea.md
keyboard.md, number-keyboard.md
picker.md, picker-view.md
radio.md
rate.md
search.md
select-picker.md
signature.md
slider.md
switch.md
upload.md, img-cropper.md
slide-verify.md
反馈 (Action)
action-sheet.md, curtain.md, drop-menu.md, overlay.md, popover.md, swipe-action.md
message-box.md, notify.md, toast.md, loading.md
tooltip.md
fab.md, floating-panel.md
展示 (Display)
avatar.md, badge.md, tag.md
card.md, circle.md, divider.md
collapse.md
count-down.md, count-to.md
grid.md, table.md
notice-bar.md, status-tip.md
progress.md, steps.md
segmented.md
skeleton.md
sort-button.md
swiper.md
text.md
tour.md
watermark.md
root-portal.md
gap.md
导航 (Navigation)
backtop.md
index-bar.md
navbar.md
pagination.md
sidebar.md
sticky.md
tabbar.md
tabs.md
组合式函数 (Composables)
use-config-provider.md
use-count-down.md
use-message.md
use-notify.md
use-toast.md
use-upload.md
其他 (Other)
consultation.md
cli-templates.md
locale.md
使用模式
识别组件: 确定用户感兴趣的组件。
查阅参考: 阅读 references/<component-name>.md 中的具体组件文档。
提供示例: 使用文档中的示例来指导用户。确保证严格遵守参考中定义的 API（props, events）。
最佳实践
类型: 使用文档中显示的正确 TypeScript 接口。
v-model: 注意支持 v-model 双向绑定的组件。
事件: 注意某些事件可能具有特定参数（例如 { item, index }）。
Weekly Installs
313
Repository
wot-ui/wot-starter
GitHub Stars
300
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass