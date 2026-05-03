---
title: google-cloud-build-expert
url: https://skills.sh/webdev70/hosting-google/google-cloud-build-expert
---

# google-cloud-build-expert

skills/webdev70/hosting-google/google-cloud-build-expert
google-cloud-build-expert
Installation
$ npx skills add https://github.com/webdev70/hosting-google --skill google-cloud-build-expert
SKILL.md
Google Cloud Build Expert

This skill provides comprehensive expert knowledge of Google Cloud Build for CI/CD pipeline configuration, Docker image building, and automated deployment to Google Cloud services.

Cloud Build Configuration File
File Format: cloudbuild.yaml or cloudbuild.json

Standard cloudbuild.yaml structure:

steps:
  - name: 'builder-image'
    args: ['arg1', 'arg2']
    env: ['ENV_VAR=value']
    dir: 'subdirectory'
    id: 'step-id'
    waitFor: ['previous-step-id']
    timeout: '300s'

substitutions:
  _CUSTOM_VAR: 'value'

options:
  machineType: 'N1_HIGHCPU_8'
  substitutionOption: 'ALLOW_LOOSE'
  logging: 'CLOUD_LOGGING_ONLY'
  logStreamingOption: 'STREAM_ON'

timeout: '1200s'

Build Steps
Common Builder Images

Docker Builder:

- name: 'gcr.io/cloud-builders/docker'
  args: ['build', '-t', 'gcr.io/$PROJECT_ID/myimage:$COMMIT_SHA', '.']


gcloud SDK Builder:

- name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
  entrypoint: 'gcloud'
  args: ['run', 'deploy', 'myservice', '--image', 'gcr.io/$PROJECT_ID/myimage:$COMMIT_SHA']


npm Builder:

- name: 'gcr.io/cloud-builders/npm'
  args: ['install']


git Builder:

- name: 'gcr.io/cloud-builders/git'
  args: ['clone', 'https://github.com/user/repo']

Step Dependencies with waitFor

Sequential execution:

steps:
  - name: 'gcr.io/cloud-builders/npm'
    id: 'install'
    args: ['install']

  - name: 'gcr.io/cloud-builders/npm'
    id: 'test'
    args: ['test']
    waitFor: ['install']

  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '-t', 'image', '.']
    waitFor: ['test']


Parallel execution:

steps:
  - name: 'gcr.io/cloud-builders/npm'
    id: 'install'
    args: ['install']

  - name: 'gcr.io/cloud-builders/npm'
    id: 'lint'
    args: ['run', 'lint']
    waitFor: ['install']

  - name: 'gcr.io/cloud-builders/npm'
    id: 'test'
    args: ['test']
    waitFor: ['install']

  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '.']
    waitFor: ['lint', 'test']  # Waits for both

Substitution Variables
Built-in Substitutions

Automatic variables provided by Cloud Build:

$PROJECT_ID - Google Cloud project ID
$PROJECT_NUMBER - Google Cloud project number
$BUILD_ID - Unique build identifier
$COMMIT_SHA - Git commit SHA (for repo triggers)
$SHORT_SHA - Short (7-char) commit SHA
$BRANCH_NAME - Git branch name
$TAG_NAME - Git tag name
$REVISION_ID - Source revision ID
$REPO_NAME - Repository name
$TRIGGER_NAME - Trigger name that initiated build
Custom Substitutions

Define in cloudbuild.yaml:

substitutions:
  _SERVICE_NAME: 'my-app'
  _REGION: 'us-central1'
  _IMAGE_TAG: 'v1.0.0'
  _ENVIRONMENT: 'production'


Reference in steps:

steps:
  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '-t', 'gcr.io/$PROJECT_ID/${_SERVICE_NAME}:${_IMAGE_TAG}', '.']

  - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
    entrypoint: gcloud
    args:
      - 'run'
      - 'deploy'
      - '${_SERVICE_NAME}'
      - '--image'
      - 'gcr.io/$PROJECT_ID/${_SERVICE_NAME}:${_IMAGE_TAG}'
      - '--region'
      - '${_REGION}'


Naming conventions:

Custom substitutions start with underscore: _CUSTOM_VAR
Built-in substitutions have no underscore: $PROJECT_ID
Use uppercase for consistency
Use descriptive names: _SERVICE_NAME not _SVC
Substitution Options
options:
  substitutionOption: 'ALLOW_LOOSE'  # Allow undefined substitutions
  # OR
  substitutionOption: 'MUST_MATCH'   # Fail if substitution undefined

Building and Pushing Docker Images
Standard Docker Build and Push
steps:
  # Build the container image
  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '-t', 'gcr.io/$PROJECT_ID/myapp:$COMMIT_SHA', '.']

  # Push to Container Registry
  - name: 'gcr.io/cloud-builders/docker'
    args: ['push', 'gcr.io/$PROJECT_ID/myapp:$COMMIT_SHA']

Multi-tag Docker Images
steps:
  - name: 'gcr.io/cloud-builders/docker'
    args:
      - 'build'
      - '-t'
      - 'gcr.io/$PROJECT_ID/myapp:$COMMIT_SHA'
      - '-t'
      - 'gcr.io/$PROJECT_ID/myapp:latest'
      - '.'

  - name: 'gcr.io/cloud-builders/docker'
    args: ['push', '--all-tags', 'gcr.io/$PROJECT_ID/myapp']

Using Artifact Registry (Modern Approach)
steps:
  - name: 'gcr.io/cloud-builders/docker'
    args:
      - 'build'
      - '-t'
      - 'us-central1-docker.pkg.dev/$PROJECT_ID/my-repo/myapp:$COMMIT_SHA'
      - '.'

  - name: 'gcr.io/cloud-builders/docker'
    args: ['push', 'us-central1-docker.pkg.dev/$PROJECT_ID/my-repo/myapp:$COMMIT_SHA']

Build Arguments
steps:
  - name: 'gcr.io/cloud-builders/docker'
    args:
      - 'build'
      - '--build-arg'
      - 'NODE_VERSION=18'
      - '--build-arg'
      - 'BUILD_ENV=production'
      - '-t'
      - 'gcr.io/$PROJECT_ID/myapp'
      - '.'

Deploying to Cloud Run
Basic Cloud Run Deployment
steps:
  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '-t', 'gcr.io/$PROJECT_ID/myapp:$COMMIT_SHA', '.']

  - name: 'gcr.io/cloud-builders/docker'
    args: ['push', 'gcr.io/$PROJECT_ID/myapp:$COMMIT_SHA']

  - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
    entrypoint: gcloud
    args:
      - 'run'
      - 'deploy'
      - 'myapp'
      - '--image'
      - 'gcr.io/$PROJECT_ID/myapp:$COMMIT_SHA'
      - '--region'
      - 'us-central1'
      - '--platform'
      - 'managed'

Cloud Run with Environment Variables
- name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
  entrypoint: gcloud
  args:
    - 'run'
    - 'deploy'
    - 'myapp'
    - '--image'
    - 'gcr.io/$PROJECT_ID/myapp:$COMMIT_SHA'
    - '--region'
    - 'us-central1'
    - '--platform'
    - 'managed'
    - '--set-env-vars'
    - 'NODE_ENV=production,LOG_LEVEL=info'

Cloud Run with Secrets
- name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
  entrypoint: gcloud
  args:
    - 'run'
    - 'deploy'
    - 'myapp'
    - '--image'
    - 'gcr.io/$PROJECT_ID/myapp:$COMMIT_SHA'
    - '--region'
    - 'us-central1'
    - '--set-secrets'
    - 'API_KEY=my-secret:latest'

Cloud Run with Allow Unauthenticated
- name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
  entrypoint: gcloud
  args:
    - 'run'
    - 'deploy'
    - 'myapp'
    - '--image'
    - 'gcr.io/$PROJECT_ID/myapp:$COMMIT_SHA'
    - '--region'
    - 'us-central1'
    - '--platform'
    - 'managed'
    - '--allow-unauthenticated'

Cloud Run with Resource Limits
- name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
  entrypoint: gcloud
  args:
    - 'run'
    - 'deploy'
    - 'myapp'
    - '--image'
    - 'gcr.io/$PROJECT_ID/myapp:$COMMIT_SHA'
    - '--region'
    - 'us-central1'
    - '--memory'
    - '512Mi'
    - '--cpu'
    - '1'
    - '--max-instances'
    - '10'
    - '--concurrency'
    - '80'

Environment Variables and Secrets
Inline Environment Variables
steps:
  - name: 'gcr.io/cloud-builders/npm'
    env:
      - 'NODE_ENV=production'
      - 'API_ENDPOINT=https://api.example.com'
    args: ['run', 'build']

Using Secret Manager
availableSecrets:
  secretManager:
    - versionName: projects/$PROJECT_ID/secrets/api-key/versions/latest
      env: 'API_KEY'
    - versionName: projects/$PROJECT_ID/secrets/db-password/versions/latest
      env: 'DB_PASSWORD'

steps:
  - name: 'gcr.io/cloud-builders/npm'
    secretEnv: ['API_KEY', 'DB_PASSWORD']
    args: ['run', 'deploy']

Encrypted Variables (Legacy)
secrets:
  - kmsKeyName: 'projects/PROJECT_ID/locations/global/keyRings/KEYRING/cryptoKeys/KEY'
    secretEnv:
      API_KEY: 'CiQAVz...'  # Base64 encrypted value

steps:
  - name: 'gcr.io/cloud-builders/npm'
    secretEnv: ['API_KEY']
    args: ['run', 'deploy']

Build Optimization
Caching Dependencies

Node.js npm cache:

steps:
  - name: 'gcr.io/cloud-builders/npm'
    args: ['ci', '--cache', '.npm']
    env:
      - 'npm_config_cache=/workspace/.npm'


Docker layer caching:

options:
  machineType: 'N1_HIGHCPU_8'
  diskSizeGb: 100

steps:
  - name: 'gcr.io/cloud-builders/docker'
    args:
      - 'build'
      - '--cache-from'
      - 'gcr.io/$PROJECT_ID/myapp:latest'
      - '-t'
      - 'gcr.io/$PROJECT_ID/myapp:$COMMIT_SHA'
      - '.'

Parallel Builds
steps:
  - name: 'gcr.io/cloud-builders/npm'
    id: 'install'
    args: ['install']

  - name: 'gcr.io/cloud-builders/npm'
    id: 'lint'
    args: ['run', 'lint']
    waitFor: ['install']

  - name: 'gcr.io/cloud-builders/npm'
    id: 'test'
    args: ['test']
    waitFor: ['install']

  - name: 'gcr.io/cloud-builders/npm'
    id: 'build'
    args: ['run', 'build']
    waitFor: ['lint', 'test']

Timeouts
Step Timeout
steps:
  - name: 'gcr.io/cloud-builders/npm'
    args: ['install']
    timeout: '300s'  # 5 minutes

  - name: 'gcr.io/cloud-builders/npm'
    args: ['test']
    timeout: '600s'  # 10 minutes

Build Timeout
timeout: '1200s'  # 20 minutes for entire build

steps:
  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '.']


Default timeout: 10 minutes (600s) Maximum timeout: 24 hours (86400s)

Logging Options
Cloud Logging Only
options:
  logging: CLOUD_LOGGING_ONLY
  logStreamingOption: STREAM_ON

GCS Logging
options:
  logging: GCS_ONLY
  logsBucket: 'gs://my-build-logs'

Combined Logging
options:
  logging: CLOUD_LOGGING_ONLY
  logStreamingOption: STREAM_ON

Build Triggers
GitHub Trigger Configuration

Trigger on push to main branch:

# In trigger configuration (not cloudbuild.yaml)
name: deploy-main
description: Deploy on push to main
filename: cloudbuild.yaml
github:
  owner: myorg
  name: myrepo
  push:
    branch: ^main$


Trigger on pull request:

github:
  owner: myorg
  name: myrepo
  pullRequest:
    branch: ^main$
    commentControl: COMMENTS_ENABLED


Trigger on tag:

github:
  owner: myorg
  name: myrepo
  tag: ^v[0-9]+\.[0-9]+\.[0-9]+$

Conditional Steps in Builds
steps:
  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '.']

  # Only deploy on main branch
  - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
    entrypoint: bash
    args:
      - '-c'
      - |
        if [ "$BRANCH_NAME" = "main" ]; then
          gcloud run deploy myapp --image gcr.io/$PROJECT_ID/myapp:$COMMIT_SHA
        fi

Service Account and IAM
Service Account for Build
serviceAccount: 'projects/PROJECT_ID/serviceAccounts/my-build-sa@PROJECT_ID.iam.gserviceaccount.com'

steps:
  - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
    args: ['run', 'deploy', 'myapp']

Required IAM Roles

For Cloud Build Service Account:

roles/run.admin - Deploy to Cloud Run
roles/iam.serviceAccountUser - Act as service account
roles/storage.admin - Push to Container Registry/Artifact Registry
roles/secretmanager.secretAccessor - Access Secret Manager
Complete Example: Node.js App to Cloud Run
steps:
  # Install dependencies
  - name: 'gcr.io/cloud-builders/npm'
    args: ['ci', '--only=production']

  # Run tests
  - name: 'gcr.io/cloud-builders/npm'
    args: ['test']
    env:
      - 'NODE_ENV=test'

  # Build Docker image
  - name: 'gcr.io/cloud-builders/docker'
    args:
      - 'build'
      - '-t'
      - 'gcr.io/$PROJECT_ID/${_SERVICE_NAME}:$COMMIT_SHA'
      - '-t'
      - 'gcr.io/$PROJECT_ID/${_SERVICE_NAME}:latest'
      - '.'

  # Push to Container Registry
  - name: 'gcr.io/cloud-builders/docker'
    args: ['push', 'gcr.io/$PROJECT_ID/${_SERVICE_NAME}:$COMMIT_SHA']

  # Deploy to Cloud Run
  - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
    entrypoint: gcloud
    args:
      - 'run'
      - 'deploy'
      - '${_SERVICE_NAME}'
      - '--image'
      - 'gcr.io/$PROJECT_ID/${_SERVICE_NAME}:$COMMIT_SHA'
      - '--region'
      - '${_REGION}'
      - '--platform'
      - 'managed'
      - '--allow-unauthenticated'
      - '--set-env-vars'
      - 'NODE_ENV=production'

substitutions:
  _SERVICE_NAME: 'my-node-app'
  _REGION: 'us-central1'

options:
  machineType: 'N1_HIGHCPU_8'
  logging: CLOUD_LOGGING_ONLY

timeout: '1200s'

Best Practices
1. Use Specific Image Tags
# Good
- name: 'gcr.io/cloud-builders/docker'
  args: ['build', '-t', 'gcr.io/$PROJECT_ID/myapp:$COMMIT_SHA', '.']

# Avoid (less reproducible)
- name: 'gcr.io/cloud-builders/docker'
  args: ['build', '-t', 'gcr.io/$PROJECT_ID/myapp:latest', '.']

2. Fail Fast
steps:
  # Run quick checks first
  - name: 'gcr.io/cloud-builders/npm'
    args: ['run', 'lint']

  - name: 'gcr.io/cloud-builders/npm'
    args: ['test']

  # Expensive operations last
  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '.']
    waitFor: ['lint', 'test']

3. Use Substitution Variables
# Good - easy to modify
substitutions:
  _SERVICE_NAME: 'my-app'
  _REGION: 'us-central1'

# Avoid - hardcoded values throughout

4. Set Appropriate Timeouts
steps:
  - name: 'gcr.io/cloud-builders/npm'
    args: ['install']
    timeout: '300s'  # Prevent hanging builds

5. Use Cloud Logging
options:
  logging: CLOUD_LOGGING_ONLY
  logStreamingOption: STREAM_ON  # See logs in real-time

6. Leverage Caching
steps:
  - name: 'gcr.io/cloud-builders/docker'
    args:
      - 'build'
      - '--cache-from'
      - 'gcr.io/$PROJECT_ID/myapp:latest'
      - '-t'
      - 'gcr.io/$PROJECT_ID/myapp:$COMMIT_SHA'
      - '.'

Common Patterns
Multi-Environment Deployment
steps:
  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '-t', 'gcr.io/$PROJECT_ID/myapp:$COMMIT_SHA', '.']

  - name: 'gcr.io/cloud-builders/docker'
    args: ['push', 'gcr.io/$PROJECT_ID/myapp:$COMMIT_SHA']

  # Deploy to staging
  - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
    entrypoint: gcloud
    args:
      - 'run'
      - 'deploy'
      - 'myapp-staging'
      - '--image'
      - 'gcr.io/$PROJECT_ID/myapp:$COMMIT_SHA'
      - '--region'
      - 'us-central1'

  # Deploy to production (manual approval required via trigger config)
  - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
    entrypoint: gcloud
    args:
      - 'run'
      - 'deploy'
      - 'myapp-production'
      - '--image'
      - 'gcr.io/$PROJECT_ID/myapp:$COMMIT_SHA'
      - '--region'
      - 'us-central1'

Running Shell Scripts
steps:
  - name: 'gcr.io/cloud-builders/gcloud'
    entrypoint: 'bash'
    args:
      - '-c'
      - |
        echo "Starting deployment..."
        gcloud run deploy myapp \
          --image gcr.io/$PROJECT_ID/myapp:$COMMIT_SHA \
          --region us-central1
        echo "Deployment complete!"

Testing Before Deploy
steps:
  - name: 'gcr.io/cloud-builders/npm'
    id: 'install'
    args: ['install']

  - name: 'gcr.io/cloud-builders/npm'
    id: 'lint'
    args: ['run', 'lint']
    waitFor: ['install']

  - name: 'gcr.io/cloud-builders/npm'
    id: 'test'
    args: ['test']
    waitFor: ['install']

  - name: 'gcr.io/cloud-builders/docker'
    id: 'build'
    args: ['build', '-t', 'gcr.io/$PROJECT_ID/myapp', '.']
    waitFor: ['lint', 'test']  # Only build if tests pass

  - name: 'gcr.io/cloud-builders/docker'
    id: 'push'
    args: ['push', 'gcr.io/$PROJECT_ID/myapp']
    waitFor: ['build']

  - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
    entrypoint: gcloud
    args: ['run', 'deploy', 'myapp', '--image', 'gcr.io/$PROJECT_ID/myapp']
    waitFor: ['push']

Troubleshooting
Common Errors

Error: "failed to find one or more images"

Cause: Image not pushed before deploy step
Solution: Ensure push step completes before deploy, use waitFor

Error: "timeout exceeded"

Cause: Step or build took too long
Solution: Increase timeout value

Error: "permission denied"

Cause: Service account lacks required IAM roles
Solution: Grant necessary roles to Cloud Build service account

Error: "substitution not found"

Cause: Undefined substitution variable
Solution: Define in substitutions section or use ALLOW_LOOSE
Debugging Builds

View build logs:

gcloud builds list
gcloud builds log BUILD_ID


View build details:

gcloud builds describe BUILD_ID


Test locally (Cloud Build Local):

cloud-build-local --config=cloudbuild.yaml --dryrun=false .

Resources
Official Documentation: https://cloud.google.com/build/docs
Builder Images: https://cloud.google.com/build/docs/cloud-builders
Substitution Variables: https://cloud.google.com/build/docs/configuring-builds/substitute-variable-values
Cloud Run Deployment: https://cloud.google.com/run/docs/deploying
Build Triggers: https://cloud.google.com/build/docs/automating-builds/create-manage-triggers
Weekly Installs
10
Repository
webdev70/hosting-google
First Seen
Feb 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass