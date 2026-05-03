---
rating: ⭐⭐⭐
title: project-memory-manager
url: https://skills.sh/entiwee-ship-it/project-memory-manager/project-memory-manager
---

# project-memory-manager

skills/entiwee-ship-it/project-memory-manager/project-memory-manager
project-memory-manager
Installation
$ npx skills add https://github.com/entiwee-ship-it/project-memory-manager --skill project-memory-manager
SKILL.md
项目记忆管理器
先判断任务类型
初始化新仓库时，先读 references/core/onboarding-playbook.md 与 references/core/work-protocols.md，再运行 scripts/init_project_memory.js 和 scripts/detect_project_topology.js
迁移旧体系时，先读 references/core/document-boundaries.md，再运行 scripts/migrate_legacy_memory.js，把长期结论迁入 docs，把可重建事实迁入 KB 配置和产物
需要全盘扫描整个仓库、学习项目自己的消息/状态协议时，先运行 scripts/build_project_kb.js --root <repo-root>，再读 references/core/project-protocol-learning.md
当问题本质是"为什么这个阶段太早/太晚切换""为什么动画没播完就进下一步"这类业务时序问题时，优先看 timing / phase / transition patterns
构建或刷新链路 KB 时，先读 references/core/kb-schema.md，再按技术栈读取对应 references/adapters/*.md，准备配置后运行 scripts/build_chain_kb.js --config ...
查询调用链、事件、request、state 时，优先运行 scripts/query_project_kb.js --root <repo-root>；当范围已经缩到 feature 再用 scripts/query_kb.js --feature ...
当任务是"给 Cocos 节点挂脚本、补点击事件、给脚本字段绑节点/组件/资源"时，先读 references/adapters/cocos.md，再运行 scripts/cocos_authoring.js
校验技能包或在新环境自举依赖时，先读 references/core/validation.md，再在技能根目录运行 python scripts/validate_skill_runtime.py . --mode auto
需要扩展新技术栈、补拓扑规则或制定前后端协同时，先读 references/core/adapter-protocol.md 与 references/core/fullstack-coordination.md
当任务是"升级这个技能本身"时，永远以 GitHub 源仓库为准，不要直接修改已安装副本目录
默认工作流
会话开始
先读目标仓库根的 AGENTS.md
再读 project-memory/state/active-work.json 与 project-memory/state/project-profile.json
再读任务相关 docs，优先看 FAQ.md、LOCATE.md、CHANGE_GUIDE.md 和对应 feature 文档
当任务是定位入口、事件绑定、request-callback、状态流转或上下游调用时，先查 project-global KB，再决定是否做 feature 级或局部源码搜索
若目标仓库还没有 project-memory/，立即切到"初始化或刷新项目记忆"流程
初始化新仓库
运行 node scripts/init_project_memory.js --root <repo-root> --name <project-name>
运行 node scripts/detect_project_topology.js --root <repo-root>
按 references/core/onboarding-playbook.md 的默认顺序补齐 AGENTS.md、project overview、active work 与工作协议
只在识别出技术栈后读取对应适配器，避免一次性加载全部技术说明
迁移旧体系
运行 node scripts/migrate_legacy_memory.js --root <repo-root> --source .kimi
先保留旧体系快照，再迁移长期结论
用 references/core/document-boundaries.md 判断哪些内容进入 docs，哪些内容应沉淀为 KB 配置或可重建产物
迁移后刷新 project-profile.json、active-work.json 与 feature registry
构建或刷新功能 KB
先准备 KB 配置 JSON，明确 featureKey、入口文件、关注目录与语义标签
运行 node scripts/build_chain_kb.js --config <config-path>
构建后会自动同步 feature-registry.json 与 kb/indexes/features.json
用 references/core/kb-schema.md 校验节点类型、边类型与查询面是否覆盖任务需求
若拓扑或抽取结果不稳定，只补适配器规则，不要手改 KB 产物
后端仓库可直接使用 serverRoots、moduleRoots、dbRoots 或 scanTargets.handlers/remotes/modules/routes/schemas
Pinus 后端优先参考 assets/templates/KB_CONFIG_PINUS_BACKEND_EXAMPLE.json
类似 qyserver 的仓库优先用绝对 scanTargets + extractorAdapter: "pinus"，不要在目标仓库里手工同步索引
旧字段 key / name / outputDir 与旧输出文件名仍兼容，但会打印弃用告警
构建 project-global KB
运行 node scripts/build_project_kb.js --root <repo-root>
这一步会全盘扫描仓库，产出：
project-memory/kb/project-global/chain.graph.json
project-memory/kb/project-global/chain.lookup.json
project-memory/kb/project-global/build.report.json
project-memory/state/project-protocols.json
这一步不是替代 feature KB，而是提供全局入口、消息协议学习和跨区域链路基座
当升级技能版本后，优先重建 project-global KB，再重建 feature KB
查询链路
全局入口优先：node scripts/query_project_kb.js --root <repo-root>
全局消息查询：node scripts/query_project_kb.js --root <repo-root> --message <message> --downstream
全局时序查询：node scripts/query_project_kb.js --root <repo-root> --timing <query>
全局阶段查询：node scripts/query_project_kb.js --root <repo-root> --phase <query>
全局状态转换查询：node scripts/query_project_kb.js --root <repo-root> --transition <query>
当范围已经缩小到单一 feature，再运行 node scripts/query_kb.js --feature <feature-key> ...
若已经在技能根目录，可直接运行 node scripts/query_kb.js --feature <feature-key> ...
若不在技能根目录，再使用 node <skill-path>/scripts/query_kb.js --feature <feature-key> ...
若只执行 --feature <key>，脚本会先返回 feature 摘要、默认排查顺序、推荐命令和各 KB 文件用途
优先用 --downstream <query>、--upstream <query>，或 --method/--event/--request/--state <query> --downstream|--upstream
scripts/query_chain_kb.js 仍保留兼容，但默认推荐入口改为 scripts/query_kb.js
兼容旧写法 --from <query> --direction <upstream|downstream>
build.report.json 是给人看的说明文件；chain.lookup.json / chain.graph.json / scan.raw.json 默认都不建议直接手读
当只知道业务语义词时，先试 --name 或 --tag
只有 KB 无法回答时，才做补充性的 rg / grep
Cocos 创作辅助
先运行 node scripts/cocos_authoring.js --feature <feature-key> --prefab <prefab-name> --intent profile 看 prefab 的节点、组件、可绑定字段和已有事件模式
如果问题是"节点 / 组件索引是多少""Spine 组件在哪""脚本字段有没有绑上"，优先继续用 profile 过滤：
--node <node-name> / --component <component-name> / --field <field-name>
新增点击事件时，运行：
node scripts/cocos_authoring.js --feature <feature-key> --prefab <prefab-name> --intent click-event --source-node <source-node> --target-component <target-component> --handler <method>
新增字段绑定时，运行：
node scripts/cocos_authoring.js --feature <feature-key> --prefab <prefab-name> --intent field-binding --component-node <component-node> --component <target-component> --field <field-name> --target-node <node-path>
或 --target-component <component-name> / --target-asset <asset-name>
先让脚本输出"该改脚本还是改 prefab"的规划，再决定是否真正修改 prefab
Cocos Profile 查询（避免 PowerShell 转义问题）

重要：当需要查询 cocos-authoring-profile.json 中的原始配置信息时，不要使用 python -c "..." 内联代码（PowerShell 对 [] 等特殊字符处理有问题），而是使用专用脚本：

# 列出所有 features
node scripts/query_cocos_profile.js --list-features

# 列出包含 golden 的 features
node scripts/query_cocos_profile.js --list-features --filter golden

# 列出所有 prefabs
node scripts/query_cocos_profile.js --list-prefabs

# 查找包含 goldenEgg 的 prefabs
node scripts/query_cocos_profile.js --list-prefabs --filter goldenEgg

# 查找标题动画节点（如 EggsTitle, PrizeBoxTitle）
node scripts/query_cocos_profile.js --find-node EggsTitle

# 查看特定 prefab 详情
node scripts/query_cocos_profile.js --prefab-detail goldenEgg

# JSON 输出（供脚本解析）
node scripts/query_cocos_profile.js --prefab-detail goldenEgg --json

会话收口
更新 active work 或对应工作文档
结构变化时刷新 KB 与索引
长期认知变化后更新 docs
高频修复优先补 FAQ.md、LOCATE.md、CHANGE_GUIDE.md
升级这个技能本身
永远不要把 <installed-skill-path> 或其它已安装副本当作最终修改目标
正确流程是：修改 GitHub 源仓库 -> 校验 -> commit/push -> npx skills update
技能升级完成后，必须在技能根目录执行 node scripts/rebuild_kbs.js --root <project-root> 重建现有 KB
如果当前查询脚本提示 [stale-kb]，说明 KB 还是旧技能版本构建的，先重建再继续分析
按需读取这些 references
接管与首次落地：references/core/onboarding-playbook.md
日常协作顺序：references/core/work-protocols.md
docs 与 KB 边界：references/core/document-boundaries.md
KB schema 与查询面：references/core/kb-schema.md
项目协议学习：references/core/project-protocol-learning.md
全栈协同：references/core/fullstack-coordination.md
适配器扩展规则：references/core/adapter-protocol.md
校验与环境自举：references/core/validation.md
核心规则
docs 是长期结论层
KB 是可脚本重建事实层
不要把全仓库搜索当作第一轮定位动作
不要把穷举方法表直接灌进长期 docs
不要手改 KB 产物
结构变化后刷新 KB
长期认知变化后更新 docs
优先补脚本、配置或适配器，不要把一次性推理结果写成长期协议
依赖 process.cwd() 的脚本要先切到目标仓库根；带 --root 的脚本可以从任意目录运行
避免使用 python -c "..." 内联代码（PowerShell 转义问题），优先使用 Node.js 脚本或 Python 文件
运行时说明
extract_feature_facts.js 在检测到 typescript 运行时时会优先使用 AST 提取类方法、箭头函数 handler、事件订阅/派发、request-callback 链与调用链
若运行环境缺少 typescript，会自动回退到正则模式
可用 node scripts/show_skill_version.js --text 查看已安装技能版本与能力指纹
可用 python scripts/validate_skill_runtime.py . --mode auto 校验技能包
show_skill_version.js 与 validate_skill_runtime.py 会在已安装副本路径下明确提示"不要直接改安装副本"
公开安装推荐使用 npx skills add https://github.com/entiwee-ship-it/project-memory-manager.git --skill project-memory-manager -g -a codex -y
技术适配器
Cocos：references/adapters/cocos.md
Pinus / Node 游戏服务端：references/adapters/pinus.md
Vue：references/adapters/vue.md
React：references/adapters/react.md
Java Spring：references/adapters/java-spring.md
Node 服务：references/adapters/node.md
Go 服务：references/adapters/go.md
Python 服务：references/adapters/python.md
Weekly Installs
11
Repository
entiwee-ship-it…-manager
First Seen
Mar 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykFail