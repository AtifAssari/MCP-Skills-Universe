---
rating: ⭐⭐
title: parse-dont-validate
url: https://skills.sh/j5ik2o/okite-ai/parse-dont-validate
---

# parse-dont-validate

skills/j5ik2o/okite-ai/parse-dont-validate
parse-dont-validate
Installation
$ npx skills add https://github.com/j5ik2o/okite-ai --skill parse-dont-validate
SKILL.md
Parse, Don't Validate

情報を捨てるvalidationから、情報を保持するparsingへ変換する。

核心原則

チェック結果を捨てずに型で保持する。

アプローチ	戻り値	情報	問題
Validate	() / void / bool	捨てる	再チェック必要、型が保証しない
Parse	型付き値	保持	一度のチェックで済む、型が保証
判断フロー
チェック関数を書こうとしている
    ↓
戻り値は何か？
    ├─ () / void / bool → Validateパターン（問題あり）
    └─ 新しい型 → Parseパターン（推奨）

アンチパターン検出

以下のパターンを見つけたら変換を検討：

❌ validate*() → ()
❌ check*() → bool
❌ assert*() → ()（表明目的以外）
❌ is*() → bool（分岐後に同じ値を使う場合）
❌ "should never happen" コメント
❌ case None/null の after 正常ケース

変換パターン
1. NonEmpty変換
// ❌ Validate: 情報を捨てる
function validateNonEmpty(list: string[]): void {
  if (list.length === 0) throw new Error("list cannot be empty");
}

// ✅ Parse: 情報を保持する
type NonEmptyArray<T> = [T, ...T[]];
function parseNonEmpty<T>(list: T[]): NonEmptyArray<T> {
  if (list.length === 0) throw new Error("list cannot be empty");
  return list as NonEmptyArray<T>;
}

2. 重複キー検出
// ❌ Validate: チェックして捨てる
function checkNoDuplicateKeys(pairs: [string, unknown][]): void {
  const seen = new Set<string>();
  for (const [key] of pairs) {
    if (seen.has(key)) throw new Error(`duplicate key: ${key}`);
    seen.add(key);
  }
}

// ✅ Parse: Mapに変換して保持
function parseToMap(pairs: [string, unknown][]): Map<string, unknown> {
  const result = new Map<string, unknown>();
  for (const [key, value] of pairs) {
    if (result.has(key)) throw new Error(`duplicate key: ${key}`);
    result.set(key, value);
  }
  return result;
}

3. Smart Constructor
// ❌ 外部から直接構築可能
pub struct Email(String);

// ✅ Parse: Smart constructorで検証済みを保証
mod email {
    pub struct Email(String);  // private field

    impl Email {
        pub fn parse(s: &str) -> Result<Self, ParseError> {
            if s.contains('@') && s.len() > 3 {
                Ok(Email(s.to_string()))
            } else {
                Err(ParseError::InvalidEmail)
            }
        }

        pub fn as_str(&self) -> &str { &self.0 }
    }
}

Shotgun Parsing

避けるべき: 入力検証がコード全体に散らばるパターン。

❌ 処理開始 → 部分処理 → 検証失敗 → ロールバック困難
✅ 境界で完全Parse → 処理は型を信頼 → 安全

適用指針
推奨
システム境界での入力処理（JSON, CLI引数, DB値）
複雑な不変式を持つドメインモデル
Maybe/Optionが頻出する箇所
"should never happen" コメントがある箇所
過剰適用を避ける
単一のerror "impossible"だけなら改修コスト大
既存APIとの互換性が必要な場合
パフォーマンスクリティカルなホットパス
レビュー観点

コードレビュー時の確認ポイント：

戻り値チェック: void/()を返す検証関数はないか
型の精度: より精密な型で表現できないか
境界の明確さ: 入力パースはシステム境界で完結しているか
shotgun: 検証ロジックがコード全体に散らばっていないか
詳細ガイドライン

言語別の実装パターン、型設計の詳細は references/patterns.md を参照。

関連スキル（併読推奨）

このスキルを使用する際は、以下のスキルも併せて参照すること：

domain-primitives-and-always-valid: スマートコンストラクタによるドメインプリミティブの設計
when-to-wrap-primitives: プリミティブ型をラップすべきかの判断基準
domain-building-blocks: 値オブジェクトの設計（parseパターンの適用先）
Weekly Installs
26
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