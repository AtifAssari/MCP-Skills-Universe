---
title: humanize
url: https://skills.sh/humanizerai/agent-skills/humanize
---

# humanize

skills/humanizerai/agent-skills/humanize
humanize
Installation
$ npx skills add https://github.com/humanizerai/agent-skills --skill humanize
Summary

Transform AI-generated text into natural writing that bypasses AI detectors.

Three intensity levels (light, medium, aggressive) adjust how extensively the text is rewritten, with credit usage based on word count
Provides before/after AI detection scores to show improvement against detectors like GPTZero, Turnitin, and Originality.ai
Requires HumanizerAI API key and consumes 1 credit per word processed; detection scoring is free
SKILL.md
Humanize AI Text

Transform AI-generated content into natural, human-like writing using the HumanizerAI API.

How It Works

When the user invokes /humanize, you should:

Parse $ARGUMENTS for text and optional --intensity flag
Call the HumanizerAI API to humanize the text
Present the humanized text with before/after scores
Show remaining credits
Parsing Arguments

The user may provide:

Just text: /humanize [their text]
With intensity: /humanize --intensity aggressive [their text]

Default intensity is medium.

Intensity Levels
Value	Name	Description	Best For
light	Light	Subtle changes, preserves style	Already-edited text, low AI scores
medium	Medium	Balanced rewrites (default)	Most use cases
aggressive	Bypass	Maximum bypass mode	High AI scores, strict detectors
API Call

Make a POST request to https://humanizerai.com/api/v1/humanize:

Authorization: Bearer $HUMANIZERAI_API_KEY
Content-Type: application/json

{
  "text": "<user's text>",
  "intensity": "medium"
}

Response Format

Present results like this:

## Humanization Complete

**Score:** X → Y (improvement)
**Words Processed:** N
**Credits Remaining:** X

---
### Humanized Text

[The humanized text]

---

[Recommendation based on final score]

Credit Usage
1 word = 1 credit
Detection is free
Check credits at https://humanizerai.com/dashboard
Error Handling
Insufficient Credits

If the user doesn't have enough credits:

Show how many credits are needed vs available
Direct them to https://humanizerai.com/dashboard to top up
Invalid API Key
Check HUMANIZERAI_API_KEY environment variable
Direct to https://humanizerai.com to get a key
Rate Limit

If rate limited, suggest waiting or upgrading to Business plan.

Weekly Installs
1.1K
Repository
humanizerai/agent-skills
GitHub Stars
16
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn