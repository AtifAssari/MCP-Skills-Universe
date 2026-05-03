---
title: insight-pdf
url: https://skills.sh/wghust/stark-skills/insight-pdf
---

# insight-pdf

skills/wghust/stark-skills/insight-pdf
insight-pdf
Installation
$ npx skills add https://github.com/wghust/stark-skills --skill insight-pdf
SKILL.md
Insight PDF

企业级报告 PDF 生成 skill。用户项目目录仅生成最终 PDF，无 HTML、node_modules 等中间产物。

完整工作流
设计系统 — 应用 reference 中的配色、字体、网格、封面规范及可视化组件
生成 HTML（内存） — 使用 templates/insight-report.html，替换占位符；正文从 Markdown 转 HTML，使用 ECharts 图表、stat cards、callout boxes、progress bars、timelines 等组件
写入临时目录 — 将 HTML 写入系统临时目录（如 /tmp/insight-pdf-<uuid>/report.html）
调用 convert 脚本 — node <skill-dir>/scripts/convert.js <temp-html-path> <project-dir>/report.pdf
清理 — 转换成功后删除临时目录

用户项目最终只得到 PDF 文件，无其他生成物。

网络与模板依赖

默认 templates/insight-report.html 通过 CDN 加载 Chart.js、ECharts、Google Fonts。转换阶段需能访问外网（或你已把模板改为本地/内网镜像脚本与字体）。纯离线环境若未改模板，可能出现图表空白、超时或版式回退。

安全提示：HTML 由 Agent/用户内容拼装；勿对不可信来源的原始 HTML 直接转换（等同在本地 Chromium 中执行页面脚本）。常规「自己撰写的报告 Markdown→HTML」场景风险可接受。

可视化能力
类型	支持
图表库	ECharts + Chart.js
基础图表	柱状图、折线图、饼图、散点图
高级图表	热力图、雷达图、仪表盘、桑基图
信息图	进度条、对比块、时间线、徽章
数据组件	Stat Cards、Callout Boxes、Enhanced Tables
新增视觉组件
组件	用途
ECharts Charts	高级可视化（热力图、雷达图、仪表盘、桑基图）
Progress Bars	进度可视化，支持渐变填充
Comparison Blocks	并排对比展示关键指标
Timeline	时间线可视化，展示事件流程
Badges	标签徽章，状态标识
Stat Cards	展示关键指标，支持图标、数值、标签
Callout Boxes	高亮重要信息（info/warning/success）
Enhanced Tables	斑马纹表格，专业样式
Gradient Cover	渐变背景封面，装饰性强调条
设计规范引用
维度	规范
配色	主色深蓝 #1e3a5f，8色图表调色板，强调色 #0ea5e9
字体	标题 serif（Libre Baskerville/Georgia），正文 sans-serif（Source Sans 3/Inter）
封面	渐变背景、装饰性强调条、专业排版
图表	ECharts 扁平配置、无动画、设计系统配色
布局	模块化网格、信息图组件、清晰层级
首次安装（在 skill 目录，非项目目录）
cd skills/insight-pdf   # 或 ~/.cursor/skills/insight-pdf
npm install


package.json 含 postinstall：会在安装后尝试拉取 Playwright Chromium。若未成功，再执行：npx playwright install chromium。详见 USAGE.md。

Agent 执行示例
生成完整 HTML 内容（参考 templates/insight-report.html 与 reference）
写入临时目录：
TEMP_DIR=$(mktemp -d)/insight-pdf-$$; mkdir -p "$TEMP_DIR"
# 将 HTML 写入 $TEMP_DIR/report.html

调用转换（skill 目录路径需为绝对路径）：
node /path/to/skills/insight-pdf/scripts/convert.js "$TEMP_DIR/report.html" "$(pwd)/report.pdf"

删除临时目录：rm -rf "$TEMP_DIR"
依赖缺失时

若转换失败且错误提示 Chromium 未安装，引导用户到 skill 目录（非项目目录）执行 npm install，必要时 npx playwright install chromium。详见 USAGE.md。

Weekly Installs
16
Repository
wghust/stark-skills
GitHub Stars
4
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn