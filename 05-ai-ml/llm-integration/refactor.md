---
title: refactor
url: https://skills.sh/zpankz/mcp-skillset/refactor
---

# refactor

skills/zpankz/mcp-skillset/refactor
refactor
Installation
$ npx skills add https://github.com/zpankz/mcp-skillset --skill refactor
SKILL.md
Refactor Skill
Trigger Patterns
"/refactor"
"refactor the architecture"
"optimize my claude code setup"
"evaluate all components"
"run architecture audit"
"check for redundancies"
"optimize token usage"
Applicable Specialized Agents
refactor-agent (primary orchestrator)
component-architect-agent (validation)
knowledge-domain-agent (learning integration)
Infrastructure Dependencies
Tool	Purpose	Health Check
bv/bd	Graph orchestration	bd --version
tweakcc	System prompt editing	ls ~/.tweakcc/
claude-mem	Context optimization	curl localhost:37777/health
hookify	Validation hooks	hookify --version
Optimization Frameworks
Homoiconic Renormalization - Self-referential optimization
BFO/GFO Ontology - Formal type definitions
Hegelian Dialectics - Thesis-antithesis-synthesis
Pareto Optimization - Multi-objective efficiency
24-Hour Auto-Trigger
<!-- ~/.claude/launchd/com.claude.refactor.plist -->
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.claude.refactor</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>-c</string>
        <string>claude -p "/refactor --auto"</string>
    </array>
    <key>StartInterval</key>
    <integer>86400</integer>
</dict>
</plist>

Weekly Installs
9
Repository
zpankz/mcp-skillset
GitHub Stars
2
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn