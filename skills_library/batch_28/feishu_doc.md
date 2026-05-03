---
title: feishu-doc
url: https://skills.sh/0xranx/agent-kit/feishu-doc
---

# feishu-doc

skills/0xranx/agent-kit/feishu-doc
feishu-doc
Installation
$ npx skills add https://github.com/0xranx/agent-kit --skill feishu-doc
SKILL.md
飞书文档助手

通过 feishu_doc.py 统一管理飞书文档的读取、写入、编辑和知识库操作。

前置条件
Python >= 3.11（feishu-docx 要求）。推荐使用 uv run --python 3.12 或确保系统 Python 版本满足要求
安装依赖：pip install feishu-docx markdown2feishu httpx pyyaml
配置凭证（二选一）：
设置环境变量 FEISHU_APP_ID 和 FEISHU_APP_SECRET
或编辑 skills/feishu-doc/config.yaml
飞书应用需开通权限：docx:document（文档读写）、wiki:wiki（知识库）、im:message（群消息）
环境变量对照表
环境变量	config.yaml 键	说明
FEISHU_APP_ID	app_id	飞书应用 ID（必需）
FEISHU_APP_SECRET	app_secret	飞书应用密钥（必需）
FEISHU_WIKI_SPACE_ID	wiki_space_id	知识库 space_id（知识库写入必需，可通过 wiki-spaces 命令查看）
FEISHU_DEFAULT_PARENT_NODE	default_parent_node	默认父节点 token
FEISHU_NOTIFY_CHAT_ID	notify_chat_id	群消息通知的 chat_id

环境变量优先于 config.yaml 中的配置。

验证连通性：

python skills/feishu-doc/feishu_doc.py test

触发条件

以下情况使用此 Skill：

用户发送了飞书链接（feishu.cn/docx/、feishu.cn/wiki/、feishu.cn/sheets/）
用户说「写到飞书」「同步到知识库」「看一下飞书文档」「发到群里」
用户要求导出、编辑、对比飞书文档内容
读取文档

当用户想查看飞书文档内容时：

python skills/feishu-doc/feishu_doc.py read <URL>                  # 读取文档，输出 Markdown
python skills/feishu-doc/feishu_doc.py read <URL> --with-block-ids  # 带 block_id（编辑前必用）


支持所有飞书文档 URL 格式：/docx/、/wiki/、/sheets/、/base/。

当用户想了解知识库结构时：

python skills/feishu-doc/feishu_doc.py wiki-tree <space_id 或 wiki_URL>  # 树形结构
python skills/feishu-doc/feishu_doc.py export-wiki <space_id 或 wiki_URL> -o ./output  # 批量导出

创建文档

当用户说「写一篇飞书文档」「把这个同步到飞书」时：

python skills/feishu-doc/feishu_doc.py create "标题" -c "Markdown 内容"   # 从内容创建
python skills/feishu-doc/feishu_doc.py create "标题" -f ./report.md       # 从文件创建
python skills/feishu-doc/feishu_doc.py create "标题" -f ./report.md --wiki <parent_node_token>  # 创建到知识库


创建到知识库时，如果权限不足会自动降级为云文档，并提示手动移入。

编辑已有文档

当用户说「改一下这个文档」「把第X段更新成…」时：

第一步 — 读出文档结构（找到要改的块）：

python skills/feishu-doc/feishu_doc.py list-blocks <URL>


输出每个块的 block_id、类型和内容摘要。

第二步 — 精确操作：

python skills/feishu-doc/feishu_doc.py update-block <URL> <block_id> "新内容"   # 改一个块
python skills/feishu-doc/feishu_doc.py delete-block <URL> <block_id>            # 删一个块
python skills/feishu-doc/feishu_doc.py append <URL> -c "追加内容"                # 末尾追加
python skills/feishu-doc/feishu_doc.py overwrite <URL> -f ./new.md              # 清空重写

知识库管理
python skills/feishu-doc/feishu_doc.py wiki-spaces                                    # 列出可访问的知识库（发现 space_id）
python skills/feishu-doc/feishu_doc.py wiki-tree <URL>                                # 查看知识库结构
python skills/feishu-doc/feishu_doc.py wiki-move <文档URL> <目标节点token>              # 云文档移入知识库
python skills/feishu-doc/feishu_doc.py wiki-move <文档URL> <目标节点token> --title "X"  # 移入并设置标题
python skills/feishu-doc/feishu_doc.py wiki-sync <md文件> --parent <节点>              # 同步到知识库（幂等）

权限管理
python skills/feishu-doc/feishu_doc.py permission <URL> editable   # 组织内可编辑
python skills/feishu-doc/feishu_doc.py permission <URL> viewable   # 组织内可查看
python skills/feishu-doc/feishu_doc.py permission <URL> public     # 互联网可查看
python skills/feishu-doc/feishu_doc.py permission <URL> closed     # 关闭链接分享

群消息

当用户说「通知群里」「发到飞书群」时：

python skills/feishu-doc/feishu_doc.py notify "标题" "Markdown内容"   # 发卡片消息
python skills/feishu-doc/feishu_doc.py send "纯文本消息"               # 发文本
python skills/feishu-doc/feishu_doc.py read-chat [N]                  # 读最近 N 条群消息

典型工作流
「帮我看看知识库里有什么」
wiki-tree 列出结构
用 read 读取感兴趣的文档
总结返回
「把这份报告写到知识库运营相关下面」
整理内容为 Markdown，写入临时文件
create --wiki <parent_node> 创建
如果权限不足，自动降级 create（云文档）→ 提示用 wiki-move 迁入
notify 通知群聊
「这个文档第二段数据错了，改成 XXX」
list-blocks <URL> 列出所有块和 block_id
找到目标块
update-block <URL> <block_id> "新内容" 精确更新
「把这篇微信文章转成飞书文档」
import-wechat <微信URL> 抓取转换
返回飞书文档链接
注意事项
知识库写入需要 Bot 被添加为空间「可编辑」成员；公开知识库需人工添加
wiki-move 优先使用 tenant token（Bot 权限），失败后自动尝试 OAuth user token
飞书 API 有限流，工具内置 429 自动重试（指数退避）
wiki-sync 有幂等保护，同名文档不会重复创建
表格超过 9 行会自动拆分成多个连续表格（飞书 API 限制）
卡片消息的内容支持飞书 Markdown（**粗体**、[链接](url)、\n 换行）
Weekly Installs
10
Repository
0xranx/agent-kit
First Seen
Mar 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn