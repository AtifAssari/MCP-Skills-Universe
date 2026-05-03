---
rating: ⭐⭐
title: openapi-specification-v3.2
url: https://skills.sh/hairyf/skills/openapi-specification-v3.2
---

# openapi-specification-v3.2

skills/hairyf/skills/openapi-specification-v3.2
openapi-specification-v3.2
Installation
$ npx skills add https://github.com/hairyf/skills --skill openapi-specification-v3.2
SKILL.md
OpenAPI Specification 3.2

Agent-oriented reference for the OpenAPI Specification 3.2.0. Use when editing, generating, or validating OpenAPI descriptions (OAD).

When to Use
Authoring or updating OpenAPI 3.2 YAML/JSON documents
Resolving $ref, $self, and relative URIs in multi-document OADs
Describing paths, operations, parameters (query/path/header/cookie/querystring), request body, and responses
Using Schema Objects (JSON Schema Draft 2020-12 dialect), components, and references
Configuring security schemes (apiKey, http, mutualTLS, oauth2, openIdConnect) and requirements
Working with media types, encoding (form, multipart), and examples (dataValue/serializedValue/externalValue)
Core References
Topic	Description	Reference
OpenAPI Object	Root object, openapi, $self, info, servers, paths, webhooks, components, security, tags	core-openapi-object
Format & Structure	JSON/YAML, case sensitivity, rich text, OAD structure, parsing, base URI	core-format-and-structure
Fixed & Patterned Fields	Fixed vs patterned fields, paths keys, components keys, extensions (x-)	core-fixed-patterned-fields
Info & Metadata	Info, Contact, License objects	core-info-metadata
Server	Server Object, Server Variable, URL templating	core-server
Paths & Operations	Paths Object, Path Item, Operation Object, additionalOperations, query	paths-and-operations
Path Templating	Path templating, path parameters, matching, ABNF	core-path-templating
Parameters	Parameter Object, in (path/query/header/cookie/querystring), style, schema vs content	parameters
Request Body & Media Type	Request Body, Media Type Object, sequential media types, itemSchema	request-body-and-media-type
Encoding Object	Encoding by name/position, contentType, style, explode, form, multipart	core-encoding-object
Media Types	Content keys, media type ranges, OpenAPI Media Type Registry	core-media-types
Responses	Responses Object, Response Object, headers, content, links	responses
HTTP Status Codes	Response keys, default, 1XX–5XX range with X	core-http-status-codes
Schema & Components	Schema Object (JSON Schema 2020-12), Components, $ref resolution	schema-and-components
Schema JSON Schema Keywords	JSON Schema 2020-12 keywords and OAS extensions in Schema	schema-json-schema-keywords
Schema Composition & Polymorphism	allOf, oneOf, anyOf, discriminator	schema-composition-polymorphism
Data Types & Formats	JSON Schema types, format keyword, OAS dialect	core-data-types-and-formats
Discriminator & XML	Discriminator Object, XML Object (nodeType, name, namespace)	core-discriminator-and-xml
Components Reuse	Reusing parameters, responses, schemas via $ref	components-reuse
Reference Object	$ref, summary/description override, resolution rules	core-reference-object
Header Object	Response/multipart headers, style simple, Set-Cookie, Link	core-header-object
Example Object	dataValue, serializedValue, value, externalValue, Working with Examples	core-example-object
Tag & External Docs	Tag Object, External Documentation Object, parent, kind	core-tags-and-external-docs
Link Object	operationRef, operationId, parameters, requestBody	core-link-object
Runtime Expressions	$request, $response, $url, $method, ABNF, Link/Callback usage	core-runtime-expressions
Security	Security Scheme, OAuth Flows, Security Requirement Object	security
Security Scheme Types	apiKey, http (basic/bearer), mutualTLS, oauth2, openIdConnect	security-scheme-types
Security Requirement Object	OR/AND semantics, {} optional, [] clear, scopes	security-requirement-object
OAuth2 Flows	OAuth Flows Object, OAuth Flow Object, authorizationCode, deviceAuthorization	security-oauth2-flows
Callbacks & Webhooks	Callback Object, webhooks	callbacks-and-webhooks
Extensions	Specification extensions (x-), extension registries	advanced-extensions
Best Practices
Topic	Description	Reference
Spec Authoring	operationId, tags, $self, components reuse, responses, security	best-practices-spec-authoring
Advanced
Topic	Description	Reference
Base URI & Resolution	$self, retrieval URI, reference resolution, parsing guidance	advanced-base-uri-and-resolution
Security Filtering	Empty Paths/Path Item, Security Considerations	advanced-security-filtering
Key Points
OAS 3.2 root uses openapi: 3.2.0; at least one of components, paths, or webhooks MUST be present.
$self provides the document's base URI for reference resolution; use it in multi-document OADs.
Schema Object is a superset of JSON Schema Draft 2020-12; empty schema = true, none = false.
Parameter: use either schema+style or content (one Media Type); in: "querystring" requires content.
Security at root is OR (one of the Security Requirement Objects); per-operation overrides; {} = optional.
Weekly Installs
504
Repository
hairyf/skills
GitHub Stars
15
First Seen
Jan 30, 2026