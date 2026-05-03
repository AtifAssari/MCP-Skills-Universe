---
rating: ⭐⭐
title: byted-mediakit-voiceover-editing
url: https://skills.sh/site/skills.volces.com/byted-mediakit-voiceover-editing
---

# byted-mediakit-voiceover-editing

skills/skills.volces.com/byted-mediakit-voiceover-editing
byted-mediakit-voiceover-editing
$ npx skills add https://skills.volces.com/c/arkclaw-personal/skills/volcengine/mediakit
SKILL.md

⚠️ 凭据与安全（必读）

能力范围：VOLC_ACCESS_KEY_ID / VOLC_ACCESS_KEY_SECRET / VOLC_SPACE_NAME 用于火山引擎视频点播（上传、媒资、导出等）；ASR_API_KEY / ASR_BASE_URL 用于豆包语音大模型转写。与 VOD + ASR 流程一致。
最小权限与隔离：在控制台创建仅含所需 API 权限的访问密钥；勿将生产主账号密钥用于本技能。测试与开发请使用独立点播空间与专用子账号/密钥，避免误操作生产媒资。
本地 .env：技能从 <SKILL_DIR>/.env 读取配置（setup.sh 可在缺失时从 templates/env.md 生成空壳文件）。密钥须由用户在本地手工填入；Agent 不得在对话或仓库中写入真实 Secret，亦不得将 .env 提交到版本库。请保持 .gitignore 忽略 .env（若仓库尚无则在本技能目录补充）。

⚠️ STRICT EXECUTION RULES — NO EXCEPTIONS

Use ONLY the scripts listed below. Creating new scripts is FORBIDDEN.
Execute ALL steps IN ORDER. Skipping any step is a task FAILURE.
SKILL_DIR：指 byted-mediakit-voiceover-editing 目录路径
Output-dir：执行任何需要 --output-dir 的命令前，必须按「从上下文推导 output-dir」规则先行推断，减少用户重复输入, 默认值为 <SKILL_DIR>往上数三级，如
<SKILL_DIR> 为： ./xx/skills/byted-mediakit-voiceover-editing ，
Output-dir 则默认值为 ./output 即**./xx 的上级**。
Always cd <SKILL_DIR>/scripts before running any command in this Skill.
At each CHECKPOINT, verify output before proceeding.
If any step fails, HALT immediately and report to the user. Do NOT continue.
禁止简化版：Step 4/5/6 的所有输出必须完整、符合规范；严禁输出「简化版」「占位符」「示例」或省略内容以绕过问题。
审核页是否自动打开由 TALKING_VIDEO_AUTO_EDIT_REVIEW_AUTO_OPEN 决定（强制）：默认不打开；.env 中 TALKING_VIDEO_AUTO_EDIT_REVIEW_AUTO_OPEN=1（或 true/yes）时打开。Agent 不得额外执行 open、start、xdg-open 等命令，以脚本行为为准；可加 --no-open 覆盖。
最终输出输出结果，必须保持原样，不能做任何修改
超时时间： 音视频处理时长较长，请把宿主超时时间设置为 60 分钟

⚠️ 职责分工（重要）

组件	职责	不做
脚本（规则引擎）	ASR 准确率优化、口播剪辑候选生成（标记位置+规则置信度+删除建议）	不做最终删除/保留决策
宿主 Agent（你）	语义断句、口癖识别确认、候选复核、最终删除/保留决策	不修改脚本

核心原则：脚本提供候选（含删除建议 deleted_parts + cleaned_text），Agent 做最终决策。

⚠️允许使用的脚本

需要 切换到 <SKILL_DIR>

./scripts/setup.sh （环境检查与安装）
./scripts/pipeline_url_to_asr.py （asr）
./scripts/prepare_export_data.py（Step 6a 数据预处理，支持 --width --height --write-step6）
./scripts/merge_asr_words.py（Step 4 产出缺 words 时，从 raw 合并）
./scripts/serve_review_page.py（审核页静态服务）
./scripts/export_server.py（导出服务，接收审核页 POST）
./scripts/vod_direct_export.py（SubmitDirectEditTaskAsync / GetDirectEditResult 任务提交与查询）
从上下文推导 output-dir（减少用户操作）

默认 output 根路径：记 <PROJECT_ROOT> 为脚本推导得到的工程根目录：<SKILL_DIR> 向上两级父目录（约定技能目录与工程根之间固定相隔两层目录，中间目录名任意、代码中不写死任何一段路径名）。则默认写入 <PROJECT_ROOT>/output/。命令行里的相对路径 output/<文件名> 均以 <PROJECT_ROOT> 为基准。

Agent 不得扫描整个仓库/读取“最近文件”来推断 output-dir；只能使用对话中或上层调用方已显式提供的 --output-dir。

 推导优先级（按顺序尝试，命中即使用）：
对话历史/命令参数：本对话中已执行过 pipeline / prepare_export_data / serve_review_page 等命令，且命令行已显式传入 --output-dir output/<子目录> → 直接沿用
无法从对话历史获得：询问用户指定 --output-dir output/<子目录>（不做仓库扫描推断）
输出目录与重复处理规则

使用绝对路径

 输出路径：视频处理产物统一存放在 「产物根」 output/<文件名>/；产物根 = <PROJECT_ROOT>（脚本内部推导的项目根目录）。<文件名> 由素材来源推导：
URL：取 URL 最后一段（如 https://x.com/video.mp4 → video）
本地文件：取文件名（不含扩展名），如 /path/Test_Video_720p.mp4 → Test_Video_720p
DirectUrl（VOD FileName）：取文件名（如 test.mp4 → test）
Vid：取 Vid 值（如 v0xxx）
 重复处理（必须执行）：在写入任何输出文件/目录前，若目标已存在，必须提示用户：
目录重复（如 output/<文件名> 已存在）：「该输出目录已存在，是否删除原目录？[删除/保留并新建(01)]」
文件重复（如 step5_asr_optimized.json、step6_speech_cut.json 已存在）：「该文件已存在，是否删除/覆盖/保留并写入新目录(01)？」
用户选择前不得执行写入；超时 20 秒无回复 → 默认「保留并新建(01)」
 执行流水线时需传入 --output-dir output/<选定目录>
必经步骤（需严格按照顺序执行）

各 Step 的完整检查单与流程示意见 references/执行步骤/ 下分步文档。须严格按下列顺序执行，不得跳过；命令与 CHECKPOINT 细则以对应文件为准。

Step	说明	文档
Step 1	环境检查与依赖安装	1. 环境检查.md
Step 2	语气词 / 卡顿词确认与规则更新	2. 语气词提示与用户行为更新.md
Step 3	URL → ASR 流水线与候选生成	3. URL到ASR流水线与候选生成.md
Step 4	宿主 Agent ASR 语义纠错（必须）	4. ASR语义纠错.md
Step 5	宿主 Agent 口播剪辑	5. 口播剪辑.md
Step 5.5	审核逻辑确认（是否打开审核页）	5.5 审核逻辑确认.md
Step 6a	数据预处理	6a. 数据预处理.md
Step 6b	审核与导出	6b. 审核与导出.md
Step 6c	VOD 导出任务提交与查询	6c. VOD导出任务提交与查询.md
常见问题
现象	处理
本地文件走了 DirectUrl 模式	本地文件必须作为第一个位置参数传入；--directurl 仅用于 VOD 空间内已有 FileName，禁止传本地路径
step5 写入失败	必须写入 output/<文件名>/step5_asr_optimized.json，禁止写 output 根目录；禁止用简化版/占位符，Step 4 与 Step 5 必须分步完整执行
concat 规则要删但音频还在播	actionTime 填了整段；必须从 step5 words 查出仅保留部分的 ms，不得含被删部分（如「这个这个」81900–82540 应排除，只填 82540–83820）
重复文件未提示	写入前必须检查目标是否存在，若存在则提示用户选择：删除/覆盖/保留并新建(01)；超时 20s 默认「保留并新建(01)」
step6 修正未生效	确保 step6 顶层为 optimized_segments 或 sentences；运行 --write-step6 写回
segment 起止时间不准	Step 6a 会依 step5 words 校正；需有 step5_asr_optimized.json 或 step5_asr_raw_*.json
自检提示 delete 未在 deleted_parts	每个 action: delete 段必须在 deleted_parts 中有对应项，含 deleted_text、description、start_time、end_time（与 delete 段一致）
字幕可见性（Alpha）
字段：textElement.Extra[transform].Alpha（0～1）
含义：0 隐藏（不渲染到画布），1 展示
删除态：Alpha 设为 0；恢复：Alpha 设为 1
Weekly Installs
193
Source
skills.volces.c…mediakit
First Seen
Mar 27, 2026