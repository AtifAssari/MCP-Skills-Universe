---
rating: ⭐⭐
title: do
url: https://skills.sh/ymkz/dotfiles/do
---

# do

skills/ymkz/dotfiles/do
do
Installation
$ npx skills add https://github.com/ymkz/dotfiles --skill do
SKILL.md
Do Work Skill (標準作業プロセス)

機能開発・バグ修正のための標準化されたワークフローを実行します。

When to Use This Skill

Use this skill when:

Implementing new features
Fixing bugs
Making code changes
Following a structured development process
Core Workflow
1. Plan (計画)

タスクの範囲を定義し、アプローチを決定します。

Actions:

要件を明確化する
既存コードベースのパターンを調査
実装のステップを分割
依存関係を特定

Deliverable:

タスクリスト（Todo）
実装計画
2. Explore (探索)

コードベースと関連パターンを調査します。

Actions:

類似の実装を検索
既存のエラーハンドリングパターンを確認
関連するモジュールの構造を把握
必要に応じて外部ドキュメントを参照

Tools:

grep / ast-grep でパターン検索
explore agent でコードベース調査
librarian agent で外部リファレンス
3. Build (実装)

計画に基づいて実装を行います。

Actions:

既存パターンに従った実装
型安全の維持
適切なエラーハンドリング
コードの一貫性を維持

Verification:

lsp_diagnostics で型エラーを確認
既存パターンとの整合性を検証
4. Run Tests/Types (検証)

実装したコードを検証します。

Actions:

型チェック（TypeScriptの場合）
テストの実行（プロジェクトにテストがある場合）
ビルドの実行
手動での動作確認

Deliverable:

すべてのチェックがパスしたことの証拠
5. Commit (コミット)

変更をコミットします。

Actions:

変更内容の確認（git status, git diff）
コミットメッセージの作成
コミットの実行
（オプション）プッシュ

Note: ユーザーが明示的に要求した場合のみコミットを実行

Stage Extensions

各ステージには状況に応じた拡張機能があります。詳細は個別のドキュメントを参照してください。

1a. Frontend Prototypes (フロントエンドプロトタイプ)

新しいフロントエンドインターフェースを設計する場合:

references/frontend-prototypes.md を参照

複数のプロトタイプを一時的なルートで作成し、比較検討します。

3a. Backend RGR Approach (バックエンドRGRアプローチ)

バックエンド作業の場合:

references/backend-rgr.md を参照

Red-Green-Refactorサイクルで実装します。

4a. Frontend QA (フロントエンドQA)

フロントエンドコードを触る場合:

references/frontend-qa.md を参照

agent-browserを使用してビジュアルQAを実施します。

Usage
/do <task description>

Key Principles
Process First: プロセスに従って作業を進める
Verification Required: 各ステージで検証を行う
Pattern Consistency: 既存パターンを尊重する
Type Safety: 型エラーを決して抑制しない
Explicit Confirmation: コミットはユーザーの明示的な要求時のみ
Example
/do ユーザー認証機能を追加


This will:

Plan: 認証の要件を定義、ステップを分割
Explore: 既存の認証パターンを調査
Build: 認証ロジックを実装
Run Tests/Types: 型チェックとテストを実行
Commit: ユーザーの確認後、変更をコミット
Weekly Installs
11
Repository
ymkz/dotfiles
First Seen
Feb 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass