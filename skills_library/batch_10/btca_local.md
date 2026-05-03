---
title: btca-local
url: https://skills.sh/davis7dotsh/better-context/btca-local
---

# btca-local

skills/davis7dotsh/better-context/btca-local
btca-local
Installation
$ npx skills add https://github.com/davis7dotsh/better-context --skill btca-local
SKILL.md
BTCA Local

BTCA Local, aka "The Better Context App Local" is a simple app defined as a skill file. The purpose of this app is to search git repos cloned onto this machine.

the BTCA Search Workflow

<end_goal> a clear, concise answer to the question with code examples </end_goal>

Startup Cases:

This skill can be invoked in a couple different ways, and your behavior should reflect that:

user invoked without extra context/question

this is the "app startup" state, almost as if a terminal app was booted up.

Your job is to search the working directory ~/.btca/agent/sandbox at the top level, just to get a list of all the repos that have been previously cloned

Then you should simply output the following markdown (filling in the existing repos):

# BTCA Local

_use your coding agent to search any git repo locally_

Previously searched:

- repo 1
- ...

Give me a question and the link to a git repo to get started!
(we can also clean out or pre-load some resources to this list...)

you invoked because of user's prompt

in this case, your job is to answer/execute the users prompt faithfully, just while also using the btca search workflow when needed to better execute your task

user invoked while also giving a prompt/questions

this one's simple, simply answer the users prompt with the btca search workflow

Weekly Installs
184
Repository
davis7dotsh/bet…-context
GitHub Stars
1.1K
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn