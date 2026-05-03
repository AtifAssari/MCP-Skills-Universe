---
rating: ⭐⭐⭐
title: typespec-create-api-plugin
url: https://skills.sh/github/awesome-copilot/typespec-create-api-plugin
---

# typespec-create-api-plugin

skills/github/awesome-copilot/typespec-create-api-plugin
typespec-create-api-plugin
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill typespec-create-api-plugin
Summary

Generate TypeSpec API plugins for Microsoft 365 Copilot with REST operations, authentication, and Adaptive Cards.

Scaffolds complete TypeSpec projects with agent definitions (main.tsp) and API operations (actions.tsp) following Microsoft 365 Copilot conventions
Supports four authentication modes: public APIs, API key headers, OAuth2 with authorization code flow, and registered auth references
Includes optional confirmation dialogs for destructive operations and Adaptive Card templates for rich response formatting
Provides decorators for operation reasoning, response instructions, and model definitions aligned with RESTful best practices
SKILL.md
Create TypeSpec API Plugin

Create a complete TypeSpec API plugin for Microsoft 365 Copilot that integrates with external REST APIs.

Requirements

Generate TypeSpec files with:

main.tsp - Agent Definition
import "@typespec/http";
import "@typespec/openapi3";
import "@microsoft/typespec-m365-copilot";
import "./actions.tsp";

using TypeSpec.Http;
using TypeSpec.M365.Copilot.Agents;
using TypeSpec.M365.Copilot.Actions;

@agent({
  name: "[Agent Name]",
  description: "[Description]"
})
@instructions("""
  [Instructions for using the API operations]
""")
namespace [AgentName] {
  // Reference operations from actions.tsp
  op operation1 is [APINamespace].operationName;
}

actions.tsp - API Operations
import "@typespec/http";
import "@microsoft/typespec-m365-copilot";

using TypeSpec.Http;
using TypeSpec.M365.Copilot.Actions;

@service
@actions(#{
    nameForHuman: "[API Display Name]",
    descriptionForModel: "[Model description]",
    descriptionForHuman: "[User description]"
})
@server("[API_BASE_URL]", "[API Name]")
@useAuth([AuthType]) // Optional
namespace [APINamespace] {
  
  @route("[/path]")
  @get
  @action
  op operationName(
    @path param1: string,
    @query param2?: string
  ): ResponseModel;

  model ResponseModel {
    // Response structure
  }
}

Authentication Options

Choose based on API requirements:

No Authentication (Public APIs)

// No @useAuth decorator needed


API Key

@useAuth(ApiKeyAuth<ApiKeyLocation.header, "X-API-Key">)


OAuth2

@useAuth(OAuth2Auth<[{
  type: OAuth2FlowType.authorizationCode;
  authorizationUrl: "https://oauth.example.com/authorize";
  tokenUrl: "https://oauth.example.com/token";
  refreshUrl: "https://oauth.example.com/token";
  scopes: ["read", "write"];
}]>)


Registered Auth Reference

@useAuth(Auth)

@authReferenceId("registration-id-here")
model Auth is ApiKeyAuth<ApiKeyLocation.header, "X-API-Key">

Function Capabilities
Confirmation Dialog
@capabilities(#{
  confirmation: #{
    type: "AdaptiveCard",
    title: "Confirm Action",
    body: """
    Are you sure you want to perform this action?
      * **Parameter**: {{ function.parameters.paramName }}
    """
  }
})

Adaptive Card Response
@card(#{
  dataPath: "$.items",
  title: "$.title",
  url: "$.link",
  file: "cards/card.json"
})

Reasoning & Response Instructions
@reasoning("""
  Consider user's context when calling this operation.
  Prioritize recent items over older ones.
""")
@responding("""
  Present results in a clear table format with columns: ID, Title, Status.
  Include a summary count at the end.
""")

Best Practices
Operation Names: Use clear, action-oriented names (listProjects, createTicket)
Models: Define TypeScript-like models for requests and responses
HTTP Methods: Use appropriate verbs (@get, @post, @patch, @delete)
Paths: Use RESTful path conventions with @route
Parameters: Use @path, @query, @header, @body appropriately
Descriptions: Provide clear descriptions for model understanding
Confirmations: Add for destructive operations (delete, update critical data)
Cards: Use for rich visual responses with multiple data items
Workflow

Ask the user:

What is the API base URL and purpose?
What operations are needed (CRUD operations)?
What authentication method does the API use?
Should confirmations be required for any operations?
Do responses need Adaptive Cards?

Then generate:

Complete main.tsp with agent definition
Complete actions.tsp with API operations and models
Optional cards/card.json if Adaptive Cards are needed
Weekly Installs
8.3K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn