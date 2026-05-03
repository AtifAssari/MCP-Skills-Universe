---
title: functional-ts-ja
url: https://skills.sh/iwasa-kosui/functional-ts-principles/functional-ts-ja
---

# functional-ts-ja

skills/iwasa-kosui/functional-ts-principles/functional-ts-ja
functional-ts-ja
Installation
$ npx skills add https://github.com/iwasa-kosui/functional-ts-principles --skill functional-ts-ja
SKILL.md
Functional Domain Modeling in TypeScript

サーバーサイドTypeScriptでドメインモデルを書くときの原則。classベースのOOPではなく、TypeScriptの型システムを最大限に活用した関数型アプローチを採る。

1. 型によるドメインモデリング

Discriminated Unionで状態を表現し、kind をdiscriminantとして統一する。type（interface ではなく）、Companion Object、Branded Types、Readonly<>、関数プロパティ記法、1概念1ファイル構成を使う。

バリデーションライブラリの検出: プロジェクトの package.json の dependencies / devDependencies を確認:

zod → validation-libraries/zod.md
valibot → validation-libraries/valibot.md
arktype → validation-libraries/arktype.md

詳細: domain-modeling.md

2. 関数による状態遷移

純粋関数で状態遷移を表現する。関数の引数型が有効な遷移元を制約し、戻り値型が遷移先を明示する。無効な遷移はコンパイルエラーになる。assertNever で網羅性をチェックする。

詳細: state-modeling.md

3. エラーハンドリング — Railway Oriented Programming

例外をスローせず、Result型でエラーを値として扱う。エラー型はDiscriminated Unionで定義し、呼び出し元が網羅的にハンドルできるようにする。

ライブラリの検出: プロジェクトの package.json の dependencies / devDependencies を確認:

neverthrow → result-libraries/neverthrow.md
byethrow → result-libraries/byethrow.md
fp-ts → result-libraries/fp-ts.md
option-t → result-libraries/option-t.md

詳細: error-handling.md

4. 境界の防御

外部入力（APIリクエスト、DB結果、ファイル読み込み）はバリデーションライブラリのスキーマでランタイムバリデーションする。ドメイン層内部では型を信頼する。型アサーション（as）は使わない。PIIフィールドには Sensitive<T> ラッパーを適用する。

詳細: boundary-defense.md

5. 宣言的なスタイル

配列の変換は filter / map / reduce でCompanion Objectの述語関数を使って宣言的に書く。ドメインイベントは不変レコードとしてモデリングする。

詳細: declarative-style.md

6. テストデータ

テストデータは as const satisfies Type で定義し、discriminantのリテラル型を保持しwideningを防ぐ。

詳細: test-data.md

原則の適用について

これらは推奨であり厳格なルールではない。コンテキストに応じて判断してよいが、原則から逸脱する場合はその理由をコメントで明示すること。

典型的な逸脱の正当理由:

外部ライブラリがclass継承を要求する場合
パフォーマンス要件により不変データの生成コストが問題になる場合
チームの合意により異なるパターンが採用されている場合
Weekly Installs
9
Repository
iwasa-kosui/fun…inciples
GitHub Stars
16
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass