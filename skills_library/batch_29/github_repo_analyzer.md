---
title: github-repo-analyzer
url: https://skills.sh/4444zyf/skills/github-repo-analyzer
---

# github-repo-analyzer

skills/4444zyf/skills/github-repo-analyzer
github-repo-analyzer
Installation
$ npx skills add https://github.com/4444zyf/skills --skill github-repo-analyzer
SKILL.md
GitHub 仓库分析器

分析 GitHub 开源仓库，生成结构化的 Markdown 分析报告，支持同步到 Notion。

工作流程
初始化：确认角色
如果你是openclaw：
测试能否连接Open Code, Claude Code或Codex任意之一；如果能连接成功则跳转第三步，否则执行第二步。
如果不能连接，请你先安装acpx插件，通过acp协议，测试连接Open Code, Claude Code或Codex这样的工具。
按照后续要求其执行# 第一步到# 第五步。期间要定时检查任务状态并汇报用户。第六步由你亲自执行。
如果你是Open Code, Claude Code或Codex任意之一，请执行完所有任务。
第一步：获取仓库地址

按需询问用户提供 GitHub 仓库地址。格式示例：

https://github.com/user/repo
github.com/user/repo
user/repo
第二步：Clone 仓库
在现有目录下创建分析工作目录（使用时间戳命名，如 analysis-20240314-123045）
在该目录下创建 repo/ 子目录用于存放 clone 的代码
执行 git clone 命令将仓库 clone 到 repo/ 目录
验证 clone 成功（检查目录非空）
第三步：获取分析要求

询问用户具体的分析要求，例如：

"分析整体架构和模块关系"
"检查代码质量和潜在问题"
"生成 API 接口文档"
"分析安全漏洞"
"评估测试覆盖率"
或用户的自定义需求
第四步：分析仓库

根据用户要求，进行深度分析：

分析策略：

首先探索仓库结构（README、目录结构、主要配置文件）
识别核心模块和入口文件
针对用户要求，深度分析相关代码
记录关键发现、模式、问题
第五步：生成分析报告

在工作目录（与 repo/ 同级）创建以下 Markdown 文档：

analysis-20240314-123045/
├── repo/                    # clone 的仓库代码
├── reports/                 # 分析报告目录
│   ├── 01-主题1.md
│   ├── 02-主题2.md
│   ├── 03-主题3.md
│   └── 04-其他用户要求的主题.md
└── notion-sync.log         # Notion 同步日志（如果启用notion同步脚本）

报告内容规范

01-项目架构概览.md

项目基本信息（名称、描述、技术栈）
目录结构说明
架构模式（MVC、微服务、分层架构等）
关键组件及其关系
依赖关系图（用文字描述）

02-代码质量分析.md

代码规范遵循情况
潜在 bug 或问题
复杂度分析
测试覆盖情况（如有）
改进建议

03-核心模块说明.md

主要模块/包的功能说明
关键类/函数的用途
数据流分析
重要算法或业务逻辑说明
第六步：Notion 同步（可选）

检查 ~/.config/notion/api_key 是否存在：

如果存在，询问用户是否同步到 Notion
如果用户同意，使用 scripts/notion_sync.py 脚本进行同步
支持单文件、目录、递归目录上传
记录同步日志到 notion-sync.log
Notion 同步脚本使用说明

脚本位置: scripts/notion_sync.py

功能特性:

✅ 单文件 Markdown 上传
✅ 目录批量上传（自动创建父页面）
✅ 递归目录上传（保持层级结构）
✅ 分块上传（支持超过 100 个 blocks 的大文件）
✅ 完整的 Markdown 格式支持（代码块、标题、列表、引用等）
✅ 查询可用页面（list 命令）
✅ 获取页面详细信息（info 命令）

使用方法:

# 基本语法
python3 scripts/notion_sync.py <command> [options]

# 列出所有可用页面
python3 scripts/notion_sync.py list

# 搜索特定页面
python3 scripts/notion_sync.py list "My Project"

# 获取页面详细信息
python3 scripts/notion_sync.py info <page_id>

# 上传文件或目录
python3 scripts/notion_sync.py upload <path> <parent_page_id> [title]


命令说明:

命令	说明	示例
list	列出所有可用的父页面	python3 notion_sync.py list
list <query>	搜索特定页面	python3 notion_sync.py list "Reports"
info <page_id>	获取页面详细信息	python3 notion_sync.py info abc123...
upload <path> <page_id>	上传 Markdown 文件或目录	python3 notion_sync.py upload report.md abc123...

示例：

# 1. 列出所有可用页面
python3 scripts/notion_sync.py list

# 2. 搜索特定页面
python3 scripts/notion_sync.py list "My Project"

# 3. 获取页面详细信息
python3 scripts/notion_sync.py info 12345678-1234-1234-1234-123456789abc

# 4. 上传单个文件
python3 scripts/notion_sync.py upload reports/01-架构.md 12345678-1234-1234-1234-123456789abc

# 5. 上传单个文件并指定标题
python3 scripts/notion_sync.py upload reports/01-架构.md 12345678-... "项目架构说明"

# 6. 上传整个目录（会创建目录父页面，子内容作为子页面）
python3 scripts/notion_sync.py upload reports/ 12345678-... "仓库分析报告"

# 7. 目录上传时指定父页面标题
python3 scripts/notion_sync.py upload reports/ 12345678-... "My Analysis Reports"


参数说明:

path: Markdown 文件路径或目录路径（必需）
parent_page_id: Notion 父页面 ID（必需）
title: 自定义标题（可选）
单文件：作为页面标题
目录：作为目录父页面标题，默认使用目录名

Notion 页面结构（目录上传）:

当上传目录时，脚本会创建层级结构：

reports/                          # 本地目录
├── 01-架构.md
├── 02-代码质量.md
├── 03-核心模块.md
└── 详细分析/                     # 子目录
    ├── 数据库设计.md
    └── API设计.md

Notion 结构:
reports (父页面)
├── 01-架构 (子页面)
├── 02-代码质量 (子页面)
├── 03-核心模块 (子页面)
└── 详细分析 (子页面，也是父页)
    ├── 数据库设计 (子子页面)
    └── API设计 (子子页面)


支持的 Markdown 格式:

标题：#、##、###、####
代码块：language ... （自动识别语言）
无序列表：- 或 *
有序列表：1.、2.
引用块：>
分隔线：--- 或 ***
普通段落

分块上传机制: Notion API 限制每次最多 100 个 blocks。对于大文件，脚本会自动：

创建空页面
分批次追加 blocks（每次最多 100 个）
支持无限大小的 Markdown 文件

API 配置:

API 版本: 2022-06-28
认证方式: Bearer Token
配置文件: ~/.config/notion/api_key

错误处理:

API Key 不存在：返回 {"success": false, "error": "..."}
路径不存在：返回错误信息
单文件非 .md 格式：返回错误
API 调用失败：记录到 errors 数组，继续处理其他文件

输出格式: 脚本返回 JSON 格式的结果：

{
  "success": true,
  "synced_files": ["/path/to/file1.md", "/path/to/file2.md"],
  "errors": [],
  "pages_created": [
    {
      "type": "directory",
      "path": "/path/to/reports",
      "notion_page_id": "xxx",
      "url": "https://notion.so/xxx"
    },
    {
      "type": "file",
      "file": "/path/to/file1.md",
      "notion_page_id": "xxx",
      "url": "https://notion.so/xxx",
      "parent_directory": "reports"
    }
  ]
}


技术细节： 如需了解脚本架构、核心函数说明和扩展开发指南，参见 references/notion-sync.md。

第七步：清理（可选）

询问用户是否删除 clone 的仓库：

如果用户选择删除，删除 repo/ 目录但保留 reports/
如果用户选择保留，告知完整路径
重要提示
报告存放位置：分析报告必须放在与 repo/ 同级的 reports/ 目录，不要放在仓库内部
仓库路径：始终使用 /github-analysis/analysis-<timestamp>/ 结构
错误处理：
Clone 失败时（网络问题、仓库不存在、权限问题），提示用户并退出
分析工具不可用时，询问用户是否采用当前会话的工具进行分析
Notion 同步失败时，记录错误但不中断流程
大仓库处理：如果仓库文件数超过 10000，提示用户分析可能需要较长时间
敏感信息：分析报告中如发现 API 密钥、密码等敏感信息，提醒用户注意
输出示例

分析完成后，向用户汇报：

✅ 仓库分析完成！

📁 分析报告位置：/github-analysis/analysis-20240314-123045/reports/

📄 生成文件：
   - 01-项目架构概览.md
   - 02-代码质量分析.md
   - 03-核心模块说明.md

📊 分析摘要：
   - 技术栈：Python/FastAPI + React
   - 代码文件：127 个
   - 主要问题：发现 3 处潜在问题，详见代码质量分析报告

🔄 Notion 同步：已同步到 https://notion.so/xxx（如适用）

❓ 是否删除 clone 的仓库？(y/n)

工具检查

在开始分析前，检查以下工具是否可用：

# 检查 git
command -v git &> /dev/null && echo "git: OK" || echo "git: MISSING"

# 检查 opencode
command -v opencode &> /dev/null && echo "opencode: OK" || echo "opencode: NOT FOUND"

# 检查 claude CLI
command -v claude &> /dev/null && echo "claude: OK" || echo "claude: NOT FOUND"

# 检查 codex
command -v codex &> /dev/null && echo "codex: OK" || echo "codex: NOT FOUND"

# 检查 Notion API 密钥
[ -f ~/.config/notion/api_key ] && echo "notion: CONFIGURED" || echo "notion: NOT CONFIGURED"

Weekly Installs
25
Repository
4444zyf/skills
First Seen
Mar 14, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn