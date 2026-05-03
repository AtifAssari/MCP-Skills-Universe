---
title: tuzi-copy-polish
url: https://skills.sh/tuziapi/tuzi-skills/tuzi-copy-polish
---

# tuzi-copy-polish

skills/tuziapi/tuzi-skills/tuzi-copy-polish
tuzi-copy-polish
Installation
$ npx skills add https://github.com/tuziapi/tuzi-skills --skill tuzi-copy-polish
SKILL.md
Social Copy Polish

Optimizes social media copy for different platforms. Adjusts tone, length, hashtags, and formatting based on platform best practices.

Step 0: Load Preferences ⛔ BLOCKING
0.1 Check EXTEND.md
test -f .tuzi-skills/tuzi-copy-polish/EXTEND.md && echo "project"
test -f "$HOME/.tuzi-skills/tuzi-copy-polish/EXTEND.md" && echo "user"

Result	Action
Found	Load, parse, apply settings
Not found	Continue with defaults (ask platform in Step 2)
Path	Location
.tuzi-skills/tuzi-copy-polish/EXTEND.md	Project directory
$HOME/.tuzi-skills/tuzi-copy-polish/EXTEND.md	User home

EXTEND.md Supports: Default platform | Default language | Custom brand voice

Schema: references/config/preferences-schema.md

Step 1: Analyze Input

Determine input source:

File path: Read file content as draft copy. Record the file path for Step 3 output.
Inline text: Use the text directly as draft copy.

Identify:

Content type (product promotion, knowledge sharing, personal story, news, opinion)
Current language and tone
Key message and selling points
Target audience (if mentioned)
Step 2: Confirm Platform

If platform not specified by user or EXTEND.md, use AskUserQuestion:

header: "Target Platform"
question: "优化目标平台？"
options:
  - label: "小红书"
    description: "种草风、emoji、标签、口语化"
  - label: "X/Twitter"
    description: "简洁有力、英文友好、话题标签"
  - label: "抖音"
    description: "口语化、悬念开头、引导互动"
  - label: "微信公众号"
    description: "深度内容、段落清晰、引导关注"
  - label: "通用"
    description: "不针对特定平台，仅优化表达"

Step 3: Polish Copy

Load platform rules from references/platforms/, then rewrite:

Optimization Dimensions
Dimension	Description
Hook	Opening line that grabs attention
Tone	Match platform culture (e.g., 小红书 casual, 公众号 professional)
Length	Trim or expand to platform sweet spot
Structure	Platform-specific formatting (line breaks, paragraphs, lists)
Hashtags	Add relevant tags per platform convention
CTA	Call-to-action matching platform interaction patterns
Emoji	Platform-appropriate emoji usage
Output Format

If input is a file path: Append the polished copy to the end of the original file, separated by a clear divider:

---

## Polished Copy ({platform})

{polished content}


Then inform the user: "已将优化后的文案追加到文件末尾: {file_path}"

If input is inline text: Present the polished copy in a code block for easy copying.

In both cases, include a brief changelog (what was changed and why, 2-3 bullet points).

Multiple Variants

When the user asks for options, generate 2-3 variants with different angles:

Variant A: Focus on emotion/story
Variant B: Focus on value/benefit
Variant C: Focus on curiosity/hook
Step 4: Iterate

After presenting the polished copy, ask if the user wants to:

Adjust tone (more casual / more professional)
Try a different angle
Optimize for another platform
Fine-tune specific parts
Extension Support

Custom configurations via EXTEND.md. See Step 0 for paths and supported options.

Weekly Installs
110
Repository
tuziapi/tuzi-skills
GitHub Stars
33
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass