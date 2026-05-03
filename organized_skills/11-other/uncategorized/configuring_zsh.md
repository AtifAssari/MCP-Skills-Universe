---
rating: ⭐⭐
title: configuring-zsh
url: https://skills.sh/mrpointer/dotfiles/configuring-zsh
---

# configuring-zsh

skills/mrpointer/dotfiles/configuring-zsh
configuring-zsh
Installation
$ npx skills add https://github.com/mrpointer/dotfiles --skill configuring-zsh
SKILL.md
Zsh Shell Configuration
Quick Reference
Topic	Reference
Startup file order	startup-files.md
oh-my-zsh patterns	oh-my-zsh.md
powerlevel10k setup	powerlevel10k.md
sheldon plugin manager	sheldon.md
Plugin load order	plugins.md
Performance tuning	performance.md
Workflow Decision Tree
Need to...	Action
Set env vars / PATH / locales	Read startup-files.md → edit .zshenv or .zprofile
Configure aliases, keybinds, completions, prompt	Edit .zshrc
Fix performance issues	Read performance.md → profile startup
Add/configure plugins	Read plugins.md + relevant manager reference
Chezmoi Integration
Edit Zsh configs in the chezmoi source (this repo), not directly in ~
Respect {{ ... }} template blocks in files
Source naming: dot_zshrc → ~/.zshrc, private_dot_config/sheldon → ~/.config/sheldon
For chezmoi workflows, see managing-chezmoi skill
Default Guardrails
Keep .zshenv idempotent and fast; no external commands
No aliases/functions in .zshenv
Use typeset -gx VAR=... or export VAR=... with defensive checks
Set fpath before compinit; run compinit once only
Document plugin load order (especially zsh-autocomplete + zsh-syntax-highlighting)
Common Tasks
Task	Approach
Add env var	.zshenv (everywhere) vs .zprofile (login) vs .zshrc (interactive)
Fix PATH	Ensure ordering, remove duplicates, avoid PATH=$PATH:... in multiple files
Enable completions	Set fpath → compinit once → cache if needed
Add plugin	Choose manager → ensure correct load order
Setup p10k	Instant prompt block first in .zshrc → source ~/.p10k.zsh after plugins
Weekly Installs
19
Repository
mrpointer/dotfiles
GitHub Stars
2
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass