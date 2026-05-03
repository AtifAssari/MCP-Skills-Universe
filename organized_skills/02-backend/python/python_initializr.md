---
rating: ⭐⭐⭐
title: python-initializr
url: https://skills.sh/ynz012x/skills/python-initializr
---

# python-initializr

skills/ynz012x/skills/python-initializr
python-initializr
Installation
$ npx skills add https://github.com/ynz012x/skills --skill python-initializr
SKILL.md
Python 项目初始化
流程概述
确认项目信息 - 与用户交互确认项目名称和 Python 版本
初始化项目 - 使用 uv init 创建项目，启用 git 版本控制
配置代码规范和类型检查 - 使用 pre-commit 管理并初始化代码规范检查 hooks，并应用相应的规范配置；使用 mypy 进行类型检查，创建 PEP-561 类型标记
配置测试框架 - 添加 pytest、pytest-cov 开发依赖
配置版本管理工具 - 配置 .gitignore 优化VCS管理，配置版本元信息，配置 bumpversion 进行语义化版本管理
添加常用开发工具 - 添加 ipython 用于本地调试
安装并验证 - 安装所有依赖并验证配置
更新README - 创建并更新README文件，添加项目使用说明
完成初始提交
Step 1: 确认项目信息

与用户确认以下信息：

项目名称 project_name: 默认使用当前目录名称
项目描述 project_description: 简短的项目描述信息，用于快速理解项目功能和定位
Python 版本 python_version: 推荐使用官方支持的版本（3.10及以上）
Step 2: 初始化项目

使用 uv 初始化项目，启用 git 版本控制：

uv init \
    # 项目名称
    --name={{project_name}} \
    # 项目描述
    --description="{{project_description}}" \
    # 初始化 src/{{project_name}} 包目录
    --package \
    # 初始化 git
    --vcs=git \
    # Python 最低支持版本
    --python={{python_version}}

Step 3: 配置代码规范和类型检查

添加 pre-commit、代码格式化工具和类型检查工具：

uv add --dev pre-commit black flake8 flake8-import-order ruff mypy


将 assets/templates/pre-commit-config.yaml 内容写入项目根目录的 .pre-commit-config.yaml 文件

使用模板 assets/templates/flake8 生成 .flake8 文件

安装 pre-commit hooks：

uv run pre-commit install


创建 PEP-561 类型标记文件（标识该包支持类型检查）：

touch src/{{project_name}}/py.typed


使用模板 assets/templates/pyproject-mypy.toml 生成 mypy 配置，追加到 pyproject.toml

Step 4: 配置测试框架

添加 pytest 和 pytest-cov 开发依赖：

uv add --dev pytest pytest-cov


创建 tests 目录和初始测试文件：

mkdir -p tests
touch tests/__init__.py


使用模板 assets/templates/pyproject-test.toml 生成 pytest 配置，追加到 pyproject.toml

Step 5: 配置版本管理工具

添加 .gitignore

curl https://raw.githubusercontent.com/github/gitignore/refs/heads/main/Python.gitignore -o .gitignore


添加 bumpversion 依赖：

uv add --dev bumpversion


配置版本元信息

使用模板 assets/templates/_version.py 生成 src/{{project_name}}/_version.py

使用模板 assets/templates/init.py 生成 src/{{project_name}}/__init__.py

使用模板 assets/templates/test_version.py 生成 tests/test_version.py

使用模板 assets/templates/bumpversion.cfg 生成 .bumpversion.cfg 文件

Step 6: 添加常用开发工具
uv add --dev ipython

Step 7: 安装并验证

安装所有依赖：

uv sync


验证配置：

# 验证 pytest
uv run pytest

# 验证 pre-commit
uv run pre-commit run --all-files

# 验证 bumpversion
uv run bumpversion --help

# 验证版本元信息
uv run python -c 'from {{project_name}} import __version__; print(__version__)'

# 验证 mypy
uv run mypy src/{{project_name}}/

Step 8: 更新README

使用模板 assets/templates/README.md 生成 README.md 文件

Step 9: 完成初始提交
git add .
git commit -m "Initial project setup"

Weekly Installs
12
Repository
ynz012x/skills
GitHub Stars
1
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn