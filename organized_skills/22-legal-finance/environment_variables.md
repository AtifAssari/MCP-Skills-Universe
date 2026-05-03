---
rating: ⭐⭐
title: environment-variables
url: https://skills.sh/elie222/inbox-zero/environment-variables
---

# environment-variables

skills/elie222/inbox-zero/environment-variables
environment-variables
Installation
$ npx skills add https://github.com/elie222/inbox-zero --skill environment-variables
SKILL.md
Environment Variables

This is how we add environment variables to the project:

Add to .env.example:

NEW_VARIABLE=value_example


Add to apps/web/env.ts:

// For server-only variables
server: {
  NEW_VARIABLE: z.string(),
}
// For client-side variables
client: {
  NEXT_PUBLIC_NEW_VARIABLE: z.string(),
}
experimental__runtimeEnv: {
  NEXT_PUBLIC_NEW_VARIABLE: process.env.NEXT_PUBLIC_NEW_VARIABLE,
}


For client-side variables:

Must be prefixed with NEXT_PUBLIC_
Add to both client and experimental__runtimeEnv sections

Add to turbo.json under globalDependencies:

{
  "tasks": {
    "build": {
      "env": [
        "NEW_VARIABLE"
      ]
    }
  }
}


examples:

input: |

Adding a server-side API key
.env.example

API_KEY=your_api_key_here

env.ts

server: { API_KEY: z.string(), }

turbo.json

"build": { "env": ["API_KEY"] } output: "Server-side environment variable properly added"

input: |

Adding a client-side feature flag
.env.example

NEXT_PUBLIC_FEATURE_ENABLED=false

env.ts

client: { NEXT_PUBLIC_FEATURE_ENABLED: z.coerce.boolean().default(false), }, experimental__runtimeEnv: { NEXT_PUBLIC_FEATURE_ENABLED: process.env.NEXT_PUBLIC_FEATURE_ENABLED, }

turbo.json

"build": { "env": ["NEXT_PUBLIC_FEATURE_ENABLED"] } output: "Client-side environment variable properly added"

references:

apps/web/env.ts
apps/web/.env.example
turbo.json
Weekly Installs
19
Repository
elie222/inbox-zero
GitHub Stars
10.6K
First Seen
Mar 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass