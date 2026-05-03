---
title: creative-seeds
url: https://skills.sh/aviz85/claude-skills-library/creative-seeds
---

# creative-seeds

skills/aviz85/claude-skills-library/creative-seeds
creative-seeds
Installation
$ npx skills add https://github.com/aviz85/claude-skills-library --skill creative-seeds
SKILL.md
Creative Seeds

Before any creative task, run the script below — it selects 3 random seeds and returns them directly.

How to Use

Run this to pull 3 random seeds:

python3 -c "
import random, re, os
with open(os.path.expanduser('~/.claude/skills/creative-seeds/seeds.md')) as f:
    content = f.read()
seeds = [s.strip() for s in re.split(r'\n---\n', content) if re.search(r'##\s*\d+\.', s)]
random.shuffle(seeds)
print('\n\n---\n\n'.join(seeds[:3]))
"

Instructions
Run the bash command above — it returns 3 randomly selected seed paragraphs
Read the output — let the absurdist logic seep in
Then proceed with the actual creative task with that mental residue active
Do NOT explain the seeds to the user unless asked — just use them internally to shift your thinking frame

The seeds are not prompts. They are cognitive disruptors. They work by contaminating your pattern-matching with nonsense, forcing novel connections.

Weekly Installs
18
Repository
aviz85/claude-s…-library
GitHub Stars
27
First Seen
Mar 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass