---
rating: ⭐⭐
title: generate-swagger-docs
url: https://skills.sh/qodex-ai/ai-agent-skills/generate-swagger-docs
---

# generate-swagger-docs

skills/qodex-ai/ai-agent-skills/generate-swagger-docs
generate-swagger-docs
Installation
$ npx skills add https://github.com/qodex-ai/ai-agent-skills --skill generate-swagger-docs
SKILL.md
Generate Swagger Documentation

Generate OpenAPI docs from your codebase in seconds with automatic API key setup.

How It Works

This skill automates the Swagger/OpenAPI documentation generation:

API Key Setup - Accepts your OpenAI API key and sets it as an environment variable
Initialization - Downloads and sets up the apimesh tool
Automatic Processing - The tool analyzes your codebase and generates documentation
Output - Outputs are saved to the apimesh/ directory
Setup Requirements

You need an OpenAI API key to use this skill. Get one from OpenAI's platform if you don't have one already.

Recommended: Quick Setup with API Key

The easiest way to use this skill is to pass your API key directly:

/Users/ankits/.claude/skills/generate-swagger-docs/generate-with-key.sh "sk-proj-your-api-key-here"


This will:

Accept your OpenAI API key as an argument
Create the apimesh/ directory and download the apimesh tool
Set up the environment variables correctly
Generate your Swagger documentation automatically
Display the output file locations
Automatic Flow

When you run this skill:

First Time: You'll be prompted for your OpenAI API key (starts with sk-proj-)

The key is saved locally and used for subsequent runs
The key is NOT committed to version control

Subsequent Runs: The skill uses the saved API key automatically

No additional prompts for the key unless you clear the config

Framework Detection: Automatically detects your API framework

Supports: Express, NestJS, FastAPI, Django, Rails, Go, and more
What It Does
Scans your repository for API endpoints
Detects the web framework (Django, Flask, FastAPI, Express, NestJS, Rails, Go)
Generates OpenAPI 3.0 specification (swagger.json)
Creates interactive HTML documentation (apimesh-docs.html)
Output
apimesh/swagger.json - OpenAPI 3.0 spec
apimesh/apimesh-docs.html - Interactive Swagger UI (self-contained, shareable)
apimesh/config.json - Saved configuration (includes your settings, gitignore this file)
Important Notes
Your OpenAI API key is needed for the LLM analysis
The generated config.json should be added to .gitignore as it contains secrets
Framework detection is automatic but can be manually specified if needed
The tool supports both public and private repositories
API Key Setup Methods
Method 1: Wrapper Script (Recommended) ✓

Use the provided wrapper script that properly handles environment variable propagation:

/Users/ankits/.claude/skills/generate-swagger-docs/generate-with-key.sh "sk-proj-your-api-key-here"


Why this works best:

Properly passes the API key to the Python subprocess
No interactive prompts in non-TTY environments
Handles environment variable propagation correctly
Provides clear success/error messages
Method 2: Using Saved Configuration

After the first run with Method 1, your key is saved in apimesh/config.json. On subsequent runs, you can omit the key (if you trust your local setup):

/Users/ankits/.claude/skills/generate-swagger-docs/generate-with-key.sh


Important: Never commit the config.json file to version control. Add it to .gitignore.

Method 3: Manual apimesh Setup

If you need more control, download and run apimesh directly:

export OPENAI_API_KEY="sk-proj-your-api-key-here"
mkdir -p apimesh && \
  curl -sSL https://raw.githubusercontent.com/qodex-ai/apimesh/refs/heads/main/run.sh -o apimesh/run.sh && \
  chmod +x apimesh/run.sh && \
  cd apimesh && \
  OPENAI_API_KEY="$OPENAI_API_KEY" ./run.sh


Note: The OPENAI_API_KEY must be explicitly passed to the subprocess as shown above.

Weekly Installs
139
Repository
qodex-ai/ai-agent-skills
GitHub Stars
6
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubFail
SocketFail
SnykFail