---
rating: ⭐⭐⭐
title: qiita
url: https://skills.sh/vm0-ai/vm0-skills/qiita
---

# qiita

skills/vm0-ai/vm0-skills/qiita
qiita
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill qiita
SKILL.md
How to Use
Commands

The script supports 5 modules: item, user, tag, comment, auth

1. Item - Articles
Search Articles
scripts/qiita.sh item search --query "React hooks"
scripts/qiita.sh item search --query "tag:Python" --per-page 20
scripts/qiita.sh item search --query "user:username title:tutorial"

Parameter	Required	Default	Description
--query	Yes	-	Search query (supports tag:, user:, title:, body:, stocks:)
--page	No	1	Page number
--per-page	No	20	Items per page (max 100)
Get Article
scripts/qiita.sh item get --id "article_id"

Get My Articles
scripts/qiita.sh item mine --per-page 10

Post Article
scripts/qiita.sh item post --title "Article Title" --body "# Content" --tags "Python,Tutorial"
scripts/qiita.sh item post --title "Draft Post" --body-file ./article.md --tags "React" --private

Parameter	Required	Default	Description
--title	Yes	-	Article title
--body	Yes*	-	Article body in Markdown
--body-file	Yes*	-	Read body from file (alternative to --body)
--tags	Yes	-	Comma-separated tags (max 5)
--private	No	false	Create as private article
Update Article
scripts/qiita.sh item update --id "article_id" --title "New Title" --body "Updated content"

Delete Article
scripts/qiita.sh item delete --id "article_id"

2. User - User Information
Get Current User
scripts/qiita.sh user me

Get User Profile
scripts/qiita.sh user get --id "username"

Get User's Articles
scripts/qiita.sh user items --id "username" --per-page 10

Get User's Stocks
scripts/qiita.sh user stocks --id "username"

Get User's Followers/Following
scripts/qiita.sh user followers --id "username"
scripts/qiita.sh user following --id "username"

3. Tag - Tags
List Popular Tags
scripts/qiita.sh tag list --per-page 20
scripts/qiita.sh tag list --sort count

Parameter	Required	Default	Description
--page	No	1	Page number
--per-page	No	20	Tags per page
--sort	No	count	Sort by: count or name
Get Tag Info
scripts/qiita.sh tag get --id "Python"

Get Articles by Tag
scripts/qiita.sh tag items --id "JavaScript" --per-page 10

4. Comment - Comments
Get Article Comments
scripts/qiita.sh comment list --item-id "article_id"

Post Comment
scripts/qiita.sh comment post --item-id "article_id" --body "Great article!"

Delete Comment
scripts/qiita.sh comment delete --id "comment_id"

5. Auth - Authentication
Verify Token
scripts/qiita.sh auth verify


Returns current user info if token is valid.

Search Query Syntax

Qiita search supports special operators:

Operator	Example	Description
tag:	tag:Python	Filter by tag
user:	user:qiita	Filter by author
title:	title:tutorial	Search in title
body:	body:example	Search in body
stocks:	stocks:>100	Filter by stock count
created:	created:>2024-01-01	Filter by date

Combine operators: tag:React title:hooks stocks:>50

Examples
Search and Read Articles
# Search for Python tutorials
scripts/qiita.sh item search --query "tag:Python title:tutorial" --per-page 5

# Get specific article
scripts/qiita.sh item get --id "abc123def456"

Publish an Article
# Post from command line
scripts/qiita.sh item post --title "Getting Started with Docker" --body "# Introduction

Docker is a containerization platform..." --tags "Docker,DevOps,Tutorial"

# Post from file
scripts/qiita.sh item post --title "My Technical Article" --body-file ./my-article.md --tags "Programming"

Explore Tags and Users
# Get trending tags
scripts/qiita.sh tag list --per-page 10 --sort count

# Get user's articles
scripts/qiita.sh user items --id "famous_author" --per-page 5

Guidelines
Rate Limits: 1000 requests/hour (authenticated), 60/hour (unauthenticated)
Tags: Maximum 5 tags per article
Markdown: Article body supports GitHub-flavored Markdown
Private Articles: Use --private flag for drafts or private content
Search: Use operators for precise search results
API Reference
Documentation: https://qiita.com/api/v2/docs
Access Tokens: https://qiita.com/settings/tokens/new
Weekly Installs
63
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
1 day ago
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn