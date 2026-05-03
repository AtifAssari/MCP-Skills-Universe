---
rating: ⭐⭐
title: alloydb-basics
url: https://skills.sh/google/skills/alloydb-basics
---

# alloydb-basics

skills/google/skills/alloydb-basics
alloydb-basics
Installation
$ npx skills add https://github.com/google/skills --skill alloydb-basics
SKILL.md
AlloyDB Basics

AlloyDB for PostgreSQL is a managed, PostgreSQL-compatible database service designed for enterprise-grade performance and availability. It utilizes a disaggregated compute and storage architecture to scale resources independently. It also provides AlloyDB AI, a collection of features that includes AI-powered search (vector, hybrid search, and AI functions), natural language capabilities, conversational analytics, and inference features like forecasting and model endpoint management to help developers build AI apps faster.

Quick Start

Enable the AlloyDB API:

gcloud services enable alloydb.googleapis.com


Create a Cluster:

gcloud alloydb clusters create my-cluster --region=us-central1 \
    --password=my-password --network=my-vpc


Note: For production, we recommend using IAM database authentication instead of passwords. If passwords must be used, use secure secret management (e.g., Secret Manager) instead of passing passwords in cleartext.

Create a Primary Instance:

gcloud alloydb instances create my-primary --cluster=my-cluster \
    --region=us-central1 --instance-type=PRIMARY --cpu-count=2

Reference Directory

Core Concepts: Architecture, disaggregated storage, and performance features.

CLI Usage: Essential gcloud alloydb commands for cluster and instance management.

Client Libraries & Connectors: Connecting to AlloyDB using Python, Java, Node.js, and Go.

MCP Usage: Using the AlloyDB remote MCP server and Gemini CLI extension.

Infrastructure as Code: Terraform configuration and deployment examples.

IAM & Security: Predefined roles, service agents, and database authentication.

If you need product information not found in these references, use the Developer Knowledge MCP server search_documents tool.

Weekly Installs
1.2K
Repository
google/skills
GitHub Stars
6.3K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail