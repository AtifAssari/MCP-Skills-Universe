---
rating: ⭐⭐
title: redteam
url: https://skills.sh/danielmiessler/personal_ai_infrastructure/redteam
---

# redteam

skills/danielmiessler/personal_ai_infrastructure/RedTeam
RedTeam
Installation
$ npx skills add https://github.com/danielmiessler/personal_ai_infrastructure --skill RedTeam
SKILL.md
Customization

Before executing, check for user customizations at: ~/.claude/PAI/USER/SKILLCUSTOMIZATIONS/RedTeam/

If this directory exists, load and apply any PREFERENCES.md, configurations, or resources found there. These override default behavior. If the directory does not exist, proceed with skill defaults.

🚨 MANDATORY: Voice Notification (REQUIRED BEFORE ANY ACTION)

You MUST send this notification BEFORE doing anything else when this skill is invoked.

Send voice notification:

curl -s -X POST http://localhost:8888/notify \
  -H "Content-Type: application/json" \
  -d '{"message": "Running the WORKFLOWNAME workflow in the RedTeam skill to ACTION"}' \
  > /dev/null 2>&1 &


Output text notification:

Running the **WorkflowName** workflow in the **RedTeam** skill to ACTION...


This is not optional. Execute this curl command immediately upon skill invocation.

RedTeam Skill

Military-grade adversarial analysis using parallel agent deployment. Breaks arguments into atomic components, attacks from 32 expert perspectives (engineers, architects, pentesters, interns), synthesizes findings, and produces devastating counter-arguments with steelman representations.

Workflow Routing

Route to the appropriate workflow based on the request.

When executing a workflow, output this notification directly:

Running the **WorkflowName** workflow in the **RedTeam** skill to ACTION...

Trigger	Workflow
Red team analysis (stress-test existing content)	Workflows/ParallelAnalysis.md
Adversarial validation (produce new content via competition)	Workflows/AdversarialValidation.md
Quick Reference
Workflow	Purpose	Output
ParallelAnalysis	Stress-test existing content	Steelman + Counter-argument (8-points each)
AdversarialValidation	Produce new content via competition	Synthesized solution from competing proposals

The Five-Phase Protocol (ParallelAnalysis):

Decomposition - Break into 24 atomic claims
Parallel Analysis - 32 agents examine strengths AND weaknesses
Synthesis - Identify convergent insights
Steelman - Strongest version of the argument
Counter-Argument - Strongest rebuttal
Context Files
Philosophy.md - Core philosophy, success criteria, agent types
Integration.md - Skill integration, FirstPrinciples usage, output format
Examples

Attack an architecture proposal:

User: "red team this microservices migration plan"
--> Workflows/ParallelAnalysis.md
--> Returns steelman + devastating counter-argument (8 points each)


Devil's advocate on a business decision:

User: "poke holes in my plan to raise prices 20%"
--> Workflows/ParallelAnalysis.md
--> Surfaces the ONE core issue that could collapse the plan


Adversarial validation for content:

User: "battle of bots - which approach is better for this feature?"
--> Workflows/AdversarialValidation.md
--> Synthesizes best solution from competing ideas


Last Updated: 2025-12-20

Weekly Installs
105
Repository
danielmiessler/…tructure
GitHub Stars
11.9K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass