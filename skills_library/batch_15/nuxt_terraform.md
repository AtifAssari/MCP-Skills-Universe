---
title: nuxt-terraform
url: https://skills.sh/ralphcrisostomo/nuxt-development-skills/nuxt-terraform
---

# nuxt-terraform

skills/ralphcrisostomo/nuxt-development-skills/nuxt-terraform
nuxt-terraform
Installation
$ npx skills add https://github.com/ralphcrisostomo/nuxt-development-skills --skill nuxt-terraform
SKILL.md
Nuxt + Terraform Scaffold Skill

Generate files for Nuxt + AWS infrastructure projects. This skill replaces the CLI — generate all files directly.

Style Guide

All generated Terraform code follows HashiCorp's official style conventions. Read references/terraform-style-guide.md for formatting rules, naming conventions, file organization, security best practices, and the code review checklist. Apply these conventions to all .tf files produced by any command below.

Pre-Requisites

Read terraform-scaffold.config.ts for functionPrefix (PascalCase), environments, and custom paths. If no config exists, ask the user for these values.

Naming Conventions
Concept	Convention	Example
Function prefix	PascalCase	MyApp
Full Lambda name	<prefix><PascalSuffix>	MyAppRedeemNow
Resolver name	camelCase	productById
GraphQL constant	SCREAMING_SNAKE_CASE	PRODUCT_BY_ID
TF module name	appsync_function_<camelName>	appsync_function_productById
TF lambda module	lambda_function_<camelName>	lambda_function_productById
Composable file	use<Model>.ts	useProduct.ts
GraphQL file	<model>.ts (lcfirst)	product.ts
TF file per model	<model>.tf (lcfirst)	product.tf
DynamoDB datasource	appsync_datasource_<modelLower>	appsync_datasource_product
DynamoDB table	dynamodb_<modelLower>s	dynamodb_products
Query index	by<Field>	byUserId

String conversions: toScreamingSnake splits on uppercase, joins with _, uppercases. toPascal capitalizes first letter. lcfirst lowercases first letter.

Command 1: Init

Ask user for: project name, function prefix (PascalCase), AWS profile, AWS region (default: ap-southeast-2), S3 state bucket, DynamoDB lock table.

AWS Profile Selection: Parse ~/.aws/credentials and ~/.aws/config for profile names. Present numbered list. Allow "add new" via aws configure --profile <name>.

Read references/init-workflow.md for directory structure, template placeholders, static files, scripts, and package.json entries. Consult references/terraform-modules.md for all 18 reusable module signatures.

Command 2: GraphQL Resolver

Ask user for:

Model name — @model type from schema.graphql (PascalCase)
Resolver type — query or mutation
Resolver name — camelCase (e.g. productById)
Runtime — APPSYNC_JS or LAMBDA
DynamoDB operation (APPSYNC_JS only) — GetItem, Query, PutItem, UpdateItem, Scan, BatchDeleteItem
Fields — model fields as arguments + optional extras (payload: AWSJSON, filter: AWSJSON, limit: Int, nextToken: String)

For advanced APPSYNC_JS resolver patterns (filters, conditions, batch operations, non-DynamoDB data sources), use the aws-appsync-resolver skill.

Read references/resolver-workflow.md for all generation templates: schema injection, GraphQL constant, Terraform modules (APPSYNC_JS and LAMBDA), dependency modules, AppSync JS functions, Lambda source, and composable generation.

Command 3: Lambda Function

Ask user for:

Name — PascalCase suffix (e.g. RedeemNow)
Type — standard or cron
Schedule (cron only) — EventBridge expression (e.g. rate(5 minutes))

Read references/lambda-workflow.md for Lambda source files, TF module block, cron resources, and dependency checks.

Command 4: Terraform Test

Generate .tftest.hcl test files for Terraform modules. Ask user for:

Module path — which module to test (e.g. ./modules/dynamodb_table)
Test type — unit (plan mode, fast), integration (apply mode, creates resources), or mock (plan mode with mock providers, no credentials needed)
Scenarios — what behaviors to validate (defaults, edge cases, validation rules)

Read references/terraform-test.md for test file structure, run block syntax, assert patterns, mock provider setup, expect_failures, parallel execution, and CI/CD integration examples.

Generated artifacts:

Test file in terraform/modules/<module>/tests/<name>_<type>_test.tftest.hcl
Mock provider blocks when test type is mock

Naming convention: <description>_unit_test.tftest.hcl, <description>_integration_test.tftest.hcl, <description>_mock_test.tftest.hcl

Rules

Idempotency — never overwrite existing files during init. Skip if TF module, schema field, GraphQL constant, composable function, or Lambda source already exists. When appending, trim trailing whitespace and add newline before new content.

Pre-generation checklist:

Read terraform-scaffold.config.ts for functionPrefix
Read schema.graphql for existing models and fields
Check TF files, graphql/ files, and composables for duplicates
Follow exact naming conventions from the table above
Verify module dependencies exist; generate if missing (see resolver-workflow.md dependency modules section)

Style compliance: All generated .tf files follow the conventions in references/terraform-style-guide.md — two-space indent, aligned equals signs, meta-arguments first, variables with type+description, descriptive resource names, security hardening defaults.

Post-generation validation: Run terraform fmt on modified .tf files, then terraform validate. If providers not initialized, skip and inform user to run terraform init first. For test files, run terraform test to verify tests pass.

Weekly Installs
32
Repository
ralphcrisostomo…t-skills
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass