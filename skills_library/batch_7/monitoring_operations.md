---
title: monitoring-operations
url: https://skills.sh/acedergren/oci-agent-skills/monitoring-operations
---

# monitoring-operations

skills/acedergren/oci-agent-skills/monitoring-operations
monitoring-operations
Installation
$ npx skills add https://github.com/acedergren/oci-agent-skills --skill monitoring-operations
Summary

OCI monitoring setup, alarm configuration, and troubleshooting for metrics, logs, and observability gaps.

Covers metric namespace patterns, alarm threshold gotchas (sparse data handling, trigger delays), and missing data strategies across OCI services
Provides decision trees for log collection troubleshooting, Service Connector setup, and IAM policy requirements
Highlights critical anti-patterns: metric lag (10-15 minutes), dimension requirements, notification channel setup, and Cloud Guard integration
Includes service-specific metric namespaces and MQL query optimization techniques to avoid rate limiting and performance issues
SKILL.md
OCI Monitoring and Observability - Expert Knowledge
🏗️ Use OCI Landing Zone Terraform Modules

Don't reinvent the wheel. Use oracle-terraform-modules/landing-zone for observability stack.

Landing Zone solves:

❌ Bad Practice #10: No logging, monitoring, notifications (Landing Zone deploys complete observability)
❌ Bad Practice #7: Limited security services (Landing Zone integrates Cloud Guard, VSS, OSMS)

This skill provides: Metrics, alarms, and troubleshooting for monitoring deployed WITHIN a Landing Zone.

⚠️ OCI CLI/API Knowledge Gap

You don't know OCI CLI commands or OCI API structure.

Your training data has limited and outdated knowledge of:

OCI CLI syntax and parameters (updates monthly)
OCI API endpoints and request/response formats
Monitoring service CLI operations (oci monitoring alarm, oci monitoring metric)
Metric namespaces and MQL (Monitoring Query Language)
Latest Logging and Service Connector features

When OCI operations are needed:

Use exact CLI commands from this skill's references
Do NOT guess metric namespace names
Do NOT assume AWS CloudWatch patterns work in OCI
Load reference files for detailed MQL documentation

What you DO know:

General observability concepts
Alerting and threshold design principles
Log aggregation patterns

This skill bridges the gap by providing current OCI-specific monitoring patterns and gotchas.

NEVER Do This

❌ NEVER assume metrics are instant (10-15 minute lag)

Metrics published every 1-5 minutes
Processing delay: 5-10 minutes
Total lag: 10-15 minutes from event to visible metric
Don't debug "missing metrics" within first 15 minutes of resource creation

❌ NEVER use = for alarm thresholds with sparse metrics

# WRONG - alarm never fires if metric has gaps
MetricName[1m].mean() = 0

# RIGHT - handle missing data
MetricName[1m]{dataMissing=zero}.mean() > 0


❌ NEVER forget metric dimensions (causes "no data")

# WRONG - missing required dimension
CPUUtilization[1m].mean()

# RIGHT - include resourceId dimension
CPUUtilization[1m]{resourceId="<instance-ocid>"}.mean()


❌ NEVER set alarm thresholds without trigger delay (alert fatigue)

# BAD - fires on every CPU spike
CPUUtilization[1m].mean() > 80

# BETTER - sustained high CPU
CPUUtilization[5m].mean() > 80
Trigger delay: 5 minutes (fires after 5 consecutive breaches)


❌ NEVER create alarms without notification channels

# WRONG - alarm fires but nobody knows
oci monitoring alarm create ... --destinations '[]'

# RIGHT - always link to notification topic
oci monitoring alarm create ... --destinations '["<notification-topic-ocid>"]'


Cost impact: Undetected outages cost $5,000-50,000/hour in production

❌ NEVER ignore Cloud Guard findings (security audit failure)

Cloud Guard detects misconfigurations BEFORE they become incidents
Integrate Cloud Guard → Notifications → Email/Slack/PagerDuty
Cost impact: $100,000+ per security breach vs $0 for proactive remediation
Metric Namespace Gotchas

OCI Metrics Use Service-Specific Namespaces:

Service	Namespace	Example Metric
Compute	oci_computeagent	CPUUtilization, MemoryUtilization
Autonomous DB	oci_autonomous_database	CpuUtilization, StorageUtilization
Load Balancer	oci_lbaas	HttpRequests, UnHealthyBackendServers
Object Storage	oci_objectstorage	ObjectCount, BytesUploaded

Common Mistake: Using wrong namespace (oci_compute vs oci_computeagent)

Alarm Missing Data Handling
Setting	Behavior	Use When
treatMissingDataAsBreaching	Alarm fires if no data	Critical services (outage = breach)
treatMissingDataAsNotBreaching	Alarm silent if no data	Optional monitoring
{dataMissing=zero}	Treat missing as 0	Counters (requests/sec)
Log Collection Common Gaps

Problem: Logs not showing in Log Analytics

Logs not appearing?
├─ Is log enabled on resource?
│  └─ Compute: oci-compute-agent must be running
│  └─ Function: Logging enabled in function config
│
├─ Is Service Connector configured?
│  └─ Source: Log Group → Target: Log Analytics
│  └─ Check: Service Connector status = ACTIVE
│
├─ IAM policy for Service Connector?
│  └─ "Allow any-user to use log-content in tenancy"
│  └─ "Allow service loganalytics to READ logcontent in tenancy"
│
└─ 10-15 minute ingestion lag?
   └─ Wait before debugging

Metric Query Optimization

Expensive (slow):

# Queries ALL instances
CPUUtilization[1m].mean()


Optimized (filter by dimension):

# Query specific instance
CPUUtilization[1m]{resourceId='<instance-ocid>'}.mean()


Cost: Queries free, but rate limited (1000 req/min)

Progressive Loading References
OCI Monitoring Reference (Official Oracle Documentation)

WHEN TO LOAD oci-monitoring-reference.md:

Need comprehensive list of all OCI service metrics
Understanding MQL (Monitoring Query Language) in depth
Implementing complex alarm conditions and composites
Need official Oracle guidance on Logging and Service Connector
Setting up Log Analytics and APM integration

Do NOT load for:

Quick alarm setup (examples in this skill)
Common metric patterns (tables above)
Troubleshooting decision trees (covered above)
When to Use This Skill
Alarms: threshold configuration, missing data handling, trigger delay
Troubleshooting: metrics not showing, alarms not firing, namespace errors
Log collection: Service Connector, IAM policies, missing logs
Performance: query optimization, dimension filtering
Weekly Installs
1.2K
Repository
acedergren/oci-…t-skills
GitHub Stars
9
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass