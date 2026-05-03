---
title: feishu-wiki
url: https://skills.sh/zephyrwang6/myskill/feishu-wiki
---

# feishu-wiki

skills/zephyrwang6/myskill/feishu-wiki
feishu-wiki
Installation
$ npx skills add https://github.com/zephyrwang6/myskill --skill feishu-wiki
SKILL.md
飞书知识库管理

将 Markdown 文档保存到飞书知识库，支持查看目录结构、指定保存位置、读取多维表格内容。

快速开始
查看目录结构
python scripts/list_wiki.py


输出示例：

📁 草稿箱 (YylJw806IinEJmkwOWVcv8HInph)
  📄 文章标题 (R6wxwODL7iCoQyknQsdcJleanFh)
  📁 分类文件夹 (ZXigwaUIViNr20k9KOKcEKgVnrg)
    📄 子文档 (GdaewKgtEicJcak37QmcgFsMnJc)

保存文档

保存 Markdown 文件到默认位置（草稿箱）：

python scripts/save_to_wiki.py --file /path/to/document.md


保存到指定父节点：

python scripts/save_to_wiki.py --file /path/to/document.md --parent TOKEN


直接指定标题和内容：

python scripts/save_to_wiki.py --title "文档标题" --content "文档内容"

工作流程

当用户请求保存文档到飞书时：

先查看目录结构

运行 list_wiki.py 获取当前知识库目录
向用户展示可选的保存位置

确定保存位置

如果用户指定了位置（如"保存到 xxx 下"），使用对应的 token
如果未指定，默认保存到草稿箱

执行保存

运行 save_to_wiki.py 保存文档
返回文档链接给用户
支持的 Markdown 格式
格式	转换结果
# 标题	一级标题
## 标题	二级标题
### 标题	三级标题
#### 标题	四级标题
普通段落	文本块
- 项目	无序列表
1. 项目	有序列表

粗体、斜体、链接等格式会转换为纯文本。

知识库配置

当前配置的知识库：

根节点: 草稿箱 (YylJw806IinEJmkwOWVcv8HInph)
Space ID: 7591325128043121630

如需修改配置，编辑脚本中的常量。

常见用法示例
用户说	操作
"保存到飞书"	保存当前文档到草稿箱
"保存到飞书的 xxx 目录下"	先查目录获取 token，再保存到指定位置
"查看飞书知识库目录"	运行 list_wiki.py 展示目录结构
"把这篇文章发布到飞书"	保存指定文档到飞书
Weekly Installs
33
Repository
zephyrwang6/myskill
GitHub Stars
281
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketFail
SnykWarn