---
title: incorporation
url: https://skills.sh/kazukinagata/shinkoku/incorporation
---

# incorporation

skills/kazukinagata/shinkoku/incorporation
incorporation
Installation
$ npx skills add https://github.com/kazukinagata/shinkoku --skill incorporation
SKILL.md
法人成り（Incorporation）

個人事業主から法人への移行（法人成り）に関する包括的な知識ベース。 税額比較シミュレーション、法人形態の選択、設立手続き、役員報酬戦略を支援する。

設定の読み込み（最初に実行）
shinkoku.config.yaml を Read ツールで読み込む
ファイルが存在しない場合は /setup スキルの実行を案内して終了する
設定値を把握し、相対パスは CWD を基準に絶対パスに変換する:
db_path: MCP ツールの db_path 引数に使用
output_dir: 進捗ファイル等の出力先ベースディレクトリ
各ディレクトリ: ファイル参照時に使用
回答の基本方針
1. シミュレーション積極提示
法人成りの相談には、必ず税額シミュレーションを提示する
ユーザーの所得レベルに応じた具体的な数値比較を行う
税額だけでなく社会保険料も含めた総負担額で比較する
「法人成りすべき」と断定せず、メリット・デメリット双方を提示する
2. 正確性の担保
回答は必ず references/ ディレクトリ内のファイルを根拠とする
一般知識や推測で回答しない。根拠が見つからない場合はその旨を明示する
金額・税率・要件は reference ファイルの数値を引用する
条文・通達の参照を回答に含める（例: 法人税法第66条、会社法第575条）
3. 回答の構造

以下の構造で回答を組み立てる:

結論を先に: 法人成りの有利/不利の概要
シミュレーション: 個人 vs 法人の税負担比較
具体的な手続き: 必要なステップと届出
注意点・落とし穴: よくある失敗パターン
免責事項: 回答の末尾に必ず disclaimer を付記
リファレンスファイル参照ガイド

質問の内容に応じて、以下のリファレンスファイルを参照する:

質問カテゴリ	参照ファイル
個人 vs 法人の税額比較・損益分岐	references/tax-simulation.md
株式会社 vs 合同会社・設立手続き	references/corporate-forms.md
役員報酬の設定・社会保険戦略	references/compensation-strategy.md
回答パターン
パターンA: 法人成りすべきか
現在の事業所得をヒアリングする（不足情報は質問する）
references/tax-simulation.md の所得レベル別シミュレーションで該当区分を特定
個人 vs 法人の税負担を具体的な金額で比較
社会保険料の差額も含めた総合判断を提示
注意: 「すべき」と断定せず判断材料を提供する
パターンB: いつ法人成りすべきか
現在の所得と今後の見通しをヒアリングする
references/tax-simulation.md の損益分岐点（事業所得800万円前後）を提示
消費税の免税リセット効果（references/tax-simulation.md）を説明
references/corporate-forms.md のタイミング最適化（決算月の選択等）を案内
インボイス登録済みの場合の注意点を付記
パターンC: どの法人形態にすべきか
事業の規模・業種・将来計画をヒアリングする
references/corporate-forms.md の株式会社 vs 合同会社の比較表を提示
1人法人（マイクロ法人）の検討が適切かを判定
設立費用・ランニングコストの比較を具体額で示す
社会的信用・資金調達の観点からの助言を付記
パターンD: 設立手続きを教えて
references/corporate-forms.md の設立手続きフローを提示
必要書類・届出先・期限を一覧で示す
個人事業の廃業手続きも案内
消費税のインボイス登録移行の注意点を付記
税理士・司法書士への依頼が推奨される場面を説明
他スキルとのクロスリファレンス
関連スキル	用途	参照タイミング
tax-advisor	所得税の税率・控除の詳細、ライフプランニング	法人成り前の個人税額計算、iDeCo・小規模企業共済との比較
invoice-system	インボイス制度・消費税の経過措置	法人成り時のインボイス登録移行、2割特例の適用判定
consumption-tax	消費税の計算方法・簡易課税	法人の消費税負担のシミュレーション
免責事項

すべての回答の末尾に以下の免責事項を付記する:

---
この回答は一般的な税務情報の提供を目的としたものであり、個別の税務アドバイスではありません。
法人成りは税務・法務・社会保険等の多面的な判断が必要です。
具体的な意思決定にあたっては、税理士・司法書士等の専門家にご相談ください。
情報は令和7年分（2025年課税年度）の税制に基づいています。

特に免責を強調すべきケース
税額シミュレーション結果に基づく法人成りの判断
役員報酬の最適額の提案
マイクロ法人＋個人事業の二刀流スキームの提案
社会保険の適用に関する判断（年金事務所への確認を推奨）
税理士法第52条に抵触する可能性のある個別具体的な税務代理行為
Weekly Installs
258
Repository
kazukinagata/shinkoku
GitHub Stars
339
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass