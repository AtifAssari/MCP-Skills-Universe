---
rating: ⭐⭐⭐
title: workspace-setup
url: https://skills.sh/anian0/pick-skills/workspace-setup
---

# workspace-setup

skills/anian0/pick-skills/workspace-setup
workspace-setup
Installation
$ npx skills add https://github.com/anian0/pick-skills --skill workspace-setup
SKILL.md
Workspace Setup Skill

快速配置和管理项目工作区，提供标准化版本目录结构、配置文件同步、技能管理等功能。

目录结构规范
项目根目录/
├── skillconfig.json       ← 配置文件
├── CLAUDE.md              ← Claude配置（可从filebrowser下载）
├── AGENTS.md              ← Agents配置（可从filebrowser下载）
├── workplace/
│   ├── 1.0/               ← 当前版本目录
│   │   ├── requirements/  ← 需求文档
│   │   ├── references/    ← 参考文档
│   │   ├── prototypes/    ← 原型设计
│   │   ├── tech-design/   ← 技术方案
│   │   ├── plan/          ← 实施计划
│   │   └── tests/         ← 测试文件
│   ├── 1.1/               ← 新版本（版本升级时创建）
│   └── archive/           ← 归档目录
│       └── 1.0/           ← 已完成版本归档
└── .agents/
    └── skills/
        └── workspace-setup/
            └── SKILL.md

配置文件
skillconfig.json 格式
{
  "workspace": {
    "config_pack": "config-1",
    "current_version": "1.0",
    "workplace_dir": "workplace"
  },
  "filebrowser": {
    "instance_url": "http://your-server:8080",
    "username": "admin",
    "password": "your-password",
    "remote_base_path": "/config"
  }
}

配置字段说明
字段	类型	必填	说明
config_pack	string	是	云端配置包名称，如 config-1、config-2
current_version	string	是	当前版本号，如 1.0、1.1
workplace_dir	string	否	工作目录名，默认 workplace
instance_url	string	是	FileBrowser 服务地址
username	string	是	登录用户名
password	string	是	登录密码
remote_base_path	string	否	云端顶层目录，默认 /config
云端配置包库

FileBrowser 服务器上存储多套预设配置包，项目选择其中一套下载使用。

云端目录结构：

/config/                      ← remote_base_path（顶层目录）
├── config-1/                 ← 配置包1（如：React项目通用配置）
│   ├── CLAUDE.md             ← 配置文件（下载到项目根目录）
│   ├── AGENTS.md             ← 配置文件（下载到项目根目录）
│   └── skills/               ← skills目录（和配置文件平级）
│       └── xxx-skill/
├── config-2/                 ← 配置包2（如：Python项目通用配置）
│   ├── CLAUDE.md
│   ├── AGENTS.md
│   └── skills/
└── config-3/                 ← 配置包3
    └── ...


下载到本地后：

项目根目录/
├── CLAUDE.md          ← 从 /config/config-1/CLAUDE.md 下载
├── AGENTS.md          ← 从 /config/config-1/AGENTS.md 下载
└── skills/            ← 从 /config/config-1/skills/ 下载
    └── xxx-skill/


路径规则：云端路径 = {remote_base_path}/{config_pack}/文件名

脚本工具

按需读取对应的脚本说明。

脚本	文档	功能
init_workspace.py	references/init-workspace.md	初始化工作区、下载配置文件
sync_config.py	references/sync-config.md	同步CLAUDE.md/AGENTS.md
version_manager.py	references/version-manager.md	创建版本、归档版本
skills_manager.py	references/skills-manager.md	管理npx skills命令
快速命令
初始化工作区
python scripts/init_workspace.py --config skillconfig.json


下载CLAUDE.md、AGENTS.md，创建workplace目录和当前版本目录结构。

同步配置文件
# 上传配置文件到 filebrowser
python scripts/sync_config.py upload --config skillconfig.json

# 上传配置文件和skills目录
python scripts/sync_config.py upload --config skillconfig.json --sync-skills

# 从 filebrowser 下载配置文件
python scripts/sync_config.py download --config skillconfig.json

# 下载配置文件和skills目录
python scripts/sync_config.py download --config skillconfig.json --sync-skills

# 双向同步（检查变更）
python scripts/sync_config.py sync --config skillconfig.json

版本管理
# 创建新版本（如从1.0升级到1.1）
python scripts/version_manager.py create --config skillconfig.json

# 归档当前版本到archive
python scripts/version_manager.py archive --config skillconfig.json

# 查看版本状态
python scripts/version_manager.py status --config skillconfig.json

技能管理
# 搜索技能
python scripts/skills_manager.py find "react testing"

# 安装技能
python scripts/skills_manager.py add "vercel-labs/agent-skills@react-best-practices"

# 检查更新
python scripts/skills_manager.py check

# 更新所有技能
python scripts/skills_manager.py update

工作流程
1. 新项目初始化
创建 skillconfig.json 配置文件
运行 init_workspace.py 初始化工作区
配置文件自动从filebrowser下载（如果存在）
workplace目录和版本结构自动创建
2. 日常配置同步
修改CLAUDE.md/AGENTS.md后，运行 sync_config.py upload 上传
需要最新配置时，运行 sync_config.py download 下载
定期运行 sync_config.py sync 保持同步
3. 版本迭代
完成当前版本开发后，运行 version_manager.py create 创建新版本
新版本目录自动创建，版本号自动递增（1.0 → 1.1）
完成最终版本时，运行 version_manager.py archive 归档
4. 技能安装

使用 skills_manager.py 或直接运行npx skills命令：

npx skills find [query] - 搜索
npx skills add <package> -g -y - 安装
npx skills check - 检查更新
npx skills update - 更新
版本子目录说明
目录	用途	典型内容
requirements/	需求文档	需求说明、用户故事、验收标准
references/	参考文档	API文档、设计规范、参考资料
prototypes/	原型设计	UI原型、流程图、架构图
tech-design/	技术方案	技术选型、架构设计、数据库设计
plan/	实施计划	任务分解、里程碑、进度跟踪
tests/	测试文件	测试计划、测试用例、测试报告
常见错误
错误	说明	处理
配置文件缺失	skillconfig.json不存在	手动创建配置文件
登录失败	filebrowser认证失败	检查用户名密码
远程路径不存在	filebrowser上无对应文件	检查remote_base_path和skill_name
版本目录已存在	目标版本已创建	使用archive先归档旧版本
Weekly Installs
8
Repository
anian0/pick-skills
First Seen
11 days ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn