---
rating: ⭐⭐
title: novel-truncator
url: https://skills.sh/vangongwanxiaowan/screen-creative-skills/novel-truncator
---

# novel-truncator

skills/vangongwanxiaowan/screen-creative-skills/novel-truncator
novel-truncator
Installation
$ npx skills add https://github.com/vangongwanxiaowan/screen-creative-skills --skill novel-truncator
SKILL.md
文本截断工具（小说版）
功能

接收文本内容与最大长度限制，智能截断文本，保持内容完整性。

使用场景
对长篇小说文本进行预处理，使其符合长度限制。
在不破坏语义完整性的前提下，截取文本片段。
确保输入到其他智能体的文本不超过其处理能力。
截断原则
优先句子结束: 在句号、问号、感叹号处断开。
其次段落结束: 在空格、换行符处断开。
最后指定长度: 确保不超过设定的最大长度限制。
输入要求
文本内容: 待截断的原始文本（字符串）。
最大长度限制: 目标文本的最大字符数（整数）。
截断标记（可选）: 用于标识文本截断位置的字符串，如 "[...]"。
输出格式
【文本截断报告】

原始长度：[字符数]
截断后长度：[字符数]
截断位置：[位置描述，如：在第 X 句句号处]

截断后的文本：
[文本内容]

约束条件
截断过程应最大限度地保留原文的语义和语境完整性。
严格遵守最大长度限制。
避免在词语中间进行截断。
示例

参见 {baseDir}/references/examples.md 目录获取更多详细示例:

examples.md - 包含不同截断场景（如按句子、按段落、强制截断）的详细示例。
详细文档

参见 {baseDir}/references/examples.md 获取关于文本截断工具的详细指导与案例。

版本历史
版本	日期	变更
2.1.0	2026-01-11	优化 description 字段，使其更精简并符合命令式语言规范；优化功能、使用场景、截断原则、输入要求、输出格式的描述，使其更符合命令式语言规范；添加约束条件、示例和详细文档部分；模型更改为 opus。
2.0.0	2026-01-11	按官方规范重构
1.0.0	2026-01-10	初始版本
Weekly Installs
28
Repository
vangongwanxiaow…e-skills
GitHub Stars
128
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass