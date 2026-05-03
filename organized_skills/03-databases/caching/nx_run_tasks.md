---
rating: ⭐⭐
title: nx-run-tasks
url: https://skills.sh/nrwl/nx-ai-agents-config/nx-run-tasks
---

# nx-run-tasks

skills/nrwl/nx-ai-agents-config/nx-run-tasks
nx-run-tasks
Installation
$ npx skills add https://github.com/nrwl/nx-ai-agents-config --skill nx-run-tasks
Summary

Execute build, test, lint, serve, and other Nx workspace tasks with flexible filtering and caching.

Run single tasks with nx run <project>:<task> or multiple tasks across projects using nx run-many with project filtering by name, pattern, or tag
Use nx affected to run tasks only on changed projects and their dependents, ideal for CI pipelines and large workspaces
Control execution with flags like --parallel, --skipNxCache, --nxBail, and --configuration to customize behavior
Automatically detects available tasks from project.json, package.json scripts, and Nx plugin inferred tasks via nx show project
SKILL.md

You can run tasks with Nx in the following way.

Keep in mind that you might have to prefix things with npx/pnpx/yarn if the user doesn't have nx installed globally. Look at the package.json or lockfile to determine which package manager is in use.

For more details on any command, run it with --help (e.g. nx run-many --help, nx affected --help).

Understand which tasks can be run

You can check those via nx show project <projectname> --json, for example nx show project myapp --json. It contains a targets section which has information about targets that can be run. You can also just look at the package.json scripts or project.json targets, but you might miss out on inferred tasks by Nx plugins.

Run a single task
nx run <project>:<task>


where project is the project name defined in package.json or project.json (if present).

Run multiple tasks
nx run-many -t build test lint typecheck


You can pass a -p flag to filter to specific projects, otherwise it runs on all projects. You can also use --exclude to exclude projects, and --parallel to control the number of parallel processes (default is 3).

Examples:

nx run-many -t test -p proj1 proj2 — test specific projects
nx run-many -t test --projects=*-app --exclude=excluded-app — test projects matching a pattern
nx run-many -t test --projects=tag:api-* — test projects by tag
Run tasks for affected projects

Use nx affected to only run tasks on projects that have been changed and projects that depend on changed projects. This is especially useful in CI and for large workspaces.

nx affected -t build test lint


By default it compares against the base branch. You can customize this:

nx affected -t test --base=main --head=HEAD — compare against a specific base and head
nx affected -t test --files=libs/mylib/src/index.ts — specify changed files directly
Useful flags

These flags work with run, run-many, and affected:

--skipNxCache — rerun tasks even when results are cached
--verbose — print additional information such as stack traces
--nxBail — stop execution after the first failed task
--configuration=<name> — use a specific configuration (e.g. production)
Weekly Installs
1.6K
Repository
nrwl/nx-ai-agents-config
GitHub Stars
19
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass