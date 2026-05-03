---
rating: ⭐⭐⭐
title: grepai-init
url: https://skills.sh/yoanbernabeu/grepai-skills/grepai-init
---

# grepai-init

skills/yoanbernabeu/grepai-skills/grepai-init
grepai-init
Installation
$ npx skills add https://github.com/yoanbernabeu/grepai-skills --skill grepai-init
SKILL.md
GrepAI Init

This skill covers the grepai init command and project initialization.

When to Use This Skill
Setting up GrepAI in a new project
Understanding what grepai init creates
Customizing initial configuration
Troubleshooting initialization issues
Basic Usage
cd /path/to/your/project
grepai init

What Init Creates

Running grepai init creates the .grepai/ directory with:

.grepai/
├── config.yaml    # Configuration file
├── index.gob      # Vector index (created by watch)
└── symbols.gob    # Symbol index for trace (created by watch)

Default Configuration

The generated config.yaml:

version: 1

embedder:
  provider: ollama
  model: nomic-embed-text
  endpoint: http://localhost:11434

store:
  backend: gob

chunking:
  size: 512
  overlap: 50

watch:
  debounce_ms: 500

trace:
  mode: fast
  enabled_languages:
    - .go
    - .js
    - .ts
    - .jsx
    - .tsx
    - .py
    - .php
    - .c
    - .h
    - .cpp
    - .hpp
    - .cc
    - .cxx
    - .rs
    - .zig
    - .cs
    - .pas
    - .dpr

ignore:
  - .git
  - .grepai
  - node_modules
  - vendor
  - target
  - __pycache__
  - dist
  - build

Understanding Default Settings
Embedder Settings
Setting	Default	Purpose
provider	ollama	Local embedding generation
model	nomic-embed-text	768-dimension model
endpoint	http://localhost:11434	Ollama API URL
Store Settings
Setting	Default	Purpose
backend	gob	Local file storage
Chunking Settings
Setting	Default	Purpose
size	512	Tokens per chunk
overlap	50	Overlap for context
Watch Settings
Setting	Default	Purpose
debounce_ms	500	Wait time before re-indexing
Ignore Patterns

Default patterns exclude:

Version control: .git
GrepAI data: .grepai
Dependencies: node_modules, vendor
Build outputs: target, dist, build
Cache: __pycache__
Customizing After Init

Edit .grepai/config.yaml to customize:

Change Embedding Provider
embedder:
  provider: openai
  model: text-embedding-3-small
  api_key: ${OPENAI_API_KEY}

Change Storage Backend
store:
  backend: postgres
  postgres:
    dsn: postgres://user:pass@localhost:5432/grepai

Add Custom Ignore Patterns
ignore:
  - .git
  - .grepai
  - node_modules
  - "*.min.js"
  - "*.bundle.js"
  - coverage/
  - .nyc_output/

Init in Monorepos

For monorepos, init at the root:

cd /path/to/monorepo
grepai init


Or use workspaces for separate indices:

grepai workspace create my-workspace
grepai workspace add my-workspace /path/to/project1
grepai workspace add my-workspace /path/to/project2

Re-Initialization

If you need to reset:

# Remove existing config
rm -rf .grepai

# Re-initialize
grepai init


Warning: This deletes your index. You'll need to re-run grepai watch.

Verifying Initialization

After init, verify with:

# Check config exists
cat .grepai/config.yaml

# Check status (will show no index yet)
grepai status

Common Issues

❌ Problem: .grepai already exists ✅ Solution: Delete it first or edit existing config:

rm -rf .grepai && grepai init


❌ Problem: Config created but Ollama not running ✅ Solution: Start Ollama before running grepai watch:

ollama serve


❌ Problem: Wrong directory initialized ✅ Solution: Remove .grepai and init in correct directory

Best Practices
Init at project root: Where your main code lives
Add .grepai/ to .gitignore: Index is machine-specific
Customize ignore patterns: Exclude generated/vendored code
Review config after init: Adjust for your stack
Example .gitignore Addition
# GrepAI
.grepai/

Output Format

After successful initialization:

✅ GrepAI Initialized

   Config: .grepai/config.yaml

   Default settings:
   - Embedder: Ollama (nomic-embed-text)
   - Storage: GOB (local file)
   - Chunking: 512 tokens, 50 overlap

   Next steps:
   1. Ensure Ollama is running: ollama serve
   2. Start indexing: grepai watch

Weekly Installs
422
Repository
yoanbernabeu/gr…i-skills
GitHub Stars
16
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass