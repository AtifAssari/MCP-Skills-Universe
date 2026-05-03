---
rating: ⭐⭐
title: generating-swift-package-docs
url: https://skills.sh/johnrogers/claude-swift-engineering/generating-swift-package-docs
---

# generating-swift-package-docs

skills/johnrogers/claude-swift-engineering/generating-swift-package-docs
generating-swift-package-docs
Installation
$ npx skills add https://github.com/johnrogers/claude-swift-engineering --skill generating-swift-package-docs
SKILL.md
Swift Package Documentation Generator

Generates API documentation for Swift package dependencies on-demand, extracting symbol information from Xcode's DerivedData to answer "what does this library do?"

Overview

When exploring unfamiliar dependencies, generate their documentation automatically instead of guessing from code. This tool uses interfazzle to extract symbol information from compiled modules.

How to Use

When asked about an unfamiliar Swift module import:

Run: ./scripts/generate_docs.py "<module_name>" "<path_to.xcodeproj>"
Script outputs path to cached documentation file
Read the file and provide relevant information

Prerequisites: Project must be built once (DerivedData exists), interfazzle CLI installed.

See reference.md for error handling and details.

Weekly Installs
90
Repository
johnrogers/clau…ineering
GitHub Stars
201
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn