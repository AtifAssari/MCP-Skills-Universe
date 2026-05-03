---
rating: ⭐⭐
title: intelligems-core
url: https://skills.sh/victorpay1/intelligems-analytics/intelligems-core
---

# intelligems-core

skills/victorpay1/intelligems-analytics/intelligems-core
intelligems-core
Installation
$ npx skills add https://github.com/victorpay1/intelligems-analytics --skill intelligems-core
SKILL.md
/intelligems-core

Shared library that powers all Intelligems Analytics skills. Sets up your workspace with the API client, metric helpers, and configuration.

You rarely need to run this directly — other skills (like /test-verdict) automatically check for the workspace and set it up if needed.

What's Included
File	Purpose
ig_client.py	API client with automatic retry and rate-limit handling
ig_metrics.py	Extract values, uplift, confidence, and CI bounds from API responses
ig_helpers.py	Formatting, runtime calculation, variation lookup
ig_config.py	Shared thresholds (80% confidence, 10-day minimum, etc.)
ig_slack.py	Slack Block Kit formatting and webhook delivery
setup_workspace.sh	Creates ~/intelligems-analytics/ with venv and dependencies
setup_automation.sh	Creates macOS LaunchAgent for scheduled Slack delivery
Step 1: Get API Key

Ask the user for their Intelligems API key.

"What's your Intelligems API key? You can get one by contacting support@intelligems.io"

Never hardcode or assume an API key.

Step 2: Set Up Workspace

Run the setup script to create the workspace:

bash setup_workspace.sh


This creates:

~/intelligems-analytics/ — working directory
~/intelligems-analytics/venv/ — Python virtual environment
~/intelligems-analytics/.env — API key configuration

Then save the user's API key:

echo "INTELLIGEMS_API_KEY=<user's key>" > ~/intelligems-analytics/.env

Step 3: Copy Core Libraries

Copy all files from references/ into the workspace:

cp references/ig_client.py ~/intelligems-analytics/
cp references/ig_metrics.py ~/intelligems-analytics/
cp references/ig_helpers.py ~/intelligems-analytics/
cp references/ig_config.py ~/intelligems-analytics/

Step 4: Verify

Activate the environment and verify the client works:

source ~/intelligems-analytics/venv/bin/activate
python3 -c "
from ig_client import IntelligemsAPI
from dotenv import load_dotenv
import os
load_dotenv()
api = IntelligemsAPI(os.getenv('INTELLIGEMS_API_KEY'))
tests = api.get_active_experiments()
print(f'Connected. Found {len(tests)} active experiment(s).')
"


If successful, the workspace is ready for any Intelligems Analytics skill.

Weekly Installs
8
Repository
victorpay1/inte…nalytics
GitHub Stars
2
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail