---
rating: ⭐⭐⭐
title: geo-prospect
url: https://skills.sh/zubair-trabzada/geo-seo-claude/geo-prospect
---

# geo-prospect

skills/zubair-trabzada/geo-seo-claude/geo-prospect
geo-prospect
Installation
$ npx skills add https://github.com/zubair-trabzada/geo-seo-claude --skill geo-prospect
SKILL.md
GEO Prospect Manager
Purpose

Manage GEO agency prospects and clients through the full sales lifecycle. All data is stored in ~/.geo-prospects/prospects.json (persistent across sessions).

Commands
Command	What It Does
/geo prospect new <domain>	Create new prospect (interactive prompts)
/geo prospect list	Show all prospects with pipeline status
/geo prospect list <status>	Filter: lead, qualified, proposal, won, lost
/geo prospect show <id-or-domain>	Full prospect detail with history
/geo prospect audit <id-or-domain>	Run quick GEO audit and save to prospect record
/geo prospect note <id-or-domain> "<text>"	Add interaction note with timestamp
/geo prospect status <id-or-domain> <new-status>	Move through pipeline
/geo prospect won <id-or-domain> <monthly-value>	Mark as won, set contract value
/geo prospect lost <id-or-domain> "<reason>"	Mark as lost with reason
/geo prospect pipeline	Visual pipeline summary with revenue forecast
Data Structure

Each prospect is stored as a JSON record:

{
  "id": "PRO-001",
  "company": "Electron Srl",
  "domain": "electron-srl.com",
  "contact_email": "info@electron-srl.com",
  "contact_name": "",
  "industry": "Educational Equipment Manufacturing",
  "country": "Italy",
  "status": "qualified",
  "geo_score": 32,
  "audit_date": "2026-03-12",
  "audit_file": "~/.geo-prospects/audits/electron-srl.com-2026-03-12.md",
  "proposal_file": "~/.geo-prospects/proposals/electron-srl.com-proposal.md",
  "monthly_value": 0,
  "contract_start": null,
  "contract_months": 0,
  "notes": [
    {
      "date": "2026-03-12",
      "text": "Initial GEO quick scan. Score 32/100 - Critical tier. Strong candidate for GEO services."
    }
  ],
  "created_at": "2026-03-12",
  "updated_at": "2026-03-12"
}

Orchestration Instructions
/geo prospect new <domain>
Check if ~/.geo-prospects/prospects.json exists, create if not (empty array)
Auto-detect company name from domain (e.g., electron-srl.com → Electron Srl)
Assign next sequential ID: PRO-001, PRO-002, etc.
Ask user for:
Contact name (optional)
Contact email
Monthly contract value estimate (optional)
Set status to lead
Save to JSON file
Suggest next step: "Run /geo prospect audit electron-srl.com to score this prospect"
/geo prospect list

Read ~/.geo-prospects/prospects.json and render a summary table:

GEO Prospect Pipeline — March 2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ID       Domain                  Company           Status      Score  Value
───────  ──────────────────────  ────────────────  ──────────  ─────  ──────
PRO-001  electron-srl.com        Electron Srl      Qualified   32/100  €4.5K
PRO-002  acme.com                ACME Corp         Lead        —       —
PRO-003  bigshop.it              BigShop           Won         41/100  €6.0K

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pipeline: 1 lead | 1 qualified | 0 proposals | 1 won | 0 lost
Committed MRR: €6,000 | Pipeline Value: €4,500

/geo prospect audit <id-or-domain>
Run /geo quick <domain> to get GEO snapshot score
Save score to prospect record: geo_score, audit_date
Save audit output to ~/.geo-prospects/audits/<domain>-<date>.md
Update audit_file path in prospect record
Add auto-note: "Quick audit run. GEO Score: XX/100."
If score < 55: suggest "Score indicates strong sales opportunity. Run /geo proposal <domain> to generate proposal."
/geo prospect note <id-or-domain> "<text>"
Find prospect by ID or domain
Append note with current ISO date
Save back to JSON
Confirm: "Note added to Electron Srl (PRO-001)"
/geo prospect status <id-or-domain> <status>

Valid statuses: lead, qualified, proposal, won, lost

Update status field
Add auto-note: "Status changed to "
Save and confirm
/geo prospect pipeline

Visual revenue-focused pipeline summary:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GEO AGENCY PIPELINE SUMMARY — March 2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STAGE          COUNT   POTENTIAL VALUE   NOTES
─────────────  ─────   ───────────────   ─────────────────────
Lead             2      €8,000/mo        New discoveries
Qualified        1      €4,500/mo        Ready for proposal
Proposal Sent    1      €6,000/mo        Awaiting signature
Won              3      €18,500/mo       Active clients (MRR)
Lost             1      —                Budget freeze

COMMITTED MRR:        €18,500
PIPELINE (qualified+): €10,500
TOTAL POTENTIAL:      €29,000/mo → €348,000/yr

Next actions:
→ PRO-003 (acme.com): Send proposal — score 38/100 (strong case)
→ PRO-007 (shop.it): Follow up — proposal sent 8 days ago
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Storage Location

All data stored in ~/.geo-prospects/:

~/.geo-prospects/
├── prospects.json          # Main CRM database
├── audits/                 # Quick audit snapshots
│   └── electron-srl.com-2026-03-12.md
└── proposals/              # Generated proposals
    └── electron-srl.com-proposal.md


Create directory if it does not exist: mkdir -p ~/.geo-prospects/audits ~/.geo-prospects/proposals

Pipeline Stage Definitions
Status	Meaning	Typical Next Action
lead	Discovered, not yet contacted	Run quick audit, assess opportunity
qualified	Audit done, confirmed pain points	Generate proposal
proposal	Proposal sent, awaiting decision	Follow up, answer questions
won	Contract signed, active client	Run full audit, start onboarding
lost	Deal closed lost	Log reason for future reference
Output
All commands print confirmation + current prospect status to terminal
No external files unless explicitly saving audits/proposals
JSON database is the single source of truth
Weekly Installs
164
Repository
zubair-trabzada…o-claude
GitHub Stars
7.0K
First Seen
Mar 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass