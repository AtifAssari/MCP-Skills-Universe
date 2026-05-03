---
title: prd-writer
url: https://skills.sh/springhalu0319/prd-writer-skill/prd-writer
---

# prd-writer

skills/springhalu0319/prd-writer-skill/prd-writer
prd-writer
Installation
$ npx skills add https://github.com/springhalu0319/prd-writer-skill --skill prd-writer
SKILL.md
PRD Writer

产品需求文档撰写 + 原型生成工作流。

工作流程
阶段1：需求采集

整理用户输入（会议记录/需求描述）为结构化格式：

## 核心业务流程
- 🔴 P0 功能名称：功能描述

## 用户端功能  
- 🟡 P1 功能名称：功能描述

## 管理端功能
- 🟢 P2 功能名称：功能描述


优先级：🔴 P0（必须）/ 🟡 P1（重要）/ 🟢 P2（优化）

详细 prompt 模板见 references/prompts.md

阶段2：Feature List

按模块组织功能表格，使用 references/feature-list-template.md

完整性检查：主动指出缺失环节（如有"加购物车"但没"购物车编辑"）

阶段3：PRD 文档

使用 references/prd-template.md 生成完整 PRD。

阶段4：原型生成
Step 1: 生成设计系统
python3 scripts/ui-ux-pro-max/search.py "<产品类型> <风格>" --design-system -p "项目名"


示例：

python3 scripts/ui-ux-pro-max/search.py "travel mobile app" --design-system -p "旅行App"
python3 scripts/ui-ux-pro-max/search.py "SaaS dashboard" --design-system -p "分析平台"

Step 2: 按需获取详细设计数据
# 配色方案
python3 scripts/ui-ux-pro-max/search.py "modern elegant" --domain color

# 字体配对
python3 scripts/ui-ux-pro-max/search.py "professional" --domain typography

# UX 准则
python3 scripts/ui-ux-pro-max/search.py "mobile form" --domain ux

# 技术栈指南
python3 scripts/ui-ux-pro-max/search.py "responsive" --stack html-tailwind


可用 domain: style, color, typography, ux, product, landing, chart 可用 stack: html-tailwind, react, nextjs, vue, svelte, shadcn, swiftui, react-native, flutter

Step 3: 生成 HTML 原型

基于设计系统输出，生成单文件 HTML（Tailwind CSS + 原生 JS）。

技术规格见 references/prototype-guide.md

阶段5：部署（可选）

Cloudflare Pages 部署（国内可访问）：

cd prototype && wrangler pages deploy . --project-name=your-project


详见 references/cloudflare-deploy.md

质量检查

完成后以四角色审视，详见 references/quality-checklist.md：

技术负责人：实现难度、性能、安全
挑剔用户：操作便捷性、流程合理性
运营负责人：数据分析、营销推广
测试工程师：异常场景、边界问题
输出文件
feature_list.md - 功能清单
PRD.md - 完整需求文档
design-system/ - 设计系统
prototype.html - 可交互原型
Weekly Installs
30
Repository
springhalu0319/…er-skill
GitHub Stars
3
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass