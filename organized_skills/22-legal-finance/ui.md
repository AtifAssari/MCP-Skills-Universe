---
rating: ⭐⭐⭐
title: ui
url: https://skills.sh/chachamaru127/claude-code-harness/ui
---

# ui

skills/chachamaru127/claude-code-harness/ui
ui
Installation
$ npx skills add https://github.com/chachamaru127/claude-code-harness --skill ui
SKILL.md
UI Skills

UIコンポーネントとフォームの生成を担当するスキル群です。

制約の優先順位と適用条件
基本は ${CLAUDE_SKILL_DIR}/references/ui-skills.md の制約を最優先で適用する。
${CLAUDE_SKILL_DIR}/references/frontend-design.md は「尖った/独自/表現強め/ブランド強化」などが明示された場合のみ適用する。
UI Skills の MUST/NEVER は原則維持。ただしユーザーが明示的に要求した場合のみ以下の例外を許可する:
グラデーション、発光、強い装飾
アニメーション（追加・拡張）
カスタム easing
機能詳細
機能	詳細
制約セット	See references/ui-skills.md / references/frontend-design.md
コンポーネント生成	See references/component-generation.md
フィードバックフォーム	See references/feedback-forms.md
実行手順
制約セットを適用（優先順位に従う）
品質判定ゲート（Step 0）
ユーザーのリクエストを分類
上記の「機能詳細」から適切な参照ファイルを読む
その内容に従って生成
Step 0: 品質判定ゲート（a11y チェックリスト）

UI コンポーネント生成時は、アクセシビリティを確保:

♿ アクセシビリティチェックリスト

生成する UI は以下を満たすことを推奨：

### 必須項目
- [ ] 画像に alt 属性を設定
- [ ] フォーム要素に label を関連付け
- [ ] キーボード操作可能（Tab でフォーカス移動）
- [ ] フォーカス状態が視覚的に分かる

### 推奨項目
- [ ] 色だけに依存しない情報伝達
- [ ] コントラスト比 4.5:1 以上（テキスト）
- [ ] aria-label / aria-describedby の適切な使用
- [ ] 見出し構造（h1 → h2 → h3）が論理的

### インタラクティブ要素
- [ ] ボタンに適切なラベル（「詳細」ではなく「製品詳細を見る」）
- [ ] モーダル/ダイアログのフォーカストラップ
- [ ] エラーメッセージがスクリーンリーダーで読まれる

VibeCoder 向け
♿ 誰でも使えるデザインにするために

1. **画像には説明をつける**
   - 「商品画像」ではなく「赤いスニーカー、正面から」

2. **クリックできる場所はキーボードでも操作可能に**
   - Tab キーで移動、Enter で決定

3. **色だけで判断させない**
   - 赤=エラー だけでなく、アイコン+テキストも

Weekly Installs
26
Repository
chachamaru127/c…-harness
GitHub Stars
598
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass