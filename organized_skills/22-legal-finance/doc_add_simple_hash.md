---
rating: ⭐⭐⭐
title: doc-add-simple-hash
url: https://skills.sh/didi/mpx/doc-add-simple-hash
---

# doc-add-simple-hash

skills/didi/mpx/doc-add-simple-hash
doc-add-simple-hash
Installation
$ npx skills add https://github.com/didi/mpx --skill doc-add-simple-hash
SKILL.md
为文档标题添加简单哈希锚点

当前markdown文档系统支持 {#simple-hash} 的语法来让中文标题的哈希锚点变为简单的英文哈希锚点，例如：

# 文档标题 {#simple-hash}


会生成哈希锚点 #simple-hash，而不是默认的 #文档标题。

需要扫描用户当前文档中的中文标题，根据其中文内容语义通过上述语法生成简单的英文哈希锚点。

特别注意
哈希锚点只能包含小写字母、数字和短横线（-），不能包含空格或其他特殊字符。
哈希锚点不能以短横线开头或结尾。
哈希锚点不能与文档中其他标题的哈希锚点重复。
Weekly Installs
16
Repository
didi/mpx
GitHub Stars
3.9K
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass