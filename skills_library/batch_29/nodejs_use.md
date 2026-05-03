---
title: nodejs-use
url: https://skills.sh/why8023/agent-skills/nodejs-use
---

# nodejs-use

skills/why8023/agent-skills/nodejs-use
nodejs-use
Installation
$ npx skills add https://github.com/why8023/agent-skills --skill nodejs-use
SKILL.md
Node.js 环境管理与版本管理规范

本技能定义 Agent 在使用 Node.js 时必须遵循的统一规范。

默认方案只有一个：使用 mise 管理 Node.js 运行时。不要再把 volta、fnm、nvm 作为正常路径；它们只应出现在老项目迁移步骤里。

工具选型

按以下顺序判断项目当前的 Node.js 版本来源：

mise.toml
.mise.toml
.tool-versions
老项目遗留配置：package.json 里的 volta 字段、.node-version、.nvmrc

执行原则：

发现 mise.toml / .mise.toml / .tool-versions 时，直接以现有 mise 配置为准。
只发现旧配置时，先迁移到 mise，再继续安装依赖或运行命令。
多个来源同时存在且版本不一致时，不要猜测，先停下来向用户确认哪一个才是唯一真相源。
核心规则
规则 1：只用 mise 管理 Node.js 运行时
所有 Node.js 的安装、切换、固定版本、临时执行，都通过 mise 完成。
禁止从 nodejs.org 手动下载安装包覆盖系统环境。
禁止继续引入 volta、fnm、nvm、nvm-windows 作为新方案。
唯一例外：项目已有明确文档要求使用别的工具，且用户显式要求保留。

原因：

mise 支持项目级版本声明、自动切换、跨语言工具链管理。
mise use 会把版本写入配置文件，便于团队协作和 CI 复现。
mise exec 可以在不污染当前 shell 的情况下运行一次性命令。
规则 2：为每个项目提交 Node.js 版本声明
新项目优先提交 mise.toml。
仓库已经统一采用 .tool-versions 时，继续沿用 .tool-versions，不要混出第二套声明。
默认使用模糊版本，例如 20；需要严格复现或升级敏感项目时，使用 --pin 写入精确版本。
版本声明文件必须提交到版本控制。

常用命令：

# 在当前项目写入 Node.js 20.x
mise use node@20

# 写入精确版本
mise use --pin node@20

# 只安装，不改配置
mise install node@20

# 根据当前项目配置安装缺失版本
mise install


mise.toml 示例：

[tools]
node = "20"


精确版本示例：

[tools]
node = "20.19.0"

规则 3：迁移老项目到 mise

发现以下任一旧配置时，执行迁移：

package.json 中的 volta 字段
.node-version
.nvmrc
shell 配置中的 fnm env、volta setup、nvm 初始化代码

迁移流程：

读取旧版本声明，确定当前项目实际使用的 Node.js 版本。
在项目根目录执行 mise use node@<version> 或 mise use --pin node@<version>。
运行 mise install，确认 node -v 与旧项目要求一致。
保留 package.json 中的 packageManager 字段和锁文件，不要因为迁移 Node 管理器而改掉包管理器声明。
如果用户不要求兼容旧工具，删除 .node-version、.nvmrc、package.json.volta 等遗留配置，避免多源冲突。
如果用户明确要求兼容旧工具，再保留旧文件；此时必须注明哪个文件才是主来源，避免后续漂移。

兼容模式说明：

mise 可以读取 .node-version 和 .nvmrc，但这类 idiomatic version files 默认不是全局启用的。
只有在用户明确想保留旧文件作为持续兼容方案时，才建议执行：
mise settings add idiomatic_version_file_enable_tools node

默认仍应把 mise.toml 或 .tool-versions 作为项目主声明，而不是依赖用户本机的全局设置。
规则 4：将“Node 版本”和“包管理器版本”分开管理
mise 负责 Node.js 运行时。
项目依赖必须安装在项目本地目录中，不得使用 npm install -g、yarn global add、pnpm add -g 安装项目依赖。
package.json 的 packageManager 字段负责声明 Yarn / pnpm 等包管理器版本。
在 mise 提供的 Node 环境里启用 Corepack，用它来执行 yarn / pnpm 的版本分发。
锁文件必须提交到版本控制。

推荐做法：

{
  "packageManager": "pnpm@10.11.1"
}

corepack enable
pnpm install


如果项目希望在安装 Node 后自动启用 Corepack，可以在 mise.toml 中写：

[tools]
node = { version = "20", postinstall = "corepack enable" }


补充约束：

Corepack 主要用于 Yarn 和 pnpm；不要假设它会像处理 Yarn / pnpm 那样接管 npm。
npm 项目通常直接使用 Node 自带的 npm；如果项目对 npm 主版本有额外要求，必须在文档或变更中明确说明并验证兼容性。
规则 5：使用 mise 的激活和一次性执行能力
日常开发环境应为当前 shell 启用 mise activate。
无法修改 shell 配置或只想执行单次命令时，使用 mise exec。
运行命令前确认当前目录是项目根目录，避免把配置写错地方。

PowerShell 激活示例：

(& mise activate pwsh) | Out-String | Invoke-Expression


一次性执行示例：

mise exec -- node -v
mise exec -- npm ci
mise exec node@20 -- node script.js

标准命令参考
安装与激活 mise
# Windows: Scoop
scoop install main/mise

# Windows: winget
winget install jdx.mise

# macOS / Linux
curl https://mise.run | sh

# PowerShell profile
New-Item -ItemType File -Force -Path $PROFILE | Out-Null
Add-Content -Path $PROFILE -Value '(& mise activate pwsh) | Out-String | Invoke-Expression'

版本管理
# 在当前项目中写入 Node.js 20.x
mise use node@20

# 写入精确版本
mise use --pin node@20

# 使用全局默认版本
mise use -g node@20

# 安装当前项目中声明的所有工具
mise install

# 只安装某个版本
mise install node@22

# 查看当前激活的 Node.js 版本
mise current node

# 查看当前 node 二进制来自哪里
mise which node
mise which node --version

# 检查 mise 激活和工具链状态
mise doctor

执行命令
# 使用项目配置运行命令
mise exec -- node -v
mise exec -- npm test

# 临时覆盖版本执行
mise exec node@22 -- node -v

标准工作流
1. 新项目
cd my-project
mise use node@20
corepack enable
npm init -y
npm install


如果项目使用 pnpm 或 Yarn，补上 packageManager 字段后再安装依赖。

2. 克隆已有 mise 项目
git clone https://github.com/user/project.git
cd project
mise install
mise exec -- node -v
mise exec -- npm install


如果项目使用 pnpm 或 Yarn，先执行 corepack enable，然后使用项目声明的包管理器安装依赖。

3. 从 volta / fnm / nvm 风格项目迁移
# 例：旧项目原先要求 Node 20.18.1
cd legacy-project
mise use --pin node@20.18.1
mise install
corepack enable
mise exec -- node -v


迁移完成后检查：

package.json 是否还残留 volta 字段
根目录或子项目目录是否仍有 .node-version / .nvmrc
shell 配置是否仍会自动注入 fnm / volta / nvm
锁文件和 packageManager 是否仍与原项目一致
mise doctor 和 mise exec -- node -v 是否通过
常见错误及避免方法
错误 1：继续用旧工具安装或切换 Node.js
# ❌ 错误做法
volta install node@20
fnm use 20
nvm use 20

# ✅ 正确做法
mise use node@20
mise install

错误 2：项目里同时保留多套版本真相源
# ❌ 错误做法
mise.toml
.node-version
.nvmrc
package.json(volta)

# ✅ 正确做法
仅保留一套主来源：
- 新项目优先 mise.toml
- 已采用 .tool-versions 的仓库继续使用 .tool-versions

错误 3：只安装了 mise，却没有激活 shell
# ❌ 错误做法
mise install
node -v

# ✅ 正确做法
(& mise activate pwsh) | Out-String | Invoke-Expression
node -v


如果不想修改当前 shell，就用 mise exec -- node -v。

错误 4：把项目依赖装成全局工具
# ❌ 错误做法
npm install -g typescript
pnpm add -g eslint

# ✅ 正确做法
npm install --save-dev typescript eslint
npx tsc --init

错误 5：迁移 Node 管理器时顺手改坏包管理器
# ❌ 错误做法
# 删除 packageManager 字段
# 删除锁文件
# 从 pnpm 改成 npm

# ✅ 正确做法
# 只迁移 Node 运行时管理方式
# 保留 packageManager 和锁文件
# 在 mise 提供的 Node 环境中继续使用原有包管理器

检查清单

执行 Node.js 相关操作前，确认以下事项：

 当前系统已安装 mise
 当前 shell 已激活 mise，或准备使用 mise exec
 项目是否已有 mise.toml、.mise.toml 或 .tool-versions
 若项目是老项目，是否存在 package.json.volta、.node-version、.nvmrc
 若存在多个版本来源，是否已经确认唯一真相源
 项目依赖是否仍安装在本地目录
 packageManager 和锁文件是否保持一致
参考资源
mise 官方文档
mise Node 文档
mise 安装文档
mise use 命令
Node.js Corepack 文档
Weekly Installs
10
Repository
why8023/agent-skills
First Seen
Feb 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn