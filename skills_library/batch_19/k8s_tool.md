---
title: k8s-tool
url: https://skills.sh/blogic-cz/agent-tools/k8s-tool
---

# k8s-tool

skills/blogic-cz/agent-tools/k8s-tool
k8s-tool
Installation
$ npx skills add https://github.com/blogic-cz/agent-tools --skill k8s-tool
SKILL.md
k8s-tool (Kubernetes)

Kubernetes tool — kubectl wrapper with config-driven context resolution and structured commands. Part of @blogic-cz/agent-tools.

How to Run

Run via bun k8s-tool (requires @blogic-cz/agent-tools as a dev dependency). NEVER run bare kubectl — the credential guard will block it. Auth: existing kubectl context (kubeconfig). Cluster ID from config resolves context automatically.

Commands
bun k8s-tool kubectl --env test --cmd "get pods -n test-ns"
bun k8s-tool kubectl --env prod --cmd "logs <pod> --tail=100"
bun k8s-tool kubectl --env test --cmd "describe pod <pod>"
bun k8s-tool pods --env test                     # List pods (structured)
bun k8s-tool logs --pod <pod> --env test --tail 50 # Fetch logs
bun k8s-tool describe --resource pod --name <pod> --env test
bun k8s-tool exec --pod <pod> --exec-cmd "ls -la" --env test
bun k8s-tool top --env test                      # Show resource usage


Environment is any string (e.g. test, prod). Set defaultEnvironment in agent-tools.json5 to skip --env on every call. Implicit production access is blocked for safety.

Tips
Use --help on any subcommand for full options.
Error responses include hint, nextCommand, and retryable fields — always check them on failure.
Prefer CLI tool over MCP tools — more efficient, doesn't load extra context.
Weekly Installs
8
Repository
blogic-cz/agent-tools
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass