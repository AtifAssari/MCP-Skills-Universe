---
title: gcp-deploy
url: https://skills.sh/fwfutures/skills/gcp-deploy
---

# gcp-deploy

skills/fwfutures/skills/gcp-deploy
gcp-deploy
Installation
$ npx skills add https://github.com/fwfutures/skills --skill gcp-deploy
SKILL.md
GCP Cloud Run Deploy

Deploy from source to Cloud Run in a single command. Requires: a GCP project, a Dockerfile in the repo root, and an app that listens on a port (default 8080 / PORT env var).

Quick Deploy
# 1. Auth (skip if already logged in)
gcloud auth login
gcloud config set project PROJECT_ID

# 2. Enable APIs (first time only)
gcloud services enable run.googleapis.com cloudbuild.googleapis.com artifactregistry.googleapis.com

# 3. Deploy
gcloud run deploy SERVICE_NAME \
  --source . \
  --region australia-southeast1 \
  --allow-unauthenticated


This builds the container remotely via Cloud Build, pushes to Artifact Registry, deploys to Cloud Run, and returns a public HTTPS URL. Redeploy by re-running the same command.

Deploy Script

Copy scripts/deploy.sh into the project root for one-command deploys:

chmod +x deploy.sh
./deploy.sh my-service


Env vars: GCP_REGION (default australia-southeast1), GCP_PROJECT (default: current gcloud project).

Common Flags
Flag	Purpose	Example
--region	Deployment region	australia-southeast1
--allow-unauthenticated	Public access	
--port	Container port (if not 8080)	--port 3000
--set-env-vars	Env vars	--set-env-vars KEY=val,FOO=bar
--set-secrets	Secret Manager secrets	--set-secrets ENV=SECRET:latest
--memory	Memory	--memory 512Mi
--cpu	CPU	--cpu 1
--min-instances	Min instances (0 = scale to zero)	--min-instances 0
--max-instances	Max instances	--max-instances 3
--timeout	Request timeout (max 3600)	--timeout 300
Environment Variables and Secrets

Inline env vars:

gcloud run deploy SERVICE --source . --region REGION --allow-unauthenticated \
  --set-env-vars "DATABASE_URL=postgres://...,API_KEY=abc123"


Secret Manager (recommended for sensitive values):

# Create secret
echo -n "secret-value" | gcloud secrets create MY_SECRET --data-file=-

# Grant access to default compute SA
gcloud secrets add-iam-policy-binding MY_SECRET \
  --member="serviceAccount:$(gcloud iam service-accounts list --format='value(email)' --filter='displayName:Compute Engine default')" \
  --role="roles/secretmanager.secretAccessor"

# Deploy with secret
gcloud run deploy SERVICE --source . --region REGION --allow-unauthenticated \
  --set-secrets "MY_SECRET=MY_SECRET:latest"

Useful Commands
# Stream logs
gcloud run services logs tail SERVICE --region REGION

# List services
gcloud run services list --region REGION

# Get service URL
gcloud run services describe SERVICE --region REGION --format "value(status.url)"

# Delete service
gcloud run services delete SERVICE --region REGION

CI/Headless Auth
gcloud auth activate-service-account --key-file=key.json
gcloud config set project PROJECT_ID

Troubleshooting
Issue	Fix
Build fails	Check Dockerfile locally: docker build .
403 on deploy	Need roles/run.admin and roles/cloudbuild.builds.editor
App crashes on start	Check logs: gcloud run services logs tail SERVICE --region REGION
Port mismatch	Set --port to match app, or have app read PORT env var
Cold start slow	Set --min-instances 1 (stays warm, costs more)
Timeout on long requests	Increase with --timeout 300 (max 3600s)
Weekly Installs
24
Repository
fwfutures/skills
First Seen
Feb 26, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykFail