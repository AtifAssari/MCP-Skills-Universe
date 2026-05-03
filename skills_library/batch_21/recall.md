---
title: recall
url: https://skills.sh/artemxtech/personal-os-skills/recall
---

# recall

skills/artemxtech/personal-os-skills/recall
recall
Installation
$ npx skills add https://github.com/artemxtech/personal-os-skills --skill recall
SKILL.md
Recall Skill

Three modes: temporal (date-based session timeline), topic (BM25 search across QMD collections), and graph (interactive visualization of session-file relationships). Every recall ends with the One Thing - a concrete, highest-leverage next action synthesized from the results.

What It Does
Temporal queries ("yesterday", "last week", "what was I doing"): Scans native Claude Code JSONL files by date. Shows a table of sessions with time, message count, and first message. Expand any session for conversation details.
Topic queries ("QMD video", "authentication"): BM25 search across sessions, notes, and daily logs in QMD collections.
Graph queries ("graph yesterday", "graph last week"): Generates an interactive HTML graph showing sessions as nodes connected to files they touched. Sessions colored by day, files colored by folder. Clusters reveal related work streams, shared files show cross-session dependencies.
One Thing synthesis: After presenting results, synthesizes the single most impactful next action based on what has momentum, what's blocked, and what's closest to done. Not generic - specific and actionable.

No custom setup needed for temporal recall - every Claude Code user has JSONL files.

Auto-Indexing (Optional)

You can auto-index sessions into QMD on every session end via a Claude Code hook. See AGENTS.md for setup instructions.

Usage
/recall yesterday
/recall last week
/recall 2026-02-25
/recall QMD video
/recall authentication work


Graph mode - visualize session relationships over time:

/recall graph yesterday        # what you touched today
/recall graph last week        # week overview - find clusters
/recall graph this week        # current week so far
/recall graph last 3 days      # recent activity window


Graph options: --min-files 5 for cleaner graphs (only sessions touching 5+ files), --all-projects to scan beyond current vault.

Workflow

See workflows/recall.md for routing logic and step-by-step process.

Weekly Installs
12
Repository
artemxtech/pers…s-skills
GitHub Stars
448
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn