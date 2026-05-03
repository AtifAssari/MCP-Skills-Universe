---
title: by-harness
url: https://skills.sh/xmzdesign/santong-skill/by-harness
---

# by-harness

skills/xmzdesign/santong-skill/by-harness
by-harness
Installation
$ npx skills add https://github.com/xmzdesign/santong-skill --skill by-harness
SKILL.md
by-harness

by-harness 是一个独立 skill，用来给目标仓库安装并运行一套稳定的工程闭环：

read task -> plan -> build -> qa -> fix -> mark_pass -> session_close


核心目标不是“多放一些文档”，而是让模型每次开发都有明确的任务来源、规格、实现边界、验收方式和会话收口记录。

1. 先判断用户意图

收到请求后，先把用户意图归到下表之一，再执行对应动作。

用户意图	常见说法	主要动作
初始化 harness	“初始化”“用 by-harness 初始化这个仓库”	运行 scripts/scaffold.py，再提示执行或执行 .harness/scripts/init.sh
持续拆任务	“持续拆任务”“拆 5 个任务”“把这个主题拆一下”	运行 scripts/decompose_tasks.py，写入 active bucket
执行某个任务	“执行 feat-03”“继续当前任务”	读取任务，按 plan/build/qa/fix/mark_pass 闭环推进
会话收口	“收口”“保存进度”“session_close”	运行 .harness/scripts/session_close.py
自动续跑	“继续下个任务”“自动续跑”	运行 .harness/scripts/task_switch.py continue --target-dir .
老仓库升级	“升级 harness”“同步 runtime”“更新脚手架”	运行 scripts/update_runtime.py，优先备份与版本化迁移
Java 规范约束	“Java 硬规则”“Service 接口实现”“MapStruct/金额/Redis/分页规则”	先读 .harness/docs/java-dev-conventions.md 入口，再按触发维度读取 .harness/docs/java/rules/ 分片规则
分布式 Java 约束	“分布式编码规范”“幂等/重试/锁/事务/消息/缓存一致性”	使用 .harness/docs/java/rules/distributed-java-gate.md 约束 spec/contract/build/qa
前端规范约束	“前端规范”“UI 约束”“按设计稿/参考页”	使用已下发的前端三层规范和 BYAI HTML 参考约束实现

如果缺少项目名、目标目录或任务 ID，能从当前仓库和 .harness/task-harness/index.json 推断时直接推断；推断风险高时再问一个简短问题。

2. 初始化目标仓库

初始化使用 skill 内置脚本：

python3 {{SKILL_PATH}}/scripts/scaffold.py \
  --project-name "<项目名称>" \
  --description "<项目目标>" \
  --tech-stack "<技术栈，可选>" \
  --project-type "<项目类型，可选>" \
  --design-guidance "<设计约束，可选>" \
  --target-dir "<项目目录>"


初始化后生成：

根目录入口：AGENTS.md、CLAUDE.md
Codex / Claude 配置：.codex/、.claude/
Harness 工作区：.harness/config/、.harness/docs/、.harness/scripts/、.harness/task-harness/
任务索引：.harness/task-harness/index.json
默认任务桶：.harness/task-harness/features/backlog-core.json
运行时版本：.harness/config/runtime-version.json
更新策略：.harness/config/update-policy.json

初始化完成后，执行或提示：

bash .harness/scripts/init.sh


不要在已有项目中默认使用 --force。只有用户明确要求覆盖时才使用。

3. 任务存储模型

默认使用分片任务存储：

.harness/task-harness/index.json：路由索引，记录 active bucket。
.harness/task-harness/features/*.json：任务分片。
.harness/task-harness/progress/latest.txt：最新会话快照，给新会话快速接续。
.harness/task-harness/progress/YYYY-MM.md：按月追加的会话历史。

.harness/feature_list.json 只用于 legacy 项目兼容：如果旧项目已经存在该文件，可以继续同步 active bucket 视图；新项目不要主动创建它。

4. 持续拆任务

当用户要求拆解需求、追加任务或扩展 backlog 时，运行：

python3 {{SKILL_PATH}}/scripts/decompose_tasks.py \
  --target-dir "<项目目录>" \
  --item "<任务描述1>" \
  --item "<任务描述2>" \
  --category "feature"


执行原则：

用户指定数量时尽量满足；未指定时通常拆 4-8 个可执行任务。
每个任务要能进入 read task -> plan -> build -> qa -> fix -> mark_pass 闭环。
新任务默认写入 active bucket；只有用户指定时才切换 bucket。
回报新增任务 ID、优先级、建议执行顺序和下一步命令。

任务过多或旧 feature_list.json 过大时，可运行：

python3 {{SKILL_PATH}}/scripts/rebalance_tasks.py --target-dir "<项目目录>"

5. 执行任务闭环

当用户要求执行某个 feature，按以下顺序推进：

定位任务：优先用用户给出的 feat-id；没有时用 .harness/scripts/ensure_task_branch.py 选择当前任务。
读取任务：看 description、steps、spec_path、contract_path、qa_report_path。
Plan：生成或更新 .harness/docs/specs/<feature>.md。
Build：只实现 contract 范围内的内容。
QA：运行可用测试；QA 默认非阻塞，但失败要记录问题。
Fix：单元测试失败时最多修 3 轮。
Mark pass：单元测试通过，且 spec_path / contract_path 文件真实存在后，才可把 passes=false 改为 true。
Session close：调用会话收口脚本，刷新最新进度。

如果 3 轮后单元测试仍失败，保持 passes=false，记录原因、已尝试修复和下一步建议。

6. 会话收口与续跑

每次会话结束或用户要求保存进度时，运行：

python3 .harness/scripts/session_close.py \
  --target-dir . \
  --feature-id "<feat-id>" \
  --outcome "in-progress|completed|blocked" \
  --qa-score "<0-100，可选>" \
  --note "<本轮摘要>"


收口脚本会：

追加进度日志。
刷新 .harness/task-harness/progress/latest.txt。
输出下一任务建议。

继续下个任务时运行：

python3 .harness/scripts/task_switch.py continue --target-dir .

7. 老仓库升级

老仓库优先使用版本化升级，不要重新全量覆盖：

python3 {{SKILL_PATH}}/scripts/update_runtime.py --target-dir "<项目目录>"


升级行为：

先备份关键配置、脚本和运行时文档。
读取 .harness/config/runtime-version.json。
有 manifest_url 时从远程 manifest 拉取并校验 checksum。
没有 manifest_url 时只执行本地兼容迁移。
当前版本高于内置或远程版本时，只告警，不降级覆盖。

远程定时检查使用：

python3 .harness/scripts/update_runtime.py --target-dir . --check-remote


默认 update-policy.json 是 enabled=false；只有用户配置 manifest_url 并开启后才自动检查。

8. 工程规范下发

初始化会下发两类工程规范：

后端入口：.harness/docs/java-dev-conventions.md
后端分片：.harness/docs/java/rules/
前端入口：.harness/docs/frontend-dev-conventions.md

Java 后端采用分片 Java 总门禁，并融合真实项目验证过的落地规则：

Plan 阶段先读 Java 入口，再按触发维度读取分片规则：00-core.md、java-ddd.md、dubbo-api.md、logging-error.md、persistence-infra.md、testing-security.md、distributed-java-gate.md。
Plan 阶段必须执行最小实体与成本评估：如无必要，勿增实体；历史项目小改动优先复用既有实体、表、DTO、Service、配置和扩展点。
所有 Java 改动都必须处理 Java 总门禁 5 条：先契约后实现、先本地后通用、边界不被突破、风险显式落地、验证可追溯。
按触发维度追加 5 条左右核心门禁：通用工程、分层与 DDD、Dubbo 与公共 API、日志与异常、持久化与基础设施、测试安全运维、分布式 Java 门禁。
所有 Java 改动必须声明分布式 Java 门禁：未触发需说明理由；触发外部调用、Dubbo/HTTP/RPC、MQ、异步、线程池、锁、Redis、事务、补偿或发布停机时，必须逐条对照 distributed-java-gate.md。
Contract 阶段必须把 Java 总门禁、触发维度核心门禁、分布式 Java 门禁转成可验收清单，不能只写“已阅读规范”。
Build 阶段复述总门禁和触发维度门禁，并按正反例实现。
QA 阶段对照 contract、触发分片和 convention-check 结果验收。
Stop hook 阶段自动拦截可机器识别的 fail/warn。

前端采用三层结构：

约束层：.harness/docs/frontend/rules.md
示范层：.harness/docs/frontend/code-design.md
视觉层：.harness/docs/frontend/ui-design.md
视觉参考：.harness/docs/frontend/references/byai-ds-v/index.html

当前任务涉及 React、Vue、Next.js、TypeScript 组件、UI、样式、表格、表单、图表、Agent 界面或交互状态时，模型必须先阅读 .harness/docs/frontend-dev-conventions.md，再按任务类型阅读三层规范。

新增页面、重构页面或明显视觉变更时，还必须打开 BYAI HTML 参考页。参考页用于理解布局、密度、状态、token 和视觉气质，不要把 demo HTML 直接复制成业务实现。

9. 运行约束
AGENTS.md 是主契约，定义 Plan / Build / Verify / Fix。
.harness/docs/TASK-HARNESS.md 是任务层契约，不得覆盖主契约。
常规任务只更新任务状态、进度和闭环工件，不随意改任务结构。
规划方案必须遵守“如无必要，勿增实体”；历史项目小改动默认按最小成本实施，新增实体/表/DTO/Service/配置项必须写明必要性、替代方案、迁移成本和回滚影响。
单元测试通过且 spec/contract 已落盘后才可 passes=true；QA 报告默认非阻塞，但必须记录结果。
任何已标记 passes=true 的 feature，如果缺少 spec_path 或 contract_path 对应文件，pre-completion hook 必须阻断完成。
所有新增或修改的函数、方法必须补齐中文注释，说明用途、关键参数、返回值和副作用。
涉及 Java 时，完成前自检 Java 总门禁、触发维度核心门禁和分布式 Java 门禁，并运行 convention-check。读取规范时必须先读入口，再按触发维度读分片，不能默认整包加载所有规则。
涉及前端时，完成前自检 token、状态覆盖、响应式、可访问性、BYAI 参考页对齐和反例规避。
不使用破坏性 git 命令，不覆盖用户已有修改，不在已有项目中默认 --force。
10. 回报格式

执行完成后，用简短结构回报：

做了什么：初始化、拆任务、执行任务、收口或升级。
改了哪里：列出关键文件或目录。
验证结果：脚本输出、测试、dry-run 或未验证原因。
下一步：给出一个最合适的命令或任务 ID。
11. 典型提示词
用 by-harness 初始化这个仓库，项目名 xxx，目标是 xxx
持续拆任务 主题：支付链路稳定性，拆 5 个
执行 feat-03，严格按 read task -> plan -> build -> qa -> fix -> mark_pass
把当前会话收口，记录 qa 分数和下一步
升级这个项目里的 harness runtime
这个 Java 功能按 Java 总门禁检查 Service、金额、Redis、分页和配置
这个 Java 功能按分布式编码规范检查幂等、重试、锁、事务和消息
这个前端页面按 BYAI 参考和三层规范重做
Weekly Installs
19
Repository
xmzdesign/santong-skill
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn