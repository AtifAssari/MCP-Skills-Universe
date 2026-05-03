---
rating: ⭐⭐
title: ecs-express
url: https://skills.sh/jritsema/ecs-express-power/ecs-express
---

# ecs-express

skills/jritsema/ecs-express-power/ecs-express
ecs-express
Installation
$ npx skills add https://github.com/jritsema/ecs-express-power --skill ecs-express
SKILL.md
ECS Express Mode Power
Overview

Assists with deploying a web app or API to AWS using Amazon ECS Express Mode. ECS Express Mode takes your container image and gives you back an HTTPS endpoint.

Key capabilities:

Builds your project into a container: Builds your Dockerfile into a container image using Docker
Deploys your project to AWS: Deploys your container to AWS using Amazon ECS Express Mode
Assists with troubleshooting: Assists with troubleshooting issues with your workload in AWS
Onboarding
Step 1: Validate tools

This skill requires the following tools to be installed:

AWS CLI
Docker CLI
AWS Credentials

If you have to use shell commands (for example, docker login) you may encounter aws credentials issues. If you do, ask the user if they'd like to use an aws profile, or prompt them to enter their credentials inside your shell.

Instructions

Your job is to help the user deploy their web app or API to AWS as an Amazon ECS Express Mode service.

Identify app-specific inputs

Search the user's codebase to identify the following input parameters that you'll need to create the ECS Express Mode service:

service name: use the current directory name
port: the port the web app/API server listens on
health check: the endpoint the web app/API server uses to signal health
envvars: any required environment variables

Before proceeding further, present these values to the user and explain that you'll use these values for the ECS Express Mode service.

Ask the user if they'd like to create a docker compose file (compose.yml) that can be used to test the container locally before deploying to AWS. This can help identify common issues first before deploying to the cloud. This can also be a place to source environment variables from. The compose file should look like this, using the variables above for app and ports:

services:
  app:
    build: .
    ports:
      - "8080:8080"
    environment:
      - PORT=8080

AWS Settings

Now ask the user if they would like to specify the amount of cpu and memory their container gets allocated.

Ask the user if they have any additional environment variables they want to include.

Ask the user if they'd like to specify the number of containers running behind the load balancer, or just use the default of 1.

Ask the user if they already have an image in ECR they'd like to deploy. If not, offer to create a new ECR repository (using the service name as the repo name) and then build and push the app image.

Do not proceed without stopping to get confirmation from the user on these things.

Note that ECS Express Mode currently only supports linux/amd64 images, so build for that architecture.

Generate a unique string to use as the image tag using the current datetime.

If they don't already exist, create the following IAM roles with the related attached policies:

ecsTaskExecutionRole - arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy
ecsInfrastructureRoleForExpressServices arn:aws:iam::aws:policy/service-role/AmazonECSInfrastructureRoleforExpressGatewayServices

When creating, updating, or deleting the ECS Express Mode service use only these APIs:

create-express-gateway-service
update-express-gateway-service
delete-express-gateway-service
describe-express-gateway-service

Here's an example of how to use the create-express-gateway-service API:

aws ecs create-express-gateway-service \
    --execution-role-arn arn:aws:iam::123456789012:role/ecsTaskExecutionRole \
    --infrastructure-role-arn arn:aws:iam::123456789012:role/ecsInfrastructureRoleForExpressServices \
    --primary-container '{
        "image": "123456789012.dkr.ecr.region.amazonaws.com/my-app:latest",
        "containerPort": 8080,
        "environment": [{
            "name": "ENV",
            "value": "Prod"
        },
        {
            "name": "DEBUG",
            "value": "false"
        }]
    }' \
    --service-name "my-web-app" \
    --cpu "1024" \
    --memory "2048" \
    --health-check-path "/health" \
    --scaling-target '{"minTaskCount":1,"maxTaskCount":10}'

After creating the ECS Express Mode service

Monitor deployment - Check the ECS service status every 60 seconds using the ECS describe-services API until the rollout state is COMPLETED.

Allow for ALB setup - Even after deployment completes, expect up to an additional minute for the ALB to configure target groups and register instances. You can use the describe-target-health API to check if the targets are healthy.

Test the endpoint - Once the ALB is fully configured, curl the health check endpoint to verify it works. Note that you may see HTTP 503 statuses during this time, this is normal.

If the user asks for help with troubleshooting, you can use the ecs troubleshooting tools to check the status and troubleshoot any potential issues.

Performing updates

When making any changes to the deployment, re-build and push the container image, and be sure to always use the express mode update tool. Do not use the traditional ECS APIs like update-service.

After the initial deployment is complete, explain to the user that ECS Express Mode defaults to blue/green canary style deployments. The default deployment strategy can take up to 10 minutes for updates to allow for traffic shifting and plenty of bake time. Explain to the user that you can speed up deployments by reducing the bake time and traffic shifting. Confirm with the user that they want this, and if they do, so run the following command (substitute actual cluster and service arns).

aws ecs update-service \
  --cluster <cluster-name> \
  --service <service-name> \
  --deployment-configuration '{
    "bakeTimeInMinutes": 0,
    "canaryConfiguration": {
      "canaryPercent": 100.0,
      "canaryBakeTimeInMinutes": 0
    }
  }'

Cleaning up

If the user wants to delete the service use the express mode delete API. Offer to delete the ECR repo as well.

Weekly Installs
20
Repository
jritsema/ecs-ex…ss-power
GitHub Stars
2
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail