---
rating: ⭐⭐
title: dws
url: https://skills.sh/stvlynn/dingtalk-wukong-skills/dws
---

# dws

skills/stvlynn/dingtalk-wukong-skills/dws
dws
Installation
$ npx skills add https://github.com/stvlynn/dingtalk-wukong-skills --skill dws
SKILL.md
钉钉全产品 Skill

通过 dws 命令管理钉钉产品能力。

严格禁止 (NEVER DO)
不要使用 dws 命令以外的方式操作（禁止 curl、HTTP API、浏览器）
不要编造 UUID、ID 等标识符，必须从命令返回中提取
不要猜测字段名/参数值，操作前必须先查询确认
严格要求 (MUST DO)
所有命令必须加 --format json 以获取可解析输出
删除操作前必须加 --yes 并和用户确认
单次批量操作不超过 100 条记录
所有命令必须严格遵循对应产品参考文档里面规定的参数格式（如：如果有参数值，则参数和参数值之间至少用一个空格隔开）
产品总览
产品	用途	参考文件
aitable	AI表格：表格/数据表/字段/记录增删改查/模板搜索	aitable.md
calendar	日历：日程/参与者/会议室/闲忙查询	calendar.md
contact	通讯录：用户查询(当前用户/搜索/详情)/部门查询(搜索/子部门/成员列表)	contact.md
doc	文档：搜索/浏览/读取/创建/更新文档/文件夹管理/块级编辑	doc.md
chat	群聊：群管理(建群/搜索/成员增删/改群名)/消息(拉取/发送/机器人群发/Webhook)/机器人搜索	chat.md
todo	待办：创建(含优先级/截止时间)/查询/修改/标记完成/删除	todo.md
mail	邮箱：查询邮箱/搜索/查看/发送邮件	mail.md
minutes	AI听记：列表/摘要/转写/关键字/标题修改	minutes.md
report	日志：收件箱/已发送/模版查看/详情/已读统计	report.md
drive	钉盘：浏览文件/元数据/下载/创建文件夹/上传文件	drive.md
ding	DING消息：发送/撤回（应用内/短信/电话）	ding.md
devdoc	开放平台文档：搜索开发文档	simple.md
conference	视频会议：预约会议	simple.md
aiapp	AI应用：创建/查询/修改AI应用	aiapp.md
live	直播：查看直播列表	simple.md
oa	OA审批：待处理/详情/同意/拒绝/撤销/记录/已发起/任务	oa.md
attendance	考勤：打卡记录/排班查询	attendance.md
意图判断决策树

用户提到"表格/多维表/AI表格/记录/数据" → aitable 用户提到"日程/日历/会议室/约会" → calendar 用户提到"通讯录/同事/部门/组织架构" → contact 用户提到"文档/知识库/写文档" → doc 用户提到"待办/TODO/任务提醒" → todo 用户提到"邮件/邮箱" → mail 用户提到"听记/会议录音/转写/AI摘要以及用户传入听记URL（如 https://shanji.dingtalk.com/*）" → minutes 用户提到"帮我做/建/生成/生成系统/AI应用/创建应用/智能应用" → aiapp 用户提到"DING/紧急消息/电话提醒" → ding 用户提到"考勤/打卡/排班" → attendance 用户提到"群聊/群消息/群成员/聊天记录/建群/机器人发消息/Webhook/通知" → chat 用户提到"审批/OA" → oa 用户提到"开发/API/调用错误 文档" → devdoc 用户提到“校招/发布职位/我的候选人” → ai_sincere_hire 用户提到"视频会议/预约会议" → conference 用户提到"直播" → live 用户提到"日志/日报/周报/日志统计" → report 用户提到"钉盘/文件/网盘/下载文件/上传文件" → drive 用户提到"企业信用/工商信息/股东/裁判文书/风险/商标/专利/招投标/联系方式/KP" → credit 用户提到"法律咨询/法规/案例/法条/判例/法律依据" → law

关键区分: aitable(数据表格) vs doc(文档编辑) 关键区分: report(钉钉日志/日报周报) vs doc(文档编辑) vs todo(待办任务) 关键区分: drive(钉盘文件存储/上传/下载) vs doc(钉钉文档内容读写/知识库空间) 关键区分: conference(视频会议预约) vs calendar event(日历日程管理) 关键区分: chat message send(个人身份群发) vs send-by-bot(机器人发消息) vs send-by-webhook(Webhook告警)

更多易混淆场景及用户表达示例，见 intent-guide.md

核心流程

作为一个智能助手，你的首要任务是理解用户的真实、完整的意图，而不是简单地执行命令。在选择 dws 的产品命令前，必须严格遵循以下三步流程：

意图分类：首先，判断用户指令的核心 动词/动作 属于哪一类。这比关注名词更重要。
歧义处理与信息追问：如果用户指令模糊或包含多个产品的关键字，严禁猜测。必须主动向用户追问以澄清意图。这是你作为智能助手而非命令执行器的核心价值。
精准产品映射：在完成前两步，意图已经清晰后，参考产品总览和意图判断决策树 来选择产品。
充分阅读产品参考文件，通过编写代码或直接调用指令实现用户意图。
错误处理
遇到错误，加 --verbose 重试一次
仍然失败，报告错误信息给用户
禁止自行尝试替代方案
如果出现身份校验失败，可以使用 dws auth login 进行登录
详细参考 (按需读取)
references/products/ — 各产品命令详细参考
references/intent-guide.md — 意图路由指南（易混淆场景对照）
references/global-reference.md — 全局标志、认证、输出格式
references/field-rules.md — AI表格字段类型规则
references/error-codes.md — 错误码 + 调试流程
scripts/ — AI表格批量操作脚本
Weekly Installs
101
Repository
stvlynn/dingtal…g-skills
GitHub Stars
110
First Seen
Mar 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass