---
rating: ⭐⭐
title: cloud-sql-basics
url: https://skills.sh/google/skills/cloud-sql-basics
---

# cloud-sql-basics

skills/google/skills/cloud-sql-basics
cloud-sql-basics
Installation
$ npx skills add https://github.com/google/skills --skill cloud-sql-basics
SKILL.md
Cloud SQL Basics

Cloud SQL is a fully managed relational database service for MySQL, PostgreSQL, and SQL Server. It automates time-consuming tasks like patches, updates, backups, and replicas, while providing high performance and availability for your applications.

Prerequisites

Ensure you have the necessary IAM permissions to create and manage Cloud SQL instances. The Cloud SQL Admin (roles/cloudsql.admin) role provides full access to Cloud SQL resources.

Quick Start (PostgreSQL)

Enable the API:

gcloud services enable sqladmin.googleapis.com


Create an Instance:

gcloud sql instances create INSTANCE_NAME \
  --database-version=POSTGRES_18 \
  --cpu=2 \
  --memory=7680MiB \
  --region=REGION


Set a password for the default user:

Because this is a Cloud SQL for PostgreSQL instance, the default admin user is postgres:

gcloud sql users set-password postgres \
  --instance=INSTANCE_NAME --password=PASSWORD


Create a database:

gcloud sql databases create DATABASE_NAME \
  --instance=INSTANCE_NAME


Get the instance connection name:

You need the instance connection name (which is formatted as PROJECT_ID:REGION:INSTANCE_NAME) to connect using the Cloud SQL Auth Proxy. Retrieve it with the following command:

gcloud sql instances describe INSTANCE_NAME \
  --format="value(connectionName)"


Connect to the instance:

The Cloud SQL Auth Proxy must be running to be able to connect to the instance. In a separate terminal, start the proxy using the connection name:

./cloud-sql-proxy INSTANCE_CONNECTION_NAME


With the proxy running, connect using psql in another terminal:

psql "host=127.0.0.1 port=5432 user=postgres dbname=DATABASE_NAME password=PASSWORD sslmode=disable"

Reference Directory

Core Concepts: Instance architecture, high availability (HA), and supported database engines.

CLI Usage: Essential gcloud sql commands for instance, database, and user management.

Client Libraries & Connectors: Connecting to Cloud SQL using Python, Java, Node.js, and Go.

MCP Usage: Using the Cloud SQL remote MCP server and Gemini CLI extension.

Infrastructure as Code: Terraform configuration for instances, databases, and users.

IAM & Security: Predefined roles, SSL/TLS certificates, and Auth Proxy configuration.

If you need product information not found in these references, use the Developer Knowledge MCP server search_documents tool.

Weekly Installs
1.5K
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