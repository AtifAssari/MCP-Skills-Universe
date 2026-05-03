---
rating: ⭐⭐
title: deepresearch-readme
url: https://skills.sh/j5ik2o/okite-ai/deepresearch-readme
---

# deepresearch-readme

skills/j5ik2o/okite-ai/deepresearch-readme
deepresearch-readme
Installation
$ npx skills add https://github.com/j5ik2o/okite-ai --skill deepresearch-readme
SKILL.md
Deepresearch Readme

GitHub OSS向けREADMEを、短時間で「何ができるか」と「どう始めるか」が伝わる状態に整える。

進め方
前提を確定する。
プロジェクト種別を特定する: ライブラリ / CLI / Webアプリ / GitHub Action
対象読者を特定する: 利用者 / 評価者 / コントリビューター
READMEの目的を確定する: 新規作成 / 改善 / レビュー
ファーストビューを構成する。
H1にプロジェクト名を書く
1〜2文で価値を書く（技術スタック説明より先に価値を出す）
Quickstartへの最短導線を置く
必要な主要リンクだけを置く（Docs、Issues、Releases）
Quickstartを最短化する。
Requirements、Install、Run の順で3〜6行程度に収める
実際に実行できるコマンドだけを残す
OS差分が長くなる場合は docs/installation.md へ分離する
構成を仕上げる。
セクションは以下を基本とする:
Highlights
Quickstart
Usage
Documentation
Getting help
Contributing
License
詳細説明は docs/ に切り出し、READMEには相対リンクだけ残す
最終検証を行う。
5分以内に「導入→最小実行」までたどれるか確認する
リンク切れ、前提バージョン、手順の古さを確認する
references/readme-review-checklist.md で網羅確認する
出力テンプレート

README本文を作るときは references/readme-template.md のテンプレートを優先して使う。

レビュー方針

既存READMEをレビューするときは以下を優先する。

Critical
Quickstartが実行不能
必須情報（What/How to start/Help）が欠落
READMEが巨大化し、開始手順が埋もれている
Warning
セクション順が読み手の意思決定順とずれている
docsへの導線が弱い
バッジやリンクが多すぎて価値が伝わりにくい
Info
表現の簡潔化
例の追加（CLI実行例、最小コード例）
FAQやトラブルシューティングへの導線追加
参照ファイル
実践チェックリスト: references/readme-review-checklist.md
README雛形: references/readme-template.md
Weekly Installs
19
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