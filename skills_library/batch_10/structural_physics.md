---
title: structural-physics
url: https://skills.sh/bbeierle12/skill-mcp-claude/structural-physics
---

# structural-physics

skills/bbeierle12/skill-mcp-claude/structural-physics
structural-physics
Installation
$ npx skills add https://github.com/bbeierle12/skill-mcp-claude --skill structural-physics
SKILL.md
Structural Physics

Stability validation and damage systems for building mechanics.

Quick Start
import { HeuristicValidator } from './scripts/heuristic-validator.js';
import { DamageSystem } from './scripts/damage-propagation.js';

// Rust/Valheim style stability
const validator = new HeuristicValidator({ mode: 'heuristic' });
validator.addPiece(piece);
const result = validator.validatePlacement(newPiece);
// result: { valid: true, stability: 0.85, supports: [...] }

// Damage and collapse
const damage = new DamageSystem(validator);
damage.applyDamage(piece, 50, 'physical');
damage.applyExplosiveDamage(position, 100, 10); // radius damage

Reference

See references/structural-physics-advanced.md for:

Physics mode comparison (arcade vs heuristic vs realistic)
Material properties and decay rates
Damage state thresholds
Cascade mechanics
Scripts
scripts/heuristic-validator.js - Fast validation (Fortnite/Rust/Valheim modes)
scripts/stability-optimizer.js - Caching and batch updates for large structures
scripts/damage-propagation.js - Damage states, fire spread, cascading collapse
scripts/physics-engine-lite.js - Optional realistic stress/strain simulation
Physics Modes
Arcade (Fortnite): Connectivity only, instant collapse, best for combat
Heuristic (Rust/Valheim): Stability %, predictable rules, best for survival
Realistic: Full stress/strain, computationally expensive, best for engineering sims
Weekly Installs
56
Repository
bbeierle12/skil…p-claude
GitHub Stars
8
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass