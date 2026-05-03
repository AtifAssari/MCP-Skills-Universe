---
rating: ⭐⭐
title: yarp
url: https://skills.sh/stuartf303/sorcha/yarp
---

# yarp

skills/stuartf303/sorcha/yarp
yarp
Installation
$ npx skills add https://github.com/stuartf303/sorcha --skill yarp
SKILL.md
YARP Skill

YARP (Yet Another Reverse Proxy) is the .NET reverse proxy used for API gateway routing in Sorcha. The gateway routes external requests to internal microservices while handling path transformations, security headers, and CORS. Key pattern: gateway-specific endpoints execute BEFORE MapReverseProxy() which must be called last.

Quick Start
Basic Setup
// Program.cs - Add YARP with configuration-based routes
builder.Services.AddReverseProxy()
    .LoadFromConfig(builder.Configuration.GetSection("ReverseProxy"));

// CRITICAL: MapReverseProxy() must be called LAST
app.MapReverseProxy();

Route Configuration
{
  "ReverseProxy": {
    "Routes": {
      "blueprint-route": {
        "ClusterId": "blueprint-cluster",
        "Match": { "Path": "/api/blueprint/{**catch-all}" },
        "Transforms": [{ "PathPattern": "/api/{**catch-all}" }]
      }
    },
    "Clusters": {
      "blueprint-cluster": {
        "Destinations": {
          "destination1": { "Address": "http://blueprint-service:8080" }
        }
      }
    }
  }
}

Key Concepts
Concept	Usage	Example
Route	Maps external path to cluster	"Path": "/api/blueprint/{**catch-all}"
Cluster	Backend service destination(s)	"Address": "http://service:8080"
Transform	Rewrites path before forwarding	"PathPattern": "/api/{**catch-all}"
Catch-all	Captures remaining path segments	{**catch-all} or {*any}
Common Patterns
Path Prefix Stripping

When: External API has service prefix, backend doesn't

{
  "Match": { "Path": "/api/blueprint/{**catch-all}" },
  "Transforms": [{ "PathPattern": "/api/{**catch-all}" }]
}


Request: GET /api/blueprint/blueprints → Backend: GET /api/blueprints

Health Endpoint Mapping

When: Unified health checks across services

{
  "blueprint-status-route": {
    "ClusterId": "blueprint-cluster",
    "Match": { "Path": "/api/blueprint/status" },
    "Transforms": [{ "PathPattern": "/api/health" }]
  }
}

X-Forwarded Headers

When: Backend needs original client info

"Transforms": [
  { "PathPattern": "/api/{**catch-all}" },
  { "X-Forwarded": "Set" }
]

See Also
patterns - Route patterns and transformations
workflows - Setup and testing workflows
Related Skills
See the aspire skill for service discovery integration
See the minimal-apis skill for gateway-specific endpoints
See the jwt skill for authentication pass-through
See the docker skill for container networking
Documentation Resources

Fetch latest YARP documentation with Context7.

How to use Context7:

Use mcp__context7__resolve-library-id to search for "yarp"
Query with mcp__context7__query-docs using the resolved library ID

Library ID: /dotnet/yarp

Recommended Queries:

"YARP configuration routes clusters transforms"
"YARP load balancing health checks"
"YARP request transforms path rewriting"
Weekly Installs
24
Repository
stuartf303/sorcha
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass