---
rating: ⭐⭐⭐⭐⭐
title: github-pull-request-description
url: https://skills.sh/longbridge/gpui-component/github-pull-request-description
---

# github-pull-request-description

skills/longbridge/gpui-component/github-pull-request-description
github-pull-request-description
Installation
$ npx skills add https://github.com/longbridge/gpui-component --skill github-pull-request-description
SKILL.md
Description

We less than 150 words description for a PR changes, including new features, bug fixes, and improvements. And if there have APIs break changes (Only crates/ui changes) we should have a section called ## Breaking Changes to list them clearly.

Breaking changes description

When a pull request introduces breaking changes to a codebase, it's important to clearly communicate these changes to users and developers who rely on the code. A well-written breaking changes description helps ensure that everyone understands what has changed, why it has changed, and how to adapt to the new version.

We can get the changes from the PR diff and summarize them in a clear and concise manner. Aim to provide a clear APIs changes for users to follow.

Format

We pefer the following format for breaking changes descriptions:

Use bullet list for each breaking change item.
Each item should have title and a code block showing the old and new usage by use diff.
Use ## Breaking Changes as the section title.
Use english language.

For example:

## Breaking Changes

- Added `id` parameter to `Sidebar::new`.

```diff
- Sidebar::new()
+ Sidebar::new("sidebar")
```

- Removed the `left` and `right` methods; use `side` instead.
  > Default is left.

```diff
- Sidebar::right()
+ Sidebar::new("sidebar").side(Side::Right)
```

Weekly Installs
138
Repository
longbridge/gpui…omponent
GitHub Stars
11.3K
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn