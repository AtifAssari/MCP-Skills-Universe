---
rating: ⭐⭐⭐
title: kotlin-mcp-server-generator
url: https://skills.sh/github/awesome-copilot/kotlin-mcp-server-generator
---

# kotlin-mcp-server-generator

skills/github/awesome-copilot/kotlin-mcp-server-generator
kotlin-mcp-server-generator
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill kotlin-mcp-server-generator
Summary

Generate production-ready Kotlin MCP server projects with Gradle, official SDK, and typed tools.

Scaffolds complete project structure with build.gradle.kts, package layout, and MCP server configuration using io.modelcontextprotocol:kotlin-sdk
Includes 2–3 sample tools with JSON schema definitions, typed inputs/outputs, and error handling patterns
Provides coroutine-based server setup with stdio transport, environment variable configuration, and kotlin-logging integration
Includes test templates using kotlinx-coroutines-test and README with build, run, and development instructions
SKILL.md
Kotlin MCP Server Project Generator

Generate a complete, production-ready Model Context Protocol (MCP) server project in Kotlin.

Project Requirements

You will create a Kotlin MCP server with:

Project Structure: Gradle-based Kotlin project layout
Dependencies: Official MCP SDK, Ktor, and kotlinx libraries
Server Setup: Configured MCP server with transports
Tools: At least 2-3 useful tools with typed inputs/outputs
Error Handling: Proper exception handling and validation
Documentation: README with setup and usage instructions
Testing: Basic test structure with coroutines
Template Structure
myserver/
├── build.gradle.kts
├── settings.gradle.kts
├── gradle.properties
├── src/
│   ├── main/
│   │   └── kotlin/
│   │       └── com/example/myserver/
│   │           ├── Main.kt
│   │           ├── Server.kt
│   │           ├── config/
│   │           │   └── Config.kt
│   │           └── tools/
│   │               ├── Tool1.kt
│   │               └── Tool2.kt
│   └── test/
│       └── kotlin/
│           └── com/example/myserver/
│               └── ServerTest.kt
└── README.md

build.gradle.kts Template
plugins {
    kotlin("jvm") version "2.1.0"
    kotlin("plugin.serialization") version "2.1.0"
    application
}

group = "com.example"
version = "1.0.0"

repositories {
    mavenCentral()
}

dependencies {
    implementation("io.modelcontextprotocol:kotlin-sdk:0.7.2")
    
    // Ktor for transports
    implementation("io.ktor:ktor-server-netty:3.0.0")
    implementation("io.ktor:ktor-client-cio:3.0.0")
    
    // Serialization
    implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.7.3")
    
    // Coroutines
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.9.0")
    
    // Logging
    implementation("io.github.oshai:kotlin-logging-jvm:7.0.0")
    implementation("ch.qos.logback:logback-classic:1.5.12")
    
    // Testing
    testImplementation(kotlin("test"))
    testImplementation("org.jetbrains.kotlinx:kotlinx-coroutines-test:1.9.0")
}

application {
    mainClass.set("com.example.myserver.MainKt")
}

tasks.test {
    useJUnitPlatform()
}

kotlin {
    jvmToolchain(17)
}

settings.gradle.kts Template
rootProject.name = "{{PROJECT_NAME}}"

Main.kt Template
package com.example.myserver

import io.modelcontextprotocol.kotlin.sdk.server.StdioServerTransport
import kotlinx.coroutines.runBlocking
import io.github.oshai.kotlinlogging.KotlinLogging

private val logger = KotlinLogging.logger {}

fun main() = runBlocking {
    logger.info { "Starting MCP server..." }
    
    val config = loadConfig()
    val server = createServer(config)
    
    // Use stdio transport
    val transport = StdioServerTransport()
    
    logger.info { "Server '${config.name}' v${config.version} ready" }
    server.connect(transport)
}

Server.kt Template
package com.example.myserver

import io.modelcontextprotocol.kotlin.sdk.server.Server
import io.modelcontextprotocol.kotlin.sdk.server.ServerOptions
import io.modelcontextprotocol.kotlin.sdk.Implementation
import io.modelcontextprotocol.kotlin.sdk.ServerCapabilities
import com.example.myserver.tools.registerTools

fun createServer(config: Config): Server {
    val server = Server(
        serverInfo = Implementation(
            name = config.name,
            version = config.version
        ),
        options = ServerOptions(
            capabilities = ServerCapabilities(
                tools = ServerCapabilities.Tools(),
                resources = ServerCapabilities.Resources(
                    subscribe = true,
                    listChanged = true
                ),
                prompts = ServerCapabilities.Prompts(listChanged = true)
            )
        )
    ) {
        config.description
    }
    
    // Register all tools
    server.registerTools()
    
    return server
}

Config.kt Template
package com.example.myserver.config

import kotlinx.serialization.Serializable

@Serializable
data class Config(
    val name: String = "{{PROJECT_NAME}}",
    val version: String = "1.0.0",
    val description: String = "{{PROJECT_DESCRIPTION}}"
)

fun loadConfig(): Config {
    return Config(
        name = System.getenv("SERVER_NAME") ?: "{{PROJECT_NAME}}",
        version = System.getenv("VERSION") ?: "1.0.0",
        description = System.getenv("DESCRIPTION") ?: "{{PROJECT_DESCRIPTION}}"
    )
}

Tool1.kt Template
package com.example.myserver.tools

import io.modelcontextprotocol.kotlin.sdk.server.Server
import io.modelcontextprotocol.kotlin.sdk.CallToolRequest
import io.modelcontextprotocol.kotlin.sdk.CallToolResult
import io.modelcontextprotocol.kotlin.sdk.TextContent
import kotlinx.serialization.json.buildJsonObject
import kotlinx.serialization.json.put
import kotlinx.serialization.json.putJsonObject
import kotlinx.serialization.json.putJsonArray

fun Server.registerTool1() {
    addTool(
        name = "tool1",
        description = "Description of what tool1 does",
        inputSchema = buildJsonObject {
            put("type", "object")
            putJsonObject("properties") {
                putJsonObject("param1") {
                    put("type", "string")
                    put("description", "First parameter")
                }
                putJsonObject("param2") {
                    put("type", "integer")
                    put("description", "Optional second parameter")
                }
            }
            putJsonArray("required") {
                add("param1")
            }
        }
    ) { request: CallToolRequest ->
        // Extract and validate parameters
        val param1 = request.params.arguments["param1"] as? String
            ?: throw IllegalArgumentException("param1 is required")
        val param2 = (request.params.arguments["param2"] as? Number)?.toInt() ?: 0
        
        // Perform tool logic
        val result = performTool1Logic(param1, param2)
        
        CallToolResult(
            content = listOf(
                TextContent(text = result)
            )
        )
    }
}

private fun performTool1Logic(param1: String, param2: Int): String {
    // Implement tool logic here
    return "Processed: $param1 with value $param2"
}

tools/ToolRegistry.kt Template
package com.example.myserver.tools

import io.modelcontextprotocol.kotlin.sdk.server.Server

fun Server.registerTools() {
    registerTool1()
    registerTool2()
    // Register additional tools here
}

ServerTest.kt Template
package com.example.myserver

import kotlinx.coroutines.test.runTest
import kotlin.test.Test
import kotlin.test.assertEquals
import kotlin.test.assertFalse

class ServerTest {
    
    @Test
    fun `test server creation`() = runTest {
        val config = Config(
            name = "test-server",
            version = "1.0.0",
            description = "Test server"
        )
        
        val server = createServer(config)
        
        assertEquals("test-server", server.serverInfo.name)
        assertEquals("1.0.0", server.serverInfo.version)
    }
    
    @Test
    fun `test tool1 execution`() = runTest {
        val config = Config()
        val server = createServer(config)
        
        // Test tool execution
        // Note: You'll need to implement proper testing utilities
        // for calling tools in the server
    }
}

README.md Template
# {{PROJECT_NAME}}

A Model Context Protocol (MCP) server built with Kotlin.

## Description

{{PROJECT_DESCRIPTION}}

## Requirements

- Java 17 or higher
- Kotlin 2.1.0

## Installation

Build the project:

\`\`\`bash
./gradlew build
\`\`\`

## Usage

Run the server with stdio transport:

\`\`\`bash
./gradlew run
\`\`\`

Or build and run the jar:

\`\`\`bash
./gradlew installDist
./build/install/{{PROJECT_NAME}}/bin/{{PROJECT_NAME}}
\`\`\`

## Configuration

Configure via environment variables:

- `SERVER_NAME`: Server name (default: "{{PROJECT_NAME}}")
- `VERSION`: Server version (default: "1.0.0")
- `DESCRIPTION`: Server description

## Available Tools

### tool1
{{TOOL1_DESCRIPTION}}

**Input:**
- `param1` (string, required): First parameter
- `param2` (integer, optional): Second parameter

**Output:**
- Text result of the operation

## Development

Run tests:

\`\`\`bash
./gradlew test
\`\`\`

Build:

\`\`\`bash
./gradlew build
\`\`\`

Run with auto-reload (development):

\`\`\`bash
./gradlew run --continuous
\`\`\`

## Multiplatform

This project uses Kotlin Multiplatform and can target JVM, Wasm, and iOS.
See `build.gradle.kts` for platform configuration.

## License

MIT

Generation Instructions

When generating a Kotlin MCP server:

Gradle Setup: Create proper build.gradle.kts with all dependencies
Package Structure: Follow Kotlin package conventions
Type Safety: Use data classes and kotlinx.serialization
Coroutines: All operations should be suspending functions
Error Handling: Use Kotlin exceptions and validation
JSON Schemas: Use buildJsonObject for tool schemas
Testing: Include coroutine test utilities
Logging: Use kotlin-logging for structured logging
Configuration: Use data classes and environment variables
Documentation: KDoc comments for public APIs
Best Practices
Use suspending functions for all async operations
Leverage Kotlin's null safety and type system
Use data classes for structured data
Apply kotlinx.serialization for JSON handling
Use sealed classes for result types
Implement proper error handling with Result/Either patterns
Write tests using kotlinx-coroutines-test
Use dependency injection for testability
Follow Kotlin coding conventions
Use meaningful names and KDoc comments
Transport Options
Stdio Transport
val transport = StdioServerTransport()
server.connect(transport)

SSE Transport (Ktor)
embeddedServer(Netty, port = 8080) {
    mcp {
        Server(/*...*/) { "Description" }
    }
}.start(wait = true)

Multiplatform Configuration

For multiplatform projects, add to build.gradle.kts:

kotlin {
    jvm()
    js(IR) { nodejs() }
    wasmJs()
    
    sourceSets {
        commonMain.dependencies {
            implementation("io.modelcontextprotocol:kotlin-sdk:0.7.2")
        }
    }
}

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
SnykPass