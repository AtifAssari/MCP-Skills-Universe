---
title: hermes-agent
url: https://skills.sh/wihy/hermes-agent-skill/hermes-agent
---

# hermes-agent

skills/wihy/hermes-agent-skill/hermes-agent
hermes-agent
Installation
$ npx skills add https://github.com/wihy/hermes-agent-skill --skill hermes-agent
SKILL.md
Hermes Agent Skill v2.0
概述

本 Skill 封装了 NousResearch Hermes Agent 的 CLI 调用能力，让 WorkBuddy/Claw 可以通过 Shell 命令利用 Hermes 的核心功能。

v2.0 改进：完全可移植，无硬编码路径，支持任意实例一键安装。

首次安装
一键安装（推荐）

当检测到 Hermes 未安装时，运行：

# 安装 Hermes Agent（自动克隆、创建虚拟环境、创建 CLI 入口）
bash ~/.workbuddy/skills/hermes-agent/scripts/install_hermes.sh

# 或自定义安装目录
bash ~/.workbuddy/skills/hermes-agent/scripts/install_hermes.sh --prefix ~/custom/path


安装脚本会自动：

✅ 检测 Python 3.11+ 环境
✅ 克隆 Hermes Agent 源码
✅ 创建 Python 虚拟环境并安装依赖
✅ 创建 ~/.local/bin/hermes CLI 入口
✅ 初始化 ~/.hermes/ 配置目录
✅ 生成默认 .env 配置模板
安装后配置 API Key
# 编辑配置文件，填入你的 API Key
nano ~/.hermes/.env


可选提供商（任选其一）：

# 智谱 AI（推荐国内用户）
GLM_API_KEY=your-key-here

# OpenRouter（支持多种模型）
OPENROUTER_API_KEY=sk-or-v1-your-key-here

# Anthropic
ANTHROPIC_API_KEY=sk-ant-your-key-here

# OpenAI
OPENAI_API_KEY=sk-your-key-here

验证安装
# 确认 PATH 包含 hermes
export PATH="$HOME/.local/bin:$PATH"
hermes --version

# 运行诊断
hermes doctor

迁移到其他 Claw 实例

将整个 Skill 目录复制到目标实例即可：

# 在目标实例上执行：
cp -r /path/to/hermes-agent ~/.workbuddy/skills/hermes-agent
bash ~/.workbuddy/skills/hermes-agent/scripts/install_hermes.sh
# 然后配置 API Key

核心工作流
1. 调用模式速查
场景	命令	说明
快速问答	hermes run "问题" --non-interactive --no-stream	最简调用
带上下文	hermes run "问题" --context-file ./ctx.md --non-interactive	注入项目上下文
子代理委托	使用 scripts/hermes_delegate.sh	复杂任务分解
技能查询	hermes skills list	查看已学技能
记忆搜索	hermes memory search "关键词"	检索历史知识
状态检查	hermes status 或 hermes doctor	诊断安装状态
2. CLI 命令完整参考
基础命令
# 启动交互式对话
hermes

# 单轮执行（WorkBuddy 集成首选）
hermes run "prompt" [选项]

# 非交互模式选项
--non-interactive    # 关闭交互式 TUI（必需）
--no-stream          # 禁用流式输出，返回完整结果
--context-file PATH  # 注入上下文文件
--toolset NAME       # 限制使用的工具集
--model MODEL        # 指定模型
--timeout SECONDS    # 超时时间（默认300秒）

子代理委托
# 通过 wrapper 脚本调用（推荐）
./scripts/hermes_delegate.sh \
  --task "分析竞品A和B的产品特性" \
  --tools "web_search,browser,file_write" \
  --timeout 300 \
  --output ./result.md

# 直接在 hermes run 中使用 delegate_task 工具
hermes run '使用delegate_task工具，任务是：分析XXX，工具限制：web_search,browser' \
  --non-interactive --no-stream

记忆管理
# 搜索历史记忆
hermes memory search "关键词"

# 查看所有笔记
hermes memory notes list

# 添加手动笔记
hermes memory notes add "重要发现：..."

# 导出/导入记忆
hermes memory export ./backup/
hermes memory import ./backup/

技能管理
hermes skills list                           # 列出所有技能
hermes skills create my-skill --description "描述"  # 创建新技能
hermes skills edit my-skill                  # 编辑技能
hermes skills remove my-skill                # 删除技能

插件管理
hermes plugins list                    # 列出插件
hermes plugins install user/repo       # 安装插件
hermes plugins enable/disable/update/remove plugin-name

定时任务 (Cron)
hermes cron list                       # 列出定时任务
hermes cron add --name "日报" --cron "0 9 * * *" --message "生成总结"
hermes cron pause/resume/remove TASK_ID

MCP 集成
hermes mcp serve --port 8080           # 启动 MCP Server
hermes mcp connect <server-config>     # 连接外部 MCP 服务

Wrapper 脚本
scripts/hermes_wrapper.sh

统一的 CLI 封装脚本，提供 JSON 格式化输出和错误处理：

./scripts/hermes_wrapper.sh [命令] [参数...]

# 示例
./scripts/hermes_wrapper.sh run "分析内容" --timeout 60
./scripts/hermes_wrapper.sh memory search "关键词"
./scripts/hermes_wrapper.sh status


输出格式：JSON（包含 success, output, error, duration_ms 字段）

scripts/hermes_delegate.sh

子代理委托专用脚本：

./scripts/hermes_delegate.sh --task "任务描述" [选项]

# 可选选项
--tools "tool1,tool2"      # 限制可用工具集
--timeout 300              # 超时时间（秒）
--output ./result.md        # 输出文件路径
--max-concurrent 3         # 最大并发数（默认3）
--context-file ./ctx.md     # 额外上下文文件
-v                         # 详细输出

scripts/install_hermes.sh

一键安装脚本（详见上方「首次安装」章节）：

bash scripts/install_hermes.sh [--skip-deps] [--prefix DIR]

模型配置

运行交互式配置向导：

hermes model


或直接编辑 ~/.hermes/config.yaml：

model:
  provider: zai           # 可选: openrouter, anthropic, openai, zai, gemini 等
  default: "glm-5"        # 默认模型
  base_url: "https://api.z.ai/api/paas/v4"  # 自定义 API 地址


支持的提供商：openrouter, anthropic, openai, gemini, zai, kimi-coding, nous, custom

最佳实践
✅ 推荐做法
始终使用 --non-interactive --no-stream：避免 TUI 阻塞
设置合理的超时时间：简单任务 60s，复杂任务 300s
限制工具集：用 --toolset 减少 Token 消耗
使用上下文文件：将大段背景信息放入文件，而非 prompt 中
错误重试机制：网络问题时自动重试 1-2 次
⚠️ 注意事项
Token 成本：每次调用都有成本
并发限制：最多 3 个并发子代理
超时保护：长时间运行的任务必须设置 timeout
API Key 安全：不要在 Skill 文件中硬编码密钥
Python 版本：确保使用 Python 3.11+
故障排除
问题	解决方案
command not found: hermes	运行 export PATH="$HOME/.local/bin:$PATH" 或重新执行 install_hermes.sh
TypeError: unsupported operand	确保 Python 3.11+
API Key 错误	检查 ~/.hermes/.env 配置
连接超时	检查网络，或更换 LLM 提供商
子代理失败	减少 --max-concurrent 或增加 --timeout
安装脚本失败	运行 hermes doctor 诊断
文件结构
hermes-agent/
├── SKILL.md                    # 本文件（Skill 说明文档）
├── _meta.json                  # Skill 元数据（可移植性声明）
├── scripts/
│   ├── install_hermes.sh       # 一键安装脚本（通用）
│   ├── hermes_wrapper.sh       # 统一 CLI 封装（动态路径检测）
│   └── hermes_delegate.sh      # 子代理委托脚本（动态路径检测）
└── references/                 # 参考文档

更新日志
v2.0.0 (2026-04-12): 完全可移植版 — 移除所有硬编码路径，添加一键安装脚本，支持任意 Claw 实例迁移
v1.0.0 (2026-04-11): 初始版本，支持基础 CLI 调用、子代理委托、记忆/技能管理
Weekly Installs
289
Repository
wihy/hermes-agent-skill
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn