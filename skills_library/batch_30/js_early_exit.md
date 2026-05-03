---
title: js-early-exit
url: https://skills.sh/theorcdev/8bitcn-ui/js-early-exit
---

# js-early-exit

skills/theorcdev/8bitcn-ui/js-early-exit
js-early-exit
Installation
$ npx skills add https://github.com/theorcdev/8bitcn-ui --skill js-early-exit
SKILL.md
Early Return from Functions

Return early when result is determined to skip unnecessary processing. This optimization is especially valuable when the skipped branch is frequently taken or when the deferred operation is expensive.

Incorrect (processes all items even after finding answer):

function validateUsers(users: User[]) {
  let hasError = false
  let errorMessage = ''

  for (const user of users) {
    if (!user.email) {
      hasError = true
      errorMessage = 'Email required'
    }
    if (!user.name) {
      hasError = true
      errorMessage = 'Name required'
    }
    // Continues checking all users even after error found
  }

  return hasError ? { valid: false, error: errorMessage } : { valid: true }
}


Correct (returns immediately on first error):

function validateUsers(users: User[]) {
  for (const user of users) {
    if (!user.email) {
      return { valid: false, error: 'Email required' }
    }
    if (!user.name) {
      return { valid: false, error: 'Name required' }
    }
  }

  return { valid: true }
}

Weekly Installs
24
Repository
theorcdev/8bitcn-ui
GitHub Stars
1.8K
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass