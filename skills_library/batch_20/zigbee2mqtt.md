---
title: zigbee2mqtt
url: https://skills.sh/szkocot/skills/zigbee2mqtt
---

# zigbee2mqtt

skills/szkocot/skills/zigbee2mqtt
zigbee2mqtt
Installation
$ npx skills add https://github.com/szkocot/skills --skill zigbee2mqtt
SKILL.md
Zigbee2MQTT

Zigbee2MQTT bridges Zigbee devices to MQTT, enabling integration with Home Assistant, Node-RED, and custom applications without proprietary hubs.

Architecture Overview
Zigbee Devices → [Adapter] → zigbee-herdsman → zigbee-herdsman-converters → zigbee2mqtt → MQTT Broker → Home Assistant/Apps


Three-layer stack:

zigbee-herdsman: Hardware abstraction, Zigbee protocol handling
zigbee-herdsman-converters: Device definitions, cluster-to-MQTT mapping
zigbee2mqtt: Bridge application, state management, web UI
Configuration

Configuration lives in data/configuration.yaml. Key sections:

# MQTT connection
mqtt:
  server: mqtt://localhost:1883
  base_topic: zigbee2mqtt
  user: mqtt_user
  password: mqtt_pass

# Zigbee adapter
serial:
  port: /dev/ttyUSB0
  # adapter: zstack  # auto-detected usually

# Network settings
advanced:
  channel: 11  # 11-26, avoid WiFi overlap
  network_key: GENERATE  # auto-generates secure key
  pan_id: GENERATE

# Web UI
frontend:
  port: 8080

# Device tracking
availability: true


Per-device config in devices.yaml:

'0x00158d0001234567':
  friendly_name: living_room_sensor
  retain: true


Groups in groups.yaml:

'1':
  friendly_name: all_lights
  devices:
    - bulb_1
    - bulb_2

MQTT Topics
Device Communication
Topic	Direction	Purpose
zigbee2mqtt/{device}	Subscribe	Device state
zigbee2mqtt/{device}/set	Publish	Control device
zigbee2mqtt/{device}/get	Publish	Request state
zigbee2mqtt/{device}/availability	Subscribe	Online/offline

Control examples:

// Turn on light with brightness
{"state": "ON", "brightness": 200}

// Set color temperature
{"color_temp": 350}

// RGB color
{"color": {"r": 255, "g": 100, "b": 50}}

Bridge Management
Topic	Purpose
zigbee2mqtt/bridge/state	Bridge online status
zigbee2mqtt/bridge/info	Version, coordinator info
zigbee2mqtt/bridge/devices	All paired devices
zigbee2mqtt/bridge/event	Join/leave events

Request/response pattern:

Publish to:   zigbee2mqtt/bridge/request/{command}
Subscribe to: zigbee2mqtt/bridge/response/{command}


Common commands:

permit_join - Enable pairing: {"value": true, "time": 120}
remove - Remove device: {"id": "0x00158d..."}
rename - Rename device: {"from": "old", "to": "new"}
restart - Restart bridge
Adding Device Support
Quick: External Converter

For testing without modifying source, create data/external_converters/my_device.js:

const {deviceEndpoints, onOff} = require('zigbee-herdsman-converters/lib/modernExtend');

const definition = {
    zigbeeModel: ['TS0001'],
    model: 'TS0001',
    vendor: 'TuYa',
    description: 'Smart switch',
    extend: [onOff()],
};

module.exports = definition;


Enable in configuration.yaml:

external_converters:
  - my_device.js

Full: Contribute to zigbee-herdsman-converters
Identify device - Pair and check logs for zigbeeModel, clusters
Find vendor file - src/devices/<vendor>.ts
Add definition:
{
    zigbeeModel: ['lumi.sensor_motion.aq2'],
    model: 'RTCGQ11LM',
    vendor: 'Aqara',
    description: 'Motion sensor',
    fromZigbee: [fz.occupancy, fz.battery, fz.illuminance],
    toZigbee: [],
    exposes: [e.occupancy(), e.battery(), e.illuminance()],
}


Key components:

fromZigbee: Converters for device → MQTT
toZigbee: Converters for MQTT → device
exposes: Capabilities exposed to Home Assistant
Modern Extend Pattern

Prefer extend for common device types:

{
    zigbeeModel: ['TRADFRI bulb E27 WS opal 980lm'],
    model: 'LED1545G12',
    vendor: 'IKEA',
    description: 'TRADFRI bulb E27 WS opal 980lm',
    extend: [light({colorTemp: {range: [250, 454]}})],
}

Debugging
Enable Debug Logging
advanced:
  log_level: debug
  log_namespaced_levels:
    z2m:mqtt: warning  # Reduce MQTT noise
    zh:zstack: debug   # Adapter-level debug


Log namespaces:

z2m:* - zigbee2mqtt core
zh:* - zigbee-herdsman (protocol)
zhc:* - zigbee-herdsman-converters
Common Issues

Device won't pair:

Verify permit_join enabled
Check adapter connection: ls -la /dev/ttyUSB*
Use USB extension cable (reduces interference)
Try different channel (avoid 11 if using 2.4GHz WiFi)

Device offline:

Check availability config
Verify device battery / power
Look for last_seen timestamp
Check for Zigbee mesh issues (weak routing)

Adapter disconnects:

dmesg | grep -i usb  # Check kernel logs
journalctl -u zigbee2mqtt -f  # Service logs

Development Setup
git clone https://github.com/Koenkk/zigbee2mqtt
cd zigbee2mqtt
pnpm install --frozen-lockfile
pnpm run build  # Compile TypeScript

# Run
node index.js


Code structure:

lib/ - TypeScript source (main application)
lib/extension/ - Extension system (OTA, groups, etc.)
lib/mqtt/ - MQTT handling
data/ - Configuration, database

Testing:

pnpm test
pnpm run lint

OTA Updates

Enable firmware updates:

ota:
  update_check_interval: 1440  # minutes
  disable_automatic_update_check: false


Check/trigger via MQTT:

zigbee2mqtt/bridge/request/device/ota_update/check
{"id": "device_name"}

Home Assistant Integration

Automatic discovery via MQTT. Ensure:

homeassistant: true


Devices appear automatically. Override discovery:

'0x00158d0001234567':
  friendly_name: motion_sensor
  homeassistant:
    occupancy:
      device_class: motion
      name: "Living Room Motion"

Reference
Configuration options - Complete settings reference
MQTT API - Full topic and payload documentation
Converter patterns - Device definition examples
Weekly Installs
21
Repository
szkocot/skills
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass