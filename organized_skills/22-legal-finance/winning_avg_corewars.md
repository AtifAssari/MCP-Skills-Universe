---
rating: ⭐⭐
title: winning-avg-corewars
url: https://skills.sh/letta-ai/skills/winning-avg-corewars
---

# winning-avg-corewars

skills/letta-ai/skills/winning-avg-corewars
winning-avg-corewars
Installation
$ npx skills add https://github.com/letta-ai/skills --skill winning-avg-corewars
SKILL.md
CoreWars Warrior Development
Overview

This skill provides a systematic methodology for developing CoreWars warriors that achieve specified win rate thresholds against multiple opponents. It emphasizes deep opponent analysis, systematic parameter tuning, automated testing, and targeted strategy development rather than ad-hoc trial-and-error approaches.

Prerequisites

Before beginning warrior development:

Verify pmars (Portable MARS) is available for testing battles
Identify all opponent warriors and their required win rate thresholds
Read and understand the opponent warrior code before writing any counter-strategies
Determine core size and other battle parameters from the task requirements
Development Workflow
Phase 1: Opponent Analysis

Before writing any warrior code, thoroughly analyze each opponent:

Read opponent source code - Understand the warrior's strategy, not just observe its behavior

Categorize opponent type - Identify if it's a bomber, scanner, replicator, imp, paper, stone, or hybrid

Extract exploitable patterns:

What step/interval does it use for bombing or scanning?
What positions in the core does it avoid or target?
Does it have predictable timing or movement patterns?
What are its weaknesses (e.g., vulnerable to imps, slow startup)?

Document findings - Create a brief profile for each opponent:

Opponent: stone.red
Type: Bomber
Step: 4 (bombs every 4 positions)
Weakness: Predictable bombing pattern, vulnerable to positions not divisible by 4
Counter-strategy ideas: Use step sizes that avoid multiples of 4

Phase 2: Strategy Selection

Based on opponent analysis, determine appropriate warrior archetypes:

Common CoreWars Warrior Types:

Scanner: Searches for enemies before attacking
Bomber: Blindly drops DAT bombs at regular intervals
Replicator (Paper): Creates copies of itself throughout the core
Imp: Simple MOV 0,1 that creates self-propagating spirals
Vampire: Uses JMP traps to capture enemy processes
Stone: Bomber with defensive spl/jmp stuns
Silk: Optimized replicator with specific step patterns

Strategy Decision Tree:

Against slow bombers → Fast replicators or scanners
Against replicators → Scanners with quick-scan or vampires
Against imps → Imp gates (spl 0, dat 0 pairs) or core clears
Against scanners → Decoys combined with attack components
Against core clears → Fast-spreading replicators
Phase 3: Initial Implementation

Start with simple, focused warriors rather than complex multi-component designs:

Begin minimal - Test the simplest version of chosen strategy first
One component at a time - Add complexity only after understanding base performance
Use proven patterns - Reference established CoreWars strategies from documentation
Avoid premature optimization - Get basic functionality working before tuning
Phase 4: Systematic Testing

Use the automated test script (scripts/test_warrior.sh) for consistent evaluation:

./scripts/test_warrior.sh warrior.red


Testing principles:

Run sufficient rounds (100+) for statistical significance
Track results in a structured format across iterations
Test against ALL opponents after every change, not just the one being targeted
Record parameter values alongside results for later analysis
Phase 5: Parameter Optimization

When tuning parameters (step sizes, gate positions, spl counts):

Systematic search - Use grid search or binary search over parameter ranges
Understand relationships - Document why certain values work (e.g., step=17 avoids common bombing intervals)
Track tradeoffs - Changes that improve one matchup may harm another
Hypothesis-driven changes - Before each modification, state the expected outcome

Key parameters to tune:

Step size for bombers/scanners (affects coverage pattern)
Gate position for imp defenses
Number of SPL instructions (affects process count vs. speed)
Starting offset from main code
Phase 6: Debugging Failures

When a warrior consistently loses to an opponent:

Profile the failure - Use pmars debugging to watch the battle:
pmars -b -r 1 warrior.red opponent.red

Identify failure mode - Is the warrior being bombed, captured, out-replicated, or core-cleared?
Trace causation - At what point in the battle does the warrior lose control?
Develop targeted fix - Address the specific failure mechanism, not symptoms
Phase 7: Multi-Opponent Optimization

When facing different win rate requirements:

Prioritize high-threshold opponents - Focus more effort on 75% targets than 33% targets
Consider specialized warriors - Sometimes separate warriors per opponent outperform one universal warrior
Identify compatible strategies - Find approaches that don't harm each other
Accept strategic tradeoffs - A warrior optimized for hard targets may sacrifice performance on easy targets
Common Pitfalls
Mistakes to Avoid
Ad-hoc parameter changes - Changing values without clear hypotheses leads to random walks
Ignoring opponent code - Reading behavior isn't understanding; examine the actual source
Over-engineering early - Complex multi-component warriors obscure what works and what doesn't
Neglecting hardest opponents - Easy wins don't compensate for failing required thresholds
Batch testing - Test after EVERY change to understand impact immediately
Syntax/spacing issues - Redcode assemblers are sensitive; verify syntax with dry runs
Copying without understanding - Adapting code from examples requires understanding why it works
Red Flags During Development
Making changes without being able to explain expected improvement
Win rate oscillating without trending upward
Spending most time on already-passing matchups
Not using debugging tools to understand failures
Submitting warriors that don't meet all thresholds
Verification Checklist

Before considering warrior complete:

 All opponents analyzed and weaknesses documented
 Win rates meet or exceed ALL required thresholds
 Tested with statistically significant round counts (100+)
 Parameter choices can be justified with reasoning
 Failure modes against difficult opponents understood
 No syntax errors or assembly warnings
Resources
scripts/

Contains test_warrior.sh - An automated test script that runs battles against all opponents and reports results in a consistent format. Use this for every iteration to track progress systematically.

references/

Contains corewars_strategies.md - Reference documentation covering CoreWars warrior archetypes, common patterns, and known effective techniques. Consult this before implementing unfamiliar strategies.

Weekly Installs
34
Repository
letta-ai/skills
GitHub Stars
94
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass