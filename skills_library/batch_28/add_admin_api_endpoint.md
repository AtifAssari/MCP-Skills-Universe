---
title: add admin api endpoint
url: https://skills.sh/tryghost/ghost/add-admin-api-endpoint
---

# add admin api endpoint

skills/tryghost/ghost/Add Admin API Endpoint
Add Admin API Endpoint
Installation
$ npx skills add https://github.com/tryghost/ghost --skill 'Add Admin API Endpoint'
SKILL.md
Create Admin API Endpoint
Instructions
If creating an endpoint for an entirely new resource, create a new endpoint file in ghost/core/core/server/api/endpoints/. Otherwise, locate the existing endpoint file in the same directory.
The endpoint file should create a controller object using the JSDoc type from (@tryghost/api-framework).Controller, including at minimum a docName and a single endpoint definition, i.e. browse.
Add routes for each endpoint to ghost/core/core/server/web/api/endpoints/admin/routes.js.
Add basic e2e-api tests for the endpoint in ghost/core/test/e2e-api/admin to ensure the new endpoints function as expected.
Run the tests and iterate until they pass: cd ghost/core && yarn test:single test/e2e-api/admin/{test-file-name}.
Reference

For a detailed reference on Ghost's API framework and how to create API controllers, see reference.md.

Weekly Installs
–
Repository
tryghost/ghost
GitHub Stars
52.7K
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass