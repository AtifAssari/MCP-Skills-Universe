---
rating: ⭐⭐⭐
title: mdx-article-publisher
url: https://skills.sh/foreveryh/deeptoai-skills/mdx-article-publisher
---

# mdx-article-publisher

skills/foreveryh/deeptoai-skills/mdx-article-publisher
mdx-article-publisher
Installation
$ npx skills add https://github.com/foreveryh/deeptoai-skills --skill mdx-article-publisher
SKILL.md
MDX Article Publisher

通用 MDX 文档发布工具 - 适用于任何 MDX 项目（Fumadocs、Next.js、Docusaurus 等）。

Prerequisites
Git repository with MDX files
Python 3.x (for validation script)
Write access to content directories
Git credentials configured
支持的项目类型
项目类型	Build 命令	状态
Fumadocs	pnpm build:docs	✅ 已测试
Next.js + MDX	npm run build	✅ 兼容
Docusaurus	npm run build	✅ 兼容
通用 MDX	自定义	✅ 可配置
Workflow
Step 0: 配置 Build 命令（首次使用）

Fumadocs / shiptiny:

# pnpm monorepo
pnpm build:docs


Next.js:

npm run build


自定义:

# 在 skill 执行时询问用户

Step 1: Identify Target Files

Single article:

content/docs/en/ai-ml/my-article.mdx


Multiple articles:

content/docs/en/ai-ml/


The skill will detect:

New MDX files
Modified MDX files
Multi-language versions (en, zh, fr)
Step 2: Check Git Status
git status
git diff --staged

Step 3: Run Validation
3.1 MDX Syntax Validation
python scripts/validate_mdx.py /path/to/article.mdx
# Or directory:
python scripts/validate_mdx.py content/docs/en/ai-ml/


What it checks:

✅ YAML frontmatter (title, description, lang)
✅ Unescaped operators (> → &gt;, < → &lt;)
✅ MDX component tag balance
✅ Common syntax errors
3.2 Build Validation (Recommended)
# For Fumadocs/Next.js
pnpm build:docs

# Or generic
npm run build


Build catches all MDX syntax errors that validation script may miss.

Step 4: Review Validation Results

Example output:

❌ ERRORS (2):
  File: content/docs/en/ai-ml/article.mdx:730
  Error: Unescaped operator. Use &gt; instead of > in: >80% accuracy

⚠️  WARNINGS (1):
  Warning: Lang code "ko" may not be supported.

📊 SUMMARY:
  Files valid: 0
  Errors: 2


Fix errors:

Replace > with &gt;, < with &lt;
Add missing frontmatter fields
Close unclosed MDX components
Step 5: Create Semantic Commit

Commit message format:

<type>(<scope>): <description>

[optional body]

[optional footer(s)]


Types:

feat: New article
fix: Article fix
docs: Documentation update
refactor: Major rewrite
translate: Translation update

Examples:

# New article
git commit -m "feat(ai-ml): add jina-vlm article"

# Multiple articles
git commit -m "feat(ai-ml): add 3 AI articles

- jina-vlm: vision language model
- rag-guide: RAG implementation
- embedding-basics: embedding intro

skill-analysis: jina-vlm, rag-guide"

# Translation
git commit -m "translate(zh): update jina-vlm to Chinese"

Step 6: Push to Remote
git push origin main


With verification:

# Pull first to avoid conflicts
git pull --rebase origin main

# Then push
git push origin main

Validation Rules
Required Frontmatter
---
title: Article Title
description: Brief description (1-2 sentences)
lang: en  # or zh, fr
---

Common Errors
Error	Cause	Fix
Unescaped operator	>80% in text	Use &gt;80%
Missing lang	No lang field	Add lang: en
Unclosed tag	<Callout> without </Callout>	Close all tags
Commit Type Detection
File Pattern	Type	Example
New file	feat	feat(ai-ml): add new article
Modified	docs	docs(ai-ml): update article
zh/ directory	translate	translate(zh): add Chinese version
Integration with Other Skills

Workflow:

fumadocs-article-importer
        ↓
skill-article-writer (optional)
        ↓
skill-article-publisher ← You are here

Troubleshooting
Issue	Solution
Build fails	Check MDX syntax, run validation first
Git push rejected	git pull --rebase, then retry
Validation timeout	Large project - use --no-build flag
Scripts
scripts/validate_mdx.py - MDX syntax validation
scripts/publish_article.py - Automated publish workflow
References
references/semantic-commit-guide.md - Commit message conventions
Weekly Installs
8
Repository
foreveryh/deept…i-skills
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass