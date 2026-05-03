---
rating: ⭐⭐
title: tax-invoice-credit-context
url: https://skills.sh/kazukinagata/shinkoku/tax-invoice-credit-context
---

# tax-invoice-credit-context

skills/kazukinagata/shinkoku/tax-invoice-credit-context
tax-invoice-credit-context
Installation
$ npx skills add https://github.com/kazukinagata/shinkoku --skill tax-invoice-credit-context
SKILL.md
インボイス仕入税額控除コンテキスト（Input Tax Credit Context）

このスキルはインボイス制度における仕入税額控除の要件・例外に関するコンテキストを提供する。

仕入税額控除の情報提供

仕入税額控除に関する回答を行う際は、references/input-tax-credit-rules.md を読み込んで以下を実行する:

原則（適格請求書＋帳簿の保存）を確認して案内する
帳簿のみ保存の恒久特例6類型（公共交通機関・自販機・郵便等）への該当を確認する
免税事業者からの仕入れに係る経過措置の控除率（80%→70%→50%→30%→0%）を案内する
課税売上割合に応じた控除方式（全額控除・個別対応方式・一括比例配分方式）を説明する
保存期間（7年間）と電子取引データ保存の要件を案内する
参照ファイル
ファイル	内容
references/input-tax-credit-rules.md	仕入税額控除の原則・帳簿記載要件・恒久特例6類型・経過措置・課税売上割合と控除方式
Weekly Installs
135
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