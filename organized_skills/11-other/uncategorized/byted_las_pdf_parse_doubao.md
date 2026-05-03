---
rating: ⭐⭐⭐
title: byted-las-pdf-parse-doubao
url: https://skills.sh/bytedance/agentkit-samples/byted-las-pdf-parse-doubao
---

# byted-las-pdf-parse-doubao

skills/bytedance/agentkit-samples/byted-las-pdf-parse-doubao
byted-las-pdf-parse-doubao
Installation
$ npx skills add https://github.com/bytedance/agentkit-samples --skill byted-las-pdf-parse-doubao
SKILL.md
LAS AI PDF 解析（las_pdf_parse_doubao）

将 PDF 解析为 Markdown 格式文本，保留标题/段落/表格结构。支持 normal（快速）和 detail（深度分析）两种模式。

设计模式

本 skill 主要采用：

Tool Wrapper：封装 lasutil CLI 调用
Pipeline：包含 Step 0 → Step N 的顺序工作流
核心 API 与配置
算子 ID: las_pdf_parse_doubao
API: 异步（submit → poll）
环境变量: LAS_API_KEY (必填)

详细参数与接口定义见 references/api.md。

Gotchas
模式选择：normal 速度快，推荐默认；detail 适合复杂排版文档，耗时更长且费用翻倍。
密钥安全：若聊天框屏蔽密钥，让用户在当前目录创建 env.sh 并写入 export LAS_API_KEY="..."，SDK 会自动读取。
免责声明：最终回复结果时必须包含："本方式的计费均为预估计费，与实际费用有差距，实际费用以运行后火山产生的账单为准。计费说明请参考 Volcengine LAS 定价。"，且禁止使用"实际费用"字眼描述预估价。
工作流（严格按步骤执行）

复制此清单并跟踪进度：

执行进度：
- [ ] Step 0: 前置检查
- [ ] Step 1: 初始化与准备
- [ ] Step 2: 预估价格
- [ ] Step 3: 提交任务
- [ ] Step 4: 异步查询
- [ ] Step 5: 结果呈现

Step 0: 前置检查（⚠️ 必须在第一轮对话中完成）

在接受用户的任务后，不要立即开始执行，必须首先进行以下环境检查：

检查 LAS_API_KEY 与 LAS_REGION：确认环境变量或 .env 中是否已配置。
若无，必须立即向用户索要（提示：LAS_REGION 常见为 cn-beijing）。
注意：LAS_REGION 必须与您的 API Key 及 TOS Bucket 所在的地域完全一致。如果用户中途切换了 Region，必须提醒用户其 TOS Bucket 也需对应更换，否则会导致权限异常或上传失败。
检查输入路径：
如果用户要求处理的是本地文件，则需要先通过 File API 上传至 TOS（只需 LAS_API_KEY，无需额外 TOS 凭证）。
如果算子的输出结果存放在 TOS 上，且用户需要下载回本地，则需要 VOLCENGINE_ACCESS_KEY 和 VOLCENGINE_SECRET_KEY。对于仅需要上传输入文件的场景，TOS 凭证不再必须。
确认无误后：才能进入下一步。
Step 1: 初始化与准备

环境初始化（Agent 必做）：

# 执行统一的环境初始化与更新脚本（会自动创建/激活虚拟环境，并检查更新）
source "$(dirname "$0")/scripts/env_init.sh" las_pdf_parse_doubao
workdir=$LAS_WORKDIR


如果网络问题导致更新失败，脚本会跳过检查，使用本地已安装的 SDK 继续执行。

处理本地文件时：使用 File API 上传（只需 LAS_API_KEY，无需 TOS 凭证和 Bucket）：
lasutil file-upload <local_path>

上传成功后返回 JSON，取其中的 presigned_url（HTTPS 预签名下载链接，24 小时有效）传给算子作为输入 URL。
Step 2: 预估价格（⚠️ 必须获得用户确认）
读取 references/prices.md 获取最新计费标准。
获取 PDF 页数：
lasutil pdf-pages <pdf_url>

根据 parse_mode 单价计算总价，将计费单价与预估总价一并告知用户并强制暂停执行，明确等待用户回复确认。在用户明确回复"继续"、"确认"等同意指令前，绝对禁止进入下一步（执行/提交任务）。提示：预估仅供参考，实际以火山账单为准。计费说明请参考 Volcengine LAS 定价。
Step 3: 提交任务 (Submit)

构造基础 data.json：

{
  "url": "<presigned_url>",
  "parse_mode": "normal"
}

data=$(cat "$workdir/data.json")
lasutil submit las_pdf_parse_doubao "$data" > "$workdir/submit.json"


⚠️ 强制反馈：任务提交成功后，必须立即向用户返回生成的 task_id，以便用户跟踪进度或在必要时手动查询。

Step 4: 异步查询 (Poll)

⚠️ 异步任务与后台轮询约束：

如果你当前的环境支持后台任务/异步长效运行：你可以利用环境提供的后台能力（例如发起后台轮询任务），并在任务完成后主动将结果返回给用户。
如果你当前的环境不支持长效后台任务（如普通的单轮对话沙箱），且直接 sleep 循环会导致超时崩溃：绝对禁止在代码中执行死循环等待！ 此时必须立即向用户输出 Task ID 并结束当前轮次，告知用户："任务已提交，请稍后向我询问进度"。
mkdir -p "./output/{task_id}"
lasutil poll las_pdf_parse_doubao {task_id} > "./output/{task_id}/result.json"
# 若解析完成，提取 Markdown
cat "./output/{task_id}/result.json" | jq -r '.data.markdown // empty' > "./output/{task_id}/parsed.md"

COMPLETED → 结果已保存至 ./output/{task_id}/parsed.md。
RUNNING/PENDING → 稍后重试。
Step 5: 结果呈现

处理结果：

# 保存结果到本地
mkdir -p "./output/{task_id}"
cat "./output/{task_id}/result.json" | jq -r '.data.markdown' > "./output/{task_id}/parsed.md"
cat "./output/{task_id}/result.json" | jq '.data.detail' > "./output/{task_id}/pages_detail.json"


上传结果文件（可选）：

# 上传 Markdown 文件供用户下载
lasutil file-upload "./output/{task_id}/parsed.md"
lasutil file-upload "./output/{task_id}/pages_detail.json"


向用户展示：

Markdown 内容摘要（前 500 字）
总页数
本地文件路径：./output/{task_id}/
签名下载链接（如上传成功）
⚠️ 图片链接有过期时间，如需保留请立即下载
计费声明
审查标准

执行完成后，Agent 应自检：

环境变量是否正确配置
输入文件是否成功上传
输出结果是否正确呈现给用户
计费声明是否包含
Weekly Installs
126
Repository
bytedance/agent…-samples
GitHub Stars
326
First Seen
Mar 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn