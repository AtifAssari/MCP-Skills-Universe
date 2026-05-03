---
title: gcp-bigquery
url: https://skills.sh/alphaonedev/openclaw-graph/gcp-bigquery
---

# gcp-bigquery

skills/alphaonedev/openclaw-graph/gcp-bigquery
gcp-bigquery
Installation
$ npx skills add https://github.com/alphaonedev/openclaw-graph --skill gcp-bigquery
SKILL.md
gcp-bigquery
Google Cloud Integration

This skill delegates all GCP provisioning and operations to the official Google Cloud Python client libraries.

# Core GCP client library
pip install google-cloud-python

# Vertex AI + Agent Engine (AI/ML workloads)
pip install google-cloud-aiplatform

# Specific service clients (install only what you need)
pip install google-cloud-bigquery      # BigQuery
pip install google-cloud-storage       # Cloud Storage
pip install google-cloud-pubsub        # Pub/Sub
pip install google-cloud-run           # Cloud Run


SDK Docs: https://github.com/googleapis/google-cloud-python Vertex AI SDK: https://cloud.google.com/vertex-ai/docs/python-sdk/use-vertex-ai-python-sdk

Use the Google Cloud Python SDK for all GCP provisioning and operational actions. This skill provides architecture guidance, cost modeling, and pre-flight requirements — the SDK handles execution.

Architecture Guidance

Consult this skill for:

GCP service selection and trade-off analysis
Cost estimation and optimization (committed use discounts, sustained use)
Pre-flight IAM / Workload Identity Federation requirements
IaC approach (Terraform AzureRM vs Deployment Manager vs Config Connector)
Integration patterns with Google Workspace and other GCP services
Vertex AI Agent Engine for multi-agent workflow design
Agent & AI Capabilities
Capability	Tool
LLM agents	Vertex AI Agent Engine
Model serving	Vertex AI Model Garden
RAG	Vertex AI Search + Embeddings API
Multi-agent	Agent Development Kit (google/adk-python)
MCP	Vertex AI Extensions (MCP-compatible)
Reference
Google Cloud Python Client
Vertex AI Python SDK
Google ADK
GCP Pricing Calculator
IAM Best Practices
Workload Identity Federation
Weekly Installs
19
Repository
alphaonedev/ope…aw-graph
GitHub Stars
4
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass