---
rating: ⭐⭐⭐
title: microsoft-code-reference
url: https://skills.sh/github/awesome-copilot/microsoft-code-reference
---

# microsoft-code-reference

skills/github/awesome-copilot/microsoft-code-reference
microsoft-code-reference
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill microsoft-code-reference
Summary

Verify Microsoft SDK methods, find working code samples, and catch hallucinated APIs against official docs.

Three core tools: microsoft_docs_search for API lookups, microsoft_code_sample_search for working examples in C#/Python/JavaScript, and microsoft_docs_fetch for full reference pages with overloads
Catches common mistakes like wrong method signatures, deprecated patterns, mismatched SDK versions (v11 vs v12), and incorrect package names
Works with Azure SDKs, .NET libraries, and Microsoft Graph APIs; falls back to mslearn CLI if the Learn MCP Server is unavailable
Recommended workflow: confirm method exists, fetch full details for complex parameters, then find a working sample before writing code
SKILL.md
Microsoft Code Reference
Tools
Need	Tool	Example
API method/class lookup	microsoft_docs_search	"BlobClient UploadAsync Azure.Storage.Blobs"
Working code sample	microsoft_code_sample_search	query: "upload blob managed identity", language: "python"
Full API reference	microsoft_docs_fetch	Fetch URL from microsoft_docs_search (for overloads, full signatures)
Finding Code Samples

Use microsoft_code_sample_search to get official, working examples:

microsoft_code_sample_search(query: "upload file to blob storage", language: "csharp")
microsoft_code_sample_search(query: "authenticate with managed identity", language: "python")
microsoft_code_sample_search(query: "send message service bus", language: "javascript")


When to use:

Before writing code—find a working pattern to follow
After errors—compare your code against a known-good sample
Unsure of initialization/setup—samples show complete context
API Lookups
# Verify method exists (include namespace for precision)
"BlobClient UploadAsync Azure.Storage.Blobs"
"GraphServiceClient Users Microsoft.Graph"

# Find class/interface
"DefaultAzureCredential class Azure.Identity"

# Find correct package
"Azure Blob Storage NuGet package"
"azure-storage-blob pip package"


Fetch full page when method has multiple overloads or you need complete parameter details.

Error Troubleshooting

Use microsoft_code_sample_search to find working code samples and compare with your implementation. For specific errors, use microsoft_docs_search and microsoft_docs_fetch:

Error Type	Query
Method not found	"[ClassName] methods [Namespace]"
Type not found	"[TypeName] NuGet package namespace"
Wrong signature	"[ClassName] [MethodName] overloads" → fetch full page
Deprecated warning	"[OldType] migration v12"
Auth failure	"DefaultAzureCredential troubleshooting"
403 Forbidden	"[ServiceName] RBAC permissions"
When to Verify

Always verify when:

Method name seems "too convenient" (UploadFile vs actual Upload)
Mixing SDK versions (v11 CloudBlobClient vs v12 BlobServiceClient)
Package name doesn't follow conventions (Azure.* for .NET, azure-* for Python)
Using an API for the first time
Validation Workflow

Before generating code using Microsoft SDKs, verify it's correct:

Confirm method or package exists — microsoft_docs_search(query: "[ClassName] [MethodName] [Namespace]")
Fetch full details (for overloads/complex params) — microsoft_docs_fetch(url: "...")
Find working sample — microsoft_code_sample_search(query: "[task]", language: "[lang]")

For simple lookups, step 1 alone may suffice. For complex API usage, complete all three steps.

CLI Alternative

If the Learn MCP server is not available, use the mslearn CLI from a terminal or shell (for example, Bash, PowerShell, or cmd) instead:

# Run directly (no install needed)
npx @microsoft/learn-cli search "BlobClient UploadAsync Azure.Storage.Blobs"

# Or install globally, then run
npm install -g @microsoft/learn-cli
mslearn search "BlobClient UploadAsync Azure.Storage.Blobs"

MCP Tool	CLI Command
microsoft_docs_search(query: "...")	mslearn search "..."
microsoft_code_sample_search(query: "...", language: "...")	mslearn code-search "..." --language ...
microsoft_docs_fetch(url: "...")	mslearn fetch "..."

Pass --json to search or code-search to get raw JSON output for further processing.

Weekly Installs
9.9K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass