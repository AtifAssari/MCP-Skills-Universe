---
title: dify-workflow-builder
url: https://skills.sh/r3flector/dify-workflow-builder/dify-workflow-builder
---

# dify-workflow-builder

skills/r3flector/dify-workflow-builder/dify-workflow-builder
dify-workflow-builder
Installation
$ npx skills add https://github.com/r3flector/dify-workflow-builder --skill dify-workflow-builder
SKILL.md
Dify Workflow Builder

Expert skill for generating production-quality Dify DSL workflow files. Generates valid YAML configurations for Dify v1.12+ with precise node schemas derived from Pydantic source models.

Reading Strategy

Always read:

This file (SKILL.md) — process, patterns, quality standards
Node Index — base fields + pick which node files to load
Entry nodes + Output nodes — every workflow needs these

Read on demand (only the files relevant to your task):

Node type files from references/nodes/ — only for node types used in the workflow
Edge Types — when connecting nodes (sourceHandle rules)
Variables — when using system/env/conversation variables
Workflow Structure — for features, conversation_variables, environment_variables
Node Positioning — for layout constants
Enums — for exact enum values
API Reference — for import/export API calls

Example workflows in assets/ — read the most relevant one as a template before generating.

Mode Selection
Choose	When
workflow	One-shot execution, batch processing, API-triggered tasks. Uses start → ... → end.
advanced-chat	Conversational UI, multi-turn dialogue, memory needed. Uses start → ... → answer.

Key differences:

workflow mode: No sys.query, no conversation memory, uses end node with explicit outputs
advanced-chat mode: Has sys.query, sys.conversation_id, sys.dialogue_count, uses answer node for streaming response
Only advanced-chat supports conversation_variables for session-persistent state
Workflow Generation Process (5 Steps)
Step 1: Define Type and Inputs
app:
  mode: workflow | advanced-chat
  name: "Workflow Name"
  description: "What this workflow does"
  icon: "🤖"
  icon_background: "#FFEAD5"
kind: app
version: "0.5.0"


Define start node variables based on user requirements:

- data:
    type: start
    title: Start
    variables:
      - type: text-input | paragraph | select | number | file | file-list
        variable: input_name
        label: "Human-readable label"
        required: true

Step 2: Design the Node Graph

Map the business logic to node types. Read the relevant files from references/nodes/:

AI processing: ai.md — llm, agent, question-classifier, parameter-extractor
Data: data.md — knowledge-retrieval, datasource, document-extractor
Logic: logic.md — if-else, code, template-transform, http-request, tool, list-operator
Flow control: flow.md — iteration, loop, human-input
Variables: variables_nodes.md — variable-aggregator, assigner
Step 3: Generate Unique IDs

Every node needs a unique ID. Use the timestamp-based format:

node_id = str(int(time.time() * 1000))[-10:]  # e.g. "1732456789"

Step 4: Configure Edges

Connect nodes with edges. Read Edge Types for full sourceHandle rules.

- data:
    sourceType: llm
    targetType: end
    isInIteration: false
    isInLoop: false
  id: "source_id-target_id-sourceHandle-targetHandle"
  source: "source_node_id"
  sourceHandle: source        # "source" | "{case_id}" | "false" | "success-branch" | "fail-branch"
  target: "target_node_id"
  targetHandle: target        # always "target"
  type: custom

Step 5: Add Positioning

See Node Positioning for full layout constants.

Linear chain: each node at x += 300 (NODE_WIDTH_X_OFFSET), starting at {x: 80, y: 282}.

  position:
    x: 80
    y: 282
  width: 244
  height: 98  # varies by node type

Common Workflow Patterns
Pattern 1: Simple LLM Chain
start → llm → end/answer


See assets/simple_llm_workflow.yml or assets/simple_llm_chatflow.yml.

Pattern 2: RAG (Retrieval-Augmented Generation)
start → knowledge-retrieval → llm → answer


See assets/knowledge_rag_chatflow.yml.

Pattern 3: Conditional Branching
start → if-else → [branch A: llm-1] → variable-aggregator → end
               → [branch B: llm-2] ↗


See assets/conditional_workflow.yml.

Pattern 4: Error Handling
start → llm (error_strategy: fail-branch)
          → [success-branch] → end
          → [fail-branch] → variable-aggregator → end


See assets/error_handling_workflow.yml.

Pattern 5: Iteration
start → iteration [llm → code] → end


See assets/iteration_workflow.yml.

Pattern 6: Loop with Break
start → loop [code → if-else → loop-end] → end


See assets/loop_workflow.yml.

Pattern 7: Agent with Tools
start → agent(tools: [web-search, calculator]) → answer


See assets/agent_chatflow.yml.

Pattern 8: Human-in-the-Loop
start → llm → human-input → code → end


See assets/human_approval_workflow.yml.

Quality Standards
Required (MUST)
version: "0.5.0" — current DSL version
mode: workflow | advanced-chat — not agent-chat
Every node has unique id (string, timestamp-based)
Every edge references existing source and target node IDs
workflow mode uses end node, advanced-chat uses answer node
All variable_selector paths resolve to existing node outputs or system variables
sourceHandle matches node type pattern (see Edge Types)
error_strategy only uses "fail-branch" or "default-value" (NOT "abort" or "retry")
Container nodes (iteration, loop) have start_node_id pointing to internal start node
assigner (v2) has version: "2" field
Recommended (SHOULD)
Use descriptive title for each node
Enable retry_config for unreliable external calls (http-request, tool)
Use error_strategy: "fail-branch" for non-critical paths
Set is_parallel: true for iteration when items are independent
Keep parallel_nums ≤ 10 to avoid rate limits
Validate with scripts/validate_workflow.py before import
Weekly Installs
17
Repository
r3flector/dify-…-builder
GitHub Stars
4
First Seen
Feb 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn