---
title: python-coding-standards
url: https://skills.sh/qiao-925/qiao-skills/python-coding-standards
---

# python-coding-standards

skills/qiao-925/qiao-skills/python-coding-standards
python-coding-standards
Installation
$ npx skills add https://github.com/qiao-925/qiao-skills --skill python-coding-standards
SKILL.md
Python 编码基线

这个 skill-unit 处理的是“Python 代码实现质量”问题。它不是个人风格清单，而是一套先对齐项目、再落通用基线的约束。

核心原则
1. 项目对齐 —— 先遵循仓库既有约定
先看当前仓库已经怎么写，再决定这次改动怎么落。
如果项目已有明确约定，优先沿用，不用通用偏好硬覆盖。
如果项目没有稳定约定，再用本 skill 作为默认基线。
2. 类型边界 —— 公共接口先清楚
新增或修改的函数、方法、类边界应补全必要类型提示。
公共接口、跨模块边界、非显然返回值，比局部变量更值得优先标注。
类型提示的目标是降低歧义，而不是机械补满每一行。
3. 运行日志 —— 正式路径不用 print
正式运行路径优先使用项目既有日志设施。
如果项目没有封装 logger，使用 Python 标准 logging 或当前框架约定。
print 只适合一次性脚本、调试、示例或测试，不应用来承载正式运行日志。
4. 命名与结构 —— 让代码顺着 Python 习惯阅读
命名应表意清楚、术语一致，避免模糊缩写。
导入、模块结构、函数主路径应让读者能顺序阅读。
Python 代码优先清晰和直达，不追求过度技巧化的“聪明写法”。
AI Agent 行为要求
默认适用场景
场景	最低要求	不该做什么
新增 Python 文件	先看项目约定，再写类型、日志、命名与结构	不看仓库现状就套个人模板
修改现有实现	沿用现有风格并修正明显基线问题	顺手把整文件改成另一套风格
Python 重构	优先改善边界清晰度和可读性	只做表面风格统一，不解决实际问题
代码审查	明确指出类型、日志、结构偏差	泛泛说“代码不够 Pythonic”
默认执行方式
先识别项目已有约定：格式化、类型检查、日志方式、导入习惯、命名风格。
若已有稳定约定，优先贴合；若缺失，再应用本 skill 的默认基线。
新增或修改公共接口时，优先补齐类型边界与必要说明。
处理运行路径时，检查是否错误地使用了 print 或缺少异常日志。
复核命名、导入、模块结构和主路径可读性，避免把小改动扩成全文件风格改造。
高风险偏差信号

出现以下任一情况时，应主动收敛：

把某个项目专用 logger 路径写成通用规范
为满足“看起来严格”而机械补充大量无效类型或 docstring
明明只是局部修复，却顺手重排整个文件风格
运行路径仍然依赖 print 输出关键状态或错误
场景化展开
涉及如何对齐现有仓库约定时，读取 references/project-alignment.md
涉及类型边界与公共接口时，读取 references/type-discipline.md
涉及日志与异常记录时，读取 references/logging-and-diagnostics.md
涉及命名、导入与模块结构时，读取 references/naming-and-structure.md
与其他 skill 的协同边界
与 python-uv-acceleration：当问题是环境、依赖安装、虚拟环境与工具链选择时联动；不要把工具链流程混进编码规范。
与 file-guardrails：当问题落到单文件过大、头部说明、拆分方式时联动。
与 architecture-governance：当 Python 问题已上升到包边界、层级依赖与模块架构时联动。
与 source-quality-control：当实现依赖第三方库、框架 API 或版本差异时联动。
判断标准
这次改动是否优先遵循了仓库已存在的 Python 约定。
公共接口、跨模块边界和非显然返回值是否有清晰类型提示。
正式运行路径是否使用了合适的日志方式，而不是 print。
命名、导入与模块结构是否让主路径更容易阅读。
规范是否保持平台无关，而不是混入项目私有实现细节。
反模式
把 src.logger.setup_logger 之类的项目私货写成通用标准。
把“所有地方都补类型”当成目标，而不看信息增益。
用 print 承载服务端、后台任务或正式脚本的运行日志。
因为个人偏好而大规模重写现有文件风格。
用“更 Pythonic”做空泛评价，却不指出具体可执行改进点。
参考资料
references/project-alignment.md - 如何先对齐仓库既有约定
references/type-discipline.md - 类型边界与公共接口的最小基线
references/logging-and-diagnostics.md - 正式运行路径的日志纪律
references/naming-and-structure.md - 命名、导入与结构可读性
Weekly Installs
23
Repository
qiao-925/qiao-skills
First Seen
Feb 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass