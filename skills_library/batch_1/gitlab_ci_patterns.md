---
title: gitlab-ci-patterns
url: https://skills.sh/wshobson/agents/gitlab-ci-patterns
---

# gitlab-ci-patterns

skills/wshobson/agents/gitlab-ci-patterns
gitlab-ci-patterns
Installation
$ npx skills add https://github.com/wshobson/agents --skill gitlab-ci-patterns
Summary

Multi-stage GitLab CI/CD pipelines with Docker builds, Kubernetes deployments, and security scanning.

Covers core pipeline patterns including build, test, and deploy stages with artifact caching and environment management
Includes Docker image building and pushing to registries, multi-environment deployments (staging/production), and Terraform infrastructure automation
Provides security scanning templates (SAST, dependency scanning, container scanning) and Trivy vulnerability checks
Demonstrates caching strategies for dependencies, dynamic child pipelines, and manual approval gates for production deployments
SKILL.md
GitLab CI Patterns

Comprehensive GitLab CI/CD pipeline patterns for automated testing, building, and deployment.

Purpose

Create efficient GitLab CI pipelines with proper stage organization, caching, and deployment strategies.

When to Use
Automate GitLab-based CI/CD
Implement multi-stage pipelines
Configure GitLab Runners
Deploy to Kubernetes from GitLab
Implement GitOps workflows
Basic Pipeline Structure
stages:
  - build
  - test
  - deploy

variables:
  DOCKER_DRIVER: overlay2
  DOCKER_TLS_CERTDIR: "/certs"

build:
  stage: build
  image: node:20
  script:
    - npm ci
    - npm run build
  artifacts:
    paths:
      - dist/
    expire_in: 1 hour
  cache:
    key: ${CI_COMMIT_REF_SLUG}
    paths:
      - node_modules/

test:
  stage: test
  image: node:20
  script:
    - npm ci
    - npm run lint
    - npm test
  coverage: '/Lines\s*:\s*(\d+\.\d+)%/'
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml

deploy:
  stage: deploy
  image: bitnami/kubectl:1.31
  script:
    - kubectl apply -f k8s/
    - kubectl rollout status deployment/my-app
  only:
    - main
  environment:
    name: production
    url: https://app.example.com

Docker Build and Push
build-docker:
  stage: build
  image: docker:24
  services:
    - docker:24-dind
  before_script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
  script:
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
    - docker build -t $CI_REGISTRY_IMAGE:latest .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
    - docker push $CI_REGISTRY_IMAGE:latest
  only:
    - main
    - tags

Multi-Environment Deployment
.deploy_template: &deploy_template
  image: bitnami/kubectl:1.31
  before_script:
    - kubectl config set-cluster k8s --server="$KUBE_URL" --insecure-skip-tls-verify=true
    - kubectl config set-credentials admin --token="$KUBE_TOKEN"
    - kubectl config set-context default --cluster=k8s --user=admin
    - kubectl config use-context default

deploy:staging:
  <<: *deploy_template
  stage: deploy
  script:
    - kubectl apply -f k8s/ -n staging
    - kubectl rollout status deployment/my-app -n staging
  environment:
    name: staging
    url: https://staging.example.com
  only:
    - develop

deploy:production:
  <<: *deploy_template
  stage: deploy
  script:
    - kubectl apply -f k8s/ -n production
    - kubectl rollout status deployment/my-app -n production
  environment:
    name: production
    url: https://app.example.com
  when: manual
  only:
    - main

Terraform Pipeline
stages:
  - validate
  - plan
  - apply

variables:
  TF_ROOT: ${CI_PROJECT_DIR}/terraform
  TF_VERSION: "1.6.0"

before_script:
  - cd ${TF_ROOT}
  - terraform --version

validate:
  stage: validate
  image: hashicorp/terraform:${TF_VERSION}
  script:
    - terraform init -backend=false
    - terraform validate
    - terraform fmt -check

plan:
  stage: plan
  image: hashicorp/terraform:${TF_VERSION}
  script:
    - terraform init
    - terraform plan -out=tfplan
  artifacts:
    paths:
      - ${TF_ROOT}/tfplan
    expire_in: 1 day

apply:
  stage: apply
  image: hashicorp/terraform:${TF_VERSION}
  script:
    - terraform init
    - terraform apply -auto-approve tfplan
  dependencies:
    - plan
  when: manual
  only:
    - main

Security Scanning
include:
  - template: Security/SAST.gitlab-ci.yml
  - template: Security/Dependency-Scanning.gitlab-ci.yml
  - template: Security/Container-Scanning.gitlab-ci.yml

trivy-scan:
  stage: test
  image: aquasec/trivy:0.58.0
  script:
    - trivy image --exit-code 1 --severity HIGH,CRITICAL $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
  allow_failure: true

Caching Strategies
# Cache node_modules
build:
  cache:
    key: ${CI_COMMIT_REF_SLUG}
    paths:
      - node_modules/
    policy: pull-push

# Global cache
cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - .cache/
    - vendor/

# Separate cache per job
job1:
  cache:
    key: job1-cache
    paths:
      - build/

job2:
  cache:
    key: job2-cache
    paths:
      - dist/

Dynamic Child Pipelines
generate-pipeline:
  stage: build
  script:
    - python generate_pipeline.py > child-pipeline.yml
  artifacts:
    paths:
      - child-pipeline.yml

trigger-child:
  stage: deploy
  trigger:
    include:
      - artifact: child-pipeline.yml
        job: generate-pipeline
    strategy: depend

Best Practices
Use specific image tags (node:20, not node:latest)
Cache dependencies appropriately
Use artifacts for build outputs
Implement manual gates for production
Use environments for deployment tracking
Enable merge request pipelines
Use pipeline schedules for recurring jobs
Implement security scanning
Use CI/CD variables for secrets
Monitor pipeline performance
Related Skills
github-actions-templates - For GitHub Actions
deployment-pipeline-design - For architecture
secrets-management - For secrets handling
Weekly Installs
6.8K
Repository
wshobson/agents
GitHub Stars
34.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn