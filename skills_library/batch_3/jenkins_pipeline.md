---
title: jenkins-pipeline
url: https://skills.sh/aj-geddes/useful-ai-prompts/jenkins-pipeline
---

# jenkins-pipeline

skills/aj-geddes/useful-ai-prompts/jenkins-pipeline
jenkins-pipeline
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill jenkins-pipeline
Summary

Enterprise-grade Jenkins pipelines with declarative and scripted syntax for multi-stage CI/CD automation.

Supports both declarative and scripted pipeline approaches, with multi-branch pipeline and parameterized build capabilities
Includes environment variables, credentials management, approval gates, and artifact archiving for production-safe deployments
Covers agent configuration, stage orchestration, test reporting (JUnit), and Docker registry integration
Best practices emphasize modular, reusable pipelines with proper secret handling and error management
SKILL.md
Jenkins Pipeline
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Create enterprise-grade Jenkins pipelines using declarative and scripted approaches to automate building, testing, and deploying with advanced control flow.

When to Use
Enterprise CI/CD infrastructure
Complex multi-stage builds
On-premise deployment automation
Parameterized builds
Quick Start

Minimal working example:

pipeline {
    agent { label 'linux-docker' }
    environment {
        REGISTRY = 'docker.io'
        IMAGE_NAME = 'myapp'
    }
    parameters {
        string(name: 'DEPLOY_ENV', defaultValue: 'staging')
    }
    stages {
        stage('Checkout') { steps { checkout scm } }
        stage('Install') { steps { sh 'npm ci' } }
        stage('Lint') { steps { sh 'npm run lint' } }
        stage('Test') {
            steps {
                sh 'npm run test:coverage'
                junit 'test-results.xml'
            }
        }
        stage('Build') {
            steps {
                sh 'npm run build'
                archiveArtifacts artifacts: 'dist/**/*'
            }
        }
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Declarative Pipeline (Jenkinsfile)	Declarative Pipeline (Jenkinsfile)
Scripted Pipeline	Scripted Pipeline (Groovy), Multi-Branch Pipeline, Parameterized Pipeline, Pipeline with Credentials
Best Practices
✅ DO
Use declarative pipelines for clarity
Use credentials plugin for secrets
Archive artifacts and reports
Implement approval gates for production
Keep pipelines modular and reusable
❌ DON'T
Store credentials in pipeline code
Ignore pipeline errors
Skip test coverage reporting
Use deprecated plugins
Weekly Installs
747
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass