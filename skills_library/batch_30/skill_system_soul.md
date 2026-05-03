---
title: skill-system-soul
url: https://skills.sh/arthur0824hao/skills/skill-system-soul
---

# skill-system-soul

skills/arthur0824hao/skills/skill-system-soul
skill-system-soul
Installation
$ npx skills add https://github.com/arthur0824hao/skills --skill skill-system-soul
SKILL.md
Skill System Soul

Soul is the canonical owner of agent personality profiles, session facets, dual-matrix soul state, and versioned soul evolution. Load it when you need to adopt a behavioral profile, extract/update user preference signals, compare candidate profile changes in an arena, or manage soul evolution snapshots and rollback.

Why

Different models (Claude, GPT, Gemini) have different default behaviors. Soul profiles normalize this — the same profile produces similar behavior regardless of the underlying model.

Different tasks also need different behavioral modes:

Exploring ideas → be creative, divergent, ask lots of questions
Reviewing code → be strict, one rule at a time, no mercy
Discussing with a user → be talkative, dig deep, use question tools
Selecting a Profile

Match the task to a profile:

Task Type	Profile	When
Brainstorming, exploration, research	creative	Ideas > correctness, divergent thinking needed
Code review, linting, compliance	strict	Correctness > speed, zero tolerance for ambiguity
User interviews, requirements gathering, discussions	talkative	Understanding > efficiency, deep-dive into user intent
Standard development work	balanced	Default. Blend of all modes.

Read the profile file: profiles/<name>.md

Profile Structure

Each profile defines:

Identity — Who you are in this mode
Decision Heuristics — How to make choices when uncertain
Communication Style — How to express yourself
Quality Bar — What counts as "done"
Tool Preferences — Which tools to favor
Anti-Patterns — What to avoid in this mode
Available Profiles
balanced (default)

Standard operating mode. Use when no specific behavioral mode is needed.

Read: profiles/balanced.md

creative

Divergent thinking mode. For exploration, brainstorming, and research.

Read: profiles/creative.md

strict

Convergent precision mode. For code review, compliance, and rule enforcement.

Read: profiles/strict.md

talkative

Deep engagement mode. For user interviews, requirements gathering, and discussions.

Read: profiles/talkative.md

Observe And Evolve

Soul now owns the full observe-and-evolve loop:

extract-facets / update-matrix / synthesize-profile
evolve-proposals / observe-from-compaction / suggest-scriptification
evolve-arena-loop / evolve-soul
list-versions / rollback

The compatibility surface for skill-system-insight remains temporarily available as a deprecated shim, but soul is the implementation owner.

Compaction-aware observation stays proposal-safe: hook-triggered summaries record compaction-derived signals only when quantitative compaction counts are present, and repeated multi-step operations can produce scriptification suggestions without auto-generating scripts.

Evolution Arena

Use scripts/evolution_arena.py run for A/B comparison between two profiles on the same task.

Soul owns the arena stage and the integrated observe/evolve operations. Arena still only emits recommendations and never auto-switches profiles or auto-merges changes.

Inputs: profile_a, profile_b, task text, and metric objects (completion_time, test_pass_rate, code_quality_score, evidence_quality)
Outputs: winner profile + rationale, rollback suggestion when candidate regresses, and merge suggestion helpers
Safety: no automatic profile switch and no automatic merge
Creating Custom Profiles

Copy profiles/balanced.md as template. Adjust the 6 sections to match your needs. Place in profiles/ directory with a descriptive name.

{
  "schema_version": "2.0",
  "id": "skill-system-soul",
  "version": "1.3.0",
  "capabilities": ["soul-profile-load", "soul-profile-list", "soul-evolution-arena", "soul-facet-extract", "soul-matrix-update", "soul-profile-synthesize", "soul-evolve", "soul-proposals", "soul-compaction-observe", "soul-scriptification-suggest", "soul-versioning"],
  "effects": ["fs.read", "fs.write", "db.read", "db.write"],
  "operations": {
    "load-profile": {
      "description": "Load a behavioral profile by name. Agent reads and adopts the profile.",
      "input": {
        "profile_name": { "type": "string", "required": true, "description": "Profile name: balanced, creative, strict, talkative, or a user name" }
      },
      "output": {
        "description": "Profile markdown content",
        "fields": { "content": "markdown text" }
      },
      "entrypoints": {
        "agent": "Read profiles/<profile_name>.md"
      }
    },
    "list-profiles": {
      "description": "List available soul profiles.",
      "input": {},
      "output": {
        "description": "Array of profile names",
        "fields": { "profiles": "array of strings" }
      },
      "entrypoints": {
        "agent": "List files in profiles/ directory"
      }
    },
    "arena-run": {
      "description": "Run an A/B arena comparison between two soul profiles and emit winner/rationale plus rollback suggestion.",
      "input": {
        "profile_a": { "type": "string", "required": true, "description": "Baseline profile" },
        "profile_b": { "type": "string", "required": true, "description": "Candidate profile" },
        "task": { "type": "string", "required": true, "description": "Task identifier" },
        "metrics": { "type": "object", "required": true, "description": "profile_a/profile_b metric payload" }
      },
      "output": {
        "description": "Arena report",
        "fields": { "winner": "object", "rollback_suggestion": "object", "auto_switch": "false" }
      },
      "entrypoints": {
        "unix": ["python3", "scripts/evolution_arena.py", "run", "--profile-a", "{profile_a}", "--profile-b", "{profile_b}", "--task", "{task}", "--metrics-json", "{metrics}"]
      }
    },
    "extract-facets": {
      "description": "Extract a per-session facet from transcript.",
      "input": {
        "session_id": { "type": "string", "required": true },
        "user": { "type": "string", "required": true }
      },
      "output": {
        "description": "Facet extraction result",
        "fields": { "status": "string", "memory_id": "integer" }
      },
      "entrypoints": {
        "agent": "Follow scripts/extract-facets.md procedure"
      }
    },
    "update-matrix": {
      "description": "Update dual matrix from stored facets.",
      "input": {
        "user": { "type": "string", "required": true }
      },
      "output": {
        "description": "Updated soul-state",
        "fields": { "status": "string", "values_changed": "boolean" }
      },
      "entrypoints": {
        "agent": "Follow scripts/update-matrix.md procedure"
      }
    },
    "synthesize-profile": {
      "description": "Regenerate a soul profile from matrix and recent facets.",
      "input": {
        "user": { "type": "string", "required": true }
      },
      "output": {
        "description": "Synthesized profile result",
        "fields": { "status": "string", "profile_path": "string", "version_tag": "string" }
      },
      "entrypoints": {
        "agent": "Follow scripts/synthesize-profile.md procedure"
      }
    },
    "evolve-proposals": {
      "description": "Generate non-destructive evolution proposals from soul-state facets.",
      "input": {
        "user": { "type": "string", "required": true }
      },
      "output": {
        "description": "Proposal-only evolve output",
        "fields": { "status": "string", "proposals": "array", "reason": "string" }
      },
      "entrypoints": {
        "agent": "Use scripts/insight_bundle_b012.py evolve-proposals"
      }
    },
    "observe-from-compaction": {
      "description": "Store compaction-derived observation signals from hook payloads.",
      "input": {
        "user": { "type": "string", "required": true },
        "session_id": { "type": "string", "required": true },
        "compaction_json": { "type": "object", "required": true }
      },
      "output": {
        "description": "Stored compaction observation result",
        "fields": { "status": "string", "stored_count": "integer", "trigger": "string" }
      },
      "entrypoints": {
        "unix": ["python3", "scripts/insight_bundle_b012.py", "observe-from-compaction", "--user", "{user}", "--session-id", "{session_id}", "--compaction-json", "{compaction_json}"],
        "windows": ["python", "scripts/insight_bundle_b012.py", "observe-from-compaction", "--user", "{user}", "--session-id", "{session_id}", "--compaction-json", "{compaction_json}"]
      }
    },
    "suggest-scriptification": {
      "description": "Suggest scriptification candidates for repeated multi-step operations.",
      "input": {
        "user": { "type": "string", "required": true },
        "session_id": { "type": "string", "required": true }
      },
      "output": {
        "description": "Suggestion-only scriptification report",
        "fields": { "status": "string", "count": "integer", "suggestions": "array" }
      },
      "entrypoints": {
        "unix": ["python3", "scripts/insight_bundle_b012.py", "suggest-scriptification", "--user", "{user}", "--session-id", "{session_id}"],
        "windows": ["python", "scripts/insight_bundle_b012.py", "suggest-scriptification", "--user", "{user}", "--session-id", "{session_id}"]
      }
    },
    "evolve-arena-loop": {
      "description": "Run proposal -> arena -> merge suggestion flow.",
      "input": {
        "user": { "type": "string", "required": true },
        "task": { "type": "string", "required": true },
        "current_profile": { "type": "string", "required": true },
        "proposals": { "type": "array", "required": true },
        "metrics": { "type": "object", "required": true }
      },
      "output": {
        "description": "Arena and merge suggestion report",
        "fields": { "arena_runs": "array", "merge_suggestions": "array", "auto_merge": "false" }
      },
      "entrypoints": {
        "agent": "Use scripts/insight_bundle_b012.py evolve-arena-loop"
      }
    },
    "evolve-soul": {
      "description": "Evolve soul profile from accumulated insight data.",
      "input": {
        "user": { "type": "string", "required": true }
      },
      "output": {
        "description": "Evolution result",
        "fields": { "version_tag": "string", "changes": "array", "profile_path": "string" }
      },
      "entrypoints": {
        "agent": "Follow scripts/evolve-soul.md procedure"
      }
    },
    "list-versions": {
      "description": "List all evolution snapshots for a user.",
      "input": {
        "user": { "type": "string", "required": true },
        "target": { "type": "string", "required": false }
      },
      "output": {
        "description": "Version snapshots",
        "fields": { "versions": "array" }
      },
      "entrypoints": {
        "agent": "Follow scripts/list-versions.md procedure"
      }
    },
    "rollback": {
      "description": "Restore a previous evolution version.",
      "input": {
        "user": { "type": "string", "required": true },
        "version_tag": { "type": "string", "required": true }
      },
      "output": {
        "description": "Rollback result",
        "fields": { "status": "string", "restored_from": "string" }
      },
      "entrypoints": {
        "agent": "Follow scripts/rollback.md procedure"
      }
    }
  },
  "stdout_contract": {
    "last_line_json": false,
    "note": "Agent-executed; profiles are markdown files read directly."
  }
}

Weekly Installs
66
Repository
arthur0824hao/skills
GitHub Stars
4
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass