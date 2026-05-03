---
rating: ⭐⭐
title: fabric-onelake-2025
url: https://skills.sh/josiahsiegel/claude-plugin-marketplace/fabric-onelake-2025
---

# fabric-onelake-2025

skills/josiahsiegel/claude-plugin-marketplace/fabric-onelake-2025
fabric-onelake-2025
Installation
$ npx skills add https://github.com/josiahsiegel/claude-plugin-marketplace --skill fabric-onelake-2025
SKILL.md
Microsoft Fabric Integration with Azure Data Factory (2025)
Overview

Microsoft Fabric is a unified SaaS analytics platform combining Power BI, Azure Synapse Analytics, and Azure Data Factory capabilities. ADF provides native connectors for Fabric Lakehouse and Fabric Warehouse, enabling seamless data movement between ADF and Fabric workspaces.

Microsoft Fabric Lakehouse Connector

The Fabric Lakehouse connector enables read and write operations to Microsoft Fabric Lakehouse for tables and files.

Supported Activities
Activity	Supported
Copy Activity (source and sink)	Yes
Lookup Activity	Yes
Get Metadata Activity	Yes
Delete Activity	Yes
Quick Reference
Linked service type: Lakehouse
Authentication: Managed Identity (preferred) or Service Principal
Required IDs: workspaceId and artifactId
Sink types: LakehouseTableSink (tables), LakehouseFileSink (files)
Source type: LakehouseTableSource
Table action options: append or overwrite

Finding Workspace and Artifact IDs:

Navigate to Fabric workspace in browser
Copy workspace ID from URL: https://app.powerbi.com/groups/<workspaceId>/...
Open Lakehouse settings to find artifact ID
Or use Fabric REST API to enumerate workspace items

For complete linked service, dataset, and copy activity JSON examples, see references/lakehouse-examples.md.

Microsoft Fabric Warehouse Connector

The Fabric Warehouse connector provides T-SQL based data warehousing capabilities within the Fabric ecosystem.

Supported Activities
Activity	Supported
Copy Activity (source and sink)	Yes
Lookup Activity	Yes
Get Metadata Activity	Yes
Script Activity	Yes
Stored Procedure Activity	Yes
Quick Reference
Linked service type: Warehouse
Authentication: System-Assigned Managed Identity (recommended), User-Assigned MI, or Service Principal
Required properties: endpoint, warehouse
Sink type: WarehouseSink
Write behaviors: insert or upsert
Table option: autoCreate (creates table if missing)

For complete linked service, copy activity, stored procedure, and script activity JSON examples, see references/warehouse-examples.md.

OneLake Integration Patterns

ADF supports three integration patterns with OneLake:

Pattern	Description	Key Benefit
ADLS Gen2 Shortcuts	Reference ADLS data via OneLake shortcuts (zero-copy)	No data duplication
Incremental Load	Watermark-based incremental copy to Lakehouse	Efficient updates
Cross-Platform Invoke	Use InvokePipeline activity to call Fabric pipelines	Hybrid orchestration

OneLake Shortcuts are the preferred approach when data already exists in ADLS Gen2 -- they provide instant zero-copy access without data movement. Use ADF Copy Activity only when data transformation or format conversion is needed.

For complete pipeline JSON examples for all three patterns, see references/onelake-patterns.md.

Permission Configuration
Azure Data Factory Managed Identity Permissions in Fabric

For Fabric Lakehouse:

Open Fabric workspace
Go to Workspace settings -> Manage access
Add ADF managed identity with Contributor role
Or assign Workspace Admin for full access

For Fabric Warehouse:

Navigate to Warehouse SQL endpoint
Execute SQL to create user:
CREATE USER [your-adf-name] FROM EXTERNAL PROVIDER;
ALTER ROLE db_datareader ADD MEMBER [your-adf-name];
ALTER ROLE db_datawriter ADD MEMBER [your-adf-name];

Service Principal Permissions

App Registration Setup:

Register app in Microsoft Entra ID
Create client secret (store in Key Vault)
Add app to Fabric workspace with Contributor role
For Warehouse, create SQL user as shown above
Best Practices (2025)

Use Managed Identity -- System-assigned for single ADF, user-assigned for multiple. Avoid service principal keys when possible. Store any secrets in Key Vault.

Enable Staging for Large Loads -- Use staging with compression for data volumes > 1 GB, complex transformations, or Fabric Warehouse loads.

Leverage OneLake Shortcuts -- Use ADLS Gen2 -> OneLake Shortcut -> Direct Access instead of ADLS Gen2 -> Copy Activity -> Lakehouse. No data movement, instant availability, reduced costs.

Monitor Fabric Capacity Units (CU) -- Track CU consumption per pipeline run, peak usage, and throttling. Optimize with incremental loads, off-peak scheduling, and right-sized parallelism.

Use Table Option AutoCreate -- Set tableOption: "autoCreate" on WarehouseSink for automatic schema management and faster development.

Implement Error Handling -- Configure retry policies on Copy activities and add WebActivity-based failure logging with dependencyConditions: ["Failed"].

Common Issues and Solutions
Issue	Error Message	Solution
Permission Denied	"User does not have permission to access Fabric workspace"	Add ADF managed identity as Contributor; for Warehouse, create SQL user; allow 5 min propagation
Endpoint Not Found	"Unable to connect to endpoint"	Verify workspaceId/artifactId; check workspace URL; ensure Lakehouse/Warehouse is not paused
Schema Mismatch	"Column types do not match"	Use tableOption: "autoCreate" or explicit column mappings in translator
Performance Degradation	Slow copy performance	Enable staging, increase parallelCopies (4-8), increase DIUs (8-32), check CU throttling
Resources
Fabric Lakehouse Connector
Fabric Warehouse Connector
OneLake Documentation
Fabric Capacity Management
ADF to Fabric Integration Guide
Progressive Disclosure References
Lakehouse Examples: references/lakehouse-examples.md - Complete linked service, dataset, copy activity, and lookup JSON examples
Warehouse Examples: references/warehouse-examples.md - Complete linked service, copy activity, stored procedure, and script activity JSON examples
OneLake Patterns: references/onelake-patterns.md - Pipeline patterns for shortcuts, incremental loads, and cross-platform Invoke Pipeline
Weekly Installs
88
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