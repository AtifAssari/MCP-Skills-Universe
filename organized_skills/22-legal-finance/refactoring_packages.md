---
rating: ⭐⭐⭐
title: refactoring-packages
url: https://skills.sh/j5ik2o/okite-ai/refactoring-packages
---

# refactoring-packages

skills/j5ik2o/okite-ai/refactoring-packages
refactoring-packages
Installation
$ npx skills add https://github.com/j5ik2o/okite-ai --skill refactoring-packages
SKILL.md
パッケージリファクタリング

既存コードのパッケージ/モジュール構造を分析し、改善提案と移行計画を作成・実行する。

ワークフロー
1. 現状分析 → 2. 問題特定 → 3. 改善提案 → 4. 移行計画

1. 現状分析

対象ディレクトリの構造を把握する。

使用ツール:

mcp__serena__list_dir: ディレクトリ構造の把握（recursive: true）
mcp__serena__get_symbols_overview: ファイル内のシンボル把握
mcp__serena__find_referencing_symbols: 依存関係の検出

確認ポイント:

ディレクトリ深度（4階層以下が理想）
ファイル数/ディレクトリ（10以下が理想）
命名規則の一貫性
2. 問題特定

references/analysis-patterns.mdを参照し問題を検出。

優先順位（高→低）：

循環依存（ビルド不可の原因）
神モジュール（変更影響が大きい）
散在機能（開発効率低下）
過度なネスト（可読性低下）
3. 改善提案

問題ごとの解決策はreferences/analysis-patterns.mdを参照。

4. 移行計画

段階的な移行計画を作成：

### Phase 1: 準備
- [ ] テストカバレッジ確認
- [ ] 依存関係マップ作成

### Phase 2: 構造変更
- [ ] 新ディレクトリ作成
- [ ] ファイル移動
- [ ] インポートパス更新

### Phase 3: 検証
- [ ] テスト実行
- [ ] ビルド確認

具体例
入力
ユーザー: 「auth/モジュールが肥大化している」

分析
auth/
├── mod.rs (800行) ← 神モジュール検出
├── jwt.rs
├── oauth.rs
└── session.rs

問題: mod.rsに認証ロジック、ミドルウェア、エラー型が混在

出力
# パッケージ構造分析レポート

## 検出された問題
1. **神モジュール**: auth/mod.rs (800行、3責務)

## 改善提案
### 提案1: 責務分離
- Before: auth/mod.rs に全ロジック
- After:
  - auth/core.rs (認証ロジック)
  - auth/middleware.rs (ミドルウェア)
  - auth/error.rs (エラー型)
- 理由: 単一責任の原則適用、変更影響範囲の限定

## 移行計画
### Phase 1: 準備
- [ ] 既存テストの確認
### Phase 2: 分割
- [ ] auth/core.rs 作成、ロジック移動
- [ ] auth/middleware.rs 作成
- [ ] auth/error.rs 作成
- [ ] mod.rs を再エクスポートのみに
### Phase 3: 検証
- [ ] cargo test
- [ ] cargo clippy

関連スキル（併読推奨）

このスキルを使用する際は、以下のスキルも併せて参照すること：

package-design: リファクタリングの目標となるパッケージ設計原則
ddd-module-pattern: DDD文脈でのリファクタリング目標構造
intent-based-dedup: リファクタリング時の重複コード共通化判断
Weekly Installs
23
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