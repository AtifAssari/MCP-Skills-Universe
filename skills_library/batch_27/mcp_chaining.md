---
title: mcp-chaining
url: https://skills.sh/parcadei/continuous-claude-v3/mcp-chaining
---

# mcp-chaining

skills/parcadei/continuous-claude-v3/mcp-chaining
mcp-chaining
Installation
$ npx skills add https://github.com/parcadei/continuous-claude-v3 --skill mcp-chaining
SKILL.md
MCP Chaining Pipeline

A research-to-implement pipeline that chains 5 MCP tools for end-to-end workflows.

When to Use
Building multi-tool MCP pipelines
Understanding how to chain MCP calls with graceful degradation
Debugging MCP environment variable issues
Learning the tool naming conventions for different MCP servers
What We Built

A pipeline that chains these tools:

Step	Server	Tool ID	Purpose
1	nia	nia__search	Search library documentation
2	ast-grep	ast-grep__find_code	Find AST code patterns
3	morph	morph__warpgrep_codebase_search	Fast codebase search
4	qlty	qlty__qlty_check	Code quality validation
5	git	git__git_status	Git operations
Key Files
scripts/research_implement_pipeline.py - Main pipeline implementation
scripts/test_research_pipeline.py - Test harness with isolated sandbox
workspace/pipeline-test/sample_code.py - Test sample code
Usage Examples
# Dry-run pipeline (preview plan without changes)
uv run python -m runtime.harness scripts/research_implement_pipeline.py \
    --topic "async error handling python" \
    --target-dir "./workspace/pipeline-test" \
    --dry-run --verbose

# Run tests
uv run python -m runtime.harness scripts/test_research_pipeline.py --test all

# View the pipeline script
cat scripts/research_implement_pipeline.py

Critical Fix: Environment Variables

The MCP SDK's get_default_environment() only includes basic vars (PATH, HOME, etc.), NOT os.environ. We fixed src/runtime/mcp_client.py to pass full environment:

# In _connect_stdio method:
full_env = {**os.environ, **(resolved_env or {})}


This ensures API keys from ~/.claude/.env reach subprocesses.

Graceful Degradation Pattern

Each tool is optional. If unavailable (disabled, no API key, etc.), the pipeline continues:

async def check_tool_available(tool_id: str) -> bool:
    """Check if an MCP tool is available."""
    server_name = tool_id.split("__")[0]
    server_config = manager._config.get_server(server_name)
    if not server_config or server_config.disabled:
        return False
    return True

# In step function:
if not await check_tool_available("nia__search"):
    return StepResult(status=StepStatus.SKIPPED, message="Nia not available")

Tool Name Reference
nia (Documentation Search)
nia__search              - Universal documentation search
nia__nia_research        - Research with sources
nia__nia_grep            - Grep-style doc search
nia__nia_explore         - Explore package structure

ast-grep (Structural Code Search)
ast-grep__find_code      - Find code by AST pattern
ast-grep__find_code_by_rule - Find by YAML rule
ast-grep__scan_code      - Scan with multiple patterns

morph (Fast Text Search + Edit)
morph__warpgrep_codebase_search  - 20x faster grep
morph__edit_file                 - Smart file editing

qlty (Code Quality)
qlty__qlty_check         - Run quality checks
qlty__qlty_fmt           - Auto-format code
qlty__qlty_metrics       - Get code metrics
qlty__smells             - Detect code smells

git (Version Control)
git__git_status          - Get repo status
git__git_diff            - Show differences
git__git_log             - View commit history
git__git_add             - Stage files

Pipeline Architecture
                    +----------------+
                    |   CLI Args     |
                    | (topic, dir)   |
                    +-------+--------+
                            |
                    +-------v--------+
                    | PipelineContext|
                    | (shared state) |
                    +-------+--------+
                            |
    +-------+-------+-------+-------+-------+
    |       |       |       |       |       |
+---v---+---v---+---v---+---v---+---v---+
| nia   |ast-grp| morph | qlty  | git   |
|search |pattern|search |check  |status |
+---+---+---+---+---+---+---+---+---+---+
    |       |       |       |       |
    +-------v-------v-------v-------+
                    |
            +-------v--------+
            | StepResult[]   |
            | (aggregated)   |
            +----------------+

Error Handling

The pipeline captures errors without failing the entire run:

try:
    result = await call_mcp_tool("nia__search", {"query": topic})
    return StepResult(status=StepStatus.SUCCESS, data=result)
except Exception as e:
    ctx.errors.append(f"nia: {e}")
    return StepResult(status=StepStatus.FAILED, error=str(e))

Creating Your Own Pipeline
Copy the pattern from scripts/research_implement_pipeline.py
Define your steps as async functions
Use check_tool_available() for graceful degradation
Chain results through PipelineContext
Aggregate with print_summary()
Weekly Installs
304
Repository
parcadei/contin…laude-v3
GitHub Stars
3.8K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass