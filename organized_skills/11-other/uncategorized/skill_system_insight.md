---
rating: ⭐⭐
title: skill-system-insight
url: https://skills.sh/arthur0824hao/skills/skill-system-insight
---

# skill-system-insight

skills/arthur0824hao/skills/skill-system-insight
skill-system-insight
Installation
$ npx skills add https://github.com/arthur0824hao/skills --skill skill-system-insight
SKILL.md
Skill System Insight

Deprecated compatibility surface. skill-system-soul is now the canonical owner of observe/evolve behavior, but this skill remains available so existing insight routes, docs, and tests do not break during the merge window.

Unified OBSERVE → EVOLVE engine for user adaptation.

This skill turns sessions into structured behavioral insights ("facets"), uses those facets to maintain a dual-matrix soul state, and periodically evolves soul profiles and workflow recipes — all versioned and rollbackable.

Two Phases, One Skill
Phase 1 — OBSERVE
  Extract facets → Update matrix buffers → (optional) Trigger synthesis

Phase 2 — EVOLVE
  Read accumulated data → Plan evidence-backed changes → Apply with versioning → Snapshot for audit/rollback


Phase 1 produces raw signal. Phase 2 consumes it to make durable changes.

The evolve lifecycle can run through an arena comparison loop:

session -> facets -> evolve proposals -> arena A/B -> merge suggestion

The arena stage only emits recommendations. It never auto-switches profiles and never auto-merges changes.

Architecture: Hybrid 3-Layer System
Layer 1: Base Profile (balanced.md)
  - Static skeleton: section format + safety/quality defaults.

Layer 2: Dual Matrix (soul-state)
  - Personality Matrix (slow/stable): openness, directness, autonomy, rigor, warmth
  - Emotion Matrix (faster baseline): patience, enthusiasm, caution, empathy

Layer 3: Synthesized Profile (user.md)
  - Periodically regenerated from Layer 1 + Layer 2 + accumulated facets.
  - Every regeneration creates a versioned snapshot.


Layer 2 is the ground truth. Layer 3 is a readable, versioned projection.

Data Model
Facets (per-session extraction): schema/facet.yaml
Soul state (dual matrix + counters/buffers): schema/soul-state.yaml
Evolution plan (proposed changes): schema/evolution-plan.yaml
Evolution snapshot (versioned artifact): schema/evolution-snapshot.yaml

Storage uses the Postgres agent_memories table and typed sub-tables:

Facets: memory_type='episodic', category='insight-facet' → typed table: insight_facets
Soul state: memory_type='semantic', category='soul-state' → typed table: soul_states
Evolution snapshots: memory_type='episodic', category='evolution-snapshot' → typed table: evolution_snapshots

Typed functions (dual-write to both typed table and agent_memories):

insert_insight_facet(user, session_id, yaml, ...) → stores facet
upsert_soul_state(user, yaml, personality, emotion, ...) → stores/updates soul state
get_soul_state(user) → reads from soul_states
get_recent_facets(user, limit) → reads from insight_facets
insert_evolution_snapshot(user, version_tag, target, ...) → stores versioned snapshot
get_evolution_history(user, limit) → reads from evolution_snapshots
Phase 1: OBSERVE Pipeline
Trigger (manual or suggested) → Extract Facet → Update Matrix → (optional) Synthesize Profile


References:

Facet extraction prompt: prompts/facet-extraction.md
Soul synthesis prompt: prompts/soul-synthesis.md
Extraction procedure: scripts/extract-facets.md
Matrix update algorithm: scripts/update-matrix.md
Profile regeneration procedure: scripts/synthesize-profile.md
How To Trigger (OBSERVE)

This is a manual workflow.

User can ask explicitly: "insight", "extract facets", "learn my preferences", "update my profile".
Router suggestion pattern (lightweight, non-pushy):
"Want me to run an insight pass to learn from this session? (stores a facet + may update your matrix)"

When the user asks (or agrees), run:

scripts/extract-facets.md
scripts/update-matrix.md
If the synthesis trigger fires: scripts/synthesize-profile.md
Phase 2: EVOLVE Pipeline
Trigger (manual or scheduled) → Read facets + matrix → Plan evolution → Safety check → Apply → Snapshot


References:

Evolution planning prompt: prompts/evolution-planning.md
Recipe evolution prompt: prompts/recipe-evolution.md
Soul evolution procedure: scripts/evolve-soul.md
Recipe evolution procedure: scripts/evolve-recipes.md
Version listing: scripts/list-versions.md
Rollback procedure: scripts/rollback.md
How To Trigger (EVOLVE)
User can ask: "evolve my profile", "evolve recipes", "list versions", "rollback to v2".
Automatic trigger when synthesis trigger fires during OBSERVE phase.
Version Tags

Format: v{N}_{target}_{timestamp} Example: v3_soul_20260211

Algorithm: N = 1 + max(existing N) for the same user+target. Start at N=1 if none exist.

Writes
Evolution snapshots → Postgres (evolution_snapshots + agent_memories)
Soul profiles (filesystem) → ../skill-system-soul/profiles/<user>.md
Workflow recipes (filesystem) → ../skill-system-workflow/recipes/*.yaml
Configuration

All runtime settings (rate limits, thresholds, step sizes, approval gates) are in config/insight.yaml.

Config is the single source of truth. Values below are documentation defaults — if they differ from config/, config/ wins.

See: ../../config/insight.yaml

Constraints (Non-Negotiable)
Transparency

Always explain what was learned and why.

Facets must contain evidence strings tied to concrete moments.
Matrix updates must add short context lines explaining each applied adjustment.
Every evolution change must include evidence strings from facets or state context.
Rate Limiting (defaults — see config/insight.yaml)
OBSERVE: Max observe.max_facets_per_day facets per user per rolling 24 hours.
If over limit: summarize what you would have captured, ask the user to pick 1 session to record.
EVOLVE: Max evolve.max_passes_per_day evolution pass per day per user (across all targets).
Use the most recent evolution-snapshot date as the limiter.
Confidence Threshold (defaults — see config/insight.yaml)

Do not change matrix values on a single observation.

Threshold: observe.confidence_threshold+ similar observations in the same direction.
Personality step size: +/- observe.personality_step per qualifying adjustment.
Emotion baseline step size: +/- observe.emotion_step per qualifying adjustment.

Accumulation tracked in buffers for testability and explainability.

Safety (Evolution)
Cannot remove core safety constraints from soul profiles.
Evolved profiles must retain: honest uncertainty, no hallucinated authority, refusal of harmful/illegal instructions.
Major changes (any dimension change > evolve.approval_drift_threshold) require explicit user approval before applying.
Where Layer 1 and Layer 3 Live
Base profile (Layer 1): ../skill-system-soul/profiles/balanced.md
Synthesized user profile (Layer 3): ../skill-system-soul/profiles/<user>.md

The synthesis step preserves the 6-section format:

Identity
Decision Heuristics
Communication Style
Quality Bar
Tool Preferences
Anti-Patterns
Storage Pattern (agent_memories)

Example SQL templates:

-- Store a facet
SELECT store_memory(
  'episodic', 'insight-facet',
  ARRAY['session:ses_xxx', 'user:arthu'],
  'Session Facet: <brief_summary>',
  '<full facet YAML as text>',
  '{"session_type": "...", "outcome": "..."}',
  'insight-agent', 'ses_xxx', 5.0
);

-- Store/update matrix state
SELECT store_memory(
  'semantic', 'soul-state',
  ARRAY['user:arthu', 'matrix'],
  'Soul State: arthu',
  '<full soul-state YAML as text>',
  '{"total_insights": 0, "last_updated": "..."}',
  'insight-agent', NULL, 9.0
);

-- Store evolution snapshot (typed — dual-writes to agent_memories)
SELECT insert_evolution_snapshot(
  '<user>', '<version_tag>', '<target>', '<trigger>',
  '<changes JSONB>', '<snapshot_data>', '<full YAML>',
  NULL, 'insight-agent'
);

-- Query recent facets
SELECT * FROM search_memories('insight-facet user:arthu', NULL, NULL, NULL, NULL, 0.0, 50);

-- List evolution history
SELECT * FROM get_evolution_history('<user>', 50);

Operational Notes
Facet extraction should be completable in one pass. If you cannot justify an adjustment with concrete evidence, propose no adjustment.
Users may communicate in Chinese; treat that as a signal about comfort, not as a personality dimension.
Keep values clamped to [0.0, 1.0].
{
  "schema_version": "2.0",
  "id": "skill-system-insight",
  "version": "2.2.0",
  "capabilities": [
    "insight-issue-routing", "insight-session-facets", "insight-extract", "insight-matrix-update", "insight-synthesize",
    "evolution-proposal-draft",
    "evolution-arena-loop",
    "evolution-soul", "evolution-recipes", "evolution-list", "evolution-rollback"
  ],
  "effects": ["db.read", "db.write", "fs.read", "fs.write"],
  "operations": {
    "route-issue-draft": {
      "description": "Route findings into a draft issue target based on tags/category without creating issues.",
      "input": {
        "finding": { "type": "object", "required": true, "description": "Finding payload with tags/category/evidence/impact/suggested_direction" },
        "project_repo": { "type": "string", "required": true, "description": "Current project repository owner/name" },
        "skill_system_repo": { "type": "string", "required": true, "description": "Skill-system repository owner/name" }
      },
      "output": {
        "description": "Draft routing payload",
        "fields": { "status": "ok | error", "target_repo": "string", "draft_command": "string" }
      },
      "entrypoints": {
        "agent": "Use scripts/insight_bundle_b012.py route-issue-draft"
      }
    },
    "extract-session-facets": {
      "description": "Session-end facet extraction to soul-state memories via mem.py DB path or pending fallback.",
      "input": {
        "user": { "type": "string", "required": true, "description": "User handle" },
        "session_id": { "type": "string", "required": true, "description": "Session id" },
        "facets": { "type": "array", "required": true, "description": "Facet entries: {dimension, value, confidence, evidence}" }
      },
      "output": {
        "description": "Extraction and storage summary",
        "fields": { "status": "ok | blocked | error", "stored_count": "integer", "skipped_low_confidence": "integer", "skipped_rate_limit": "integer" }
      },
      "entrypoints": {
        "agent": "Use scripts/insight_bundle_b012.py extract-session-facets"
      }
    },
    "evolve-proposals": {
      "description": "Generate non-destructive evolution proposals from soul-state facets with daily-pass safety.",
      "input": {
        "user": { "type": "string", "required": true, "description": "User handle" }
      },
      "output": {
        "description": "Proposal-only evolve output",
        "fields": { "status": "ok | blocked | error", "proposals": "array", "reason": "string" }
      },
      "entrypoints": {
        "agent": "Use scripts/insight_bundle_b012.py evolve-proposals"
      }
    },
    "evolve-arena-loop": {
      "description": "Run proposal -> arena -> merge-suggestion flow using current profile versus mutated proposal candidates.",
      "input": {
        "user": { "type": "string", "required": true, "description": "User handle" },
        "task": { "type": "string", "required": true, "description": "Task label" },
        "current_profile": { "type": "string", "required": true, "description": "Current active profile" },
        "proposals": { "type": "array", "required": true, "description": "Evolution proposals to evaluate" },
        "metrics": { "type": "object", "required": true, "description": "Per-candidate arena metrics" }
      },
      "output": {
        "description": "Arena and merge suggestion report",
        "fields": { "arena_runs": "array", "merge_suggestions": "array", "auto_merge": "false" }
      },
      "entrypoints": {
        "agent": "Use scripts/insight_bundle_b012.py evolve-arena-loop"
      }
    },
    "extract-facets": {
      "description": "Extract a per-session facet from transcript. Rate limited to 3/24h per user.",
      "input": {
        "session_id": { "type": "string", "required": true, "description": "Session to analyze" },
        "user": { "type": "string", "required": true, "description": "User handle" }
      },
      "output": {
        "description": "Facet YAML stored to agent_memories",
        "fields": { "status": "ok | error", "memory_id": "integer" }
      },
      "entrypoints": {
        "agent": "Follow scripts/extract-facets.md procedure"
      }
    },
    "update-matrix": {
      "description": "Update dual matrix from stored facet with confidence gating.",
      "input": {
        "user": { "type": "string", "required": true, "description": "User handle" }
      },
      "output": {
        "description": "Updated soul-state YAML stored to agent_memories",
        "fields": { "status": "ok | error", "values_changed": "boolean" }
      },
      "entrypoints": {
        "agent": "Follow scripts/update-matrix.md procedure"
      }
    },
    "synthesize-profile": {
      "description": "Regenerate Layer 3 Soul profile from matrix + recent facets. Creates versioned snapshot.",
      "input": {
        "user": { "type": "string", "required": true, "description": "User handle" }
      },
      "output": {
        "description": "User profile written to skill-system-soul/profiles/<user>.md with version snapshot",
        "fields": { "status": "ok | error", "profile_path": "string", "version_tag": "string" }
      },
      "entrypoints": {
        "agent": "Follow scripts/synthesize-profile.md then scripts/evolve-soul.md snapshot step"
      }
    },
    "evolve-soul": {
      "description": "Evolve soul profile from accumulated insight data. Creates versioned snapshot.",
      "input": {
        "user": { "type": "string", "required": true, "description": "User handle" }
      },
      "output": {
        "description": "Evolution result with version tag",
        "fields": { "version_tag": "string", "changes": "array", "profile_path": "string" }
      },
      "entrypoints": {
        "agent": "Follow scripts/evolve-soul.md procedure"
      }
    },
    "evolve-recipes": {
      "description": "Evolve workflow recipes based on effectiveness data from insight facets.",
      "input": {
        "user": { "type": "string", "required": true, "description": "User handle" }
      },
      "output": {
        "description": "Recipe evolution result with version tag",
        "fields": { "version_tag": "string", "recipes_changed": "array" }
      },
      "entrypoints": {
        "agent": "Follow scripts/evolve-recipes.md procedure"
      }
    },
    "list-versions": {
      "description": "List all evolution snapshots for a user.",
      "input": {
        "user": { "type": "string", "required": true },
        "target": { "type": "string", "required": false, "description": "Filter: soul | recipe | all" }
      },
      "output": {
        "description": "Array of version snapshots",
        "fields": { "versions": "array of {tag, target, timestamp, summary}" }
      },
      "entrypoints": {
        "agent": "Follow scripts/list-versions.md procedure"
      }
    },
    "rollback": {
      "description": "Restore a previous evolution version.",
      "input": {
        "user": { "type": "string", "required": true },
        "version_tag": { "type": "string", "required": true, "description": "Version tag to restore" }
      },
      "output": {
        "description": "Rollback result",
        "fields": { "status": "ok | error", "restored_from": "string" }
      },
      "entrypoints": {
        "agent": "Follow scripts/rollback.md procedure"
      }
    }
  },
  "stdout_contract": {
    "last_line_json": true,
    "note": "The b012 helper script emits pretty-printed JSON to stdout for routing, facet extraction, and evolve proposals."
  }
}

Weekly Installs
62
Repository
arthur0824hao/skills
GitHub Stars
4
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykPass