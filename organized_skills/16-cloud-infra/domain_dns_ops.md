---
rating: ⭐⭐
title: domain-dns-ops
url: https://skills.sh/steipete/agent-scripts/domain-dns-ops
---

# domain-dns-ops

skills/steipete/agent-scripts/domain-dns-ops
domain-dns-ops
Installation
$ npx skills add https://github.com/steipete/agent-scripts --skill domain-dns-ops
SKILL.md
Domain/DNS Ops (Peter)

This skill is a thin router: use ~/Projects/manager as truth, run the repo scripts, follow the checklists.

Source of truth (read first)
~/Projects/manager/DOMAINS.md (domain -> target map; registrar hints; exclusions)
~/Projects/manager/DNS.md (Cloudflare onboarding + DNS/redirect checklist)
~/Projects/manager/redirect-worker.ts + ~/Projects/manager/redirect-worker-mapping.md (worker redirects)
Golden path (new vanity domain -> Cloudflare -> redirect)
Decide routing model
Page Rule redirect (small scale, per-zone).
Rulesets / Bulk Redirects (account-level; needs token perms).
Worker route (fallback; uses redirect-worker).
Cloudflare zone
Create zone (UI), then confirm with cli4:
cli4 --get name=example.com /zones
Nameservers
If registrar = Namecheap: cd ~/Projects/manager && source profile && bin/namecheap-set-ns example.com emma.ns.cloudflare.com scott.ns.cloudflare.com
If registrar = DNSimple: see ~/Projects/manager/DNS.md for delegation API notes.
DNS placeholders (so CF can terminate HTTPS)
Proxied apex A + wildcard A → 192.0.2.1 (see ~/Projects/manager/DNS.md for exact cli4 calls).
Redirect
If using Page Rules: use the cli4 --post ... /pagerules template from ~/Projects/manager/DNS.md.
If using Worker: update mapping (~/Projects/manager/redirect-worker-mapping.md), deploy/bind routes per ~/Projects/manager/DNS.md.
Verify
DNS: dig +short example.com @1.1.1.1 (expect CF anycast).
HTTPS redirect: curl -I https://example.com (expect 301).
Common ops
Cloudflare token sanity: source ~/.profile (prefer CLOUDFLARE_API_TOKEN; CF_API_TOKEN fallback).
Disable “Block AI bots”: cd ~/Projects/manager && source profile && bin/cloudflare-ai-bots status / bin/cloudflare-ai-bots disable.
After edits (commit/push)

If you changed anything in ~/Projects/manager (docs, worker, scripts, mappings): commit there too.

Review: cd ~/Projects/manager && git status && git diff
Stage: git add <paths>
Commit (Conventional Commits): git commit -m "feat: …" / fix: / docs: / chore:
Push only when explicitly asked: git push origin main
Guardrails
Don’t touch .md lore domains or steipete.md unless explicitly asked; check ~/Projects/manager/DOMAINS.md.
Confirm registrar before debugging CF “invalid nameservers” (often “wrong registrar”).
Prefer reversible steps; verify after each change (NS → DNS → redirect).
Weekly Installs
83
Repository
steipete/agent-scripts
GitHub Stars
2.5K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass