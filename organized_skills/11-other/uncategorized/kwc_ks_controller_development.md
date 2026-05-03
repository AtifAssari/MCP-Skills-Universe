---
rating: ⭐⭐
title: kwc-ks-controller-development
url: https://skills.sh/kingdee/kwc-skills/kwc-ks-controller-development
---

# kwc-ks-controller-development

skills/kingdee/kwc-skills/kwc-ks-controller-development
kwc-ks-controller-development
Installation
$ npx skills add https://github.com/kingdee/kwc-skills --skill kwc-ks-controller-development
SKILL.md
KWC KS Controller 开发专家

当项目中需要开发 KingScript 脚本控制器（后端 REST API）时，本 Skill 负责控制器的 .kws 元数据配置和脚本代码实现。

必须严格遵守本 Skill 目录下的 rule.md 中定义的硬性约束。

使用前置条件

必须同时满足以下条件才能使用本 Skill：

当前目录已存在 .kd/config.json 文件
工程中已存在 app/ks/controller/ 目录
工程已通过 kwc-project-scaffold 完成初始化

以下场景必须交由 kwc-project-scaffold：

工程初始化、创建组件/页面/Controller 目录（kd project init / kd project create）
生成或修改 .js-meta.kwc / .page-meta.kwp 元数据
环境配置、构建、部署、调试（kd env / npm run build / kd project deploy / kd debug）

若当前不满足上述前置条件，请立即停止并切换到 kwc-project-scaffold Skill。

标准工作流
确认目录存在：Controller 目录已由 scaffold 创建（app/ks/controller/<Name>/）
读取工程配置（强制）：读取 .kd/config.json，获取 isv、app 等字段的真实值，后续 .kws 中的 <isv>、<app>、<url> 必须基于这些值拼装，禁止猜测或硬编码
查询实体字段（涉及业务实体操作时）：通过 meta-query-api.mjs 获取真实字段结构，禁止猜测字段名
编写 .kws 元数据：基于第 2 步读取的配置拼装 URL（/{isv}/{app}/...），定义 HTTP 方法和权限
编写脚本代码：开始写代码前，必须先读取 ./reference/脚本控制器防坑指南.md，确保不使用不存在的 API、不踩已知运行时陷阱；SDK 调用前先在索引中确认存在
交付构建：完成后通知用户回到 scaffold 进行部署
参考资源
类别	资源	路径
本 Skill	.kws 元数据配置规范	./reference/kws-metadata-reference.md
	Controller 集成工作流	./reference/controller-scaffold-workflow.md
	常见模式和代码示例	./reference/controller-patterns.md
	前端 adapterApi 调用指南	./reference/frontend-integration.md
KingScript	脚本控制器开发指南	../kingscript-code-generator/references/docs/custom-development/脚本控制器开发指南.md
	脚本控制器防坑指南	./reference/脚本控制器防坑指南.md
	语言基础	../kingscript-code-generator/references/language/kingscript/README.md
	SDK 类索引	../kingscript-code-generator/references/sdk/indexes/class-index.md
	SDK 方法索引	../kingscript-code-generator/references/sdk/indexes/method-index.md
	SDK 场景索引	../kingscript-code-generator/references/sdk/indexes/scenario-index.md
	SDK 策略和降级链路	../kingscript-code-generator/references/sdk/strategy.md
	Java-KS 类型桥接	../kingscript-code-generator/references/sdk/docs/java-kingscript-bridge.md
Scaffold	实体字段查询工具	../kwc-project-scaffold/references/meta-query.md
Weekly Installs
26
Repository
kingdee/kwc-skills
GitHub Stars
2
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass