---
rating: ⭐⭐
title: skill-system-workflow
url: https://skills.sh/arthur0824hao/skills/skill-system-workflow
---

# skill-system-workflow

skills/arthur0824hao/skills/skill-system-workflow
skill-system-workflow
Installation
$ npx skills add https://github.com/arthur0824hao/skills --skill skill-system-workflow
SKILL.md
Skill System Workflow

skill-system-workflow is the planning layer for the skill system. It turns a goal into a DAG with Mermaid output, prefers reusable recipes when possible, and stays strictly read-only with respect to execution.

Ticket lifecycle operations are owned by skill-system-tkt. This skill now owns only planning, visualization, and recipe discovery.

Overview
Input: a goal plus optional context
Output: a DAG document and Mermaid flowchart TD
Planning strategy: recipe match first, dynamic planning second
Execution: out of scope; downstream skills consume the DAG
Core Operations
plan

Analyze a goal and produce a workflow DAG plus Mermaid visualization.

Read the available recipes/
Match goal against trigger_patterns
If a recipe matches, adapt it to the goal
Otherwise, use prompts/plan-workflow.md to generate a custom DAG
Render Mermaid from the DAG using the conventions below

Procedure: scripts/plan-and-visualize.md

visualize

Convert an existing DAG YAML into a Mermaid flowchart.

Parse waves[*].tasks[*]
Use one Mermaid subgraph per wave
Add depends_on edges
Apply status styling (pending, running, done, failed)
list-recipes

List available workflow recipes by reading recipes/ and returning each recipe's name and description.

File Layout
prompts/plan-workflow.md: one-pass dynamic DAG planning prompt
schema/workflow-dag.yaml: workflow DAG shape specification
schema/recipe.yaml: recipe shape specification
recipes/*.yaml: reusable workflow templates
scripts/plan-and-visualize.md: human procedure for plan -> DAG -> Mermaid
scripts/dispatch.sh: multi-agent dispatch engine (sends opencode run commands)
scripts/chain.sh: step completion handler (auto-dispatches next step or notifies reviewer)
schema/dispatch-order.yaml: dispatch order shape specification
recipes/multi-agent-dispatch.yaml: recipe for cross-repo bundle dispatch
Recipe Format Reference

Recipes are small YAML documents that describe reusable waves and tasks.

name: recipe identifier (must match the filename without extension)
trigger_patterns: goal keywords/phrases that indicate the recipe is applicable
waves: ordered execution waves
waves[*].parallel: whether tasks in the wave can be performed simultaneously
waves[*].tasks[*].depends_on: task ids from earlier waves that must complete first

See: schema/recipe.yaml

Mermaid Conventions
Diagram structure
Graph direction: flowchart TD
One subgraph per wave: subgraph waveN [Wave N: <description>]
Each task is a node with id task_id
Node label format: <agent_type>\n<task name>
Node shapes
Task nodes: rounded rectangles: task_id(["<agent_type>\\n<name>"])
Optional start/end anchors (if used): start((Start)), end((End))
Status styling

Use Mermaid classes based on each task's status:

pending: not started
running: in progress
done: completed successfully
failed: needs intervention

Configuration

Runtime settings are in config/workflow.yaml. Config is the single source of truth.

See: ../../config/workflow.yaml

Multi-Agent Dispatch

skill-system-workflow now also orchestrates cross-repo dispatch via opencode run. The TKT-000 integrator ticket pattern from skill-system-tkt serves as the coordination point.

dispatch

Dispatch a bundle's downstream work to multiple project coders.

Read the upstream bundle's downstream_bundles field
Build a dispatch-order.yaml with steps in dependency order
Execute scripts/dispatch.sh to send opencode run commands
Coders complete their work and call scripts/chain.sh
chain.sh auto-dispatches the next step or notifies the reviewer

Procedure: see recipe multi-agent-dispatch.yaml

Scripts:

scripts/dispatch.sh <dispatch-order.yaml> — Send opencode run commands
scripts/chain.sh <dispatch-order.yaml> <step-id> — Handle step completion
Both support --dry-run for verification

Schema: schema/dispatch-order.yaml

Chain Protocol:

Reviewer → dispatch.sh → opencode run (coder A)
                             ↓ (coder A completes)
                         chain.sh → opencode run (coder B)
                                        ↓ (coder B completes)
                                    chain.sh → notify reviewer

Integration with TKT-000

The TKT-000 integrator ticket coordinates the bundle. When the dispatch chain completes:

Each coder marks their bundle as done
chain.sh updates the dispatch-order step status
On final step: writes .done file or notifies reviewer via claude CLI
Reviewer closes the upstream TKT-000
Migration Note

Ticket lifecycle operations are owned by skill-system-tkt. skill-system-workflow handles planning (3 ops: plan, visualize, list-recipes) and now also multi-agent dispatch (dispatch).

Operational Notes
Keep waves small (2-6 tasks) so the diagram remains readable.
Prefer parallelism inside a wave; use depends_on for cross-wave ordering.
Every task should have a clear verification outcome.
{
  "schema_version": "2.0",
  "id": "skill-system-workflow",
  "version": "2.0.0",
  "capabilities": ["workflow-plan", "workflow-visualize", "workflow-list-recipes", "workflow-dispatch"],
  "effects": ["fs.read", "fs.write", "db.read", "proc.exec"],
  "operations": {
    "plan": {
      "description": "Analyze a goal and produce an execution plan as a DAG with Mermaid visualization.",
      "input": {
        "goal": {"type": "string", "required": true, "description": "User's goal or task description"},
        "context": {"type": "string", "required": false, "description": "Additional context (files, constraints)"}
      },
      "output": {
        "description": "Workflow DAG YAML plus Mermaid diagram",
        "fields": {"dag": "YAML", "mermaid": "string"}
      },
      "entrypoints": {
        "agent": "Follow scripts/plan-and-visualize.md procedure"
      }
    },
    "visualize": {
      "description": "Convert an existing DAG YAML to a Mermaid flowchart.",
      "input": {
        "dag_yaml": {"type": "string", "required": true, "description": "DAG YAML content"}
      },
      "output": {
        "description": "Mermaid flowchart string",
        "fields": {"mermaid": "string"}
      },
      "entrypoints": {
        "agent": "Apply Mermaid conventions from SKILL.md to the DAG"
      }
    },
    "list-recipes": {
      "description": "List available workflow recipes.",
      "input": {},
      "output": {
        "description": "Array of recipe names and descriptions",
        "fields": {"recipes": "array"}
      },
      "entrypoints": {
        "agent": "List files in recipes/ directory"
      }
    },
    "dispatch": {
      "description": "Dispatch a bundle's downstream work to multiple project coders via opencode run with automatic chaining.",
      "input": {
        "upstream_bundle": {"type": "string", "required": true, "description": "Path to the upstream bundle directory containing downstream_bundles"},
        "workspace_root": {"type": "string", "required": true, "description": "Absolute path to the workspace root"},
        "dry_run": {"type": "boolean", "required": false, "description": "If true, show commands without executing"}
      },
      "output": {
        "description": "Dispatch order YAML with step statuses",
        "fields": {"dispatch_order": "YAML", "steps_dispatched": "number"}
      },
      "entrypoints": {
        "agent": "Follow recipe multi-agent-dispatch.yaml: build dispatch-order.yaml from bundle, then run scripts/dispatch.sh",
        "cli": "scripts/dispatch.sh <dispatch-order.yaml> [--dry-run]"
      }
    }
  },
  "stdout_contract": {
    "last_line_json": false,
    "note": "Agent-executed procedures; output is DAG YAML and Mermaid text."
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
Gen Agent Trust HubPass
SocketPass
SnykPass