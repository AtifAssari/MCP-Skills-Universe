---
title: kwc-project-scaffold
url: https://skills.sh/kingdee/kwc-skills/kwc-project-scaffold
---

# kwc-project-scaffold

skills/kingdee/kwc-skills/kwc-project-scaffold
kwc-project-scaffold
Installation
$ npx skills add https://github.com/kingdee/kwc-skills --skill kwc-project-scaffold
SKILL.md
KWC Project Scaffold

将本 Skill 作为 KWC 工程脚手架工作的入口。 优先把用户需求归入以下几类：初始化项目、创建组件、创建 Controller、创建页面元数据、配置环境、部署、查看环境效果、调试。

正确认知交付对象

不要把 KWC 工作流理解成“本地把一个组件渲染出来”。 KWC 的核心交付对象是：

组件工程本身（前端代码 + 组件元数据 .js-meta.kwc）
页面元数据 *.page-meta.kwp
KS Controller 元数据 *.kws 和脚本代码（当功能涉及后端数据交互时）
目标环境配置与认证
通过 kd project deploy 上传后的环境渲染结果

页面最终展示依赖页面元数据中的 <controls> 和组件类型映射，而不是本地 main.tsx 是否挂载了某个组件。 main.tsx和npm run dev` 只用于本地辅助预览，不是最终交付路径。

KWC 不仅是前端开发框架。当页面需要读取或操作业务数据时，KS Controller 提供后端 REST API 能力，通过 KingScript 脚本访问苍穹平台的数据查询、业务操作等服务。一个完整的业务功能通常包含前端组件（展示与交互）和后端 Controller（数据获取与业务逻辑）两部分。

Controller 也遵循"元数据 + 代码"的二元模型：

Controller 元数据（.kws）：定义路由 URL、HTTP 方法、权限策略等声明式配置
Controller 脚本代码（.ts）：实现具体的业务逻辑

这与前端的"组件元数据 .kwc + 组件代码"模式完全对称。

元数据驱动的全栈开发模型

从用户开发角度看，一个完整的 KWC 功能最多涵盖以下层次：

前端（展示与交互）：

组件代码（*.tsx / *.vue / *.js）：负责渲染和交互逻辑
组件元数据 .js-meta.kwc：声明"这个组件可以被页面如何引用、可以暴露哪些可配置属性"
页面元数据 .page-meta.kwp：声明"这个页面由哪些组件实例组成，并给每个实例传什么属性值"

后端（数据与业务逻辑）： 4. Controller 元数据 .kws：声明"这个 Controller 暴露哪些 API 端点、使用什么 HTTP 方法、需要什么权限" 5. Controller 脚本代码（*.ts）：实现具体的数据查询、业务操作等后端逻辑

前端和后端都遵循"元数据先行、代码实现跟进"的模式——先声明结构和契约，再填充实现。

因此，面对需求时不要只问“要写几个组件”，还要继续判断：

哪些参数是写死在组件代码里的
哪些参数需要暴露给页面配置者，通过组件元数据定义为 <property>
哪些组件实例会出现在页面元数据的 <controls> 中
组件是否需要调用后端 API 获取数据或提交操作
若需要，Controller 元数据（.kws）需要定义哪些 API 端点（URL、HTTP 方法、权限）
Controller 脚本需要调用哪些 SDK 能力（数据查询、业务操作等）

默认原则：

能固定在组件内部的实现细节，不要暴露到元数据
只有需要被页面装配、复用、配置的参数，才进入组件元数据和页面元数据
先把需求翻译成工程目标

面对“帮我开发一个 KWC 页面/功能”的请求时，先把需求翻译成下面几项：

是否需要新建工程，还是在已有工程里继续开发
需要几个组件，各自承担什么职责
组件是否需要后端数据支持？若需要，规划对应的 KS Controller 和 API 方法
需要几个页面元数据文件，页面里如何组合这些组件
最终要部署到哪个环境

只有把这几项补齐，脚手架命令才有明确目标。

框架开发 Skill 协作

将 kwc-project-scaffold 视为 KWC 工作流的总入口，但不要让它吞掉框架开发 Skill 的职责。

硬性约束：代码实现必须移交框架 Skill

当任务进入"实现组件代码"阶段时，必须遵循以下强制规则：

禁止直接编写代码：本 Skill 严禁直接编写、修改任何组件实现代码（*.tsx / *.vue / .js）和 Controller 脚本代码（.ts）
必须先加载对应 Skill：前端代码加载框架开发 Skill（kwc-react/vue/lwc-development），Controller 代码加载 kwc-ks-controller-development
禁止凭通用知识自行编写：KingScript 运行时的 request/response API 与 Node.js / Java Servlet 完全不同，凭通用经验编写的代码将部署失败
多环节任务不是例外：即使当前任务涉及工程搭建 + 元数据 + Controller + 前端组件多个环节，每进入一个代码编写阶段都必须切换 Skill，不可"一口气"跳过
框架识别依据：
新建工程：以 kd project init 时用户选择的 framework 为准
已有工程：以 .kd/config.json 中的 framework 字段为准
若无法识别 framework，必须停止并向用户确认，禁止猜测
协作边界表
任务阶段	负责 Skill	产出物
工程初始化	scaffold	.kd/config.json
创建组件目录	scaffold	app/kwc/Component/
编写组件代码	react/vue/lwc-development	***.tsx / .vue / .js
补全组件元数据	scaffold	*.js-meta.kwc
创建页面元数据	scaffold	*.page-meta.kwp
环境配置与部署	scaffold	环境渲染结果
创建 Controller 目录	scaffold	app/ks/controller/ControllerName/
补全 Controller 元数据	scaffold	*.kws（URL、方法、权限配置）
构建 Controller	scaffold	dist/controller/
编写 Controller 脚本代码	kwc-ks-controller-development	.ts 脚本（业务逻辑实现）
切换时机
当任务仍处于需求拆分、脚手架命令、元数据、环境、deploy、open、debug 阶段时，继续由本 Skill 主导
当 kd project create 完成后需写代码 → 必须切到框架 Skill，禁止本 Skill 直接编写
当代码写完需补元数据或部署 → 回到 scaffold
当 Controller 目录已创建且需要编写脚本代码 → 必须切到 kwc-ks-controller-development，禁止本 Skill 直接编写
当 Controller 脚本代码写完需构建或部署 → 回到 scaffold
异常流程保护

当 CLI 命令失败（如 kd project create 报错）而改用手动方式创建文件/目录时，代码编写阶段的 Skill 切换规则同样适用。手动创建目录结构不等于可以手动编写业务代码。

只要进入 .ts / .tsx / .vue / .js 文件的编写，无论前置步骤是否通过 CLI 完成，都必须先切换到对应的框架 Skill
典型场景：kd project create 失败 → 手动创建 app/kwc/MyComponent/ 目录和 .js-meta.kwc → 到这里仍是 scaffold 职责 → 开始写 MyComponent.tsx 时 → 必须切换到框架 Skill
Controller 同理：手动创建 app/ks/controller/ 目录和 .kws → scaffold 职责 → 开始写 .ts 脚本 → 必须切换到 kwc-ks-controller-development
框架 Skill 激活检查清单

在进入代码实现阶段前，确认以下事项：

 已识别当前工程 framework（react/vue/lwc）
 已调用对应的框架开发 Skill（kwc-*-development）
 框架 Skill 的 rule.md 约束已加载并生效
 本 Skill 不再直接处理任何代码文件内容
推荐规则
若是新建工程，以 kd project init 交互中用户选择的 framework 作为后续推荐 Skill 依据
若是已有工程，以 .kd/config.json 中的 framework 作为推荐 Skill 依据
当 framework=react 时，必须转入 kwc-react-development
当 framework=vue 时，必须转入 kwc-vue-development
当 framework=lwc 时，必须转入 kwc-lwc-development
若还无法判断 framework，先停下来向用户确认
当任务涉及 Controller/脚本控制器代码编写时，必须转入 kwc-ks-controller-development
Controller 代码实现与前端框架无关，不受 framework 字段影响

注意：不要同时加载三个框架开发 Skill；只根据当前工程的 framework 推荐一个。

需要用户提供或确认的输入

这些输入若无法从现有工程或上下文推断，就必须向用户确认：

项目名或现有项目路径
框架和语言
苍穹应用编码 app
目标环境别名和 URL
认证方式，以及 OpenAPI 所需的真实参数
页面标识，例如 page name，以及业务页面用途
哪些组件需要暴露给页面使用，哪些只是内部逻辑组件
哪些参数需要做成可配置属性
若用户已有环境，是否允许直接部署到该环境

这些信息不要擅自编造，尤其是 app、环境 URL、认证参数和最终部署环境。

关于 isv（开发商标识）：开发阶段可以留空，在组件与环境绑定时会从环境拉取开发商标识，kd project deploy 时会自动写入组件和页面元数据，因此不需要用户手工提供或维护。

对 app 使用最严格的规则（本节为全文唯一权威定义）：

app 必须由用户明确提供，或来自 .kd/config.json
不可猜测、不可使用示例值
新建工程时在 kd project init 交互中输入
若无 app，不继续生成元数据或部署
由 Skill 自动决策或生成的内容

这些内容应由 Skill 基于用户需求主动完成，不要把它们再推回给用户逐项设计：

将业务需求拆成组件列表
为组件生成稳定的 PascalCase 名称
为页面和实例生成符合规范的小写标识
判断组件是否需要保留 .js-meta.kwc，还是应删除以避免被当成可部署组件
将需求映射为组件元数据里的 <property>
为页面生成 page-meta.kwp 并填充 <controls>
为页面中的每个组件实例生成唯一 name
判断当前该执行 init、create、deploy、open 还是 debug
查看环境效果时结合当前任务和页面元数据，自行判断使用 kd open 的目标页面；仅当用户明确要求本地联调时才使用 kd debug
仅当对应元数据文件变更并需要重新上传时，递增该元数据的 version
在环境操作后复核 kd env list 和 kd env info

默认策略是：让用户确认不可推断的关键环境参数，由 Skill 负责把需求落实成工程结构和元数据。

app 是例外：即使在自动决策范围内，也必须严格遵守"需要用户提供或确认的输入"中的 app 规则。

从需求生成组件元数据

当用户要“开发一个页面功能”时，不要等到最后才补 .js-meta.kwc。 应在组件职责确定后，立即判断组件元数据应如何生成。

按这个顺序处理：

先识别组件是否会被页面元数据直接引用。
若会被页面引用，就保留并完善对应的 .js-meta.kwc。
若组件只是内部复用逻辑、不需要在元数据页面中声明，可删除对应 .js-meta.kwc，避免被脚手架当作可部署组件。
将“页面配置者可调的参数”提炼为 <property>，不要把所有内部 props 都暴露出去。

组件元数据至少应关注这些字段：

version：自然数；脚手架模板可能留空，Skill 需要补成有效值
name：通常与组件名保持一致，作为组件类型标识
masterLabel：组件的中文名称（如「销售订单卡片」「采购申请列表」），作为组件在页面装配侧的显示标题
isv：开发商标识，开发阶段可留空，deploy 时自动从环境拉取写入
app：规则见“需要用户提供或确认的输入”一节
framework
targets
targetConfigs

如果需要字段规则、类型和示例，读取：

references/component-metadata.md
从需求生成页面元数据

页面元数据不是简单“列出组件名称”，而是把用户要的页面装配结构显式写出来。

按这个顺序处理：

先确定页面名称、标题、所属应用、业务单元、版本策略。
根据需求把页面拆成一个或多个组件实例。
为每个实例生成 <control>。
control.type 必须与组件元数据里的组件 name 完全一致，包含大小写也必须一致。
control.name 是页面内唯一实例名，必须符合页面元数据命名规范。
只有组件元数据中定义过的属性，才能写进 <propertys>。

例如，若组件元数据中的 name 是 OverviewCard，则页面元数据里的 control.type 只能写 OverviewCard。 不要因为组件目录在 app/kwc/ 下，就擅自写成 kwc_OverviewCard；这类前缀不是组件类型名的一部分。

页面字段默认策略：

masterLabel：页面的中文名称（如「销售订单」「采购申请」「库存查询」），作为页面在导航和管理界面的显示标题
template 默认使用 oneregion
isv deploy 时自动写入，无需手填
app 规则见“需要用户提供或确认的输入”一节

如果需要字段规则、校验约束和示例，读取：

references/page-metadata.md
先判断当前所处阶段

按这个顺序判断并推进：

若当前目录下不存在 .kd，先视为“尚未初始化 KWC 工程”。
若用户要新建页面或组件，优先使用 kd project create，不要手工拼目录结构。
若用户要部署或调试，先检查环境是否已经通过 kd env create 和 kd env auth openapi 完成配置。
若用户开始编写具体前端实现代码，先判断当前工程 framework，再建议转入对应框架的专用 Skill，不要把本 Skill 当成组件编码规范。
执行前置检查

先确认以下前提：

将 Project 理解为本地工程目录。
将 Env 理解为远端苍穹环境。
提醒用户本地需具备 node、npm、git。
初始化工程

在用户尚未拥有 KWC 工程时，按以下流程执行：

安装 CLI。
运行 kd project init <project-name>。
在交互流程中按用户要求选择框架和语言；若用户未指定，应主动询问。
输入应用标识 app（规则见“需要用户提供或确认的输入”一节）。
初始化完成后进入项目目录，执行 npm install。
仅在需要本地辅助预览组件时，再执行 npm run dev。

补充：kd project init 依赖 git clone 下载模板，若失败优先检查 git。

创建组件

在已有项目中新增组件时：

运行 kd project create <ComponentName> --type kwc。
使用 PascalCase 组件名。
让 CLI 生成目录和基础文件。
立刻检查生成出来的 .js-meta.kwc，补齐可部署所需字段和属性定义（这是本 Skill 的职责）。
组件代码实现移交：确认 .js-meta.kwc 补齐后，必须停止本 Skill 的代码编写，转而加载对应的框架开发 Skill（kwc-react-development / kwc-vue-development / kwc-lwc-development）来编写组件实现代码。
若用户同时要创建多个组件，逐个执行创建命令，不要手工复制推断目录结构。

若用户只提供了页面结构想法，没有组件名，先根据语义生成稳定、可复用的组件名，再创建。 若用户给的是完整业务诉求，而不是组件清单，先主动拆分组件职责，再批量创建。

补充：

组件生成在 app/kwc/<ComponentName>/ 下
脚手架生成的 .js-meta.kwc 只是模板，需按上述规则补齐
**严禁在本 Skill 中直接修改组件代码文件（*.tsx / .vue / .js），代码实现必须交由框架 Skill
创建 Controller

在已有项目中新增 KingScript 脚本控制器时：

运行 kd project create <ControllerName> --type controller。
使用 PascalCase 控制器名，建议以 Controller 后缀结尾。
让 CLI 生成目录和基础文件。Controller 工程生成在 app/ks/controller/<ControllerName>/ 下。
创建后检查生成的 .kws 元数据文件，补齐必填字段（name/isv/app/version/url/scriptFile/methods）。
Controller 代码实现移交：确认 .kws 元数据补齐后，必须停止本 Skill 的代码编写，转而加载 kwc-ks-controller-development 来编写控制器脚本代码。
若需指定拉取 SDK 的目标环境，可使用 -e 选项：kd project create <ControllerName> --type controller -e dev。

补充：

Controller 与前端组件（KWC）是独立的工程实体，可以在同一个项目中共存
脚手架生成的 .kws 元数据只是模板，需按控制器开发指南补齐
严禁在本 Skill 中直接修改 Controller 脚本代码（*.ts），代码实现必须交由 kwc-ks-controller-development
创建页面元数据

页面元数据是最终交付链路的核心。 环境在部署后会根据 page-meta.kwp 的 <controls> 来渲染页面包含的组件，因此这里不是可选步骤，而是页面交付的主入口。

在需要新增页面时：

运行 kd project create <page-name> --type page。
打开 app/pages/<page-name>.page-meta.kwp。
至少核对并填写 name、masterLabel、app、version。
在 <controls> 中把页面实例和组件类型关联起来。
仅当该页面元数据文件有变更并准备重新上传时，手动将 version 加 1。
将组件树、实例名和页面布局映射到 XML，而不是停留在“组件已经创建”这一步。

不要忽略以下约束：

type 是组件类型名，必须与组件元数据中的组件 name 完全一致，不能只做到语义对应或名称相近。
name 是组件实例名，需要在页面内唯一。
isv 开发阶段可留空，deploy 时会自动从环境拉取并写入
app 规则见“需要用户提供或确认的输入”一节

若需要字段规则、校验约束和示例，读取 references/page-metadata.md。

补充：新生成的 page-meta.kwp 默认只包含注释掉的 <control> 模板，Skill 必须根据需求主动补全 <controls>。

脚手架命令的推荐编排
需求前后端评估

面对完整业务需求时，按以下优先级判断是否需要 Controller：

强信号（命中任意一条即直接判定需要 Controller，无需询问用户）：

需求涉及列表/表格数据展示（如"XX列表"、"XX查询"、"XX监控"）
需求涉及筛选/搜索/过滤条件
需求涉及图表/报表/统计/仪表盘
需求涉及数据的增删改操作（保存、提交、审核、删除等）
需求涉及详情查看/编辑
需求涉及业务实体名称（如物料、仓库、订单、客户、库存等）

弱信号（需要询问用户确认）：

需求仅描述了 UI 样式或布局，未提及数据来源
需求可能通过本地 mock 数据或配置项完成

排除信号（不需要 Controller）：

页面仅展示静态内容、说明文档或本地计算结果
纯展示型组件（如欢迎页、关于页）

默认倾向：当需求描述中出现任何业务数据相关的词汇时，优先判定需要 Controller，而非询问用户。

实体识别与澄清

判定需要 Controller 后，必须进一步识别需求涉及哪些业务实体，用于后续 meta-query-api.mjs 查询真实字段：

从需求中提取实体关键词：分析用户需求描述，提取所有可能的业务实体名称（如"物料"、"仓库"、"库存"、"订单"等）
确认表单编码来源：表单/实体编码禁止猜测，只能通过以下两种方式获取：
用户直接提供：用户在需求中明确给出了表单编码（如 bd_material、im_inventory）
通过查询确认：使用 queryFormsByApp 搜索表单，从返回结果中确认真实编码
向用户澄清实体：若用户未提供表单编码，且实体名称可能存在歧义（如"库存"可能对应库存台账、库存余额、安全库存等不同表单），必须主动向用户确认：
"您提到的'库存'对应的是哪个业务表单？请提供表单编码或名称，以便查询准确的字段结构"
若实体名称无歧义且用户也不确定编码，可先用 queryFormsByApp 按关键词搜索，将结果展示给用户选择
确认后再查询字段：只有在明确了表单编码后，才执行 getEntityFields 查询字段结构
前后端统一编排

当需求同时涉及前端组件和后端 Controller 时，按以下流程执行（元数据先于代码）：

若无工程，执行 kd project init
创建工程结构（本 Skill 职责）： a. 对每个前端组件执行 kd project create <ComponentName> --type kwc b. 对每个后端 Controller 执行 kd project create <ControllerName> --type controller
查询业务实体字段（当 Controller 涉及实体数据操作时）：
用户提供了表单名称/编码/实体相关信息时，使用 meta-query-api.mjs 查询真实字段
先 queryFormsByApp 搜索表单，再 getEntityFields 获取字段结构（见「元数据查询」章节）
查询结果用于指导后续 Controller 元数据和代码编写，禁止猜测字段名
补全所有元数据（本 Skill 职责，元数据先行）： a. 补全组件元数据 .js-meta.kwc b. 补全 Controller 元数据 .kws（定义 URL、方法、权限配置）
移交前端代码实现：加载框架开发 Skill 编写组件代码（*.tsx / *.vue / *.js）
移交后端代码实现：加载 kwc-ks-controller-development 编写 Controller 脚本（*.ts）
回到本 Skill：创建页面元数据并补全 <controls>
构建前端：npm run build:frontend
确认或创建目标环境，完成认证
执行 kd project deploy
部署成功后，调用 form-link.mjs 输出渲染卡片（见「部署完成标准输出」章节）

关键原则：

步骤 4（元数据补全）中，组件元数据 .kwc + Controller 元数据 .kws 都由本 Skill 完成
步骤 5-6（代码实现）分别移交给对应的开发 Skill，本 Skill 严禁直接编写代码
步骤 7 起回到本 Skill 主导
仅前端编排

若确认不涉及后端，仅前端开发时，优先按这条顺序执行：

若无工程，执行 kd project init
对每个"会出现在页面里的组件"执行 kd project create <ComponentName> --type kwc
补全组件 .js-meta.kwc（本 Skill 职责）
查询关联业务实体（可选，当组件涉及表单数据绑定时）：使用 meta-query-api.mjs 查询关联表单的字段结构，辅助组件设计（见「元数据查询」章节）
移交代码实现：确认当前工程 framework，必须加载并切换到对应框架开发 Skill（kwc-react-development / kwc-vue-development / kwc-lwc-development）
框架 Skill 实现组件代码（*.tsx / *.vue / *.js）
代码实现完成后，回到本 Skill：执行 kd project create <page-name> --type page
补全页面 app/pages/<page-name>.page-meta.kwp
确认或创建目标环境，完成认证
构建前端：npm run build:frontend
若元数据有变更或需要更新环境上的静态文件，执行 kd project deploy（部署到开发环境时会同时上传前端静态文件）
当次任务所有部署完成后，调用 form-link.mjs 输出渲染卡片（见「部署完成标准输出」，不可跳过）
仅当用户明确要求查看效果时执行 kd open，明确要求本地联调时执行 kd debug（须后台模式）

关键原则：

步骤 3（元数据补全）必须由本 Skill 完成
步骤 5-6（代码实现）必须由框架 Skill 完成，本 Skill 严禁直接编写代码
步骤 7 起（页面创建及后续）回到本 Skill 主导

如果是修改已有页面：

先识别是改组件实现、改组件元数据、改页面元数据，还是三者都改
若涉及组件代码修改：必须加载对应框架 Skill，禁止本 Skill 直接修改代码
参考"是否需要 deploy 决策"决定后续操作
仅后端 Controller 编排

若确认仅涉及后端，不需要新增前端组件时：

若无工程，执行 kd project init
执行 kd project create <ControllerName> --type controller 创建 Controller
查询业务实体字段（当 Controller 涉及实体数据操作时）：使用 meta-query-api.mjs 先搜索表单再获取字段结构（见「元数据查询」章节），禁止猜测字段名
补全 Controller 元数据 .kws（本 Skill 职责）
移交代码实现：必须加载并切换到 kwc-ks-controller-development
controller-development Skill 编写脚本代码（*.ts）
代码实现完成后，回到本 Skill：执行 kd project deploy 部署到目标环境（Controller 无需预先 build）
当次任务所有部署完成后，调用 form-link.mjs 输出渲染卡片（见「部署完成标准输出」，不可跳过）
配置环境

在部署前先完成环境配置。

环境存在性检查

当用户提供了具体的环境名称或别名（如 dev、sit、uat 等）时，应先执行环境存在性检查：

运行 kd env list 查看当前已配置的环境列表
若目标环境已存在于列表中：
不需要再让用户提供 URL、Client ID/Secret 等环境信息
直接使用该环境进行后续操作（如 deploy、debug）
若该环境不是当前默认环境，可通过 kd env set target-env <name> 切换
使用 kd env info 确认环境认证状态
只有当环境不存在时，才进入完整的环境创建和认证流程
新建环境流程

当环境不存在时，按以下流程执行：

使用 kd env create <env-name> --url <url> 创建环境别名。
使用 kd env auth openapi 走交互式认证。
若用户经常切换环境，可用 kd env set target-env <env-name> 设置默认环境。
必要时使用 kd env list 和 kd env info 检查当前配置。

优先采用 openapi 认证方式；web 模式暂不作为默认路径。

需要收集环境信息的情况

如果目标环境不存在，或环境存在但尚未完成认证，先停下来收集这些字段：

环境别名
环境 URL
Client ID
Client Secret
Username

其中 data center 不属于预先手填字段，而属于“读取后选择”的字段：

先有环境 URL
再进入 kd env auth openapi
由脚手架读取该环境可用的数据中心列表
最后让用户从列表中选择

收集规则：

环境别名、环境 URL、Client ID、Client Secret、Username 这些值必须由用户手工提供
data center 不要让用户自由输入，应让脚手架读取候选项后再选择
不要使用历史环境中的凭据去猜测新环境
不要因为存在 dev、sit、base 等别名，就自动推断这次要绑定哪个环境

交互方式规则：

不要假设当前一定支持弹窗或表单式输入
在当前常规模式下，先让用户回填手工字段，再在 kd env auth openapi 的交互里选择数据中心
若运行环境明确支持结构化选择工具，可以在读到数据中心列表后把候选项展示给用户选择
即便如此，Client Secret 这类自由文本仍应让用户手填

推荐向用户索要环境信息的格式：

请补充以下环境信息：
1. env name:
2. env url:
3. client id:
4. client secret:
5. username:

说明：data center 不需要先手填，后续会由脚手架读取候选项供选择。


补充：环境配置保存在 ~/.kd 而非项目目录；创建后必须用 kd env list 复核是否持久化成功；kd env auth openapi 在 URL 不可达时会直接失败。

部署与调试
构建命令

开发阶段只需要构建前端，Controller 由 deploy 直接处理：

场景	构建命令	说明
改了前端代码（.tsx/.vue/.js）	npm run build:frontend	构建前端静态资源，输出到 dist/kwc/
改了 Controller 代码（.ts）或 .kws	不需要 build	开发阶段 deploy 直接处理 Controller
仅改元数据文件（.kwc/.kwp/.kws）	不需要 build	元数据由 deploy 直接上传

补充用法：

npm run build:frontend -- MyComponent：构建指定前端组件
npm run build:controller：仅用于生产环境构建 Controller 产物，开发阶段不需要
npm run build：全量构建（前端 + Controller），仅用于生产环境
是否需要 deploy 决策
改了什么？
├── 只改前端代码（.tsx/.vue/.js/.html/.scss）
│   ├── 仅本地调试 → npm run build:frontend → kd debug（不需要 deploy）
│   └── 更新环境效果 → npm run build:frontend → kd project deploy
├── 只改 Controller 代码（.ts）或 .kws 元数据
│   → .kws version + 1 → 直接 kd project deploy（不需要 build）
├── 前端 + Controller 都改了
│   → 递增相关 version → npm run build:frontend → kd project deploy
├── 只改元数据（.js-meta.kwc / .page-meta.kwp）
│   → version + 1 → 直接 kd project deploy（不需要 build）
└── 新建组件/页面/Controller
    → version = 1 → 若有前端代码则 npm run build:frontend → kd project deploy

常用命令
kd project deploy：一次性部署整个项目的所有元数据（.js-meta.kwc + .page-meta.kwp + .kws）和前端静态文件到默认环境；开发阶段 Controller 由 deploy 直接处理，无需预先 build
kd project deploy -d app/kwc/MyComponent -e sit：仅部署指定组件到 sit
kd project deploy -d app/pages/my_page -e sit：仅部署指定页面元数据到 sit
kd project deploy -d app/ks/controller/MyController -e sit：仅部署指定 Controller 到 sit
kd open -e dev -f kdtest_demo_page：部署后直接打开环境上的表单查看效果（无 DNS 代理）
kd debug：进入本地调试，通过 DNS 代理连接环境（必须使用 is_background: true 运行，仅当用户明确要求调试时使用）
部署完成标准输出

每当 AI 完成一段工作并且部署成功后，必须调用 form-link.mjs 脚本生成渲染卡片并输出给用户，展示已部署页面的访问入口。渲染卡片是用户触发预览效果的入口。

关键规则：

完成即输出：每完成一段可预览的工作（该段涉及的所有 deploy 均已成功），立即输出渲染卡片。多轮对话中，每段完成的工作都应有渲染卡片输出，不要攒到最后才输出
同一段工作内不重复：如果一段工作涉及多次 deploy（如先部署组件、再部署页面、再部署 Controller），应在该段全部部署完成后输出一次，不要每执行一条 deploy 命令就输出一次
适用于任何 deploy 形式：整体部署（kd project deploy）、指定路径部署（-d app/kwc/...、-d app/pages/...、-d app/ks/controller/...）
调用命令
# 页面无关联实体时（纯展示页、配置页等）
node "{form_link}" generate --pageMeta app/pages/<page-name>.page-meta.kwp [--env <envName>]

# 页面关联了业务实体时（如销售订单、采购申请等）
node "{form_link}" generate --pageMeta app/pages/<page-name>.page-meta.kwp --formNumber <entity-formNumber> [--env <envName>]

metadata 字段判断规则
metadata 字段是条件性的，仅当页面关联了业务实体时才输出
--formNumber 传入的是实体的 formNumber（如 sal_salorder），不是页面元数据的 <name>
必须传入 --formNumber 的场景（满足任一即必须传入）：
用户需求提及了任何已有的表单、实体或元数据名称（如"销售订单"、"采购申请"等业务对象）
开发过程中使用了 meta-query-api.mjs 查询过表单/字段（如 queryFormsByApp、getEntityFields）
Controller 配置了 entityNumber
用户明确提供了表单编码 / formNumber
已有实体主动查询规则：当需求涉及一个已经存在的实体、元数据或表单时，必须先通过 meta-query-api.mjs 的 queryFormsByApp 搜索表单获取 formNumber，再将其传入 --formNumber。不能因为开发过程中没有调用过 getEntityFields 就忽略该参数
不确定就查：当不确定页面是否关联已有实体时，应优先通过 queryFormsByApp 查询确认，而不是默认不传
可不传 --formNumber 的场景（仅以下情况才可省略）：
明确是纯展示页、配置页、仪表盘等无关联实体的页面
页面是全新创建的，不基于任何已有实体
执行顺序
当段工作所有 deploy 完成 → 调用 form-link.mjs 输出渲染卡片（强制） → 询问菜单发布（可选）

强制约束
每段工作的部署完成后必须输出渲染卡片，不可省略或跳过
多轮对话中每段完成的工作都应输出，不要只在最终结束时才输出
同一段工作内不重复输出（多条 deploy 命令属于同一段工作时，等全部完成后输出一次）
脚本输出内容必须直接呈现给用户
所有值从实际文件和环境中读取，禁止猜测
查看环境效果（kd open）

注意：部署后默认仅输出渲染卡片（见「部署完成标准输出」），不自动执行 kd open。仅当用户明确要求查看环境效果时才使用本命令。

部署后使用 kd open 查看环境上的表单效果：

kd open -e <env> -f <page_name>：直接在浏览器中打开对应环境上已部署的表单页面
-e 指定目标环境（必填），-f 传入页面元数据 <name> 值（必填），取值规则与 kd debug -f 一致
不需要本地 dev server 运行，不走 DNS 代理
使用前提：已通过 kd project deploy 将元数据和静态文件部署到目标环境

适用场景：用户说"看看效果"、"打开页面"、"查看环境上的表单"、"看看部署结果"等。

本地调试（kd debug）

仅当用户明确说"调试"、"本地调试"、"联调"、"实时预览代码修改"时才使用 kd debug：

运行 kd debug 时必须使用后台模式（is_background: true），因为这是一个持续运行的开发服务器，不会自动结束
若使用前台模式运行 kd debug，命令会在 90 秒后因超时被强制终止，导致本地服务被 kill
kd debug 启动后会先打开浏览器访问对应地址，但此时本地开发服务可能尚未完全启动，页面可能暂时无法访问。应等待服务启动完成后再刷新浏览器
可以通过 get_terminal_output 查看 kd debug 的运行状态和输出
若目标环境不是当前默认环境，先执行 kd env set target-env <env-name>
不要手工拼调试 URL，由 AI 自行结合任务和页面元数据判断预览目标
浏览器自动打开后继续定位目标页面
触发决策

前置条件（必须在触发 open/debug 前完成）：

已完成代码编写
已执行必要的 build 命令（若修改了代码）
已执行 kd project deploy（若需要部署）
已输出渲染卡片（见「部署完成标准输出」，部署后必须先输出渲染卡片再执行 open/debug）
环境已认证
用户意图判断：
├── "看效果/打开页面/查看部署结果/看看环境上的表单" → kd open
├── "调试/联调/本地调试/实时预览修改" → kd debug
└── 未明确表达 → 默认输出渲染卡片即结束，不自动执行 kd open 或 kd debug


补充：环境未认证时 kd project deploy 会直接阻止部署。

应用菜单管理

菜单管理将部署后的页面注册到应用导航菜单，使页面在苍穹环境中可被用户导航访问。 所有菜单操作通过 scripts/menu-api.mjs 脚本完成，详细命令参考见 references/app-menu.md。

触发条件
kd project deploy 成功后，引导用户是否将页面发布到应用菜单
用户直接说"发布菜单"、"添加菜单"、"菜单管理"、"查看菜单"、"修改菜单"、"删除菜单"、"移动菜单"
前置条件
环境已认证（kd env auth openapi 已完成）
bizAppNumber 已知（来自 .kd/config.json 的 app 字段，或用户明确提供）
接口依赖关系（强制约束）

所有菜单操作必须遵循「先查后改」原则，禁止跳过查询直接执行写操作。

queryTree（必须）→ 获得 menuId / 菜单结构 → 执行写操作 → getMenu 或 queryTree 验证结果

约束	说明
menuId 只能从接口获取	menuId 只能来自 queryTree 返回的菜单树、addMenu 返回的新建菜单、或 getMenu 返回的详情。禁止凭记忆或猜测构造 menuId
修改/删除/移动前必须先查询	执行 updateMenu、deleteMenu、moveMenu 前，必须先执行 queryTree 获取当前菜单树，从返回结果中确认目标 menuId 存在且状态正确
新增后必须捕获 menuId	addMenu 成功后，必须从响应中提取新菜单的 menuId 并记录，供后续修改/移动使用
写操作后必须验证	任何写操作（add/update/delete/move）完成后，必须执行 getMenu 或 queryTree 验证实际状态，不能仅凭返回的 success 判断
parentMenuId 必须来自查询	新增子菜单时，parentMenuId 必须从 queryTree 的返回结果中获取已有菜单的 menuId，禁止猜测
Step 1: 上下文准备
读取 .kd/config.json 的 app 字段作为 bizAppNumber
若从部署流程进入：formNumber = deploy 后 .page-meta.kwp 中 <name> 标签的实际值（已含 ISV 前缀）
若用户直接触发菜单管理：仅已知 bizAppNumber，进入 Step 2 查询菜单树

⚠ formNumber 必须从 deploy 后的 .page-meta.kwp 文件中读取 <name> 标签的实际值，不要自行拼接 ISV 前缀。

Step 2: 查询并展示菜单树（任何操作的前置步骤）

无论用户要求什么菜单操作，都必须先执行此步骤获取当前菜单状态。

node "{menu_api}" queryTree --bizAppNumber {bizAppNumber}

按层级缩进展示，用图标区分类型（📁 分组 / 📄 页面 / 🔗 链接），展示规范见 references/app-menu.md
记录所有菜单的 menuId，后续操作必须使用这里获取到的 menuId
展示后根据来源引导下一步：
部署后进入 → 根据表单名称和现有菜单结构，推荐菜单放置位置（分析语义关联，推荐同类分组；菜单树为空则推荐创建一级菜单）。推荐前须检查目标位置层级深度（不超过 3 级）
用户直接触发 → 展示菜单树后等待用户指示操作
Step 3: 执行菜单操作

根据用户意图执行对应操作（所有 menuId 必须来自 Step 2 的查询结果）：

操作	命令	执行前检查
新增	addMenu --bizAppNumber {app} --name {name} --formNumber {form} [--parentMenuId {pid}] [--seq {n}]	确认菜单名称和位置；检查层级不超 3 级；parentMenuId 必须来自 queryTree 结果；批量新增同级菜单时必须传递从小开始的递增 --seq 值（如 1、2、3），禁止使用大数值，范围 1–32767
修改	updateMenu --bizAppNumber {app} --menuId {id} [--name ...] [--visible ...] [--seq {n}]	menuId 必须来自 queryTree 结果；修改 visible 为 0 时警告级联隐藏；修改 parentMenuId 时检查循环引用和层级
删除	deleteMenu --bizAppNumber {app} --menuId {id}	menuId 必须来自 queryTree 结果；检查 HPCE 保护；警告级联删除子菜单；需用户确认
移动	moveMenu --bizAppNumber {app} --menuId {id} --direction {up/down}	menuId 必须来自 queryTree 结果；展示当前排序位置；若报错「序号一致」，先用 updateMenu --seq 修改相邻菜单序号再重试

每次操作前均需将配置方案展示给用户确认，用户确认后再执行。

Step 4: 验证并展示结果
任何写操作完成后必须验证实际结果：
删除操作：优先用 getMenu 确认目标菜单返回 MENU_NOT_FOUND（菜单树可能存在短暂缓存延迟）
其他写操作：执行 getMenu（单个菜单）或 queryTree（全局）验证
addMenu 成功后，从响应中提取并记录新菜单的 menuId
展示完成信息，并提供后续操作选项：
修改此菜单
移动菜单位置
删除此菜单
继续添加其他菜单
查看完整菜单树
完成
与部署流程的集成

kd project deploy 成功后：

先输出渲染卡片：调用 form-link.mjs 生成部署完成渲染卡片（见「部署完成标准输出」章节）
再引导菜单发布：询问用户是否需要将页面发布到应用菜单

部署成功。是否需要将页面发布到应用菜单？

若用户同意 → 自动进入 Step 1（bizAppNumber 和 formNumber 均已可从当前上下文获取）。

约束速查
约束	何时提醒
菜单最多 3 级	新增或移动菜单时检查
HPCE 菜单不可删除	删除前检查 menuId 是否以 HPCE 结尾
级联隐藏	修改 visible 从 1→0 时警告
级联删除	删除有子菜单的菜单时警告
formNumber 取实际值	新增页面菜单时
元数据查询

元数据查询用于在已认证环境中搜索表单和获取实体字段结构，为 KS 脚本编写、页面开发等提供上下文信息。 所有查询操作通过 scripts/meta-query-api.mjs 脚本完成，详细命令参考见 references/meta-query.md。

触发条件
用户提到表单名称（如"销售订单"）但未提供 formNumber
需要查询某个表单的字段结构
KS Controller 开发前需了解目标表单的实体字段
页面开发时需了解关联表单的数据模型
前置条件
环境已认证（kd env auth openapi 已完成）
appNumber 已知（来自 .kd/config.json 的 app 字段，或用户明确提供）
工作流
Step 1: 搜索表单

优先使用 queryFormsByApp 在当前应用范围内搜索：

node "{meta_query_api}" queryFormsByApp --appNumber {appNumber} --keyword {keyword}

appNumber 从 .kd/config.json 的 app 字段获取
keyword 为用户提到的表单名称关键词（可选，不传则列出应用下所有表单）
Step 2: 确认目标表单

根据返回结果数量处理：

场景	处理方式
返回单条	直接确认为目标表单，提取 formNumber
返回多条	列表展示让用户选择（序号 / 表单名称 / 表单编码 / 模型类型 / 所属应用）
返回空	提示未找到，建议尝试换关键词重试
Step 3: 获取实体字段（按需）

确认目标表单后，根据需要获取字段结构：

node "{meta_query_api}" getEntityFields --formNumber {formNumber}


返回结果按单头和单据体分组展示字段的 key、类型、是否必录等信息。

灵活使用
用户也可以只执行 Step 1-2（仅查询表单列表），不必每次都查字段
若用户已知 formNumber，可直接执行 Step 3 获取字段结构
查询结果可用于 KS 脚本编写、页面开发、或单纯了解表单结构
与其他流程的集成
KS Controller 开发：开发前先查询目标表单字段结构，了解单头/单据体/子分录的字段 key 和类型
页面开发：查询关联表单了解数据模型，辅助组件设计
独立使用：用户只想了解某个表单结构时，可独立调用
端到端执行原则

当用户说“帮我开发一个 KWC 页面/功能”时，默认按这条链路推进：

识别是新工程还是已有工程
收集不可推断的环境输入
评估需求是否涉及后端数据交互，若是则规划 Controller
拆分组件并创建组件工程；若需要 Controller，一并创建 Controller 工程
补全所有元数据：组件元数据 .js-meta.kwc、Controller 元数据 .kws（若有）
实现前端组件代码（移交框架 Skill）
若有 Controller，实现 Controller 脚本代码（移交 kwc-ks-controller-development）
创建并补全页面元数据
若有 Controller，执行 npm run build:controller
配置环境并确认认证状态
若元数据有变更，执行 deploy
部署成功后，调用 form-link.mjs 输出渲染卡片（见「部署完成标准输出」章节）
仅当用户明确要求查看效果时，执行 kd open
仅当用户明确要求本地联调时，执行 kd debug

不要只完成其中的"创建组件"或"本地跑起来"，除非用户明确只要某个局部步骤。

输出要求

输出方案或执行命令时，尽量同时给出：

用户还需要补充哪些关键输入
当前处于哪个阶段
下一条应执行的命令
是否依赖已有环境认证
是否需要修改 page-meta.kwp
页面元数据将如何组合组件
是否真的需要 deploy
若需要部署，是否因为元数据变更而必须递增 version
部署成功后是否已输出 :::render:kdform 渲染卡片（见「部署完成标准输出」章节）
故障排查速查表
症状	可能原因	解决方案
kd project deploy 提示未认证	环境未执行 auth	kd env auth openapi
页面元数据上传失败	version 未递增	递增 version 后重试
页面显示空白	control.type 与组件 name 不匹配	检查大小写完全一致
组件属性不生效	属性未在 .js-meta.kwc 声明	添加 <property> 定义
name 校验失败	格式不符	字母开头，仅小写+数字+下划线，≤30字符
isv 不一致	页面与环境开发商不匹配	deploy 会自动替换，无需手填
在非 KWC 工程目录执行命令	缺少 .kd 目录	先执行 kd project init
创建了页面但组件不显示	未把组件写入 <controls>	编辑 page-meta.kwp 添加 control
kd debug 提示端口占用	3333 端口被占用	关闭占用进程或重启终端
kd debug 启动后无法找到目标表单 / 进入了错误的表单	未使用 -f 参数指定页面元数据 name，或传入了文件名而非元数据 name 值	使用 kd debug -f <page_name>，其中 <page_name> 为当前本地 .page-meta.kwp 文件中 <name> 节点的实际值。注意：deploy 后脚手架会自动更新本地文件中的 name（拼接 isv 前缀），因此应使用 deploy 后的完整名称，如 kdtest_demo_page
kd open 打开页面后显示空白	未部署或静态文件未上传	先执行 kd project deploy 确保元数据和静态文件已上传
kd open 提示表单不存在	-f 参数值不正确	传入页面元数据 <name> 节点的实际值（deploy 后的完整名称）
表单名称与 ISV 前缀说明
创建阶段：.page-meta.kwp 中的 <name> 可填写业务标识，如 demo_page
Deploy 阶段：脚手架自动从环境拉取 isv（如 kdtest），拼接成 kdtest_demo_page 上传到远端，并同步更新本地文件
Debug/Open 阶段：kd debug -f 和 kd open -f 均应传入当前本地文件中的 <name> 值（即 deploy 后的完整名称）
如果不确定，直接打开 .page-meta.kwp 查看 <name> 节点即可
快速导航

按常见场景快速定位参考文档：

新工程初始化 → cli-reference.md（project init）+ 本文「初始化工程」章节
添加组件 → cli-reference.md（project create）+ component-metadata.md
创建页面 → page-metadata.md + 本文「创建页面元数据」章节
环境配置与部署 → env-setup.md + cli-reference.md（deploy/open/debug）+ 本文「配置环境」「部署与调试」章节
应用菜单管理 → app-menu.md + 本文「应用菜单管理」章节
元数据查询 → meta-query.md + 本文「元数据查询」章节
参考资料
主题	参考文件
CLI 命令语法、参数、示例	references/cli-reference.md
组件元数据字段与属性类型	references/component-metadata.md
环境信息收集与认证流程	references/env-setup.md
页面元数据字段、controls 规则、命名规范	references/page-metadata.md
应用菜单管理命令与展示规范	references/app-menu.md
元数据查询命令与响应格式	references/meta-query.md
Weekly Installs
75
Repository
kingdee/kwc-skills
GitHub Stars
2
First Seen
Mar 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn