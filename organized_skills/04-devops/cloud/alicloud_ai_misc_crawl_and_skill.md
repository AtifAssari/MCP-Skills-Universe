---
rating: ⭐⭐
title: alicloud-ai-misc-crawl-and-skill
url: https://skills.sh/cinience/alicloud-skills/alicloud-ai-misc-crawl-and-skill
---

# alicloud-ai-misc-crawl-and-skill

skills/cinience/alicloud-skills/alicloud-ai-misc-crawl-and-skill
alicloud-ai-misc-crawl-and-skill
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill alicloud-ai-misc-crawl-and-skill
SKILL.md

Category: task

Alibaba Cloud Model Studio Crawl and Skill Generation
Prerequisites
Node.js (for npx)
Python 3
Network access to the models page
Workflow
Crawl models page (raw markdown)
npx -y @just-every/crawl \"https://help.aliyun.com/zh/model-studio/models\" > alicloud-model-studio-models.md

Rebuild summary (models + API/usage links)
python3 skills/ai/misc/alicloud-ai-misc-crawl-and-skill/scripts/refresh_models_summary.py

Regenerate skills (creates/updates skills/ai/**)
python3 skills/ai/misc/alicloud-ai-misc-crawl-and-skill/scripts/refresh_alicloud_skills.py

Outputs
alicloud-model-studio-models.md: raw crawl output
output/alicloud-model-studio-models-summary.md: cleaned summary
output/alicloud-model-studio-models.json: structured model list
output/alicloud-model-studio-skill-scan.md: skill coverage report
skills/ai/**: generated skills
Notes
Do not invent model IDs or API endpoints; only use links present on the models page.
After regeneration, update README.md, README.en.md, and README.zh-TW.md if skills list changed.
Validation
mkdir -p output/alicloud-ai-misc-crawl-and-skill
for f in skills/ai/misc/alicloud-ai-misc-crawl-and-skill/scripts/*.py; do
  python3 -m py_compile "$f"
done
echo "py_compile_ok" > output/alicloud-ai-misc-crawl-and-skill/validate.txt


Pass criteria: command exits 0 and output/alicloud-ai-misc-crawl-and-skill/validate.txt is generated.

Output And Evidence
Save artifacts, command outputs, and API response summaries under output/alicloud-ai-misc-crawl-and-skill/.
Include key parameters (region/resource id/time range) in evidence files for reproducibility.
References
Source list: references/sources.md
Weekly Installs
267
Repository
cinience/alicloud-skills
GitHub Stars
383
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn