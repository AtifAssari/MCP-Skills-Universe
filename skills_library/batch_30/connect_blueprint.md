---
title: connect-blueprint
url: https://skills.sh/ippei2480/connect-blueprint/connect-blueprint
---

# connect-blueprint

skills/ippei2480/connect-blueprint/connect-blueprint
connect-blueprint
Installation
$ npx skills add https://github.com/ippei2480/connect-blueprint --skill connect-blueprint
SKILL.md
connect-blueprint
Overview

2つのモードで Amazon Connect コンタクトフローを生成する：

モードA（ゼロから設計）: 要件ヒアリング → Mermaid設計図 → フローJSON → デプロイ
モードB（設計図から生成）: draw.io/Mermaid/画像 → フローJSON → デプロイ
Prerequisites
AWS CLI + 有効なプロファイル（aws sts get-caller-identity --profile <profile> で確認）
Connect インスタンスID（aws connect list-instances --profile <profile> で取得可）
必要IAM権限: connect:*
Mode A: Design from Scratch
Progress Tracking

各ステップ完了時にチェックし、現在の進捗を把握する：

 Step 1: 要件ヒアリング完了
 Step 2: Mermaid 設計図作成 → ユーザー承認済み
 Step 3: フロー JSON 生成 + AWS MCP パラメータ検証完了
 Step 4a: ローカルバリデーション通過
 Step 4b: (任意) API バリデーション通過
 Step 4c: デプロイ → ユーザー承認 → 完了
Step 1: 要件ヒアリング

以下を確認する：

電話の目的・業種・主なユースケース
IVR選択肢（番号と対応内容）
営業時間分岐の有無
外部システム連携（Lambda/DynamoDB等）
既存フローとの統合有無
通話録音の要否と録音対象（Agent / Customer / 両方）
Contact Lens 分析の有効/無効
分析言語（ja-JP, en-US 等）
機密情報マスキング（redaction）の要否

環境情報を取得してユーザーに見せる： references/aws_cli_commands.md の「環境情報の取得」セクションのコマンドで以下を取得し、ユーザーに提示する：

キュー一覧、プロンプト一覧、Lambda一覧、フローモジュール一覧

実現不可能な要件があればこの段階で明示してユーザーに伝える。

Step 2: Mermaid 設計図の生成

references/mermaid_notation.md の記法に従ってMermaid図を生成する。

繰り返し処理（リトライメニュー等）は、まず Loop ActionType の使用を検討する。 Loop で実現できない場合のみ UpdateContactAttributes + Compare によるカウンタ方式を検討する。

Mermaid図は .md ファイルとして保存する（例: <flow-name>-design.md）。 保存後、必ずユーザーにレビューを依頼し承認を得てから次のステップへ。

Step 3: フローJSON生成

Mermaidからフロー構造を解析してJSON（Actions配列 + Transitions）を生成する。 references/flow_json_structure.md の構造仕様に従う。

フローの最初のアクションは必ず UpdateFlowLoggingBehavior とする。 StartAction に UpdateFlowLoggingBehavior のIDを設定し、その NextAction を本来のエントリーアクションにする。

AWS MCP Parameter Validation

各ActionTypeのパラメータを設定する際、references/action_types.md の共通ルールを確認した上で、AWS MCP で公式ドキュメントを参照してパラメータの正確性を保証する：

references/action_types.md の AWS Docs パス対応テーブルから該当URLパスを取得
aws___read_documentation でパラメータ仕様を確認
ドキュメントに基づいてパラメータを設定する

Why: ローカルリファレンスはパラメータの概要のみ記載。正確なフィールド名・型・制約は AWS 公式ドキュメントが信頼できるソース。

position付与:

python3 scripts/layout.py <flow.json>

Step 4: Validate & Deploy

IMPORTANT: Always validate before deploying. Never skip this step.

ローカルバリデーション (required)
./scripts/validate.sh flow.json


If validation returns errors, fix the flow JSON and re-validate before proceeding. Only deploy after validation passes with no errors.

Validation Feedback Loop
./scripts/validate.sh flow.json を実行
エラーがある場合: a. エラーメッセージを解析 b. aws___read_documentation で公式仕様を確認 c. フローJSONを修正 d. 手順 1 に戻り再実行する
エラーなしになるまで繰り返す（最大3回。超過時はユーザーに報告）
APIバリデーション (recommended)
./scripts/validate.sh --api --instance-id $INSTANCE_ID --profile $PROFILE flow.json


ローカルチェック通過後、create-contact-flow --status SAVED で下書きを作成してConnect APIによるバリデーションを実行する。成功時は下書きを自動削除する。

Why: ローカルチェックはJSON構造・遷移参照の整合性のみ検証する。ActionType固有のパラメータ制約やErrors/Conditionsの妥当性はConnect API側でしか検証できないため、APIバリデーションで事前にエラーを検出する。

Deploy

references/aws_cli_commands.md の「フロー操作」セクションのコマンドでデプロイする。 2ステップ方式: --status SAVED で作成 → update-contact-flow-metadata --contact-flow-state ACTIVE で公開。

Mode B: Convert from Diagram

入力形式に応じて処理：

Mermaid: そのまま Step A-3 へ
draw.io XML: ノード/エッジを抽出してMermaidに変換 → Step A-3 へ
画像: Vision解析でフロー構造を読み取り → Mermaidに変換 → Step A-3 へ

変換後は必ずユーザーに確認してから進む。

Key Constraints

references/flow_json_structure.md と references/action_types.md の共通ルールに従う。 以下はフロー生成時に特に重要な制約：

StartAction は UpdateFlowLoggingBehavior にする
サンプルフローは提供しない — 要件に応じてゼロから設計すること
Security Rules
Deploy Safety Guard
scripts/deploy.sh の実行、または aws connect create-contact-flow / aws connect update-contact-flow-content コマンドの実行前に、必ずユーザーの明示的な承認を得ること
.env ファイルや AWS クレデンシャルファイル（~/.aws/credentials 等）を読み取らないこと
Safe Operations (No Confirmation Required)
scripts/validate.sh <file> によるローカルバリデーション（--api オプション含む。下書き保存は自動削除される）
python3 scripts/layout.py <file> によるレイアウト座標付与
フローJSONの作成・編集
Placeholders
<YOUR_XXX_ARN> プレースホルダーを実際の ARN に置き換える際は、ユーザーから提供された値のみ使用すること
推測や仮の値で ARN を埋めないこと
Coding Conventions
シェルスクリプト: 変数は必ずダブルクォートで囲む。AWS CLI 引数の組み立てには bash 配列を使用する
Python: 標準ライブラリのみ使用（外部パッケージ不可）
JSON: テンプレートでは実際の ARN/ID を使用せず <YOUR_XXX> プレースホルダーを使う
Validation

3層バリデーションでフロー品質を保証する:

AWS MCP: aws___read_documentation で ActionType パラメータ仕様を確認（フロー生成時）
ローカル: ./scripts/validate.sh flow.json で構造・遷移・孤立ブロック・デッドエンド検出
Connect API: ./scripts/validate.sh --api --instance-id $ID --profile $P flow.json で API 側の制約を検証
Troubleshooting

エラー発生時の対処:

references/error_handling_patterns.md でパターンを確認
aws___search_documentation / aws___read_documentation で公式ドキュメントを調査
推測による修正は避け、必ず公式ドキュメントで裏付けを取る
References
Action Types: references/action_types.md
Flow JSON Structure: references/flow_json_structure.md
Mermaid Notation: references/mermaid_notation.md
AWS CLI Commands: references/aws_cli_commands.md
Layout Rules: references/layout_rules.md
Error Handling Patterns: references/error_handling_patterns.md
Connect Limits: references/connect_limits.md
Weekly Installs
16
Repository
ippei2480/conne…lueprint
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass