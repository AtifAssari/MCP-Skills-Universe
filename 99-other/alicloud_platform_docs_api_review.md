---
rating: ⭐⭐
title: alicloud-platform-docs-api-review
url: https://skills.sh/cinience/alicloud-skills/alicloud-platform-docs-api-review
---

# alicloud-platform-docs-api-review

skills/cinience/alicloud-skills/alicloud-platform-docs-api-review
alicloud-platform-docs-api-review
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill alicloud-platform-docs-api-review
SKILL.md
Alibaba Cloud Product Docs + API Docs Reviewer

Use this skill when the user gives a product name and asks for an end-to-end documentation/API quality review.

What this skill does
Resolve product from latest OpenAPI metadata.
Fetch latest API docs for default version.
Discover product/help-doc links from official product page.
Produce a structured review report with:
score
evidence
prioritized suggestions (P0/P1/P2)
Workflow

Run the bundled script:

python skills/platform/docs/alicloud-platform-docs-api-review/scripts/review_product_docs_and_api.py --product "<product name or product code>"


Example:

python skills/platform/docs/alicloud-platform-docs-api-review/scripts/review_product_docs_and_api.py --product "ECS"

Output policy

All generated artifacts must be written under:

output/alicloud-platform-docs-api-review/

For each run, the script creates:

review_evidence.json
review_report.md
Reporting guidance

When answering the user:

State resolved product + version first.
Summarize the score and the top 3 issues.
List P0/P1/P2 recommendations with concrete actions.
Provide source links used in the report.
Validation
mkdir -p output/alicloud-platform-docs-api-review
for f in skills/platform/docs/alicloud-platform-docs-api-review/scripts/*.py; do
  python3 -m py_compile "$f"
done
echo "py_compile_ok" > output/alicloud-platform-docs-api-review/validate.txt


Pass criteria: command exits 0 and output/alicloud-platform-docs-api-review/validate.txt is generated.

Output And Evidence
Save artifacts, command outputs, and API response summaries under output/alicloud-platform-docs-api-review/.
Include key parameters (region/resource id/time range) in evidence files for reproducibility.
Prerequisites
Configure least-privilege Alibaba Cloud credentials before execution.
Prefer environment variables: ALICLOUD_ACCESS_KEY_ID, ALICLOUD_ACCESS_KEY_SECRET, optional ALICLOUD_REGION_ID.
If region is unclear, ask the user before running mutating operations.
References
Review rubric: references/review-rubric.md
Weekly Installs
266
Repository
cinience/alicloud-skills
GitHub Stars
383
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass