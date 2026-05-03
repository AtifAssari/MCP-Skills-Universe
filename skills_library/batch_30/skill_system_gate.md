---
title: skill-system-gate
url: https://skills.sh/arthur0824hao/skills/skill-system-gate
---

# skill-system-gate

skills/arthur0824hao/skills/skill-system-gate
skill-system-gate
Installation
$ npx skills add https://github.com/arthur0824hao/skills --skill skill-system-gate
SKILL.md
Skill System Gate

Enforce a fail-closed gate before experiment registration and provide read-only registry safety/status checks.

Decision Matrix
Task Intent	Operation	Primary Backend	Use When
Validate repository artifacts against configurable gate rules	validate	scripts/gate_validate.py	Before close-gate decisions or deterministic policy checks
Validate experiment implementation and logs against gate rules	validate-experiment	preprocess_lib.gate_engine	Legacy GNN/FraudDetect pipeline checks
Check whether registry state is safe for rerun/reset	verify-registry	db_registry.DBExperimentsDB	Before any manual reset/rerun action
View queue health and state counts	status	db_registry.DBExperimentsDB	Need a quick dashboard of current experiment states
Core Patterns
Pattern 1: Validate repository gate compliance
python3 scripts/gate_validate.py --rules config/gate_rules.yaml --artifact-root .

Load configurable gate_rules.yaml.
Support rule types: command, structural, eda-contract.
Emit markdown verdict and JSON summary on the last line.
Pattern 2: Validate legacy experiment gate compliance
scripts/validate_exp.sh <exp_name> [phase_root]

Load gate_bank.json rules.
Run all rule classes (source_contains, source_not_contains, stderr_scan, file_exists, file_min_size).
Emit markdown verdict and JSON summary on the last line.
Pattern 3: Verify registry safety before reset decisions
scripts/check_registry.sh <exp_name> [phase_root]

Read registry entry for the experiment.
Block reset recommendation for RUNNING experiments.
Return status details and safe_to_reset decision JSON.
Pattern 4: Show current registry health dashboard
scripts/status.sh [phase_root]

Aggregate counts across active/completed sets.
Show running experiments and execution location.
Return compact JSON counters on the last line.
Guidelines
Always treat validation as fail-closed: any error-severity rule violation means gate failure.
Always run validate-experiment before registry-facing actions.
Never modify experiment source/config files during checks.
Never execute reset/rerun from this skill; only report recommendations.
Never override RUNNING experiments as safe to reset.
Keep all operations read-only with respect to registry and experiment artifacts.
{
  "schema_version": "2.0",
  "id": "skill-system-gate",
  "version": "1.0.0",
  "capabilities": ["configurable-gate", "experiment-gate", "registry-safety", "experiment-status"],
  "effects": ["fs.read", "db.read", "proc.exec"],
  "operations": {
    "validate-experiment": {
      "description": "Validate experiment source artifacts and logs against gate_bank rules and return a pass/fail verdict.",
      "input": {
        "exp_name": { "type": "string", "required": true, "description": "Experiment directory name under experiments/" },
        "phase_root": { "type": "string", "required": false, "description": "Phase directory path", "default": "/datas/store162/arthur0824hao/Study/GNN/FraudDetect/SubProject/Phase3" }
      },
      "output": {
        "description": "Gate validation markdown plus machine-readable verdict.",
        "fields": { "passed": "boolean", "errors": "number", "warnings": "number" }
      },
      "entrypoints": {
        "unix": ["bash", "scripts/validate_exp.sh", "{exp_name}", "{phase_root}"]
      }
    },
    "validate": {
      "description": "Run configurable gate_rules.yaml checks and emit pass/fail with per-rule results.",
      "input": {
        "rules": { "type": "string", "required": false, "description": "Path to gate rules file", "default": "config/gate_rules.yaml" },
        "artifact_root": { "type": "string", "required": false, "description": "Working directory for rule execution", "default": "." }
      },
      "output": {
        "description": "Gate verdict with per-rule details.",
        "fields": { "passed": "boolean", "errors": "number", "warnings": "number" }
      },
      "entrypoints": {
        "unix": ["python3", "scripts/gate_validate.py", "--rules", "{rules}", "--artifact-root", "{artifact_root}"]
      }
    },
    "verify-registry": {
      "description": "Check registry state safety and recommend whether reset/rerun is safe without mutating state.",
      "input": {
        "exp_name": { "type": "string", "required": true, "description": "Experiment name in registry" },
        "phase_root": { "type": "string", "required": false, "description": "Phase directory path", "default": "/datas/store162/arthur0824hao/Study/GNN/FraudDetect/SubProject/Phase3" }
      },
      "output": {
        "description": "Registry safety markdown plus recommendation payload.",
        "fields": { "found": "boolean", "status": "string", "safe_to_reset": "boolean" }
      },
      "entrypoints": {
        "unix": ["bash", "scripts/check_registry.sh", "{exp_name}", "{phase_root}"]
      }
    },
    "status": {
      "description": "Show current registry dashboard with counts by status and running experiment details.",
      "input": {
        "phase_root": { "type": "string", "required": false, "description": "Phase directory path", "default": "/datas/store162/arthur0824hao/Study/GNN/FraudDetect/SubProject/Phase3" }
      },
      "output": {
        "description": "Registry status dashboard and aggregate counters.",
        "fields": { "running": "number", "needs_rerun": "number", "completed": "number", "total": "number" }
      },
      "entrypoints": {
        "unix": ["bash", "scripts/status.sh", "{phase_root}"]
      }
    }
  },
  "stdout_contract": {
    "last_line_json": true
  }
}

Weekly Installs
37
Repository
arthur0824hao/skills
GitHub Stars
4
First Seen
Mar 8, 2026
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykPass