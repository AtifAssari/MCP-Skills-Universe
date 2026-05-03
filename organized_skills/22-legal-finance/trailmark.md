---
rating: ⭐⭐⭐
title: trailmark
url: https://skills.sh/trailofbits/skills/trailmark
---

# trailmark

skills/trailofbits/skills/trailmark
trailmark
Installation
$ npx skills add https://github.com/trailofbits/skills --skill trailmark
SKILL.md
Trailmark

Parses source code into a directed graph of functions, classes, calls, and semantic metadata for security analysis.

When to Use
Mapping call paths from user input to sensitive functions
Finding complexity hotspots for audit prioritization
Identifying attack surface and entrypoints
Understanding call relationships in unfamiliar codebases
Security review or audit preparation across polyglot projects
Adding LLM-inferred annotations (assumptions, preconditions) to code units
Pre-analysis before mutation testing (genotoxic skill) or diagramming
When NOT to Use
Single-file scripts where call graph adds no value (read the file directly)
Architecture diagrams not derived from code (use the diagramming-code skill or draw by hand)
Mutation testing triage (use the genotoxic skill, which calls trailmark internally)
Runtime behavior analysis (trailmark is static, not dynamic)
Rationalizations to Reject
Rationalization	Why It's Wrong	Required Action
"I'll just read the source files manually"	Manual reading misses call paths, blast radius, and taint data	Install trailmark and use the API
"Pre-analysis isn't needed for a quick query"	Blast radius, taint, and privilege data are only available after preanalysis()	Always run engine.preanalysis() before handing off to other skills
"The graph is too large, I'll sample"	Sampling misses cross-module attack paths	Build the full graph; use subgraph queries to focus
"Uncertain edges don't matter"	Dynamic dispatch is where type confusion bugs hide	Account for uncertain edges in security claims
"Single-language analysis is enough"	Polyglot repos have FFI boundaries where bugs cluster	Use the correct --language flag per component
"Complexity hotspots are the only thing worth checking"	Low-complexity functions on tainted paths are high-value targets	Combine complexity with taint and blast radius data
Installation

MANDATORY: If uv run trailmark fails (command not found, import error, ModuleNotFoundError), install trailmark before doing anything else:

uv pip install trailmark


DO NOT fall back to "manual verification", "manual analysis", or reading source files by hand as a substitute for running trailmark. The tool must be installed and used programmatically. If installation fails, report the error to the user instead of silently switching to manual code reading.

Quick Start
# Auto-detect and merge every supported language under the tree
uv run trailmark analyze --language auto --summary {targetDir}

# Explicit languages (single language or comma-separated list)
uv run trailmark analyze --language rust {targetDir}
uv run trailmark analyze --language python,rust {targetDir}

# Complexity hotspots
uv run trailmark analyze --language auto --complexity 10 {targetDir}

Programmatic API
from trailmark.parse import detect_languages, supported_languages
from trailmark.query.api import QueryEngine

# Ask the installed Trailmark build what it supports
supported_languages()
detect_languages("{targetDir}")

# Prefer auto for unknown or polyglot trees; use explicit lists when needed
engine = QueryEngine.from_directory("{targetDir}", language="auto")
engine = QueryEngine.from_directory("{targetDir}", language="python,rust")

engine.callers_of("function_name")
engine.callees_of("function_name")
engine.paths_between("entry_func", "db_query")
engine.complexity_hotspots(threshold=10)
engine.attack_surface()
engine.summary()
engine.to_json()

# Run pre-analysis (blast radius, entrypoints, privilege
# boundaries, taint propagation)
result = engine.preanalysis()

# Query subgraphs created by pre-analysis
engine.subgraph_names()
engine.subgraph("tainted")
engine.subgraph("high_blast_radius")
engine.subgraph("privilege_boundary")
engine.subgraph("entrypoint_reachable")

# Add LLM-inferred annotations
from trailmark.models import AnnotationKind

engine.annotate("function_name", AnnotationKind.ASSUMPTION,
                "input is URL-encoded", source="llm")

# Query annotations (including pre-analysis results)
engine.annotations_of("function_name")
engine.annotations_of("function_name",
                       kind=AnnotationKind.BLAST_RADIUS)
engine.annotations_of("function_name",
                       kind=AnnotationKind.TAINT_PROPAGATION)

Pre-Analysis Passes

Always run engine.preanalysis() before handing off to genotoxic or diagramming-code skills. Pre-analysis enriches the graph with four passes:

Blast radius estimation — counts downstream and upstream nodes per function, identifies critical high-complexity descendants
Entry point enumeration — maps entrypoints by trust level, computes reachable node sets
Privilege boundary detection — finds call edges where trust levels change (untrusted -> trusted)
Taint propagation — marks all nodes reachable from untrusted entrypoints

Results are stored as annotations and named subgraphs on the graph.

For detailed documentation, see references/preanalysis-passes.md.

Language Selection

Do not hardcode a stale language table in downstream workflows. Ask the installed Trailmark build what it supports:

from trailmark.parse import detect_languages, supported_languages

supported_languages()
detect_languages("{targetDir}")


CLI patterns:

# Auto-detect and merge
uv run trailmark analyze --language auto {targetDir}

# Explicit list for a known polyglot target
uv run trailmark analyze --language python,rust {targetDir}

Graph Model

Node kinds: function, method, class, module, struct, interface, trait, enum, namespace, contract, library, template

Edge kinds: calls, inherits, implements, contains, imports

Edge confidence: certain (direct call, self.method()), inferred (attribute access on non-self object), uncertain (dynamic dispatch)

Per Code Unit
Parameters with types, return types, exception types
Cyclomatic complexity and branch metadata
Docstrings
Annotations: assumption, precondition, postcondition, invariant, blast_radius, privilege_boundary, taint_propagation, finding, audit_note (last two set by augment_sarif / augment_weaudit)
Per Edge
Source/target node IDs, edge kind, confidence level
Project Level
Dependencies (imported packages)
Entrypoints with trust levels and asset values
Named subgraphs (populated by pre-analysis)
Key Concepts

Declared contract vs. effective input domain: Trailmark separates what a function declares it accepts from what can actually reach it via call paths. Mismatches are where vulnerabilities hide:

Widening: Unconstrained data reaches a function that assumes validation
Safe by coincidence: No validation, but only safe callers exist today

Edge confidence: Dynamic dispatch produces uncertain edges. Account for confidence when making security claims.

Subgraphs: Named collections of node IDs produced by pre-analysis. Query with engine.subgraph("name"). Available after engine.preanalysis().

Query Patterns

See references/query-patterns.md for common security analysis patterns.

See references/preanalysis-passes.md for pre-analysis pass documentation.

Weekly Installs
650
Repository
trailofbits/skills
GitHub Stars
4.9K
First Seen
Mar 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass