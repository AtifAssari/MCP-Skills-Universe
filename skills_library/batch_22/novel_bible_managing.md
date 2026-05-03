---
title: novel-bible-managing
url: https://skills.sh/chen893/--skill/novel-bible-managing
---

# novel-bible-managing

skills/chen893/--skill/novel-bible-managing
novel-bible-managing
Installation
$ npx skills add https://github.com/chen893/--skill --skill novel-bible-managing
SKILL.md
小说圣经管理（novel-bible-managing）
目标
把“权威事实（canon）”落到 bible/**，避免设定散落在正文与对话里。
为长篇写作提供稳定锚点：统一 ID、别名、关键标签，便于检索与一致性检查。
默认约束
权威事实只写入 bible/**（必要时同步 continuity/**），不要把设定写进正文当数据库。
任何会影响已写章节的重大改动：登记 decisions/decision-log.md（原因/替代方案/影响范围/回修清单）。
最短路径工作流（新增或修改一个设定条目）

明确实体类型与 ID（前缀固定：char-/loc-/fac-/item-/sys-；后缀使用中文主名，禁止拼音）：

示例：char-林瑶、loc-旧镇、fac-青竹会、item-青铜钥、sys-灵力体系
重名处理：追加短区分后缀（仍用中文）：char-林瑶-剑修 / char-林瑶-二
ID 是稳定引用：后续改显示名时，保持 id 不变，把新旧称呼放进 name/aliases

读取或创建对应文件（推荐文件名直接用 <id>.md）：

人物：bible/characters/char-林瑶.md
地点：bible/locations/loc-旧镇.md
势力：bible/factions/fac-青竹会.md
物品：bible/items/item-青铜钥.md
体系规则：bible/systems/sys-灵力体系.md

命名约定：<name> 取 frontmatter 的 name，并做最小清洗（去除 Windows 不允许字符如 <>:\"/\\|?*）。 若后续改名：必须保持 id 不变；文件名可选跟随改名以提升可读性。

填写最小 frontmatter（强烈建议）：

id（稳定引用）
name（显示名）
aliases（别名/外号/旧译名）
tags（主角/反派/组织/地理/体系等）

写入正文：只保留“会影响创作与一致性”的信息（动机、底线、能力边界、关系、关键历史）。

如新增专名/术语：同步更新 bible/glossary.md（统一写法与解释）。

如改动影响已写内容：在 decisions/decision-log.md 登记，并建议走 novel-retcon-managing 做影响面与回修清单。

输出要求（必须落盘）
更新后的 bible 文件（或新建文件）
如有影响面：decisions/decision-log.md 增量记录
如暴露冲突/不确定：continuity/issues.md 增量记录
模板

需要新建条目时，复制：

assets/character-template.md
assets/location-template.md
assets/faction-template.md
assets/item-template.md
assets/system-template.md
Weekly Installs
11
Repository
chen893/--skill
GitHub Stars
1
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass