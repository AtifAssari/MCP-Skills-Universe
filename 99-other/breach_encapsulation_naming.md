---
title: breach-encapsulation-naming
url: https://skills.sh/j5ik2o/okite-ai/breach-encapsulation-naming
---

# breach-encapsulation-naming

skills/j5ik2o/okite-ai/breach-encapsulation-naming
breach-encapsulation-naming
Installation
$ npx skills add https://github.com/j5ik2o/okite-ai --skill breach-encapsulation-naming
SKILL.md
Breach Encapsulation Naming

getterを作るなら「カプセル化を破っている」と名前で叫べ。

核心原則

ドメインモデルのgetterには breachEncapsulationOf プレフィックスを付与し、カプセル化を破っていることを明示する。

アプローチ	特徴	効果
通常のgetter (getName())	気軽に使える	濫用されやすい
明示的なgetter (breachEncapsulationOfName())	使用時に「破っている」と意識	濫用を抑制
なぜこの命名規約が必要か
ジレンマ
Tell Don't Ask原則: getterを使わず、オブジェクトに命じるべき
現実の制約: 永続化やJSON変換ではgetterが必要
問題: getterがあると、ビジネスロジックでも使ってしまう
解決策

getterを「長くて目立つ名前」にすることで：

使うたびに「これは例外的な使用だ」と意識させる
コードレビューで発見しやすくなる
静的解析ツールで検出可能になる
命名パターン
基本形式
breachEncapsulationOf<PropertyName>()

言語別の例
// Java
public String breachEncapsulationOfName() { return this.name; }
public Money breachEncapsulationOfPrice() { return this.price; }

// Kotlin
fun breachEncapsulationOfName(): String = name
fun breachEncapsulationOfPrice(): Money = price

// TypeScript
breachEncapsulationOfName(): string { return this.name; }
breachEncapsulationOfPrice(): Money { return this.price; }

# Python
def breach_encapsulation_of_name(self) -> str:
    return self._name

// Go
func (u *User) BreachEncapsulationOfName() string { return u.name }

// Rust
pub fn breach_encapsulation_of_name(&self) -> &str { &self.name }

適用判断フロー
getterが必要か？
    ↓
├─ NO → getterを作らない（Tell Don't Ask）
│
└─ YES → 対象は？
          │
          ├─ 値オブジェクト → 通常のアクセサでOK
          │   （イミュータブルかつ振る舞いが限定的なため）
          │   例: Money.amount(), UserId.value()
          │
          └─ エンティティ → breachEncapsulationOf を使用
                            │
                            └─ なぜ必要？
                                ├─ 永続化/シリアライズ → ✅ 許容
                                ├─ 表示/UI → ✅ 許容
                                ├─ テスト → ✅ 許容
                                └─ ビジネスロジック → ❌ Tell パターンに変換

値オブジェクト vs エンティティ
種類	特徴	getter方針
値オブジェクト	イミュータブル、等価性で識別	通常のアクセサ可（amount(), value()）
エンティティ	ミュータブル、IDで識別	breachEncapsulationOf を使用

理由: 値オブジェクトは内部状態が変わらないため、getterを公開しても「状態を取得→外部で判断→更新」というAskパターンが発生しにくい。

アンチパターン検出

以下のパターンを見つけたら警告：

// ❌ breachEncapsulationOf + if → Tell Don't Ask違反
if (user.breachEncapsulationOfAge() >= 18) {
    // ロジック
}

// ❌ breachEncapsulationOf + 計算 → ロジックが外部に漏れている
total = item.breachEncapsulationOfPrice() * item.breachEncapsulationOfQuantity();

// ❌ 連鎖呼び出し → デメテルの法則違反
order.breachEncapsulationOfCustomer().breachEncapsulationOfAddress().getCity();

許容される使用例
1. 永続化層（リポジトリ実装）
// ✅ 永続化のためのアクセスは許容
public UserEntity toEntity(User user) {
    return new UserEntity(
        user.breachEncapsulationOfId(),
        user.breachEncapsulationOfName(),
        user.breachEncapsulationOfEmail()
    );
}

2. JSON/XMLシリアライズ
// ✅ DTOへの変換は許容
toJson(): UserJson {
    return {
        id: this.breachEncapsulationOfId(),
        name: this.breachEncapsulationOfName()
    };
}

3. テストでのアサーション
// ✅ テストでの検証は許容
@Test
void shouldChangeName() {
    user.rename("New Name");
    assertEquals("New Name", user.breachEncapsulationOfName());
}

4. デバッグ/ログ出力
# ✅ デバッグ目的は許容
logger.debug(f"User: {user.breach_encapsulation_of_name()}")

実装ガイドライン
1. ドメインモデル側
public class User {
    private final UserId id;
    private String name;
    private Email email;

    // ❌ 通常のgetterは作らない
    // public String getName() { return name; }

    // ✅ カプセル化を破ることを明示
    public String breachEncapsulationOfName() {
        return name;
    }

    // ✅ ビジネスロジックは振る舞いとして提供
    public void rename(String newName) {
        validateName(newName);
        this.name = newName;
    }

    public boolean hasName(String name) {
        return this.name.equals(name);
    }
}

2. インフラ層での使用
// リポジトリ実装
public class JpaUserRepository implements UserRepository {
    @Override
    public void save(User user) {
        UserEntity entity = new UserEntity();
        entity.setId(user.breachEncapsulationOfId().value());
        entity.setName(user.breachEncapsulationOfName());
        entity.setEmail(user.breachEncapsulationOfEmail().value());
        jpa.save(entity);
    }
}

コードレビュー観点
チェック項目	対応
breachEncapsulationOf + if	Tellパターンへの変換を提案
breachEncapsulationOf + 計算	計算ロジックをオブジェクトに移動
ドメイン層での使用	永続化/シリアライズ以外なら警告
連鎖呼び出し	委譲メソッドの追加を提案
通常のgetter (getName())	breachEncapsulationOf への変更を提案
静的解析との連携
カスタムリントルール例
# 検出ルール
1. breachEncapsulationOf の後に if/switch が続く → 警告
2. ドメイン層で breachEncapsulationOf を呼び出している → 警告
3. 通常の get プレフィックスがドメインモデルにある → 警告

関連スキル
スキル	関係
tell-dont-ask	本スキルの前提。getterを使わない設計を優先
first-class-collection	コレクションのカプセル化にも同じ原則を適用
domain-building-blocks	値オブジェクト設計との整合性
参考文献
かとじゅん「ドメインオブジェクトのためのGetter/Setter」(2018)
https://blog.j5ik2o.me/entry/2018/08/14/134125
本スキルの原典。カプセル化の歴史的劣化とbreachEncapsulationOf命名規約の提案
詳細ガイドライン

言語別の詳細な実装パターンは references/patterns.md を参照。

関連スキル（併読推奨）

このスキルを使用する際は、以下のスキルも併せて参照すること：

tell-dont-ask: getterを避けるべき理由の基盤原則
law-of-demeter: getter連鎖が違反する構造面の原則
first-class-collection: コレクションのカプセル化パターン
Weekly Installs
27
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