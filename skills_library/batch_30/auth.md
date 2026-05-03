---
title: auth
url: https://skills.sh/chachamaru127/claude-code-harness/auth
---

# auth

skills/chachamaru127/claude-code-harness/auth
auth
Installation
$ npx skills add https://github.com/chachamaru127/claude-code-harness --skill auth
SKILL.md
Auth Skills

認証と決済機能の実装を担当するスキル群です。

機能詳細
機能	詳細
認証機能	See references/authentication.md
決済機能	See references/payments.md
実行手順
品質判定ゲート（Step 0）
ユーザーのリクエストを分類(認証 or 決済)
上記の「機能詳細」から適切な参照ファイルを読む
その内容に従って実装
Step 0: 品質判定ゲート（セキュリティチェックリスト）

認証・決済機能は常にセキュリティリスクが高いため、作業開始前に必ず以下を表示:

🔐 セキュリティチェックリスト

この作業はセキュリティ上重要です。以下を確認してください：

### 認証関連
- [ ] パスワードはハッシュ化（bcrypt/argon2）
- [ ] セッション管理は安全か（HTTPOnly Cookie）
- [ ] CSRF 対策は実装されているか
- [ ] レート制限（ブルートフォース対策）

### 決済関連
- [ ] 機密情報（カード番号等）をサーバーに保存しない
- [ ] Stripe/決済プロバイダの SDK を正しく使用
- [ ] Webhook の署名検証
- [ ] 金額改ざん防止（サーバー側で金額を確定）

### 共通
- [ ] エラーメッセージが詳細すぎないか（情報漏洩防止）
- [ ] ログに機密情報を出力していないか

セキュリティ重要度表示
⚠️ 注意レベル: 🔴 高

この機能は以下のリスクがあります：
- 認証情報の漏洩
- 不正アクセス
- 決済の不正操作

専門家によるレビューを推奨します。

VibeCoder 向け
🔐 安全にログイン・決済機能を作るために

1. **パスワードは「ハッシュ化」する**
   - 元のパスワードを復元できない形で保存
   - 万が一データが漏れても安全

2. **カード情報はサーバーに保存しない**
   - Stripe などの専用サービスに任せる
   - 自分のサーバーには一切保存しない

3. **エラーメッセージは曖昧に**
   - 「パスワードが違います」ではなく「認証に失敗しました」
   - 悪意ある人にヒントを与えない

Weekly Installs
36
Repository
chachamaru127/c…-harness
GitHub Stars
598
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn