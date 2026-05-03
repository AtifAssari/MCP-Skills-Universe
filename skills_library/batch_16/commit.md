---
title: commit
url: https://skills.sh/arjenschwarz/agentic-coding/commit
---

# commit

skills/arjenschwarz/agentic-coding/commit
commit
Installation
$ npx skills add https://github.com/arjenschwarz/agentic-coding --skill commit
SKILL.md
Commits
Use the command line to get an overview of the staged git changes. If no changes are staged, stage all files.
Determine if the changes include code files (not just documentation like .md files, comments, or config files). If code changes are present, run all formatting and test commands. If only documentation changes, skip tests and linting. If running the formatting resulted in unstaged changes to files, stage these as well. DO NOT revert code changes unless specifically asked to do so.
Create a concise, well-documented summary of the changes in the format as defined at keepachangelog.com, excluding any changes to the changelog file itself. Use proper formatting and be specific about the changes. Ignore the marking of tasks as complete.
Read the CHANGELOG.md file, if the file does not exist, create it.
Verify if the summary is already present in the changelog, if not add it to the top of the file.
Add the changelog to staged commits
Verify the current git branch using the git command.
Extract any ticket numbers from the branch, check for the below options based on what is likely. a. Extract the ticket number from the branch. The ticket number will be in the format ABC-123 and will be the combination of 1-5 letters or numbers, a -, and 1-5 numbers. This will be at the start of the branch name, possibly preceeded by something like feature/ or hotfix/. b. Check for a pure number, this would likely reflect a GitHub Issue.
If a ticket number was found, use this as the commit message prefix, otherwise use [feat] / [bug] / [doc] as appropriate based on any prefixes in the branchname and/or the code changes
Summarise the changes into a multi-line detailed commit message, prefixed with the commit message prefix and :. Do NOT include any co-authored-by information in the commit message.
Commit the code
Weekly Installs
18
Repository
arjenschwarz/ag…c-coding
GitHub Stars
18
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass