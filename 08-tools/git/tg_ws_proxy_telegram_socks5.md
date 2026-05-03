---
title: tg-ws-proxy-telegram-socks5
url: https://skills.sh/aradotso/trending-skills/tg-ws-proxy-telegram-socks5
---

# tg-ws-proxy-telegram-socks5

skills/aradotso/trending-skills/tg-ws-proxy-telegram-socks5
tg-ws-proxy-telegram-socks5
Installation
$ npx skills add https://github.com/aradotso/trending-skills --skill tg-ws-proxy-telegram-socks5
SKILL.md
TG WS Proxy

Skill by ara.so — Daily 2026 Skills collection.

TG WS Proxy is a local SOCKS5 proxy server for Telegram Desktop that reroutes traffic through WebSocket (WSS) connections to Telegram's Data Centers, bypassing network-level blocking without external servers.

Telegram Desktop → SOCKS5 (127.0.0.1:1080) → TG WS Proxy → WSS → Telegram DC

How It Works
Starts a local SOCKS5 proxy on 127.0.0.1:1080
Intercepts connections to Telegram IP addresses
Extracts DC ID from MTProto obfuscation init packet
Opens a WebSocket (TLS) connection to the matching DC via Telegram domains
Falls back to direct TCP if WebSocket returns a 302 redirect
Installation
From Source (All Platforms)
git clone https://github.com/Flowseal/tg-ws-proxy.git
cd tg-ws-proxy
pip install -e .

Run Console Proxy (No GUI)
tg-ws-proxy

Run with Tray GUI
# Windows
tg-ws-proxy-tray-win

# macOS
tg-ws-proxy-tray-macos

# Linux
tg-ws-proxy-tray-linux

Linux — AUR (Arch-based)
paru -S tg-ws-proxy-bin
# or
git clone https://aur.archlinux.org/tg-ws-proxy-bin.git
cd tg-ws-proxy-bin
makepkg -si

Linux — systemd CLI
sudo systemctl start tg-ws-proxy-cli@1080

Linux — .deb

Download TgWsProxy_linux_amd64.deb from releases and install:

sudo dpkg -i TgWsProxy_linux_amd64.deb

Linux — binary
chmod +x TgWsProxy_linux_amd64
./TgWsProxy_linux_amd64

CLI Reference
tg-ws-proxy [--port PORT] [--host HOST] [--dc-ip DC:IP ...] [-v]

Argument	Default	Description
--port	1080	SOCKS5 proxy port
--host	127.0.0.1	SOCKS5 proxy bind host
--dc-ip	2:149.154.167.220, 4:149.154.167.220	Target IP per DC ID (repeat for multiple)
-v, --verbose	off	Enable DEBUG logging
Examples
# Default startup
tg-ws-proxy

# Custom port
tg-ws-proxy --port 9050

# Specify multiple DCs with IPs
tg-ws-proxy --dc-ip 1:149.154.175.205 --dc-ip 2:149.154.167.220 --dc-ip 4:149.154.167.220

# Verbose debug logging
tg-ws-proxy -v

# Full custom example
tg-ws-proxy --host 0.0.0.0 --port 1080 --dc-ip 2:149.154.167.220 -v

Configuration File

The tray application stores config in a platform-specific location:

Windows: %APPDATA%/TgWsProxy/config.json
macOS: ~/Library/Application Support/TgWsProxy/config.json
Linux: ~/.config/TgWsProxy/config.json (or $XDG_CONFIG_HOME/TgWsProxy/config.json)
config.json structure
{
  "port": 1080,
  "dc_ip": [
    "2:149.154.167.220",
    "4:149.154.167.220"
  ],
  "verbose": false
}

pyproject.toml Script Registration

CLI entry points are declared in pyproject.toml:

[project.scripts]
tg-ws-proxy = "proxy.tg_ws_proxy:main"
tg-ws-proxy-tray-win = "windows:main"
tg-ws-proxy-tray-macos = "macos:main"
tg-ws-proxy-tray-linux = "linux:main"

Connecting Telegram Desktop
Manual Setup
Open Telegram Desktop
Go to Settings → Advanced → Connection type → Use custom proxy
Click Add Proxy and set:
Type: SOCKS5
Server: 127.0.0.1
Port: 1080
Username/Password: leave empty
Click Save and enable the proxy
Automatic (Tray GUI)

Right-click the tray icon → "Открыть в Telegram" — this opens a tg://socks deep link that auto-configures Telegram Desktop.

Code Examples
Launching the Proxy Programmatically
from proxy.tg_ws_proxy import main
import threading

# Run proxy in background thread
proxy_thread = threading.Thread(target=main, daemon=True)
proxy_thread.start()

Using the Proxy with Python Requests (via PySocks)
pip install requests[socks]

import requests

proxies = {
    "http":  "socks5h://127.0.0.1:1080",
    "https": "socks5h://127.0.0.1:1080",
}

response = requests.get("https://api.telegram.org/botTOKEN/getMe", proxies=proxies)
print(response.json())

Using with Telethon (MTProto client)
from telethon import TelegramClient
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
import socks

client = TelegramClient(
    'session',
    api_id=int(os.environ["TG_API_ID"]),
    api_hash=os.environ["TG_API_HASH"],
    proxy=(socks.SOCKS5, '127.0.0.1', 1080)
)

async def main():
    await client.start()
    me = await client.get_me()
    print(me.username)

import asyncio
asyncio.run(main())

Custom DC IP Mapping (Python)
import subprocess

dc_map = {
    1: "149.154.175.205",
    2: "149.154.167.220",
    3: "149.154.175.100",
    4: "149.154.167.220",
    5: "91.108.56.130",
}

dc_args = []
for dc_id, ip in dc_map.items():
    dc_args += ["--dc-ip", f"{dc_id}:{ip}"]

subprocess.Popen(["tg-ws-proxy", "--port", "1080"] + dc_args)

Building Binaries (PyInstaller)
# Windows
pyinstaller packaging/windows.spec

# macOS
pyinstaller packaging/macos.spec

# Linux
pyinstaller packaging/linux.spec


Builds are also produced automatically via GitHub Actions in .github/workflows/build.yml.

Minimum OS Support
Binary	Minimum Version
TgWsProxy_windows.exe	Windows 10+
TgWsProxy_windows_7_64bit.exe	Windows 7 x64
TgWsProxy_windows_7_32bit.exe	Windows 7 x32
TgWsProxy_macos_universal.dmg (Intel)	macOS 10.15+
TgWsProxy_macos_universal.dmg (Apple Silicon)	macOS 11.0+
TgWsProxy_linux_amd64	Linux x86_64 + AppIndicator
Troubleshooting
Telegram still not connecting
Confirm the proxy is running: tg-ws-proxy -v and watch for connection logs
Make sure Telegram Desktop is set to SOCKS5, not HTTP/MTProxy
Try restarting the proxy from the tray menu (Перезапустить прокси)
Check no firewall or other process is blocking port 1080
Port already in use
# Find what's using port 1080
lsof -i :1080        # macOS/Linux
netstat -ano | findstr :1080  # Windows

# Run on a different port
tg-ws-proxy --port 1081


Then update Telegram Desktop's proxy port to 1081.

Windows Defender false positive (Wacatac)
Download the win7 variant — functionally identical, lower detection rate
Or temporarily disable Defender, download, add to exclusions, re-enable
Verify the build on VirusTotal using the file hash
macOS "unverified developer" block
Open System Settings → Privacy & Security
Scroll down and click Open Anyway next to TG WS Proxy
Linux tray icon not visible

AppIndicator is required. Install it:

# Ubuntu/Debian
sudo apt install gir1.2-appindicator3-0.1

# Fedora
sudo dnf install libappindicator-gtk3

WebSocket not available — proxy falls back to TCP

This is expected behavior. If WS returns a 302 redirect, the proxy automatically uses direct TCP. No action needed; Telegram will still connect.

Verbose debug logging
tg-ws-proxy -v


Or set "verbose": true in config.json for the tray app.

Weekly Installs
648
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