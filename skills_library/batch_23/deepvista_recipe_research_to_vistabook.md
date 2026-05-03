---
title: deepvista-recipe-research-to-vistabook
url: https://skills.sh/deepvista-ai/deepvista-cli/deepvista-recipe-research-to-vistabook
---

# deepvista-recipe-research-to-vistabook

skills/deepvista-ai/deepvista-cli/deepvista-recipe-research-to-vistabook
deepvista-recipe-research-to-vistabook
Installation
$ npx skills add https://github.com/deepvista-ai/deepvista-cli --skill deepvista-recipe-research-to-vistabook
SKILL.md
Research to VistaBook

PREREQUISITE: Load the following skills: deepvista-vistabase, deepvista-vistabook

Search your knowledge base for relevant context, then run a VistaBook workflow with that context.

Steps

Search for relevant cards:

deepvista --profile local vistabase +search "your research topic" --limit 10


Read the most relevant cards (pick IDs from search results):

deepvista --profile local vistabase get <card_id_1>
deepvista --profile local vistabase get <card_id_2>


Summarize findings into a context string for the VistaBook.

List available VistaBooks to find the right workflow:

deepvista --profile local vistabook list


Run the VistaBook with your research context:

deepvista --profile local vistabook +run <vistabook_id> --input "Based on my research: <summary of findings>"


Check run status:

deepvista --profile local vistabook +status <run_chat_id>

Tips
This recipe combines read operations (search, get) with a write operation (run).
Confirm with the user before step 5 (the write step).
The VistaBook run will have access to the full knowledge base, so the context input is for focusing the run, not the only information available.
Weekly Installs
22
Repository
deepvista-ai/de…ista-cli
GitHub Stars
5
First Seen
Mar 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass