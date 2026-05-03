---
title: fdt-refactor-mock-to-fake
url: https://skills.sh/dagster-io/fake-driven-testing/fdt-refactor-mock-to-fake
---

# fdt-refactor-mock-to-fake

skills/dagster-io/fake-driven-testing/fdt-refactor-mock-to-fake
fdt-refactor-mock-to-fake
Installation
$ npx skills add https://github.com/dagster-io/fake-driven-testing --skill fdt-refactor-mock-to-fake
SKILL.md
Refactoring Mocks to Fakes

Remove unittest.mock.patch from tests by making source code inject gateway dependencies, then configuring pre-canned fakes in tests.

Use this skill when: A test imports from unittest.mock import patch or uses @patch(...) decorators.

Key principle: Don't stop at the lowest-level matching gateway. Look for a higher-level abstraction that covers ALL the things being mocked together.

Phase 1: Audit Mock Usage

Read the test file. For each patch(...) call, record:

Mock target (fully qualified)	System boundary (tool)	What it simulates	Return value configured
erk.core.fast_llm.shutil.which	Claude CLI	CLI availability check	None or "/usr/bin/claude"
erk.core.fast_llm.subprocess.run	Claude CLI	CLI execution result	CompletedProcess(returncode=0, stdout="...")

The system boundary column identifies which gateway should own this mock. Multiple mocks with the same system boundary should be covered by a single gateway.

Group mocks by test: A single test patching 2-3 things together suggests those things form a unit that should be covered by one injectable gateway.

Phase 2: Gateway Discovery (Critical)

For each mock group, find the right gateway. Do not stop at the first match.

Rule: subprocess.run is never the right gateway boundary. The gateway should be named after the tool being invoked (e.g., GhCli, CmuxGateway, GitGateway), not after the underlying mechanism (subprocess, shell). A gateway that just wraps subprocess.run is no better than mocking subprocess.run directly — it skips the meaningful abstraction layer.

Step 1: Identify the system boundary being tested

Ask: what is the test actually testing? Not "what function is being patched" but "what behavior is under test?" Think in terms of the tool or service being interacted with, not the Python function being called.

Examples:

shutil.which("claude") -> "is the Claude CLI installed?" (tool: Claude CLI)
subprocess.run(["claude", "--print", ...]) -> "run a prompt via Claude CLI" (tool: Claude CLI)
Together -> "interact with the Claude CLI" -> gateway is PromptExecutor (Claude-specific), not Shell (subprocess-generic)
Step 2: Targeted gateway search

Before broad exploration, do a quick targeted search using the tool names from Phase 1:

Grep(pattern="<tool_name>", path="packages/erk-shared/src/erk_shared/gateway/")


If zero hits for a tool → no gateway exists for it. You'll need to create one (see Phase 5). If hits → read the matching gateway to assess coverage.

This takes seconds and immediately tells you whether you're in "reuse" or "create" territory.

Step 3: Check if any mock target is already covered

Before creating anything new, check if existing gateways already cover some of your mock targets. A test mocking subprocess.run(["gh", "pr", "view", ...]) is already covered by LocalGitHub.get_pr() — no new gateway needed for that mock.

For each system boundary from Phase 1, ask:

Does an existing gateway already provide this operation?
Can the test use the existing fake instead of mocking subprocess?

This often eliminates half the mocks immediately, reducing the scope of new work.

Step 4: Search for existing gateways at the right abstraction level

Search from highest to lowest. A higher-level gateway is preferable because it covers multiple low-level calls as a unit.

# 1. Search for existing ABCs that describe the behavior
Grep(pattern="class Fake\w+", path="packages/erk-shared/src/erk_shared/")
Grep(pattern="class Fake\w+", path="tests/fakes/")

# 2. Find gateways that mention the system call you're replacing
Grep(pattern="shutil.which|subprocess.run|is_available", path="packages/erk-shared/")


Priority order when multiple gateways match:

A gateway that covers ALL mocked targets in a test -> inject this one
A gateway that covers the highest-level behavior (e.g., PromptExecutor.execute_prompt rather than Shell.get_installed_tool_path)
The lowest-level matching gateway as a last resort

Erk gateway locations:

packages/erk-shared/src/erk_shared/gateway/*/abc.py -- gateway ABCs
packages/erk-shared/src/erk_shared/gateway/*/fake.py -- matching fakes
packages/erk-shared/src/erk_shared/core/fakes.py -- fakes for service ABCs (FakePromptExecutor, FakeLlmCaller, FakeScriptWriter, etc.)
tests/fakes/ -- erk-specific fakes
Step 5: Verify the fake covers what you need

Read the fake's __init__ signature. Check:

Can you configure the pre-canned responses the test needs?
Does the fake record calls for assertion (calls, prompt_calls, etc.)?
Does the fake's is_available() return what you need?

If no fake exists at the right level, you'll need to create one (see Phase 5).

Decision Fork: Gateway Found vs. New Gateway Needed

After Phase 2, you're in one of two paths:

Path A: Existing gateway covers all mocks

Skip to Phase 3 (plan injection) → Phase 4 (make injectable) → Phase 6 (rewrite tests)
This is the fast path. Scope: modify source + rewrite tests.

Path B: No gateway exists for one or more system boundaries

You must create a new gateway before rewriting tests
Load the gateway-abc-implementation doc (docs/learned/architecture/gateway-abc-implementation.md)
Follow Phase 5-expanded below
Scope is significantly larger: new gateway files + ErkContext wiring + modify source + rewrite tests
Phase 3: Plan the injection

Identify what source code needs to change.

Where is the mocked code called from?

Read the source file being patched (e.g., erk.core.fast_llm -> src/erk/core/fast_llm.py). Find the class or function that directly calls the mocked thing.

Is there already a constructor parameter for this gateway?
Yes -> skip Phase 4, go to Phase 6
No -> plan to add a constructor parameter
What's the production wiring?

Find where the class is instantiated in production (usually src/erk/core/context.py). Plan what real implementation to wire in:

FallbackPromptExecutor -> ClaudeCliPromptExecutor(console=None)
Shell -> RealShell()
etc.
Phase 4: Make source code injectable

Add the gateway as a constructor parameter. Follow erk's conventions:

Named parameters only (def __init__(self, *, gateway: GatewayABC))
No default parameter values -- caller must wire it explicitly
Store as self._gateway

Replace direct system calls with gateway method calls:

# Before:
if shutil.which("claude") is None: ...
result = subprocess.run(["claude", "--print", ...])

# After:
if not self._prompt_executor.is_available(): ...
result = self._prompt_executor.execute_prompt(prompt, model=..., ...)


Map gateway return types to the source function's return types. If the gateway returns PromptResult(success, output, error) but the function returns LlmResponse | LlmCallFailed, add the mapping:

if not result.success:
    return LlmCallFailed(message=f"CLI failed: {result.error}")
return LlmResponse(text=result.output)


Update production wiring in context.py:

from erk.core.prompt_executor import ClaudeCliPromptExecutor
MyClass(prompt_executor=ClaudeCliPromptExecutor(console=None))

Variant: Click command injection (exec scripts)

For Click commands (especially exec scripts), use Click's context system instead of constructor injection:

@click.command(name="my-command")
@click.pass_context
def my_command(ctx: click.Context, ...) -> None:
    github = require_github(ctx)       # existing gateway from context
    cmux = require_context(ctx).cmux   # new gateway from context


Replace direct system calls with gateway method calls obtained from context. See src/erk/cli/commands/exec/scripts/AGENTS.md for the full pattern.

Phase 5: Create a new gateway (when no suitable gateway exists)

Load docs/learned/architecture/gateway-abc-implementation.md for full patterns.

Decide: 3-file or 5-file pattern
3-file (abc, real, fake): For all-or-nothing operations, process replacement, or operations where dry-run/printing don't add value. Examples: Codespace, AgentLauncher.
5-file (abc, real, fake, dry_run, printing): For gateways with distinct read vs mutation methods where dry-run preview is useful. Examples: Git, LocalGitHub, Graphite.

Most new gateways for mock-to-fake refactoring use the 3-file pattern.

Gateway creation checklist
 Create directory: packages/erk-shared/src/erk_shared/gateway/<tool_name>/
 __init__.py — empty
 abc.py — ABC with abstract methods named after tool operations (not subprocess)
 real.py — Production implementation using subprocess calls to the tool
 fake.py — Constructor-injected test data, NamedTuple call tracking, read-only properties
ErkContext wiring checklist
 Add <tool>: <ToolABC> field to ErkContext dataclass (packages/erk-shared/src/erk_shared/context/context.py)
 Add <tool> parameter to ErkContext.for_test() with default Fake<Tool>(...)
 Wire Real<Tool>() in production context factory (src/erk/core/context.py, near other Real* instantiations)
Error handling decision
All callers terminate on failure → raise RuntimeError
Some callers branch on error → return discriminated union (see Non-Ideal State Decision Checklist in gateway-abc-implementation.md)
Phase 6: Rewrite the tests

For each test that used patch:

Remove from unittest.mock import patch (and any from subprocess import CompletedProcess)
Construct the fake with pre-canned responses
Pass it to the class under test via the new constructor parameter
Replace mock assertions (mock_run.assert_called_once()) with fake property checks (assert len(executor.prompt_calls) == 1)

Pattern:

# Before:
def test_falls_back_to_cli(monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    fake_result = CompletedProcess(args=[], returncode=0, stdout="my-slug\n", stderr="")
    with (
        patch("erk.core.fast_llm.shutil.which", return_value="/usr/bin/claude"),
        patch("erk.core.fast_llm.subprocess.run", return_value=fake_result) as mock_run,
    ):
        result = AnthropicLlmCaller().call("test prompt", system_prompt="sys", max_tokens=50)
    assert isinstance(result, LlmResponse)
    mock_run.assert_called_once()

# After:
def test_falls_back_to_cli(monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    executor = FakePromptExecutor(
        prompt_results=[PromptResult(success=True, output="my-slug", error=None)]
    )
    caller = AnthropicLlmCaller(prompt_executor=executor)
    result = caller.call("test prompt", system_prompt="sys", max_tokens=50)
    assert isinstance(result, LlmResponse)
    assert result.text == "my-slug"
    assert len(executor.prompt_calls) == 1
    assert executor.prompt_calls[0].prompt == "test prompt"


Note: monkeypatch.delenv is a pytest fixture, not mock.patch -- it's fine to keep.

Phase 7: Verify

Run the affected test file:

uv run pytest <test_file> -v


Then lint and type-check the modified source files.

Common pitfalls

Pitfall 1: Matching the wrong gateway level If shutil.which is mocked, the obvious match is Shell.get_installed_tool_path(). But if subprocess.run is also mocked in the same test, the real abstraction is something that covers BOTH -- often PromptExecutor or a similar higher-level gateway.

Pitfall 2: monkeypatch.delenv vs mock.patch monkeypatch.delenv("ANTHROPIC_API_KEY") is a pytest builtin, not mock.patch. Keep it -- it's acceptable and doesn't need replacement.

Pitfall 3: Forgetting to update production wiring After adding a constructor parameter, always update context.py (or wherever the class is instantiated). The type checker will catch this but only if you run it.

Pitfall 4: One test, multiple patch contexts Multiple patch() calls in one test is a red flag that something needs to be at a higher abstraction level. A single fake should replace all of them.

Pitfall 5: Creating a subprocess-level gateway If you find yourself designing a gateway called ShellRunner, SubprocessGateway, or CommandRunner, stop. That's still mocking at the wrong level. The gateway must be specific to the tool being called:

subprocess.run(["gh", ...]) → LocalGitHub or a GhCli gateway
subprocess.run(["cmux", ...]) → CmuxGateway
subprocess.run(["claude", ...]) → PromptExecutor
subprocess.run(["git", ...]) → Git gateway

Name the gateway after what it represents, not how it executes.

Weekly Installs
8
Repository
dagster-io/fake…-testing
First Seen
Mar 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass