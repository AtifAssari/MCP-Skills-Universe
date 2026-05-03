---
title: qt-translation-assistant
url: https://skills.sh/re2zero/deepin-skills/qt-translation-assistant
---

# qt-translation-assistant

skills/re2zero/deepin-skills/qt-translation-assistant
qt-translation-assistant
Installation
$ npx skills add https://github.com/re2zero/deepin-skills --skill qt-translation-assistant
SKILL.md
Qt Translation Assistant Skill
Iron Laws
Never modify original TS files without backup - Always preserve original content
Validate AI translation quality - Verify translations are accurate and contextually appropriate
Maintain translation consistency - Use consistent terminology across all translations
Respect file encoding - Preserve UTF-8 encoding and special characters
Minimal changes principle - Only modify translation content, preserve XML structure
Red Flags
User requests translation of non-TS files
User asks to translate without proper AI configuration
Requests to overwrite existing translations without verification
Asks to translate to unsupported language codes
Rationalization Table
Excuse	Response
"Just translate everything quickly"	Quality matters in localization - proper AI configuration and validation required
"We don't need consistent terminology"	Inconsistent translations hurt user experience - consistency is critical
"Original files don't need backup"	Always preserve originals - translation errors can corrupt content
"Rewrite the whole file"	Only translation text should change - git diff will show other modifications
Quick Reference
Core Commands
# Translate entire directory of TS files
python translate.py /path/to/ts/files/

# Translate specific file
python translate.py /path/to/file.ts

# With custom batch size and workers
python translate.py /path/to/ts/files/ --batch-size 30 --max-workers 3

# Create configuration file
python translate.py --create-config

Configuration
{
  "api_url": "http://localhost:8080/v1/chat/completions",
  "api_key": "sk-uos-12345",
  "model": "qwen3-coder-flash",
  "temperature": 0.3
}

Common Mistakes & Fixes
Mistake: AI provider not configured properly

Fix: Create qt_translation_config.json with valid API credentials using --create-config

Mistake: Large files causing API timeouts

Fix: Adjust --batch-size parameter (try 20-50) and --max-workers (try 2-5)

Mistake: Language codes not detected correctly

Fix: Ensure TS files follow standard naming convention (e.g., project_zh_CN.ts, project_de.ts)

Mistake: Translation quality issues

Fix: Adjust model selection and temperature settings in configuration file

Mistake: Git diff shows many unnecessary changes

Fix: The tool only modifies translation content - any other changes indicate a bug that needs fixing

Architecture

This skill uses a parallel processing architecture:

TranslationWorker: Handles AI API calls with automatic retry and exponential backoff
QtTranslationAssistant: Main orchestrator with parallel batch processing
ThreadPoolExecutor: Manages concurrent translation workers (default 3)

Performance improvements over subagent architecture:

Direct API calls without subprocess overhead (~5-10x faster)
Larger batch sizes (default 30 vs previous 10)
Parallel workers (3 concurrent API calls vs sequential)
Error isolation (single batch failure doesn't affect others)
Key Features
Smart parsing of TS files to identify incomplete translations
Parallel batch processing with ThreadPoolExecutor
Support for multiple AI providers (OpenAI, Anthropic, DeepSeek, local servers)
Configurable batch size and worker count
Automatic retries with exponential backoff
Git diff-friendly modifications (only changes translation content)
Weekly Installs
36
Repository
re2zero/deepin-skills
GitHub Stars
6
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail