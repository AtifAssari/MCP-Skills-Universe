---
title: modao-capture
url: https://skills.sh/abcfed/claude-marketplace/modao-capture
---

# modao-capture

skills/abcfed/claude-marketplace/modao-capture
modao-capture
Installation
$ npx skills add https://github.com/abcfed/claude-marketplace --skill modao-capture
SKILL.md
Modao-Capture Skill

本 skill 提供墨刀原型稿抓取的 Node.js 脚本工具，使用 Puppeteer 进行浏览器自动化。

环境配置

使用前需要安装依赖：

npm install


系统要求：

Node.js >= 18.0.0
Google Chrome（macOS 自动检测 /Applications/Google Chrome.app）
使用方式
node scripts/modao-capture.js --url "墨刀原型稿链接" --output "项目目录"

命令参数
参数	说明
-u, --url <url>	墨刀原型稿分享链接（必填）
-o, --output <dir>	项目根目录路径（必填）
-c, --concurrency <number>	并发处理数量（默认: 3）
-s, --scale <number>	截图缩放因子 1-5（默认: 3）
使用示例
基本用法
# 抓取原型稿并输出到当前目录
node scripts/modao-capture.js \
    --url "https://modao.cc/proto/abc123/sharing" \
    --output "$(pwd)"

自定义并发和缩放
# 高质量截图（缩放因子 5），并发数 2
node scripts/modao-capture.js \
    --url "https://modao.cc/proto/abc123/sharing" \
    --output "/path/to/project" \
    --scale 5 \
    --concurrency 2

输出结果

执行后会在指定目录下创建 modao_画布名称/ 文件夹，包含：

modao_画布名称/
├── README.md                    # 索引文件
├── 01_首页图1.png              # 页面截图
├── 01_首页.md                  # 页面文档
├── 02_详情页图1.png
├── 02_详情页.md
└── ...

README.md 索引内容
# 墨刀原型稿索引

**项目ID**: abc123
**链接**: https://modao.cc/proto/abc123/sharing

---

## 页面列表

| 序号 | 页面 | 批注数 |
|------|------|--------|
| 1 | [首页](./01_首页.md) | 3 |
| 2 | [详情页](./02_详情页.md) | 0 |

页面文档内容
# 首页

## 原型稿
![首页](./01_首页图1.png)

## 批注内容

### 批注 1

**内容**：
这是第一个批注的说明

---

Claude 使用方式

当用户需要抓取墨刀原型稿时：

检查依赖：确认已安装 node_modules
构建命令：根据需求构建参数
执行脚本：使用 Bash 工具运行
处理结果：解析输出，分析数据

示例工作流：

用户: "抓取这个原型稿 https://modao.cc/proto/xxx/sharing"

Claude:
1. node scripts/modao-capture.js --url "https://modao.cc/proto/xxx/sharing" --output "$(pwd)"
2. 检查输出目录中的 README.md 索引
3. 读取生成的页面文档

文件结构
modao-capture/
├── .gitignore
├── SKILL.md
├── package.json
└── scripts/
    └── modao-capture.js    # 主脚本

Weekly Installs
62
Repository
abcfed/claude-m…ketplace
GitHub Stars
19
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn