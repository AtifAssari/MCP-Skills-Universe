---
title: memory
url: https://skills.sh/chachamaru127/claude-code-harness/memory
---

# memory

skills/chachamaru127/claude-code-harness/memory
memory
Installation
$ npx skills add https://github.com/chachamaru127/claude-code-harness --skill memory
SKILL.md
Memory Skills

メモリとSSOT管理を担当するスキル群です。

機能詳細
機能	詳細
SSOT初期化	See references/ssot-initialization.md
Plans.mdマージ	See references/plans-merging.md
移行処理	See references/workflow-migration.md
プロジェクト仕様同期	See references/sync-project-specs.md
メモリ→SSOT昇格	See references/sync-ssot-from-memory.md
Unified Harness Memory（共通DB）

Claude Code / Codex / OpenCode 共通の記録・検索は harness_mem_* MCP を優先する。

検索: harness_mem_search, harness_mem_timeline, harness_mem_get_observations
注入: harness_mem_resume_pack
記録: harness_mem_record_checkpoint, harness_mem_finalize_session, harness_mem_record_event
Claude Code 自動メモリとの関係（D22）

Harness の SSOT メモリ（Layer 2）は Claude Code の自動メモリ（Layer 1）と共存します。 自動メモリは汎用的な学習を暗黙的に記録し、SSOT はプロジェクト固有の意思決定を明示的に管理します。 Layer 1 の知見がプロジェクト全体に重要な場合、/memory ssot で Layer 2 に昇格してください。

詳細: D22: 3層メモリアーキテクチャ

実行手順
ユーザーのリクエストを分類
上記の「機能詳細」から適切な参照ファイルを読む
その内容に従って実行
SSOT昇格

メモリシステム（Claude-mem / Serena）から重要な学びをSSOTに永続化します。

"Save what we learned" → references/sync-ssot-from-memory.md
"Promote decisions to SSOT" → references/sync-ssot-from-memory.md
Weekly Installs
28
Repository
chachamaru127/c…-harness
GitHub Stars
598
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass