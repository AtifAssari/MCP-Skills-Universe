---
title: cloud-expense-management
url: https://skills.sh/qodex-ai/ai-agent-skills/cloud-expense-management
---

# cloud-expense-management

skills/qodex-ai/ai-agent-skills/cloud-expense-management
cloud-expense-management
Installation
$ npx skills add https://github.com/qodex-ai/ai-agent-skills --skill cloud-expense-management
SKILL.md
AWS Cost & Operations

This skill provides comprehensive guidance for AWS cost optimization, monitoring, observability, and operational excellence with integrated MCP servers.

AWS Documentation Requirement

CRITICAL: This skill requires AWS MCP tools for accurate, up-to-date AWS information.

Before Answering AWS Questions

Always verify using AWS MCP tools (if available):

mcp__aws-mcp__aws___search_documentation or mcp__*awsdocs*__aws___search_documentation - Search AWS docs
mcp__aws-mcp__aws___read_documentation or mcp__*awsdocs*__aws___read_documentation - Read specific pages
mcp__aws-mcp__aws___get_regional_availability - Check service availability

If AWS MCP tools are unavailable:

Guide user to configure AWS MCP: See AWS MCP Setup Guide
Help determine which option fits their environment:
Has uvx + AWS credentials → Full AWS MCP Server
No Python/credentials → AWS Documentation MCP (no auth)
If cannot determine → Ask user which option to use
Integrated MCP Servers

This skill includes 8 MCP servers automatically configured with the plugin:

Cost Management Servers
1. AWS Billing and Cost Management MCP Server

Purpose: Real-time billing and cost management

View current AWS spending and trends
Analyze billing details across services
Track budget utilization
Monitor cost allocation tags
Review consolidated billing for organizations
2. AWS Pricing MCP Server

Purpose: Pre-deployment cost estimation and optimization

Estimate costs before deploying resources
Compare pricing across regions
Calculate Total Cost of Ownership (TCO)
Evaluate different service options for cost efficiency
Get current pricing information for AWS services
3. AWS Cost Explorer MCP Server

Purpose: Detailed cost analysis and reporting

Analyze historical spending patterns
Create custom cost reports
Identify cost anomalies and trends
Forecast future costs
Analyze cost by service, region, or tag
Generate cost optimization recommendations
Monitoring & Observability Servers
4. Amazon CloudWatch MCP Server

Purpose: Metrics, alarms, and logs analysis

Query CloudWatch metrics and logs
Create and manage CloudWatch alarms
Analyze application performance metrics
Troubleshoot operational issues
Set up custom dashboards
Monitor resource utilization
5. Amazon CloudWatch Application Signals MCP Server

Purpose: Application monitoring and performance insights

Monitor application health and performance
Analyze service-level objectives (SLOs)
Track application dependencies
Identify performance bottlenecks
Monitor service map and traces
6. AWS Managed Prometheus MCP Server

Purpose: Prometheus-compatible monitoring

Query Prometheus metrics
Monitor containerized applications
Analyze Kubernetes workload metrics
Create PromQL queries
Track custom application metrics
Audit & Security Servers
7. AWS CloudTrail MCP Server

Purpose: AWS API activity and audit analysis

Analyze AWS API calls and user activity
Track resource changes and modifications
Investigate security incidents
Audit compliance requirements
Identify unusual access patterns
Review who made what changes when
8. AWS Well-Architected Security Assessment Tool MCP Server

Purpose: Security assessment against Well-Architected Framework

Assess security posture against AWS best practices
Identify security gaps and vulnerabilities
Get security improvement recommendations
Review security pillar compliance
Generate security assessment reports
When to Use This Skill

Use this skill when:

Optimizing AWS costs and reducing spending
Estimating costs before deployment
Monitoring application and infrastructure performance
Setting up observability and alerting
Analyzing spending patterns and trends
Investigating operational issues
Auditing AWS activity and changes
Assessing security posture
Implementing operational excellence
Cost Optimization Best Practices
Pre-Deployment Cost Estimation

Always estimate costs before deploying:

Use AWS Pricing MCP to estimate resource costs
Compare pricing across different regions
Evaluate alternative service options
Calculate expected monthly costs
Plan for scaling and growth

Example workflow:

"Estimate the monthly cost of running a Lambda function with
1 million invocations, 512MB memory, 3-second duration in us-east-1"

Cost Analysis and Optimization

Regular cost reviews:

Use Cost Explorer MCP to analyze spending trends
Identify cost anomalies and unexpected charges
Review costs by service, region, and environment
Compare actual vs. budgeted costs
Generate cost optimization recommendations

Cost optimization strategies:

Right-size over-provisioned resources
Use appropriate storage classes (S3, EBS)
Implement auto-scaling for dynamic workloads
Leverage Savings Plans and Reserved Instances
Delete unused resources and snapshots
Use cost allocation tags effectively
Budget Monitoring

Track spending against budgets:

Use Billing and Cost Management MCP to monitor budgets
Set up budget alerts for threshold breaches
Review budget utilization regularly
Adjust budgets based on trends
Implement cost controls and governance
Monitoring and Observability Best Practices
CloudWatch Metrics and Alarms

Implement comprehensive monitoring:

Use CloudWatch MCP to query metrics and logs
Set up alarms for critical metrics:
CPU and memory utilization
Error rates and latency
Queue depths and processing times
API gateway throttling
Lambda errors and timeouts
Create CloudWatch dashboards for visualization
Use log insights for troubleshooting

Example alarm scenarios:

Lambda error rate > 1%
EC2 CPU utilization > 80%
API Gateway 4xx/5xx error spike
DynamoDB throttled requests
ECS task failures
Application Performance Monitoring

Monitor application health:

Use CloudWatch Application Signals MCP for APM
Track service-level objectives (SLOs)
Monitor application dependencies
Identify performance bottlenecks
Set up distributed tracing
Container and Kubernetes Monitoring

For containerized workloads:

Use AWS Managed Prometheus MCP for metrics
Monitor container resource utilization
Track pod and node health
Create PromQL queries for custom metrics
Set up alerts for container anomalies
Audit and Security Best Practices
CloudTrail Activity Analysis

Audit AWS activity:

Use CloudTrail MCP to analyze API activity
Track who made changes to resources
Investigate security incidents
Monitor for suspicious activity patterns
Audit compliance with policies

Common audit scenarios:

"Who deleted this S3 bucket?"
"Show all IAM role changes in the last 24 hours"
"List failed login attempts"
"Find all actions by a specific user"
"Track modifications to security groups"
Security Assessment

Regular security reviews:

Use Well-Architected Security Assessment MCP
Assess security posture against best practices
Identify security gaps and vulnerabilities
Implement recommended security improvements
Document security compliance

Security assessment areas:

Identity and Access Management (IAM)
Detective controls and monitoring
Infrastructure protection
Data protection and encryption
Incident response preparedness
Using MCP Servers Effectively
Cost Analysis Workflow
Pre-deployment: Use Pricing MCP to estimate costs
Post-deployment: Use Billing MCP to track actual spending
Analysis: Use Cost Explorer MCP for detailed cost analysis
Optimization: Implement recommendations from Cost Explorer
Monitoring Workflow
Setup: Configure CloudWatch metrics and alarms
Monitor: Use CloudWatch MCP to track key metrics
Analyze: Use Application Signals for APM insights
Troubleshoot: Query CloudWatch Logs for issue resolution
Security Workflow
Audit: Use CloudTrail MCP to review activity
Assess: Use Well-Architected Security Assessment
Remediate: Implement security recommendations
Monitor: Track security events via CloudWatch
MCP Usage Best Practices
Cost Awareness: Check pricing before deploying resources
Proactive Monitoring: Set up alarms for critical metrics
Regular Reviews: Analyze costs and performance weekly
Audit Trails: Review CloudTrail logs for compliance
Security First: Run security assessments regularly
Optimize Continuously: Act on cost and performance recommendations
Operational Excellence Guidelines
Cost Optimization
Tag Everything: Use consistent cost allocation tags
Review Monthly: Analyze spending trends and anomalies
Right-size: Match resources to actual usage
Automate: Use auto-scaling and scheduling
Monitor Budgets: Set alerts for cost overruns
Monitoring and Alerting
Critical Metrics: Alert on business-critical metrics
Noise Reduction: Fine-tune thresholds to reduce false positives
Actionable Alerts: Ensure alerts have clear remediation steps
Dashboard Visibility: Create dashboards for key stakeholders
Log Retention: Balance cost and compliance needs
Security and Compliance
Least Privilege: Grant minimum required permissions
Audit Regularly: Review CloudTrail logs for anomalies
Encrypt Data: Use encryption at rest and in transit
Assess Continuously: Run security assessments frequently
Incident Response: Have procedures for security events
Additional Resources

For detailed operational patterns and best practices, refer to the comprehensive reference:

File: references/operations-patterns.md

This reference includes:

Cost optimization strategies
Monitoring and alerting patterns
Observability best practices
Security and compliance guidelines
Troubleshooting workflows
CloudWatch Alarms Reference

File: references/cloudwatch-alarms.md

Common alarm configurations for:

Lambda functions
EC2 instances
RDS databases
DynamoDB tables
API Gateway
ECS services
Application Load Balancers
Weekly Installs
73
Repository
qodex-ai/ai-agent-skills
GitHub Stars
6
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass