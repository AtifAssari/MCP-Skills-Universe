---
rating: ⭐⭐
title: rewrite-rustdoc
url: https://skills.sh/jim60105/copilot-prompt/rewrite-rustdoc
---

# rewrite-rustdoc

skills/jim60105/copilot-prompt/rewrite-rustdoc
rewrite-rustdoc
Installation
$ npx skills add https://github.com/jim60105/copilot-prompt --skill rewrite-rustdoc
SKILL.md
Rewrite Rustdoc

Ensure all Rust documentation and comments are exclusively written in English, following rustdoc guidelines.

Steps

Determine which files to process:

If the user provides a method to find files, use that method.
Otherwise, assume files are in the src/ directory.
Proceed immediately to the next steps after acquiring file information.

Conduct a comprehensive review to ensure all documentation and comments are in English.

Any Chinese text in documentation or code comments must be identified and corrected.
Chinese characters in test case strings are permissible and do not require modification.
Chinese report files should not be modified — focus on Rust source code files only.

Search for Chinese characters in the source code:

rg -n "[\u4e00-\u9fff]" src/


Check for missing documentation:

cd src/ && cargo clippy -- -W missing_docs


Replace src/ with the user-specified location if provided.

Refer to ./docs/rustdoc-guidelines.md for documentation structure and style standards.

Ensure all corrections adhere strictly to the documentation guidelines.

Repeat the search and revision process iteratively until no further occurrences require modification.

Do not prompt for confirmation before proceeding to the next item.
Complete all necessary changes before reporting back.
Weekly Installs
11
Repository
jim60105/copilot-prompt
GitHub Stars
18
First Seen
8 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass