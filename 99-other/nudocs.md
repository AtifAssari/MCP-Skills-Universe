---
title: nudocs
url: https://skills.sh/jdrhyne/agent-skills/nudocs
---

# nudocs

skills/jdrhyne/agent-skills/nudocs
nudocs
Installation
$ npx skills add https://github.com/jdrhyne/agent-skills --skill nudocs
SKILL.md
Nudocs

Upload documents to Nudocs.ai for rich editing, get shareable links, and pull back the results.

Setup

Install the CLI using the repo's declared install metadata or your preferred package manager before first use.

Get your API key from https://nudocs.ai (click "Integration" after signing in)

Configure the key:

# Option 1: Environment variable
export NUDOCS_API_KEY="nudocs_your_key_here"

# Option 2: Config file
mkdir -p ~/.config/nudocs
echo "nudocs_your_key_here" > ~/.config/nudocs/api_key

Commands
nudocs upload <file>              # Upload and get edit link
nudocs list                       # List all documents
nudocs link [ulid]                # Get edit link (last upload if no ULID)
nudocs pull [ulid] [--format fmt] # Download document (default: docx)
nudocs delete <ulid>              # Delete a document
nudocs config                     # Show configuration

Workflow
Upload Flow
Create/write document content
Save as markdown (or other supported format)
Run: nudocs upload <file>
Share the returned edit link with user
Pull Flow
User requests document back
Run: nudocs pull [ulid] --format <fmt>
Read and present the downloaded file
Format Selection
Scenario	Recommended Format
User edited with rich formatting	docx (default)
Simple text/code content	md
Final delivery/sharing	pdf

See formats.md in this skill's references folder for full format support.

Natural Language Triggers

Recognize these user intents:

Upload/Send:

"send to nudocs"
"upload to nudocs"
"open in nudocs"
"edit this in nudocs"
"let me edit this in nudocs"
"put this in nudocs"

Pull/Fetch:

"pull it back"
"pull from nudocs"
"get that doc"
"fetch from nudocs"
"download from nudocs"
"grab the updated version"
"what did I change"
"get my edits"

Link:

"get the nudocs link"
"share link"
"where's that doc"
"nudocs url"

List:

"show my nudocs"
"list my documents"
"what docs do I have"
"my nudocs documents"
Document Best Practices

Before uploading, ensure good structure:

Clear heading hierarchy (H1 → H2 → H3)
Consistent spacing
Appropriate list formatting
Concise paragraphs (3-5 sentences)

See document-design.md in this skill's references folder for templates and guidelines.

Example Session
User: Write me a blog post about remote work and send it to Nudocs

Agent:
1. Writes blog-remote-work.md with proper structure
2. Runs: nudocs upload blog-remote-work.md
3. Returns: "Here's your Nudocs link: https://nudocs.ai/file/01ABC..."

User: *edits in Nudocs, adds formatting, images*
User: Pull that back

Agent:
1. Runs: nudocs pull --format docx
2. Reads the downloaded file
3. Returns: "Got your updated document! Here's what changed..."

Error Handling
Error	Cause	Solution
"No API key found"	Missing credentials	Set NUDOCS_API_KEY or create config file
"DOCUMENT_LIMIT_REACHED"	Free tier limit (10 docs)	Delete old docs or upgrade to Pro
"Unauthorized"	Invalid API key	Regenerate key in Nudocs settings
"No ULID provided"	Missing document ID	Specify ULID or upload a doc first
Links
CLI: https://github.com/PSPDFKit/nudocs-cli (@nutrient-sdk/nudocs-cli on npm)
MCP integration repo: https://github.com/PSPDFKit/nudocs-mcp-server
Nudocs: https://nudocs.ai
Safety Boundaries
Do not upload sensitive documents unless the user confirmed that third-party processing is acceptable.
Do not print API keys, edit links meant to stay private, or document contents the user did not ask to expose.
Do not delete documents from Nudocs without explicit confirmation.
Do not assume the default download format is correct; confirm the output format when it matters.
Weekly Installs
21
Repository
jdrhyne/agent-skills
GitHub Stars
232
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn