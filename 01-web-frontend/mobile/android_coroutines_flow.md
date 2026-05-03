---
title: android-coroutines-flow
url: https://skills.sh/krutikjain/android-agent-skills/android-coroutines-flow
---

# android-coroutines-flow

skills/krutikjain/android-agent-skills/android-coroutines-flow
android-coroutines-flow
Installation
$ npx skills add https://github.com/krutikjain/android-agent-skills --skill android-coroutines-flow
SKILL.md
Android Coroutines Flow
When To Use
Use this skill when the request is about: android flow collection, fix coroutine scope in android, structured concurrency in viewmodel.
Primary outcome: Use coroutines, Flow, structured concurrency, dispatchers, and cancellation-safe Android async pipelines.
Handoff skills when the scope expands:
android-state-management
android-workmanager-notifications
Workflow
Map the request to the current Android stack, module boundaries, and minimum supported API level.
Inspect the existing implementation for implicit assumptions, duplicate helpers, and outdated patterns.
Apply the smallest change that improves correctness, readability, and long-term maintainability.
Validate the result against the relevant showcase app path and repo benchmarks.
Hand off adjacent work to the next specialized skill only after the core foundation is stable.
Guardrails
Prefer official Android and Kotlin guidance over custom local conventions when they conflict.
Keep public APIs boring and explicit; avoid clever abstractions that hide Android lifecycle costs.
Do not mix architectural cleanup with product behavior changes unless the request explicitly needs both.
Document any compatibility constraints that will affect old modules or generated code.
Anti-Patterns
Sprinkling helpers across modules without a clear ownership boundary.
Introducing framework-specific code into pure domain or data layers.
Refactoring every adjacent file when only one contract needed to change.
Leaving migration notes implied instead of writing them down.
Remediation Examples
Inject dispatchers instead of hard-coding them
class TaskRepository(
    private val ioDispatcher: CoroutineDispatcher = Dispatchers.IO,
) {
    suspend fun refresh(): List<TaskUiModel> = withContext(ioDispatcher) { loadTasks() }
}

Collect flows with lifecycle awareness
viewLifecycleOwner.lifecycleScope.launch {
    viewLifecycleOwner.repeatOnLifecycle(Lifecycle.State.STARTED) {
        viewModel.uiState.collect { render(it) }
    }
}

Preserve cancellation in generic error handling
try {
    repository.refresh()
} catch (error: CancellationException) {
    throw error
} catch (error: Exception) {
    emit(UiState.Error(error))
}

Examples
Happy path
Scenario: Model task updates as StateFlow and shared event channels in the Compose fixture.
Command: cd examples/orbittasks-compose && ./gradlew :app:testDebugUnitTest
Edge case
Scenario: Recover from cancellation and configuration changes in the XML activity flow.
Command: cd examples/orbittasks-xml && ./gradlew :app:testDebugUnitTest
Failure recovery
Scenario: Disambiguate coroutine requests from state-management and WorkManager prompts.
Command: python3 scripts/eval_triggers.py --skill android-coroutines-flow
Done Checklist
The implementation path is explicit, minimal, and tied to the right Android surface.
Relevant example commands and benchmark prompts have been exercised or updated.
Handoffs to adjacent skills are documented when the request crosses boundaries.
Official references cover the chosen pattern and the main migration or troubleshooting path.
Official References
https://developer.android.com/kotlin/coroutines
https://developer.android.com/topic/libraries/architecture/coroutines
https://kotlinlang.org/docs/coroutines-overview.html
https://kotlinlang.org/docs/flow.html
Weekly Installs
177
Repository
krutikjain/andr…t-skills
GitHub Stars
5
First Seen
Mar 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass