---
title: langsmith-dataset
url: https://skills.sh/langchain-ai/langsmith-skills/langsmith-dataset
---

# langsmith-dataset

skills/langchain-ai/langsmith-skills/langsmith-dataset
langsmith-dataset
Installation
$ npx skills add https://github.com/langchain-ai/langsmith-skills --skill langsmith-dataset
Summary

Create, manage, and upload evaluation datasets to LangSmith for testing and validation.

Supports four dataset types: final_response (full conversations), single_step (individual node behavior), trajectory (tool call sequences), and RAG (question/chunks/answer/citations)
CLI commands for dataset lifecycle management: create, list, get, delete, export, and upload from local JSON files
SDK-based dataset creation in Python and JavaScript with programmatic example addition
Example management commands to add, list, and delete individual examples within datasets
Complete workflow from trace export through processing to LangSmith upload with experiment tracking
SKILL.md
LANGSMITH_API_KEY=lsv2_pt_your_api_key_here          # REQUIRED
LANGSMITH_PROJECT=your-project-name                   # Check this to know which project has traces
LANGSMITH_WORKSPACE_ID=your-workspace-id              # Optional: for org-scoped keys


Authentication is REQUIRED: either set the LANGSMITH_API_KEY environment variable, or pass the --api-key flag to CLI commands (preferred):

langsmith dataset list --api-key $LANGSMITH_API_KEY


IMPORTANT: Always check the environment variables or .env file for LANGSMITH_PROJECT before querying or interacting with LangSmith. This tells you which project contains the relevant traces and data. If the LangSmith project is not available, use your best judgement to identify the right one.

Python Dependencies

pip install langsmith


JavaScript Dependencies

npm install langsmith


CLI Tool

curl -sSL https://raw.githubusercontent.com/langchain-ai/langsmith-cli/main/scripts/install.sh | sh

Dataset Commands
langsmith dataset list - List datasets in LangSmith
langsmith dataset get <name-or-id> - View dataset details
langsmith dataset create --name <name> - Create a new empty dataset
langsmith dataset delete <name-or-id> - Delete a dataset
langsmith dataset export <name-or-id> <output-file> - Export dataset to local JSON file
langsmith dataset upload <file> --name <name> - Upload a local JSON file as a dataset
Example Commands
langsmith example list --dataset <name> - List examples in a dataset
langsmith example create --dataset <name> --inputs <json> - Add an example to a dataset
langsmith example delete <example-id> - Delete an example
Experiment Commands
langsmith experiment list --dataset <name> - List experiments for a dataset
langsmith experiment get <name> - View experiment results
Common Flags
--limit N - Limit number of results
--yes - Skip confirmation prompts (use with caution)

IMPORTANT - Safety Prompts:

The CLI prompts for confirmation before destructive operations (delete, overwrite)
If you are running with user input: ALWAYS wait for user input; NEVER use --yes unless the user explicitly requests it
If you are running non-interactively: Use --yes to skip confirmation prompts

<dataset_types_overview> Common evaluation dataset types:

final_response - Full conversation with expected output. Tests complete agent behavior.
single_step - Single node inputs/outputs. Tests specific node behavior (e.g., one LLM call or tool).
trajectory - Tool call sequence. Tests execution path (ordered list of tool names).
rag - Question/chunks/answer/citations. Tests retrieval quality. </dataset_types_overview>

<creating_datasets>

Creating Datasets

Datasets are JSON files with an array of examples. Each example has inputs and outputs.

From Exported Traces (Programmatic)

Export traces first, then process them into dataset format using code:

# 1. Export traces to JSONL files
langsmith trace export ./traces --project my-project --limit 20 --full --api-key $LANGSMITH_API_KEY


client = Client()

2. Process traces into dataset examples

examples = [] for jsonl_file in Path("./traces").glob("*.jsonl"): runs = [json.loads(line) for line in jsonl_file.read_text().strip().split("\n")] root = next((r for r in runs if r.get("parent_run_id") is None), None) if root and root.get("inputs") and root.get("outputs"): examples.append({ "trace_id": root.get("trace_id"), "inputs": root["inputs"], "outputs": root["outputs"] })

3. Save locally

with open("/tmp/dataset.json", "w") as f: json.dump(examples, f, indent=2)

</python>

<typescript>
```typescript
import { Client } from "langsmith";
import { readFileSync, writeFileSync, readdirSync } from "fs";
import { join } from "path";

const client = new Client();

// 2. Process traces into dataset examples
const examples: Array<{trace_id?: string, inputs: Record<string, any>, outputs: Record<string, any>}> = [];
const files = readdirSync("./traces").filter(f => f.endsWith(".jsonl"));

for (const file of files) {
  const lines = readFileSync(join("./traces", file), "utf-8").trim().split("\n");
  const runs = lines.map(line => JSON.parse(line));
  const root = runs.find(r => r.parent_run_id == null);
  if (root?.inputs && root?.outputs) {
    examples.push({ trace_id: root.trace_id, inputs: root.inputs, outputs: root.outputs });
  }
}

// 3. Save locally
writeFileSync("/tmp/dataset.json", JSON.stringify(examples, null, 2));

Upload to LangSmith
# Upload local JSON file as a dataset
langsmith dataset upload /tmp/dataset.json --name "My Evaluation Dataset" --api-key $LANGSMITH_API_KEY

Using the SDK Directly

client = Client()

Create dataset and add examples in one step

dataset = client.create_dataset("My Dataset", description="Evaluation dataset")

client.create_examples( inputs=[{"query": "What is AI?"}, {"query": "Explain RAG"}], outputs=[{"answer": "AI is..."}, {"answer": "RAG is..."}], dataset_name="My Dataset", )

</python>

<typescript>
```typescript
import { Client } from "langsmith";

const client = new Client();

// Create dataset and add examples
const dataset = await client.createDataset("My Dataset", {
  description: "Evaluation dataset",
});

await client.createExamples({
  inputs: [{ query: "What is AI?" }, { query: "Explain RAG" }],
  outputs: [{ answer: "AI is..." }, { answer: "RAG is..." }],
  datasetName: "My Dataset",
});


<dataset_structures>

Dataset Structures by Type
Final Response
{"trace_id": "...", "inputs": {"query": "What are the top genres?"}, "outputs": {"response": "The top genres are..."}}

Single Step
{"trace_id": "...", "inputs": {"messages": [...]}, "outputs": {"content": "..."}, "metadata": {"node_name": "model"}}

Trajectory
{"trace_id": "...", "inputs": {"query": "..."}, "outputs": {"expected_trajectory": ["tool_a", "tool_b", "tool_c"]}}

RAG
{"trace_id": "...", "inputs": {"question": "How do I..."}, "outputs": {"answer": "...", "retrieved_chunks": ["..."], "cited_chunks": ["..."]}}


</dataset_structures>

<script_usage>

CLI Usage
# List all datasets
langsmith dataset list --api-key $LANGSMITH_API_KEY

# Get dataset details
langsmith dataset get "My Dataset" --api-key $LANGSMITH_API_KEY

# Create an empty dataset
langsmith dataset create --name "New Dataset" --description "For evaluation" --api-key $LANGSMITH_API_KEY

# Upload a local JSON file
langsmith dataset upload /tmp/dataset.json --name "My Dataset" --api-key $LANGSMITH_API_KEY

# Export a dataset to local file
langsmith dataset export "My Dataset" /tmp/exported.json --limit 100 --api-key $LANGSMITH_API_KEY

# Delete a dataset
langsmith dataset delete "My Dataset" --api-key $LANGSMITH_API_KEY

# List examples in a dataset
langsmith example list --dataset "My Dataset" --limit 10 --api-key $LANGSMITH_API_KEY

# Add an example
langsmith example create --dataset "My Dataset" \
  --inputs '{"query": "test"}' \
  --outputs '{"answer": "result"}' --api-key $LANGSMITH_API_KEY

# List experiments
langsmith experiment list --dataset "My Dataset" --api-key $LANGSMITH_API_KEY
langsmith experiment get "eval-v1" --api-key $LANGSMITH_API_KEY


</script_usage>

<example_workflow> Complete workflow from traces to uploaded LangSmith dataset:

# 1. Export traces from LangSmith
langsmith trace export ./traces --project my-project --limit 20 --full --api-key $LANGSMITH_API_KEY

# 2. Process traces into dataset format (using Python/JS code)
# See "Creating Datasets" section above

# 3. Upload to LangSmith
langsmith dataset upload /tmp/final_response.json --name "Skills: Final Response" --api-key $LANGSMITH_API_KEY
langsmith dataset upload /tmp/trajectory.json --name "Skills: Trajectory" --api-key $LANGSMITH_API_KEY

# 4. Verify upload
langsmith dataset list --api-key $LANGSMITH_API_KEY
langsmith dataset get "Skills: Final Response" --api-key $LANGSMITH_API_KEY
langsmith example list --dataset "Skills: Final Response" --limit 3 --api-key $LANGSMITH_API_KEY

# 5. Run experiments
langsmith experiment list --dataset "Skills: Final Response" --api-key $LANGSMITH_API_KEY


</example_workflow>

Empty dataset after upload:

Verify JSON file contains an array of objects with inputs key
Check file isn't empty: langsmith example list --dataset "Name"

Export has no data:

Ensure traces were exported with --full flag to include inputs/outputs
Verify traces have both inputs and outputs populated

Example count mismatch:

Use langsmith dataset get "Name" to check remote count
Compare with local file to verify upload completeness
Weekly Installs
1.5K
Repository
langchain-ai/la…h-skills
GitHub Stars
105
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn