---
title: interactive-input
url: https://skills.sh/sugarforever/01coder-agent-skills/interactive-input
---

# interactive-input

skills/sugarforever/01coder-agent-skills/interactive-input
interactive-input
Installation
$ npx skills add https://github.com/sugarforever/01coder-agent-skills --skill interactive-input
SKILL.md
Interactive Input Blocks

Embed interactive UI components (radio buttons, checkboxes, text fields, toggles) directly in chat responses. Compatible clients render these as native UI elements; other clients show a readable JSON code block as fallback.

When to Use
Quizzes and exercises (single/multiple choice, fill-in-the-blank)
Surveys and polls
Structured data collection (forms)
Any scenario where the user needs to select from options or provide structured input
How It Works

Wrap a JSON block in a ```interactive code fence within your normal markdown response. You can mix regular text and interactive blocks freely in the same message.

Schema Reference

See references/schema.md for the complete schema specification.

Quick Example

When presenting a multiple-choice question, instead of listing options as text:

Here's your first question:

```interactive
{
  "id": "q1",
  "card": {
    "body": [
      { "type": "TextBlock", "text": "What is the capital of France?", "weight": "bold" },
      { "type": "Input.ChoiceSet", "id": "answer", "style": "expanded",
        "choices": [
          { "title": "A. London", "value": "london" },
          { "title": "B. Paris", "value": "paris" },
          { "title": "C. Berlin", "value": "berlin" },
          { "title": "D. Madrid", "value": "madrid" }
        ]
      }
    ],
    "actions": [{ "type": "Action.Submit", "title": "Submit" }]
  }
}
```

Rules
Every interactive block MUST have a unique id field
Every interactive block MUST have at least one element in card.body
Include an Action.Submit in card.actions so the user can submit their response
Use "style": "expanded" for choice sets to show all options visually (recommended for quizzes)
Use "style": "compact" for dropdown selects when there are many options
Set "isMultiSelect": true on Input.ChoiceSet for multiple-choice questions
The first TextBlock in the body is used as the question label in the submitted response
You can include multiple interactive blocks in one message (e.g., a full quiz)
Always wrap the JSON in a ```interactive code fence — never use ```json for interactive blocks
Keep the JSON compact and valid — no comments, no trailing commas
Weekly Installs
104
Repository
sugarforever/01…t-skills
GitHub Stars
91
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass