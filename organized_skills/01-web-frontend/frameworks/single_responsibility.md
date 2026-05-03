---
rating: ⭐⭐
title: single-responsibility
url: https://skills.sh/qiao-925/qiao-skills/single-responsibility
---

# single-responsibility

skills/qiao-925/qiao-skills/single-responsibility
single-responsibility
Installation
$ npx skills add https://github.com/qiao-925/qiao-skills --skill single-responsibility
SKILL.md
单一职责

这个 skill-unit 处理的是“职责是否混在一起”问题。它不负责定义系统分层，而负责把文件、函数、类、模块收敛到一个稳定职责上。

核心原则
1. 职责可说清 —— 说不清，通常就是过重
一个文件、函数、类或模块，应该能用一句话说明自己负责什么。
如果解释一个单元时必须用“既负责 A，也负责 B，还顺便处理 C”，通常说明职责已经混杂。
名称与实际行为长期不一致，也是职责失焦的信号。
2. 变化原因单一 —— 不同变化面不要绑在一起
单一职责的本质不是“代码少”，而是“变化原因尽量单一”。
如果一段代码会因为不同角色、不同业务意图、不同技术原因频繁一起被改，就应考虑拆分。
验证、计算、格式化、IO、编排等不同变化面，不应长期绑定在同一职责里。
3. 边界先清 —— 先定职责，再定拆分方式
拆分不是为了把代码切碎，而是为了让边界更稳定。
先回答“这个单元真正负责什么”，再决定拆成几个文件、几个函数、几个模块。
如果拆分后边界仍然模糊，只是把混乱搬到更多地方。
4. 拆分有收益 —— 清晰度比数量更重要
更小不一定更好，关键是更清楚。
拆分后的单元应更容易命名、更容易测试、更容易定位修改原因。
如果拆分只增加跳转层级，却没有提升边界清晰度，就不值得做。
AI Agent 行为要求
默认适用场景
场景	最低要求	不该做什么
文件重构	判断文件是否承载多个不相关职责	只因为文件长就机械拆分
函数重构	判断是否混合了验证、计算、IO、格式化等职责	把一个清晰函数硬拆成很多碎片
模块设计	判断模块是否围绕稳定业务意图组织	用“可能复用”提前堆很多抽象层
代码审查	明确指出职责混杂点与拆分方向	只说“可以再优化”
默认执行方式
先要求每个候选单元都能被一句话准确描述。
检查它是否承载了多个不同变化原因。
若职责混杂，先标出边界，再给拆分方案。
拆分时优先保持外部接口和阅读主路径稳定。
拆分后复核：职责更清楚了，而不是文件更多了。
典型职责混杂信号
一个函数同时做校验、执行、格式化和输出
一个文件同时放了不相关的工具函数、业务逻辑和外部适配
一个模块名字很大而泛，里面什么都装
一个类同时承担编排、状态管理、业务计算和基础设施细节
场景化展开
涉及文件与类边界时，读取 references/file-level.md
涉及函数重构时，读取 references/function-level.md
涉及模块与包边界时，读取 references/module-level.md
与其他 skill 的协同边界
与 architecture-governance：当问题已上升到分层、依赖方向和接口契约时联动，顺序为“先定大边界，再拆职责”。
与 file-guardrails：当文件超限的根因是职责混杂时联动，顺序为“先识别职责，再给拆分方案”。
与 core-first-simplicity：当职责混杂是因为顺手叠加了很多非核心能力时联动。
判断标准
是否能用一句话准确描述该单元职责。
是否存在多个独立变化原因被绑在一起。
拆分后是否更容易命名、测试和定位修改原因。
外部接口和主阅读路径是否仍然清晰。
是否避免了“为了拆而拆”的机械碎片化。
反模式
用一个 utils.py、service.py、manager.py 承载大量无关职责。
一个函数既取数据、又验证、又计算、又输出。
为了追求“单一职责”把代码拆成大量难以追踪的小碎片。
拆分前不澄清职责边界，只按行数或感觉切文件。
名称长期不能准确反映行为，却继续往里面加功能。
参考资料
references/file-level.md - 文件与类边界的职责识别与拆分
references/function-level.md - 函数职责混杂的常见模式与重构方式
references/module-level.md - 模块边界、依赖关系与职责收敛
Weekly Installs
20
Repository
qiao-925/qiao-skills
First Seen
Feb 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass