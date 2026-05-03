---
title: unix-software-design
url: https://skills.sh/zrr1999/skills/unix-software-design
---

# unix-software-design

skills/zrr1999/skills/unix-software-design
unix-software-design
Installation
$ npx skills add https://github.com/zrr1999/skills --skill unix-software-design
SKILL.md
目的

在涉及模块边界、接口设计、复杂度取舍时，提供 Unix 哲学下的设计原则作为参考，帮助做更简单、透明、可组合的决策。

适用场景
设计新模块或服务的边界
重构时的拆分与接口规划
讨论复杂度取舍、抽象层次
不适用
已经是纯实现任务，主要问题不在设计而在落代码
只是选一个现成工具或框架，不涉及系统边界和结构
若任务主要是「开新坑 / 维护推进 / 读项目提炼」的流程与产出结构，用 project-workflows；本 skill 聚焦边界与原则，不替代工作方式契约
模块化原则
Rule of Modularity: 编写简单部件，通过清晰接口连接。
Rule of Composition: 设计程序以便与其他程序连接。
Rule of Separation: 分离策略与机制；分离接口与引擎。
简洁性原则
Rule of Clarity: 清晰优于巧妙。
Rule of Simplicity: 为简洁而设计；仅在必要时才增加复杂性。
Rule of Parsimony: 仅在明确证明别无他法时才写大程序。
Rule of Extensible: 为未来设计，因为它会比你想象的更快到来。
健壮性原则
Rule of Transparency: 为可见设计，使检查和调试更容易。
Rule of Robustness: 健壮性是透明和简洁的产物。
Rule of Representation: 将知识融入数据，使程序逻辑可以更简单和健壮。
Rule of Least Surprise: 在界面设计中，始终做最不令人惊讶的事。
Rule of Silence: 当程序无话可说时，应该什么都不说。
Rule of Repair: 必须失败时，要尽快大声地失败。
效率原则
Rule of Economy: 程序员时间昂贵；优先节省程序员时间而非机器时间。
Rule of Generation: 避免手写代码；用代码生成器（如 protobuf、SQLAlchemy、cargo-generate）替代重复劳动。
Rule of Optimization: 原型先于优化。先让它工作，再用 profiling 工具定位瓶颈后优化。
多元性原则
Rule of Diversity: 质疑"唯一正确方式"的所有声明。
补充原则
尽可能将数据流设计为文本格式（便于用标准工具查看和过滤）。
数据库布局和应用程序协议应尽可能采用文本格式（JSON/YAML/TOML，人类可读和可编辑）。
复杂前端（用户界面）应与复杂后端清晰分离。
优先使用 Rust/Go/Zig 等现代系统级语言；用 Python/TypeScript 快速原型后再用编译型语言优化关键路径。
用 uv 管理 Python 依赖，用 cargo 管理 Rust 依赖，用 npm/pnpm 管理 JS 依赖。
对输入慷慨，对输出严格。
过滤时永远不要丢弃不需要的信息。
小即美。编写尽可能少做与完成任务一致的程序。
用 Docker/容器化封装应用，确保开发与生产环境一致。
用 CI/CD 流水线自动化测试和部署。
Weekly Installs
32
Repository
zrr1999/skills
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass