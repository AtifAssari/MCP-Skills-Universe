---
title: mhr-cfw-domain-fronting-relay
url: https://skills.sh/aradotso/trending-skills/mhr-cfw-domain-fronting-relay
---

# mhr-cfw-domain-fronting-relay

skills/aradotso/trending-skills/mhr-cfw-domain-fronting-relay
mhr-cfw-domain-fronting-relay
Installation
$ npx skills add https://github.com/aradotso/trending-skills --skill mhr-cfw-domain-fronting-relay
SKILL.md
MHR-CFW Domain-Fronting Relay

Skill by ara.so — Daily 2026 Skills collection.

MHR-CFW (MasterHttpRelay + Cloudflare Worker) is a Python-based domain-fronting relay that routes HTTP/SOCKS5 proxy traffic through Google Apps Script (GAS) and Cloudflare Workers. Network DPI filters see only traffic to www.google.com, while the actual destination is hidden inside the relay chain.

Traffic Flow
Client → Local Proxy (127.0.0.1:8085)
           ↓
       Google IP (216.239.38.120) — DPI sees www.google.com
           ↓
       Google Apps Script Web App (Relay)
           ↓
       Cloudflare Worker
           ↓
       Target Website

Installation
git clone https://github.com/denuitt1/mhr-cfw.git
cd mhr-cfw
pip install -r requirements.txt


If PyPI is blocked:

pip install -r requirements.txt \
  -i https://mirror-pypi.runflare.com/simple/ \
  --trusted-host mirror-pypi.runflare.com

Full Setup Guide
Step 1: Deploy the Cloudflare Worker
Log in to Cloudflare Dashboard
Navigate to Compute > Workers & Pages
Click Create Application → Start with Hello World → Deploy
Click Edit code, delete all default code
Paste the contents of script/worker.js from the repo
Edit the worker URL constant:
const WORKER_URL = "your-worker-name.workers.dev";

Click Deploy — note your worker URL (e.g., your-worker-name.workers.dev)
Step 2: Deploy the Google Apps Script Relay
Go to script.google.com and create a New project
Delete all default code
Paste the contents of script/Code.gs from the repo
Edit these two constants at the top:
const AUTH_KEY = "your-secret-password-here";   // choose a strong password
const WORKER_URL = "https://your-worker-name.workers.dev";

Click Deploy → New deployment
Type: Web app
Execute as: Me
Who has access: Anyone
Click Deploy and copy the Deployment ID (long random string like AKfycb...)
Step 3: Configure config.json
cp config.example.json config.json


Edit config.json:

{
  "mode": "apps_script",
  "google_ip": "216.239.38.120",
  "front_domain": "www.google.com",
  "script_id": "AKfycbXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
  "auth_key": "your-secret-password-here",
  "listen_host": "127.0.0.1",
  "listen_port": 8085,
  "socks5_enabled": true,
  "socks5_port": 1080,
  "log_level": "INFO",
  "verify_ssl": true
}

Field	Description
mode	Always "apps_script" for GAS relay
google_ip	IP of Google's infrastructure for fronting
front_domain	Domain shown to DPI (www.google.com)
script_id	Your GAS Deployment ID from Step 2
auth_key	Must match AUTH_KEY in Code.gs
listen_host	Local bind address (keep 127.0.0.1)
listen_port	HTTP proxy port (default 8085)
socks5_enabled	Enable SOCKS5 proxy on socks5_port
socks5_port	SOCKS5 proxy port (default 1080)
log_level	DEBUG, INFO, WARNING, ERROR
verify_ssl	Verify SSL certs; set false to skip
Step 4: Run the Proxy

Linux/macOS:

bash start.sh
# or
python3 main.py


Windows:

start.bat


Expected output:

[INFO] HTTP proxy running on 127.0.0.1:8085
[INFO] SOCKS5 proxy running on 127.0.0.1:1080

Using the Proxy
Browser via FoxyProxy

Install FoxyProxy:

Chrome: Chrome Web Store
Firefox: Firefox Add-ons

Configure FoxyProxy:

Proxy Type: HTTP or SOCKS5
Host: 127.0.0.1
Port: 8085 (HTTP) or 1080 (SOCKS5)
curl (HTTP proxy)
curl -x http://127.0.0.1:8085 https://ipleak.net/json/

curl (SOCKS5 proxy)
curl --socks5 127.0.0.1:1080 https://ipleak.net/json/

Python requests
import requests

proxies = {
    "http": "http://127.0.0.1:8085",
    "https": "http://127.0.0.1:8085",
}

response = requests.get("https://ipleak.net/json/", proxies=proxies)
print(response.json())

Python with SOCKS5
import requests

proxies = {
    "http": "socks5://127.0.0.1:1080",
    "https": "socks5://127.0.0.1:1080",
}

response = requests.get("https://ipleak.net/json/", proxies=proxies)
print(response.json())

Configuration Patterns
Minimal config (HTTP only, no SOCKS5)
{
  "mode": "apps_script",
  "google_ip": "216.239.38.120",
  "front_domain": "www.google.com",
  "script_id": "YOUR_DEPLOYMENT_ID",
  "auth_key": "YOUR_AUTH_KEY",
  "listen_host": "127.0.0.1",
  "listen_port": 8085,
  "socks5_enabled": false,
  "log_level": "INFO",
  "verify_ssl": true
}

Debug config (verbose logging, skip SSL verification)
{
  "mode": "apps_script",
  "google_ip": "216.239.38.120",
  "front_domain": "www.google.com",
  "script_id": "YOUR_DEPLOYMENT_ID",
  "auth_key": "YOUR_AUTH_KEY",
  "listen_host": "127.0.0.1",
  "listen_port": 8085,
  "socks5_enabled": true,
  "socks5_port": 1080,
  "log_level": "DEBUG",
  "verify_ssl": false
}

Listen on all interfaces (for LAN sharing)
{
  "listen_host": "0.0.0.0",
  "listen_port": 8085
}


⚠️ Only use 0.0.0.0 on trusted networks. Anyone on the LAN can use your proxy.

Cloudflare Worker (script/worker.js) — Key Structure
// The worker receives proxied requests and forwards them to the target
const WORKER_URL = "your-worker-name.workers.dev"; // set this to your own worker

addEventListener("fetch", event => {
  event.respondWith(handleRequest(event.request));
});


The worker:

Receives requests from GAS relay
Extracts the target URL from the request
Fetches the target on behalf of the client
Returns the response back through the chain
Google Apps Script (script/Code.gs) — Key Structure
const AUTH_KEY = "your-secret-password-here";      // must match config.json auth_key
const WORKER_URL = "https://your-worker.workers.dev";

function doPost(e) {
  // Validates AUTH_KEY, extracts target URL, forwards via WORKER_URL
}


The GAS relay:

Exposes a public HTTPS endpoint (/exec) that acts as the domain-fronted relay
Validates AUTH_KEY on every request
Forwards validated requests to your Cloudflare Worker
Verifying It Works

After starting the proxy and configuring your browser:

Visit ipleak.net — your IP should show as a Cloudflare IP
Visit whoer.net — should reflect Cloudflare's location
Via curl:
curl -x http://127.0.0.1:8085 https://ipleak.net/json/ | python3 -m json.tool

Look for "ip" showing a Cloudflare address range.
Troubleshooting
Proxy starts but no traffic gets through
Verify script_id in config.json is the Deployment ID, not the Script ID
Re-check that auth_key in config.json exactly matches AUTH_KEY in Code.gs
In GAS, confirm deployment is set to Execute as: Me and Who has access: Anyone
Try redeploying the GAS app — old deployments sometimes break
SSL errors
"verify_ssl": false


Set to false temporarily to diagnose. Re-enable for production use.

pip install fails (PyPI blocked)
pip install -r requirements.txt \
  -i https://mirror-pypi.runflare.com/simple/ \
  --trusted-host mirror-pypi.runflare.com

GAS quota exceeded

Google Apps Script has daily quotas (~20,000 URL fetch calls/day for free accounts). If the relay stops working mid-day:

Use a different Google account for a fresh GAS deployment
Deploy multiple GAS relays and alternate script_id values
Port already in use
{
  "listen_port": 8086,
  "socks5_port": 1081
}


Change ports in config.json and update your browser/FoxyProxy settings.

Cloudflare Worker errors (5xx)
Check the worker is deployed and the WORKER_URL in Code.gs matches exactly
Visit https://your-worker.workers.dev directly in browser — should respond (even with an error page) rather than timeout
Check Cloudflare Worker logs in the dashboard under Workers & Pages > your worker > Logs
Debug logging
"log_level": "DEBUG"


Restart main.py — you'll see each relay hop logged to stdout.

Environment Variable Pattern for Automation

When scripting deployment or CI, avoid hardcoding secrets. Use environment variables and generate config dynamically:

import json
import os

config = {
    "mode": "apps_script",
    "google_ip": "216.239.38.120",
    "front_domain": "www.google.com",
    "script_id": os.environ["GAS_DEPLOYMENT_ID"],
    "auth_key": os.environ["MHR_AUTH_KEY"],
    "listen_host": "127.0.0.1",
    "listen_port": int(os.environ.get("MHR_PORT", "8085")),
    "socks5_enabled": True,
    "socks5_port": 1080,
    "log_level": os.environ.get("MHR_LOG_LEVEL", "INFO"),
    "verify_ssl": True
}

with open("config.json", "w") as f:
    json.dump(config, f, indent=2)

print("config.json written")


Then run:

export GAS_DEPLOYMENT_ID="AKfycbXXXXXXXXXXXXXX"
export MHR_AUTH_KEY="$(openssl rand -hex 32)"
python3 write_config.py
python3 main.py

Project File Reference
File	Purpose
main.py	Entry point — starts HTTP and SOCKS5 proxy listeners
config.json	Runtime configuration (copy from config.example.json)
config.example.json	Template configuration with placeholder values
script/worker.js	Cloudflare Worker source — deploy to Cloudflare
script/Code.gs	Google Apps Script relay source — deploy to GAS
start.bat	Windows launcher
start.sh	Linux/macOS launcher
requirements.txt	Python dependencies
Weekly Installs
59
Repository
aradotso/trending-skills
GitHub Stars
42
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykFail