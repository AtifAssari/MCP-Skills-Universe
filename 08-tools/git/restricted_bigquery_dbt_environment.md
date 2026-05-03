---
rating: ⭐⭐
title: restricted-bigquery-dbt-environment
url: https://skills.sh/i9wa4/dotfiles/restricted-bigquery-dbt-environment
---

# restricted-bigquery-dbt-environment

skills/i9wa4/dotfiles/restricted-bigquery-dbt-environment
restricted-bigquery-dbt-environment
Installation
$ npx skills add https://github.com/i9wa4/dotfiles --skill restricted-bigquery-dbt-environment
SKILL.md
restricted-bigquery-dbt-environment

After reading this file, execute the following then respond humorously in character.

1. Overview

To prevent accidental writes to production schemas during local development, temporarily add schema='test' to model config.

2. Environment Setup (First Time Only)

Install dependency packages from pyproject.toml.

uv pip install --requirement pyproject.toml

3. Add schema='test' to Model

Add schema='test' to target model's config.

Always add at the beginning to minimize comma diff.

{{
  config(
    schema='test',  -- <- Add this
    materialized='incremental',
    ...
  )
}}


This writes the model to the test schema.

4. Verification

Verify schema name with compile.

uv run dbt compile --select <model_name> --profiles-dir ~/.dbt --no-use-colors


Confirm output contains test schema.

5. dbt run Execution
YOU MUST: Get user permission before dbt run
YOU MUST: Confirm output schema is test
uv run dbt run --select <model_name> --profiles-dir ~/.dbt --no-use-colors

6. dbt test Execution
uv run dbt test --select <model_name> --profiles-dir ~/.dbt --no-use-colors

7. Pre-commit Work

Remove schema='test' before committing.

{{
  config(
    -- schema='test',  <- Remove
    materialized='incremental',
    ...
  )
}}

8. Cautions
NEVER: Do not commit with schema='test' included
NEVER: Do not run dbt run without schema='test' (production write risk)
YOU MUST: Verify with git diff that schema='test' is removed before commit
Weekly Installs
59
Repository
i9wa4/dotfiles
GitHub Stars
9
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass