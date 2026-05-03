---
rating: ⭐⭐
title: deepline-feedback
url: https://skills.sh/site/code.deepline.com/deepline-feedback
---

# deepline-feedback

skills/code.deepline.com/deepline-feedback
deepline-feedback
$ npx skills add https://code.deepline.com
SKILL.md
Deepline Feedback

Send feedback or a bug report to the Deepline team.

Steps

Get feedback text. Use the argument if provided (e.g. /deepline-feedback the waterfall broke). Otherwise ask the user.

Confirm. Use AskUserQuestion with a question like:

This report will include:

Your feedback: {feedback text}
Environment info (auto-collected)
Current session transcript

Send this feedback?

Options: "Send it" / "Cancel".

If confirmed, run:

deepline provide-feedback --text "{feedback text}" --json
deepline session send --current-session --json


Tell the user it was sent. If cancelled, do nothing.

Weekly Installs
1.7K
Source
code.deepline.com
First Seen
1 day ago
Security Audits
SocketPass