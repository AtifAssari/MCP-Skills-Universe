---
title: b2c-mrt
url: https://skills.sh/salesforcecommercecloud/b2c-developer-tooling/b2c-mrt
---

# b2c-mrt

skills/salesforcecommercecloud/b2c-developer-tooling/b2c-mrt
b2c-mrt
Installation
$ npx skills add https://github.com/salesforcecommercecloud/b2c-developer-tooling --skill b2c-mrt
SKILL.md
B2C MRT Skill

Use the b2c CLI to manage Managed Runtime (MRT) projects, environments, bundles, and deployments for PWA Kit storefronts.

Tip: If b2c is not installed globally, use npx @salesforce/b2c-cli instead (e.g., npx @salesforce/b2c-cli mrt bundle deploy).

Command Structure
mrt
├── org (list, b2c)              - Organizations and B2C connections
├── project                      - Project management
│   ├── member                   - Team member management
│   └── notification             - Deployment notifications
├── env                          - Environment management
│   ├── var                      - Environment variables
│   ├── redirect                 - URL redirects
│   └── access-control           - Access control headers
├── bundle                       - Bundle and deployment management
└── user                         - User profile and settings

Quick Examples
Deploy a Bundle
# Push local build to staging
b2c mrt bundle deploy -p my-storefront -e staging

# Push to production with release message
b2c mrt bundle deploy -p my-storefront -e production -m "Release v1.0.0"

# Deploy existing bundle by ID
b2c mrt bundle deploy 12345 -p my-storefront -e production

Manage Environments
# List environments
b2c mrt env list -p my-storefront

# Create a new environment
b2c mrt env create qa -p my-storefront --name "QA Environment"

# Get environment details
b2c mrt env get -p my-storefront -e production

# Invalidate CDN cache
b2c mrt env invalidate -p my-storefront -e production

Environment Variables
# List variables
b2c mrt env var list -p my-storefront -e production

# Set variables
b2c mrt env var set API_KEY=secret DEBUG=true -p my-storefront -e staging

# Delete a variable
b2c mrt env var delete OLD_VAR -p my-storefront -e production

View Deployment History
# List bundles in project
b2c mrt bundle list -p my-storefront

# View deployment history for environment
b2c mrt bundle history -p my-storefront -e production

# Download a bundle artifact
b2c mrt bundle download 12345 -p my-storefront

Project Management
# List projects
b2c mrt project list

# Get project details
b2c mrt project get -p my-storefront

# List project members
b2c mrt project member list -p my-storefront

# Add a member
b2c mrt project member add user@example.com -p my-storefront --role developer

URL Redirects
# List redirects
b2c mrt env redirect list -p my-storefront -e production

# Create a redirect
b2c mrt env redirect create -p my-storefront -e production \
  --from "/old-path" --to "/new-path"

# Clone redirects between environments
b2c mrt env redirect clone -p my-storefront --source staging --target production

Configuration
dw.json

Configure MRT settings in your project's dw.json:

{
  "mrtProject": "my-storefront",
  "mrtEnvironment": "staging"
}

Environment Variables
export MRT_API_KEY=your-api-key
export MRT_PROJECT=my-storefront
export MRT_ENVIRONMENT=staging

~/.mobify Config

Store your API key in ~/.mobify:

{
  "api_key": "your-mrt-api-key"
}

Detailed References
Project Commands - Projects, members, and notifications
Environment Commands - Environments, variables, redirects
Bundle Commands - Deployments, history, downloads
More Commands

See b2c mrt --help for a full list of available commands and options.

Weekly Installs
78
Repository
salesforcecomme…-tooling
GitHub Stars
39
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail