---
title: gdelt-gkg-fetch
url: https://skills.sh/tiangong-ai/skills/gdelt-gkg-fetch
---

# gdelt-gkg-fetch

skills/tiangong-ai/skills/gdelt-gkg-fetch
gdelt-gkg-fetch
Installation
$ npx skills add https://github.com/tiangong-ai/skills --skill gdelt-gkg-fetch
SKILL.md
GDELT GKG Fetch
Core Goal
Fetch GDELT 2.0 GKG table exports (*.gkg.csv.zip) from official public endpoints.
Resolve latest available snapshot via lastupdate.txt.
Resolve historical snapshots in a UTC range via masterfilelist.txt.
Persist downloaded files and return machine-readable JSON manifest.
Keep runtime observable with structured logs and optional log file.
Required Environment
Configure runtime by environment variables (see references/env.md).
Start from assets/config.example.env.
Load env values before running commands:
set -a
source assets/config.example.env
set +a

Workflow
Validate effective configuration.
python3 scripts/gdelt_gkg_fetch.py check-config --pretty

Inspect the latest available GKG snapshot.
python3 scripts/gdelt_gkg_fetch.py resolve-latest --pretty

Dry-run a historical range selection before downloading.
python3 scripts/gdelt_gkg_fetch.py fetch \
  --mode range \
  --start-datetime 20260301000000 \
  --end-datetime 20260301120000 \
  --max-files 3 \
  --dry-run \
  --pretty

Fetch files with transport and structure validation.
python3 scripts/gdelt_gkg_fetch.py fetch \
  --mode latest \
  --max-files 1 \
  --output-dir ./data/gdelt-gkg \
  --preview-lines 2 \
  --validate-structure \
  --expected-columns 27 \
  --quarantine-dir ./data/gdelt-gkg-quarantine \
  --log-level INFO \
  --log-file ./logs/gdelt-gkg-fetch.log \
  --pretty

Built-in Robustness
Apply retry with exponential backoff on transient HTTP/network failures.
Respect Retry-After when present on retriable responses.
Throttle request frequency with a minimum interval between requests.
Enforce --max-files safety cap (GDELT_MAX_FILES_PER_RUN) to prevent accidental bulk pulls.
Validate datetime format and range boundaries before remote calls.
Validate transport and structure after download:
ZIP CRC/integrity check
UTF-8 strict decoding check
Tab column-count check (default 27)
Optional bad-line issue quarantine (--quarantine-dir)
Emit JSON results while writing operational logs to stderr and optional log file.
Scope Decision
Keep one concrete file-table fetch implementation: GKG (*.gkg.csv.zip).
Keep atomic operations only; do not add internal scheduler/polling loops.
References
references/gdelt-data-sources.md
references/gdelt-limitations.md
references/gdelt-schema.md
references/env.md
references/openclaw-chaining-templates.md
Script
scripts/gdelt_gkg_fetch.py
OpenClaw Invocation Compatibility
Keep skill trigger metadata in name, description, and agents/openai.yaml.
Invoke in prompts with $gdelt-gkg-fetch.
Keep the skill atomic: only resolve/fetch on demand.
Use script parameters for fetch conditions (--mode range --start-datetime --end-datetime).
If you need polling, let OpenClaw orchestrate repeated invocations externally, not inside this skill.
OpenClaw Prompt Templates

Use these templates directly in OpenClaw and only replace bracketed placeholders.

Recon (latest availability)
Use $gdelt-gkg-fetch.
Run:
python3 scripts/gdelt_gkg_fetch.py resolve-latest --pretty
Return only the JSON result.

Fetch (historical window, dry-run first)
Use $gdelt-gkg-fetch.
Run:
python3 scripts/gdelt_gkg_fetch.py fetch \
  --mode range \
  --start-datetime [YYYYMMDDHHMMSS] \
  --end-datetime [YYYYMMDDHHMMSS] \
  --max-files [N] \
  --dry-run \
  --pretty

Then run without --dry-run using:
  --output-dir [OUTPUT_DIR]
  --validate-structure
  --expected-columns 27
  --quarantine-dir [QUARANTINE_DIR]
Return only the JSON result.

Validate (download quality gate)
Use $gdelt-gkg-fetch.
Run:
python3 scripts/gdelt_gkg_fetch.py fetch \
  --mode latest \
  --max-files 1 \
  --output-dir [OUTPUT_DIR] \
  --validate-structure \
  --expected-columns 27 \
  --quarantine-dir [QUARANTINE_DIR] \
  --pretty
Check validation.issue_count, decode_error_count, column_mismatch_count.
Return JSON plus one-line pass/fail verdict.

Weekly Installs
8
Repository
tiangong-ai/skills
GitHub Stars
6
First Seen
Mar 15, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn