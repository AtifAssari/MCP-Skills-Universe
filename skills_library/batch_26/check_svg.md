---
title: check-svg
url: https://skills.sh/forge-town/skills/check-svg
---

# check-svg

skills/forge-town/skills/check-svg
check-svg
Installation
$ npx skills add https://github.com/forge-town/skills --skill check-svg
SKILL.md
SVG 组件检查
使用说明
扫描组件文件，用正则 <svg[^>]*>[\s\S]*?<\/svg> 检测内联 <svg> 标签
发现违规时，将内联 SVG 提取为 IconName.tsx（PascalCase），放入 components/icons/，原处改为 import + <IconName />
迁移时将 width/height/fill/className 等属性改为 props

规范： 禁止在业务组件中内联 <svg>；所有图标必须封装为独立组件并通过 import 使用

参考： 具体迁移流程见 svg-icon-best-practice

Weekly Installs
15
Repository
forge-town/skills
GitHub Stars
1
First Seen
Feb 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass