---
title: esp32-serial-logging
url: https://skills.sh/h1d/agent-skills-esp32/esp32-serial-logging
---

# esp32-serial-logging

skills/h1d/agent-skills-esp32/esp32-serial-logging
esp32-serial-logging
Installation
$ npx skills add https://github.com/h1d/agent-skills-esp32 --skill esp32-serial-logging
SKILL.md
ESP32 Serial Log Monitoring
Overview

Capture serial output from ESP32 (or any microcontroller) to a file for real-time monitoring and analysis.

ESP32 Setup (Device Side)
ESP-IDF Framework
#include "esp_log.h"

static const char* TAG = "MyComponent";

void my_function() {
    ESP_LOGI(TAG, "Info message");
    ESP_LOGW(TAG, "Warning: value=%d", some_value);
    ESP_LOGE(TAG, "Error occurred");
    ESP_LOGD(TAG, "Debug details");
}

Arduino Framework
void setup() {
    Serial.begin(115200);
}

void loop() {
    Serial.println("Status: running");
    Serial.printf("Sensor: %d\n", analogRead(A0));
    delay(1000);
}

Host Side - Capture Logs
# Find serial port
PORT=$(ls /dev/cu.usbmodem* /dev/ttyUSB* /dev/ttyACM* 2>/dev/null | head -1)
echo "Found port: $PORT"

# Configure and start capture
stty -f "$PORT" 115200 raw -echo 2>/dev/null || stty -F "$PORT" 115200 raw -echo
cat "$PORT" >> /tmp/device.log &
echo "Logging to /tmp/device.log (PID: $!)"

Monitor Logs
# Real-time monitoring
tail -f /tmp/device.log

# Filter specific patterns
tail -f /tmp/device.log | grep -E "ERROR|WiFi|Button"

Search for Errors
# Find crashes and errors
grep -E "ERROR|crash|overflow|panic|assert|Backtrace" /tmp/device.log

# Find reboots (look for boot messages or uptime resets)
grep -E "boot:|rst:|Uptime: [0-9] sec" /tmp/device.log

Debug Workflow

Clear log before reproducing issue:

> /tmp/device.log


Reproduce the issue

Analyze captured logs:

cat /tmp/device.log

Common Baud Rates
Device	Baud Rate
ESP32 (default)	115200
ESP32 (fast)	460800
Arduino	9600
STM32	115200
Stop Logging
pkill -f "cat /dev/cu.usbmodem"
pkill -f "cat /dev/ttyUSB"

Troubleshooting
Port not found: Check USB connection, try ls /dev/cu.* /dev/tty.*
Permission denied: Add user to dialout group (Linux)
Garbled output: Wrong baud rate
Weekly Installs
68
Repository
h1d/agent-skills-esp32
GitHub Stars
7
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass