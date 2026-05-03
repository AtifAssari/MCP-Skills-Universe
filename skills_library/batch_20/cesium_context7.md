---
title: cesium-context7
url: https://skills.sh/cesiumgs/cesium-ai-integrations/cesium-context7
---

# cesium-context7

skills/cesiumgs/cesium-ai-integrations/cesium-context7
cesium-context7
Installation
$ npx skills add https://github.com/cesiumgs/cesium-ai-integrations --skill cesium-context7
SKILL.md
Context7 for Cesium Development

This skill provides access to up-to-date Cesium documentation for CesiumJS, Unreal Engine integration, and Unity integration.

When working with Cesium-related code, use Context7 MCP Server tools to fetch current documentation before providing answers or generating code.

Available Tools
1. resolve-library-id

Search for libraries and retrieve their Context7 library IDs.

⚠️ Only use this tool when it's unclear which library to use. For Cesium projects, use the Known Library IDs listed below.

Parameters:

libraryName (string, required): Name of the library to search
query (string, optional): Additional search context

Example use case: Find the correct library ID for an unfamiliar library or when the library ID is unknown.

2. query-docs

Retrieve documentation for a specific library and query.

Parameters:

libraryId (string, required): Context7 library ID
query (string, required): Documentation query or topic
version (string, optional): Specific library version

Example use case: Get documentation for Cesium Viewer initialization using library /cesiumgs/cesium.

Known Library IDs
CesiumJS API Documentation

For class constructors, methods, and properties (e.g., Viewer, Entity, Cartesian3, Camera methods, Scene properties):

Library ID: /cesiumgs/cesium
Cesium for Unreal Engine

For Unreal Engine integration (e.g., ACesium3DTileset, ACesiumGeoreference, Blueprint integration):

Library ID: /cesiumgs/cesium-unreal
Cesium for Unity

For Unity integration (e.g., Cesium3DTileset component, CesiumCameraController, C# scripting):

Library ID: /cesiumgs/cesium-unity
3D Tiles Specification

For tile formats and schema details (e.g., tileset JSON structure, refinement strategies, metadata schemas):

Library ID: /websites/ogc_cs_22-025r4
Usage Guidelines
Use the Known Library IDs listed above for Cesium-related queries
When a question requires information from multiple sources (e.g., CesiumJS API + 3D Tiles spec, or Unreal integration + CesiumJS concepts), make separate query-docs calls with different library IDs to gather comprehensive documentation
Use resolve-library-id when the library is unknown, not listed in Known Library IDs, or when it's unclear which library best fits the question
Use query-docs to fetch documentation before generating code to ensure accuracy
Specify the version parameter when working with a specific version
Provide clear, specific queries to get the most relevant documentation
Avoid hallucinations by using current, version-specific documentation
Weekly Installs
72
Repository
cesiumgs/cesium…grations
GitHub Stars
63
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn