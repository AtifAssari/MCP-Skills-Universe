---
rating: ⭐⭐
title: apple-intelligence
url: https://skills.sh/rshankras/claude-code-apple-skills/apple-intelligence
---

# apple-intelligence

skills/rshankras/claude-code-apple-skills/apple-intelligence
apple-intelligence
Installation
$ npx skills add https://github.com/rshankras/claude-code-apple-skills --skill apple-intelligence
SKILL.md
Apple Intelligence Skills

Skills for implementing Apple Intelligence features including on-device LLMs, visual recognition, App Intents integration, and intelligent assistants.

When This Skill Activates

Use this skill when the user:

Wants to add AI/LLM features to their app
Needs on-device text generation or understanding
Asks about Foundation Models or Apple Intelligence
Wants to implement structured AI output
Needs prompt engineering guidance
Wants camera-based visual intelligence features
Needs Siri, Shortcuts, or Spotlight integration via App Intents
Wants to expose app actions or content to the system
Available Skills
foundation-models/

On-device LLM integration with prompt engineering best practices.

Model availability checking
Session management
@Generable structured output
Tool calling patterns
Snapshot streaming
Prompt engineering techniques
visual-intelligence/

Integrate with iOS Visual Intelligence for camera-based search.

IntentValueQuery implementation
SemanticContentDescriptor handling
AppEntity for searchable content
Display representations
Deep linking from results
app-intents/

App Intents for Siri, Shortcuts, Spotlight, and Apple Intelligence.

AppIntent protocol, parameters, perform()
AppEntity and entity queries
App Shortcuts with voice phrases
IndexedEntity and Spotlight indexing
Intent modes (background, foreground)
Interactive snippets with SnippetIntent
Visual intelligence integration
Onscreen entities for Siri/ChatGPT
Multiple choice API
Swift package support
Key Principles
1. Privacy First
All processing happens on-device
No cloud connectivity required
User data never leaves the device
2. Graceful Degradation
Always check model availability
Provide fallback UI for unsupported devices
Handle errors gracefully
3. Efficient Prompting
Keep prompts focused and specific
Use structured output when possible
Respect context window limits (4,096 tokens)
Reference Documentation
/Users/ravishankar/Downloads/docs/FoundationModels-Using-on-device-LLM-in-your-app.md
/Users/ravishankar/Downloads/docs/Implementing-Visual-Intelligence-in-iOS.md
/Users/ravishankar/Downloads/docs/AppIntents-Updates.md
Weekly Installs
156
Repository
rshankras/claud…e-skills
GitHub Stars
312
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass