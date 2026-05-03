---
rating: ⭐⭐
title: emacsclient
url: https://skills.sh/xenodium/emacs-skills/emacsclient
---

# emacsclient

skills/xenodium/emacs-skills/emacsclient
emacsclient
Installation
$ npx skills add https://github.com/xenodium/emacs-skills --skill emacsclient
SKILL.md
Always use emacsclient

The user has an Emacs server running. All Emacs operations must go through emacsclient, never emacs or emacs --batch. This includes both user-requested actions and agent-initiated operations like byte compilation, syntax checking, or running tests.

Examples
Open a file: emacsclient --no-wait "/path/to/file"
Evaluate elisp: emacsclient --eval '(some-function)'
Open at a line: emacsclient --no-wait +42 "/path/to/file"
Byte compile a file:
emacsclient --eval '
(byte-compile-file "/path/to/file.el")'

Check parentheses:
emacsclient --eval '
(with-temp-buffer
  (insert-file-contents "/path/to/file.el")
  (check-parens))'

Run ERT tests:
emacsclient --eval '
(progn
  (load "/path/to/test-file.el" nil t)
  (ert-run-tests-batch-and-exit "pattern"))'

Rules
Always use emacsclient, never emacs or emacs --batch.
Use --no-wait when opening files so the command returns immediately.
Use --eval when evaluating elisp.
Always format --eval elisp across multiple lines with proper indentation.
Run emacsclient commands via the Bash tool.
Weekly Installs
47
Repository
xenodium/emacs-skills
GitHub Stars
90
First Seen
Feb 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass