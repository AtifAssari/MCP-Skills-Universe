---
rating: ⭐⭐⭐
title: esp32-serial-commands
url: https://skills.sh/h1d/agent-skills-esp32/esp32-serial-commands
---

# esp32-serial-commands

skills/h1d/agent-skills-esp32/esp32-serial-commands
esp32-serial-commands
Installation
$ npx skills add https://github.com/h1d/agent-skills-esp32 --skill esp32-serial-commands
SKILL.md
ESP32 Serial Command Emulation
Overview

Send commands directly to the serial port to emulate button presses and user actions. Works over USB serial.

ESP32 Setup (Device Side)
ESP-IDF Framework
#include "esp_log.h"
#include <string.h>

static const char* TAG = "SerialCmd";

void serial_command_task(void* arg) {
    char buf[64];
    int idx = 0;

    while (1) {
        int c = getchar();
        if (c == EOF) {
            vTaskDelay(pdMS_TO_TICKS(10));
            continue;
        }

        if (c == '\n' || c == '\r') {
            buf[idx] = '\0';
            if (idx > 0) {
                ESP_LOGI(TAG, "Command: %s", buf);

                if (strcmp(buf, "PRESS") == 0) {
                    button_callback();
                } else if (strncmp(buf, "SCREEN:", 7) == 0) {
                    int screen = atoi(buf + 7);
                    go_to_screen(screen);
                }
            }
            idx = 0;
        } else if (idx < sizeof(buf) - 1) {
            buf[idx++] = c;
        }
    }
}

// In app_main():
// xTaskCreate(serial_command_task, "serial_cmd", 2048, NULL, 5, NULL);

Arduino Framework
void setup() {
    Serial.begin(115200);
}

void loop() {
    if (Serial.available()) {
        String cmd = Serial.readStringUntil('\n');
        cmd.trim();

        Serial.printf("Command: %s\n", cmd.c_str());

        if (cmd == "PRESS") {
            button_callback();
        } else if (cmd.startsWith("SCREEN:")) {
            int screen = cmd.substring(7).toInt();
            go_to_screen(screen);
        } else if (cmd == "STATUS") {
            Serial.println("OK");
        }
    }
}

Host Side - Send Commands
# Find serial port
PORT=$(ls /dev/cu.usbmodem* /dev/ttyUSB* /dev/ttyACM* 2>/dev/null | head -1)

# Send a command
echo "PRESS" > "$PORT"

Common Command Patterns
# Simple command
echo "PRESS" > "$PORT"

# Command with parameter
echo "PRESS:3" > "$PORT"      # Press 3 times
echo "SCREEN:2" > "$PORT"     # Go to screen 2
echo "MODE:debug" > "$PORT"   # Set debug mode

Automated Testing
Stress Test
PORT=$(ls /dev/cu.usbmodem* /dev/ttyUSB* 2>/dev/null | head -1)
for i in {1..100}; do
  echo "PRESS" > "$PORT"
  echo "Sent press $i"
  sleep 2
done

Long-Duration Stability Test
PORT=$(ls /dev/cu.usbmodem* /dev/ttyUSB* 2>/dev/null | head -1)
END=$(($(date +%s) + 3600))  # 1 hour
count=0

while [ $(date +%s) -lt $END ]; do
  count=$((count + 1))
  echo "PRESS" > "$PORT"
  echo "[$(date +%H:%M:%S)] Press $count"
  sleep 30
done

echo "Total: $count presses"

Test with Log Monitoring

Terminal 1 - Monitor logs:

tail -f /tmp/device.log


Terminal 2 - Send commands:

PORT=$(ls /dev/cu.usbmodem* /dev/ttyUSB* 2>/dev/null | head -1)
echo "PRESS" > "$PORT"

Tips
Timing: Add delays between commands to let device process
Feedback: Check serial logs to confirm command was received
Error handling: Device should echo back status (OK/ERROR)
Combine with logging: Always monitor logs while testing
Weekly Installs
104
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