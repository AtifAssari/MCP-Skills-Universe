---
rating: ⭐⭐⭐
title: arduino-code-generator
url: https://skills.sh/wedsamuel1230/arduino-skills/arduino-code-generator
---

# arduino-code-generator

skills/wedsamuel1230/arduino-skills/arduino-code-generator
arduino-code-generator
Installation
$ npx skills add https://github.com/wedsamuel1230/arduino-skills --skill arduino-code-generator
SKILL.md
Arduino Code Generator

Generate production-quality Arduino code snippets for sensors, actuators, communication, and embedded patterns.

Quick Start

Browse example sketches:

# See 9 production-ready examples in examples/ folder
ls examples/
# config-example.ino, filtering-example.ino, buttons-example.ino,
# i2c-example.ino, csv-example.ino, scheduler-example.ino,
# state-machine-example.ino, hardware-detection-example.ino,
# data-logging-example.ino


List available patterns:

uv run --no-project scripts/generate_snippet.py --list


Generate code for specific pattern and board:

uv run --no-project scripts/generate_snippet.py --pattern i2c --board esp32
uv run --no-project scripts/generate_snippet.py --pattern buttons --board uno --output button.ino


Interactive mode:

uv run --no-project scripts/generate_snippet.py --interactive

Resources
examples/ - 9 production-ready example sketches (one per pattern category)
examples/README.md - Detailed documentation for each example with wiring diagrams
scripts/generate_snippet.py - CLI tool for code generation with 9 pattern templates
scripts/verify_patterns.ps1 - Compile examples for UNO/ESP32/RP2040 (PowerShell)
scripts/verify_patterns.sh - Compile examples for UNO/ESP32/RP2040 (bash)
assets/workflow.mmd - Mermaid diagram of code generation workflow
Supported Patterns
Hardware Abstraction
Multi-board config.h with conditional compilation
Pin definitions for UNO/ESP32/RP2040
Memory budget tracking

See patterns-config.md | Example: config-example.ino

Sensor Reading & Filtering
ADC noise reduction (moving average, median, Kalman)
DHT22, BME280, analog sensors
Data validation and calibration

See patterns-filtering.md | Example: filtering-example.ino

Input Handling
Software button debouncing
Edge detection (PRESSED/RELEASED/LONG_PRESS)
Multi-button management

See patterns-buttons.md | Example: buttons-example.ino

Communication
I2C device scanning and diagnostics
SPI configuration
UART/Serial protocols
CSV data output

See patterns-i2c.md and patterns-csv.md | Examples: i2c-example.ino, csv-example.ino

Timing & Concurrency
Non-blocking millis() patterns
Task scheduling without delay()
Priority-based schedulers
State machines

See patterns-scheduler.md and patterns-state-machine.md | Examples: scheduler-example.ino, state-machine-example.ino

Hardware Detection
Auto-detect boards (UNO/ESP32/RP2040)
SRAM usage monitoring
Sensor fallback strategies
Adaptive configuration

See patterns-hardware-detection.md | Example: hardware-detection-example.ino

Data Persistence
EEPROM with CRC validation
SD card FAT32 logging
Wear leveling for EEPROM
Buffered writes

See patterns-data-logging.md | Example: data-logging-example.ino

Code Generation Workflow
 Identify Pattern Type - Analyze user request to determine core pattern category
 Read Reference Documentation - Consult pattern-specific reference files for implementation details
 Generate Code - Create production-ready code following quality standards
 Provide Instructions - Include wiring diagrams and usage guidance
 Mention Integration - Suggest combinations with other patterns when relevant
Quality Standards & Rules
 Quality Standards - Compilation, timing, memory safety, and error handling requirements
 Board Optimization - UNO, ESP32, and RP2040 specific optimizations and features
 Common Pitfalls - Critical mistakes to avoid in Arduino development
Code Output Template
 Code Template - Standardized structure for generated Arduino sketches
Resources
examples/ - 9 production-ready example sketches (one per pattern category)
examples/README.md - Detailed documentation for each example with wiring diagrams
scripts/generate_snippet.py - CLI tool for code generation with 9 pattern templates
assets/workflow.mmd - Mermaid diagram of code generation workflow
workflow/ - Step-by-step code generation process
rules/ - Quality standards and board-specific optimizations
templates/ - Code output templates and structure guidelines
references/ - Detailed pattern documentation and API references
references/README.md - Reference structure and formatting guide
Weekly Installs
99
Repository
wedsamuel1230/a…o-skills
GitHub Stars
14
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass