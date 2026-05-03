---
title: azure-storage
url: https://skills.sh/microsoft/azure-skills/azure-storage
---

# azure-storage

skills/microsoft/azure-skills/azure-storage
azure-storage
Installation
$ npx skills add https://github.com/microsoft/azure-skills --skill azure-storage
Summary

Unified access to Azure blob storage, file shares, queues, tables, and data lake services.

Supports five storage service types: Blob Storage for objects and backups, File Shares for SMB access, Queue Storage for async messaging, Table Storage for NoSQL key-value data, and Data Lake for big data analytics
MCP server tools enable listing storage accounts, containers, and blobs, plus downloading and uploading blob content directly
Configurable access tiers (hot, cool, cold, archive) and redundancy options (LRS, ZRS, GRS, GZRS) for cost and durability optimization
CLI fallback available via az storage commands when MCP is not enabled; SDK references provided for Python, TypeScript, Java, Rust, and Go
SKILL.md
Azure Storage Services
Services
Service	Use When	MCP Tools	CLI
Blob Storage	Objects, files, backups, static content	azure__storage	az storage blob
File Shares	SMB file shares, lift-and-shift	-	az storage file
Queue Storage	Async messaging, task queues	-	az storage queue
Table Storage	NoSQL key-value (consider Cosmos DB)	-	az storage table
Data Lake	Big data analytics, hierarchical namespace	-	az storage fs
MCP Server (Preferred)

When Azure MCP is enabled:

azure__storage with command storage_account_list - List storage accounts
azure__storage with command storage_container_list - List containers in account
azure__storage with command storage_blob_list - List blobs in container
azure__storage with command storage_blob_get - Download blob content
azure__storage with command storage_blob_put - Upload blob content

If Azure MCP is not enabled: Run /azure:setup or enable via /mcp.

CLI Fallback
# List storage accounts
az storage account list --output table

# List containers
az storage container list --account-name ACCOUNT --output table

# List blobs
az storage blob list --account-name ACCOUNT --container-name CONTAINER --output table

# Download blob
az storage blob download --account-name ACCOUNT --container-name CONTAINER --name BLOB --file LOCAL_PATH

# Upload blob
az storage blob upload --account-name ACCOUNT --container-name CONTAINER --name BLOB --file LOCAL_PATH

Storage Account Tiers
Tier	Use Case	Performance
Standard	General purpose, backup	Milliseconds
Premium	Databases, high IOPS	Sub-millisecond
Blob Access Tiers
Tier	Access Frequency	Cost
Hot	Frequent	Higher storage, lower access
Cool	Infrequent (30+ days)	Lower storage, higher access
Cold	Rare (90+ days)	Lower still
Archive	Rarely (180+ days)	Lowest storage, rehydration required
Redundancy Options
Type	Durability	Use Case
LRS	11 nines	Dev/test, recreatable data
ZRS	12 nines	Regional high availability
GRS	16 nines	Disaster recovery
GZRS	16 nines	Best durability
Service Details

For deep documentation on specific services:

Blob storage patterns and lifecycle -> Blob Storage documentation
File shares and Azure File Sync -> Azure Files documentation
Queue patterns and poison handling -> Queue Storage documentation
SDK Quick References

For building applications with Azure Storage SDKs, see the condensed guides:

Blob Storage: Python | TypeScript | Java | Rust
Queue Storage: Python | TypeScript
File Shares: Python | TypeScript
Data Lake: Python
Tables: Python | Java

For full package listing across all languages, see SDK Usage Guide.

Azure SDKs

For building applications that interact with Azure Storage programmatically, Azure provides SDK packages in multiple languages (.NET, Java, JavaScript, Python, Go, Rust). See SDK Usage Guide for package names, installation commands, and quick start examples.

Weekly Installs
275.9K
Repository
microsoft/azure-skills
GitHub Stars
796
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass