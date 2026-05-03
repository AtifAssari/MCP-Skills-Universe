---
rating: ⭐⭐
title: alicloud-platform-multicloud-docs-api-benchmark
url: https://skills.sh/cinience/alicloud-skills/alicloud-platform-multicloud-docs-api-benchmark
---

# alicloud-platform-multicloud-docs-api-benchmark

skills/cinience/alicloud-skills/alicloud-platform-multicloud-docs-api-benchmark
alicloud-platform-multicloud-docs-api-benchmark
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill alicloud-platform-multicloud-docs-api-benchmark
SKILL.md
Multi-Cloud Product Docs/API Benchmark

Use this skill when the user wants cross-cloud documentation/API comparison for similar products.

Supported clouds
Alibaba Cloud
AWS
Azure
GCP
Tencent Cloud
Volcano Engine
Huawei Cloud
Data source policy
L0 (highest): user-pinned official links via --<provider>-links
L1: machine-readable official metadata/source
GCP: Discovery API
AWS: API Models repository
Azure: REST API Specs repository
L2: official-domain constrained web discovery fallback
L3: insufficient discovery (low confidence)
Workflow

Run the benchmark script:

python skills/platform/docs/alicloud-platform-multicloud-docs-api-benchmark/scripts/benchmark_multicloud_docs_api.py --product "<product keyword>"


Example:

python skills/platform/docs/alicloud-platform-multicloud-docs-api-benchmark/scripts/benchmark_multicloud_docs_api.py --product "serverless"


LLM platform benchmark example (Bailian/Bedrock/Azure OpenAI/Vertex AI/Hunyuan/Ark/Pangu):

python skills/platform/docs/alicloud-platform-multicloud-docs-api-benchmark/scripts/benchmark_multicloud_docs_api.py --product "Bailian" --preset "llm-platform"


If --preset is omitted, script attempts to auto-match preset based on keyword.

Scoring weights can be switched by profile (see references/scoring.json):

python skills/platform/docs/alicloud-platform-multicloud-docs-api-benchmark/scripts/benchmark_multicloud_docs_api.py --product "Bailian" --preset "llm-platform" --scoring-profile "llm-platform"

Optional: pin authoritative links

Auto-discovery may miss pages. For stricter comparison, pass official links manually:

python skills/platform/docs/alicloud-platform-multicloud-docs-api-benchmark/scripts/benchmark_multicloud_docs_api.py \
  --product "object storage" \
  --aws-links "https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html" \
  --azure-links "https://learn.microsoft.com/azure/storage/blobs/"


Available manual flags:

--alicloud-links
--aws-links
--azure-links
--gcp-links
--tencent-links
--volcengine-links
--huawei-links

Each flag accepts comma-separated URLs.

Output policy

All artifacts must be written under:

output/alicloud-platform-multicloud-docs-api-benchmark/

Per run:

benchmark_evidence.json
benchmark_report.md
Reporting guidance

When answering the user:

Show score ranking across all providers.
Highlight top gaps (P0/P1/P2) and concrete fix actions.
If discovery confidence is low, ask user to provide pinned links and rerun.
Validation
mkdir -p output/alicloud-platform-multicloud-docs-api-benchmark
for f in skills/platform/docs/alicloud-platform-multicloud-docs-api-benchmark/scripts/*.py; do
  python3 -m py_compile "$f"
done
echo "py_compile_ok" > output/alicloud-platform-multicloud-docs-api-benchmark/validate.txt


Pass criteria: command exits 0 and output/alicloud-platform-multicloud-docs-api-benchmark/validate.txt is generated.

Output And Evidence
Save artifacts, command outputs, and API response summaries under output/alicloud-platform-multicloud-docs-api-benchmark/.
Include key parameters (region/resource id/time range) in evidence files for reproducibility.
Prerequisites
Configure least-privilege Alibaba Cloud credentials before execution.
Prefer environment variables: ALICLOUD_ACCESS_KEY_ID, ALICLOUD_ACCESS_KEY_SECRET, optional ALICLOUD_REGION_ID.
If region is unclear, ask the user before running mutating operations.
References
Rubric: references/review-rubric.md
Weekly Installs
260
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