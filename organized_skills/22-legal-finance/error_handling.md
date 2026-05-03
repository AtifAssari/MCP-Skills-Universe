---
rating: ⭐⭐
title: error-handling
url: https://skills.sh/j5ik2o/okite-ai/error-handling
---

# error-handling

skills/j5ik2o/okite-ai/error-handling
error-handling
Installation
$ npx skills add https://github.com/j5ik2o/okite-ai --skill error-handling
SKILL.md
エラーハンドリング

回復可能性を基準にしたエラーハンドリング設計を支援する。

基本方針

ドメインロジック（ビジネスルール）では Either/Result 型を採用する。

ドメイン層のエラーは呼び出し元が判断すべき → 型で明示
例外は制御フローではなく、本当の異常事態に限定
戻り値の型を見るだけでエラーの可能性が分かる設計
判断フロー
エラー発生
    ↓
回復可能か？
    ├─ YES → Either/Result型で表現
    └─ NO → 例外/panicで即座に停止

回復可能	回復不能
ビジネスルール違反	引数の不正 (IllegalArgumentException)
外部システムエラー	状態の矛盾 (IllegalStateException)
権限不足・リソース競合	到達不可コード (unreachable)
回復可能なエラー

Either/Result型で表現し、呼び出し元に判断を委ねる。

// TypeScript - neverthrow
function findUser(id: string): Result<User, UserError> {
  if (!isValidId(id)) return err({ type: 'VALIDATION_FAILED', field: 'id' });
  return repository.find(id)
    ? ok(user)
    : err({ type: 'NOT_FOUND', userId: id });
}

回復不能なエラー

プログラムの前提条件違反は即座に停止。

// 引数の不正 → IllegalArgumentException 相当
if (order === null) throw new Error('order must not be null');

// 状態の矛盾 → IllegalStateException 相当
if (order.status === 'COMPLETED' && order.items.isEmpty())
  throw new Error('completed order must have items');

// 到達不可コード → unreachable
default: throw new Error(`unreachable: ${status}`);

推奨ライブラリ
言語	ライブラリ	選択基準
TypeScript	neverthrow	Result のみで十分な場合（軽量・シンプル）
TypeScript	fp-ts	関数型全般を使う場合（Option, Task, IO, Reader 等）
JavaScript	neverthrow	TypeScript と同様
Rust	標準 Result<T, E>	常にこれを使用。エラー定義には thiserror
Go	標準 (T, error)	Go らしいシンプルなコードを書く場合
Go	samber/mo	Result/Either でチェーン処理したい場合
Scala	標準 Either[L, R]	標準で十分。cats は大規模 FP 向け
Java	vavr.io Either	関数型コレクションも使うなら vavr 一択
Python	returns (dry-python)	本番環境向け。型アノテーション充実
Python	result	軽量。Rust ライクなシンプルな API
詳細ガイドライン

全言語の実装パターン、エラー型設計の詳細は references/guidelines.md を参照。

関連スキル（併読推奨）

このスキルを使用する際は、以下のスキルも併せて参照すること：

error-classification: エラーの分類（Error, Defect, Fault, Failure）に基づく処理方式の選択
domain-building-blocks: ドメイン操作におけるResult/Eitherの適用
repository-design: リポジトリのエラー処理パターン（同期・非同期）
Weekly Installs
25
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