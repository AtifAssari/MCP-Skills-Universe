---
rating: ⭐⭐
title: ship-position
url: https://skills.sh/charleiwang/hifleet-skills/ship-position
---

# ship-position

skills/charleiwang/hifleet-skills/ship-position
ship-position
Installation
$ npx skills add https://github.com/charleiwang/hifleet-skills --skill ship-position
SKILL.md
技能说明

不配置鉴权也可使用本技能中不需 token 的部分；船位、档案等已实现功能需配置 token 后可用。技能列表与触发词见 references/skills_index.md。

技能	状态	说明
船位 Ship Position	✅ 已实现	获取最新船舶位置
档案 Archive	✅ 已实现	船舶/公司档案
红海/波斯湾通航 Strait Traffic	✅ 已实现	海峡通航统计（曼德、苏伊士、好望角、霍尔木兹），POST；无 token 限最近 1 周，有 token 不限
区域船舶 Area Traffic	✅ 已实现	查询指定区域内的当前船舶：支持 bbox、areaId（区域清单 id）或 polygon（WKT），需 token
PSC 检查 PSC Inspection	✅ 已实现	按 IMO 查 PSC；船名/MMSI 先 shipSearch。含：统计异常 openclaw/anomalies*；宏观统计 `openclaw/stats/compare
港口 Port guide	✅ 已实现	港口列表/检索（港名或代码）、单港详情（piuid→portId）；portguide/getPort/token、portguide/getPortDetail/token
性能 Performance	待实现	油耗、能效、主机性能
航程 Voyage	待实现	航次、挂港、ETA/ETD
航线 Route	待实现	推荐航线、航路点
租船 Charter	待实现	租约、租家、租金
航运 Shipping	待实现	运价、市场、新闻
气象海况 Weather	待实现	风浪、台风、能见度
船队 Fleet	待实现	多船监控、船队报表
AIS	待实现	AIS 报文、轨迹回放
Token 配置（可选，部分接口必填）

船位、档案等已实现功能依赖 HiFleet API 鉴权；不配置 token 时这些接口不可用，但技能中其他不需鉴权的部分仍可使用。需要用到船位/档案/PSC 等时，请配置：

环境变量（二选一）：HIFLEET_USER_TOKEN 或 HIFLEET_USERTOKEN
项目/ClawHub 配置：usertoken / userToken
请求参数：接口支持时传入 usertoken

建议使用仅限本技能使用的专用 token，停用后及时轮换。

常用定义

国际航行船舶 : 通常有有效的IMO注册号码的船舶 电子围栏: 区域范围

已实现功能
船位 / Ship Position

获取（岸基+卫星+移动）船舶最新位置信息。支持**关键字（船名或 MMSI）**查询，自动走“先搜船、再查位”的两步流程。

触发：船位、位置、报位、在哪、MMSI、ship position、vessel position
输入：关键字（船名或 MMSI）或直接 9 位 MMSI；usertoken 从配置读取
API 详情：references/position_api.md（含 shipSearch 与 position/get/token）
脚本：scripts/get_position.py（支持关键字或 MMSI，可选用于命令行/集成）

两步流程：

第一步 - 搜船：用用户关键字调用 position/shipSearch（shipname、usertoken、i18n=zh、count）。
第二步 - 查位：根据结果数量处理：
0 条：提示未找到，请检查关键字。
1 条：直接取该条 mmsi，调用 position/position/get/token 查位置并展示。
多条：若可推断用户目标船（如关键字为完整 MMSI 或唯一匹配船名），则用对应 MMSI 查位；否则列出船名/MMSI/船型/船籍等，请用户选择具体 MMSI，再按所选 MMSI 调用 position/position/get/token 查位置。

若用户已提供 9 位数字 MMSI，可省略第一步，直接调用 position/position/get/token。展示时经纬度需将接口返回的 la/lo 除以 60 转为度。

档案 / Archive

根据 IMO 或 MMSI 获取船舶档案（基本信息、尺度、舱容、建造、入级、动力、公司信息、互保协会等）。接口支持 imo 与 mmsi 二选一，内贸船无 IMO 时仅传 mmsi 即可。船名不支持，需先通过 shipSearch 得到 MMSI/IMO。

触发：档案、船舶信息、船籍、船型、船东、管理公司、archive、vessel profile、ship info
输入：IMO（7 位）或 MMSI（9 位）；usertoken 从配置读取
API 详情：references/archive_api.md
脚本：scripts/get_archive.py（支持 IMO 或 MMSI，MMSI 直接传 mmsi 参数，需 token）

调用流程：检查 token → 若为 IMO：GET ...?imo={imo}&usertoken=...；若为 MMSI：GET ...?mmsi={mmsi}&usertoken=...（支持内贸船无 IMO）→ 解析 data，按 labelZh 分块展示。船名需先 shipSearch 得到 MMSI/IMO 再查档案。

红海与波斯湾海峡通航 / Strait Traffic

咽喉航道通航船舶统计，支持曼德海峡、苏伊士运河、好望角、霍尔木兹海峡，按日期区间与方向返回船型统计及船舶明细。无 usertoken 仅可查最近 1 周，有 usertoken 时间区间不限。

触发：红海、波斯湾、海峡通航、曼德海峡、苏伊士运河、好望角、霍尔木兹、strait traffic、Red Sea、Persian Gulf
输入：海峡名称或 oid；可选开始/结束日期（yyyy-MM-dd），不传默认最近 7 天；可选 i18n（zh/en）。usertoken 从配置读取，有则时间不限。
API 文档：references/strait_traffic_api.md；完整接口以 ShowDoc 45/2234 为准。
脚本：scripts/get_strait_traffic.py（海峡名或 oid + 可选 startdate/enddate/i18n，有 token 可查超 7 天）

接口：POST http://api.hifleet.com/position/statisticzonetraffic，Query 参数 oid、startdate、enddate、i18n（可选）、usertoken（可选）。海峡 oid：曼德海峡 24480、苏伊士运河 132808、好望角 1062830、霍尔木兹海峡 24471。无 token 时校验时间区间 ≤ 7 天。

区域船舶 / Area Traffic

查询当前指定区域内的船舶列表。支持三种区域指定方式：矩形 bbox、区域 id（areaId） 或 WKT 多边形（polygon）。用户仅文字描述区域（如 [波斯湾]「红海」「北太平洋」「马六甲海峡」）时，先查区域清单再按 areaId 查询。

触发：区域船舶、范围内船舶、区域船位、某区域有多少船、area traffic、vessels in area
输入：① 矩形区域（左下经度、左下纬度、右上经度、右上纬度）；或 ② 区域名称/海区/贸易区（先调区域清单接口，用 name/cnName 匹配得到 id，再按 areaId 查）；或 ③ WKT 格式 polygon；usertoken 必填
API 详情：references/area_traffic_api.md（gettraffic 支持 bbox、areaId、polygon）；references/areas_api.md（区域清单）
脚本：scripts/get_areas.py（获取区域清单，供按名称选区域）；scripts/get_area_traffic.py（bbox 四参数、--area-id <id> 或 --polygon "POLYGON((...))"，需 token）

调用流程：检查 token → 若用户给的是矩形坐标：组 bbox → GET position/gettraffic/token?bbox=...&usertoken=...；若用户给的是文字描述：GET position/areas/token（可选 usertoken）→ 用 name/cnName 匹配得 id → GET position/gettraffic/token?areaId={id}&usertoken=...；若用户给的是WKT 多边形：GET position/gettraffic/token?polygon=...&usertoken=... → 解析 list 展示船名、MMSI、经纬度、航速、状态、目的港等。

PSC 检查 / PSC Inspection

根据 IMO 查询船舶 港口国监督检查（PSC） 数据。接口为 GET https://api.hifleet.com/pscapi/get，必须带 usertoken（与其它需鉴权接口一致）。支持用户直接提供 IMO，或提供船名/关键字、9 位 MMSI 时先走 position/shipSearch，从命中结果的 imonumber 取得 IMO 再请求 PSC；无 IMO 的内贸船无法调本接口。

触发：PSC、港口国监督、港口国检查、滞留、缺陷、检查记录、port state control、PSC inspection、detention、deficiency
输入：IMO（6～7 位数字，可带 IMO 前缀）；或船名/关键字；或 9 位 MMSI（与船位技能相同，先搜船再取 IMO）；usertoken 从配置读取
API 详情：references/psc_api.md
脚本：scripts/get_psc.py（IMO / 船名 / 船名 + MMSI / MMSI）

调用流程：检查 token → 若用户已给 IMO：GET pscapi/get?imo={imo}&usertoken=... → 解析并展示（脚本对常见 status+data / list 结构做分条输出，否则整段 JSON）。若用户给 船名或 MMSI 关键字：与船位相同的搜船规则（0/1/多条、多条时让用户选 MMSI）→ 取选定船的 imonumber；若为空则提示无 IMO、无法查 PSC → 有 IMO 再调 pscapi/get。

权限：若接口返回 code 4001（token 无权访问该 URL），说明当前 token 未开通 PSC API，需在 HiFleet 开通权限或更换 token（详见 references/psc_api.md）。

港口指南 / Port guide

港口列表检索与单港详细信息。两步：列表可选 portName（港口名称）、portCode（港口代码），传其一即可筛选，均不传返回全部港口（数据可能很大，宜带条件）；详情用列表项中的 piuid 作为 Query 参数 portId（整数）调用详情接口。

触发：港口、港名、港口代码、UN/LOCODE、泊位、锚地、港口信息、port guide、port detail
输入：列表步可选港名、港口代码；详情步必选港口 id（来自上一步的 piuid）；usertoken 从配置读取；可选 HIFLEET_API_BASE
API 详情：references/port_api.md
脚本：scripts/get_port.py（子命令 search [--port-name] [--port-code]、detail <portId>）

调用流程：检查 token → 列表：GET {BASE}/portguide/getPort/token?usertoken=...（按需加 portName、portCode）→ 展示命中列表（含 piuid、港名、代码等以实际字段为准）→ 详情：用户确认目标后 GET {BASE}/portguide/getPortDetail/token?portId={piuid}&usertoken=... → 解析并展示详情字段。

PSC 统计异常（OpenClaw，同属 PSC 技能）

基于日批统计的 异常事件表（psc_anomaly_event），与「单船 PSC 记录」互补：回答某时段、某当局/旗国/港口等维度下「滞留率/平均缺陷是否相对历史显著升高」等宏观问题。均需 usertoken（与 pscapi/get 相同）。

集装箱红海饶航 / Container ship Red Sea detour

集装箱船舶绕航红海每日统计，按日期区间与方向返回船型统计及船舶明细。无 usertoken 仅可查最近 1 周，有 usertoken 时间区间不限。

触发：红海饶航、集装箱饶航、Container ship Red Sea detour
输入：必选选开始/结束日期（yyyy-MM-dd）。usertoken 从配置读取，有则时间不限。
API 文档：references/avoidredsea_traffic_api.md；完整接口以 ShowDoc 45/2234 为准。
脚本：scripts/get_avoidredsea_traffic.py（ 必选 starttiime/endtime，有 token 可查超 7 天）

接口：POST http://api.hifleet.com/routerisk/getAvoidRedSeaDetail/token，Query 参数 startdate、enddate、i18n（可选）、usertoken（可选）。**无 token 时校验时间区间 ≤ 7 天。

OpenClaw 必知：PSC 统计相关字段语义（整页必读）
见 references/psc_stats_field_semantics.md，核心两条：

authority：在 psc、psc_daily_stats、psc_daily_stats_roll、psc_defect_distribution、psc_port_authority_daily、psc_company_daily、psc_anomaly_event、psc_anomalies 等表中，均表示 船舶当时接受检查的检查国/检查当局，不是船舶注册国；船旗国看 flag。
ship_type / 接口 shipType：在 psc（源字段 type_ins）、psc_daily_stats、psc_daily_stats_roll、psc_anomaly_event 中，均为 检查类型（如初检、后续检查），不是船舶类型（船型）。对用户勿把 authority 说成「船籍国」，勿把 shipType 说成「船型」。
若用户要「按真实船型」的统计，说明当前日批维度不提供，需后端扩展。

接口路径与参数细节仍见 references/psc_anomaly_api.md。

触发：PSC 异常、统计异常、滞留率飙升、缺陷异常、港口国监督风险、HIGH 严重度 PSC 事件、PSC anomaly、detention spike、deficiency spike、PSC statistics risk
输入：可选日期区间（yyyy-MM-dd）；可选 authority/flag/port（精确）、authorityContains/flagContains（子串 LIKE，适合「中国/China」等）、sliceType（AUTHORITY_FLAG=当局×旗国粗粒度异常；AUTHORITY_FLAG_PORT_TYPE=含港口×检查类型细切片）、severity、anomalyType 等；列表支持 page、pageSize
API 详情：references/psc_anomaly_api.md
脚本：scripts/get_psc_anomalies.py（子命令 list / summary / get <id>）

三类调用（Agent 按需组合）：

汇总：GET .../pscapi/openclaw/anomalies/summary?usertoken=...&dateFrom=...&dateTo=... → 按 severity 计数，适合先答「严重异常有多少」。
列表：GET .../pscapi/openclaw/anomalies?usertoken=...（同上筛选 + 分页）→ data.list 展示 title、dateEnd、severity、metric 等。
详情：GET .../pscapi/openclaw/anomalies/{id}?usertoken=... → 展开 description、evidence（JSON 字符串可格式化）。

数据稀疏时的回答规则（OpenClaw 必守）
psc_anomaly_event 可能只有极少行或全空，不得据此下结论「没有 PSC 风险」「监管很松」等。须遵守 references/psc_anomaly_api.md 中的 「异常表数据量过少」专节，要点如下：

情况	Agent 应做
list 的 total == 0 或 summary 全为 0	明确说：仅表示「统计异常事件表」在当前筛选/时间窗内无命中，不代表无 PSC 活动、不代表无滞留；原因可能是检测阈值严、切片样本不足、未跑全量 backfill-anomalies、或 authority/flag/port 与库内精确字符串不一致。
total 为个位数（如 1～5）	如实列出；注明 样本极少、不宜做宏观推断；可建议放宽日期、减少筛选维度，或改用单船 PSC。
用户问「中国/巴拿马」等自然语言	优先用 authorityContains/flagContains（如 China、Panama）再查异常表；宏观「某检查国对哪些船旗」优先 sliceType=AUTHORITY_FLAG；仍 0 条时再说明精确值可能不一致或模型未命中。
用户要「某船有没有被查」	不要用异常表代替：应走上文 PSC 检查（pscapi/get + IMO）。
用户问「为什么一直没有异常」	可简述：日批模型只标记相对历史基线显著升高的切片；min-inspections、Z 阈值、是否已跑异常补算均会影响条数；运维侧可调 newpsc psc.stats 或补跑 backfill-anomalies（不展开实现细节除非用户是运维）。

Base URL：默认 https://api.hifleet.com；其它部署可设环境变量 HIFLEET_API_BASE（脚本与文档均支持）。

PSC 宏观统计（OpenClaw，原始聚合 / 缺陷 / 占比）

与 异常事件表互补：直接基于 pscdata.psc（及 psc_defect_distribution）做可引用数字，支撑「哪国变严」「哪旗/哪港风险」「缺陷热点」「是否某旗占比上升」等；不替代因果推断与预测。

文档：references/psc_openclaw_stats_api.md（含与九类问题的映射与能力边界）
脚本：scripts/get_psc_openclaw_stats.py（compare / defects / mix）

Agent 路由建议：

用户意图	优先接口
国家/全局监管变严、检查量/滞留率环比	GET .../pscapi/openclaw/stats/compare（groupBy=AUTHORITY/GLOBAL，可用 authorityContains）
船旗风险排行、某旗滞留率	compare + groupBy=FLAG；结合 anomalies
中国/某国主要检查港口、哪港严	stats/compare 必调：groupBy=PORT 或 AUTHORITY_PORT + authorityContains（如 China）；禁止在未请求接口时用常识港口列表冒充数据；禁止谎称「港口接口故障」除非返回明确错误（并说明 code）。
最近查什么缺陷、缺陷码热点	GET .../pscapi/openclaw/stats/defects/top（需 newpsc 已写缺陷分布表）
是否「针对」某旗 / 检查类型占比变化	GET .../pscapi/openclaw/stats/mix/compare（mixDimension=FLAG 或 TYPE_INS）；勿断言政治针对，TYPE_INS 不是散货船等船型
统计模型认定的异常 spike	仍用 openclaw/anomalies*
某船/IMO	pscapi/get

合规：勿输出投资建议（「必避开某港」）；可陈述事实与风险提示。无「风险预测」专用接口，对未来表述须谨慎。

安全与合规

本技能仅向 api.hifleet.com（或 HIFLEET_API_BASE）的船位/档案/PSC/PSC openclaw（anomalies + stats）/海峡通航/区域船舶等接口发起只读请求（GET 或 POST）；海峡通航统计无需 token，其余需鉴权的接口使用 token。详见 SECURITY.md。

参考资料与脚本
路径	说明
SECURITY.md	安全说明（网络行为、Token 用途、无动态代码）
references/skills_index.md	技能清单（中英双语、触发词）
references/position_api.md	船位 API 完整说明与响应字段
references/archive_api.md	档案 API 说明与 data 分类
references/strait_traffic_api.md	红海/波斯湾海峡通航 API（oid、时间范围、ShowDoc 链接）
references/area_traffic_api.md	区域船舶 API（bbox、areaId、polygon、usertoken）
references/areas_api.md	区域清单 API（海区/贸易区列表，供按名称选 areaId）
references/psc_api.md	PSC 检查 API（pscapi/get，imo + usertoken）
references/psc_anomaly_api.md	PSC 统计异常 API（openclaw/anomalies*，usertoken，可选 HIFLEET_API_BASE）
references/psc_openclaw_stats_api.md	PSC 宏观统计（openclaw/stats/compare、defects/top、mix/compare）
references/psc_stats_field_semantics.md	PSC 多表字段语义：authority=检查国、ship_type=检查类型（非船型）
scripts/get_position.py	按关键字或 MMSI 获取船位（需 token）
scripts/get_archive.py	按 IMO 或 MMSI 获取船舶档案（接口支持 mmsi 参数，内贸船无 IMO 可用 MMSI，需 token）
scripts/get_strait_traffic.py	海峡通航统计（POST statisticzonetraffic），oid+日期+i18n；无 token 限 7 天，有 token 不限
scripts/get_areas.py	区域清单（海区/贸易区），供按名称匹配 areaId
scripts/get_area_traffic.py	区域船舶（bbox、--area-id 或 --polygon，需 token）
scripts/get_psc.py	PSC 检查（IMO 或船名/MMSI 先搜船取 IMO，需 token）
scripts/get_psc_anomalies.py	PSC 统计异常：list / summary / get id（需 token，可选 HIFLEET_API_BASE）
scripts/get_psc_openclaw_stats.py	PSC 宏观统计：compare / defects / mix（需 token，可选 HIFLEET_API_BASE）
Weekly Installs
8
Repository
charleiwang/hif…t-skills
GitHub Stars
1
First Seen
Mar 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail