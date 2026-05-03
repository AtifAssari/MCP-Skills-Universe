---
rating: ⭐⭐
title: add-function-examples
url: https://skills.sh/vercel/ai/add-function-examples
---

# add-function-examples

skills/vercel/ai/add-function-examples
add-function-examples
Installation
$ npx skills add https://github.com/vercel/ai --skill add-function-examples
SKILL.md
Adding Function Examples

Review the changes in the current branch, and identify new or modified features or bug fixes that would benefit from having an example in the examples/ai-functions directory. These examples are used for testing specific features against the actual provider APIs, and can also serve as documentation for users.

Determine for which kind of model and top-level function the example should be added. For a language model, the example should be added in two variants, one for generateText and one for streamText. For any other models kinds, add the example for the relevant top-level function (e.g. generateImage, generateSpeech).

After creating the example, run pnpm type-check:full; fix any errors encountered.

Weekly Installs
43
Repository
vercel/ai
GitHub Stars
24.0K
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass