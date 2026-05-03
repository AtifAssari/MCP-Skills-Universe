---
rating: ⭐⭐
title: databricks-2025
url: https://skills.sh/josiahsiegel/claude-plugin-marketplace/databricks-2025
---

# databricks-2025

skills/josiahsiegel/claude-plugin-marketplace/databricks-2025
databricks-2025
Installation
$ npx skills add https://github.com/josiahsiegel/claude-plugin-marketplace --skill databricks-2025
SKILL.md
Azure Data Factory Databricks Integration 2025
Databricks Job Activity (Recommended 2025)

CRITICAL UPDATE (2025): The Databricks Job activity is now the ONLY recommended method for orchestrating Databricks in ADF. Microsoft strongly recommends migrating from legacy Notebook, Python, and JAR activities.

Quick Reference
Activity type: DatabricksJob (NOT DatabricksSparkJob or DatabricksNotebook)
Parameter property: jobParameters (NOT parameters)
Linked service auth: Managed Identity ("authentication": "MSI") recommended
Cluster config: Do NOT specify cluster properties in linked service; the Databricks Job controls compute
Why Databricks Job Activity?
Feature	Notebook Activity (Legacy)	Job Activity (2025)
Compute	Must configure cluster in linked service	Serverless by default
Workflow tasks	Single notebook	Multi-task DAGs (notebook, Python, SQL, DLT)
Retry	ADF-level only	Job-level + task-level
Repair runs	Not supported	Rerun failed tasks only
Git integration	Limited	Full Databricks Git support + DABs
Lineage	None	Built-in data lineage
If/Else logic	Must use ADF control flow	Native If/Else task types
Benefits Summary
Serverless Execution -- No cluster specification needed; automatic serverless compute with faster startup and lower costs
Advanced Workflow Features -- Run As, Task Values, Conditional Execution, AI/BI Tasks, Repair Runs, Notifications, Queuing
Centralized Job Management -- Jobs defined once in Databricks workspace; single source of truth with Git-backed versioning
Cost Optimization -- Serverless compute (pay only for execution), job clusters (auto-terminating), spot instance support

For complete JSON examples of Job activity, linked service, and pipeline configurations, see references/databricks-job-examples.md.

Connectors and Enhancements (2025+)
ServiceNow V2 Connector (RECOMMENDED - V1 End of Support)

ServiceNow V1 connector is at End of Support. Migrate to V2 immediately.

Feature	V1	V2
Linked service type	ServiceNow	ServiceNowV2
Source type	ServiceNowSource	ServiceNowV2Source
Query builder	Custom	Aligns with ServiceNow condition builder
Performance	Standard	Enhanced extraction
OData support	No	Yes

Migration steps: Update linked service type to ServiceNowV2, update source type to ServiceNowV2Source, test queries in ServiceNow UI condition builder, adjust timeouts.

Enhanced PostgreSQL Connector

Improved performance with 2025 SSL enhancements: enableSsl: true, sslMode: "Require".

Enhanced Snowflake Connector

Improved performance with KeyPair authentication support and Key Vault secret integration.

Managed Identity for Azure Storage

New managed identity support for Azure Table Storage and Azure Files connectors (system-assigned and user-assigned).

Mapping Data Flows - Spark 3.3

Spark 3.3 now powers Mapping Data Flows with 30% faster processing, Adaptive Query Execution (AQE), dynamic partition pruning, improved caching, and better column statistics.

Azure DevOps Server 2022 Support

Git integration now supports on-premises Azure DevOps Server 2022 via the hostName property.

For complete JSON examples of all connectors, see references/connector-examples.md.

Managed Identity 2025 Best Practices
User-Assigned vs System-Assigned
Scenario	Recommendation
Single ADF, simple setup	System-assigned
Multiple data factories	User-assigned (shared identity)
Complex multi-environment	User-assigned
Granular permission control	User-assigned
Identity lifecycle independence	User-assigned

Use ADF's centralized Credentials feature to consolidate Microsoft Entra ID-based credentials across multiple linked services.

MFA Enforcement (Enforced Since October 2025)

Azure MFA is mandatory for all interactive user logins. Impact on ADF:

Managed identities are UNAFFECTED -- no MFA required for service accounts
Service principals with certificate auth are the recommended alternative to secrets
All interactive user logins require MFA
Principle of Least Privilege
Resource	Source Role	Sink Role
Storage Blob	Storage Blob Data Reader	Storage Blob Data Contributor
SQL Database	db_datareader	db_datareader + db_datawriter
Key Vault	Get secrets only	Get secrets only

For complete managed identity JSON examples, see references/connector-examples.md.

Best Practices (2025)

Use Databricks Job Activity (MANDATORY) -- Stop using Notebook, Python, JAR activities. Define workflows in Databricks workspace with serverless compute.

Managed Identity Authentication (MANDATORY) -- Use managed identities for ALL Azure resources. Leverage Credentials feature for consolidation. MFA-compliant since October 2025.

Monitor Job Execution -- Track Databricks Job run IDs from ADF output, log parameters for auditability, set up alerts for failures, leverage built-in lineage.

Optimize Spark 3.3 (Data Flows) -- Enable AQE, use 4-8 partitions per core, broadcast joins for small dimensions, dynamic partition pruning.

Resources
Databricks Job Activity
ADF Connectors
Managed Identity Authentication
Mapping Data Flows
Progressive Disclosure References
Databricks Job Examples: references/databricks-job-examples.md - Complete JSON for Job activity, linked services, pipeline, and Databricks workspace job definition
Connector Examples: references/connector-examples.md - Complete JSON for ServiceNow V2, PostgreSQL, Snowflake, Azure Storage MI, Mapping Data Flows, and Azure DevOps Server
Weekly Installs
92
Repository
josiahsiegel/cl…ketplace
GitHub Stars
33
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass