---
rating: ⭐⭐⭐
title: notebooklm-ppt-designer
url: https://skills.sh/orangon/learning2peak/notebooklm-ppt-designer
---

# notebooklm-ppt-designer

skills/orangon/learning2peak/notebooklm-ppt-designer
notebooklm-ppt-designer
Installation
$ npx skills add https://github.com/orangon/learning2peak --skill notebooklm-ppt-designer
SKILL.md
NotebookLM PPT设计大师

将用户内容素材转化为可直接执行的PPT设计方案，支持TED演讲级信息架构和Apple Keynote风格极简美学。

核心能力
TED演讲级信息架构设计
Apple Keynote风格极简美学
品牌视觉规范精确执行
结构化设计文档输出
工作流程
步骤1：识别输入类型
输入类型	判断标准	处理方式
完整讲稿	超过500字，有段落结构	直接提取观点 → 生成设计
主题词	少于50字，无结构	先询问细节 → 生成大纲 → 确认后设计
内容大纲	有明确的1/2/3条目	直接进入设计阶段
步骤2：构建PPT结构

标准演示结构：

Page 01: 标题页 → 主题+副标题+品牌标识
Page 02: 背景页 → 建立共鸣，引出话题
Page 03~N-1: 内容页 → 每页一个核心观点
Page N: 总结页 → 核心金句+行动号召
步骤3：选择视觉形式

根据内容类型选择最佳视觉形式（详见 references/visual-forms.md）：

内容类型	最佳视觉形式
对比/演进	箭头流程图
并列选项	横向卡片组
层级递进	金字塔/阶梯
维度展示	左侧竖线+列表
数据强调	大数字+说明
金句/总结	居中引用框
步骤4：生成设计方案

为每页生成完整设计参数：

设计思路（目标、策略、视觉形式）
ASCII布局示意图
YAML格式精确参数（位置、字体、颜色、尺寸）
品牌视觉规范

如用户提供品牌规范文档，严格遵循。否则使用默认极简风格。

默认配色：

背景: #000000 纯黑
强调: #00FF94 荧光绿（仅占3-5%）
主文字: #FFFFFF 纯白
次要: #CCCCCC 浅灰
弱化: #808080 中灰

默认布局：

画布: 1920×1080px (16:9)
外边距: 60px
留白: 55-60%
网格: 8px单位

详细规范见 references/brand-defaults.md

输出格式
项目概览
| 项目 | 信息 |
|-----|-----|
| 项目标题 | [标题] |
| 目标受众 | [受众] |
| 演讲时长 | [X-X分钟] |
| 总页数 | [N]页 |

单页设计
### Page [XX] - [页面标题]

#### 💡 设计思路
- 目标：[3秒内传达什么]
- 视觉形式：[选择的形式]

#### 📐 布局结构
[ASCII示意图]

#### 🎯 设计参数
[YAML格式参数]


完整模板见 references/output-templates.md

交互模式
主题词输入

仅提供主题词时，先确认：

目标受众
演讲场景
预期页数
核心要点

然后提供大纲草案，确认后生成设计。

讲稿输入

分析讲稿，提取：

核心观点列表
建议视觉形式
PPT结构方案

确认后生成完整设计文档。

Gamma Pro适配

需要Gamma Pro指令时，在末尾添加简化英文格式。详见 references/gamma-pro-format.md

质量检查
 页面背景统一
 强调色≤5%
 留白55-60%
 每页一个核心观点
 间距8px倍数
 参数可直接执行
Weekly Installs
50
Repository
orangon/learning2peak
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass