---
title: lovstudio:xbti-gallery
url: https://skills.sh/lovstudio/skills/lovstudio:xbti-gallery
---

# lovstudio:xbti-gallery

skills/lovstudio/skills/lovstudio:xbti-gallery
lovstudio:xbti-gallery
Installation
$ npx skills add https://github.com/lovstudio/skills --skill lovstudio:xbti-gallery
SKILL.md
xbti-gallery — Browse Community BTI Tests

Open the XBTI Gallery and list all community-created BTI personality tests.

When to Use
User wants to browse existing BTI personality tests
User says "打开 XBTI Gallery" or "show me BTI cases"
User wants to see what others have created before making their own
Workflow
Step 1: Open Gallery
open https://xbti.lovstudio.ai

Step 2: List Available Cases

Fetch and display all BTI variants from the repository:

gh api repos/lovstudio/XBTI/contents/cases 2>/dev/null | python3 -c "
import json, sys
try:
    items = json.load(sys.stdin)
    if isinstance(items, list):
        for item in items:
            if item.get('type') == 'dir':
                print(f'  - {item[\"name\"]}')
    else:
        print('  (no cases yet)')
except:
    print('  (unable to fetch)')
"


If no cases exist, tell the user: "Gallery 还没有案例，用 /lovstudio-xbti-creator 创建一个并提交吧！"

Weekly Installs
28
Repository
lovstudio/skills
GitHub Stars
46
First Seen
Apr 10, 2026