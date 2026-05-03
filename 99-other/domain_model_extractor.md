---
title: domain-model-extractor
url: https://skills.sh/j5ik2o/okite-ai/domain-model-extractor
---

# domain-model-extractor

skills/j5ik2o/okite-ai/domain-model-extractor
domain-model-extractor
Installation
$ npx skills add https://github.com/j5ik2o/okite-ai --skill domain-model-extractor
SKILL.md
Domain Model Extractor

既存の非DDDコードを分析し、DDDのビルディングブロック（集約・ローカルエンティティ・値オブジェクト・ドメインサービス）を擬似コード付きで提案する。

分析ワークフロー
Phase 1: スコープ確認

ユーザーに以下を確認する：

分析対象のディレクトリ/ファイル範囲
ドメインの概要（何を扱うシステムか）
特に関心のある領域（あれば）
Phase 2: 既存コードの探索

以下の順序で情報を収集する：

Step 1: 構造の把握

ディレクトリ構造を確認し、モジュール/パッケージの全体像を掴む
主要なクラス/構造体/型を一覧化する

Step 2: データ構造の分析

DB スキーマ（マイグレーション、ORMモデル等）があれば確認
主要なクラス/構造体のフィールド・プロパティを確認
データ間の参照関係（外部キー、IDフィールド等）を把握

Step 3: ビジネスロジックの所在特定

バリデーションロジックの散在箇所を特定
条件分岐の多いメソッドを特定（ビジネスルールの候補）
複数エンティティにまたがる操作を特定

Step 4: トランザクション境界の分析

同一トランザクションで更新されるデータ群を特定
これが集約境界の最重要手がかりとなる
Phase 3: ドメインモデルの導出

収集した情報を基に、以下の順序でモデルを導出する。 詳細なヒューリスティクスは references/analysis-heuristics.md を参照。

導出順序:

値オブジェクト - プリミティブ型で表現されたドメイン概念、検証ロジックの散在箇所から
集約 - トランザクション境界、CRUDの単位、不変条件の範囲から
ローカルエンティティ - 集約内部でのみ意味を持つ、IDを持つオブジェクト
ドメインサービス - 複数集約にまたがる操作、特定オブジェクトに属さないルール

各モデルに含める情報:

プロパティ（型情報付き）
ファクトリメソッド（生成時の検証）
コマンドメソッド（状態変更操作、不変で新インスタンスを返す）
クエリメソッド（状態参照操作）
不変条件（集約が常に満たすべきルール）
Phase 4: 提案ドキュメントの出力

references/output-template.md のテンプレートに従い、以下を含むMarkdownドキュメントを生成する：

概要（分析対象、発見したモデル数）
集約ごとのセクション（擬似コード付き）
値オブジェクト一覧（擬似コード付き）
ドメインサービス一覧（擬似コード付き）
集約関連図（テキストベース）
既存コードとの対応表
出力例（抜粋）

以下は EC サイトの注文管理コードを分析した場合の出力イメージ（集約1つ分）:

Aggregate Order {
  id: OrderId
  customerId: CustomerId        // 他集約へのID参照
  items: List<OrderItem>        // ローカルエンティティ
  status: OrderStatus           // 値オブジェクト
  shippingAddress: Address      // 値オブジェクト

  // Invariants: items は1件以上、合計金額は0より大きい

  static create(customerId, firstItem, address): Order
  addItem(item: OrderItem): Order       // returns 新しいインスタンス
  removeItem(itemId: OrderItemId): Order
  submit(): Order                        // status を Submitted に変更
  totalAmount(): Money
}

分類判断基準
判断ポイント	集約	ローカルエンティティ	値オブジェクト
独自のIDを持つか	Yes（ルートID）	Yes（ローカルID）	No
単独で取得されるか	Yes	No（親経由）	No
ライフサイクルがあるか	Yes	親に従属	なし（不変）
同一性で比較するか	Yes（ID）	Yes（ID）	No（値で比較）
注意事項
既存コードの1クラス = 1集約とは限らない。複数クラスが1集約になることも、1クラスが複数に分割されることもある
テーブル構造に引きずられすぎない。テーブルは永続化の都合であり、ドメインモデルの構造と一致するとは限らない
過度に細かい値オブジェクトを作りすぎない。ドメインで意味のある単位のみ
集約は小さく保つ（Vernon's Rule）。迷ったら分割する方向で
関連スキル（併読推奨）

このスキルを使用する際は、以下のスキルも併せて参照すること：

domain-building-blocks: 抽出対象となるビルディングブロックの定義と設計
aggregate-design: 集約境界の特定と設計ルール
cqrs-aggregate-modeling: 読み取り責務が混在する集約の分離指針
Weekly Installs
30
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