---
title: azure-usage
url: https://skills.sh/fcakyon/claude-codex-settings/azure-usage
---

# azure-usage

skills/fcakyon/claude-codex-settings/azure-usage
azure-usage
Installation
$ npx skills add https://github.com/fcakyon/claude-codex-settings --skill azure-usage
SKILL.md
Azure MCP Best Practices
Tool Selection
Task	Tool	Example
List resources	mcp__azure__*_list	Storage accounts, Key Vault secrets
Get resource details	mcp__azure__*_get	Container details, database info
Create resources	mcp__azure__*_create	New secrets, storage containers
Query data	mcp__azure__*_query	Log Analytics, Cosmos DB
Common Operations
Storage
storage_accounts_list - List storage accounts
storage_blobs_list - List blobs in container
storage_blobs_upload - Upload file to blob
Key Vault
keyvault_secrets_list - List secrets
keyvault_secrets_get - Get secret value
keyvault_secrets_set - Create/update secret
Cosmos DB
cosmosdb_databases_list - List databases
cosmosdb_containers_list - List containers
cosmosdb_query - Query documents
AKS
aks_clusters_list - List AKS clusters
aks_nodepools_list - List node pools
Monitor
monitor_logs_query - Query Log Analytics
Authentication

Azure MCP uses Azure Identity SDK. Authenticate via:

az login (Azure CLI - recommended)
VS Code Azure extension
Environment variables (service principal)
Reference
Azure MCP Server
Supported Services (40+)
Weekly Installs
46
Repository
fcakyon/claude-…settings
GitHub Stars
657
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass