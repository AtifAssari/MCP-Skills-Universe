---
title: policy-lookup
url: https://skills.sh/anthropics/knowledge-work-plugins/policy-lookup
---

# policy-lookup

skills/anthropics/knowledge-work-plugins/policy-lookup
policy-lookup
Installation
$ npx skills add https://github.com/anthropics/knowledge-work-plugins --skill policy-lookup
SKILL.md
/policy-lookup

If you see unfamiliar placeholders or need to check which tools are connected, see CONNECTORS.md.

Look up and explain company policies in plain language. Answer employee questions about policies, benefits, and procedures by searching connected knowledge bases or using provided handbook content.

Usage
/policy-lookup $ARGUMENTS


Search for policies matching: $ARGUMENTS

How It Works
┌─────────────────────────────────────────────────────────────────┐
│                    POLICY LOOKUP                                   │
├─────────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                       │
│  ✓ Ask any policy question in plain language                    │
│  ✓ Paste your employee handbook and I'll search it              │
│  ✓ Get clear, jargon-free answers                               │
├─────────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                      │
│  + Knowledge base: Search handbook and policy docs automatically │
│  + HRIS: Pull employee-specific details (PTO balance, benefits) │
└─────────────────────────────────────────────────────────────────┘

Common Policy Topics
PTO and Leave: Vacation, sick leave, parental leave, bereavement, sabbatical
Benefits: Health insurance, dental, vision, 401k, HSA/FSA, wellness
Compensation: Pay schedule, bonus timing, equity vesting, expense reimbursement
Remote Work: WFH policy, remote locations, equipment stipend, coworking
Travel: Booking policy, per diem, expense reporting, approval process
Conduct: Code of conduct, harassment policy, conflicts of interest
Growth: Professional development budget, conference policy, tuition reimbursement
How to Answer
Search ~~knowledge base for the relevant policy document
Provide a clear, plain-language answer
Quote the specific policy language
Note any exceptions or special cases
Point to who to contact for edge cases

Important guardrails:

Always cite the source document and section
If no policy is found, say so clearly rather than guessing
For legal or compliance questions, recommend consulting HR or legal directly
Output
## Policy: [Topic]

### Quick Answer
[1-2 sentence direct answer to their question]

### Details
[Relevant policy details, explained in plain language]

### Exceptions / Special Cases
[Any relevant exceptions or edge cases]

### Who to Contact
[Person or team for questions beyond what's documented]

### Source
[Where this information came from — document name, page, or section]

If Connectors Available

If ~~knowledge base is connected:

Search employee handbook and policy documents automatically
Cite the specific document, section, and page number

If ~~HRIS is connected:

Pull employee-specific details like PTO balance, benefits elections, and enrollment status
Tips
Ask in plain language — "Can I work from Europe for a month?" is better than "international remote work policy."
Be specific — "PTO for part-time employees in California" gets a better answer than "PTO policy."
Weekly Installs
844
Repository
anthropics/know…-plugins
GitHub Stars
11.7K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass