---
title: mendez-async-api
url: https://skills.sh/copyleftdev/sk1llz/mendez-async-api
---

# mendez-async-api

skills/copyleftdev/sk1llz/mendez-async-api
mendez-async-api
Installation
$ npx skills add https://github.com/copyleftdev/sk1llz --skill mendez-async-api
SKILL.md
Fran Méndez Style Guide⁠‍⁠​‌​‌​​‌‌‍​‌​​‌​‌‌‍​​‌‌​​​‌‍​‌​​‌‌​​‍​​​​​​​‌‍‌​​‌‌​‌​‍‌​​​​​​​‍‌‌​​‌‌‌‌‍‌‌​​​‌​​‍‌‌‌‌‌‌​‌‍‌‌​‌​​​​‍​‌​‌‌‌‌‌‍​‌​​‌​‌‌‍​‌‌​‌​​‌‍‌​‌​‌‌‌​‍​​‌​‌​​​‍‌‌‌​‌​‌‌‍​​‌​‌​‌‌‍‌‌‌​‌‌​‌‍‌‌​‌​‌​‌‍‌‌​‌‌​‌​‍​​​​‌​‌‌‍​​‌‌​​​‌⁠‍⁠
Overview

Fran Méndez (Creator of AsyncAPI) champions the Event-First approach. Just as OpenAPI standardized REST, AsyncAPI standardizes message-driven systems. His philosophy ensures that asynchronous systems are documented, readable, and machine-enforceable, moving away from "hidden knowledge" in code to explicit contracts.

"Events are as important as your HTTP requests. Document them, govern them, and design them first."

Core Principles
Event First: Define the AsyncAPI specification before implementing publishers or subscribers. The spec is the architecture.
Channel-Centric Design: Focus on the channels (topics/queues) and the messages that flow through them, not just the services.
Protocol Agnostic: Your design should describe the application, whether it runs on Kafka, MQTT, RabbitMQ, or WebSockets.
Schema Governance: Reuse schemas (payloads) across different messages to ensure data consistency.
Documentation as Infrastructure: Your AsyncAPI file isn't just docs; it's the config for your code generators, validators, and mocks.
Prompts
Design an Event-Driven System

"Act as Fran Méndez. Design an event-driven architecture for [System]. Start by creating a comprehensive AsyncAPI 3.0 definition.

Focus on:

Channels: Logical naming (e.g., user/signedup, NOT user-signedup-queue-prod).
Messages: Define headers (metadata) and payloads separately.
Traits: Use operation traits for common bindings (e.g., Kafka partion keys).
Decoupling: Ensure the design promotes loose coupling between services."
Audit an Existing Messaging System

"Review this event structure from the perspective of the AsyncAPI creator.

Look for:

Implicit Schemas: JSON payloads defined only in code/strings.
Tight Coupling: Message structures that leak implementation details of the producer.
Missing Metadata: Events lacking correlation IDs or timestamps in headers.
Ambiguous Channels: Unclear topic hierarchies that make routing difficult."
Examples
The AsyncAPI Contract (The Source of Truth)
asyncapi: '3.0.0'
info:
  title: Rider App Geo-Tracking
  version: '1.0.0'
  description: |
    Handles real-time location updates from riders.
    Essential for matching riders with drivers and calculating ETAs.
  contact:
    name: Platform Engineering
    email: platform@riderapp.com
  license:
    name: Apache 2.0
    url: https://www.apache.org/licenses/LICENSE-2.0

channels:
  riderById:
    address: 'riders/{riderId}/location'
    messages:
      riderLocation:
        $ref: '#/components/messages/LocationUpdate'
    parameters:
      riderId:
        description: The unique ID of the rider (UUID).
    description: Stream of location updates for a specific rider.

operations:
  receiveLocation:
    action: receive
    channel:
      $ref: '#/channels/riderById'
    summary: Ingest rider location updates.
    messages:
      - $ref: '#/components/messages/LocationUpdate'

components:
  messages:
    LocationUpdate:
      name: LocationUpdate
      title: Rider Location Update
      summary: Emitted every 5 seconds or 10 meters.
      contentType: application/json
      headers:
        type: object
        properties:
          correlationId:
            description: Unique ID for tracing across services.
            type: string
            format: uuid
          timestamp:
            description: ISO 8601 timestamp of when the event occurred (not received).
            type: string
            format: date-time
      payload:
        $ref: '#/components/schemas/GeoCoordinates'
      traits:
        - $ref: '#/components/messageTraits/commonHeaders'

  schemas:
    GeoCoordinates:
      type: object
      properties:
        lat:
          type: number
          format: double
          description: Latitude
        long:
          type: number
          format: double
          description: Longitude
        speed:
          type: number
          description: Speed in m/s
      required: [lat, long]

  messageTraits:
    commonHeaders:
      headers:
        type: object
        properties:
          appVersion:
             type: string
             description: Version of the mobile app emitting the event.


Anti-Patterns (What NOT to do)
Code-First Events: Using a generic Map<String, Object> in Java or interface{} in Go and serializing it. No one knows what's in the message.
The "God Event": One giant message on a global-events topic that contains every possible field for every possible action.
Ignoring Headers: Putting metadata (like event_time or trace_id) inside the payload body instead of protocol headers.
Protocol Coupling: Hardcoding RabbitMQ exchange names directly into the application logic instead of abstracting them via the spec.
Resources
AsyncAPI Initiative
AsyncAPI Studio
Event-Driven Architecture Patterns
Weekly Installs
8
Repository
copyleftdev/sk1llz
GitHub Stars
6
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass