---
title: paper-context-resolver
url: https://skills.sh/lllllllama/ai-paper-reproduction-skill/paper-context-resolver
---

# paper-context-resolver

skills/lllllllama/ai-paper-reproduction-skill/paper-context-resolver
paper-context-resolver
Installation
$ npx skills add https://github.com/lllllllama/ai-paper-reproduction-skill --skill paper-context-resolver
SKILL.md
paper-context-resolver
When to apply
README and repo files leave a reproduction-critical gap.
The gap concerns dataset version, split, preprocessing, evaluation protocol, checkpoint mapping, or runtime assumptions.
The main skill needs a narrow evidence supplement instead of a full paper summary.
There is already a concrete reproduction question to answer.
When not to apply
The README already gives enough reproduction detail.
The user wants a general paper explanation rather than reproduction support.
The goal is to override README instructions without documenting the conflict.
The only available input is a paper title and there is no concrete reproduction gap yet.
Clear boundaries
This skill is optional.
This skill is helper-tier and should usually be orchestrator-invoked.
It supplements README-first reproduction.
It does not replace the main orchestration flow.
It does not summarize the whole paper by default.
Input expectations
target repo metadata
reproduction-critical question
existing README or repo evidence
any already known paper links
Output expectations
narrowed source list
reproduction-relevant answer only
explicit README-paper conflict note when applicable
clear distinction between direct evidence and inference
Notes

Use references/paper-assisted-reproduction.md.

Weekly Installs
63.1K
Repository
lllllllama/ai-p…on-skill
GitHub Stars
10
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn