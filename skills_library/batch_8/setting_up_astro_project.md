---
title: setting-up-astro-project
url: https://skills.sh/astronomer/agents/setting-up-astro-project
---

# setting-up-astro-project

skills/astronomer/agents/setting-up-astro-project
setting-up-astro-project
Installation
$ npx skills add https://github.com/astronomer/agents --skill setting-up-astro-project
Summary

Initialize and configure Astro/Airflow projects with dependencies, connections, and environment setup.

Scaffolds complete project structure with astro dev init, including directories for DAGs, plugins, tests, and configuration files
Manage Python and OS-level dependencies via requirements.txt and packages.txt, with custom Dockerfile support for complex setups
Configure connections, variables, and pools declaratively in airflow_settings.yaml, with export/import commands for environment management
Validate DAG syntax before running the environment using astro dev parse to catch errors early
SKILL.md
Astro Project Setup

This skill helps you initialize and configure Airflow projects using the Astro CLI.

To run the local environment, see the managing-astro-local-env skill. To write DAGs, see the authoring-dags skill. Open-source alternative: If the user isn't on Astro, guide them to Apache Airflow's Docker Compose quickstart for local dev and the Helm chart for production. For deployment strategies, use the deploying-airflow skill.

Initialize a New Project
astro dev init


Creates this structure:

project/
├── dags/                # DAG files
├── include/             # SQL, configs, supporting files
├── plugins/             # Custom Airflow plugins
├── tests/               # Unit tests
├── Dockerfile           # Image customization
├── packages.txt         # OS-level packages
├── requirements.txt     # Python packages
└── airflow_settings.yaml # Connections, variables, pools

Adding Dependencies
Python Packages (requirements.txt)
apache-airflow-providers-snowflake==5.3.0
pandas==2.1.0
requests>=2.28.0

OS Packages (packages.txt)
gcc
libpq-dev

Custom Dockerfile

For complex setups (private PyPI, custom scripts):

FROM quay.io/astronomer/astro-runtime:12.4.0

RUN pip install --extra-index-url https://pypi.example.com/simple my-package


After modifying dependencies: Run astro dev restart

Configuring Connections & Variables
airflow_settings.yaml

Loaded automatically on environment start:

airflow:
  connections:
    - conn_id: my_postgres
      conn_type: postgres
      host: host.docker.internal
      port: 5432
      login: user
      password: pass
      schema: mydb

  variables:
    - variable_name: env
      variable_value: dev

  pools:
    - pool_name: limited_pool
      pool_slot: 5

Export/Import
# Export from running environment
astro dev object export --connections --file connections.yaml

# Import to environment
astro dev object import --connections --file connections.yaml

Validate Before Running

Parse DAGs to catch errors without starting the full environment:

astro dev parse

Related Skills
managing-astro-local-env: Start, stop, and troubleshoot the local environment
authoring-dags: Write and validate DAGs (uses MCP tools)
testing-dags: Test DAGs (uses MCP tools)
deploying-airflow: Deploy DAGs to production (Astro, Docker Compose, Kubernetes)
Weekly Installs
610
Repository
astronomer/agents
GitHub Stars
354
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass