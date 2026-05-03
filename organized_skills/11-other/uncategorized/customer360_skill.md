---
rating: ⭐⭐
title: customer360-skill
url: https://skills.sh/site/skills.netease.im/customer360-skill
---

# customer360-skill

skills/skills.netease.im/customer360-skill
customer360-skill
$ npx skills add https://skills.netease.im/api/install/af2d38954b96d575921bf379d7725985
SKILL.md
客户360全景报告查询

根据用户输入的企业名称，调用客户360系统 API 查询并输出 HTML 全景报告。

触发条件

当用户提到以下内容时触发此 skill：

"查询XX公司"、"查下XX的信息"、"看看XX的报告"
"客户360"、"全景报告"、"企业画像"
"XX公司的客户信息"、"帮我查XX"
任何包含企业名称 + 查询/搜索/报告意图的自然语言
服务配置
服务域名: https://gate.netease.com
Context Path: /bus-360
搜索接口: GET /bus-360/api/v1/query/customer/search?keyword={企业名称}
报告接口: GET /bus-360/api/v1/report/{customerId}
执行流程
第一步：提取企业名称

从用户输入 $ARGUMENTS 中提取企业名称关键词。如果用户输入类似"帮我查下华为的信息"，提取"华为"作为关键词。如果用户直接输入公司名如"杭州网易智企科技有限公司"，直接使用全名。

第二步：搜索企业

使用 Bash 工具调用搜索接口：

curl -s -G "https://gate.netease.com/bus-360/api/v1/query/customer/search" --data-urlencode "keyword=${keyword}"

第三步：处理搜索结果

解析返回的 JSON 响应，根据 data.matched 字段判断：

情况A：精确匹配（matched: true）

直接使用返回的 data.customer.customerId，跳到第四步获取报告。

情况B：多个匹配（matched: false，data.suggestions 非空）

使用 AskUserQuestion 工具展示所有匹配项，让用户选择：

每个选项显示：公司全称（companyName）
描述中显示：行业（industryL1 / industryL2）、CRM状态（crmStatus）
用户选择后，使用对应的 customerId 进入第四步

构造 AskUserQuestion 示例：

question: "搜索到多个匹配的企业，请选择目标企业："
options:
  - label: "杭州XX科技有限公司"
    description: "行业：互联网 / SaaS | CRM状态：active"
  - label: "北京XX科技有限公司"
    description: "行业：金融 / 银行 | CRM状态：prospect"
  ...（最多展示4个选项，超过4个时取前4个最相关的，其余提示用户输入更精确的名称）

情况C：无匹配（data.suggestions 为空或不存在）

告知用户未找到该企业，建议：

检查企业名称是否正确
尝试使用企业全称重新搜索
该企业可能尚未录入系统
第四步：获取全景报告

使用 Bash 工具调用报告接口获取 HTML：

curl -s "https://gate.netease.com/bus-360/api/v1/report/${customerId}"

第五步：保存并输出报告
将获取到的 HTML 内容保存到文件：
mkdir -p output
# 文件名使用企业名称 + 时间戳，避免覆盖
echo "${html_content}" > "output/${companyName}-360报告-$(date +%Y%m%d%H%M%S).html"

告知用户：
报告已保存的文件路径
提示用户可以用浏览器打开查看（open output/xxx.html）
简要说明报告包含的主要模块：基础信息、业务概况、信息化建设、外部动态信号、竞品格局、同业对标、商机分析、风险提示
注意事项
所有 API 调用使用 curl -s（静默模式），避免输出进度条
如果 API 返回非 200 状态码或连接失败，提示用户检查网络连接或服务状态
HTML 报告是自包含的（内嵌 CSS），可直接在浏览器中打开
不要在终端中直接输出 HTML 内容（太长），始终保存到文件
Weekly Installs
16
Source
skills.netease.…d7725985
First Seen
Apr 10, 2026