---
title: dagu-webui
url: https://skills.sh/vinnie357/claude-skills/dagu-webui
---

# dagu-webui

skills/vinnie357/claude-skills/dagu-webui
dagu-webui
Installation
$ npx skills add https://github.com/vinnie357/claude-skills --skill dagu-webui
SKILL.md
Dagu Web UI

Use this skill when working with Dagu's web interface to manage workflows, view execution history, monitor running workflows, or configure the UI.

When to Use This Skill

Activate when:

Navigating the Dagu web interface
Starting, stopping, or retrying workflows via UI
Viewing workflow execution logs and status
Monitoring running workflows
Managing workflow history
Configuring workflow schedules through the UI
Troubleshooting workflow issues using the UI
Core Capabilities

The Dagu Web UI provides:

Workflow Management - View, start, stop, and manage workflows
Execution Monitoring - Real-time status and logs
History Viewing - Past execution records and results
DAG Visualization - Visual representation of workflow structure
Log Access - View detailed execution logs
Schedule Management - Configure when workflows run
Quick Start

Access Dagu Web UI at http://localhost:8080 (default) after starting Dagu:

dagu server

Primary Operations
Start a Workflow

To manually execute a workflow:

Navigate to workflow list
Click the workflow name
Click "Start" button
View real-time execution progress
Monitor Execution

For detailed information on a running workflow, consult references/monitoring.md which covers:

Reading execution logs
Understanding status indicators
Tracking step progress
Identifying failures
View History

To review past executions, see references/history.md for guidance on:

Filtering execution history
Analyzing failed runs
Comparing execution times
Exporting execution data
Workflow Visualization

The DAG view shows workflow structure. For detailed visualization features, see references/visualization.md.

When to Consult References
Detailed UI navigation: Read references/ui-navigation.md
Advanced monitoring: Read references/monitoring.md
History analysis: Read references/history.md
Workflow editing via UI: Read references/workflow-editor.md
Configuration options: Read references/configuration.md
Common Tasks
Restart a Failed Workflow
Find the failed execution in history
Click the retry/restart button
Monitor the new execution
Stop a Running Workflow
Navigate to the running workflow
Click "Stop" or "Cancel"
Confirm the action
View cleanup handlers execution
View Detailed Logs

When you need to debug a workflow:

Click on the specific workflow execution
Select the step with issues
View stdout/stderr logs
Check for error messages

For advanced log analysis, consult references/monitoring.md.

Key Principles
Real-time visibility: Web UI provides live updates of workflow execution
Click-based operations: No CLI needed for basic workflow management
History preservation: All executions are logged and accessible
Visual feedback: Status indicators show current state at a glance
Log accessibility: Detailed logs available for debugging
Pro Tips
Use the search feature to quickly find workflows by name
Filter execution history by date range or status
Click on step names in DAG view for step-specific details
Use the refresh button if live updates seem delayed
Check the scheduler status to verify cron jobs are active
Weekly Installs
8
Repository
vinnie357/claude-skills
GitHub Stars
17
First Seen
Feb 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass