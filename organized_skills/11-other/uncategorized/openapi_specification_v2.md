---
rating: ⭐⭐
title: openapi-specification-v2
url: https://skills.sh/hairyf/skills/openapi-specification-v2
---

# openapi-specification-v2

skills/hairyf/skills/openapi-specification-v2
openapi-specification-v2
Installation
$ npx skills add https://github.com/hairyf/skills --skill openapi-specification-v2
Summary

Complete reference for writing, validating, and interpreting OpenAPI Specification 2.0 (Swagger) documents.

Covers all core schema elements: Swagger Object root, Info/Contact/License metadata, Paths, Operations, Parameters (path, query, header, body, formData), Responses, and Schemas with composition and polymorphism support
Includes security definitions for Basic auth, API Key, and OAuth2 flows (implicit, password, application, accessCode) with scope and requirement objects
Provides reference guidance for $ref usage, JSON Pointers, external file references, and root-level parameter/response/schema reuse
Addresses data types, formats, MIME types, HTTP status codes, path templating, headers, and vendor extensions (x- prefix)
Includes best practices for operationId, tags, responses, and spec authoring patterns
SKILL.md

OpenAPI Specification 2.0 (formerly Swagger 2.0) defines a JSON/YAML format for describing RESTful APIs: paths, operations, parameters, responses, schemas, and security. Use this skill when creating or editing Swagger 2.0 specs, validating structure, or generating code/documentation from them.

The skill is based on OpenAPI Specification 2.0, generated at 2026-01-30.

Core References
Topic	Description	Reference
Format and Structure	Document format, file structure, data types	core-format-and-structure
Fixed and Patterned Fields	Fixed vs patterned field names in the schema	core-fixed-patterned-fields
Swagger Object	Root document, required/optional fields, extensions	core-swagger-object
Info and Metadata	Info, Contact, License objects	core-info-metadata
Tags and External Docs	Tag Object, External Documentation Object	core-tags-and-external-docs
Reference Object	$ref, JSON Pointer, same-document and external file references	core-reference-object
Data Types and Formats	Primitives, format table, validation, file type	core-data-types-and-formats
MIME Types	consumes/produces, RFC 6838, examples	core-mime-types
HTTP Status Codes	Response keys, default response, IANA/RFC 7231	core-http-status-codes
Path Templating	Curly braces, path parameters, name matching	core-path-templating
Header Object	Response header definition (type, format, items, validation)	core-header-object
Headers Object	Container for response headers (name → Header Object)	core-headers-object
Items Object	Non-body array items (parameters, headers)	core-items-object
Example Object	Response examples by MIME type	core-example-object
Paths and Operations
Topic	Description	Reference
Paths and Operations	Paths Object, Path Item, Operation Object	paths-and-operations
Path Item $ref	External path definition, conflict behavior	path-item-ref
Parameters and Responses
Topic	Description	Reference
Parameters	Parameter locations (path, query, header, body, formData)	parameters
collectionFormat	csv, ssv, tsv, pipes, multi and where they apply	parameters-collection-format
Parameters Definitions (Reuse)	Root-level parameters, reuse via $ref	parameters-definitions-reuse
Responses	Responses Object, Response Object	responses
Responses Definitions (Reuse)	Root-level responses, reuse via $ref	responses-definitions-reuse
Schemas and Definitions
Topic	Description	Reference
Schema and Definitions	Schema Object, Definitions, composition, polymorphism	schema-and-definitions
Schema JSON Schema Keywords	JSON Schema Draft 4 subset and Swagger-specific fields	schema-json-schema-keywords
Security
Topic	Description	Reference
Security	Security Definitions, Security Scheme	security
Security Requirement Object	Applying security at root/operation, OR/AND logic	security-requirement-object
Scopes Object	OAuth2 scope name → description	security-scopes-object
Basic and API Key	basic and apiKey Security Scheme	security-basic-apikey
OAuth2 Flows	implicit, password, application, accessCode and required URLs	security-oauth2-flows
Best Practices
Topic	Description	Reference
Spec Authoring	operationId, tags, responses, parameters, definitions, security	best-practices-spec-authoring
Advanced
Topic	Description	Reference
Vendor Extensions	x- prefix, value types, where allowed	advanced-vendor-extensions
Security Filtering	Empty Paths, empty Path Item for access control	advanced-security-filtering
Extensions and XML	XML Object for schema properties	advanced-extensions-and-xml
Weekly Installs
433
Repository
hairyf/skills
GitHub Stars
15
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass