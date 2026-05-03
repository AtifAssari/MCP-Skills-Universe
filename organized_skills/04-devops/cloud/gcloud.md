---
rating: ⭐⭐⭐
title: gcloud
url: https://skills.sh/dicklesworthstone/agent_flywheel_clawdbot_skills_and_integrations/gcloud
---

# gcloud

skills/dicklesworthstone/agent_flywheel_clawdbot_skills_and_integrations/gcloud
gcloud
Installation
$ npx skills add https://github.com/dicklesworthstone/agent_flywheel_clawdbot_skills_and_integrations --skill gcloud
SKILL.md
GCloud Skill

Use the gcloud CLI to manage Google Cloud Platform resources and services.

Authentication

Check current auth:

gcloud auth list


Login interactively:

gcloud auth login


Login with service account:

gcloud auth activate-service-account --key-file=key.json


Application default credentials:

gcloud auth application-default login

Project & Configuration

List projects:

gcloud projects list


Set default project:

gcloud config set project PROJECT_ID


Show current config:

gcloud config list


Create named configuration:

gcloud config configurations create my-config
gcloud config configurations activate my-config


Set default region/zone:

gcloud config set compute/region us-central1
gcloud config set compute/zone us-central1-a

Compute Engine (VMs)

List instances:

gcloud compute instances list


Create instance:

gcloud compute instances create my-vm \
  --zone=us-central1-a \
  --machine-type=e2-medium \
  --image-family=debian-12 \
  --image-project=debian-cloud


SSH to instance:

gcloud compute ssh my-vm --zone=us-central1-a


Stop/start instance:

gcloud compute instances stop my-vm --zone=us-central1-a
gcloud compute instances start my-vm --zone=us-central1-a


Delete instance:

gcloud compute instances delete my-vm --zone=us-central1-a

Cloud Run

List services:

gcloud run services list


Deploy from source:

gcloud run deploy my-service --source . --region=us-central1


Deploy container:

gcloud run deploy my-service \
  --image=gcr.io/PROJECT/IMAGE \
  --region=us-central1 \
  --allow-unauthenticated


View logs:

gcloud run services logs read my-service --region=us-central1


Update traffic split:

gcloud run services update-traffic my-service \
  --to-revisions=LATEST=100 \
  --region=us-central1

Cloud Functions

List functions:

gcloud functions list


Deploy function (2nd gen):

gcloud functions deploy my-function \
  --gen2 \
  --runtime=nodejs20 \
  --region=us-central1 \
  --trigger-http \
  --entry-point=handler \
  --source=.


View logs:

gcloud functions logs read my-function --region=us-central1


Delete function:

gcloud functions delete my-function --region=us-central1

Google Kubernetes Engine (GKE)

List clusters:

gcloud container clusters list


Get credentials for kubectl:

gcloud container clusters get-credentials my-cluster \
  --zone=us-central1-a


Create cluster:

gcloud container clusters create my-cluster \
  --zone=us-central1-a \
  --num-nodes=3


Resize node pool:

gcloud container clusters resize my-cluster \
  --node-pool=default-pool \
  --num-nodes=5 \
  --zone=us-central1-a

Cloud Storage

List buckets:

gcloud storage buckets list


Create bucket:

gcloud storage buckets create gs://my-bucket --location=us-central1


List objects:

gcloud storage ls gs://my-bucket/


Copy files:

# Upload
gcloud storage cp local-file.txt gs://my-bucket/

# Download
gcloud storage cp gs://my-bucket/file.txt ./

# Recursive
gcloud storage cp -r ./local-dir gs://my-bucket/


Sync directory:

gcloud storage rsync -r ./local-dir gs://my-bucket/remote-dir

Cloud SQL

List instances:

gcloud sql instances list


Create instance:

gcloud sql instances create my-instance \
  --database-version=POSTGRES_15 \
  --tier=db-f1-micro \
  --region=us-central1


Connect via proxy:

gcloud sql connect my-instance --user=postgres


Create database:

gcloud sql databases create mydb --instance=my-instance

BigQuery

List datasets:

bq ls


Run query:

bq query --use_legacy_sql=false 'SELECT * FROM dataset.table LIMIT 10'


Create dataset:

bq mk --dataset my_dataset


Load data:

bq load --source_format=CSV my_dataset.my_table gs://bucket/data.csv

Pub/Sub

List topics:

gcloud pubsub topics list


Create topic:

gcloud pubsub topics create my-topic


Publish message:

gcloud pubsub topics publish my-topic --message="Hello"


Create subscription:

gcloud pubsub subscriptions create my-sub --topic=my-topic


Pull messages:

gcloud pubsub subscriptions pull my-sub --auto-ack

Secret Manager

List secrets:

gcloud secrets list


Create secret:

echo -n "my-secret-value" | gcloud secrets create my-secret --data-file=-


Access secret:

gcloud secrets versions access latest --secret=my-secret


Add new version:

echo -n "new-value" | gcloud secrets versions add my-secret --data-file=-

IAM

List service accounts:

gcloud iam service-accounts list


Create service account:

gcloud iam service-accounts create my-sa \
  --display-name="My Service Account"


Create key:

gcloud iam service-accounts keys create key.json \
  --iam-account=my-sa@PROJECT.iam.gserviceaccount.com


Add IAM binding:

gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:my-sa@PROJECT.iam.gserviceaccount.com" \
  --role="roles/storage.admin"

Cloud Build

Submit build:

gcloud builds submit --tag gcr.io/PROJECT/IMAGE


List builds:

gcloud builds list


View build logs:

gcloud builds log BUILD_ID

Artifact Registry

List repositories:

gcloud artifacts repositories list


Configure Docker:

gcloud auth configure-docker us-central1-docker.pkg.dev

Logging

Read logs:

gcloud logging read "resource.type=cloud_run_revision" --limit=50


Tail logs:

gcloud logging tail "resource.type=gce_instance"

App Engine

Deploy app:

gcloud app deploy


View logs:

gcloud app logs tail


Browse app:

gcloud app browse

Useful Flags

Format as JSON:

gcloud compute instances list --format=json


Format as table with specific columns:

gcloud compute instances list --format="table(name,zone,status)"


Filter results:

gcloud compute instances list --filter="status=RUNNING"


Quiet mode (no prompts):

gcloud compute instances delete my-vm --quiet

Cheat Sheet

Quick reference:

gcloud cheat-sheet


Interactive shell:

gcloud interactive

Weekly Installs
178
Repository
dicklesworthsto…grations
GitHub Stars
63
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass