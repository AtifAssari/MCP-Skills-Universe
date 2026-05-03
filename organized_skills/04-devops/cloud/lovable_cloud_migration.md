---
rating: ⭐⭐
title: lovable-cloud-migration
url: https://skills.sh/carolmonroe22/lovable-cloud-migration/lovable-cloud-migration
---

# lovable-cloud-migration

skills/carolmonroe22/lovable-cloud-migration/lovable-cloud-migration
lovable-cloud-migration
Installation
$ npx skills add https://github.com/carolmonroe22/lovable-cloud-migration --skill lovable-cloud-migration
SKILL.md
Lovable Cloud to Own Supabase Migration
Key Facts
Lovable Cloud cannot be disconnected once enabled
No direct SQL or dashboard access to Cloud database
Workaround: new Lovable project + import repo + connect own Supabase
Auth passwords cannot be exported — users must reset after migration
Storage files must be migrated manually (download + re-upload)
Decision Tree

Want to keep Lovable as IDE?

New blank Lovable project → import GitHub repo → connect own Supabase
See "Disconnect Workaround" in migration-steps.md

Want to switch IDE (Cursor/Claude Code)?

GitHub export → clone locally → connect own Supabase via MCP
See "Full Migration" in migration-steps.md

Need data export first?

See export-methods.md

Having issues during migration?

See troubleshooting.md
Migration Workflow (Summary)
Enable GitHub integration in Lovable (if not already)
Export data using methods in export-methods.md
Create new Supabase project (free tier works)
Import schema + data into new project
Update environment variables
Migrate Storage files manually
Notify users to reset passwords
Lovable Cloud Limitations (Why Migrate)
Limitation	Detail
No SQL access	Only via Lovable chat or support@lovable.dev (3-5 days)
No custom auth	Only Google and Email
No email templates	Sent from no-reply@auth.lovable.cloud
No disconnect	Once enabled, permanent
No monitoring	No real-time metrics
No mobile schemes	Only https://, rejects com.app://
No staging/prod	Requires two projects
No direct dashboard	Can't login to Supabase dashboard
Resources by Carol Monroe
Export guide: https://carolmonroe.com/blog/export-lovable-cloud-claude-code
Disconnect guide: https://carolmonroe.com/blog/disconnect-lovable-cloud
Video tutorial: https://youtu.be/jEBVpl1GBvQ
Weekly Installs
20
Repository
carolmonroe22/l…igration
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass