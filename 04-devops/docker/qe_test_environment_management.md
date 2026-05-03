---
title: qe-test-environment-management
url: https://skills.sh/proffesor-for-testing/agentic-qe/qe-test-environment-management
---

# qe-test-environment-management

skills/proffesor-for-testing/agentic-qe/qe-test-environment-management
qe-test-environment-management
Installation
$ npx skills add https://github.com/proffesor-for-testing/agentic-qe --skill qe-test-environment-management
SKILL.md
Test Environment Management

<default_to_action> When managing test environments:

DEFINE environment types (local, CI, staging, prod)
CONTAINERIZE with Docker for consistency
ENSURE parity with production (same versions, configs)
MOCK external services (service virtualization)
OPTIMIZE costs (auto-shutdown, spot instances)

Quick Environment Checklist:

Same OS/versions as production
Same database type and version
Same configuration structure
Containers for reproducibility
Auto-shutdown after hours

Critical Success Factors:

"Works on my machine" = environment inconsistency
Infrastructure as Code = repeatable environments
Service virtualization = test without external dependencies </default_to_action>
Quick Reference Card
When to Use
Setting up test infrastructure
Debugging environment-specific failures
Reducing test infrastructure costs
Ensuring dev/prod parity
Environment Types
Type	Purpose	Lifetime
Local	Fast feedback	Developer session
CI	Automated tests	Per build (ephemeral)
Staging	Pre-prod validation	Persistent
Production	Canary/synthetic	Continuous
Dev/Prod Parity Checklist
Item	Must Match
OS	Same version
Database	Same type + version
Dependencies	Same versions
Config	Same structure
Env vars	Same names
Docker for Test Environments
# docker-compose.test.yml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      NODE_ENV: test
      DATABASE_URL: postgres://postgres:password@db:5432/test
    depends_on:
      - db
      - redis

  db:
    image: postgres:15
    environment:
      POSTGRES_DB: test
      POSTGRES_PASSWORD: password

  redis:
    image: redis:7


Run tests in container:

docker-compose -f docker-compose.test.yml up -d
docker-compose -f docker-compose.test.yml exec app npm test
docker-compose -f docker-compose.test.yml down

Infrastructure as Code
# test-environment.tf
resource "aws_instance" "test_server" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.medium"

  tags = {
    Name         = "test-environment"
    Environment  = "test"
    AutoShutdown = "20:00" # Cost optimization
  }
}

resource "aws_rds_instance" "test_db" {
  engine                  = "postgres"
  engine_version          = "15"
  instance_class          = "db.t3.micro"
  backup_retention_period = 0 # No backups needed for test
  skip_final_snapshot     = true
}

Service Virtualization
// Mock external services with WireMock
import { WireMock } from 'wiremock-captain';

const wiremock = new WireMock('http://localhost:8080');

// Mock payment gateway
await wiremock.register({
  request: {
    method: 'POST',
    url: '/charge'
  },
  response: {
    status: 200,
    jsonBody: { transactionId: '12345', status: 'approved' }
  }
});

// Tests use mock instead of real gateway

Cost Optimization
# Auto-shutdown test environments after hours
0 20 * * * aws ec2 stop-instances --instance-ids $(aws ec2 describe-instances \
  --filters "Name=tag:Environment,Values=test" \
  --query "Reservations[].Instances[].InstanceId" --output text)

# Start before work hours
0 7 * * 1-5 aws ec2 start-instances --instance-ids $(aws ec2 describe-instances \
  --filters "Name=tag:Environment,Values=test" \
  --query "Reservations[].Instances[].InstanceId" --output text)


Use spot instances (70% savings):

resource "aws_instance" "test_runner" {
  instance_type = "c5.2xlarge"
  instance_market_options {
    market_type = "spot"
    spot_options {
      max_price = "0.10"
    }
  }
}

Agent-Driven Environment Management
// Provision test environment
await Task("Environment Provisioning", {
  type: 'integration-testing',
  services: ['app', 'db', 'redis', 'mocks'],
  parity: 'production',
  lifetime: '2h'
}, "qe-test-executor");

// Chaos testing in isolated environment
await Task("Chaos Test Environment", {
  baseline: 'staging',
  isolate: true,
  injectFaults: ['network-delay', 'pod-failure']
}, "qe-chaos-engineer");

Agent Coordination Hints
Memory Namespace
aqe/environment-management/
├── configs/*            - Environment configurations
├── parity-checks/*      - Dev/prod parity results
├── cost-reports/*       - Infrastructure costs
└── service-mocks/*      - Service virtualization configs

Fleet Coordination
const envFleet = await FleetManager.coordinate({
  strategy: 'environment-management',
  agents: [
    'qe-test-executor',       // Provision environments
    'qe-performance-tester',  // Environment performance
    'qe-chaos-engineer'       // Resilience testing
  ],
  topology: 'sequential'
});

Related Skills
test-data-management - Data for environments
continuous-testing-shift-left - CI/CD environments
chaos-engineering-resilience - Environment resilience
Remember

Environment inconsistency = flaky tests. "Works on my machine" problems come from: different OS/versions, missing dependencies, configuration differences, data differences.

Infrastructure as Code ensures repeatability. Version control your environment configurations. Spin up identical environments on demand.

With Agents: Agents automatically provision test environments matching production, ensure parity, mock external services, and optimize costs with auto-scaling and auto-shutdown.

Weekly Installs
42
Repository
proffesor-for-t…entic-qe
GitHub Stars
334
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail