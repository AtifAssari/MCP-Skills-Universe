---
rating: ⭐⭐
title: python-uv-acceleration
url: https://skills.sh/qiao-925/qiao-skills/python-uv-acceleration
---

# python-uv-acceleration

skills/qiao-925/qiao-skills/python-uv-acceleration
python-uv-acceleration
Installation
$ npx skills add https://github.com/qiao-925/qiao-skills --skill python-uv-acceleration
SKILL.md
Python uv 加速

这个 skill-unit 处理的是“Python 环境与依赖工具链”问题。它默认把 uv 作为 pip/venv 工作流的优先实现，但不会强行覆盖项目已存在的完整包管理器。

Instructions
Step 1：先判断适用边界 —— 替代 pip/venv，不替代一切

先看当前项目到底属于哪类情况：

只是需要创建虚拟环境、安装依赖、同步 requirements.txt
现有流程本来就是 pip + venv
新建小型或中型 Python 项目，尚未形成固定工具链

以上情况，默认优先使用 uv。

以下情况不要无脑切到 uv 主导：

项目已稳定使用 poetry、pdm、hatch 等完整项目管理器
团队已有明确工具链约定或 CI 已深度绑定某套命令
当前任务并不是环境/依赖问题，而是 Python 代码实现问题
Step 2：识别项目形态 —— 先看现状再给命令

优先检查这些信号：

requirements.txt
requirements-dev.txt
pyproject.toml
setup.py / setup.cfg
.python-version
仓库脚本、README、CI 文件中的现有安装命令

判断规则：

若项目明显是 pip/venv 工作流，直接给 uv 替代命令。
若项目已有完整管理器，优先沿用该管理器，只在局部可替代环节提到 uv。
若是空白项目或脚本型项目，可直接采用 uv 作为默认工具链。
Step 3：环境创建 —— 默认用 uv venv

当需要创建虚拟环境时，默认使用：

uv venv


常见变体：

uv venv .venv
uv venv --python 3.11


若用户需要激活命令，也一并给出：

source .venv/bin/activate

Step 4：依赖安装 —— 默认用 uv pip

当任务是安装、补齐、同步依赖时，优先给出 uv pip 方案：

uv pip install -r requirements.txt
uv pip install requests
uv pip install -e .


若当前任务强调“与现有 requirements 状态对齐”，优先考虑：

uv pip sync requirements.txt

Step 5：替换表达 —— 给出旧命令到新命令映射

当用户原本说的是 pip、venv、virtualenv，推荐显式给出映射：

旧命令	uv 替代
python -m venv .venv	uv venv
pip install -r requirements.txt	uv pip install -r requirements.txt
pip install package	uv pip install package
pip install -e .	uv pip install -e .
pip freeze	uv pip freeze
pip uninstall package	uv pip uninstall package
Step 6：补齐工程细节 —— 别忘了 .gitignore

如果任务涉及新建环境或初始化项目，检查是否需要补充：

.venv/
venv/
env/
ENV/

Examples
示例 1：把传统 pip/venv 初始化改成 uv
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt

示例 2：新建一个轻量 Python 项目
uv venv
source .venv/bin/activate
uv pip install requests ruff pytest
uv pip freeze > requirements.txt

示例 3：给出迁移说明而不是直接覆盖现有工具链
当前项目已使用 poetry 管理依赖，不建议直接改成 uv 主导。
如果只是想提升局部安装速度，可以先保持现有工具链，再评估是否需要单独引入 uv。

Edge Cases
uv 未安装

如果环境里没有 uv，先提示安装，再继续给后续命令。具体安装方式见 references/common-commands.md。

已有完整项目管理器

如果仓库已经稳定使用 poetry、pdm、hatch 等工具，不要把“默认使用 uv”升级成强制迁移建议。边界判断见 references/adoption-boundaries.md。

需要指定 Python 版本

明确给出：

uv venv --python 3.11

私有包源或额外索引

优先在 uv pip install 中沿用现有索引参数，不要因为换成 uv 就丢失仓库原有安装上下文。

参考资料
references/adoption-boundaries.md - 何时应使用 uv，何时不应强推
references/common-commands.md - 常用命令、安装方式与命令映射
Weekly Installs
19
Repository
qiao-925/qiao-skills
First Seen
Feb 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn