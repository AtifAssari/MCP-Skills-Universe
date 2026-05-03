---
title: wechat-article-maker
url: https://skills.sh/alpha-hecoding/awesome-skills/wechat-article-maker
---

# wechat-article-maker

skills/alpha-hecoding/awesome-skills/wechat-article-maker
wechat-article-maker
Installation
$ npx skills add https://github.com/alpha-hecoding/awesome-skills --skill wechat-article-maker
SKILL.md
微信公众号文章创作与发布
语言

匹配用户语言：使用用户所用的语言进行回应。用户用中文则用中文回应，用英文则用英文回应。

目录结构
wechat-article-maker/
├── scripts/                  # TypeScript 源文件
│   ├── wechat-api.ts        # API 发布逻辑
│   ├── wechat-article.ts    # 浏览器发布逻辑
│   ├── wechat-browser.ts    # 图文发布逻辑
│   ├── image-utils.ts       # 图片处理工具（sharp 集成）
│   ├── base64-utils.ts      # Base64 图片提取工具
│   ├── generate-cover.ts    # 封面生成逻辑
│   ├── md-to-wechat.ts      # Markdown 转换逻辑
│   ├── summary-utils.ts     # 文章摘要工具
│   ├── ensure-deps.ts       # 依赖自动安装
│   └── md/                  # Markdown 渲染引擎
│       ├── render.ts
│       ├── themes/          # 主题样式
│       └── extensions/      # 扩展插件
├── templates/                # 🆕 文章创作模板库
│   ├── opening_patterns.md  # 开篇模式库
│   ├── closing_patterns.md  # 结尾模式库
│   ├── language_rules.md    # 语言风格规则
│   └── structure_guide.md   # 结构模板
├── styles/                   # 🆕 文章样式
│   └── base_style.css       # 基础样式
├── examples/                 # 🆕 示例文章
│   ├── beginner_article.html
│   ├── intermediate_article.html
│   └── advanced_article.html
├── references/              # 参考文档
├── SKILL.md                 # 技能文档
├── package.json             # 依赖锁定
└── README.md                # 项目说明


Agent 执行：确定此 SKILL.md 目录为 SKILL_DIR，所有命令通过 npx -y bun 运行：

运行方式
# 设置技能目录
SKILL_DIR="${SKILL_DIR}"

# 所有脚本通过 npx -y bun 运行（跨平台统一）
npx -y bun "${SKILL_DIR}/scripts/wechat-api.ts" article.md --inline-css
npx -y bun "${SKILL_DIR}/scripts/md-to-wechat.ts" article.md --theme grace
npx -y bun "${SKILL_DIR}/scripts/generate-cover.ts" --title "标题" --output cover.jpg


依赖自动安装：脚本首次运行时会自动检测并安装所需依赖，无需手动操作。

依赖安装

自动安装：所有依赖会在脚本首次运行时自动安装，无需手动操作。

运行时要求：

✅ Bun（推荐，通过 npx -y bun 使用）

核心依赖（自动安装）：

front-matter - Frontmatter 解析
highlight.js - 代码高亮
marked - Markdown 渲染引擎
reading-time - 阅读时间计算
juice - CSS 内联转换

可选依赖（封面图生成）：

@napi-rs/canvas - 高性能图片生成
sharp - 图片处理库

依赖说明：

sharp 会在首次运行时通过 scripts/ensure-deps.ts 自动安装
如果可选依赖未安装，generate-cover 会自动生成 SVG 格式的封面图（微信也支持）
功能概述

本技能提供双重能力的微信公众号文章工作流：

模式A：完整创作流程
关键词/URL → AI生成 → HTML → 图片清洗 → 发布

AI 内容生成：基于关键词或链接智能生成文章
模板驱动创作：内置开篇、结尾、语言风格模板
参数化配置：支持长度、深度、风格等多维度配置
模式B：直接发布流程
HTML/MD文件/链接 → 清洗 → 发布（跳过生成）

链接发布模式：下载文章链接，处理并发布
Markdown 转换：内置 Markdown 到 HTML 转换，支持多主题
HTML 直接发布：处理并发布现有 HTML 文件
图片处理：自动下载、清洗元数据、符合微信规范
样式转换：自动将 CSS 转为内联样式
一键发布：支持 API（快速）和浏览器（可视化）两种方式
偏好设置（EXTEND.md）

使用 Bash 检查 EXTEND.md 存在性（优先级顺序）：

# 检查项目级别
test -f .awesome-skills/wechat-article-maker/EXTEND.md && echo "project"

# 检查用户级别（跨平台：$HOME 在 macOS/Linux/WSL 上都可用）
test -f "$HOME/.awesome-skills/wechat-article-maker/EXTEND.md" && echo "user"


┌────────────────────────────────────────────────────────────┬───────────────────┐ │ 路径 │ 位置 │ ├────────────────────────────────────────────────────────────┼───────────────────┤ │ .awesome-skills/wechat-article-maker/EXTEND.md │ 项目目录 │ ├────────────────────────────────────────────────────────────┼───────────────────┤ │ $HOME/.awesome-skills/wechat-article-maker/EXTEND.md │ 用户主目录 │ └────────────────────────────────────────────────────────────┴───────────────────┘

┌───────────┬───────────────────────────────────────────────────────────────────────────┐ │ 结果 │ 操作 │ ├───────────┼───────────────────────────────────────────────────────────────────────────┤ │ 找到 │ 读取、解析、应用设置 │ ├───────────┼───────────────────────────────────────────────────────────────────────────┤ │ 未找到 │ 使用默认值 │ └───────────┴───────────────────────────────────────────────────────────────────────────┘

EXTEND.md 支持：默认主题 | 默认发布方法（api/browser）| 默认作者 | Chrome 配置文件路径

工作流程选择

根据用户输入自动识别并选择工作流程：

输入类型	识别方式	工作流程	是否生成
文本内容	不包含链接，也不是文件路径	流程1：内容创作	✅ 需要生成
文本 + 参考链接	包含链接，但主体是文本描述	流程1：内容创作（含链接分析）	✅ 需要生成
关键词	明确说"写一篇关于X的文章"	流程1：内容创作	✅ 需要生成
单个文章链接	仅包含 URL，或说"发布这篇文章"	流程2：链接发布	❌ 跳过生成
Markdown 文件	以 .md 结尾的文件路径	流程3：Markdown发布	❌ 跳过生成
HTML 文件	以 .html 结尾的文件路径	流程4：HTML发布	❌ 跳过生成
识别示例
用户输入                                    →  自动识别
─────────────────────────────────────────────────────────────
"写一篇关于 Docker 的文章"                   →  流程1（创作）
"帮我生成一篇介绍 MCP 的技术文章"             →  流程1（创作）
"https://blog.example.com/docker-tutorial"   →  流程2（链接发布）
"发布这个链接到公众号：https://..."           →  流程2（链接发布）
"./articles/my-article.md"                   →  流程3（MD发布）
"发布 ./posts/tutorial.html"                 →  流程4（HTML发布）

用户显式指定

如果自动识别不确定，使用 AskUserQuestion 确认：

header: "操作类型"
选项：
- 创作新文章 - 基于输入内容生成文章
- 直接发布 - 跳过生成，直接处理并发布

流程 1: 内容创作与发布（AI生成）

当用户输入文本内容、关键词或带参考链接的内容时使用此流程。

创作进度清单

复制此清单并在完成时勾选：

内容创作进度：
- [ ] 步骤 0: 加载偏好设置
- [ ] 步骤 1: 识别输入类型
- [ ] 步骤 2: 信息收集（关键词/URL）
- [ ] 步骤 3: 询问创作参数
- [ ] 步骤 4: 选择结构模板
- [ ] 步骤 5: 撰写开篇
- [ ] 步骤 6: 撰写主体内容
- [ ] 步骤 7: 撰写结尾
- [ ] 步骤 8: 生成 HTML
- [ ] 步骤 9: 质量检查
- [ ] 步骤 10: 用户确认
- [ ] 步骤 11: 图片处理与发布
- [ ] 步骤 12: 完成报告

步骤 0: 加载偏好设置

检查并加载 EXTEND.md 设置（见上方偏好设置部分）。

步骤 1: 识别输入类型

根据输入内容判断：

关键词输入：用户说"写一篇关于X的文章"
URL 输入：用户提供链接作为参考资料
文本内容：用户提供具体的创作需求
步骤 2: 信息收集
如果是关键词（keyword）
使用 WebSearch 搜索关键词，获取 3-5 篇高质量参考资料
收集信息：
核心概念和定义
主要特性和功能
使用场景和案例
最佳实践和建议
常见问题和解决方案
如果是 URL 链接（url）
使用 WebFetch 读取 URL 内容
提取：
核心观点和主题
文章结构和逻辑
关键信息和数据
代码示例和案例
使用 WebSearch 补充背景知识
步骤 3: 询问创作参数

使用 AskUserQuestion 询问：

文章创作配置

问题1：文章风格
header: "风格"
选项：
- guide（指南型）- 全面系统，多角度讲解（推荐）
- tutorial（教程型）- 步骤清晰，循序渐进
- analysis（分析型）- 深入透彻，对比分析
- story（故事型）- 情境代入，经验分享

问题2：文章长度
header: "长度"
选项：
- short（2000-3000字）- 快速阅读
- medium（3000-5000字）- 平衡深度与可读性（推荐）
- long（5000-8000字）- 深度长文

问题3：技术深度
header: "深度"
选项：
- beginner（入门）- 多用比喻，减少术语
- intermediate（中级）- 平衡理论与实践（推荐）
- advanced（高级）- 深入细节，专业术语

问题4：是否包含代码示例
header: "代码"
选项：
- true - 包含可运行的代码示例
- false - 仅文字描述

问题5：是否进行网络调研
header: "调研"
选项：
- true - 使用 WebSearch 调研关键词（推荐）
- false - 仅基于已有知识生成

步骤 4: 选择结构模板

根据 style 参数选择模板（详见 templates/structure_guide.md）：

guide（指南型）- 最常用：

# [标题]

[开篇引入 - 痛点场景]

---

## 什么是[X]?

[概念介绍 + 比喻说明]

---

## [X]有什么厉害之处?

### [特性1]
[说明 + 实例]

### [特性2]
[说明 + 实例]

### [特性3]
[说明 + 实例]

---

## 怎么使用[X]?

### [方式1]
[详细说明 + 代码示例]

### [方式2]
[详细说明 + 代码示例]

---

## 实战案例

### 案例一：[场景]
[背景 + 问题 + 解决方案 + 效果]

### 案例二：[场景]
[背景 + 问题 + 解决方案 + 效果]

---

## [X]适合谁用?

### 如果你是[角色1]
[适用说明]

### 如果你是[角色2]
[适用说明]

---

## 写在最后

[总结 + 金句 + 互动]


tutorial（教程型）：

# [标题]

[开篇引入 - 痛点场景]

---

## 准备工作

[环境要求]
[前置知识]
[工具安装]

---

## 步骤一：[步骤名称]

[详细说明]
[代码示例]
[注意事项]

---

## 步骤二：[步骤名称]

[详细说明]
[代码示例]
[注意事项]

---

## 常见问题

### 问题1：[问题描述]
[解决方案]

---

## 写在最后

[总结 + 行动号召 + 互动]


analysis（分析型）、story（故事型） 模板详见 templates/structure_guide.md

步骤 5: 撰写开篇

必须遵循模板（详见 templates/opening_patterns.md）：

标准开篇模式：

你有没有遇到过这种情况?

[痛点1: 具体场景描述,用口语化表达]

[痛点2: 具体场景描述,用口语化表达]

[痛点3: 具体场景描述,用口语化表达]

说实话,我之前也是这样。

直到我发现了一个[解决方案]——**[主题]**。

[一句话核心价值说明]。


开篇要求：

必须使用"你有没有遇到过这种情况?"
列举 2-3 个痛点（具体场景，不是抽象描述）
必须包含"说实话，我之前也是这样"
开篇长度：100-150字
步骤 6: 撰写主体内容

语言风格要求（详见 templates/language_rules.md）：

口语化表达（必须）：

使用"说实话"、"其实"、"简单来说"
使用"你"、"我"第一第二人称
短句为主，每句不超过 30 字

比喻和类比（至少 3 个）：

"就像..."、"好比..."
用日常生活事物比喻技术概念

反问句和疑问句（适当使用）

表情符号（每段不超过 2 个）：

✅ ❌ 🔧 💡 🔍 ⚠️

段落撰写规范：

每段 3-5 行，避免大段文字
重要数据单独成段并加粗
金句单独成段，控制在 20 字以内

标题生成规范：

文章标题必须包含以下 5 个特点中的至少 3 个：

特点	说明	示例
痛点明确	直击目标读者的具体困扰	《还在手动改代码？这个工具让你开发效率提升 300%》
数字吸引	用具体数字增加可信度	《我花了 3 个月，整理了 1000 个 Python 技巧》
结果导向	承诺可量化的收益或改变	《学会这招，你的代码审查通过率提升 90%》
情绪调动	激发好奇心、紧迫感或共鸣	《千万别再这样写代码了！后果很严重》
悬念设置	制造悬念引发点击欲望	《99% 的程序员都不知道的调试技巧》
步骤 7: 撰写结尾

必须遵循模板（详见 templates/closing_patterns.md）：

标准结尾模式：

## 写在最后

[总结要点,2-3句]

[价值提炼,1-2句]

> [金句,一句话朗朗上口]

---

💬 **[互动问题]?**

评论区聊聊~

如果这篇文章对你有帮助,点个**在看**让更多人看到吧 👇


结尾要求：

必须有"## 写在最后"标题
总结不超过 150 字
金句朗朗上口，不超过 20 字
必须有互动问题
必须有点赞在看号召
步骤 8: 生成 HTML

输出完整的 HTML 文档，包含内联 CSS 样式（参考 styles/base_style.css）：

<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[文章标题]</title>
    <style>
        body {
            font-family: Optima, "Microsoft YaHei", PingFangSC-regular, serif;
            font-size: 16px;
            line-height: 1.8;
            color: rgb(89, 89, 89);
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }

        h1 {
            font-size: 24px;
            color: rgba(53, 179, 120, 1);
            font-weight: bold;
            margin: 30px 0 15px;
        }

        h2 {
            font-size: 18px;
            color: rgb(255, 255, 255);
            background: rgb(0, 0, 0);
            padding: 2px 10px;
            font-weight: bold;
            margin: 30px 0 15px;
        }

        h3 {
            font-size: 20px;
            color: rgb(53, 179, 120);
            font-weight: bold;
            margin: 30px 0 15px;
        }

        strong {
            color: rgb(53, 179, 120);
            font-weight: bold;
        }

        blockquote {
            margin: 20px 0;
            padding: 10px 10px 10px 20px;
            border-left: 3px solid rgb(53, 179, 120);
            background: rgb(251, 249, 253);
        }

        code {
            font-family: Consolas, Monaco, Menlo, monospace;
            font-size: 14px;
            background: rgba(27, 31, 35, 0.05);
            padding: 2px 4px;
            border-radius: 4px;
            color: rgba(30, 107, 184, 1);
        }

        pre {
            background: #282c34;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            margin: 10px 0;
        }

        pre code {
            background: none;
            padding: 0;
            color: #abb2bf;
        }
    </style>
</head>
<body>

[文章内容,转为HTML标签]

</body>
</html>


⚠️ 重要：代码块格式规范

代码块必须使用标准的 <pre><code> 标签，禁止使用 <section> 或其他标签模拟代码块：

✅ 正确格式：

<pre><code class="language-json">{
  "name": "example"
}</code></pre>


❌ 错误格式（不支持）：

<!-- 禁止使用 section 模拟代码块 -->
<section style="background: #f6f8fa; padding: 15px; ...">
{<br>
  "name": "example"<br>
}
</section>


语言标识：

必须在 <code> 标签上添加 class="language-xxx" 属性
支持的语言：json, jsonc, javascript, typescript, python, bash, go, rust, java, c, cpp, sql 等
示例：<code class="language-python">, <code class="language-bash">

自动化处理：

Markdown 转 HTML：已自动使用标准 <pre><code> 格式（无需手动干预）
非标准格式：wechat-api.ts 会尝试自动识别并转换 background: #f6f8fa 的 <section> 标签
步骤 9: 质量检查

内容检查：

 文章长度符合 length 参数要求
 技术深度符合 depth 参数定位
 文章结构符合 style 参数模板
 所有技术概念准确无误

风格检查：

 开篇使用痛点引入模式
 包含"说实话"等口语化表达
 使用第一人称"我"
 包含至少 3 个比喻或类比
 结尾有金句和互动
 表情符号使用恰当（每段≤2个）

格式检查：

 H2 标题使用正确（黑底白字）
 代码示例有注释说明
 图片有 alt 文本和说明
 HTML 格式完整
 CSS 样式完整

可读性检查：

 句子简短（每句≤30字）
 段落清晰，主题明确
 逻辑连贯，前后一致
步骤 10: 保存文件与用户确认
保存 HTML 文件：
# 生成 slug（文件名）
title="文章标题"
slug=$(echo "$title" | \
  iconv -t ascii//TRANSLIT 2>/dev/null | \
  tr '[:upper:]' '[:lower:]' | \
  tr ' ' '-' | \
  tr -cd '[:alnum:]-' | \
  cut -c1-50)

# 创建目录并保存
output_dir="wechat-articles/$(date +%Y-%m-%d)"
mkdir -p "$output_dir"
echo "$html_content" > "$output_dir/$slug.html"

询问用户下一步：

使用 AskUserQuestion：

header: "下一步"
选项：
- 直接发布 - 转换为微信格式并发布（推荐）
- 修改内容 - 说明需要调整的部分
- 仅保存文件 - 不发布，稍后手动处理

步骤 11: 图片处理与发布

如果用户选择直接发布：

处理图片：

自动下载 HTML 中的远程图片
清洗图片元数据（使用 sharp）
上传到微信素材库

CSS 内联转换（如需要）：

npx -y bun "${SKILL_DIR}/scripts/wechat-api.ts" \
  "$output_dir/$slug.html" \
  --inline-css


准备封面图（强制规则）：

优先级 1：显式指定（frontmatter 中的 featureImage/coverImage）
优先级 2：自动提取文章中第一张图片
优先级 3：自动生成（AI 或脚本）

发布到微信：

API 方式（推荐）
浏览器方式
步骤 12: 完成报告
✓ 微信公众号文章创作与发布完成！

创作信息：
• 输入类型：关键词/URL
• 文章风格：guide
• 文章长度：3500字
• 技术深度：intermediate

发布信息：
• 标题：[标题]
• 封面：自动生成
• 图片：3张（已清洗）

结果：
✓ 草稿已保存到微信公众号
• media_id: [ID]

下一步：
→ 管理草稿：https://mp.weixin.qq.com

生成的文件：
• $output_dir/$slug.html（HTML 文件）

流程 2: 链接文章发布（直接发布）

当用户提供单个文章链接时，跳过生成阶段，直接下载、清洗、发布。

发布进度清单
链接发布进度：
- [ ] 步骤 0: 加载偏好设置
- [ ] 步骤 1: 链接验证
- [ ] 步骤 2: 文章下载与解析
- [ ] 步骤 3: 图片下载与清洗
- [ ] 步骤 4: 样式转换（CSS 内联）
- [ ] 步骤 5: 用户确认
- [ ] 步骤 6: 准备封面图
- [ ] 步骤 7: 执行发布
- [ ] 步骤 8: 完成报告


无生成步骤：直接处理原始内容并发布。

详细步骤

参考原 SKILL.md 流程2（保持不变，从第588行开始）。

流程 3: Markdown 文件发布（直接发布）

当用户提供 .md 文件时，跳过生成阶段，直接渲染、处理、发布。

快速发布
# 一键转换并发布
npx -y bun "${SKILL_DIR}/scripts/md-to-wechat.ts" \
  "$markdown_file" \
  --theme grace \
  --output ./output

# 然后使用 API 发布
npx -y bun "${SKILL_DIR}/scripts/wechat-api.ts" \
  "$html_output" \
  --inline-css \
  --cover "$cover_image"

步骤说明
解析 Markdown：提取 frontmatter（title, author, summary 等）
转换为 HTML：应用主题样式
处理图片：下载远程图片，替换为本地路径
发布：同流程 1 的步骤 11

无生成步骤：直接渲染并发布。

流程 4: HTML 文件直接发布

当用户提供 .html 文件时，跳过所有处理阶段，直接发布。

快速发布
# 直接发布（自动内联 CSS）
npx -y bun "${SKILL_DIR}/scripts/wechat-api.ts" \
  "$html_file" \
  --title "文章标题" \
  --summary "摘要" \
  --cover "$cover_image" \
  --inline-css


注意：必须使用 --inline-css 参数，否则样式会丢失。

无生成步骤：直接发布。

图文发布（图文消息）

用于发布短内容 + 多张图片（最多 9 张）。

使用方法
# 从 Markdown 文件发布
npx -y bun "${SKILL_DIR}/scripts/wechat-browser.ts" \
  --markdown article.md \
  --images ./images/

# 直接指定内容和图片
npx -y bun "${SKILL_DIR}/scripts/wechat-browser.ts" \
  --title "标题" \
  --content "内容" \
  --image img1.png \
  --image img2.png \
  --submit


详见：references/image-text-posting.md

模板库

本技能内置完整的文章创作模板库，位于 templates/ 目录。

开篇模式库

文件：templates/opening_patterns.md

包含 4 种开篇模式：

痛点场景引入（最常用）- 适用于工具介绍、问题解决
对比式引入 - 适用于对比、优化类文章
提问式引入 - 适用于功能介绍、新特性发布
故事式引入 - 适用于案例分析、经验分享
结尾模式库

文件：templates/closing_patterns.md

包含 4 种结尾模式：

价值总结型（最常用）- 总结 + 金句 + 互动
行动号召型 - 强调实践和行动
展望未来型 - 趋势分析、未来展望
要点提炼型 - 知识密集型文章，帮助记忆
语言风格规则

文件：templates/language_rules.md

核心原则：

口语化优先（使用"说实话"、"其实"等）
第一人称叙述（建立情感连接）
大量比喻和类比（降低理解门槛）
反问句和疑问句（增强互动性）
适当表情符号（每段不超过 2 个）
结构模板

文件：templates/structure_guide.md

包含 4 种文章结构的详细模板：

guide（指南型）
tutorial（教程型）
analysis（分析型）
story（故事型）
样式文件

文件：styles/base_style.css

定义文章的统一样式：

主色调：#35B378（绿色）
H1：绿色 24px 加粗
H2：黑底白字 18px
H3：绿色 20px 加粗
正文：15px 深灰，行高 1.8
示例文章

位于 examples/ 目录：

beginner_article.html - 入门深度示例
intermediate_article.html - 中级深度示例
advanced_article.html - 高级深度示例
主题样式

内置三种主题（位于 scripts/md/themes/）：

default - 经典主题
传统排版风格
标题居中，带底边装饰
二级标题：白字彩底
适合：正式文章、行业报告
grace - 优雅主题（推荐）
文字带柔和阴影
圆角卡片式引用块
精致的列表样式
适合：科普文章、个人博客
simple - 简洁主题
现代极简风格
不对称圆角设计
清爽留白
适合：教程、短文
自定义主题
在 scripts/md/themes/ 创建新的 CSS 文件
基于 base.css 扩展样式
使用 --theme <name> 参数应用
配置与环境
环境变量

从以下位置加载配置（优先级从高到低）：

环境变量
<cwd>/.awesome-skills/.env
~/.awesome-skills/.env

必需的环境变量（API 发布方式）：

WECHAT_APP_ID=your_app_id
WECHAT_APP_SECRET=your_app_secret


可选的环境变量：

WECHAT_BROWSER_CHROME_PATH=/path/to/chrome  # 自定义 Chrome 路径

EXTEND.md 配置示例
# wechat-article-maker 配置

## 默认设置

- 主题：grace
- 发布方式：api
- 作者：AI爱好者
- Chrome 配置文件：~/.chrome-wechat

## 自动操作

- 自动生成封面：true
- 自动清洗图片：true
- 自动内联样式：true

技术细节
Markdown 渲染引擎

使用 markdown-it 及扩展（位于 scripts/md/）：

基础渲染：render.ts
扩展插件：
alert.ts - GitHub 风格提示块
footnotes.ts - 脚注支持
katex.ts - 数学公式
toc.ts - 目录生成
infographic.ts - 信息图
ruby.ts - 注音
slider.ts - 滑块
plantuml.ts - UML 图表
图片处理算法

Base64 图片提取（scripts/base64-utils.ts）：

自动检测并处理 HTML 中嵌入的 base64 图片：

智能检测：扫描 HTML 内容，识别 <img src="data:image/...;base64,..."> 格式的图片
自动提取：将 base64 数据解码并保存为本地文件（extracted-images/base64-*.jpg）
路径替换：将 data URI 替换为相对文件路径，便于后续上传到微信
哈希命名：使用 MD5 哈希生成唯一文件名，避免重复和冲突

处理示例：

<!-- 原始 HTML -->
<img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBD..." alt="示例图片">

<!-- 处理后 -->
<img src="extracted-images/base64-0-a1b2c3d4.jpg" alt="示例图片">


元数据清洗（scripts/image-utils.ts）：

内置 sharp 库提供可靠的图片处理能力：

智能检测：扫描图片前 2KB，检测 AIGC/Coze/Adobe 等非标准元数据标记
深度清理：使用 sharp 重新编码 JPEG，彻底移除所有元数据
自动降级：sharp 不可用时，使用手动解析作为后备方案
尺寸优化：自动调整超大图片（限制 1920x1080）以符合微信规范

双引擎清理策略：

方法	优先级	说明
Sharp 重新编码	首选	完全重新编码图片，100% 移除元数据
手动解析	后备	解析 JPEG 段结构，跳过非标准标记

自动重试逻辑：

try {
  await uploadImage(imageBuffer);
} catch (error) {
  if (error.code === 40113) {
    // 强制使用 sharp 深度清理后重试
    const cleanedBuffer = await cleanImage(imageBuffer, true);
    await uploadImage(cleanedBuffer);
  }
}

CSS 内联转换

使用 juice 库将 CSS 规则转换为内联样式：

之前：

<style>
  h1 { color: blue; font-size: 24px; }
</style>
<h1>标题</h1>


之后：

<h1 style="color: blue; font-size: 24px;">标题</h1>


为什么需要：微信公众号编辑器不支持 <style> 标签，只接受内联样式。

封面图生成

方式 1: 多模态大模型生成（推荐）

如果 Agent 具备文生图能力，优先根据文章内容生成定制化封面图。

方式 2: 纯 Node.js（无系统依赖）

脚本：scripts/generate-cover.ts

npx -y bun "${SKILL_DIR}/scripts/generate-cover.ts" \
  --title "文章标题" \
  --output cover.jpg \
  --gradient-start "#667eea" \
  --gradient-end "#764ba2"


特性：

✓ 无需 ImageMagick
✓ 支持多种图片库（@napi-rs/canvas、sharp、SVG）
✓ 自动换行长标题
✓ 可自定义颜色和尺寸
✓ 跨平台（Node.js/Bun）
功能对比
功能	流程1: 内容创作	流程2: 链接发布	流程3: MD发布	流程4: HTML发布	图文发布
输入类型	文本/关键词/URL	单个链接	.md 文件	.html 文件	短文+图片
是否生成	✅ 是	❌ 否	❌ 否	❌ 否	❌ 否
AI创作	✅	❌	❌	❌	❌
内容理解	✅	✅	❌	❌	❌
Markdown转换	✅	❌	✅	❌	✅
主题样式	✅ generator样式	保留原样	✅ 3种主题	保留原样	❌
图片清洗	✅	✅	✅	✅	❌
CSS内联	✅	✅	✅	✅	❌
封面生成	✅	✅	✅	✅	❌
API发布	✅	✅	✅	✅	❌
浏览器发布	✅	✅	✅	✅	✅
适用场景	原创内容	转载/分享	本地文章	现成HTML	图片展示
故障排查
问题	解决方案
依赖未安装	依赖会在首次运行时自动安装
Cannot find module	尝试重新运行命令，会自动安装缺失依赖
封面图生成 SVG 而非 PNG/JPEG	可选依赖未安装，运行 cd ${SKILL_DIR}/scripts && npm install @napi-rs/canvas 或接受 SVG 格式
链接无法访问	检查网络连接，尝试使用代理或 VPN
图片上传失败 (40113)	sharp 自动深度清理元数据后重试，无需手动处理
样式丢失	确保使用了 --inline-css 参数
API 错误 40001	access_token 无效或过期，检查 API 凭证
API 错误 40164 (invalid ip)	在微信公众号后台添加服务器 IP 到白名单：mp.weixin.qq.com → 开发 → 基本配置 → IP白名单
Chrome 未找到	设置环境变量 WECHAT_BROWSER_CHROME_PATH
标题/摘要缺失	手动指定 --title 和 --summary 参数
粘贴失败（浏览器方式）	检查系统剪贴板权限
Markdown 转换错误	检查 Markdown 语法，确保 frontmatter 格式正确
最佳实践
1. 内容创作
✓ 提供清晰的创作意图和目标读者
✓ 引用链接时说明如何使用（深度分析 vs 简要提及）
✓ 预览后再发布，避免返工
✓ 保存源文件，便于后续修改
✓ 标题必须包含至少 3 个特点：痛点明确、数字吸引、结果导向、情绪调动、悬念设置
✓ 段落控制 3-5 行，重要数据单独成段加粗
✓ 金句单独成段，控制在 20 字以内，便于传播
2. 链接发布
✓ 确认链接可访问（避免需要登录的页面）
✓ 检查原文图片质量（模糊图片建议替换）
✓ 优先使用 API 方式（快速可靠）
✓ 发布前预览处理后的 HTML
3. 样式与排版
✓ 专业文章用 default 主题
✓ 大众内容用 grace 主题（推荐）
✓ 教程类用 simple 主题
✓ 确保图片清晰度（推荐 2x 分辨率）
✓ 封面图使用 2:1 比例（900x500px）
4. 发布流程
✓ 首次使用先配置 API 凭证
✓ 发布前在草稿箱预览
✓ 保留源文件（markdown/html）以便后续修改
✓ 定期备份已发布的文章
5. 图片处理
✓ 使用高质量原图（避免二次压缩）
✓ 图片尺寸适中（宽度 800-1200px）
✓ 文件大小控制在 1MB 以内
✓ 如有 AIGC 图片，让脚本自动清洗
使用示例
示例 1: 创作新文章（需要生成）
用户：创作一篇关于 Docker 容器化的文章

Agent：
✓ 识别为内容创作模式
✓ WebSearch 调研关键词
✓ 询问参数
✓ 生成 3500 字文章（guide风格，中级深度）
✓ 转换为 HTML
✓ 清洗图片
✓ 发布到微信

结果：草稿已保存（media_id: abc123...）

示例 2: 发布链接文章（跳过生成）
用户：发布这篇文章到公众号：https://blog.example.com/docker

Agent：
✓ 识别为链接发布模式
✓ 下载文章 HTML 和 3 张图片
✓ 清洗图片元数据
✓ CSS 内联转换
✓ 展示处理结果
✓ 用户确认
✓ 发布到微信

结果：草稿已保存（无生成步骤）

示例 3: 发布 Markdown 文件（跳过生成）
用户：发布 ./articles/docker-tutorial.md

Agent：
✓ 识别为 Markdown 发布模式
✓ 解析 frontmatter
✓ 渲染 HTML（grace 主题）
✓ 下载 2 张远程图片
✓ 自动生成封面
✓ 发布到微信

结果：草稿已保存（无生成步骤）

权限要求
网络访问：获取链接内容、下载图片
文件读写：保存文章、图片和配置
环境变量：读取微信 API 凭证
外部命令：调用 bun/npx 执行 TypeScript 脚本
浏览器（可选）：Chrome 用于浏览器发布方式
依赖与许可
核心依赖
Bun/Node.js：运行 TypeScript 脚本（Node.js >= 18.0.0）
npm/bun：包管理器（用于安装依赖）
自动安装的依赖

脚本会在首次运行时通过 scripts/ensure-deps.ts 自动安装以下依赖：

必需包：

front-matter - Frontmatter 解析
highlight.js - 代码高亮
marked - Markdown 渲染引擎
reading-time - 阅读时间计算
juice - CSS 内联转换库

可选包（封面图生成）：

@napi-rs/canvas - 高性能图片生成
sharp - 图片处理库
运行时依赖（可选）
Chrome/Chromium：浏览器发布方式需要
微信公众号 API 凭证：API 发布方式需要
许可证
Markdown 渲染引擎基于 MIT 许可证
微信公众号 API 使用需遵守微信公众平台服务协议
致谢

本技能整合了以下功能和技术：

wechat-article-generator：AI 文章生成、模板库、样式系统
wechat-article-writer：内容理解与创作
baoyu-post-to-wechat：发布流程与技术实现
Markdown 渲染：基于 marked 及扩展插件
样式主题：参考微信公众号优秀排版实践
图片处理：JPEG 元数据清洗算法
微信 API：官方文档和最佳实践
更新日志
v2.0.0 (2026-03-24)

重大更新：整合 wechat-article-generator 与 wechat-article-maker

✅ 新增 AI 文章生成能力（基于 generator）
✅ 新增模板库（开篇、结尾、语言风格、结构）
✅ 新增参数化配置（长度、深度、风格、代码、调研）
✅ 保留独立发布能力（HTML/MD/链接直接发布）
✅ 优化工作流程识别逻辑
✅ 新增 package.json 依赖锁定
✅ 新增示例文章
v1.0.3 (2026-02-10)
✓ 优化封面图规则：设置为强制逻辑。未指定封面时，若文章中有图则默认使用第一张，仅在文章无图时才生成默认封面。
v1.0.2 (2026-02-10)
✓ 优化配图策略：优先使用多模态大模型生成高质量封面图
✓ 修正 md-to-wechat.ts 脚本支持 --output 参数
v1.0.1 (2026-02-10)
✓ 新增标题生成 5 大原则（痛点明确、数字吸引、结果导向、情绪调动、悬念设置）
✓ 新增文章排版规范（段落结构、配图位置、代码块、金句设计）
✓ 优化内容创作流程，提升文章可读性和传播性
v1.0.0 (2026-02-09)
✓ 整合内容创作和链接发布功能
✓ 内置 Markdown 转 HTML 转换器
✓ 支持三种主题样式（default, grace, simple）
✓ 自动图片元数据清洗
✓ CSS 自动内联转换
✓ 封面图生成（无系统依赖）
✓ API 和浏览器两种发布方式
✓ 完整的工作流程和错误处理

技能版本：2.0.0 最后更新：2026-03-24 作者：整合自 wechat-article-generator、wechat-article-writer 和 baoyu-post-to-wechat

Weekly Installs
121
Repository
alpha-hecoding/…e-skills
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn