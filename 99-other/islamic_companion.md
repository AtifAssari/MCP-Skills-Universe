---
title: islamic-companion
url: https://skills.sh/ilmimris/islamic-skills/islamic-companion
---

# islamic-companion

skills/ilmimris/islamic-skills/islamic-companion
islamic-companion
Installation
$ npx skills add https://github.com/ilmimris/islamic-skills --skill islamic-companion
SKILL.md
Islamic Companion Skill

Unified tool for prayer times, fasting schedules, and Zakat calculations.

This skill consolidates Islamic utilities into a single CLI with shared configuration and efficient caching.

Features
Prayer Times: Retrieve daily prayer times (Fajr, Dhuhr, Asr, Maghrib, Isha).
Fasting: Check Imsak and Maghrib times for fasting.
Zakat: Calculate Nisab thresholds for Gold and Silver based on current market prices.
Quran: Search for verses by keyword or fetch specific Surah/Ayah with translation.
Calendar: Generate a monthly prayer schedule for any city.
Quotes: Fetch and display random Islamic quotes or setup daily automation.
Scheduler: Generate OpenClaw cron commands to schedule daily prayer reminders.
Caching: Minimizes API calls by caching daily results locally.
Usage

Run the CLI using the bash script:

# Get today's prayer times for Jakarta (explicit timezone override)
./bin/islamic-companion prayer --today --lat -6.2088 --long 106.8456 --tz Asia/Jakarta

# Setup daily quote automation for specific location
./bin/islamic-companion prayer --sync --lat -6.2088 --long 106.8456 --timezone Asia/Jakarta

# Get a random quote
./bin/islamic-companion quotes --random

# Get monthly calendar (Example: Serang, Banten)
./bin/islamic-companion calendar --city "Serang" --month 2 --year 2026

# Sync prayer schedule to cron (generates commands)
./bin/islamic-companion prayer --sync --lat -6.2088 --long 106.8456 --tz Asia/Jakarta

# Check fasting times (Imsak/Maghrib)
./bin/islamic-companion fasting --today --lat -6.2088 --long 106.8456

# Check Zakat Nisab values
./bin/islamic-companion zakat --nisab

# Search Quran for keyword
./bin/islamic-companion quran --search "sabar"

# Get specific Surah (e.g., Al-Fatihah)
./bin/islamic-companion quran --surah 1

# Get specific Ayah (e.g., Al-Baqarah:255)
./bin/islamic-companion quran --surah 2 --ayah 255

Configuration

Edit config.json to set your calculation method and Zakat preferences. Location is provided via CLI arguments. Defaults to UTC if no timezone is specified.

{
  "calculation": {
    "method": 20,
    "school": 0
  },
  "zakat": {
    "currency": "IDR",
    "gold_gram_threshold": 85,
    "api_key": ""
  },
  "timezone": "Asia/Jakarta",
  "quran_language": "id"
}

Calculation Methods
Method 20: Kemenag RI (Indonesia)
School 0: Standard (Shafi, Maliki, Hanbali)
School 1: Hanafi
User Intent	Command Executed
"Get prayer times"	./bin/islamic-companion prayer --today --lat [LAT] --long [LONG]
"Show me the calendar for [City]"	./bin/islamic-companion calendar --city [City]
"Setup daily Islamic quotes"	./bin/islamic-companion quotes --setup
"Give me a random Islamic quote"	./bin/islamic-companion quotes --random
"Sync prayer schedule"	./bin/islamic-companion prayer --sync
"When is Imsak?"	./bin/islamic-companion fasting --today
"Check Zakat Nisab"	./bin/islamic-companion zakat --nisab
"Search Quran for [keyword]"	./bin/islamic-companion quran --search "[keyword]"
"Read Surah [Name/Number]"	./bin/islamic-companion quran --surah [Number]
"Read Surah [Number] Ayah [Number]"	./bin/islamic-companion quran --surah [Number] --ayah [Number]
Dependencies
System: bash, curl, jq (Required for Quran features and recommended for speed)
Python (Alternative Implementation): python3, requests (Only needed if using src/main.py directly)
Security & Privacy

[!WARNING] API Keys: The Zakat feature uses an API key. You can store it in config.json (less secure) or export it as an environment variable ZAKAT_API_KEY (recommended).

[!IMPORTANT] Automation: The --sync and --setup commands generate cron schedules. Always review the output before adding it to your system crontab.

If you are using the cron tool, you MUST parse the JSON string from the CRON_ADD: output into a JSON object. Do not pass the string directly.

Installation
Clone the repository or download the skill.
Install Python dependencies:
pip install -r requirements.txt

Ensure curl is installed. jq is recommended for JSON parsing speed and reliability.

Run the CLI using the bash script wrapper, which handles configuration loading and environment setup. Location must be provided on-the-fly:

Get today's prayer times (uses HTTPS)

./bin/islamic-companion prayer --today --lat -6.2088 --long 106.8456


## Tools

When installing this skill for openclaw, the agent should update `TOOLS.md` to insert these lines:

- Get today's prayer times for Jakarta (explicit timezone override)
    ```
    ~/.openclaw/skills/islamic-companion/bin/islamic-companion prayer --today --lat -6.2088 --long 106.8456 --tz Asia/Jakarta
    ```
- Setup daily quote automation for specific location
    ```
    ~/.openclaw/skills/islamic-companion/bin/islamic-companion prayer --sync --lat -6.2088 --long 106.8456 --timezone Asia/Jakarta
    ```
- Get a random quote
    ```
    ~/.openclaw/skills/islamic-companion/bin/islamic-companion quotes --random
    ```
- Get monthly calendar (Example: Serang, Banten)
    ```
    ~/.openclaw/skills/islamic-companion/bin/islamic-companion calendar --city "Serang" --month 2 --year 2026
    ```
- Sync prayer schedule to cron (generates commands)
    ```
    ~/.openclaw/skills/islamic-companion/bin/islamic-companion prayer --sync --lat -6.2088 --long 106.8456 --tz Asia/Jakarta
    ```
- Check fasting times (Imsak/Maghrib)
    ```
    ~/.openclaw/skills/islamic-companion/bin/islamic-companion fasting --today --lat -6.2088 --long 106.8456
    ```
- Check Zakat Nisab values
    ```
    ~/.openclaw/skills/islamic-companion/bin/islamic-companion zakat --nisab
    ```
- Search Quran for keyword
    ```
    ~/.openclaw/skills/islamic-companion/bin/islamic-companion quran --search "sabar"
    ```
- Get specific Surah (e.g., Al-Fatihah)
    ```
    ~/.openclaw/skills/islamic-companion/bin/islamic-companion quran --surah 1
    ```
- Get specific Ayah (e.g., Al-Baqarah:255)
    ```
    ~/.openclaw/skills/islamic-companion/bin/islamic-companion quran --surah 2 --ayah 255
    ```


Weekly Installs
38
Repository
ilmimris/islamic-skills
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn