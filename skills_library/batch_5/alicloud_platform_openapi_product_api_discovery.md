---
title: alicloud-platform-openapi-product-api-discovery
url: https://skills.sh/cinience/alicloud-skills/alicloud-platform-openapi-product-api-discovery
---

# alicloud-platform-openapi-product-api-discovery

skills/cinience/alicloud-skills/alicloud-platform-openapi-product-api-discovery
alicloud-platform-openapi-product-api-discovery
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill alicloud-platform-openapi-product-api-discovery
SKILL.md
Alibaba Cloud Product + API Discovery

Follow this workflow to collect products, resolve API metadata, and build summaries for skill planning.

Workflow
Fetch product lists from the three sources
Ticket System (ListProducts)
Support & Service (ListProductByGroup)
BSS OpenAPI (QueryProductList)

Run the bundled scripts (from this skill folder):

python scripts/products_from_ticket_system.py
python scripts/products_from_support_service.py
python scripts/products_from_bssopenapi.py


Provide required env vars in each script (see references).

Merge product lists
python scripts/merge_product_sources.py


This writes output/product-scan/merged_products.json and .md.

Fetch OpenAPI metadata product list
python scripts/products_from_openapi_meta.py


This writes output/product-scan/openapi-meta/products.json and products_normalized.json.

Fetch OpenAPI API docs per product/version
python scripts/apis_from_openapi_meta.py


By default this can be large. Use filters for dry runs:

OPENAPI_META_MAX_PRODUCTS=10
OPENAPI_META_PRODUCTS=Ecs,Ons
OPENAPI_META_VERSIONS=2014-05-26
Join products with API counts
python scripts/join_products_with_api_meta.py

Summarize products by category/group
python scripts/summarize_openapi_meta_products.py

(Optional) Compare products vs existing skills
python scripts/analyze_products_vs_skills.py

Output discipline

All generated files must go under output/. Do not place temporary files elsewhere.

Validation
mkdir -p output/alicloud-platform-openapi-product-api-discovery
for f in skills/platform/openapi/alicloud-platform-openapi-product-api-discovery/scripts/*.py; do
  python3 -m py_compile "$f"
done
echo "py_compile_ok" > output/alicloud-platform-openapi-product-api-discovery/validate.txt


Pass criteria: command exits 0 and output/alicloud-platform-openapi-product-api-discovery/validate.txt is generated.

Output And Evidence
Save artifacts, command outputs, and API response summaries under output/alicloud-platform-openapi-product-api-discovery/.
Include key parameters (region/resource id/time range) in evidence files for reproducibility.
Prerequisites
Configure least-privilege Alibaba Cloud credentials before execution.
Prefer environment variables: ALICLOUD_ACCESS_KEY_ID, ALICLOUD_ACCESS_KEY_SECRET, optional ALICLOUD_REGION_ID.
If region is unclear, ask the user before running mutating operations.
References
Product source APIs: see references/product-sources.md
OpenAPI meta endpoints: see references/openapi-meta.md
Weekly Installs
275
Repository
cinience/alicloud-skills
GitHub Stars
383
First Seen
Feb 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn