---
title: openclaw-bot-dashboard
url: https://skills.sh/xmanrui/openclaw-bot-dashboard/openclaw-bot-dashboard
---

# openclaw-bot-dashboard

skills/xmanrui/openclaw-bot-dashboard/openclaw-bot-dashboard
openclaw-bot-dashboard
Installation
$ npx skills add https://github.com/xmanrui/openclaw-bot-dashboard --skill openclaw-bot-dashboard
SKILL.md
OpenClaw Dashboard Skill

Launch and manage the OpenClaw Dashboard web UI for monitoring all your bots, agents, models, and sessions.

Activation

Activate when user says:

"打开 OpenClaw-bot-review"
"打开 Openclaw dashboard"
"打开 bot review"
"打开机器人大盘"
"打开 bot-review"
"打开openclaw机器人大盘"
"open openclaw dashboard"
"open OpenClaw-bot-review"
"open bot review"
"open bot-review"
"launch bot review"
"start dashboard"
What This Skill Does
Detects the operating system (macOS/Windows)
Checks if git is installed
Downloads/clones the OpenClaw Dashboard project if not already present
Installs dependencies (npm install)
Starts the development server in background
Returns the access URL to the user
Installation Directory
macOS/Linux: ~/projects/OpenClaw-bot-review/
Windows: %USERPROFILE%\projects\OpenClaw-bot-review\
Prerequisites
Node.js 18+ must be installed
OpenClaw config at ~/.openclaw/openclaw.json (or %USERPROFILE%\.openclaw\openclaw.json on Windows)
Workflow
Step 1: Check if already running and stop it
# Check if process is already running on port 3000
# macOS/Linux
lsof -ti:3000

# Windows
netstat -ano | findstr :3000


If already running:

Stop the service first (ensure clean restart)

macOS/Linux:

lsof -ti:3000 | xargs kill -9 2>/dev/null
echo "已停止旧服务"


Windows (PowerShell):

Get-Process -Id (Get-NetTCPConnection -LocalPort 3000).OwningProcess | Stop-Process -Force
Write-Host "已停止旧服务"


Windows (cmd):

for /f "tokens=5" %a in ('netstat -ano ^| findstr :3000') do taskkill /F /PID %a
echo 已停止旧服务


Then proceed to Step 1.5.

Step 1.5: Check for updates (if project exists)

If project exists, check if there's a newer version:

If git is available:

# macOS/Linux
cd ~/projects/OpenClaw-bot-review
git fetch origin main 2>/dev/null
LOCAL=$(git rev-parse HEAD 2>/dev/null)
REMOTE=$(git rev-parse origin/main 2>/dev/null)

if [ "$LOCAL" != "$REMOTE" ]; then
  echo "update_available"
else
  echo "up_to_date"
fi

# Windows (PowerShell)
cd "$env:USERPROFILE\projects\OpenClaw-bot-review"
git fetch origin main 2>$null
$local = git rev-parse HEAD 2>$null
$remote = git rev-parse origin/main 2>$null
if ($local -ne $remote) { "update_available" } else { "up_to_date" }


If update available:

Inform user: "检测到新版本，正在更新..."
Pull latest code: git pull origin main
Reinstall dependencies: npm install
Continue to Step 5 (start service)

If up to date:

Continue to Step 5 (start service)

If git is NOT available:

Inform user: "检测到项目无 git 管理，正在重新下载最新版本..."
Remove old project directory:
# macOS/Linux
rm -rf ~/projects/OpenClaw-bot-review

# Windows (PowerShell)
Remove-Item -Recurse -Force "$env:USERPROFILE\projects\OpenClaw-bot-review"

Go to Step 3 (download project via ZIP)
Step 2: Check if project exists
# macOS/Linux
test -d ~/projects/OpenClaw-bot-review && echo "exists" || echo "not found"

# Windows (PowerShell)
Test-Path "$env:USERPROFILE\projects\OpenClaw-bot-review"


If exists, skip to Step 4.

Step 3: Download project

Option A: With git (preferred)

# macOS/Linux
mkdir -p ~/projects
cd ~/projects
git clone https://github.com/xmanrui/OpenClaw-bot-review.git

# Windows (PowerShell)
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\projects"
cd "$env:USERPROFILE\projects"
git clone https://github.com/xmanrui/OpenClaw-bot-review.git


Option B: Without git (fallback)

macOS/Linux:

mkdir -p ~/projects
cd ~/projects
curl -L https://github.com/xmanrui/OpenClaw-bot-review/archive/refs/heads/main.zip -o openclaw-dashboard.zip
unzip openclaw-dashboard.zip
mv OpenClaw-bot-review-main OpenClaw-bot-review
rm openclaw-dashboard.zip


Windows (PowerShell):

New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\projects"
cd "$env:USERPROFILE\projects"
Invoke-WebRequest -Uri "https://github.com/xmanrui/OpenClaw-bot-review/archive/refs/heads/main.zip" -OutFile "openclaw-dashboard.zip"
Expand-Archive -Path "openclaw-dashboard.zip" -DestinationPath "."
Rename-Item -Path "OpenClaw-bot-review-main" -NewName "OpenClaw-bot-review"
Remove-Item "openclaw-dashboard.zip"


Windows (cmd with curl - Windows 10+):

mkdir "%USERPROFILE%\projects" 2>nul
cd /d "%USERPROFILE%\projects"
curl -L https://github.com/xmanrui/OpenClaw-bot-review/archive/refs/heads/main.zip -o openclaw-dashboard.zip
tar -xf openclaw-dashboard.zip
ren OpenClaw-bot-review-main OpenClaw-bot-review
del openclaw-dashboard.zip

Step 4: Install dependencies (if needed)

Check if node_modules exists. If not:

# macOS/Linux
cd ~/projects/OpenClaw-bot-review
npm install

# Windows
cd "%USERPROFILE%\projects\OpenClaw-bot-review"
npm install

Step 5: Start the server

macOS/Linux:

cd ~/projects/OpenClaw-bot-review
npm run dev > /dev/null 2>&1 &


Windows (PowerShell):

cd "$env:USERPROFILE\projects\OpenClaw-bot-review"
Start-Process -NoNewWindow -FilePath "npm" -ArgumentList "run", "dev"


Windows (cmd):

cd /d "%USERPROFILE%\projects\OpenClaw-bot-review"
start /B npm run dev

Step 6: Wait for server to be ready

Poll http://localhost:3000 until it responds (max 30 seconds).

# macOS/Linux
for i in {1..30}; do
  curl -s http://localhost:3000 > /dev/null && break
  sleep 1
done

# Windows (PowerShell)
for ($i=0; $i -lt 30; $i++) {
  try {
    Invoke-WebRequest -Uri "http://localhost:3000" -UseBasicParsing -TimeoutSec 1 | Out-Null
    break
  } catch {
    Start-Sleep -Seconds 1
  }
}

Step 7: Return access URLs (required)

You MUST return both:

Local URL
LAN URL

First, actually detect the machine's LAN IPv4 address. Do not guess it.

macOS/Linux:

(ipconfig getifaddr en0 || ipconfig getifaddr en1 || hostname -I | awk '{print $1}') 2>/dev/null


Windows (PowerShell):

(Get-NetIPAddress -AddressFamily IPv4 -InterfaceAlias "Ethernet*","Wi-Fi*" | Select-Object -First 1).IPAddress


Rules:

You MUST execute an IP detection command before composing the final reply.
Do NOT guess or fabricate the LAN IP.
Do NOT omit the LAN URL just because localhost works.
You MUST include both the local URL and the LAN URL in the final reply.
If LAN IP detection fails, you MUST still include the local URL and explicitly say:
局域网访问地址：获取失败
and briefly mention that LAN IP detection failed.
Do NOT end with only a localhost URL.

Return message format:

✅ OpenClaw Dashboard 已启动！

访问地址：
- 本地访问：http://localhost:3000
- 局域网访问：http://<LAN-IP>:3000

Dashboard 会自动读取你的 OpenClaw 配置，展示所有机器人、模型、会话的状态。

需要停止服务时告诉我一声。


If LAN IP detection fails, use:

✅ OpenClaw Dashboard 已启动！

访问地址：
- 本地访问：http://localhost:3000
- 局域网访问：获取失败

原因：未能检测到当前机器的局域网 IPv4 地址。

需要停止服务时告诉我一声。

Stopping the Server

When user asks to stop:

macOS/Linux:

lsof -ti:3000 | xargs kill -9


Windows (PowerShell):

Get-Process -Id (Get-NetTCPConnection -LocalPort 3000).OwningProcess | Stop-Process -Force


Windows (cmd):

for /f "tokens=5" %a in ('netstat -ano ^| findstr :3000') do taskkill /F /PID %a

Error Handling
Node.js not found: Tell user to install Node.js 18+ from https://nodejs.org/
Port 3000 already in use: Check if it's the dashboard (return URL) or another service (suggest using a different port with PORT=3001 npm run dev)
OpenClaw config not found: Warn that dashboard may not work properly without ~/.openclaw/openclaw.json
Download failed: Suggest checking internet connection or manually downloading from GitHub
npm install failed: Suggest running npm cache clean --force and retrying
Notes
The server runs in background and persists until stopped or system reboot
Dashboard reads config directly from ~/.openclaw/openclaw.json - no database needed
Supports auto-refresh, dark/light theme, i18n (Chinese/English)
Includes pixel-art office animation for fun visualization
Platform Detection
# Detect OS
uname -s  # macOS: Darwin, Linux: Linux, Windows (Git Bash): MINGW*/MSYS*

# Windows detection in PowerShell
$PSVersionTable.Platform  # Win32NT or empty on Windows

Git Detection
# Check if git is available
git --version
# Exit code 0 = installed, non-zero = not installed


Detection logic:

Run git --version at the beginning
Store result (available/not available)
Use this result throughout the workflow

If git not available:

Always use ZIP download method
Always force re-download when project exists (to get latest version)
Clean up old directory before downloading
Implementation Tips
Always stop old service first - ensures clean restart with latest code
Check git availability at the start - determines update strategy
With git: Check for updates and pull if needed
Without git: Force re-download ZIP to ensure latest version
No user confirmation needed - auto-update and restart for best UX
Use background process management to avoid blocking
Provide clear feedback at each step ("已停止旧服务", "检测到新版本，正在更新...", "正在重新下载最新版本...")
Handle both PowerShell and cmd on Windows
Clean up temporary files (zip archives)
Log errors for debugging but keep user messages simple
Always ensure latest code - either via git pull or re-download
Weekly Installs
105
Repository
xmanrui/opencla…ashboard
GitHub Stars
3
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn