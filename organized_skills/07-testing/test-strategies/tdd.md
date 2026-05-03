---
rating: ⭐⭐⭐
title: tdd
url: https://skills.sh/kimny1143/claude-code-template/tdd
---

# tdd

skills/kimny1143/claude-code-template/tdd
tdd
Installation
$ npx skills add https://github.com/kimny1143/claude-code-template --skill tdd
SKILL.md
/tdd - Test-Driven Development

テスト駆動開発ワークフローを実行する。

使い方
/tdd                    # 対話的にTDDを開始
/tdd UserService        # UserServiceのテストから開始
/tdd handlePayment edge # handlePaymentのエッジケーステスト

TDDサイクル
┌─────────────────────────────────────────────────┐
│  1. RED    → テストを書く（失敗することを確認） │
│  2. GREEN  → 最小限のコードで通す               │
│  3. REFACTOR → リファクタ（テストは通ったまま）│
└─────────────────────────────────────────────────┘

ワークフロー
Step 1: RED（テストを書く）

テスト対象を特定

新機能: 期待する入出力を定義
バグ修正: バグを再現するテストを書く

テストファイルを作成/更新

// tests/unit/services/user.service.test.ts
describe('UserService', () => {
  describe('createUser', () => {
    it('should create user with valid data', async () => {
      const result = await userService.createUser({
        email: 'test@example.com',
        name: 'Test User',
      });
      expect(result.id).toBeDefined();
      expect(result.email).toBe('test@example.com');
    });

    it('should throw error for duplicate email', async () => {
      // エッジケース
      await expect(
        userService.createUser({ email: 'existing@example.com', name: 'Test' })
      ).rejects.toThrow('Email already exists');
    });
  });
});


テスト実行 → 失敗を確認

npm run test -- --watch tests/unit/services/user.service.test.ts

Step 2: GREEN（実装する）

最小限の実装で通す

完璧を目指さない
ハードコードでもOK（後でリファクタ）
テストが通ることだけに集中

テスト実行 → 成功を確認

Step 3: REFACTOR（改善する）

テストが通った状態で:

重複を排除
命名を改善
構造を整理

テスト実行 → まだ通ることを確認

満足したら次のテストへ（Step 1に戻る）

テストの書き方ガイド
命名規則
describe('[対象]', () => {
  describe('[メソッド/機能]', () => {
    it('should [期待する動作] when [条件]', () => {
      // ...
    });
  });
});

カバーすべきケース
ケース	例
正常系	有効な入力で期待通り動作
境界値	0, 空文字, 配列の最初/最後
エラー系	無効な入力、null/undefined
エッジケース	並行アクセス、タイムアウト
モックの使い方
// 外部依存はモック
vi.mock('@/db', () => ({
  db: {
    select: vi.fn().mockReturnValue({
      from: vi.fn().mockReturnValue({
        where: vi.fn().mockResolvedValue([{ id: '1', name: 'Test' }]),
      }),
    }),
  },
}));

テストコマンド例
Vitest
npm run test                           # 全テスト
npm run test -- --watch               # ウォッチモード
npm run test -- tests/unit/specific   # 特定ディレクトリ
npm run test -- --coverage            # カバレッジ

Jest
npm test                              # 全テスト
npm test -- --watch                   # ウォッチモード
npm test -- --coverage                # カバレッジ

Playwright (E2E)
npm run test:e2e                      # 全E2E
npx playwright test --grep "login"    # 特定テスト

チェックリスト

TDD完了時の確認:

 テストが先に書かれた（実装より前）
 テストが一度失敗した（REDフェーズ）
 最小限の実装で通した（GREEN）
 リファクタ後もテストが通る
 エッジケースがカバーされている
 テスト名が動作を説明している
Weekly Installs
65
Repository
kimny1143/claud…template
GitHub Stars
3
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass