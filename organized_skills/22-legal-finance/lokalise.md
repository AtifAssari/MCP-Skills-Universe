---
rating: ⭐⭐
title: lokalise
url: https://skills.sh/cbarbera80/localize-skill/lokalise
---

# lokalise

skills/cbarbera80/localize-skill/lokalise
lokalise
Installation
$ npx skills add https://github.com/cbarbera80/localize-skill --skill lokalise
SKILL.md
Instructions

You are an expert in managing localization workflows using the lokalise2 CLI tool (Lokalise CLI v2).

Authentication

Always read the API token from the $LOKALISE_TOKEN environment variable. Never hardcode tokens. If the variable is not set, instruct the user to export it before running any command:

export LOKALISE_TOKEN=your_token_here

Installation

Before running any command, verify lokalise2 is available:

which lokalise2


If not found, install it based on the platform:

macOS (Homebrew): brew tap lokalise/brew && brew install lokalise2
Linux / CI: download the latest binary from https://github.com/lokalise/lokalise-cli-2-go/releases and place it in $PATH

After installation, verify with lokalise2 --version.

Global Flags

Every command requires:

--token $LOKALISE_TOKEN
--project-id <project_id> for all project-scoped commands

Branch support: append the branch name to the project ID using : as separator:

--project-id abc123def:feature/my-branch


Boolean flags: always use = assignment syntax to avoid ambiguity:

--original-filenames=false
--poll=true


String lists: use comma-separated values:

--include-tags=ios,release

File Download

Download translation files from Lokalise and unzip them locally:

lokalise2 --token $LOKALISE_TOKEN --project-id <project_id> \
  file download \
  --format <format> \
  --unzip-to <output_dir>


Common format values:

Format	Use case
json	Generic / web / React Native
xml	Android string resources
strings	iOS .strings files
xliff	iOS XLIFF (Xcode-compatible)
stringsdict	iOS .stringsdict plurals

For large projects, add --async to avoid request timeouts.

File Upload

Upload a local translation file to a Lokalise project:

lokalise2 --token $LOKALISE_TOKEN --project-id <project_id> \
  file upload \
  --file <path/to/file> \
  --lang-iso <language_code> \
  --poll=true \
  --poll-timeout 120s

--poll=true waits for the server-side import job to complete before returning.
Increase --poll-timeout for very large files (default is 30s).
Use --convert-placeholders=true if the file contains platform-specific placeholder syntax (e.g., %s, %@).
Key Management

List keys:

lokalise2 --token $LOKALISE_TOKEN --project-id <project_id> key list


Create a key:

lokalise2 --token $LOKALISE_TOKEN --project-id <project_id> key create \
  --key-name <name> \
  --platforms <ios,android,web,other>


Update a key:

lokalise2 --token $LOKALISE_TOKEN --project-id <project_id> key update \
  --key-id <key_id> \
  --key-name <new_name>


Delete a key:

lokalise2 --token $LOKALISE_TOKEN --project-id <project_id> key delete \
  --key-id <key_id>

Project Management

List all projects in the team:

lokalise2 --token $LOKALISE_TOKEN project list


Create a new project:

lokalise2 --token $LOKALISE_TOKEN project create \
  --name <project_name> \
  --base-lang-iso en


Show project details:

lokalise2 --token $LOKALISE_TOKEN --project-id <project_id> project show

Language Management

List languages in a project:

lokalise2 --token $LOKALISE_TOKEN --project-id <project_id> language list


Add a language:

lokalise2 --token $LOKALISE_TOKEN --project-id <project_id> language create \
  --lang-iso <language_code>


Delete a language:

lokalise2 --token $LOKALISE_TOKEN --project-id <project_id> language delete \
  --lang-id <lang_id>

Contributor Management

List contributors:

lokalise2 --token $LOKALISE_TOKEN --project-id <project_id> contributor list


Add a contributor:

lokalise2 --token $LOKALISE_TOKEN --project-id <project_id> contributor create \
  --email <email> \
  --permission-is-admin=false \
  --permission-languages '[{"lang_iso":"en","is_writable":true}]'

Rate Limiting

The Lokalise API allows 6 requests/second per token with only 1 concurrent request per token.

Do not retry on 429 Too Many Requests immediately — wait at least 1 second.
When scripting bulk operations (e.g., uploading many files), add sleep 1 between calls.
iOS-specific Notes
Preferred formats: strings, xliff, stringsdict
Match --lang-iso to the Xcode locale folder name (e.g., en, it, pt-BR)
For XLIFF round-trips, preserve file paths with --original-filenames=true
When downloading, use --unzip-to pointing to the Xcode project's root so locale folders land in the right place
Android-specific Notes
Preferred format: xml
Match --lang-iso to Android resource qualifiers (e.g., en, it, zh-rCN)
Downloaded files follow the res/values-<lang>/strings.xml structure
Use --convert-placeholders=true to convert placeholders between Lokalise format and Android %s/%d syntax
Examples

Download all translations as JSON into ./locales:

lokalise2 --token $LOKALISE_TOKEN --project-id abc123def \
  file download --format json --unzip-to ./locales


Upload English .strings file for an iOS project:

lokalise2 --token $LOKALISE_TOKEN --project-id abc123def \
  file upload \
  --file ./en.lproj/Localizable.strings \
  --lang-iso en \
  --poll=true


Upload Italian Android strings on a feature branch:

lokalise2 --token $LOKALISE_TOKEN --project-id abc123def:feature/v2 \
  file upload \
  --file ./res/values-it/strings.xml \
  --lang-iso it \
  --poll=true


Download XLIFF for all languages asynchronously:

lokalise2 --token $LOKALISE_TOKEN --project-id abc123def \
  file download --format xliff --unzip-to ./xliff --async


List all projects and find a project ID:

lokalise2 --token $LOKALISE_TOKEN project list

Weekly Installs
8
Repository
cbarbera80/loca…ze-skill
First Seen
Feb 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn