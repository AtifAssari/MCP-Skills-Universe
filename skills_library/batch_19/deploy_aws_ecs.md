---
title: deploy-aws-ecs
url: https://skills.sh/dralgorhythm/claude-agentic-framework/deploy-aws-ecs
---

# deploy-aws-ecs

skills/dralgorhythm/claude-agentic-framework/deploy-aws-ecs
deploy-aws-ecs
Installation
$ npx skills add https://github.com/dralgorhythm/claude-agentic-framework --skill deploy-aws-ecs
SKILL.md
Deploy to AWS ECS/Fargate
Why ECS/Fargate?
Serverless container orchestration
No cluster management
Auto-scaling built-in
Deep AWS integration
Pay-per-use pricing
Production-grade reliability
Quick Start
# Install AWS CLI
aws --version

# Configure credentials (use OIDC in production)
aws configure

# Login to ECR
aws ecr get-login-password --region us-east-1 | \
  docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com

ECR Setup
Create Repository
# Create ECR repository
aws ecr create-repository --repository-name myapp

# Build and tag image
docker build -t myapp:latest .
docker tag myapp:latest <account-id>.dkr.ecr.us-east-1.amazonaws.com/myapp:latest

# Push to ECR
docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/myapp:latest

Task Definition
Basic task-definition.json
{
  "family": "myapp-task",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "256",
  "memory": "512",
  "executionRoleArn": "arn:aws:iam::<account-id>:role/ecsTaskExecutionRole",
  "containerDefinitions": [
    {
      "name": "myapp",
      "image": "<account-id>.dkr.ecr.us-east-1.amazonaws.com/myapp:latest",
      "portMappings": [
        {
          "containerPort": 8080,
          "protocol": "tcp"
        }
      ],
      "environment": [
        {"name": "NODE_ENV", "value": "production"}
      ],
      "secrets": [
        {
          "name": "DATABASE_URL",
          "valueFrom": "arn:aws:secretsmanager:us-east-1:<account-id>:secret:db-url"
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/myapp",
          "awslogs-region": "us-east-1",
          "awslogs-stream-prefix": "ecs"
        }
      }
    }
  ]
}

Register Task Definition
aws ecs register-task-definition --cli-input-json file://task-definition.json

Service Creation
# Create ECS cluster
aws ecs create-cluster --cluster-name myapp-cluster

# Create service with ALB
aws ecs create-service \
  --cluster myapp-cluster \
  --service-name myapp-service \
  --task-definition myapp-task \
  --desired-count 2 \
  --launch-type FARGATE \
  --network-configuration "awsvpcConfiguration={subnets=[subnet-xxx],securityGroups=[sg-xxx],assignPublicIp=ENABLED}" \
  --load-balancers "targetGroupArn=arn:aws:elasticloadbalancing:...,containerName=myapp,containerPort=8080"

Deployment Workflow
1. Build and Push
# Build new version
docker build -t myapp:${VERSION} .

# Tag and push
docker tag myapp:${VERSION} ${ECR_REPO}:${VERSION}
docker tag myapp:${VERSION} ${ECR_REPO}:latest
docker push ${ECR_REPO}:${VERSION}
docker push ${ECR_REPO}:latest

2. Update Task Definition
# Register new task definition
aws ecs register-task-definition --cli-input-json file://task-definition.json

3. Update Service
# Force new deployment
aws ecs update-service \
  --cluster myapp-cluster \
  --service myapp-service \
  --force-new-deployment

Best Practices
Use Secrets Manager: Store sensitive data in AWS Secrets Manager, reference in task definition
Health Checks: Configure ALB health checks for reliability
Auto-scaling: Set up target tracking based on CPU/memory
Logging: Always use CloudWatch Logs for centralized logging
Tags: Tag all resources for cost tracking and organization
IAM Roles: Use task roles for least-privilege access to AWS services
CI/CD: Integrate with GitHub Actions using OIDC (no long-lived credentials)
Common Commands
# List services
aws ecs list-services --cluster myapp-cluster

# Describe service
aws ecs describe-services --cluster myapp-cluster --services myapp-service

# View logs (requires CloudWatch)
aws logs tail /ecs/myapp --follow

# Scale service
aws ecs update-service --cluster myapp-cluster --service myapp-service --desired-count 4

# Stop all tasks (for maintenance)
aws ecs update-service --cluster myapp-cluster --service myapp-service --desired-count 0

Resources
ECS Task Definitions
Fargate Platform Versions
ECR User Guide
Weekly Installs
33
Repository
dralgorhythm/cl…ramework
GitHub Stars
76
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass