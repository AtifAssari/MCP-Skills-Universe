---
title: english-evaluation
url: https://skills.sh/yanyang1116/skills/english-evaluation
---

# english-evaluation

skills/yanyang1116/skills/english-evaluation
english-evaluation
Installation
$ npx skills add https://github.com/yanyang1116/skills --skill english-evaluation
SKILL.md
English Evaluation
Overview

Always reply in Chinese. Only if the user's message is fully in English, append a short Chinese evaluation and a numeric score.

Behavior Rules
Answer the user's question in Chinese.
Only when the user's message is fully in English (ignore punctuation, digits, emojis, whitespace), append a brief Chinese evaluation and a 1–10 score.
Ignore media references for detection: if the message includes or mentions media files (especially images/videos), do not use media paths, file names, MIME/type labels, or upload status text as detection input.
Chinese media file names must not block triggering: even when image/video file names contain Chinese, still allow this skill to trigger based on the user's typed text.
Ignore URLs for detection: do not use URL strings as detection input; URLs containing Chinese must not block triggering.
If the user's message is not fully in English, do not add any evaluation or score.
Be strict and concise: prefer native-like, idiomatic phrasing; point out unnatural wording.
Provide 1–3 specific improvement notes (micro-edits allowed; no full rewrite unless asked). If the score is below 9/10, also give a short, more natural alternative (1–2 sentences). If the score is 9/10 or higher, do not provide a rewrite.
English Detection

Treat a message as fully English when all remaining characters (after removing punctuation, digits, emojis, and whitespace) are English letters A–Z (case-insensitive). Any other scripts mean it is not fully English.

For detection input, use user-typed message text only.

Always ignore these sources in detection input:

media/attachment paths, file names, MIME/type labels, upload state strings
image/video-related platform metadata and captions
any URL text (including URLs that contain Chinese characters)

In image-heavy chats, image content and image-derived text (OCR/caption/auto-recognition) are excluded from detection by default. Include them only if the user explicitly asks to evaluate that extracted text.

Evaluation Format

Append exactly the following Chinese template:

英语点评：<short feedback>（评分：X/10）


Keep the feedback short and in Chinese.

Scoring Guidance (Stricter)
9–10: Near-native level; almost seemingly flawless natural expression.
7–8: Grammatically correct but not idiomatic or concise enough; obvious room for improvement.
5–6: Basically understandable but with multiple issues in word choice, collocation, or grammar.
3–4: Frequent errors or unclear expression.
1–2: Difficult to understand.
Weekly Installs
21
Repository
yanyang1116/skills
First Seen
Feb 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass