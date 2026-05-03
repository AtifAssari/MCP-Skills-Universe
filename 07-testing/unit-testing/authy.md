---
rating: ⭐⭐
title: authy
url: https://skills.sh/eric8810/authy/authy
---

# authy

skills/eric8810/authy/authy
authy
Installation
$ npx skills add https://github.com/eric8810/authy --skill authy
SKILL.md
Authy — Secure Secret Injection

Inject secrets into subprocesses as environment variables. You never see, handle, or log secret values.

How It Works

Your token is run-only. You can discover secret names with authy list and inject them into subprocesses with authy run. You never see secret values directly.

Inject Secrets into a Command
authy run --scope <policy> --uppercase --replace-dash '_' -- <command> [args...]


The --uppercase --replace-dash '_' flags turn secret names like db-host into env vars like DB_HOST.

Examples:

authy run --scope deploy --uppercase --replace-dash '_' -- ./deploy.sh
authy run --scope backend --uppercase --replace-dash '_' -- node server.js
authy run --scope testing --uppercase --replace-dash '_' -- pytest

Discover Secret Names
authy list --scope <policy> --json


Output: {"secrets":[{"name":"db-host","version":1,...}]}

Resolve Placeholders in Files

Replace <authy:key-name> placeholders in config files with secret values:

authy resolve config.yaml.tpl --scope <policy> --output config.yaml


Placeholders use the format <authy:key-name>. Example template:

database:
  host: <authy:db-host>
  port: <authy:db-port>

Write Scripts That Use Secrets

Write code that reads environment variables, then run it with authy run:

cat > task.sh << 'EOF'
#!/bin/bash
curl -H "Authorization: Bearer $API_KEY" https://api.example.com/data
EOF
chmod +x task.sh
authy run --scope my-scope --uppercase --replace-dash '_' -- ./task.sh

Error Codes
Code	Meaning
0	Success
2	Auth failed — check AUTHY_TOKEN / AUTHY_KEYFILE
3	Secret or policy not found
4	Access denied or run-only restriction
6	Token invalid, expired, or revoked
Rules
Only use authy run, authy resolve, and authy list — these are the only commands available to you
Never hardcode credentials — reference env vars, run via authy run
Never echo, print, or log env vars in subprocess scripts — secrets exist in memory only
Never redirect env vars to files — do not write $SECRET to disk
Use --scope to limit access to needed secrets only
Weekly Installs
18
Repository
eric8810/authy
GitHub Stars
22
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykPass