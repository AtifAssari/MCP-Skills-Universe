---
rating: ⭐⭐⭐
title: gh-link-subissues
url: https://skills.sh/seika139/dotfiles/gh-link-subissues
---

# gh-link-subissues

skills/seika139/dotfiles/gh-link-subissues
gh-link-subissues
Installation
$ npx skills add https://github.com/seika139/dotfiles --skill gh-link-subissues
SKILL.md
GitHub Sub-issue 紐付けスキル

親 Issue に1つ以上の子 Issue を Sub-issue として紐付けます。 異なるリポジトリ間（クロスリポジトリ）でも紐付け可能です。 紐付け後、全 Issue を GitHub Project に自動追加します。

前提条件
gh CLI がインストール・認証済みであること
対象リポジトリへのアクセス権があること
設定ファイル

GitHub Project への追加に使用する設定は ~/.claude/custom-config/create-issue-config.json から読み込みます。 /create-issue スキルと設定を共有し、二重管理を防ぎます。

{
  "project": {
    "owner": "org-or-user-name",
    "number": 1
  }
}


設定ファイルが存在しない場合は、Project への追加をスキップし、ユーザーに設定ファイルの作成を案内してください。

入力

ユーザーから以下の情報を収集してください：

親 Issue: owner/repo#number 形式または GitHub URL
子 Issue（1つ以上）: owner/repo#number 形式または GitHub URL のリスト
手順
Step 1: Issue の Node ID を取得

各 Issue の Node ID を GitHub GraphQL API で取得します。 同一リポジトリの Issue はエイリアスを使って1回の API コールでまとめて取得できます。

# 単一 Issue の Node ID 取得
gh api graphql -f query='
query($owner: String!, $repo: String!, $number: Int!) {
  repository(owner: $owner, name: $repo) {
    issue(number: $number) { id title }
  }
}' -f owner="OWNER" -f repo="REPO" -F number=NUMBER \
  -q '.data.repository.issue.id'

# 同一リポジトリの複数 Issue をエイリアスで一括取得
gh api graphql -f query='
query {
  repository(owner: "OWNER", name: "REPO") {
    i1: issue(number: 10) { id title }
    i2: issue(number: 20) { id title }
  }
}' -q '.data.repository'

Step 2: addSubIssue mutation で紐付け

取得した Node ID を使い、各子 Issue を親 Issue に紐付けます。

gh api graphql -f query='
mutation($parent: ID!, $child: ID!) {
  addSubIssue(input: {issueId: $parent, subIssueId: $child}) {
    issue { id title }
    subIssue { id title }
  }
}' -f parent="PARENT_NODE_ID" -f child="CHILD_NODE_ID"


子 Issue が複数ある場合は、それぞれに対して mutation を実行してください。

Step 3: GitHub Project に追加

~/.claude/custom-config/create-issue-config.json から project.owner と project.number を読み込み、 親 Issue と全子 Issue を GitHub Project に追加します。

# 設定ファイルから Project 情報を読み込み
PROJECT_OWNER=$(jq -r '.project.owner' ~/.claude/custom-config/create-issue-config.json)
PROJECT_NUMBER=$(jq -r '.project.number' ~/.claude/custom-config/create-issue-config.json)

# 全 Issue（親 + 子）を Project に追加
# gh project item-add は冪等（既に追加済みでもエラーにならない）
gh project item-add "$PROJECT_NUMBER" --owner "$PROJECT_OWNER" --url "ISSUE_URL"


親 Issue と全子 Issue それぞれに対して実行してください。 Issue の URL は https://github.com/{owner}/{repo}/issues/{number} の形式です。

Step 4: Project フィールドの設定

Project に追加した各 Issue の Status、Priority、Start date を設定します。

4a. Project のフィールド定義を取得
gh api graphql -f query='
{
  user(login: "PROJECT_OWNER") {
    projectV2(number: PROJECT_NUMBER) {
      id
      fields(first: 30) {
        nodes {
          ... on ProjectV2Field {
            id
            name
            dataType
          }
          ... on ProjectV2SingleSelectField {
            id
            name
            options { id name }
          }
        }
      }
    }
  }
}'


取得すべきフィールド ID:

Status フィールド ID と各オプション（Backlog, In progress 等）の ID
Priority フィールド ID と各オプション（P0, P1, P2）の ID
Start date フィールド ID
4b. 各 Issue の Project Item ID を取得
gh api graphql -f query='
{
  repository(owner: "OWNER", name: "REPO") {
    issue(number: NUMBER) {
      projectItems(first: 5) {
        nodes {
          id
          project { id }
        }
      }
    }
  }
}' -q '.data.repository.issue.projectItems.nodes[] | select(.project.id == "PROJECT_ID") | .id'


同一リポジトリの Issue はエイリアスでまとめて取得可能。

4c. フィールド値を設定
# Status の設定
gh project item-edit --project-id "PROJECT_ID" --id "ITEM_ID" \
  --field-id "STATUS_FIELD_ID" --single-select-option-id "OPTION_ID"

# Priority の設定
gh project item-edit --project-id "PROJECT_ID" --id "ITEM_ID" \
  --field-id "PRIORITY_FIELD_ID" --single-select-option-id "OPTION_ID"

# Start date の設定
gh project item-edit --project-id "PROJECT_ID" --id "ITEM_ID" \
  --field-id "START_DATE_FIELD_ID" --date "$(date +%Y-%m-%d)"

フィールド値の決定ルール
フィールド	値の決定方法
Status	デフォルト: Backlog。ユーザーが指示した場合はその値
Priority	Issue タイトルに [P0]/[P1]/[P2] プレフィックスがあればそれに対応。なければスキップ
Start date	create-issue-config.json の project.start_date が "today" なら今日の日付。それ以外はスキップ

親 Issue には Priority を設定しない（子 Issue の優先度が混在するため）。

Step 5: 結果の確認

紐付けと Project 設定の結果をまとめて報告してください：

紐付け成功した親 Issue と子 Issue のタイトル
Project に追加された Issue の件数
設定したフィールド（Status, Priority, Start date）の内訳
エラーが発生した場合はその内容
注意事項
-f は文字列パラメータ、-F は数値パラメータに使う（number は Int! 型なので -F）
-q は jq フィルタで結果から特定フィールドを抽出する
Node ID は I_kwDO で始まるグローバルに一意な識別子
既に紐付け済みの場合はエラーが返る
gh project item-add は冪等なので、既に Project に追加済みの Issue に対しても安全に実行できる
gh project item-edit も冪等なので、既に設定済みのフィールドに同じ値を再設定しても問題ない
設定ファイルが存在しない場合は Project 追加とフィールド設定をスキップし、Sub-issue 紐付けのみ実行する
Project Item ID は Issue の Node ID とは異なる。Issue → projectItems → 対象 Project でフィルタという手順で取得する
Weekly Installs
10
Repository
seika139/dotfiles
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass