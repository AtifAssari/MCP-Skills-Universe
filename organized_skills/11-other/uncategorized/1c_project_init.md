---
rating: ⭐⭐⭐
title: 1c-project-init
url: https://skills.sh/arman-kudaibergenov/1c-ai-development-kit/1c-project-init
---

# 1c-project-init

skills/arman-kudaibergenov/1c-ai-development-kit/1c-project-init
1c-project-init
Installation
$ npx skills add https://github.com/arman-kudaibergenov/1c-ai-development-kit --skill 1c-project-init
SKILL.md
/1c-project-init — Initialize or enrich 1C project

Source workspace: C:\Users\YOUR_USERNAME\workspace\ai\1c-AI-workspace

Mode detection
.claude/skills/ exists in target → enrich (sync missing/outdated skills & docs)
No .claude/skills/ → new (full init)
CRITICAL: Use skills, not manual 1C commands

NEVER run 1cv8 DESIGNER manually when a skill exists for the operation.

Task	WRONG	RIGHT
Dump XML	ssh ... docker exec ... 1cv8 DESIGNER /DumpConfigToFiles	/db-dump-xml skill
Load XML	docker exec ... 1cv8 DESIGNER /LoadConfigFromFiles	/db-load-xml skill
Build CF	manual 1cv8	/db-dump-cf, /cf-init skills

The /db-dump-xml skill reads .v8-project.json automatically and connects to the remote server directly — no need to run DESIGNER inside the container. License PROF on the local machine is sufficient for all DESIGNER operations including DumpConfigToFiles and extension dumps.

Steps
1. Determine target path
If argument provided → use it
Otherwise → current working directory (pwd)
2. Run init script
powershell.exe -NoProfile -File "C:\Users\YOUR_USERNAME\workspace\ai\1c-AI-workspace\.claude\skills\1c-project-init\scripts\init.ps1" -TargetPath "<target>" -Mode <new|enrich>


Script output lists what was copied/updated.

3. If mode = new — collect project info interactively

Ask ALL questions upfront in a single AskUserQuestion call (multiple questions at once).

Question order matters — project type and extension names come FIRST:

Project type (options): configuration / extension / configuration + extension / external-processor / other
Extension name(s) — ask only if type includes extension. If multiple, comma-separated (e.g. МоёРасширение, ДругоеРасширение)
1C base name (e.g. Forte, Buh)
Platform version: 8.3.24 / 8.3.25 / 8.3.27
Web publication name (e.g. forte, buh) — for HTTP API and playwright
Admin login and password — for .v8-project.json

Note: questions 1+2 can be asked together in first call; 3-6 in second call if user answered that extensions are involved. Or ask all in one call if possible.

Platform → server mapping (all on CT107 / YOUR_EDT_SERVER):

8.3.24 → server YOUR_EDT_SERVER:1641, container onec-server-24, web port 8081
8.3.25 → server YOUR_EDT_SERVER:1541, container onec-server-25, web port 8080
8.3.27 → server YOUR_EDT_SERVER:1741, container onec-server-27, web port 8082
4. Generate CLAUDE.md

Read template: C:\Users\YOUR_USERNAME\workspace\ai\1c-AI-workspace\.claude\skills\1c-project-init\templates\CLAUDE.md.template Fill all placeholders:

{{PROJECT_NAME}} — project name
{{PROJECT_DESCRIPTION}} — brief description (include project type + extensions if applicable)
{{V8_VERSION}} — platform version (e.g. 8.3.25)
{{SERVER}} — YOUR_EDT_SERVER
{{PORT}} — from platform map
{{SERVER_SUFFIX}} — 24 / 25 / 27
{{WEB_PORT}} — from platform map
{{BASE_NAME}} — 1C base name
{{PUBLICATION}} — web publication name
{{EXTENSION_LINE}} — - Extensions: <names> if extensions present, else omit line
{{DEV_ZONE}} — src/ / ext/<ExtName>/ / src/ + ext/<ExtName>/
{{DEV_ZONE_NOTE}} — All modifications go into the extension, not the base configuration. if extension-only or mixed; empty if configuration-only
{{STRUCTURE_LINES}} — include src/ line if has config, ext/ line if has extensions:
config: src/ — configuration source
extension: ext/<ExtName>/ — extension source (primary development zone)
both: src/ — base configuration source (read-only reference)\next/<ExtName>/ — extension source (PRIMARY development zone)

Write to <target>/CLAUDE.md.

5. Generate .mcp.json

Read template: C:\Users\YOUR_USERNAME\workspace\ai\1c-AI-workspace\.claude\skills\1c-project-init\templates\mcp.json.template Fill all placeholders:

{{PROJECT_NAME}} — project directory name (for bsl-lsp container)
{{PUBLICATION}} — web publication name (for ai-debug URL)
{{WEB_PORT}} — from platform map (8081/8080/8082)
{{ADMIN_USER}} — admin login
{{ADMIN_PWD}} — admin password
{{CODEMETADATA_URL}} — codemetadata MCP URL. Format: http://YOUR_MCP_SERVER:<PORT>/mcp. Port from registry: next free in 7530+ range. If codemetadata not yet deployed, use placeholder http://YOUR_MCP_SERVER:{{CODEMETADATA_PORT}}/mcp and note in report.

Write to <target>/.mcp.json.

6. Generate .v8-project.json if not exists

Read template: C:\Users\YOUR_USERNAME\workspace\ai\1c-AI-workspace\.claude\skills\1c-project-init\templates\v8-project.json.template Fill all placeholders:

{{V8PATH}} — C:\\Program Files\\1cv8\\<V8_VERSION>\\bin matching the server platform. NEVER leave empty — local default may be a different version.
{{PORT}} — from platform map (1641/1541/1741)
{{BASE_NAME}} — 1C base name
{{ADMIN_USER}} — admin login
{{ADMIN_PWD}} — admin password
{{WEB_PORT}} — from platform map (8081/8080/8082)
{{PUBLICATION}} — web publication name

Write to <target>/.v8-project.json.

7. Create openspec structure if mode = new
openspec/
  project.md        ← project context for AI
  changes/          ← active proposals
  specs/            ← feature specs
  archive/          ← done
dist/               ← built artifacts (CFE/CF/EPF) — tracked in git for distribution

8. Deploy infobase on CT107 (mode = new)

Ask: "Развернуть базу на CT107?"

If yes:

Step 8.1 — Copy .dt file to CT107 (/mnt/data/data-24/ maps to /var/lib/onec/ inside container):

scp "<dt_file_path>" root@YOUR_EDT_SERVER:/mnt/data/data-<SERVER_SUFFIX>/<BASE_NAME>.dt


Step 8.2 — Ensure Xvfb is running in the target container (required for 1cv8 DESIGNER):

ssh root@YOUR_EDT_SERVER "docker exec onec-server-<SERVER_SUFFIX> pgrep Xvfb || docker exec -d onec-server-<SERVER_SUFFIX> Xvfb :99 -screen 0 1024x768x16"


deploy-infobase.sh uses DISPLAY=:99 but does NOT auto-start Xvfb. Without this step, deploy fails with "Unable to initialize GTK+".

Step 8.2b — Run deploy script on CT107:

ssh root@YOUR_EDT_SERVER "/opt/1c-dev/deploy-infobase.sh --name <BASE_NAME> --dt /mnt/data/data-<SERVER_SUFFIX>/<BASE_NAME>.dt --server <SERVER_SUFFIX> --admin-user <user> --admin-pwd <pwd>"


Script /opt/1c-dev/deploy-infobase.sh — universal script (supports 24/25/27):

--server 24|25|27 — selects container (onec-server-XX), ports, web container automatically
Auto-detects platform version (ls /opt/1cv8/x86_64/ inside container)
Auto-detects cluster ID via rac cluster list
DT path mapping: /mnt/data/data-<SERVER>/X.dt → /var/lib/onec/X.dt inside container

Does 4 steps automatically:

Check if infobase already exists (rac infobase summary list); if not — create via rac infobase create + PostgreSQL DB (--create-database). Fails with error if UUID can't be obtained.
1cv8 DESIGNER /RestoreIB — restores .dt. Verifies "успешно завершена" in log, exits on failure.
onec-webinst.sh publish — publishes web in onec-web-<SERVER_SUFFIX>
rac infobase update --license-distribution=allow

Script behaviour:

DB password read from /opt/1c-dev/secrets/pg_password (not hardcoded)
Lock file /tmp/deploy-<NAME>.lock prevents concurrent runs
Log written to /tmp/deploy-<NAME>-<timestamp>.log (timestamped, not overwritten)
set -euo pipefail — stops on any error

Known cluster IDs: 8.3.24=eecfed03-e569-4bc7-a729-b8518e4b6859, 8.3.27=0c2ac9c1-8017-4ac8-8b93-35f1409a3ecb. Result URL: http://YOUR_EDT_SERVER:<WEB_PORT>/<BASE_NAME>/

Step 8.3 — Verify infobase availability:

# 1. Infobase registered in cluster
ssh root@YOUR_EDT_SERVER "docker exec onec-server-24 /opt/1cv8/x86_64/<ONEC_VERSION>/rac localhost:1645 infobase summary --cluster=<CLUSTER_ID> | grep -i '<BASE_NAME>'"

# 2. Web publication responds
curl -s -o /dev/null -w "%{http_code}" "http://YOUR_EDT_SERVER:<WEB_PORT>/<BASE_NAME>/"
# Expected: 200 or 302

# 3. HTTP API available (if 1c-ai-debug configured)
curl -s "http://YOUR_EDT_SERVER:<WEB_PORT>/<BASE_NAME>/hs/ai/ping" -u "<user>:<pwd>"
# Expected: {"status":"ok"} or any 200 response


Only proceed to next steps if web check returns 200/302. If 503/404 — check deploy log on CT107: docker exec onec-server-24 cat /var/lib/onec/restore_<BASE_NAME>.log

8.3.1. Install AI_Debug extension (MANDATORY for all 1C projects)

AI_Debug extension provides: HTTP API for MCP (1c-ai-debug), unit test framework (ЮТТесты/ЮТУтверждения), and hosts all *_Test modules. Without it, 1c-ai-debug MCP and /1c-test-runner won't work.

Source: C:\Users\YOUR_USERNAME\workspace\ai\1c-ai-debug-extension\dist\AI_Debug.cfe (pre-built, kept in git).

# Load extension into database
powershell.exe -NoProfile -File .claude/skills/db-load-xml/scripts/db-load-xml.ps1 `
  -V8Path "C:\Program Files\1cv8\<V8_VERSION>\bin" `
  -InfoBaseServer "YOUR_EDT_SERVER:<PORT>" `
  -InfoBaseRef "<BASE_NAME>" `
  -UserName "<ADMIN_USER>" -Password "<ADMIN_PWD>" `
  -ConfigDir "C:\Users\YOUR_USERNAME\workspace\ai\1c-ai-debug-extension\src" `
  -Extension "AI_Debug" -Mode Full


Then update DB to apply extension:

powershell.exe -NoProfile -File .claude/skills/db-update/scripts/db-update.ps1 `
  -V8Path "C:\Program Files\1cv8\<V8_VERSION>\bin" `
  -InfoBaseServer "YOUR_EDT_SERVER:<PORT>" `
  -InfoBaseRef "<BASE_NAME>" `
  -UserName "<ADMIN_USER>" -Password "<ADMIN_PWD>"


Verify: curl -s "http://YOUR_EDT_SERVER:<WEB_PORT>/<BASE_NAME>/hs/ai/ping" -u "<user>:<pwd>" → {"status":"ok"}.

Test modules go HERE — never into the main project configuration. See "Test modules (*_Test)" rule in global CLAUDE.md.

8.3.2. Deploy codemetadata MCP (MANDATORY for all 1C projects)

Follow the codemetadata MCP — auto-deploy section in ~/.claude/1c-development-rules.md.

Summary:

Find XML config dump in project (src/cf/, src/src/, or src/cfe/)
Copy to CT104: ssh proxmox "pct exec 104 -- mkdir -p /mnt/onec-xml/<PROJECT>/src/cf ..."
Add service to C:\Users\YOUR_USERNAME\workspace\ai\1c-enhanced-codemetadata\docker-compose-ct104.yml with next free port (7530+)
Deploy: scp compose file → docker compose up -d <project>-codemetadata-enhanced
Update {{CODEMETADATA_URL}} in .mcp.json with actual port
Verify: curl -s "http://YOUR_MCP_SERVER:<PORT>/health"

Port registry (from 1c-development-rules.md): minimkg=7530, mcparqa24=7540, ai-debug=7550, kaf=7560, next=7570, ...

If source dump not yet available (step 8.4 hasn't run yet), defer codemetadata deploy to AFTER step 8.4 completes.

8.4. Export source from deployed database

Use /db-dump-xml skill — reads .v8-project.json automatically, runs local DESIGNER against remote server. Do NOT run DESIGNER manually inside the container — the skill works fine from the local machine with PROF license.

8.4.1 — Export main configuration (if project type = configuration or both):

powershell.exe -NoProfile -File .claude/skills/db-dump-xml/scripts/db-dump-xml.ps1 `
  -V8Path "C:\Program Files\1cv8\<V8_VERSION>\bin" `
  -InfoBaseServer "YOUR_EDT_SERVER:<PORT>" `
  -InfoBaseRef "<BASE_NAME>" `
  -UserName "<ADMIN_USER>" -Password "<ADMIN_PWD>" `
  -ConfigDir "src" -Mode Full


IMPORTANT: Always pass -V8Path matching the server platform version. The local default 1cv8.exe may be a newer version (e.g. 8.3.27), causing "version mismatch" error if server is 8.3.24 or 8.3.25.

Note: Full config dump can take several minutes (17k+ XML files is normal for ERP/BSP-based configs).

8.4.2 — Export extension(s) (if project type = extension or both):

For each extension name in EXTENSION_NAMES:

powershell.exe -NoProfile -File .claude/skills/db-dump-xml/scripts/db-dump-xml.ps1 `
  -InfoBaseServer "YOUR_EDT_SERVER:<PORT>" `
  -InfoBaseRef "<BASE_NAME>" `
  -UserName "<ADMIN_USER>" -Password "<ADMIN_PWD>" `
  -ConfigDir "ext/<EXTENSION_NAME>" -Extension "<EXTENSION_NAME>" -Mode Full


If project type = extension only — skip step 8.4.1, only export extension(s). If project type = configuration + extension — do both 8.4.1 and 8.4.2.

9. Initialize git repository
# 1. Create .gitignore
cat > .gitignore << 'EOF'
# 1C binaries (intermediate/working files)
*.dt

# Built artifacts in dist/ are tracked (for distribution)
# All other CF/CFE/EPF/ERF outside dist/ are ignored
*.cf
*.cfe
*.epf
*.erf
!dist/*.cf
!dist/*.cfe
!dist/*.epf
!dist/*.erf

# Credentials (contains passwords)
.v8-project.json

# Logs and temp
*.log
tmp/

# OS
.DS_Store
Thumbs.db
EOF

# 2. Create .gitattributes
cat > .gitattributes << 'EOF'
* text=auto eol=lf
src/**/*.xml text eol=lf
src/**/*.mdo text eol=lf
*.ps1 text eol=crlf
*.dt binary
*.cf binary
*.cfe binary
*.epf binary
*.erf binary
EOF

# 3. Init repo
git init
git config user.name "Arman"
git config user.email "arman@localhost"

# 4. Create Gitea repo via API
curl -s -X POST "http://YOUR_SERVER:3000/api/v1/user/repos" \
  -H "Authorization: token YOUR_GITEA_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"name\":\"<PROJECT_NAME>\",\"description\":\"<PROJECT_DESCRIPTION>\",\"private\":true}"

# 5. Add remote, commit, push
git remote add gitea http://admin:admin123@YOUR_SERVER:3000/admin/<PROJECT_NAME>.git

# Add dirs based on project type:
# configuration only:   git add .gitignore .gitattributes CLAUDE.md .mcp.json openspec/ .claude/ src/
# extension only:       git add .gitignore .gitattributes CLAUDE.md .mcp.json openspec/ .claude/ ext/ dist/
# configuration + ext:  git add .gitignore .gitattributes CLAUDE.md .mcp.json openspec/ .claude/ src/ ext/ dist/

git commit -m "Initial commit: project scaffold + source"
git push -u gitea master


Note: git push with 17k+ files takes time. Run in background if needed. Note: .v8-project.json is intentionally excluded (contains passwords) — keep it only locally.

10. Configure mcp-bsl-lsp on CT100

The mcp-lsp-<PROJECT_NAME> container was created by the init script but needs:

10.1 — Clone project to CT100 workspace:

ssh root@YOUR_SERVER "git clone http://admin:admin123@YOUR_SERVER:3000/admin/<PROJECT_NAME>.git /opt/workspace/<PROJECT_NAME>"


10.2 — Recreate container with correct WORKSPACE_ROOT:

If extension project: WORKSPACE_ROOT=/projects/<PROJECT_NAME>/ext/<EXTENSION_NAME>
If configuration only: WORKSPACE_ROOT=/projects/<PROJECT_NAME>/src
If both: WORKSPACE_ROOT=/projects/<PROJECT_NAME>/src (LSP indexes base config; ext files accessed via Grep)
ssh root@YOUR_SERVER "
docker stop mcp-lsp-<PROJECT_NAME> && docker rm mcp-lsp-<PROJECT_NAME> && \
docker run -d \
  --name mcp-lsp-<PROJECT_NAME> \
  --restart unless-stopped \
  -v /opt/workspace:/projects:rw \
  -e MCP_LSP_BSL_JAVA_XMX=4g \
  -e MCP_LSP_BSL_JAVA_XMS=1g \
  -e MCP_LSP_LOG_LEVEL=error \
  -e FILE_WATCHER_MODE=polling \
  -e FILE_WATCHER_INTERVAL=30s \
  -e HOST_PROJECTS_ROOT=/opt/workspace \
  -e PROJECTS_ROOT=/projects \
  -e WORKSPACE_ROOT=/projects/<PROJECT_NAME>/<DEV_PATH> \
  mcp-lsp-bridge-bsl:latest
"


10.3 — Set up auto-sync (git pull on CT100 every 5 min):

ssh root@YOUR_SERVER "(crontab -l 2>/dev/null; echo '*/5 * * * * cd /opt/workspace/<PROJECT_NAME> && git pull --quiet origin master 2>/dev/null') | crontab -"


Note: .mcp.json template uses /usr/bin/mcp-lsp-bridge (correct path in container).

11. Report

List what was created/updated. Remind user to configure:

v8path in .v8-project.json if auto-detect fails
Open project with claude in target directory (MCP servers load from .mcp.json)
Enrich mode specifics

Compare skill files by content hash — copy only if workspace version is newer or file missing in target. Always overwrite .claude/docs/ (platform specs don't change per-project). Never overwrite: CLAUDE.md, .mcp.json, .v8-project.json, openspec/.

Weekly Installs
11
Repository
arman-kudaiberg…ment-kit
GitHub Stars
122
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn