---
rating: ⭐⭐⭐
title: provenance
url: https://skills.sh/boshu2/agentops/provenance
---

# provenance

skills/boshu2/agentops/provenance
provenance
Installation
$ npx skills add https://github.com/boshu2/agentops --skill provenance
SKILL.md
Provenance Skill

Trace knowledge artifact lineage to sources.

Execution Steps

Given /provenance <artifact>:

Step 1: Read the Artifact
Tool: Read
Parameters:
  file_path: <artifact-path>


Look for provenance metadata:

Source references
Session IDs
Dates
Related artifacts
Step 2: Trace Source Chain
# Check for source metadata in the file
grep -i "source\|session\|from\|extracted" <artifact-path>

# Search for related transcripts using ao
ao search "<artifact-name>" 2>/dev/null

Step 3: Search Session Transcripts with CASS

Use CASS to find when this artifact was discussed:

# Extract artifact name for search
artifact_name=$(basename "<artifact-path>" .md)

# Search session transcripts
cass search "$artifact_name" --json --limit 5


Parse CASS results to find:

Sessions where artifact was created/discussed
Timeline of references
Related sessions by workspace

CASS JSON output fields:

{
  "hits": [{
    "title": "...",
    "source_path": "/path/to/session.jsonl",
    "created_at": 1766076237333,
    "score": 18.5,
    "agent": "claude_code"
  }]
}

Step 4: Build Lineage Chain
Transcript (source of truth)
    ↓
Forge extraction (candidate)
    ↓
Human review (promotion)
    ↓
Pattern recognition (tier-up)
    ↓
Skill creation (automation)

Step 5: Write Provenance Report
# Provenance: <artifact-name>

## Current State
- **Tier:** <0-3>
- **Created:** <date>
- **Citations:** <count>

## Source Chain
1. **Origin:** <transcript or session>
   - Line/context: <where extracted>
   - Extracted: <date>

2. **Promoted:** <tier change>
   - Reason: <why promoted>
   - Date: <when>

## Session References (from CASS)
| Date | Session | Agent | Score |
|------|---------|-------|-------|
| <date> | <session-id> | <agent> | <score> |

## Related Artifacts
- <related artifact 1>
- <related artifact 2>

Step 6: Report to User

Tell the user:

Artifact lineage
Original source
Promotion history
Session references (from CASS)
Related artifacts
Finding Orphans
/provenance --orphans


Find artifacts without source tracking:

# Files without "Source:" or "Session:" metadata
for f in .agents/learnings/*.md; do
  grep -L "Source\|Session" "$f" 2>/dev/null
done

Finding Stale Artifacts
/provenance --stale


Find artifacts where source may have changed:

# Artifacts older than their sources
find .agents/ -name "*.md" -mtime +30 2>/dev/null

Key Rules
Every insight has a source - trace it
Track promotions - know why tier changed
Find orphans - clean up untracked knowledge
Maintain lineage - provenance enables trust
Use CASS - find when artifacts were discussed
Examples
Trace Artifact Lineage

User says: /provenance .agents/learnings/2026-01-15-auth-tokens.md

What happens:

Agent reads artifact and extracts source metadata (session ID, date, references)
Agent searches session transcripts with cass search "auth-tokens" --json --limit 5
Agent parses CASS results to find origin session and timeline
Agent traces promotion history from forge → learnings → patterns
Agent builds lineage chain and writes report to markdown
Agent reports artifact tier, citations, related artifacts

Result: Full provenance chain from transcript to current tier, showing when artifact was created, discussed, and promoted.

Find Orphaned Artifacts

User says: /provenance --orphans

What happens:

Agent scans .agents/learnings/, .agents/patterns/ for files missing source metadata
Agent greps each file for "Source:" or "Session:" fields
Agent lists files without provenance tracking
Agent reports orphan count and recommends adding source references

Result: Untracked knowledge identified, enabling retroactive lineage documentation or archival.

Troubleshooting
Problem	Cause	Solution
No source metadata found	Artifact created before provenance tracking	Use CASS to find origin session retroactively; add Source field manually
CASS returns no results	Session not indexed or artifact name mismatch	Check session transcript exists; try broader search terms
Stale artifact check fails	find command not available or permission error	Use `ls -lt .agents/
Lineage chain incomplete	Promotion not recorded in artifact metadata	Reconstruct from git history or session transcripts; document gaps
Weekly Installs
435
Repository
boshu2/agentops
GitHub Stars
323
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass