---
title: zcl
url: https://skills.sh/marcohefti/zero-context-lab/zcl
---

# zcl

skills/marcohefti/zero-context-lab/zcl
zcl
Installation
$ npx skills add https://github.com/marcohefti/zero-context-lab --skill zcl
SKILL.md
ZCL Orchestrator (Codex Skill)

This skill is for the orchestrator (you), not the spawned mission agent.

Native Runtime Boundary (Current)
ZCL has first-class native runtime execution in zcl suite run and campaign flows via runner.type=codex_app_server.
Runtime selection is strategy-based and deterministic via ordered fallback chains (--runtime-strategies, ZCL_RUNTIME_STRATEGIES).
Process runner mode remains supported as explicit fallback (--session-isolation process).
Native runtime strategy health/failure classes are typed and surfaced in artifacts/JSON outputs.
Capability Matrix
Capability	Implemented	Enforced	Notes
Native suite execution (--session-isolation native)	yes	yes	suite run forbids process runner command in native mode.
Runtime strategy fallback chain	yes	yes	Ordered strategy IDs, capability checks, typed per-strategy failures.
Native campaign runner (runner.type=codex_app_server)	yes	yes	No per-flow runner.command required.
Native event trace mapping (tool=native)	yes	yes	Redaction + bounds + integrity flags preserved.
Mission-only result-channel finalization	yes	yes	3-turn workflows via minResultTurn.
Provider onboarding structure	yes	partial	provider_stub demonstrates unsupported-capability behavior.
Runtime failure taxonomy (auth/rate-limit/stream/crash/listener/stall)	yes	yes	Typed ZCL_E_RUNTIME_* codes in summaries + feedback failure payloads.

Primary evidence:

.zcl/.../tool.calls.jsonl
.zcl/.../feedback.json
Operator Invocation Story

When asked to "run this through ZCL", use this order:

zcl init
Optional preflight:
zcl update status --json
zcl doctor --json
Optional single-attempt allocation path:
zcl attempt start --suite <suiteId> --mission <missionId> --prompt <text> --isolation-model native_spawn --json
Preferred native suite path:
zcl suite run --file <suite.(yaml|yml|json)> --session-isolation native --runtime-strategies codex_app_server --feedback-policy auto_fail --finalization-mode auto_from_result_json --result-channel file_json --result-min-turn 3 --campaign-id <campaignId> --progress-jsonl <path|-> --json
Process fallback path:
zcl suite run --file <suite.(yaml|yml|json)> --session-isolation process --feedback-policy auto_fail --finalization-mode auto_from_result_json --result-channel file_json --result-min-turn 3 --campaign-id <campaignId> --progress-jsonl <path|-> --shim tool-cli --json -- <runner-cmd> [args...]
First-class campaign path:
zcl campaign lint --spec <campaign.(yaml|yml|json)> --json
zcl campaign canary --spec <campaign.(yaml|yml|json)> --missions 3 --json
zcl campaign run --spec <campaign.(yaml|yml|json)> --json
zcl campaign resume --campaign-id <id> --json
zcl campaign status --campaign-id <id> --json
zcl campaign report --campaign-id <id> --allow-invalid --json
zcl campaign publish-check --campaign-id <id> --json
Validate/report from artifacts:
zcl report --strict <attemptDir|runDir>
zcl validate --strict <attemptDir|runDir>
zcl attempt explain --json <attemptDir>

Explicit finalization path for harness-aware prompts:

zcl feedback --ok --result <text> or zcl feedback --fail --result-json <json>
Operator Guardrails
Native suite attempts now anchor timeout windows before native turn execution; stalled native attempts classify as ZCL_E_RUNTIME_STALL.
Native suite orchestration now guarantees terminal artifacts on failure paths (feedback.json + best-effort attempt.report.json) for post-mortem continuity.
Campaign read/report/resume commands fail fast with ZCL_E_CAMPAIGN_STATE_DRIFT when persisted campaign.run.state.json disagrees with current spec mission selection (for example totalMissions=0 on a non-empty selection).
For CI/automation, prefer zcl campaign report --allow-invalid --json to collect report payloads without branching on process exit codes; keep zcl campaign publish-check as the strict publish gate.
Campaign Guidance

Recommended native Codex flow:

flows:
  - flowId: codex-native
    runner:
      type: codex_app_server
      sessionIsolation: native
      runtimeStrategies: ["codex_app_server"]
      feedbackPolicy: auto_fail
      freshAgentPerAttempt: true


Mission-only recommended variant:

promptMode: mission_only
flows:
  - flowId: codex-native
    runner:
      type: codex_app_server
      sessionIsolation: native
      runtimeStrategies: ["codex_app_server"]
      finalization:
        mode: auto_from_result_json
        minResultTurn: 3
        resultChannel:
          kind: file_json
          path: mission.result.json

Prompt Policy

Use exactly one mode per campaign:

promptMode: mission_only (preferred): mission intent + output contract only; no harness terms.
promptMode: default: harness-aware prompts permitted.
Native Recommendation Criteria (Measured)

Codex native runtime is recommended when both hold in CI/nightly checks:

Reliability: native 20-attempt parallel smoke run success rate >= 95%.
Throughput: same run completes in <= 30 seconds on CI worker baseline.

Guard test path:

internal/interfaces/cli/suite_run_integration_test.go (TestSuiteRun_NativeParallelUniqueSessions, TestSuiteRun_NativeSchedulerRateLimitIsDeterministic).
Templates
examples/campaign.canonical.yaml
examples/campaign.no-context.comparison.yaml
examples/campaign.no-context.codex-exec.yaml
examples/campaign.no-context.codex-subagent.yaml
examples/campaign.no-context.claude-subagent.yaml
examples/campaign.native.codex.minimal.yaml
examples/campaign.native.codex.advanced.yaml
docs/migration/shell-adapter-to-native-codex.md
Weekly Installs
101
Repository
marcohefti/zero…text-lab
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass