---
title: aws-cost-operations
url: https://skills.sh/zxkane/aws-skills/aws-cost-operations
---

# aws-cost-operations

skills/zxkane/aws-skills/aws-cost-operations
aws-cost-operations
Installation
$ npx skills add https://github.com/zxkane/aws-skills --skill aws-cost-operations
SKILL.md
Contains Hooks

This skill uses Claude hooks which can execute code automatically in response to events. Review carefully before installing.

AWS Cost & Operations

This skill provides comprehensive guidance for AWS cost optimization, monitoring, observability, and operational excellence with integrated MCP servers.

AWS Documentation Requirement

Always verify AWS facts using MCP tools (mcp__aws-mcp__* or mcp__*awsdocs*__*) before answering. The aws-mcp-setup dependency is auto-loaded — if MCP tools are unavailable, guide the user through that skill's setup flow.

Integrated MCP Servers

This plugin provides 3 MCP servers:

Bundled Servers
1. AWS Pricing MCP Server (pricing)

Purpose: Pre-deployment cost estimation and optimization

Estimate costs before deploying resources
Compare pricing across regions
Calculate Total Cost of Ownership (TCO)
Evaluate different service options for cost efficiency
2. AWS Cost Explorer MCP Server (costexp)

Purpose: Detailed cost analysis and reporting

Analyze historical spending patterns
Identify cost anomalies and trends
Forecast future costs
Analyze cost by service, region, or tag
3. Amazon CloudWatch MCP Server (cw)

Purpose: Metrics, alarms, and logs analysis

Query CloudWatch metrics and logs
Create and manage CloudWatch alarms
Troubleshoot operational issues
Monitor resource utilization

Note: The following servers are available separately via the Full AWS MCP Server (see aws-mcp-setup skill) and are not bundled with this plugin:

AWS Billing and Cost Management MCP — Real-time billing details
CloudWatch Application Signals MCP — APM and SLOs
AWS Managed Prometheus MCP — PromQL queries for containers
AWS CloudTrail MCP — API activity audit
AWS Well-Architected Security Assessment MCP — Security posture assessment
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
300
Repository
zxkane/aws-skills
GitHub Stars
265
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass