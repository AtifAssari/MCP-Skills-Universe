---
rating: ⭐⭐⭐
title: update-documentation
url: https://skills.sh/tenzir/skills/update-documentation
---

# update-documentation

skills/tenzir/skills/update-documentation
update-documentation
Installation
$ npx skills add https://github.com/tenzir/skills --skill update-documentation
SKILL.md
Update Documentation

Handle the operational workflow around docs.tenzir.com changes.

Workflow
Ensure .docs/ exists and is up to date by cloning tenzir/docs or fetching from origin.
Create or check out a topic branch in .docs/ that matches the parent repo branch name.
Author the content update in .docs/ using the docs repository's own documentation guidance and conventions.
Run relevant documentation checks if the docs repository provides them.
File a tenzir/docs pull request from .docs/.
Cross-link the pull requests using one shared compact footer pattern:
In the docs PR, append a final <sub>...</sub> footer block that links the code PR and references the same Linear issue(s), for example ⚙️ Code PR: tenzir/tenzir#6048<br>🎫 References TNZ-150, TNZ-151.
In the code PR, append or extend the final <sub>...</sub> footer with 📚 Docs PR: tenzir/docs#261.
Use GitHub shorthand for PR links in both directions, such as tenzir/tenzir#6048 or tenzir/docs#261, instead of full URLs. Use full URLs only for deep links that shorthand cannot express, such as a specific comment.
Prefer that footer over dedicated Code PR or Docs PR sections. If a footer already exists, add another <br>-separated line instead of creating a second footer.
Summarize what changed and note any follow-up work.
Branching

Keep the .docs/ branch name aligned with the code branch whenever possible. If the code change spans multiple repositories, use the code branch as the source of truth for naming and cross-links.

PR cross-link format

Keep docs/code cross-links in a compact footer at the end of each PR description. In the docs PR footer, reference the same Linear issue(s) with a non-closing word such as references so the companion docs PR does not move the issue independently. When multiple issues share the same relationship, enumerate them after one magic word on one line to keep the footer compact. Use separate lines only when the relationship differs.

Docs PR example:

<sub>
⚙️ Code PR: tenzir/tenzir#1234<br>
🎫 References TNZ-150, TNZ-151
</sub>


Code PR example:

<sub>
📚 Docs PR: tenzir/docs#261<br>
✅ Closes TNZ-150, TNZ-151<br>
📎 Related: tenzir/tenzir#5999
</sub>

Cross-Checks

Before opening the docs PR:

Confirm the changed pages still fit their Diataxis section.
Check nearby pages and "See also" links for follow-on edits.
Ensure code samples, paths, and UI labels match the current product behavior.
Weekly Installs
40
Repository
tenzir/skills
GitHub Stars
1
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass