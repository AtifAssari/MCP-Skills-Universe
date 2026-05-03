---
title: lingo-tube
url: https://skills.sh/liuwei1025/lingotube/lingo-tube
---

# lingo-tube

skills/liuwei1025/lingotube/lingo-tube
lingo-tube
Installation
$ npx skills add https://github.com/liuwei1025/lingotube --skill lingo-tube
SKILL.md
LingoTube

Download → Auto-subs → AI Analysis → Clip → Translate → Burn Subtitles → Sync

AI Protocol

Working directory: This skill's own directory (same directory as this SKILL.md file)

Setup (first time): pip install -r requirements.txt

输入处理规则：

当用户提供 YouTube URL 时，直接执行默认工作流，不要询问用户想做什么。YouTube URL 是本 Skill 最明确的输入信号，无需确认意图。
如果用户同时提供了额外参数（如 --content-only、--clip、语言指定），按参数执行；否则全部使用默认值。

工作流选择策略：

默认使用 Notion Agent Workflow（notion_agent_workflow agent）。只有用户明确要求本地流程，或未配置 Notion 环境变量时，才回退到 URL Workflow（scripts.workflow）。

字幕分析 / 翻译执行策略：

默认使用 subagent 完成字幕分析和字幕翻译。
只有当前环境不支持 subagent 时，才回退到本地 provider 流程。
provider 回退路径沿用现有脚本能力；优先使用已配置的 provider，未显式指定时按仓库默认选择逻辑执行。
字幕分析不会直接把原始 source/subtitles.{lang}.vtt 发给模型。workflow 会先生成 source/subtitles.deduped.vtt，再压缩生成 source/subtitles.analysis.vtt，分析阶段只读取这个预处理后的 VTT。
分析阶段最终写回的 start_anchor_text / end_anchor_text 必须能在去重后的源字幕中命中；命不中的候选会被过滤，无效的 AI 建议锚点会被丢弃并回退到本地派生锚点。

Detailed reference: See WORKFLOW.md for full config table, API examples, flow diagrams, and troubleshooting.

Quick Start
Notion Agent Workflow (default)

Delegate subtitle analysis & translation to a Notion agent; local script handles download, clip, burn, and upload:

python -m scripts.notion.agent_workflow agent --url "URL" [--subtitle-lang it] [--target-language zh]


The flow: download subtitles → create Notion page (no status) → write source subtitles → set status=pending → poll until agent marks translated → set processing → download video → clip → build bilingual VTT → burn → upload → set ready → add comment (triggers Notion automation).

All operations target the same Notion database, configured via LINGO_TUBE_AGENT_WORKSPACE_ID.

Flag	Purpose
--url	YouTube video URL (required)
--output-dir	Output directory (default: ~/Downloads)
--agent-workspace-id	Notion Agent Workspace database ID (overrides LINGO_TUBE_AGENT_WORKSPACE_ID)
--subtitle-lang	Source subtitle language (default: auto)
--target-language	Translation target language (default: zh)
--poll-interval	Seconds between Notion polls (default: 30)
--poll-timeout	Max seconds to wait for agent (default: 1800)
--cookies-from-browser chrome	Use browser cookies for restricted videos
Process Translated Pages (batch post-processing)

Pull all pages with status=translated from the Notion database, then run the full clip → burn → upload pipeline for each one. Designed to run as an external cron job (plan steps 3-6):

python -m scripts.notion.agent_workflow process-translated

# crontab example: check every 10 minutes
*/10 * * * * cd /path/to/LingoTube/skills/lingo-tube && python -m scripts.notion.agent_workflow process-translated


The flow: query translated pages → set processing → read Video URL + Start/End Time + bilingual text → download video → clip → extract audio → build bilingual VTT → generate ASS → burn subtitles → upload clip.mp4 / audio.mp3 / with_bilingual.mp4 → set ready → add comment (triggers Notion automation).

The database defaults to LINGO_TUBE_AGENT_WORKSPACE_ID (same database as the agent mode). Override with --database-id.

Flag	Purpose
--database-id	Notion database ID (defaults to LINGO_TUBE_AGENT_WORKSPACE_ID)
--output-dir	Output directory (default: ~/Downloads)
--cookies-from-browser chrome	Use browser cookies for restricted videos
--api-version	Notion API version
--comment "自定义评论"	Comment text added after processing (default: 视频处理完成，资源已上传。)

Page requirements (each translated page must have):

Video URL — YouTube source URL
Start Time / End Time — date properties encoding video timestamps as 1970-01-01THH:MM:SS.000Z
Bilingual text — in the page body under a "翻译" subsection within a Clip heading
Process Video Links From Notion (batch URL ingestion)

When the user provides a Notion database id or data source id and wants to process the stored video links directly, use the dedicated batch entrypoint:

python -m scripts.notion.process_video_links --database-id "NOTION_DB_ID" --source-lang from-notion --target-lang zh --output-dir ~/Downloads


This mode:

queries the Notion database/data source directly,
reads the 视频链接 property,
filters out rows already marked 已完成 by default,
infers --source-lang from the Notion 语言 property when --source-lang from-notion,
and then iterates python -m scripts.workflow "URL" for each row.

Common flags:

Flag	Purpose
--database-id / --data-source-id	Notion database or data source id
--language 阿拉伯语	Only process a specific language; repeatable
--limit 20	Only process the first N matching rows
--dry-run	Print the candidate rows without running workflow
--workflow-arg --burn-preset + --workflow-arg slow	Pass extra flags through to scripts.workflow
--cookies-from-browser chrome	Pass browser cookies through to workflow

Recommended when:

the Notion database already contains curated 视频链接,
you want to batch-run the local workflow over those links,
or you want the agent to treat the Notion database itself as the work queue.
Prompt Template

Use this prompt when you want the skill to start directly from a Notion queue:

读取 Notion data source/database `33a85e149a4c80df9f4fd79e42c9635d` 中的 `视频链接`，按 `处理状态 != 已完成` 过滤，按 `语言` 从 Notion 推断 source-lang，target-lang=zh，串行调用 LingoTube workflow 处理每个 URL。不要先问确认，直接开始；失败继续；最后汇总成功、失败和输出目录。


If you only want a subset, extend the prompt:

读取 Notion data source/database `33a85e149a4c80df9f4fd79e42c9635d` 中的 `视频链接`，只处理 `韩语` 和 `日语`，最多 20 条，按 `处理状态 != 已完成` 过滤，source-lang 从 Notion `语言` 推断，target-lang=zh，处理完成后汇总结果。

URL Workflow (local fallback)

Use when Notion is not configured or the user explicitly requests a fully local pipeline:

python -m scripts.workflow "URL" [--source-lang it] [--clip "01:30-03:45"]


One command runs the full pipeline. Skip individual steps with --no-translation, --no-burn, --no-download, etc.

超时设置： 运行此命令时必须设置 bash timeout=3600000（60 分钟），因为分析/翻译阶段无论走 subagent 还是 provider 回退都可能耗时较长。如果进程因超时中断，重新运行同一命令即可从断点续跑（已完成的步骤会自动跳过）。

Flag	Purpose
--source-lang it	Source subtitle language (default: auto)
--target-lang zh	Translation target language (default: zh)
--clip "01:30-03:45"	Manual time range, skips AI analysis
--no-translation / --no-burn	Skip translation / burn step
--no-download	Use already-downloaded files
--force-reanalyze	Ignore cached progress, re-run analysis
--cookies-from-browser chrome	Use browser cookies for restricted videos
--sync-notion / --nas	Enable Notion / NAS sync
--notion-data-source-id <id>	Override the Notion data source for this run
--no-parallel	Disable parallel processing
--burn-preset slow --burn-crf 18	High-quality burn
Text Input Workflow

Generate bilingual subtitles from raw text, optionally matched to a YouTube video's timestamps:

# URL mode: match text to YouTube subtitle timestamps, then clip + burn
python -m scripts.text_input --url "URL" --file input.txt -o ./output

# Pure text mode: generate subtitles from interleaved source/translation lines
python -m scripts.text_input --file input.txt -o ./output

# With video burn
python -m scripts.text_input --file input.txt --video clip.mp4 -o ./output


Input file formats (auto-detected):

Format	Description	Example
interleaved	Source and translation lines separated by blank lines	Source line\n翻译行\n\nSource line\n翻译行
parallel	Tab-separated source and translation per line	Source\t翻译
source_only	Source text only, auto-split by sentences	Plain paragraph text
Re-run / Resume Behavior
progress.json stores step-completion flags (analysis_done, clips_done, etc.); it does not store segment data.
Segment data is stored in workflow_result.json, which is written when the workflow reaches normal completion, even if some steps produced warnings or partial failures. If the run is interrupted before completion, workflow_result.json may be absent or stale, so segment data may not be recoverable on the next run—the analysis phase will re-run instead.
Re-running the same URL does auto-resume completed steps (skips re-download, re-clip, etc.) as long as the corresponding output files still exist.

--no-analysis caveat: This flag skips AI analysis and leaves segments empty unless --clip (or equivalent time_ranges) is also provided. With empty segments, all downstream steps (clip, translate, burn) are silently skipped. Always pair --no-analysis with an explicit --clip range.

Hard Requirements
When the agent runs the workflow, always request 1080p or higher video quality. If the source does not provide 1080p+, stop and report instead of falling back to lower quality. (The CLI does accept lower values like 720p for manual override.)
Subtitle downloads must use auto-generated subtitles only. Do not use manually uploaded subtitles.
Pipeline

The workflow runs as a single process. Video download and subtitle download happen in parallel; analysis starts as soon as subtitles are ready, without waiting for the video.

Step	Depends on	Output
1. Download video (background)	URL	source/video.mp4, source/cover.jpg
2. Download subtitles	URL	source/subtitles.{lang}.vtt
3. Analyze subtitles	Step 2	Segment list in memory → workflow_result.json on completion
4. Clip segments	Steps 1+3	clips/{time}/clip.mp4, subtitle.vtt
5. Translate subtitles	Step 4	clips/{time}/subtitle_translation.vtt
6. Burn subtitles	Step 4 (plus Step 5 for translated bilingual burn)	clips/{time}/with_subs.mp4 and/or with_bilingual.mp4
7. Sync (optional)	Workflow outputs	Notion data source item, NAS upload

Steps 1-3 overlap: video downloads in a background thread while subtitles download and analysis runs in the foreground. Step 4 onward waits for the video file.

On error: Re-run the same command. Completed steps are skipped via progress.json flags; the analysis phase re-runs if workflow_result.json is missing or the previous run was interrupted. Force full restart: rm ~/Downloads/{video_id}/progress.json ~/Downloads/{video_id}/workflow_result.json

Output Structure
~/Downloads/{video_id}/
├── metadata.json
├── progress.json
├── workflow_result.json
├── source/
│   ├── video.mp4
│   ├── cover.jpg
│   ├── subtitles.{lang}.vtt
│   ├── subtitles.deduped.vtt
│   └── subtitles.analysis.vtt
└── clips/
    └── 00m08s-01m57s/           # {MMmSSs}-{MMmSSs} compact format
        ├── clip.mp4
        ├── subtitle.vtt
        ├── subtitle.ass
        ├── subtitle_translation.vtt
        ├── subtitle_bilingual.vtt    # optional prebuilt or repaired bilingual VTT
        ├── subtitle_bilingual.ass
        ├── audio.mp3
        ├── with_subs.mp4
        └── with_bilingual.mp4

Environment Variables
Notion Agent Workflow (agent + process-translated)
Variable	Required	Purpose
LINGO_TUBE_AGENT_WORKSPACE_ID	Agent Workflow	Notion 数据库 ID（agent 和 process-translated 共用）
NOTION_API_TOKEN	Agent Workflow	Notion API Token
NOTION_API_VERSION	Optional	Notion API 版本

Legacy fallback: LINGOTUBE_AGENT_WORKSPACE_ID, LINGOTUBE_NOTION_TOKEN, LINGOTUBE_NOTION_API_VERSION, NOTION_AGENT_WORKSPACE_ID are also accepted, but the names in the table are preferred.

URL Workflow (local pipeline) + Notion Sync
Variable	Required	Purpose
LINGO_TUBE_PROVIDER	Optional	provider 回退时显式指定 provider
OPENAI_API_KEY	Fallback only	OpenAI-compatible provider key
MINIMAX_API_KEY	Fallback only	MiniMax provider key
MINIMAX_BASE_URL	Fallback only	MiniMax provider endpoint
MINIMAX_MODEL	Fallback only	MiniMax model name
ARK_API_KEY	Fallback only	Ark provider key
ARK_BASE_URL	Fallback only	Ark provider endpoint
ARK_MODEL	Fallback only	Ark provider model name
MOONSHOT_API_KEY	Fallback only	Kimi / Moonshot provider key
NOTION_API_TOKEN	Optional	Notion sync
NOTION_DATA_SOURCE_ID	Optional	Preferred Notion data source id
NOTION_DATABASE_ID	Optional	Legacy Notion database id compatibility fallback
NAS_INTRANET_URL	Optional	NAS WebDAV (intranet)
NAS_EXTRANET_URL	Optional	NAS WebDAV (extranet fallback)
NAS_USERNAME / NAS_PASSWORD	Optional	NAS credentials

provider 环境变量仅在当前运行环境不支持 subagent 时需要。See WORKFLOW.md for full values and examples.

Troubleshooting
Problem	Solution
Download restricted (login required)	Add --cookies-from-browser chrome
Interrupted mid-run	Re-run the same command; completed steps auto-resume
Force full restart	rm ~/Downloads/{video_id}/progress.json ~/Downloads/{video_id}/workflow_result.json
--no-analysis produces no clips	Always pair with --clip to provide explicit time range
Agent workflow times out	Increase --poll-timeout; ensure agent is running in Notion
Agent workspace not found	Set LINGO_TUBE_AGENT_WORKSPACE_ID or pass --agent-workspace-id
Prerequisites
ffmpeg (brew install ffmpeg)
yt-dlp (auto-installed)
Python: requests, openai, tqdm
Weekly Installs
8
Repository
liuwei1025/lingotube
First Seen
Apr 6, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykWarn