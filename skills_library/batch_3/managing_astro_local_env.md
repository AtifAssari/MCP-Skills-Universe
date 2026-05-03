---
title: managing-astro-local-env
url: https://skills.sh/astronomer/agents/managing-astro-local-env
---

# managing-astro-local-env

skills/astronomer/agents/managing-astro-local-env
managing-astro-local-env
Installation
$ npx skills add https://github.com/astronomer/agents --skill managing-astro-local-env
Summary

Manage local Airflow development environment with Astro CLI commands.

Start, stop, restart, and kill local Airflow containers; default credentials are admin/admin with webserver at http://localhost:8080
View logs for all components or specific services (scheduler, webserver) with real-time follow option
Access container shells and run Airflow CLI commands directly via astro dev bash and astro dev run
Troubleshoot common issues including port conflicts, startup failures, package errors, and DAG parsing problems with quick reset procedures
Upgrade Airflow versions by editing the Dockerfile and testing compatibility before applying changes
SKILL.md
Astro Local Environment

This skill helps you manage your local Airflow environment using the Astro CLI.

Two modes: Docker (default, uses containers) and Standalone (Docker-free, uses a local venv — requires Airflow 3 + uv).

To set up a new project, see the setting-up-astro-project skill. When Airflow is running, use MCP tools from authoring-dags and testing-dags skills.

Start / Stop / Restart (Docker)
# Start local Airflow (webserver at http://localhost:8080)
astro dev start

# Stop containers (preserves data)
astro dev stop

# Kill and remove volumes (clean slate)
astro dev kill

# Restart all containers
astro dev restart

# Restart specific component
astro dev restart --scheduler
astro dev restart --webserver


Default credentials: admin / admin

Restart after modifying: requirements.txt, packages.txt, Dockerfile

Standalone mode? See the next section.

Standalone Mode

Docker-free local development. Runs Airflow directly on your machine in a .venv/ managed by uv.

Requirements: Airflow 3 (runtime 3.x), uv on PATH. Not supported on Windows.

Start
# One-time: set standalone as default mode
astro config set dev.mode standalone

# Or use the flag per invocation
astro dev start --standalone

Flag	Description
--foreground / -f	Stream output in foreground
--port / -p	Override webserver port (default: 8080)
--no-proxy	Disable reverse proxy
Stop / Kill / Restart
# Stop (preserves .venv)
astro dev stop

# Kill (removes .venv and .astro/standalone/ — clean slate)
astro dev kill

# Restart (preserves .venv for fast restart, use -k to kill first)
astro dev restart


If you used --standalone on start instead of setting the config, pass --standalone on every subsequent command too (stop, kill, restart, bash, run, logs, etc.).

State locations: venv in .venv/, database and logs in .astro/standalone/, DAGs from dags/.

Reverse Proxy

Run multiple Airflow projects locally without port conflicts. Works in both Docker and standalone modes.

Each project gets a hostname like <project-name>.localhost:6563. Visit http://localhost:6563 to see all active projects.

# Check proxy status and active routes
astro dev proxy status

# Force-stop proxy (auto-restarts on next astro dev start)
astro dev proxy stop

Config	Command
Change proxy port	astro config set proxy.port <port>
Disable per-start	astro dev start --no-proxy

Default proxy port: 6563

Check Status
astro dev ps

View Logs
# All logs
astro dev logs

# Specific component
astro dev logs --scheduler
astro dev logs --webserver

# Follow in real-time
astro dev logs -f


Standalone: astro dev logs works the same but shows a unified log (no per-component filtering).

Run Airflow CLI Commands
# Open a shell with Airflow environment
astro dev bash

# Run Airflow CLI commands
astro dev run airflow info
astro dev run airflow dags list


Standalone: Same commands work — bash opens a venv-activated shell, run executes in the venv.

Querying the Airflow API

Use astro api airflow to query a running local Airflow instance. Prefer operation IDs over URL paths.

Defaults: localhost:8080, admin/admin (auto-detected). Override with --api-url, --username, --password.

Discovery
# List all endpoints
astro api airflow ls

# Filter by keyword
astro api airflow ls dags
astro api airflow ls task

# Show params and schema for an operation
astro api airflow describe get_dag

Key Flags
Flag	Purpose
-p key=value	Path parameters
-F key=value	Body/query fields (auto-converts booleans/numbers)
-q / --jq	jq filter on response
--paginate	Fetch all pages
-X / --method	Override HTTP method
--generate	Output curl command instead of executing
DAGs
# List all DAGs
astro api airflow get_dags

# Filter by pattern (SQL LIKE — use % wildcards)
astro api airflow get_dags -F dag_id_pattern=%etl%

# Get a specific DAG
astro api airflow get_dag -p dag_id=my_dag

# Get full details (schedule, params, etc.)
astro api airflow get_dag_details -p dag_id=my_dag

# Pause / unpause
astro api airflow patch_dag -p dag_id=my_dag -F is_paused=true
astro api airflow patch_dag -p dag_id=my_dag -F is_paused=false

# View DAG source code
astro api airflow get_dag_source -p dag_id=my_dag

# Check import errors
astro api airflow get_import_errors

DAG Runs
# List runs for a DAG
astro api airflow get_dag_runs -p dag_id=my_dag

# Trigger a run
astro api airflow trigger_dag_run -p dag_id=my_dag

# Trigger with config
astro api airflow trigger_dag_run -p dag_id=my_dag -F conf[key]=value

# Get a specific run
astro api airflow get_dag_run -p dag_id=my_dag -p dag_run_id=manual__2026-04-07

# Clear (re-run) a DAG run
astro api airflow clear_dag_run -p dag_id=my_dag -p dag_run_id=manual__2026-04-07 -F dry_run=false

Task Instances
# List task instances for a run
astro api airflow get_task_instances -p dag_id=my_dag -p dag_run_id=manual__2026-04-07

# Use ~ as wildcard (all DAGs or all runs)
astro api airflow get_task_instances -p dag_id=my_dag -p dag_run_id=~

# Get a specific task instance
astro api airflow get_task_instance -p dag_id=my_dag -p dag_run_id=manual__2026-04-07 -p task_id=extract

# Clear/retry failed tasks
astro api airflow post_clear_task_instances -p dag_id=my_dag \
  -F dag_run_id=manual__2026-04-07 -F only_failed=true -F dry_run=false

# Get task logs
astro api airflow get_log -p dag_id=my_dag -p dag_run_id=manual__2026-04-07 \
  -p task_id=extract -p try_number=1

Config & Connections
astro api airflow get_connections
astro api airflow get_variables
astro api airflow get_config

Filtering with jq
# List only DAG IDs
astro api airflow get_dags -q '.dags[].dag_id'

# Get failed task IDs from a run
astro api airflow get_task_instances -p dag_id=my_dag -p dag_run_id=~ \
  -q '[.task_instances[] | select(.state=="failed") | .task_id]'

Troubleshooting
Issue	Solution
Port 8080 in use	Stop other containers or edit .astro/config.yaml
Container won't start	astro dev kill then astro dev start
Package install failed	Check requirements.txt syntax
DAG not appearing	Run astro dev parse to check for import errors
Out of disk space	docker system prune
Standalone won't start	Ensure uv is on PATH and runtime is 3.x
Proxy port conflict	astro config set proxy.port <port>
.venv corrupted	astro dev kill then astro dev start --standalone
Reset Environment

When things are broken:

astro dev kill
astro dev start

Upgrade Airflow
Test compatibility first
astro dev upgrade-test

Change version

Edit Dockerfile:

FROM quay.io/astronomer/astro-runtime:13.0.0


Restart:

astro dev kill && astro dev start

Related Skills
setting-up-astro-project: Initialize projects and configure dependencies
authoring-dags: Write DAGs (uses MCP tools, requires running Airflow)
testing-dags: Test DAGs (uses MCP tools, requires running Airflow)
deploying-airflow: Deploy DAGs to production (Astro, Docker Compose, Kubernetes)
Weekly Installs
618
Repository
astronomer/agents
GitHub Stars
354
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn