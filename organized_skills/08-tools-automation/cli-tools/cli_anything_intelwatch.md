---
rating: ⭐⭐⭐
title: cli-anything-intelwatch
url: https://skills.sh/hkuds/cli-anything/cli-anything-intelwatch
---

# cli-anything-intelwatch

skills/hkuds/cli-anything/cli-anything-intelwatch
cli-anything-intelwatch
Installation
$ npx skills add https://github.com/hkuds/cli-anything --skill cli-anything-intelwatch
SKILL.md
cli-anything-intelwatch

Intelwatch bridges the gap between hacker OSINT and B2B Sales/M&A data. It executes complex financial data aggregation, technology stack detection, and AI-powered due diligence in seconds.

Installation

This CLI is installed as part of the cli-anything-intelwatch package:

pip install cli-anything-intelwatch


Prerequisites:

Node.js >=18 must be installed and accessible via npx
Run node -v and npx -v to ensure your system meets the requirements
Usage
Basic Commands
# Show help
cli-anything-intelwatch --help

# Generate a deep profile for a company
cli-anything-intelwatch profile kpmg.fr

# Generate a profile with AI Due Diligence
cli-anything-intelwatch profile kpmg.fr --ai

For AI Agents

When using this CLI programmatically:

Provide the domain name (e.g., doctolib.fr)
Use the --ai flag to let Intelwatch perform due diligence automatically
The output is human-readable and provides a deep breakdown of the company
Ensure npx is available on the machine
Example Scenarios
M&A Due Diligence: cli-anything-intelwatch profile company-name.com --ai
Sales Intelligence: cli-anything-intelwatch profile target-client.com
Weekly Installs
88
Repository
hkuds/cli-anything
GitHub Stars
33.2K
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SnykWarn