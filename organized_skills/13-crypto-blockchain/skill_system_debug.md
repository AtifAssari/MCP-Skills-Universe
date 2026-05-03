---
rating: ⭐⭐
title: skill-system-debug
url: https://skills.sh/arthur0824hao/skills/skill-system-debug
---

# skill-system-debug

skills/arthur0824hao/skills/skill-system-debug
skill-system-debug
Installation
$ npx skills add https://github.com/arthur0824hao/skills --skill skill-system-debug
SKILL.md
skill-system-debug

This skill is coder-only. The public contract is a lifecycle:

start opens a debug session with its own scratch dir and time budget
step records hypothesis progression, evidence, and optional tool friction
close writes a structured lesson with root-cause and verification fields back into memory

Reviewer surfaces should consume the resulting lesson or friction artifacts, not run sk debug directly.

Operations

The preferred public entrypoint is the unified CLI:

python3 ../skill-system-cli/scripts/sk.py debug start --title "FD entry path bug" --symptom "entry.json env paths failed from arbitrary cwd"
python3 ../skill-system-cli/scripts/sk.py debug step --debug-id dbg_123 --hypothesis "paths are cwd-relative" --action "inspect entry rewrite"
python3 ../skill-system-cli/scripts/sk.py debug close --debug-id dbg_123 --root-cause-file path/to/file.py --root-cause-line 42 --hypothesis-chain "..." --counter-evidence "..." --fix "..." --verification "..."


Direct debug_tool.py invocation remains the underlying runtime surface.

start
python3 scripts/debug_tool.py start --title "FD entry path bug" --symptom "entry.json relative path fails in runtime"

step
python3 scripts/debug_tool.py step --debug-id dbg_123 --hypothesis "entry path resolved relative to cwd" --action "inspect loader path join" --evidence "loader joins cwd + entry.json"

close
python3 scripts/debug_tool.py close \
  --debug-id dbg_123 \
  --root-cause-file skills/skill-system-memory/scripts/mem.py \
  --root-cause-line 2162 \
  --hypothesis-chain "cwd-relative path hypothesis -> reproduction -> fix confirmed" \
  --counter-evidence "absolute paths worked, proving parser was fine" \
  --fix "normalize to artifact-relative path resolution" \
  --verification "reproduced bug, applied fix, reran loader successfully"

Lifecycle Rules
Canonical session state lives under .tkt/debug/<debug_id>.yaml
Scratch artifacts live under .sisyphus/tmp/debug/<debug_id>/
Default time budget is 30 minutes; step/close must warn when elapsed time exceeds budget
close is fail-closed if required lesson fields are missing
Tool-unfriendly moments should emit an inbox/friction artifact through the comms helper instead of silently disappearing
Required Lesson Fields

Every successful close must capture:

root_cause.file
root_cause.line
hypothesis_chain
counter_evidence
fix
verification
Integration Notes
Memory writeback should use the existing skill-system-memory surface rather than raw SQL
Friction logging should use the existing skill-system-comms inbox helper path
Existing low-level debug helpers (diagnose/trace/bisect/compare) may remain as internals, but the public lifecycle is start / step / close
Example: real bug workflow

This lifecycle was exercised against the real FD entry.json relative-path bug in:

/share/nas165/arthur0824hao/Work/Study/GNN/FraudDetect/Experiment/scripts/regenerate_fd_absolute_entries.py:54

The resulting close lesson recorded:

root cause file:line
hypothesis chain
counter-evidence
fix
verification

and wrote a debug-lesson memory row after the close path was corrected to respect procedural-memory importance rules.

{
  "schema_version": "2.0",
  "id": "skill-system-debug",
  "version": "0.2.0",
  "capabilities": ["debug-start", "debug-step", "debug-close"],
  "effects": ["fs.read", "fs.write", "proc.exec", "db.write"],
  "operations": {
    "start": {
      "description": "Open a coder-only debug session with isolated scratch state and budget tracking.",
      "input": {
        "title": { "type": "string", "required": true },
        "symptom": { "type": "string", "required": true },
        "workdir": { "type": "string", "required": false },
        "time_budget_minutes": { "type": "integer", "required": false }
      },
      "output": {
        "description": "Debug session metadata",
        "fields": { "debug_id": "string", "state_path": "string", "scratch_dir": "string", "time_budget_minutes": "integer" }
      },
      "entrypoints": {
        "unix": ["python3", "scripts/debug_tool.py", "start", "--title", "{title}", "--symptom", "{symptom}"],
        "windows": ["python", "scripts/debug_tool.py", "start", "--title", "{title}", "--symptom", "{symptom}"]
      }
    },
    "step": {
      "description": "Record one debug step with hypothesis, evidence, and optional tool friction.",
      "input": {
        "debug_id": { "type": "string", "required": true },
        "hypothesis": { "type": "string", "required": true },
        "action": { "type": "string", "required": true },
        "evidence": { "type": "string", "required": false },
        "counter_evidence": { "type": "string", "required": false },
        "tool_unfriendly": { "type": "boolean", "required": false },
        "friction_note": { "type": "string", "required": false }
      },
      "output": {
        "description": "Step progression result",
        "fields": { "debug_id": "string", "step_index": "integer", "budget_warning": "boolean", "friction_logged": "boolean" }
      },
      "entrypoints": {
        "unix": ["python3", "scripts/debug_tool.py", "step", "--debug-id", "{debug_id}", "--hypothesis", "{hypothesis}", "--action", "{action}"],
        "windows": ["python", "scripts/debug_tool.py", "step", "--debug-id", "{debug_id}", "--hypothesis", "{hypothesis}", "--action", "{action}"]
      }
    },
    "close": {
      "description": "Close a debug session and write a structured lesson into memory.",
      "input": {
        "debug_id": { "type": "string", "required": true },
        "root_cause_file": { "type": "string", "required": true },
        "root_cause_line": { "type": "integer", "required": true },
        "hypothesis_chain": { "type": "string", "required": true },
        "counter_evidence": { "type": "string", "required": true },
        "fix": { "type": "string", "required": true },
        "verification": { "type": "string", "required": true }
      },
      "output": {
        "description": "Debug closure result",
        "fields": { "debug_id": "string", "closed": "boolean", "lesson_path": "string", "memory_write_status": "string", "friction_count": "integer" }
      },
      "entrypoints": {
        "unix": ["python3", "scripts/debug_tool.py", "close", "--debug-id", "{debug_id}", "--root-cause-file", "{root_cause_file}", "--root-cause-line", "{root_cause_line}", "--hypothesis-chain", "{hypothesis_chain}", "--counter-evidence", "{counter_evidence}", "--fix", "{fix}", "--verification", "{verification}"],
        "windows": ["python", "scripts/debug_tool.py", "close", "--debug-id", "{debug_id}", "--root-cause-file", "{root_cause_file}", "--root-cause-line", "{root_cause_line}", "--hypothesis-chain", "{hypothesis_chain}", "--counter-evidence", "{counter_evidence}", "--fix", "{fix}", "--verification", "{verification}"]
      }
    }
  }
}

Weekly Installs
19
Repository
arthur0824hao/skills
GitHub Stars
4
First Seen
Mar 22, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass