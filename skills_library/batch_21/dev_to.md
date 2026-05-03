---
title: dev.to
url: https://skills.sh/vm0-ai/vm0-skills/dev.to
---

# dev.to

skills/vm0-ai/vm0-skills/devto
devto
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill devto
SKILL.md
Troubleshooting

If requests fail, run zero doctor check-connector --env-name DEVTO_TOKEN or zero doctor check-connector --url https://dev.to/api/articles --method GET

How to Use

All examples below assume you have DEVTO_TOKEN set.

1. Publish an Article

Write to /tmp/devto_request.json:

{
  "article": {
    "title": "My Awesome Article",
    "body_markdown": "## Introduction\n\nThis is my article content.\n\n## Conclusion\n\nThanks for reading!",
    "published": false,
    "tags": ["javascript", "webdev"]
  }
}


Then run:

curl -s -X POST "https://dev.to/api/articles" -H "api-key: $DEVTO_TOKEN" -H "Content-Type: application/json" -d @/tmp/devto_request.json | jq '{id, url, published}'


Response:

{
  "id": 123456,
  "url": "https://dev.to/username/my-awesome-article-abc",
  "published": false
}

2. Publish Immediately

Set published: true to publish right away:

Write to /tmp/devto_request.json:

{
  "article": {
    "title": "Published Article",
    "body_markdown": "Content here...",
    "published": true,
    "tags": ["tutorial"]
  }
}


Then run:

curl -s -X POST "https://dev.to/api/articles" -H "api-key: $DEVTO_TOKEN" -H "Content-Type: application/json" -d @/tmp/devto_request.json | jq '{id, url, published}'

3. Publish with Cover Image

Write to /tmp/devto_request.json:

{
  "article": {
    "title": "Article with Cover",
    "body_markdown": "Content here...",
    "published": true,
    "tags": ["webdev", "tutorial"],
    "main_image": "https://example.com/cover.png"
  }
}


Then run:

curl -s -X POST "https://dev.to/api/articles" -H "api-key: $DEVTO_TOKEN" -H "Content-Type: application/json" -d @/tmp/devto_request.json | jq '{id, url}'

4. Publish from Markdown File

To publish from a markdown file, first convert it to JSON:

cat article.md | jq -Rs '.' > /tmp/content.json


Write to /tmp/devto_request.json:

{
  "article": {
    "title": "My Article Title",
    "body_markdown": "Your article content here...",
    "published": false,
    "tags": ["programming"]
  }
}


Then run:

curl -s -X POST "https://dev.to/api/articles" -H "api-key: $DEVTO_TOKEN" -H "Content-Type: application/json" -d @/tmp/devto_request.json | jq '{id, url, published}'

Managing Articles
5. Get Your Articles
curl -s "https://dev.to/api/articles/me?per_page=10" -H "api-key: $DEVTO_TOKEN" | jq '.[] | {id, title, published, url}'

6. Get Published Articles Only
curl -s "https://dev.to/api/articles/me/published?per_page=10" -H "api-key: $DEVTO_TOKEN" | jq '.[] | {id, title, url}'

7. Get Unpublished (Drafts)
curl -s "https://dev.to/api/articles/me/unpublished" -H "api-key: $DEVTO_TOKEN" | jq '.[] | {id, title}'

8. Get Single Article

Replace <your-article-id> with an actual article ID from the "List My Articles" response (example 5) or from the id field in the create article response (example 1).

curl -s "https://dev.to/api/articles/<your-article-id>" -H "api-key: $DEVTO_TOKEN" | jq '{id, title, url, published}'

9. Update an Article

Replace <your-article-id> with an actual article ID from the "List My Articles" response (example 5) or from the id field in the create article response (example 1).

Write to /tmp/devto_request.json:

{
  "article": {
    "title": "Updated Title",
    "body_markdown": "Updated content..."
  }
}


Then run:

curl -s -X PUT "https://dev.to/api/articles/<your-article-id>" -H "api-key: $DEVTO_TOKEN" -H "Content-Type: application/json" -d @/tmp/devto_request.json | jq '{id, url}'

10. Publish a Draft

Replace <your-article-id> with an actual article ID from the "List My Articles" response (example 5) or from the id field in the create article response (example 1).

Write to /tmp/devto_request.json:

{
  "article": {
    "published": true
  }
}


Then run:

curl -s -X PUT "https://dev.to/api/articles/<your-article-id>" -H "api-key: $DEVTO_TOKEN" -H "Content-Type: application/json" -d @/tmp/devto_request.json | jq '{id, url, published}'

Article Parameters
Parameter	Type	Description
title	string	Article title (required)
body_markdown	string	Content in Markdown
published	boolean	true to publish, false for draft
tags	array	Up to 4 tags (lowercase, no spaces)
main_image	string	Cover image URL
canonical_url	string	Original article URL (for cross-posts)
series	string	Series name to group articles
Examples
Tech Tutorial

Write to /tmp/devto_request.json:

{
  "article": {
    "title": "Getting Started with Docker",
    "body_markdown": "## What is Docker?\n\nDocker is a platform for developing...\n\n## Installation\n\n```bash\nbrew install docker\n```\n\n## Your First Container\n\n```bash\ndocker run hello-world\n```",
    "published": true,
    "tags": ["docker", "devops", "tutorial", "beginners"]
  }
}


Then run:

curl -s -X POST "https://dev.to/api/articles" -H "api-key: $DEVTO_TOKEN" -H "Content-Type: application/json" -d @/tmp/devto_request.json | jq '{url}'

Cross-post from Blog

Write to /tmp/devto_request.json:

{
  "article": {
    "title": "My Blog Post",
    "body_markdown": "Content from my blog...",
    "published": true,
    "canonical_url": "https://myblog.com/original-post",
    "tags": ["webdev"]
  }
}


Then run:

curl -s -X POST "https://dev.to/api/articles" -H "api-key: $DEVTO_TOKEN" -H "Content-Type: application/json" -d @/tmp/devto_request.json | jq '{url}'

Article in a Series

Write to /tmp/devto_request.json:

{
  "article": {
    "title": "React Hooks - Part 1: useState",
    "body_markdown": "First part of the series...",
    "published": true,
    "series": "React Hooks Deep Dive",
    "tags": ["react", "javascript", "hooks"]
  }
}


Then run:

curl -s -X POST "https://dev.to/api/articles" -H "api-key: $DEVTO_TOKEN" -H "Content-Type: application/json" -d @/tmp/devto_request.json | jq '{url}'

Guidelines
Max 4 tags: Dev.to limits articles to 4 tags
Lowercase tags: Tags should be lowercase without spaces
Escape markdown: Use jq -Rs to properly escape markdown content
Cover images: Must be URLs, not local files
Draft first: Set published: false to review before publishing
Check response: Always verify the returned URL
Weekly Installs
39
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
Jan 24, 2026