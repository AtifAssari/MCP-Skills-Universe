---
title: tech-article-image
url: https://skills.sh/zd-ai-lab/tech-article-illustration-master/tech-article-image
---

# tech-article-image

skills/zd-ai-lab/tech-article-illustration-master/tech-article-image
tech-article-image
Installation
$ npx skills add https://github.com/zd-ai-lab/tech-article-illustration-master --skill tech-article-image
SKILL.md
技术文章配图生成器

为技术类文章生成高质量、有辨识度、无AI塑料感的主题配图。

核心原则

拒绝AI典型病：

禁止：塑料感、光污染、发光大脑、霓虹泛滥、过度渲染
追求：物理质感、摄影真实性、特定艺术流派的纯粹性
工作流程
第一步：分析 → 选风格 → 写提示词

提取核心要素

文章主题（技术领域、具体产品/概念）
情绪基调（客观分析/人文叙事/硬核深度/未来展望/哲学思考）
视觉意象（文章中可视觉化的核心概念）

匹配风格 根据情绪基调选择，详见 references/styles.md：

理性与精确 → 瑞士设计、等轴测、专利、绘图仪、ASCII
人文与叙事 → 孔版印刷、科技黑色漫画、达芬奇手稿、拼贴、版画
工业力量 → 粗野主义、点画、X光、平铺、蓝晒
数字原生 → 1-Bit像素、故障艺术、低多边形、合成波、激光雷达
美学与愿景 → 热成像、纸雕、太阳朋克、包豪斯、现代水墨

构建提示词

[风格名称 + 核心视觉特征]. [文章核心意象的具体描述]. [材质/纹理细节]. [色彩方案]. No text, no watermark, no plastic texture, no lens flare.


输出给用户确认

推荐风格（中英文名称）
风格简介（1-2句，解释这是什么风格）
选择理由（为什么适合这篇文章）
英文提示词
中文提示词
第二步：生成图像

环境检测与执行：

情况A：MCP生图工具可用

如果环境中存在 mcp-image:generate_image 工具，用户确认后直接调用：

{
  "name": "mcp-image:generate_image",
  "parameters": {
    "prompt": "[英文提示词]",
    "aspectRatio": "16:9",
    "imageSize": "2K",
    "purpose": "Tech article hero image"
  }
}

情况B：无MCP生图工具

输出完整提示词（中英双语）+ 提示词结构解释，格式如下：

📷 生成提示词

英文版（推荐用于 Midjourney / DALL-E / Stable Diffusion）：

[完整英文提示词]


中文版（参考理解）：

[中文翻译]


🔍 提示词结构解析：

组成部分	内容	作用
风格声明	[如：Algorithmic plotter art]	锁定整体视觉语言，避免AI默认的"通用科技风"
核心意象	[如：neural network topology]	将文章抽象概念转化为可视觉化的具体画面
材质/纹理	[如：fine black ink lines on textured white paper]	赋予物理质感，消除AI图像的"塑料感"
氛围词	[如：Mathematical precision, computational beauty]	微调情绪，引导模型理解画面气质
负向约束	[如：No text, no watermark, no plastic texture]	排除常见AI图像病（光污染、水印、假文字）

💡 修改建议：

换风格：替换"风格声明"部分，参考25种风格库
换意象：修改"核心意象"，贴合你的文章具体内容
调氛围：增减"氛围词"改变画面情绪（如加 "dramatic contrast" 增强冲击）

🛠 生图工具参数建议：

工具	推荐设置
Midjourney	--ar 16:9 --v 6 --style raw
DALL-E	横版、HD模式、Natural风格
Stable Diffusion	CFG 7-9, Steps 30+

💡 提示： 如需在 Claude 中直接生图，可配置支持图像生成的 MCP 工具。配置后再次使用本skill将自动调用生图，无需手动复制提示词。

风格速查表
情绪	推荐风格	典型场景
战略分析	瑞士设计、包豪斯	行业趋势、宏观报告
技术架构	等轴测、X光	系统设计、深度拆解
硬件评测	专利、平铺、X光	芯片分析、供应链
算法原理	绘图仪、现代水墨	数学模型、神经网络
代码/安全	ASCII、版画	极客文化、网络安全
行业观察	孔版印刷、拼贴	带温度的分析、冲突
未来预测	科技黑色漫画、合成波	自动驾驶、未来城市
概念创新	达芬奇手稿	从0到1、原型设计
基础设施	粗野主义、蓝晒	数据中心、云计算
人物特写	点画	CEO专访、商业领袖
元宇宙/VR	低多边形、激光雷达	空间计算、数字孪生
系统故障	故障艺术	AI幻觉、Bug分析
能效/热度	热成像	散热评测、市场热度
层级结构	纸雕	软件栈、数据库
绿色科技	太阳朋克	碳中和、可持续
东方战略	现代水墨	万物互联、禅意科技
宽高比选择
用途	推荐比例	说明
微信公众号封面	16:9	标准横版
网站文章题图	16:9 或 21:9	宽幅更有冲击力
社交媒体	1:1	Instagram、微博
竖版/手机	9:16	Stories、手机壁纸
PPT封面	16:9	演示文稿标准
详细风格参考

完整的25种风格说明、关键词、适用场景和代表性提示词模板，见 references/styles.md。

完整示例

输入： 一篇关于大模型推理优化的技术文章

第一步输出：

推荐风格：绘图仪生成艺术 (Algorithmic Plotter Art)

风格简介： 模拟机械绘图仪用数学公式驱动笔尖绘制的艺术。特点是精密的细线交织、摩尔纹干涉图案、纯粹的黑白墨线在纸上的物理质感。

选择理由： 推理优化本质是数学与算法的极致追求，绘图仪风格的数学美感与摩尔纹视觉完美契合"优化"这一核心概念。

英文提示词：

Algorithmic plotter art. A generative art piece featuring dense intersecting fine black ink lines forming a neural network topology with flowing optimization gradients, creating geometric moiré interference patterns on textured white paper. Mathematical precision, computational beauty. No text, no watermark, no plastic texture, no lens flare.


中文提示词：

算法绘图仪艺术。一幅生成艺术作品，由密集交叉的精细黑色墨线构成神经网络拓扑结构，流动的优化梯度形成几何摩尔纹干涉图案，绘于有纹理的白纸上。数学的精确，计算的美感。无文字，无水印，无塑料质感，无镜头光晕。


确认后我将为您生成图像（或提供详细的生图工具参数）。

用户确认 → 第二步输出（无MCP时）：

📷 生成提示词

英文版：

Algorithmic plotter art. A generative art piece featuring dense intersecting fine black ink lines forming a neural network topology with flowing optimization gradients, creating geometric moiré interference patterns on textured white paper. Mathematical precision, computational beauty. No text, no watermark, no plastic texture, no lens flare.


中文版：

算法绘图仪艺术。一幅生成艺术作品，由密集交叉的精细黑色墨线构成神经网络拓扑结构，流动的优化梯度形成几何摩尔纹干涉图案，绘于有纹理的白纸上。数学的精确，计算的美感。无文字，无水印，无塑料质感，无镜头光晕。


🔍 提示词结构解析：

组成部分	本例内容	作用
风格声明	Algorithmic plotter art	锁定"绘图仪生成艺术"视觉语言
核心意象	neural network topology with flowing optimization gradients	将"推理优化"转化为"网络拓扑+梯度流动"
材质/纹理	fine black ink lines on textured white paper	墨线+纸张质感，消除数字塑料感
视觉效果	geometric moiré interference patterns	摩尔纹增强数学美感
氛围词	Mathematical precision, computational beauty	强调理性、精确的情绪基调
负向约束	No text, no watermark, no plastic texture, no lens flare	排除AI图像常见问题

💡 修改建议：

如果文章更偏"性能提升"，可将意象改为 "accelerating data streams through optimized pathways"
如果想要更抽象，删除 "neural network"，保留纯粹的线条交织

🛠 生图工具参数：

Midjourney: --ar 16:9 --v 6 --style raw
DALL-E: 横版、HD、Natural风格
Weekly Installs
12
Repository
zd-ai-lab/tech-…n-master
GitHub Stars
19
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass