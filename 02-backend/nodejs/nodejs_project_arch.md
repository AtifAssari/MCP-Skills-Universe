---
rating: ⭐⭐
title: nodejs-project-arch
url: https://skills.sh/abczsl520/nodejs-project-arch/nodejs-project-arch
---

# nodejs-project-arch

skills/abczsl520/nodejs-project-arch/nodejs-project-arch
nodejs-project-arch
Installation
$ npx skills add https://github.com/abczsl520/nodejs-project-arch --skill nodejs-project-arch
SKILL.md
Node.js Project Architecture for AI-Friendly Development

Architecture standards that keep files small enough for AI agents to read/edit without blowing the context window.

Core Rules
Single file max 400 lines, index.html max 200 lines, server.js entry max 100 lines
All tunable values in config.json, loaded at runtime, editable via admin dashboard
Backend: routes/ by domain, services/ for shared logic, db.js for database
Frontend: HTML skeleton only, JS/CSS in separate files
Every project gets admin.html + routes/admin.js for config hot-reload
Project Type Selection

Determine project type, then read the corresponding reference:

Type	Signals	Reference
H5 Game	Canvas, Phaser, Matter.js, game loop, sprites	references/game.md
Data Tool	Crawler, scraper, scheduler, data sync, analytics	references/tool.md
Content/Utility	Generator, library, publisher, file processing	references/tool.md
Dashboard/Monitor	Charts, real-time, alerts, metrics	references/tool.md
API Service	REST endpoints, middleware, microservice	references/tool.md
SDK/Library	Shared module, build step, multi-consumer	references/sdk.md
Quick Start (All Types)
Identify project type from table above
Read the corresponding reference file
Create directory structure per the reference
Extract hardcoded values → config.json
Split large files by function (each <400 lines)
Add routes/admin.js + admin.html
Frontend: config.js fetches /api/config at startup, code reads GAME_CONFIG.xxx or APP_CONFIG.xxx
Test locally → backup → deploy
config.json Pattern (Universal)
// Server: load and serve config
const config = JSON.parse(fs.readFileSync('./config.json', 'utf8'));
app.get('/api/config', (req, res) => {
  const safe = { ...config };
  delete safe.admin; // strip secrets
  res.json(safe);
});

// Admin: hot-reload
app.post('/admin/config', requireAdmin, (req, res) => {
  fs.writeFileSync('./config.json.bak', fs.readFileSync('./config.json'));
  fs.writeFileSync('./config.json', JSON.stringify(req.body, null, 2));
  Object.assign(config, req.body);
  res.json({ ok: true });
});

Admin Dashboard Pattern (Universal)

admin.html auto-generates form from config structure:

Password login (x-admin-password header)
Visual config editor with save + hot-reload
Stats overview (users/data/uptime)
Config backup history + restore
Why This Matters

Large single files consume massive context tokens when AI reads them:

3000-line file → ~40K tokens per read (20% of 200K window)
200-line module → ~2.7K tokens per read (1.3% of window)
Result: 10-15 productive rounds vs 3-5 before context compression
Weekly Installs
17
Repository
abczsl520/nodej…ect-arch
GitHub Stars
20
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass