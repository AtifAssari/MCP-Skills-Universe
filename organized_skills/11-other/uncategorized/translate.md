---
rating: ⭐⭐
title: translate
url: https://skills.sh/sunqb/ccsdk/translate
---

# translate

skills/sunqb/ccsdk/translate
translate
Installation
$ npx skills add https://github.com/sunqb/ccsdk --skill translate
SKILL.md
翻译 - Translate

触发命令: /translate 触发关键词: 翻译、translate、英文、中文、多语言、本地化

简介

多语言翻译技能,支持中英日韩法德西等多种语言互译。提供直译、意译、专业术语、口语化等多种翻译风格,支持翻译后自动润色和去AI化处理。

功能一: Translate Content
Translate Content - 翻译
简介

将文本翻译为目标语言,支持多种翻译风格和场景。翻译完成后可选择调用humanize_text去除AI痕迹。

使用场景
将中文内容翻译为英文,发布到国际平台
将英文内容翻译为中文,供国内用户阅读
多语言内容创作和本地化
支持翻译后润色、改写等组合操作
输入参数
必需参数
source_text (string): 源文本
target_language (string): 目标语言
en - 英文
zh - 中文
ja - 日文
ko - 韩文
fr - 法文
de - 德文
es - 西班牙文
自定义其他语言名称
可选参数

translation_style (string): 翻译风格

literal - 直译 (贴近原文结构)
free - 意译 (更符合目标语言习惯)
professional - 专业术语 (适合学术、商务)
casual - 口语化 (适合社交媒体)
默认值: 根据文本内容自动判断

retain_format (boolean): 是否保留格式

true - 保留原有格式(段落、列表、标题等)
false - 仅翻译内容,调整格式以符合目标语言习惯
默认值: true

auto_humanize (boolean): 翻译后自动去AI味

true - 翻译完成后自动调用humanize_text
false - 不自动去AI味
默认值: false

polish_after_translation (boolean): 翻译后润色

true - 翻译完成后自动调用polish_text
false - 不自动润色
默认值: false
输出

翻译后的文本。如果auto_humanize=true,还将输出去AI味后的版本。

快速模式

当用户输入包含完整的source_text和target_language时,直接使用默认参数执行。

交互问题模板 (简化版)
我将为您翻译这段文本,请确认以下要求:

1. 源文本 (必选):
   请提供需要翻译的文本

2. 目标语言 (必选):
   [1] 英文
   [2] 中文
   [3] 日文
   [4] 韩文
   [5] 法文
   [6] 德文
   [7] 西班牙文
   [8] 其他 (请指定语言名称)

3. 翻译风格 (可选):
   [1] 直译 (贴近原文结构)
   [2] 意译 (更符合目标语言习惯,推荐)
   [3] 专业术语 (适合学术、商务)
   [4] 口语化 (适合社交媒体)

4. 是否保留格式 (可选):
   [1] 保留原有格式
   [2] 仅翻译内容,调整格式

5. 是否去AI味 (可选):
   [1] 不去AI味
   [2] 翻译后自动去AI味

6. 是否润色 (可选):
   [1] 不润色
   [2] 翻译后自动润色

您可以:
- 一次性回复所有信息
- 回复"翻译"或"好的",使用推荐设置执行

请回复:

在其他场景中的触发时机
场景1: 改写为不同渠道内容时

当用户使用rewrite_content生成多渠道内容时,如果用户要求国际化内容:

用户: "帮我改写成英文版本,发到Instagram和TikTok"
→ 自动调用translate_content + target_language=en

场景2: 生成播客文案时

当用户选择播客平台时,如果需要双语版本:

用户: "生成喜马拉雅播客文案,要有中英文版本"
→ 先生成中文版本,然后调用translate_content生成英文版本

场景3: 生成标题或口号时

当用户需要多语言标题:

用户: "生成5个英文标题"
→ 自动调用translate_content + target_language=en

场景4: SEO内容生成时

当用户需要多语言SEO内容:

用户: "生成SEO内容,中英文都要"
→ 先生成中文版本,然后调用translate_content生成英文版本

示例
示例1: 中文翻译为英文

输入:

source_text: "我们公司推出了一款全新的智能办公产品,能够帮助用户提高工作效率,降低运营成本。产品采用人工智能技术,支持多种办公场景,界面简洁友好。"
target_language: "en"
translation_style: "professional"


输出:

【翻译结果】

Our company has launched a brand new smart office product that helps users improve work efficiency and reduce operational costs. The product utilizes artificial intelligence technology, supports various office scenarios, and features a clean and user-friendly interface.

示例2: 英文翻译为中文 (意译+润色)

输入:

source_text: "This innovative solution leverages cutting-edge AI technology to transform how businesses operate, delivering unprecedented efficiency and productivity gains."
target_language: "zh"
translation_style: "free"
polish_after_translation: true


输出:

【翻译结果】

这一创新方案运用了最前沿的人工智能技术,彻底改变了企业的运营方式,带来了前所未有的效率和生产力提升。

【润色后】

这一创新方案运用了最前沿的人工智能技术,彻底改变了企业的运营方式,带来了前所未有的效率和生产力提升。通过智能化的流程优化和自动化操作,企业能够大幅降低成本,提升核心竞争力。

示例3: 中文翻译为英文 (口语化)

输入:

source_text: "这款产品真的太棒了!强烈推荐给大家,用了都说好。"
target_language: "en"
translation_style: "casual"


输出:

【翻译结果】

This product is absolutely amazing! Highly recommend it to everyone, everyone who's tried it loves it!

示例4: 英文翻译为中文 (专业术语)

输入:

source_text: "The system implements machine learning algorithms to optimize data processing workflows and enhance predictive analytics capabilities."
target_language: "zh"
translation_style: "professional"


输出:

【翻译结果】

该系统实施机器学习算法,以优化数据处理工作流程并增强预测分析能力。

注意事项
翻译质量取决于源文本的清晰度和专业性
专业术语的翻译建议使用professional风格
如果内容包含文化背景信息,意译可能更合适
翻译后如需润色,建议设置polish_after_translation=true
参数调整提示

在生成内容后,如果对当前结果不满意,可以尝试调整以下参数:

💡 参数调整选项:

翻译风格: literal直译(贴近原文结构) | free意译(更符合目标语言习惯) | professional专业术语(适合学术、商务) | casual口语化(适合社交媒体)
是否保留格式: true保留原有格式 | false仅翻译内容,调整格式
是否去AI味: false不去AI味 | true翻译后自动去AI味
是否润色: false不润色 | true翻译后自动润色

使用方式: 直接回复如 "改成意译风格" 或 "翻译后自动去AI味"

与其他技能的关联
humanize_text: 翻译后如需去AI味,可配合使用
polish_text: 翻译后如需润色,可配合使用
rewrite_content: 如果需要在翻译后进行风格迁移,可配合使用
generate_script: 生成脚本时如需多语言版本,可配合使用
generate_titles: 生成多语言标题时,可配合使用
配置文件引用
intent_keywords: ["翻译", "translate", "英文", "中文", "多语言", "本地化"]
translation_rules: 在config/translation_rules.json中定义翻译规则和术语库
Weekly Installs
14
Repository
sunqb/ccsdk
GitHub Stars
2
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass