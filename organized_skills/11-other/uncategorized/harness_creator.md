---
rating: ⭐⭐⭐
title: harness-creator
url: https://skills.sh/fanlw0816/harness-creator/harness-creator
---

# harness-creator

skills/fanlw0816/harness-creator/harness-creator
harness-creator
Installation
$ npx skills add https://github.com/fanlw0816/harness-creator --skill harness-creator
SKILL.md
Harness Creator

Generate a customized Claude Code harness framework for your project with Fusion Architecture: GAN-inspired multi-agent system + Domain Specialists.

Quick Start
/harness-creator [target-dir]

With argument: Use specified directory
Without argument: Ask for target directory
New project (0→1): Full brainstorm flow
Existing project (1→N): Auto-analyze and quick setup
Fusion Architecture
Core Pattern: GAN-Inspired Multi-Agent
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Planner   │ ──► │  Generator  │ ──► │  Evaluator  │
│  (Plans)    │     │ (Implements)│     │  (Grades)   │
└─────────────┘     └──────┬──────┘     └─────────────┘
                           │
                    spawns specialists
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
        ┌──────────┐ ┌──────────┐ ┌──────────┐
        │ frontend │ │   api    │ │ database │
        │   -dev   │ │   -dev   │ │   -dev   │
        └──────────┘ └──────────┘ └──────────┘


Why separate agents? Models cannot reliably evaluate their own work. They praise mediocre output and skip edge cases. Separation enables objective quality assessment.

Three Layers
Layer	Agents	Responsibility
Decision	Planner, architect-lead	Product & Architecture decisions
Execution	Generator, [domain]-dev	Implement features
Evaluation	Evaluator	Test and grade implementation
Key Components
Component	Purpose
Sprint Contract	Negotiate "done" criteria before implementation
Domain Specialists	Specialized implementation agents per domain
Evaluation Criteria	Convert subjective judgments to gradable standards
Context Reset	Structured handoffs for long-running tasks
Workflow
1. Parse Arguments
Validate target path
Ask user if not provided:
Where should I generate the harness?
A) Current directory: .
B) Specify path: [input]
C) Create new project: [name]

2. Analyze Target Directory

Auto-detect:

Project type: package.json → Node.js, pyproject.toml → Python
Architecture: services/ → microservices, apps/ + packages/ → monorepo
Tech stack: Read dependencies from config files
Module boundaries: Detect src/, apps/, packages/
Domain type: Match against domain templates

Generate analysis report → User confirms or adjusts

3. Domain Detection (NEW in v2.0)
Analyze project structure
        │
        ▼
┌─────────────────────────────────────┐
│ Match against domain templates:     │
│                                     │
│ • web-development   (frontend+api+db)│
│ • game-development  (gameplay+gfx+audio)│
│ • data-science      (ml+data+analysis)│
│ • mobile-app        (ios+android)│
│ • ...                               │
└─────────────────────────────────────┘
        │
        ├─────────────┬─────────────┐
        ▼             ▼             ▼
   Matchfound    No match      User specifies
        │             │             │
        ▼             ▼             ▼
   Use template   Dynamic gen   Custom config

4. Specialist Selection
检测到项目类型: Game Development (Unity)

推荐的配置:

核心 Agents (固定):
  Planner        - 产品规划
  Generator      - 协调执行 (+Agent工具)
  Evaluator      - 评估实现
  architect-lead - 架构决策

Specialists (可调整):
  [√] gameplay-dev    游戏逻辑、机制、AI
  [√] graphics-dev    渲染、shader、特效
  [√] audio-dev       音效、音乐系统
  [ ] physics-dev     物理模拟、碰撞检测
  [√] ui-dev          游戏UI、HUD、菜单

操作:
  A) 直接使用推荐
  B) 调整选择
  C) 添加自定义 specialist
  D) 查看详情

5. Generate Harness (Parallel Execution)

Use subagents to generate components in parallel for speed:

User confirms generation│
        ├─► Subagent 1: Core agents (planner, generator, evaluator, architect-lead)
        │
        ├─► Subagent 2: Domain specialists (from template or dynamic)
        │
        ├─► Subagent 3: Evaluation system (skills, templates, docs)
        │
        ├─► Subagent 4: Progress system (skills, hooks, templates)
        │
        ├─► Subagent 5: Safety system (hooks, rules, docs)
        │
        ├─► Subagent 6: Domain-specific skills and rules
        │
        └─► Main thread: Integrate results + generate settings.json

6. Post-Generation Guidance
✅ Harness generated at [target-dir]/.claude/

Next steps:
1. cd [target-dir]
2. claude
3. Run /start

Domain Template System
Template Location
domain-templates/
├── web-development/      # Web应用模板│   ├── template.yaml
│   └── specialists/
│       ├── frontend-dev.yaml
│       ├── api-dev.yaml
│       ├── database-dev.yaml
│       └── devops-dev.yaml
│
├── game-development/     # 游戏开发模板
│   ├── template.yaml
│   └── specialists/
│       ├── gameplay-dev.yaml
│       ├── graphics-dev.yaml
│       ├── audio-dev.yaml
│       └── ui-dev.yaml
│
├── data-science/         # 数据科学模板│   └── ...
│
└── _dynamic/             # 动态生成│   ├── specialist-template.yaml
    └── detection-rules.yaml

Template Structure (template.yaml)
template:
  name: game-development
  version: 1.0.0
  
  # Detection rules
  detection:
    files: ["*.unity", "*.gd"]
    directories: ["Assets/", "Scripts/"]
    keywords: ["game", "unity"]
  
  # Core agents (fixed)
  core_agents:
    - planner
    - generator
    - evaluator
    - architect-lead
  
  # Domain specialists
  specialists:
    - name: gameplay-dev
      source: ./specialists/gameplay-dev.yaml
    - name: graphics-dev
      source: ./specialists/graphics-dev.yaml

Specialist Definition
name: gameplay-dev
description: "Specialist for gameplay logic"

delegation:
  mode: spawned_by_generator
  contract_required: true

domain_scope:
  directories:
    - "Scripts/Gameplay/"
    - "Scripts/AI/"responsibilities:
  - Implement game mechanics
  - Create state machines
  - Implement AI behavior

anti_patterns:
  - "Don't put rendering code in gameplay scripts"

Generated Harness Structure
<target-dir>/
├── .claude/
│   ├── settings.json
│   ├── agents/
│   │   ├── planner.md
│   │   ├── generator.md          # + Agent 工具
│   │   ├── evaluator.md
│   │   ├── architect-lead.md
│   │   └── [domain]-dev.md        # 领域 specialist
│   ├── skills/
│   │   ├── start/
│   │   ├── checkpoint/
│   │   ├── resume/
│   │   ├── sprint-contract/
│   │   └── [domain-specific]/     # 领域特定 skills
│   ├── hooks/
│   ├── rules/
│   ├── evaluation/
│   └── docs/
├── production/
│   ├── session-state/
│   └── session-logs/
└── CLAUDE.md

Key Principles
Generator-Evaluator Separation: Never the same agent
Sprint Contract First: Negotiate "done" before building
Domain Specialists: Delegated by Generator, specialized implementation
Context Reset: Use handoff artifacts for long tasks
Concrete Criteria: Convert subjective to gradable
Reference

Design based on Anthropic: Harness Design for Long-Running Apps

Weekly Installs
21
Repository
fanlw0816/harne…-creator
GitHub Stars
8
First Seen
9 days ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass