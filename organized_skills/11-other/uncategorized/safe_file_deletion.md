---
rating: ⭐⭐
title: safe-file-deletion
url: https://skills.sh/memtensor/memos/safe-file-deletion
---

# safe-file-deletion

skills/memtensor/memos/safe-file-deletion
safe-file-deletion
Installation
$ npx skills add https://github.com/memtensor/memos --skill safe-file-deletion
SKILL.md
Safe File Deletion
Rule

Before deleting ANY file, you MUST:

Call request_file_permission with operation: "delete"
For multiple files, use filePaths array (not multiple calls)
Wait for response
Only proceed if "allowed"
If "denied", acknowledge and do NOT delete
Applies To
rm commands (single or multiple files)
rm -rf (directories)
unlink, fs.rm, fs.rmdir
Any script or tool that deletes files
Examples

Single file:

{
  "operation": "delete",
  "filePath": "/path/to/file.txt"
}


Multiple files (batched into one prompt):

{
  "operation": "delete",
  "filePaths": ["/path/to/file1.txt", "/path/to/file2.txt"]
}

No Workarounds

Never bypass deletion warnings by:

Emptying files instead of deleting
Moving to hidden/temp locations
Using obscure commands

The user will see a prominent warning. Wait for explicit approval.

Weekly Installs
30
Repository
memtensor/memos
GitHub Stars
8.9K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass