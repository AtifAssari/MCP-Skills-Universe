---
rating: ⭐⭐
title: api catalog
url: https://skills.sh/tonylofgren/aurora-smart-home/api-catalog
---

# api catalog

skills/tonylofgren/aurora-smart-home/API Catalog
API Catalog
Installation
$ npx skills add https://github.com/tonylofgren/aurora-smart-home --skill 'API Catalog'
SKILL.md
API Catalog for Home Assistant

Reference skill for connecting external APIs and services to Home Assistant.

Overview

This skill covers authentication patterns and working code examples for connecting popular APIs to Home Assistant via three methods:

Node-RED - HTTP request node flows (fastest to get running)
HA YAML - rest sensor and rest_command (good for simple polling)
Custom integration - Full HACS-publishable Python component (use ha-integration skill)
The Iron Law
CREDENTIALS IN SECRETS - NEVER HARDCODED IN FLOWS OR YAML


API keys belong in Node-RED credentials, ESPHome secrets.yaml, or HA secrets.yaml. Never paste real tokens into chat, flows that get exported, or YAML committed to git.

How to Use This Skill
User mentions an API or service by name
Read the relevant reference file for auth setup and endpoints
Generate working code for the user's chosen method (Node-RED / YAML / integration)
Include credential setup instructions
Reference Files
Category	File	APIs Covered
Energy & electricity	references/energy-apis.md	Tibber, Nordpool, Energi Data Service
Weather	references/weather-apis.md	SMHI, OpenWeatherMap, yr.no, Tomorrow.io
Transport	references/transport-apis.md	SL, Trafikverket, Resrobot, Entur (NO)
Smart home clouds	references/smarthome-apis.md	Shelly Cloud, Tuya IoT, Philips Hue, IKEA Dirigera
Global / other	references/global-apis.md	OpenAI, Spotify, Google Calendar, Telegram, GitHub
Authentication Patterns at a Glance
Pattern	How it works	Examples
API key in header	Authorization: Bearer {key} or X-API-Key: {key}	Tibber, OpenAI
API key in URL	?appid={key} appended to URL	OpenWeatherMap
OAuth2	Get access token first, refresh periodically	Spotify, Google
Local token	One-time press-button auth on device	Philips Hue
No auth	Public API, no credentials needed	SMHI, yr.no, Nordpool
Basic auth	Username + password Base64-encoded	Some local devices
Output Methods

For each API, generate code for the method the user needs:

Node-RED: http request node + function node to parse + api-call-service to push to HA HA YAML: rest sensor platform or rest_command under configuration.yaml Full integration: Use ha-integration skill with the polling-integration template

Common Patterns
Node-RED: API key in header
{
  "type": "http request",
  "method": "GET",
  "url": "https://api.example.com/data",
  "headers": {"Authorization": "Bearer {{env.API_KEY}}"},
  "ret": "obj"
}

Node-RED: GraphQL (Tibber-style)
{
  "type": "http request",
  "method": "POST",
  "url": "https://api.tibber.com/v1-beta/gql",
  "headers": {
    "Authorization": "Bearer {{env.TIBBER_TOKEN}}",
    "Content-Type": "application/json"
  },
  "payload": "{\"query\": \"{ viewer { homes { currentSubscription { priceInfo { current { total } } } } } }\"}",
  "ret": "obj"
}

HA YAML: REST sensor
rest:
  - scan_interval: 300
    resource: https://api.example.com/current
    headers:
      Authorization: !secret example_api_key
    sensor:
      - name: "Example Value"
        value_template: "{{ value_json.data.value }}"
        unit_of_measurement: "°C"

Pre-Output Checklist
 Credentials use !secret (YAML), Node-RED credentials, or env vars - never hardcoded
 Rate limits respected (include scan_interval or flow timer accordingly)
 Error handling included (Node-RED catch node or YAML timeout)
 For OAuth2: refresh token flow explained
 Attribution: which API endpoint, what data it returns
Integration

Pairs with:

node-red skill - for flow JSON implementation
ha-yaml skill - for YAML sensor and automation using the fetched data
ha-integration skill - for building a full HACS-publishable Python integration
Weekly Installs
–
Repository
tonylofgren/aur…art-home
GitHub Stars
37
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn