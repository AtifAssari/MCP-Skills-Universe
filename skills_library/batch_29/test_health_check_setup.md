---
title: test-health-check-setup
url: https://skills.sh/victorpay1/intelligems-plugins/test-health-check-setup
---

# test-health-check-setup

skills/victorpay1/intelligems-plugins/test-health-check-setup
test-health-check-setup
Installation
$ npx skills add https://github.com/victorpay1/intelligems-plugins --skill test-health-check-setup
SKILL.md
/test-health-check-setup

Create the Intelligems Test Health Check automation through conversation.

What you'll get:

Daily Slack messages with health status for each active test
Alerts when tests need attention (conversion drops, low orders)
Clear statistical outlook for each test
One message per test (not per brand)

Based on: Jerica's tutorial

Setup Workflow

Follow these steps in order. Ask questions conversationally, then create files directly.

Step 1: Project Directory

Ask where to create the project files.

Default: current working directory. If it's empty or home directory, suggest creating ~/Desktop/intelligems-slack-health-check/.

Step 2: Slack Webhook

Ask: "Do you already have a Slack webhook URL, or do you need help creating one?"

If they need help creating one:

Guide them through:

Go to https://api.slack.com/apps
Click "Create New App" > "From scratch"
Name it "Intelligems Health Check" and select workspace
Click "Incoming Webhooks" in sidebar
Toggle "Activate Incoming Webhooks" to On
Click "Add New Webhook to Workspace"
Select the channel and click "Allow"
Copy the webhook URL (starts with https://hooks.slack.com/services/)

If using Chrome browser automation: Offer to guide them through the Slack API website step by step.

Once they have the URL, save it for Step 4.

Step 3: Intelligems API Key

Ask: "What's your Intelligems API key?"

Format is ig_live_xxxxxxxxxx. If they don't have one, direct them to contact Intelligems support.

This is for a single brand - unlike the agency digest which handles multiple brands.

Step 4: Optional Threshold Customization

Show the default thresholds and ask if they want to change any:

Setting	Default	Purpose
MIN_SESSIONS_FOR_SIGNIFICANCE	100	Minimum visitors before analyzing
MIN_ORDERS_FOR_SIGNIFICANCE	10	Minimum orders before analyzing
CONVERSION_DROP_ALERT_THRESHOLD	0.20	Alert if conversion drops 20%+
MIN_CONFIDENCE_LEVEL	0.95	95% confidence for conclusions

Ask: "These are the default thresholds. Want to customize any of them?"

Step 5: Schedule Time

Ask: "What time should the daily health check run? (Default: 10:00 AM)"

Convert their answer to 24-hour format for the scheduler.

Step 6: Create Files

Read the templates from references/file-templates.md and create these files in the project directory:

intelligems_health_check.py - Main script (copy exactly from template)
config.py - Fill in user's thresholds
.env - Fill in user's API key and Slack webhook
requirements.txt - Python dependencies (copy from template)
.gitignore - Protects credentials (copy from template)
Step 7: Install Dependencies

Create a virtual environment and install dependencies:

cd {PROJECT_DIR}
python3 -m venv venv
./venv/bin/pip install -r requirements.txt


This isolates packages and avoids conflicts with system Python.

Step 8: Daily Scheduler (Optional, macOS only)

Ask: "Want to set up automatic daily health checks?"

If yes:

Create the plist file at ~/Library/LaunchAgents/com.intelligems.health-check.plist using template
Replace {PROJECT_DIR} with the actual project path (uses venv Python automatically)
Replace {HOUR} and {MINUTE} with user's chosen time
Load the scheduler: launchctl load ~/Library/LaunchAgents/com.intelligems.health-check.plist

Tell user: "Your computer needs to be on at the scheduled time for the check to run."

Step 9: Test

Ask: "Want to run a test health check now?"

If yes, run:

./venv/bin/python3 intelligems_health_check.py


Check Slack for the message. The format should show:

Header with status icon (checkmark or warning)
Test name
Runtime and sessions
Control vs variant metrics
Key metrics with lift percentages
Statistical outlook
Step 10: Confirm Setup

Summarize what was created:

Files location
API key configured (masked)
Scheduler status and time
Commands for later use
Commands After Setup
# Run health check now (from project directory)
./venv/bin/python3 intelligems_health_check.py

# Check scheduler status (macOS)
launchctl list | grep health-check

Customizing Thresholds Later

Edit config.py:

# Alert if conversion drops more than this percentage
CONVERSION_DROP_ALERT_THRESHOLD = 0.20  # 20%

# Minimum data before analyzing
MIN_SESSIONS_FOR_SIGNIFICANCE = 100
MIN_ORDERS_FOR_SIGNIFICANCE = 10

# Confidence level for conclusions
MIN_CONFIDENCE_LEVEL = 0.95  # 95%

Troubleshooting

No Slack message?

Check the terminal for error messages
Verify webhook URL in .env
Verify API key format: ig_live_xxxxxxxxxx

Scheduler not running (macOS)?

launchctl list | grep health-check


Getting warnings for healthy tests?

Adjust CONVERSION_DROP_ALERT_THRESHOLD in config.py
Lower the percentage for stricter monitoring
Differences from Agency Digest
This Skill	Agency Digest
Single brand	Multiple brands
Health alerts per test	Summary per brand
Conversion drop detection	Lift + confidence focus
Based on Jerica's tutorial	Based on Victor's approach
Weekly Installs
9
Repository
victorpay1/inte…-plugins
GitHub Stars
1
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykFail