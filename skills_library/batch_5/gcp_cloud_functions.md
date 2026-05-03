---
title: gcp-cloud-functions
url: https://skills.sh/aj-geddes/useful-ai-prompts/gcp-cloud-functions
---

# gcp-cloud-functions

skills/aj-geddes/useful-ai-prompts/gcp-cloud-functions
gcp-cloud-functions
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill gcp-cloud-functions
SKILL.md
GCP Cloud Functions
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Google Cloud Functions enables event-driven serverless computing on Google Cloud Platform. Build functions with automatic scaling, integrated security, and seamless integration with Google Cloud services for rapid development.

When to Use
HTTP APIs and webhooks
Pub/Sub message processing
Storage bucket events
Firestore database triggers
Cloud Scheduler jobs
Real-time data processing
Image and video processing
Data pipeline orchestration
Quick Start

Minimal working example:

# Install Google Cloud SDK
curl https://sdk.cloud.google.com | bash
exec -l $SHELL

# Initialize and authenticate
gcloud init
gcloud auth application-default login

# Set project
gcloud config set project MY_PROJECT_ID

# Create service account
gcloud iam service-accounts create cloud-function-sa \
  --display-name "Cloud Function Service Account"

# Grant permissions
gcloud projects add-iam-policy-binding MY_PROJECT_ID \
  --member="serviceAccount:cloud-function-sa@MY_PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/cloudfunctions.invoker"

# Deploy HTTP function
gcloud functions deploy my-http-function \
  --gen2 \
  --runtime nodejs18 \
  --region us-central1 \
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Cloud Function Creation with gcloud CLI	Cloud Function Creation with gcloud CLI
Cloud Functions Implementation (Node.js)	Cloud Functions Implementation (Node.js)
Terraform Cloud Functions Configuration	Terraform Cloud Functions Configuration
Best Practices
✅ DO
Use service accounts with least privilege
Store secrets in Secret Manager
Implement proper error handling
Use environment variables for configuration
Monitor with Cloud Logging and Cloud Monitoring
Set appropriate memory and timeout
Use event filters to reduce invocations
Implement idempotent functions
❌ DON'T
Store secrets in code
Use default service account
Create long-running functions
Ignore error handling
Deploy without testing
Use unauthenticated access for sensitive functions
Weekly Installs
302
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn