---
title: ai-mlops
url: https://skills.sh/vasilyu1983/ai-agents-public/ai-mlops
---

# ai-mlops

skills/vasilyu1983/ai-agents-public/ai-mlops
ai-mlops
Installation
$ npx skills add https://github.com/vasilyu1983/ai-agents-public --skill ai-mlops
SKILL.md
MLOps & ML Security - Complete Reference (Jan 2026)

Production ML lifecycle with modern security practices.

This skill covers:

Production: Data ingestion, deployment, drift detection, monitoring, incident response
Security: Prompt injection, jailbreak defense, RAG security, output filtering
Governance: Privacy protection, supply chain security, safety evaluation
Data ingestion (dlt): Load data from APIs, databases to warehouses
Model deployment: Batch jobs, real-time APIs, hybrid systems, event-driven automation
Operations: Real-time monitoring, drift detection, automated retraining, incident response

Modern Best Practices (Jan 2026):

Version everything that can change: model artifacts, data snapshots, feature definitions, prompts/configs, and agent graphs; require reproducibility, rollbacks, and audit logs (NIST SSDF: https://csrc.nist.gov/pubs/sp/800/218/final).
Gate changes with evals (offline + online) and safe rollout (shadow/canary/blue-green); treat regressions in quality, safety, latency, and cost as release blockers.
Align controls and documentation to risk posture (EU AI Act: https://eur-lex.europa.eu/eli/reg/2024/1689/oj; NIST AI RMF + GenAI profile: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf, https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf).
Operationalize security: threat model the full system (data, model, prompts, tools, RAG), harden the supply chain (SBOM/signing), and ship incident playbooks for both reliability and safety events.

It is execution-focused:

Data ingestion patterns (REST APIs, database replication, incremental loading)
Deployment patterns (batch, online, hybrid, streaming, event-driven)
Automated monitoring with real-time drift detection
Automated retraining pipelines (monitor → detect → trigger → validate → deploy)
Incident handling with validated rollback and postmortems
Links to copy-paste templates in assets/
Quick Reference
Task	Tool/Framework	Command	When to Use
Data Ingestion	dlt (data load tool)	dlt pipeline run, dlt init	Loading from APIs, databases to warehouses
Batch Deployment	Airflow, Dagster, Prefect	airflow dags trigger, dagster job launch	Scheduled predictions on large datasets
API Deployment	FastAPI, Flask, TorchServe	uvicorn app:app, torchserve --start	Real-time inference (<500ms latency)
LLM Serving	vLLM, TGI, BentoML	vllm serve model, bentoml serve	High-throughput LLM inference
Model Registry	MLflow, W&B, ZenML	mlflow.register_model(), zenml model register	Versioning and promoting models
Drift Detection	Statistical tests + monitors	PSI/KS, embedding drift, prediction drift	Detect data/process changes and trigger review
Monitoring	Prometheus, Grafana	prometheus.yml, Grafana dashboards	Metrics, alerts, SLO tracking
AgentOps	AgentOps, Langfuse, LangSmith	agentops.init(), trace visualization	AI agent observability, session replay
Incident Response	Runbooks, PagerDuty	Documented playbooks, alert routing	Handling failures and degradation
Use This Skill When

Use this skill when the user asks for deployment, operations, monitoring, incident handling, or governance for ML/LLM/agent systems, e.g.:

"How do I deploy this model to prod?"
"Design a batch + online scoring architecture."
"Add monitoring and drift detection to our model."
"Write an incident runbook for this ML service."
"Package this LLM/RAG pipeline as an API."
"Plan our retraining and promotion workflow."
"Load data from Stripe API to Snowflake."
"Set up incremental database replication with dlt."
"Build an ELT pipeline for warehouse loading."

If the user is asking only about EDA, modelling, or theory, prefer:

ai-ml-data-science (EDA, features, modelling, SQL transformation with SQLMesh)
ai-llm (prompting, fine-tuning, eval)
ai-rag (retrieval pipeline design)
ai-llm-inference (compression, spec decode, serving internals)

If the user is asking about SQL transformation (after data is loaded), prefer:

ai-ml-data-science (SQLMesh templates for staging, intermediate, marts layers)
Decision Tree: Choosing Deployment Strategy
User needs to deploy: [ML System]
    ├─ Data Ingestion?
    │   ├─ From REST APIs? → dlt REST API templates
    │   ├─ From databases? → dlt database sources (PostgreSQL, MySQL, MongoDB)
    │   └─ Incremental loading? → dlt incremental patterns (timestamp, ID-based)
    │
    ├─ Model Serving?
    │   ├─ Latency <500ms? → FastAPI real-time API
    │   ├─ Batch predictions? → Airflow/Dagster batch pipeline
    │   └─ Mix of both? → Hybrid (batch features + online scoring)
    │
    ├─ Monitoring & Ops?
    │   ├─ Drift detection? → Evidently + automated retraining triggers
    │   ├─ Performance tracking? → Prometheus + Grafana dashboards
    │   └─ Incident response? → Runbooks + PagerDuty alerts
    │
    └─ LLM/RAG Production?
        ├─ Cost optimization? → Caching, prompt templates, token budgets
        └─ Safety? → See ai-mlops skill

Core Concepts (Vendor-Agnostic)
Lifecycle loop: train → validate → deploy → monitor → respond → retrain/retire.
Risk controls: access control, data minimization, logging, and change management (NIST AI RMF: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf).
Observability planes: system metrics (latency/errors), data metrics (freshness/drift), quality metrics (model performance).
Incident readiness: detection, containment, rollback, and root-cause analysis.
Do / Avoid

Do

Do gate deployments with repeatable checks: evaluation pass, load test, security review, rollback plan.
Do version everything: code, data, features, model artifact, prompt templates, configuration.
Do define SLOs and budgets (latency/cost/error rate) before optimizing.

Avoid

Avoid manual “clickops” deployments without audit trail.
Avoid silent upgrades; require eval + canary for model/prompt changes.
Avoid drift dashboards without actions; every alert needs an owner and runbook.
Core Patterns Overview

This skill provides production-ready patterns and guides organized into comprehensive references:

Data & Infrastructure Patterns

Pattern 0: Data Contracts, Ingestion & Lineage → See Data Ingestion Patterns

Data contracts with SLAs and versioning
Ingestion modes (CDC, batch, streaming)
Lineage tracking and schema evolution
Replay and backfill procedures

Pattern 1: Choose Deployment Mode → See Deployment Patterns

Decision table (batch, online, hybrid, streaming)
When to use each mode
Deployment mode selection checklist

Pattern 2: Standard Deployment Lifecycle → See Deployment Lifecycle

Pre-deploy, deploy, observe, operate, evolve phases
Environment promotion (dev → staging → prod)
Gradual rollout strategies (canary, blue-green)

Pattern 3: Packaging & Model Registry → See Model Registry Patterns

Model registry structure and metadata
Packaging strategies (Docker, ONNX, MLflow)
Promotion flows (experimental → production)
Versioning and governance
Serving Patterns

Pattern 4: Batch Scoring Pipeline → See Deployment Patterns

Orchestration with Airflow/Dagster
Idempotent scoring jobs
Validation and backfill procedures

Pattern 5: Real-Time API Scoring → See API Design Patterns

Service design (HTTP/JSON, gRPC)
Input/output schemas
Rate limiting, timeouts, circuit breakers

Pattern 6: Hybrid & Feature Store Integration → See Feature Store Patterns

Batch vs online features
Feature store architecture
Training-serving consistency
Point-in-time correctness
Operations Patterns

Pattern 7: Monitoring & Alerting → See Monitoring Best Practices

Data, performance, and technical metrics
SLO definition and tracking
Dashboard design and alerting strategies

Pattern 8: Drift Detection & Automated Retraining → See Drift Detection Guide

Automated retraining triggers
Event-driven retraining pipelines

Pattern 9: Incidents & Runbooks → See Incident Response Playbooks

Common failure modes
Detection, diagnosis, resolution
Post-mortem procedures

Pattern 10: LLM / RAG in Production → See LLM & RAG Production Patterns

Prompt and configuration management
Safety and compliance (PII, jailbreaks)
Cost optimization (token budgets, caching)
Monitoring and fallbacks

Pattern 11: Cross-Region, Residency & Rollback → See Multi-Region Patterns

Multi-region deployment architectures
Data residency and tenant isolation
Disaster recovery and failover
Regional rollback procedures

Pattern 12: Online Evaluation & Feedback Loops → See Online Evaluation Patterns

Feedback signal collection (implicit, explicit)
Shadow and canary deployments
A/B testing with statistical significance
Human-in-the-loop labeling
Automated retraining cadence

Pattern 13: AgentOps (AI Agent Operations) → See AgentOps Patterns

Session tracing and replay for AI agents
Cost and latency tracking across agent runs
Multi-agent visualization and debugging
Tool invocation monitoring
Integration with CrewAI, LangGraph, OpenAI Agents SDK

Pattern 14: Edge MLOps & TinyML → See Edge MLOps Patterns

Device-aware CI/CD pipelines
OTA model updates with rollback
Federated learning operations
Edge drift detection
Intermittent connectivity handling
Resources (Detailed Guides)

For comprehensive operational guides, see:

Core Infrastructure:

Data Ingestion Patterns - Data contracts, CDC, batch/streaming ingestion, lineage, schema evolution
Deployment Lifecycle - Pre-deploy validation, environment promotion, gradual rollout, rollback
Model Registry Patterns - Versioning, packaging, promotion workflows, governance
Feature Store Patterns - Batch/online features, hybrid architectures, consistency, latency optimization

Serving & APIs:

Deployment Patterns - Batch, online, hybrid, streaming deployment strategies and architectures
API Design Patterns - ML/LLM/RAG API patterns, input/output schemas, reliability patterns, versioning

Operations & Reliability:

Monitoring Best Practices - Metrics collection, alerting strategies, SLO definition, dashboard design
Drift Detection Guide - Statistical tests, automated detection, retraining triggers, recovery strategies
Incident Response Playbooks - Runbooks for common failure modes, diagnostics, resolution steps

Security & Governance:

Threat Models - Trust boundaries, attack surface, control mapping
Prompt Injection Mitigation - Input hardening, tool/RAG containment, least privilege
Jailbreak Defense - Robust refusal behavior, safe completion patterns
RAG Security - Retrieval poisoning, context injection, sensitive data leakage
Output Filtering - Layered filters (PII/toxicity/policy), block/rewrite strategies
Privacy Protection - PII handling, data minimization, retention, consent
Supply Chain Security - SBOM, dependency pinning, artifact signing
Safety Evaluation - Red teaming, eval sets, incident readiness

Advanced Patterns:

LLM & RAG Production Patterns - Prompt management, safety, cost optimization, caching, monitoring
Multi-Region Patterns - Multi-region deployment, data residency, disaster recovery, rollback
Online Evaluation Patterns - A/B testing, shadow deployments, feedback loops, automated retraining
AgentOps Patterns - AI agent observability, session replay, cost tracking, multi-agent debugging
Edge MLOps Patterns - TinyML, federated learning, OTA updates, device-aware CI/CD
Cost Management & FinOps - ML/LLM cost modeling, budget guardrails, chargeback, cloud optimization
Experiment Tracking Patterns - MLflow/W&B patterns, experiment organization, artifact management, team workflows
Automated Retraining Patterns - Trigger strategies, validation gates, safe rollout, canary retraining pipelines
Templates

Use these as copy-paste starting points for production artifacts:

Data Ingestion (dlt)

For loading data into warehouses and pipelines:

dlt basic pipeline setup - Install, configure, run basic extraction and loading
dlt REST API sources - Extract from REST APIs with pagination, authentication, rate limiting
dlt database sources - Replicate from PostgreSQL, MySQL, MongoDB, SQL Server
dlt incremental loading - Timestamp-based, ID-based, merge/upsert patterns, lookback windows
dlt warehouse loading - Load to Snowflake, BigQuery, Redshift, Postgres, DuckDB

Use dlt when:

Loading data from APIs (Stripe, HubSpot, Shopify, custom APIs)
Replicating databases to warehouses
Building ELT pipelines with incremental loading
Managing data ingestion with Python

For SQL transformation (after ingestion), use:

→ ai-ml-data-science skill (SQLMesh templates for staging/intermediate/marts layers)

Deployment & Packaging
Deployment & MLOps template - Complete MLOps lifecycle, model registry, promotion workflows
Deployment readiness checklist - Go/No-Go gate, monitoring, and rollback plan
API service template - Real-time REST/gRPC API with FastAPI, input validation, rate limiting
Batch scoring pipeline template - Orchestrated batch inference with Airflow/Dagster, validation, backfill
Monitoring & Operations
Monitoring & alerting template - Data/performance/technical metrics, dashboards, SLO definition
Drift detection & retraining template - Automated drift detection, retraining triggers, promotion pipelines
Incident runbook template - Failure mode playbooks, diagnosis steps, resolution procedures
Navigation

Resources

references/drift-detection-guide.md
references/model-registry-patterns.md
references/online-evaluation-patterns.md
references/monitoring-best-practices.md
references/llm-rag-production-patterns.md
references/api-design-patterns.md
references/incident-response-playbooks.md
references/deployment-patterns.md
references/data-ingestion-patterns.md
references/deployment-lifecycle.md
references/feature-store-patterns.md
references/multi-region-patterns.md
references/agentops-patterns.md
references/edge-mlops-patterns.md
references/cost-management-finops.md
references/experiment-tracking-patterns.md
references/automated-retraining-patterns.md

Templates

template-dlt-pipeline.md
template-dlt-rest-api.md
template-dlt-database-source.md
template-dlt-incremental.md
template-dlt-warehouse-loading.md
assets/deployment/template-deployment-mlops.md
assets/deployment/deployment-readiness-checklist.md
assets/deployment/template-api-service.md
assets/deployment/template-batch-pipeline.md
assets/ops/template-incident-runbook.md
assets/monitoring/template-drift-retraining.md
assets/monitoring/template-monitoring-plan.md

Data

data/sources.json - Curated external references
External Resources

See data/sources.json for curated references on:

Serving frameworks (FastAPI, Flask, gRPC, TorchServe, KServe, Ray Serve)
Orchestration (Airflow, Dagster, Prefect)
Model registries and MLOps (MLflow, W&B, Vertex AI, Sagemaker)
Monitoring and observability (Prometheus, Grafana, OpenTelemetry, Evidently)
Feature stores (Feast, Tecton, Vertex, Databricks)
Streaming & messaging (Kafka, Pulsar, Kinesis)
LLMOps & RAG infra (vector DBs, LLM gateways, safety tools)
Data Lake & Lakehouse

For comprehensive data lake/lakehouse patterns (beyond dlt ingestion), see data-lake-platform:

Table formats: Apache Iceberg, Delta Lake, Apache Hudi
Query engines: ClickHouse, DuckDB, Apache Doris, StarRocks
Alternative ingestion: Airbyte (GUI-based connectors)
Transformation: dbt (alternative to SQLMesh)
Streaming: Apache Kafka patterns
Orchestration: Dagster, Airflow

This skill focuses on ML-specific deployment, monitoring, and security. Use data-lake-platform for general-purpose data infrastructure.

Recency Protocol (Tooling Recommendations)

When users ask recommendation questions about MLOps tooling, verify recency before answering.

Trigger Conditions
"What's the best MLOps platform for [use case]?"
"What should I use for [deployment/monitoring/drift detection]?"
"What's the latest in MLOps?"
"Current best practices for [model registry/feature store/observability]?"
"Is [MLflow/Kubeflow/Vertex AI] still relevant in 2026?"
"[MLOps tool A] vs [MLOps tool B]?"
"Best way to deploy [LLM/ML model] to production?"
"What feature store should I use?"
Minimal Recency Check
Start from data/sources.json and prefer sources with add_as_web_search: true.
If web search or browsing is available, confirm at least: (a) the tool’s latest release/docs date, (b) active maintenance signals, (c) a recent comparison/alternatives post.
If live search is not available, state that you are relying on static knowledge + data/sources.json, and recommend validation steps (POC + evals + rollout plan).
What to Report

After searching, provide:

Current landscape: What MLOps tools/platforms are popular NOW
Emerging trends: New approaches gaining traction (LLMOps, GenAI ops)
Deprecated/declining: Tools or approaches losing relevance
Recommendation: Based on fresh data, not just static knowledge
Related Skills

For adjacent topics, reference these skills:

ai-ml-data-science - EDA, feature engineering, modelling, evaluation, SQLMesh transformations
ai-llm - Prompting, fine-tuning, evaluation for LLMs
ai-agents - Agentic workflows, multi-agent systems, LLMOps
ai-rag - RAG pipeline design, chunking, retrieval, evaluation
ai-llm-inference - Model serving optimization, quantization, batching
ai-prompt-engineering - Prompt design patterns and best practices
data-lake-platform - Data lake/lakehouse infrastructure (ClickHouse, Iceberg, Kafka)

Use this skill to turn trained models into reliable services, not to derive the model itself.

Fact-Checking
Use web search/web fetch to verify current external facts, versions, pricing, deadlines, regulations, or platform behavior before final answers.
Prefer primary sources; report source links and dates for volatile information.
If web access is unavailable, state the limitation and mark guidance as unverified.
Weekly Installs
112
Repository
vasilyu1983/ai-…s-public
GitHub Stars
59
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn