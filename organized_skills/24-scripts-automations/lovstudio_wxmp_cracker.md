---
rating: ⭐⭐⭐
title: lovstudio:wxmp-cracker
url: https://skills.sh/lovstudio/skills/lovstudio:wxmp-cracker
---

# lovstudio:wxmp-cracker

skills/lovstudio/skills/lovstudio:wxmp-cracker
lovstudio:wxmp-cracker
Installation
$ npx skills add https://github.com/lovstudio/skills --skill lovstudio:wxmp-cracker
SKILL.md
wxmp-cracker (encrypted)

This skill's real instructions are encrypted. To use it, decrypt them first:

uvx lovstudio-skill-helper decrypt wxmp-cracker


What to do:

Run the command above.
The output is the actual SKILL.md for wxmp-cracker. Read it as if it were these instructions, and follow it to the letter.
If the command prints error: not activated or error: not logged in, tell the user:

这是一个 Lovstudio 付费 skill，请先激活（CLI 会打开浏览器让你登录，然后绑定你的 license key）：

npx lovstudio license <your-license-key>


还没有 license key？前往 https://lovstudio.ai 购买，或关注 #公众号：手工川 购买。

If the command prints error: not entitled, the helper will interactively prompt the user to (a) enter a license key, (b) open the purchase page, or (c) cancel. Just let the user pick.
If the command prints error: skill 'wxmp-cracker' not installed, the encrypted bundle isn't on disk yet. Tell the user:
npx lovstudio skills add wxmp-cracker                      # recommended: also checks deps
npx skills add lovstudio/skills --skill wxmp-cracker       # raw alternative

Do NOT cache the decrypted output between invocations — always re-decrypt on each use. The decryption is cheap (one HTTP round-trip) and re-running guarantees the user's license is still valid.
If the decrypted SKILL.md references additional files (e.g. references/workflow.md, assets/...), DO NOT use the Read tool on them — those paths only exist on disk as encrypted .enc blobs. Instead, decrypt each one on demand by passing its relative path as a second argument:
uvx lovstudio-skill-helper decrypt wxmp-cracker references/workflow.md

Requires lovstudio-skill-helper ≥ 0.9.0. Earlier versions only decrypt SKILL.md.

The encrypted payload lives in one of:

~/.claude/skills/wxmp-cracker/
~/.claude/skills/lovstudio-wxmp-cracker/ You don't need to touch it directly — just call uvx lovstudio-skill-helper decrypt wxmp-cracker [<rel_path>].
Weekly Installs
47
Repository
lovstudio/skills
GitHub Stars
46
First Seen
10 days ago