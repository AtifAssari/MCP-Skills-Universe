---
title: langsmith evaluators
url: https://skills.sh/langchain-ai/langchain-skills/langsmith-evaluators
---

# langsmith evaluators

skills/langchain-ai/langchain-skills/LangSmith Evaluators
LangSmith Evaluators
Installation
$ npx skills add https://github.com/langchain-ai/langchain-skills --skill 'LangSmith Evaluators'
SKILL.md
LANGSMITH_API_KEY=lsv2_pt_your_api_key_here          # Required
LANGSMITH_WORKSPACE_ID=your-workspace-id              # Optional: for org-scoped keys
OPENAI_API_KEY=your_openai_key                        # For LLM as Judge


Python Dependencies

pip install langsmith langchain-openai python-dotenv


JavaScript Dependencies

npm install langsmith commander chalk cli-table3 dotenv openai


<crucial_requirement>

Golden Rule: Inspect Before You Implement

CRITICAL: Before writing ANY evaluator or extraction logic, you MUST:

Run your agent on sample inputs and capture the actual output
Inspect the output - print it, query LangSmith traces, understand the exact structure
Only then write code that processes that output

Output structures vary significantly by framework, agent type, and configuration. Never assume the shape - always verify first. Query LangSmith traces to when outputs don't contain needed data to understand how to extract from execution. </crucial_requirement>

<evaluator_format>

Offline vs Online Evaluators

Offline Evaluators (attached to datasets):

Function signature: (run, example) - receives both run outputs and dataset example
Use case: Comparing agent outputs to expected values in a dataset
Upload with: --dataset "Dataset Name"

Online Evaluators (attached to projects):

Function signature: (run) - receives only run outputs, NO example parameter
Use case: Real-time quality checks on production runs (no reference data)
Upload with: --project "Project Name"

CRITICAL - Return Format:

Return {"score": value, "comment": "..."} - the metric key is auto-derived from the function name
Each evaluator returns ONE metric only. For multiple metrics, create multiple evaluator functions.
Do NOT return {"metric_name": value} or lists of metrics - this will error.

CRITICAL - Local vs Uploaded (Python only):

Local evaluate(): run is a RunTree object → use run.outputs
Uploaded to LangSmith: run is a dict → use run["outputs"]
Handle both: run.outputs if hasattr(run, "outputs") else run.get("outputs", {})
TypeScript always uses attribute access: run.outputs?.field </evaluator_format>

<evaluator_types>

LLM as Judge - Uses an LLM to grade outputs. Best for subjective quality (accuracy, helpfulness, relevance).
Custom Code - Deterministic logic. Best for objective checks (exact match, trajectory validation, format compliance). </evaluator_types>

<llm_judge>

LLM as Judge Evaluators

NOTE: LLM-as-Judge upload is currently not supported by our script only supports code evaluators. For evaluations against a dataset, STRONGLY PREFER defining local evaluators to use with evaluate(evaluators=[...]).

class Grade(TypedDict): reasoning: Annotated[str, ..., "Explain your reasoning"] is_accurate: Annotated[bool, ..., "True if response is accurate"]

judge = ChatOpenAI(model="gpt-4o-mini", temperature=0).with_structured_output(Grade, method="json_schema", strict=True)

async def accuracy_evaluator(run, example): run_outputs = run.outputs if hasattr(run, "outputs") else run.get("outputs", {}) or {} example_outputs = example.outputs if hasattr(example, "outputs") else example.get("outputs", {}) or {} grade = await judge.ainvoke([{"role": "user", "content": f"Expected: {example_outputs}\nActual: {run_outputs}\nIs this accurate?"}]) return {"score": 1 if grade["is_accurate"] else 0, "comment": grade["reasoning"]}

</python>
</llm_judge>

<code_evaluators>
## Custom Code Evaluators

**Before writing an evaluator:**
1. Inspect your dataset to understand expected field names (see Golden Rule above)
2. Test your run function and verify its output structure matches the dataset schema
3. Query LangSmith traces to debug any mismatches

<python>
```python
def trajectory_evaluator(run, example):
    run_outputs = run.outputs if hasattr(run, "outputs") else run.get("outputs", {}) or {}
    example_outputs = example.outputs if hasattr(example, "outputs") else example.get("outputs", {}) or {}
    # IMPORTANT: Replace these placeholders with your actual field names
    # 1. Query your LangSmith trace to see what fields exist in run outputs
    # 2. Check your dataset schema for expected field names
    # Note: Trajectory data may not appear in default output - verify against trace!
    actual = run_outputs.get("YOUR_TRAJECTORY_FIELD", [])
    expected = example_outputs.get("YOUR_EXPECTED_FIELD", [])
    return {"score": 1 if actual == expected else 0, "comment": f"Expected {expected}, got {actual}"}


<run_functions>

Defining Run Functions

Run functions execute your agent and return outputs for evaluation.

CRITICAL - Test Your Run Function First: Before writing evaluators, you MUST test your run function and inspect the actual output structure. Output shapes vary by framework, agent type, and configuration.

Debugging workflow:

Run your agent once on sample input
Query the trace to see the execution structure
Print the raw output and verify against trace to output contains the right data
Adjust the run function as needed
Verify your output matches your dataset schema

Try your hardest to match your run function output to your dataset schema. This makes evaluators simple and reusable. If matching isn't possible, your evaluator must know how to extract and compare the right fields from each side.

def run_agent(inputs: dict) -> dict:
    result = your_agent.run(inputs)
    # ALWAYS inspect output shape first - run this, check the print, query traces
    print(f"DEBUG - type: {type(result)}, keys: {result.keys() if hasattr(result, 'keys') else 'N/A'}")
    print(f"DEBUG - value: {result}")
    return {"output": result}  # Adjust to match your dataset schema

Capturing Trajectories

For trajectory evaluation, your run function must capture tool calls during execution.

CRITICAL: Run output formats vary significantly by framework and agent type. You MUST inspect before implementing:

LangGraph agents (LangChain OSS): Use stream_mode="debug" with subgraphs=True to capture nested subagent tool calls.

import uuid

def run_agent_with_trajectory(agent, inputs: dict) -> dict:
    config = {"configurable": {"thread_id": f"eval-{uuid.uuid4()}"}}
    trajectory = []
    final_result = None

    for chunk in agent.stream(inputs, config=config, stream_mode="debug", subgraphs=True):
        # STEP 1: Print chunks to understand the structure
        print(f"DEBUG chunk: {chunk}")

        # STEP 2: Write extraction based on YOUR observed structure
        # ... your extraction logic here ...

    # IMPORTANT: After running, query the LangSmith trace to verify
    # your trajectory data is complete. Default output may be missing
    # tool calls that appear in the trace.
    return {"output": final_result, "trajectory": trajectory}


Custom / Non-LangChain Agents:

Inspect output first - Run your agent and inspect the result structure. Trajectory data may already be included in the output (e.g., result.tool_calls, result.steps, etc.)
Callbacks/Hooks - If your framework supports execution callbacks, register a hook that records tool names on each invocation
Parse execution logs - As a last resort, extract tool names from structured logs or trace data

The key is to capture the tool name at execution time, not at definition time. </run_functions>

IMPORTANT - Auto-Run Behavior: Evaluators uploaded to a dataset automatically run when you run experiments on that dataset. You do NOT need to pass them to evaluate() - just run your agent against the dataset and the uploaded evaluators execute automatically.

IMPORTANT - Local vs Uploaded: Uploaded evaluators have very limited package access for security reasons! DO NOT upload evaluators that unless they only need to rely on standard Python / Javascript functionality, such as built-in packages. For dataset (offline) evaluators, prefer running locally with evaluate(evaluators=[...]) first. This gives you full package access.

IMPORTANT - Code vs Structured Evaluators:

Code evaluators (what our script uploads): Run in a limited environment without external packages. Use for deterministic logic (exact match, trajectory validation).
Structured evaluators (LLM-as-Judge): Configured via LangSmith UI, use a specific payload format with model/prompt/schema. Our script does not support this format yet.

IMPORTANT - Choose the right target:

--dataset: Offline evaluator with (run, example) signature - for comparing to expected values
--project: Online evaluator with (run) signature - for real-time quality checks

You must specify one. Global evaluators are not supported.

# List all evaluators
python upload_evaluators.py list

# Upload offline evaluator (attached to dataset)
python upload_evaluators.py upload my_evaluators.py \
  --name "Trajectory Match" --function trajectory_evaluator \
  --dataset "My Dataset" --replace

# Upload online evaluator (attached to project)
python upload_evaluators.py upload my_evaluators.py \
  --name "Quality Check" --function quality_check \
  --project "Production Agent" --replace

# Delete
python upload_evaluators.py delete "Trajectory Match"

# List all evaluators
npx tsx upload_evaluators.ts list

# Upload offline evaluator (attached to dataset)
npx tsx upload_evaluators.ts upload my_evaluators.js \
  --name "Trajectory Match" --function trajectoryEvaluator \
  --dataset "My Dataset" --replace

# Upload online evaluator (attached to project)
npx tsx upload_evaluators.ts upload my_evaluators.js \
  --name "Quality Check" --function qualityCheck \
  --project "Production Agent" --replace

# Delete
npx tsx upload_evaluators.ts delete "Trajectory Match"


IMPORTANT - Safety Prompts:

The script prompts for confirmation before destructive operations
NEVER use --yes flag unless the user explicitly requests it

<best_practices>

Use structured output for LLM judges - More reliable than parsing free-text
Match evaluator to dataset type
Final Response → LLM as Judge for quality
Trajectory → Custom Code for sequence
Use async for LLM judges - Enables parallel evaluation
Test evaluators independently - Validate on known good/bad examples first
Choose the right language
Python: Use for Python agents, langchain integrations
JavaScript: Use for TypeScript/Node.js agents </best_practices>

<running_evaluations>

Running Evaluations

Uploaded evaluators auto-run when you run experiments - no code needed. Local evaluators are passed directly for development/testing.

from langsmith import evaluate

# Uploaded evaluators run automatically
results = evaluate(run_agent, data="My Dataset", experiment_prefix="eval-v1")

# Or pass local evaluators for testing
results = evaluate(run_agent, data="My Dataset", evaluators=[my_evaluator], experiment_prefix="eval-v1")


</running_evaluations>

Output doesn't match what you expect: Query the LangSmith trace. It shows exact inputs/outputs at each step - compare what you find to what you're trying to extract.

One metric per evaluator: Return {"score": value, "comment": "..."}. For multiple metrics, create separate functions.

Field name mismatch: Your run function output must match dataset schema exactly. Inspect dataset first with client.read_example(example_id).

RunTree vs dict (Python): Local evaluate() passes RunTree, uploaded evaluators receive dict. Handle both:

run_outputs = run.outputs if hasattr(run, "outputs") else run.get("outputs", {}) or {}

Weekly Installs
–
Repository
langchain-ai/la…n-skills
GitHub Stars
643
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail