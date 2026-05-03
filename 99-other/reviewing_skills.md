---
title: reviewing-skills
url: https://skills.sh/j5ik2o/okite-ai/reviewing-skills
---

# reviewing-skills

skills/j5ik2o/okite-ai/reviewing-skills
reviewing-skills
Installation
$ npx skills add https://github.com/j5ik2o/okite-ai --skill reviewing-skills
SKILL.md
スキルレビュー

公式ベストプラクティスに基づいてスキルをレビューし、具体的な改善提案を行う。

レビューワークフロー
ステップ1: 対象スキルの特定

レビュー対象のSKILL.mdファイルを特定する：

ユーザーがパスを直接指定
カレントディレクトリでSKILL.mdを検索
複数のスキルが存在する場合はユーザーに確認
ステップ2: 読み込みと分析
対象のSKILL.mdファイルを完全に読み込む
best-practices.md でチェックリストを確認
YAMLフロントマター（name, description）を解析
ボディコンテンツの構造を分析
ステップ3: ベストプラクティスとの照合

各カテゴリを評価：

フロントマターチェック

name: 長さ、形式、命名規則
description: 完全性、具体性、トリガー

ボディチェック

行数（目標: 500行以下）
構造の明確さ
Progressive Disclosureの使用
ワークフロー設計の品質

コンテンツチェック

用語の一貫性
例の品質
テンプレートの適切さ

アンチパターン検出

デフォルトなしの複数選択肢
Windowsスタイルのパス
時間に依存する情報
マジック定数
ステップ4: レビューレポート生成

出力形式：

# スキルレビューレポート: {skill-name}

## サマリー
- 総合評価: {PASS | NEEDS_IMPROVEMENT | CRITICAL_ISSUES}
- Critical: {件数}
- Warning: {件数}
- Info: {件数}

## Critical（必須修正）
{修正必須の問題をリスト}

## Warning（推奨修正）
{推奨される改善をリスト}

## Info（改善提案）
{オプションの強化をリスト}

## 具体的な推奨事項
{例を含む具体的なアクションアイテム}

ステップ5: インタラクティブな改善

レポート提示後：

ユーザーに修正を希望するか確認
Critical問題を優先的に修正
段階的に修正を適用
各修正後に再検証
重大度分類
Critical

スキルの正常な機能を妨げる問題：

descriptionが空または不足
ボディが500行を大幅に超過
スクリプトのセキュリティ脆弱性
スクリプトのエラー処理不足
Warning

スキルの効果を低下させる問題：

Progressive Disclosureが適用されていない
例が不十分
用語が一貫していない
ワークフローが不明確
Info

改善の機会：

より簡潔にできる
構造の最適化
追加の例があると良い
レビューセッション例

ユーザー: 「pdf-processorスキルをレビューして」

1. 読み込み: skills/pdf-processor/SKILL.md
2. ロード: references/best-practices.md
3. チェックリストに照らして分析
4. 日本語でレポート生成
5. 修正を提案

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