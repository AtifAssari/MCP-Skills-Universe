---
title: migrate-skill-to-agent
url: https://skills.sh/j5ik2o/okite-ai/migrate-skill-to-agent
---

# migrate-skill-to-agent

skills/j5ik2o/okite-ai/migrate-skill-to-agent
migrate-skill-to-agent
Installation
$ npx skills add https://github.com/j5ik2o/okite-ai --skill migrate-skill-to-agent
SKILL.md
Migrate Skill To Agent

.claude/skills/{name} にあるスキルを .agents/skills/{name} へ移動し、 .claude/skills/ と .codex/skills/ の両方からシンボリックリンクを張る。

使い方

引数としてスキル名を受け取り、scripts/migrate.sh を実行する。

bash scripts/migrate.sh <skill-name> [project-root]

skill-name（必須）: 移動対象のスキル名（ディレクトリ名）
project-root（省略可）: プロジェクトルートパス。省略時はカレントディレクトリ
実行前の確認事項
.claude/skills/{name} が実ディレクトリとして存在すること（シンボリックリンクでないこと）
.agents/skills/{name} がまだ存在しないこと
実行結果
移動前:
  .claude/skills/{name}/  (実ディレクトリ)

移動後:
  .agents/skills/{name}/               (実体)
  .claude/skills/{name} -> ../../.agents/skills/{name}  (シンボリックリンク)
  .codex/skills/{name}  -> ../../.agents/skills/{name}  (シンボリックリンク)

ワークフロー
ユーザーからスキル名を引数として受け取る
バリデーション（ソースの存在確認、既存リンクチェック、ターゲット重複チェック）
scripts/migrate.sh をプロジェクトルートを第2引数として実行
結果を報告
実行例

ユーザー: 「intent-based-dedup を .agents に移動して」

bash /path/to/migrate-skill-to-agent/scripts/migrate.sh intent-based-dedup /path/to/project

Weekly Installs
20
Repository
j5ik2o/okite-ai
GitHub Stars
75
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass