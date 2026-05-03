---
title: workflow-local-dev
url: https://skills.sh/lgariv-dn/frontend-skills/workflow-local-dev
---

# workflow-local-dev

skills/lgariv-dn/frontend-skills/workflow-local-dev
workflow-local-dev
Installation
$ npx skills add https://github.com/lgariv-dn/frontend-skills --skill workflow-local-dev
SKILL.md
Workflow Local Development
Quick Reference
Key Commands
Task	Command
Check pods	kubectl get pods --context kind-kind
Restart component	tilt trigger workflow-<service>
View component logs	tilt logs workflow-<service>
Locally Deployed Components

These workflow services are deployed locally as shared dependencies: workflow-catalog, workflow-executions-api, workflow-engine-worker, workflow-consumer, workflow-validator, workflows-worker, standalone-tasks-worker

Utility Scripts

Execute these scripts for common operations:

Check Pod Status
bash .cursor/skills/workflow-local-dev/scripts/check-pods.sh

Restart a Service
bash .cursor/skills/workflow-local-dev/scripts/restart-service.sh <service-name>
# Example: bash .cursor/skills/workflow-local-dev/scripts/restart-service.sh catalog

Tail Service Logs
bash .cursor/skills/workflow-local-dev/scripts/tail-logs.sh <service-name>
# Example: bash .cursor/skills/workflow-local-dev/scripts/tail-logs.sh executions-api

Query Database
bash .cursor/skills/workflow-local-dev/scripts/db-query.sh "<SQL query>"
# Example: bash .cursor/skills/workflow-local-dev/scripts/db-query.sh "SELECT * FROM workflow_engine.workflows ORDER BY created_at DESC LIMIT 5"

Development Workflow

Use this flow primarily when containers fail locally or when you need to debug runtime behavior.

Capture current status: kubectl get pods --context kind-kind
Rebuild/restart component: tilt trigger workflow-<service>
Watch logs or health: kubectl logs -f <pod> --context kind-kind
Inspect configuration or data (if needed): bash .cursor/skills/workflow-local-dev/scripts/db-query.sh "<SQL query>"
Troubleshooting
Pod Issues
kubectl get pods --context kind-kind
kubectl describe pod <pod-name> --context kind-kind
kubectl logs -f <pod-name> --context kind-kind

Temporal Workflows

Open http://localhost:8081 (Temporal UI) and search by workflow ID.

Database State
# Use the db-query script (runs psql inside the postgres pod)
bash .cursor/skills/workflow-local-dev/scripts/db-query.sh "SELECT * FROM workflow_engine.workflows ORDER BY created_at DESC LIMIT 5"

Pulsar Messages
pulsar-admin topics stats persistent://public/dap/<topic>
pulsar-client consume persistent://public/dap/<topic> -s test-sub -n 10

Using Kubernetes MCP (When Available)

If the Kubernetes MCP server is enabled, you can use MCP tools instead of shell commands for a more integrated experience. The MCP defaults to the kind-kind context.

List Pods
Tool: pods_list
Arguments: { "labelSelector": "app=workflow-catalog" }


Or list all pods:

Tool: pods_list
Arguments: {}

Get Pod Logs
Tool: pods_log
Arguments: {
  "name": "workflow-catalog-xxxxx",
  "namespace": "default",
  "tail": 100
}


For previous container logs (after crash):

Tool: pods_log
Arguments: {
  "name": "workflow-catalog-xxxxx",
  "namespace": "default",
  "previous": true
}

Execute Commands in Pods (e.g., Database Queries)
Tool: pods_exec
Arguments: {
  "name": "postgres-xxxxx",
  "namespace": "default",
  "command": ["psql", "-U", "postgres", "-d", "temporal", "-c", "SELECT * FROM workflow_engine.workflows ORDER BY created_at DESC LIMIT 5"]
}

Delete Pod (Force Restart)
Tool: pods_delete
Arguments: {
  "name": "workflow-catalog-xxxxx",
  "namespace": "default"
}

Get Pod Details
Tool: pods_get
Arguments: {
  "name": "workflow-catalog-xxxxx",
  "namespace": "default"
}

List Cluster Events (Troubleshooting)
Tool: events_list
Arguments: { "namespace": "default" }


Note: When using MCP tools, you don't need to specify context as it defaults to kind-kind. The MCP approach is useful when you want the agent to directly interact with the cluster without spawning shell processes.

Additional Resources
For complete service URLs and infrastructure details, see reference.md
Weekly Installs
18
Repository
lgariv-dn/front…d-skills
GitHub Stars
1
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass