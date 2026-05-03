---
rating: ⭐⭐⭐
title: skill-system-cli
url: https://skills.sh/arthur0824hao/skills/skill-system-cli
---

# skill-system-cli

skills/arthur0824hao/skills/skill-system-cli
skill-system-cli
Installation
$ npx skills add https://github.com/arthur0824hao/skills --skill skill-system-cli
SKILL.md
Skill System CLI

Single command sk that dispatches to all skill system operations. Agent-native: JSON output by default, progressive disclosure via --help.

This is the public user-facing contract for the skill system. Other skills are capability modules behind this entrypoint.

Inspired by CLI-Anything — making everything agent-native through structured CLI interfaces.

Quick Start
# Show all domains
python3 "<this-skill-dir>/scripts/sk.py" --help

# Bootstrap a project
python3 "<this-skill-dir>/scripts/sk.py" init

# Check project status
python3 "<this-skill-dir>/scripts/sk.py" status

# Ticket operations
python3 "<this-skill-dir>/scripts/sk.py" tkt claim --ticket-id TKT-001

# Memory operations
python3 "<this-skill-dir>/scripts/sk.py" mem search "query"

# Config operations
python3 "<this-skill-dir>/scripts/sk.py" config get tkt.bundle.max_tickets

# Thin host shell MVP (installer-backed direct entry)
bash "skills/skill-system-installer/scripts/skills.sh" host-shell doctor --target .

Configuration

Runtime settings are in config/cli.yaml. Config is the single source of truth.

See: ../../config/cli.yaml

Architecture
sk (thin dispatcher)
├── init           → bootstrap.md Phase 1+2 logic
├── status         → aggregate project health
├── scan           → discover runnable scripts and CLI hints
├── run            → execute script with auto-detected runner
├── config         → read/write config/*.yaml
│   ├── list
│   ├── show <file>
│   ├── get <key>
│   └── set <key> <value>
├── tkt            → tkt.sh + tickets.py
│   ├── init-roadmap, create-bundle, bundle-status, close-bundle, list-bundles
│   ├── intake, list-tickets, claim, block, close
│   ├── check-open, summary, loop, startup
│   ├── refresh-new, refresh-inbox
│   ├── closure-report, scope
├── mem            → mem.py
│   ├── search, store, status, tags, categories
├── gate           → skill-system-gate
│   └── validate
└── install        → skills.sh
    ├── list, add, status, update, sync

Design Principles
Thin dispatcher — sk.py never reimplements logic. It routes to existing scripts via subprocess or import.
JSON-first — All output follows the last-line JSON contract. Agents parse the last line.
Progressive disclosure — No args shows domains. sk tkt shows tkt actions. sk tkt claim --help shows claim options.
Config-aware — Reads from config/ for defaults.
Idempotent init — sk init only creates what's missing, never overwrites.
Note governance — sk status exposes AGENTS.md guidance merged with note/preferences.md, note/constraints.md, and note/style.md, with note files taking precedence.
Output Contract

Every command emits JSON on the last line:

{"status": "ok", ...}
{"status": "error", "message": "...", ...}

Domains
sk init

Bootstrap project structure. Scaffolds config/, note/, .tkt/, checks PostgreSQL.

It also scaffolds note governance overlays when missing:

note/preferences.md
note/constraints.md
note/style.md
sk status

Aggregate project health: config, note, tkt, postgres, skills counts, plus merged governance context.

sk config

Read/write config values using dot-path notation: sk config get tkt.bundle.max_tickets.

sk tkt

Full ticket lifecycle — both filesystem bundles (tkt.sh) and DB durable tickets (tickets.py).

sk mem

Memory operations — search, store, list, compact, export, status, tags, categories.

Examples:

python3 "<this-skill-dir>/scripts/sk.py" mem search "fraud" --scope project --limit 5
python3 "<this-skill-dir>/scripts/sk.py" mem store --type semantic --category fraud --title note --content hello --scope session
python3 "<this-skill-dir>/scripts/sk.py" mem list --scope project --limit 20
python3 "<this-skill-dir>/scripts/sk.py" mem compact --scope project
python3 "<this-skill-dir>/scripts/sk.py" mem export --format json --scope global

sk install

Skill management — list, add, update, sync.

{
  "schema_version": "2.0",
  "id": "skill-system-cli",
  "version": "1.1.0",
  "capabilities": [
    "cli-dispatch", "project-init", "project-status",
    "cli-scan", "cli-run", "gate-dispatch",
    "config-read", "config-write",
    "tkt-dispatch", "tkt-create-shortcut", "mem-dispatch", "install-dispatch", "router-dispatch", "graph-dispatch", "coder-lifecycle-dispatch", "coder-harness-dispatch", "debug-lifecycle-dispatch", "reviewer-comms-dispatch", "cron-dispatch", "github-dispatch", "creator-dispatch"
  ],
  "effects": ["fs.read", "fs.write", "db.read", "db.write", "proc.exec"],
  "operations": {
    "init": {
      "description": "Bootstrap project structure and report what was created or verified.",
      "input": {
        "check": {"type": "boolean", "required": false, "description": "Detect only, do not create missing structure"}
      },
      "output": {
        "description": "Bootstrap report",
        "fields": {"status": "string", "init_report": "object"}
      },
      "entrypoints": {
        "unix": ["python3", "{skill_dir}/scripts/sk.py", "init"],
        "windows": ["python", "{skill_dir}/scripts/sk.py", "init"]
      }
    },
    "status": {
      "description": "Show global project health across config, note, TKT, postgres, and skills inventory.",
      "input": {},
      "output": {
        "description": "Aggregated health report",
        "fields": {"status": "string", "config": "object", "note": "object", "tkt": "object", "postgres": "object", "skills": "object"}
      },
      "entrypoints": {
        "unix": ["python3", "{skill_dir}/scripts/sk.py", "status"],
        "windows": ["python", "{skill_dir}/scripts/sk.py", "status"]
      }
    },
    "scan": {
      "description": "Scan repository scripts and infer runnable CLI targets.",
      "input": {},
      "output": {
        "description": "Discovered script targets",
        "fields": {"status": "string", "targets": "array"}
      },
      "entrypoints": {
        "unix": ["python3", "{skill_dir}/scripts/sk.py", "scan"],
        "windows": ["python", "{skill_dir}/scripts/sk.py", "scan"]
      }
    },
    "run": {
      "description": "Run any discovered script with auto-detected runner.",
      "input": {
        "script": {"type": "string", "required": true, "description": "Script path or basename"},
        "args": {"type": "array", "required": false, "description": "Pass-through arguments"}
      },
      "output": {
        "description": "Script stdout/stderr passthrough",
        "fields": {"status": "string"}
      },
      "entrypoints": {
        "agent": "Invoke scripts/sk.py run <script> [args...]"
      }
    },
    "gate-validate": {
      "description": "Route configurable gate validation through skill-system-gate.",
      "input": {
        "rules": {"type": "string", "required": false, "description": "Gate rules path"},
        "artifact_root": {"type": "string", "required": false, "description": "Rule execution root"}
      },
      "output": {
        "description": "Gate validation payload",
        "fields": {"status": "string", "passed": "boolean"}
      },
      "entrypoints": {
        "unix": ["python3", "{skill_dir}/scripts/sk.py", "gate", "validate"]
      }
    },
    "config-get": {
      "description": "Read a config value by dot-path.",
      "input": {
        "key": {"type": "string", "required": true, "description": "Dot-path key to read"}
      },
      "output": {
        "description": "Resolved config value",
        "fields": {"status": "string", "value": "json"}
      },
      "entrypoints": {
        "unix": ["python3", "{skill_dir}/scripts/sk.py", "config", "get", "{key}"],
        "windows": ["python", "{skill_dir}/scripts/sk.py", "config", "get", "{key}"]
      }
    },
    "config-set": {
      "description": "Set a config value by dot-path.",
      "input": {
        "key": {"type": "string", "required": true, "description": "Dot-path key to update"},
        "value": {"type": "string", "required": true, "description": "Value to write"}
      },
      "output": {
        "description": "Updated config confirmation",
        "fields": {"status": "string", "key": "string", "value": "string", "file": "string"}
      },
      "entrypoints": {
        "unix": ["python3", "{skill_dir}/scripts/sk.py", "config", "set", "{key}", "{value}"],
        "windows": ["python", "{skill_dir}/scripts/sk.py", "config", "set", "{key}", "{value}"]
      }
    },
    "tkt-dispatch": {
      "description": "Route any TKT subcommand through the unified CLI.",
      "input": {
        "args": {"type": "string", "required": false, "description": "Pass-through TKT arguments"}
      },
      "output": {
        "description": "Passthrough JSON payload from skill-system-tkt",
        "fields": {"status": "string"}
      },
      "entrypoints": {
        "agent": "Invoke scripts/sk.py with the tkt subcommand family and forward args unchanged"
      }
    },
    "tkt-create-shortcut": {
      "description": "Provide a simpler public CLI alias for express ticket creation with templates.",
      "input": {
        "title": {"type": "string", "required": true},
        "template": {"type": "string", "required": false},
        "acceptance": {"type": "string", "required": false}
      },
      "output": {
        "description": "Passthrough JSON payload from tkt express create",
        "fields": {"status": "string"}
      },
      "entrypoints": {
        "agent": "Invoke scripts/sk.py tkt create --title <title> [--template <name>] [--acceptance <text>]"
      }
    },
    "tkt-batch-update-shortcut": {
      "description": "Provide a simpler public CLI alias for batch ticket updates with evidence parity.",
      "input": {
        "bundle": {"type": "string", "required": true},
        "status": {"type": "string", "required": true},
        "summary": {"type": "string", "required": false},
        "evidence": {"type": "string", "required": false},
        "evidence_file": {"type": "string", "required": false},
        "reason": {"type": "string", "required": false},
        "ticket_ids": {"type": "array", "required": true}
      },
      "output": {
        "description": "Passthrough JSON payload from tkt batch update",
        "fields": {"status": "string"}
      },
      "entrypoints": {
        "agent": "Invoke scripts/sk.py tkt batch-update --bundle <bundle> --status <status> [--evidence <text> | --evidence-file <path>] <ticket-id>..."
      }
    },
    "mem-dispatch": {
      "description": "Route any memory subcommand through the unified CLI.",
      "input": {
        "args": {"type": "string", "required": false, "description": "Pass-through memory arguments"}
      },
      "output": {
        "description": "Passthrough JSON payload from skill-system-memory",
        "fields": {"status": "string"}
      },
      "entrypoints": {
        "agent": "Invoke scripts/sk.py with the mem subcommand family and forward args unchanged"
      }
    },
    "install-dispatch": {
      "description": "Route any installer subcommand through the unified CLI.",
      "input": {
        "args": {"type": "string", "required": false, "description": "Pass-through installer arguments"}
      },
      "output": {
        "description": "Passthrough JSON payload from skill-system-installer",
        "fields": {"status": "string"}
      },
      "entrypoints": {
        "agent": "Invoke scripts/sk.py with the install subcommand family and forward args unchanged"
      }
    },
    "router-check-policy": {
      "description": "Route router policy evaluation and surface structured policy decisions.",
      "input": {
        "skill_id": {"type": "string", "required": true, "description": "Skill identifier being evaluated"},
        "effects": {"type": "array", "required": true, "description": "Requested effects to evaluate"},
        "profile": {"type": "string", "required": false, "description": "Policy profile name; defaults to dev"},
        "verbose": {"type": "boolean", "required": false, "description": "Print a human policy summary before the final JSON line"}
      },
      "output": {
        "description": "Passthrough JSON payload from the CLI-owned router policy evaluation",
        "fields": {"status": "string", "policy_decisions": "array"}
      },
      "entrypoints": {
        "agent": "Invoke scripts/sk.py [--verbose] router check-policy --skill-id <id> --effect <effect>... using scripts/router.py owned by skill-system-cli"
      }
    },
    "graph-dispatch": {
      "description": "Route graph navigation and refresh commands through the unified CLI.",
      "input": {
        "args": {"type": "string", "required": false, "description": "Pass-through graph arguments"}
      },
      "output": {
        "description": "Passthrough JSON payload from skill-system-graph",
        "fields": {"status": "string"}
      },
      "entrypoints": {
        "agent": "Invoke scripts/sk.py with the graph subcommand family and forward args unchanged"
      }
    },
    "coder-lifecycle-dispatch": {
      "description": "Route coder lifecycle session management commands through the unified CLI.",
      "input": {
        "args": {"type": "string", "required": false, "description": "Pass-through coder lifecycle arguments"}
      },
      "output": {
        "description": "Passthrough JSON payload from skill-system-coder-lifecycle",
        "fields": {"status": "string"}
      },
      "entrypoints": {
        "agent": "Invoke scripts/sk.py with the coder-lifecycle subcommand family and forward args unchanged"
      }
    },
    "coder-harness-dispatch": {
      "description": "Route thin coder harness shell commands through the unified CLI.",
      "input": {
        "args": {"type": "string", "required": false, "description": "Pass-through coder harness arguments"}
      },
      "output": {
        "description": "Passthrough stdout/stderr/exit behavior from skill-system-comms coder shell scripts",
        "fields": {"status": "plaintext-or-exitcode"}
      },
      "entrypoints": {
        "agent": "Invoke scripts/sk.py with the coder subcommand family and forward args unchanged to skill-system-comms/scripts/coder/*.sh"
      }
    },
    "debug-lifecycle-dispatch": {
      "description": "Route the debug v2 lifecycle commands through the unified CLI.",
      "input": {
        "args": {"type": "string", "required": false, "description": "Pass-through debug lifecycle arguments"}
      },
      "output": {
        "description": "Passthrough JSON payload from skill-system-debug",
        "fields": {"status": "string"}
      },
      "entrypoints": {
        "agent": "Invoke scripts/sk.py with the debug subcommand family and forward args unchanged to skill-system-debug/scripts/debug_tool.py"
      }
    },
    "reviewer-comms-dispatch": {
      "description": "Route reviewer communication commands through the unified CLI.",
      "input": {
        "args": {"type": "string", "required": false, "description": "Pass-through reviewer comms arguments"}
      },
      "output": {
        "description": "Passthrough JSON payload from skill-system-reviewer-comms",
        "fields": {"status": "string"}
      },
      "entrypoints": {
        "agent": "Invoke scripts/sk.py with the reviewer-comms subcommand family and forward args unchanged"
      }
    },
    "cron-dispatch": {
      "description": "Route cron management commands through the unified CLI.",
      "input": {
        "args": {"type": "string", "required": false, "description": "Pass-through cron arguments"}
      },
      "output": {
        "description": "Passthrough JSON payload from skill-system-cron",
        "fields": {"status": "string"}
      },
      "entrypoints": {
        "agent": "Invoke scripts/sk.py with the cron subcommand family and forward args unchanged"
      }
    },
    "github-dispatch": {
      "description": "Route GitHub issue and PR commands through the unified CLI.",
      "input": {
        "args": {"type": "string", "required": false, "description": "Pass-through github arguments"}
      },
      "output": {
        "description": "Passthrough JSON payload from skill-system-github",
        "fields": {"status": "string"}
      },
      "entrypoints": {
        "agent": "Invoke scripts/sk.py with the github subcommand family and forward args unchanged"
      }
    },
    "creator-dispatch": {
      "description": "Route creator brainstorm and grill-me commands through the unified CLI.",
      "input": {
        "args": {"type": "string", "required": false, "description": "Pass-through creator arguments"}
      },
      "output": {
        "description": "Passthrough JSON payload from skill-system-creator",
        "fields": {"status": "string"}
      },
      "entrypoints": {
        "agent": "Invoke scripts/sk.py with the creator subcommand family and forward args unchanged"
      }
    }
  },
  "stdout_contract": {
    "last_line_json": true,
    "note": "All commands emit JSON on last line. Status is always 'ok' or 'error'."
  }
}

Weekly Installs
26
Repository
arthur0824hao/skills
GitHub Stars
4
First Seen
Mar 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykFail