---
title: skill-system-dashboard
url: https://skills.sh/arthur0824hao/skills/skill-system-dashboard
---

# skill-system-dashboard

skills/arthur0824hao/skills/skill-system-dashboard
skill-system-dashboard
Installation
$ npx skills add https://github.com/arthur0824hao/skills --skill skill-system-dashboard
SKILL.md
Skill System Dashboard

This skill generates the project dashboard HTML using repository-local data.

Usage
python3 "<this-skill-dir>/scripts/generate.py" --target /path/to/project
python3 "<this-skill-dir>/scripts/generate.py" --target /path/to/project --output /tmp/index.html

Behavior
Reads graph data from skills/skill-system-graph scan output.
Reads skill metadata from skills/skill-system-*/SKILL.spec.yaml and SKILL.behavior.yaml.
Reads ticket/roadmap data from .tkt/.
Reads pending/DB memory snapshots when available.
Writes one HTML file (default <target>/dashboard/index.html).
{
  "schema_version": "2.0",
  "id": "skill-system-dashboard",
  "version": "1.0.0",
  "capabilities": ["dashboard-generate", "dashboard-render"],
  "effects": ["fs.read", "fs.write", "proc.exec", "db.read"],
  "operations": {
    "dashboard-generate": {
      "description": "Generate target dashboard/index.html using target project context.",
      "input": {
        "target": {"type": "string", "required": false, "default": ".", "description": "Target project root"},
        "output": {"type": "string", "required": false, "description": "Output HTML path override"}
      },
      "output": {
        "description": "Dashboard generation report",
        "fields": {"status": "ok | error", "output": "string", "target": "string"}
      },
      "entrypoints": {
        "unix": ["python3", "{skill_dir}/scripts/generate.py", "--target", "{target}"],
        "windows": ["python", "{skill_dir}/scripts/generate.py", "--target", "{target}"]
      }
    }
  }
}

Weekly Installs
11
Repository
arthur0824hao/skills
GitHub Stars
4
First Seen
Mar 24, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass