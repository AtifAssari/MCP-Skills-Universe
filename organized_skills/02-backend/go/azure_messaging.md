---
rating: ⭐⭐
title: azure-messaging
url: https://skills.sh/microsoft/azure-skills/azure-messaging
---

# azure-messaging

skills/microsoft/azure-skills/azure-messaging
azure-messaging
Installation
$ npx skills add https://github.com/microsoft/azure-skills --skill azure-messaging
Summary

Diagnose and resolve Azure Event Hubs and Service Bus SDK issues with structured troubleshooting workflows.

Covers connection failures, authentication errors, AMQP link issues, message lock timeouts, and event processor stalls across Python, Java, JavaScript, and .NET SDKs
Includes language-specific troubleshooting guides for Event Hubs and Service Bus, plus connectivity diagnostics for ports, WebSocket fallback, IP firewalls, and private endpoints
Provides MCP tools to query resource health, list namespaces/hubs/queues/topics, and search Microsoft Learn documentation for error resolution
Structured diagnosis workflow: identify SDK version, check resource health, match error messages, look up docs, verify configuration, and apply fixes
SKILL.md
Azure Messaging SDK Troubleshooting
Quick Reference
Property	Value
Services	Azure Event Hubs, Azure Service Bus
MCP Tools	mcp_azure_mcp_eventhubs, mcp_azure_mcp_servicebus
Best For	Diagnosing SDK connection, auth, and message processing issues
When to Use This Skill
SDK connection failures, auth errors, or AMQP link errors
Idle timeout, connection inactivity, or slow reconnection after disconnect
AMQP link detach or detach-forced errors
Message lock lost, message lock expired, lock renewal failures, or batch lock timeouts
Session lock lost, session lock expired, or session receiver errors
Event processor or message handler stops processing
Duplicate events or checkpoint offset resets
SDK configuration questions (retry, prefetch, batch size, receive batch behavior)
MCP Tools
Tool	Command	Use
mcp_azure_mcp_eventhubs	Namespace/hub ops	List namespaces, hubs, consumer groups
mcp_azure_mcp_servicebus	Queue/topic ops	List namespaces, queues, topics, subscriptions
mcp_azure_mcp_monitor	logs_query	Query diagnostic logs with KQL
mcp_azure_mcp_resourcehealth	get	Check service health status
mcp_azure_mcp_documentation	Doc search	Search Microsoft Learn for troubleshooting docs
Diagnosis Workflow
Identify the SDK and version — Check the prompt for SDK and version clues; if not stated, proceed with diagnosis and ask later if needed
Check resource health — Use mcp_azure_mcp_resourcehealth to verify the namespace is healthy
Review the error message — Match against language-specific troubleshooting guide
Look up documentation — Use mcp_azure_mcp_documentation to search Microsoft Learn for the error or topic
Check configuration — Verify connection string, entity name, consumer group
Recommend fix — Apply remediation, citing documentation found
Troubleshooting Guides

Connectivity, SDK, and auth troubleshooting guides are located in the azure-diagnostics skill under troubleshooting/messaging/.

References
Use mcp_azure_mcp_documentation to search Microsoft Learn for latest guidance.
Weekly Installs
275.8K
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