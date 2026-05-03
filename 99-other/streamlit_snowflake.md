---
rating: ⭐⭐⭐
title: streamlit-snowflake
url: https://skills.sh/jezweb/claude-skills/streamlit-snowflake
---

# streamlit-snowflake

skills/jezweb/claude-skills/streamlit-snowflake
streamlit-snowflake
Installation
$ npx skills add https://github.com/jezweb/claude-skills --skill streamlit-snowflake
Summary

Build and deploy Streamlit apps natively in Snowflake with Snowpark integration and Marketplace publishing.

Supports two runtime options: Warehouse Runtime (personal instances, Anaconda packages) and Container Runtime (shared instances, PyPI packages, significantly lower cost)
Includes Snowpark session integration for native data access, multi-page app structure, and caller's rights connections (v1.53.0+) for per-user data isolation
Prevents 14 documented errors including package channel misconfigurations, authentication failures, caching bugs with parametrized queries, and performance issues with wide DataFrames
Covers deployment via Snowflake CLI, CI/CD workflows, and Native App publishing to Snowflake Marketplace
SKILL.md
Streamlit in Snowflake Skill

Build and deploy Streamlit apps natively within Snowflake, including Marketplace publishing as Native Apps.

Quick Start
1. Initialize Project

Copy the templates to your project:

# Create project directory
mkdir my-streamlit-app && cd my-streamlit-app

# Copy templates (Claude will provide these)

2. Configure snowflake.yml

Update placeholders in snowflake.yml:

definition_version: 2
entities:
  my_app:
    type: streamlit
    identifier: my_streamlit_app        # ← Your app name
    stage: my_app_stage                 # ← Your stage name
    query_warehouse: my_warehouse       # ← Your warehouse
    main_file: streamlit_app.py
    pages_dir: pages/
    artifacts:
      - common/
      - environment.yml

3. Deploy
# Deploy to Snowflake
snow streamlit deploy --replace

# Open in browser
snow streamlit deploy --replace --open

When to Use This Skill

Use when:

Building data apps that run natively in Snowflake
Need Snowpark integration for data access
Publishing apps to Snowflake Marketplace
Setting up CI/CD for Streamlit in Snowflake

Don't use when:

Hosting Streamlit externally (use Streamlit Community Cloud)
Building general Snowpark pipelines (use a Snowpark-specific skill)
Need custom Streamlit components (not supported in SiS)
Runtime Environments

Snowflake offers two runtime options for Streamlit apps:

Warehouse Runtime (Default)
Creates a personal instance for each viewer
Uses environment.yml with Snowflake Anaconda Channel
Python 3.9, 3.10, or 3.11
Streamlit 1.22.0 - 1.35.0
Best for: Sporadic usage, isolated sessions
Container Runtime (Preview)
Creates a shared instance for all viewers
Uses requirements.txt or pyproject.toml with PyPI packages
Python 3.11 only
Streamlit 1.49+
Significantly lower cost (~$2.88/day vs ~$48/day for equivalent compute)
Best for: Frequent usage, cost optimization

Container Runtime Configuration:

CREATE STREAMLIT my_app
  FROM '@my_stage/app_folder'
  MAIN_FILE = 'streamlit_app.py'
  RUNTIME_NAME = 'SYSTEM$ST_CONTAINER_RUNTIME_PY3_11'
  COMPUTE_POOL = my_compute_pool
  QUERY_WAREHOUSE = my_warehouse;


Key difference: Container runtime allows external PyPI packages - not limited to Snowflake Anaconda Channel.

See: Runtime Environments

Security Model

Streamlit apps support two privilege models:

Owner's Rights (Default)
Apps execute with the owner's privileges, not the viewer's
Apps use the warehouse provisioned by the owner
Viewers can interact with data using all owner role privileges

Security implications:

Exercise caution when granting write privileges to app roles
Use dedicated roles for app creation/viewing
Viewers can access any data the owner role can access
Best for: Internal tools with trusted users
Caller's Rights (v1.53.0+)
Apps execute with the viewer's privileges
Each viewer sees only data they have permission to access
Provides data isolation in multi-tenant scenarios

Use caller's rights when:

Building public or external-facing apps
Need per-user data access control
Multi-tenant applications requiring data isolation

See Caller's Rights Connection pattern below.

Project Structure
my-streamlit-app/
├── snowflake.yml           # Project definition (required)
├── environment.yml         # Package dependencies (required)
├── streamlit_app.py        # Main entry point
├── pages/                  # Multi-page apps
│   └── data_explorer.py
├── common/                 # Shared utilities
│   └── utils.py
└── .gitignore

Key Patterns
Snowpark Session Connection
import streamlit as st

# Get Snowpark session (native SiS connection)
conn = st.connection("snowflake")
session = conn.session()

# Query data
df = session.sql("SELECT * FROM my_table LIMIT 100").to_pandas()
st.dataframe(df)

Caller's Rights Connection (v1.53.0+)

Execute queries with viewer's privileges instead of owner's privileges:

import streamlit as st

# Use caller's rights for data isolation
conn = st.connection("snowflake", type="callers_rights")

# Each viewer sees only data they have permission to access
df = conn.query("SELECT * FROM sensitive_customer_data")
st.dataframe(df)


Security comparison:

Connection Type	Privilege Model	Use Case
type="snowflake" (default)	Owner's rights	Internal tools, trusted users
type="callers_rights" (v1.53.0+)	Caller's rights	Public apps, data isolation

Source: Streamlit v1.53.0 Release

Caching Expensive Queries
@st.cache_data(ttl=600)  # Cache for 10 minutes
def load_data(query: str):
    conn = st.connection("snowflake")
    return conn.session().sql(query).to_pandas()

# Use cached function
df = load_data("SELECT * FROM large_table")


Warning: In Streamlit v1.22.0-1.53.0, params argument is not included in cache key. Use ttl=0 to disable caching when using parametrized queries, or upgrade to 1.54.0+ when available (Issue #13644).

Optimizing Snowpark DataFrame Performance

When using Snowpark DataFrames with charts or tables, select only required columns to avoid fetching unnecessary data:

# ❌ Fetches all 50 columns even though chart only needs 2
df = session.table("wide_table")  # 50 columns
st.line_chart(df, x="date", y="value")

# ✅ Fetch only needed columns for better performance
df = session.table("wide_table").select("date", "value")
st.line_chart(df, x="date", y="value")
# 5-10x faster for wide tables


Why it matters: st.dataframe() and chart components call df.to_pandas() which evaluates ALL columns, even if the visualization only needs some. Pre-selecting columns reduces data transfer and improves performance (Issue #11701).

Environment Configuration

environment.yml (required format):

name: sf_env
channels:
  - snowflake          # REQUIRED - only supported channel
dependencies:
  - streamlit=1.35.0   # Explicit version (default is old 1.22.0)
  - pandas
  - plotly
  - altair=4.0         # Version 4.0 supported in SiS
  - snowflake-snowpark-python

Error Prevention

This skill prevents 14 documented errors:

Error	Cause	Prevention
PackageNotFoundError	Using conda-forge or external channel	Use channels: - snowflake (or Container Runtime for PyPI)
Missing Streamlit features	Default version 1.22.0	Explicitly set streamlit=1.35.0 (or use Container Runtime for 1.49+)
ROOT_LOCATION deprecated	Old CLI syntax	Use Snowflake CLI 3.14.0+ with FROM source_location
Auth failures (2026+)	Password-only authentication	Use key-pair or OAuth (see references/authentication.md)
File upload fails	File >200MB	Keep uploads under 200MB limit
DataFrame display fails	Data >32MB	Paginate or limit data before display
page_title not supported	SiS limitation	Don't use page_title, page_icon, or menu_items in st.set_page_config()
Custom component error	SiS limitation	Only components without external service calls work
_snowflake module not found	Container Runtime migration	Use from snowflake.snowpark.context import get_active_session instead of from _snowflake import get_active_session (Migration Guide)
Cached query returns wrong data with different params	params not in cache key (v1.22.0-1.53.0)	Use ttl=0 to disable caching for parametrized queries, or upgrade to 1.54.0+ when available (Issue #13644)
Invalid connection_name 'default' with kwargs only	Missing secrets.toml or connections.toml	Create minimal .streamlit/secrets.toml with [connections.snowflake] section (Issue #9016)
Native App upgrades unexpectedly	Implicit default Streamlit version (BCR-1857)	Explicitly set streamlit=1.35.0 in environment.yml to prevent automatic version changes (BCR-1857)
File paths fail in Container Runtime subdirectories	Some commands use entrypoint-relative paths	Use pathlib to resolve absolute paths: Path(__file__).parent / "assets/logo.png" (Runtime Docs)
Slow performance with wide Snowpark DataFrames	st.dataframe() fetches all columns even if unused	Pre-select only needed columns: df.select("col1", "col2") before passing to Streamlit (Issue #11701)
Deployment Commands
Basic Deployment
# Deploy and replace existing
snow streamlit deploy --replace

# Deploy and open in browser
snow streamlit deploy --replace --open

# Deploy specific entity (if multiple in snowflake.yml)
snow streamlit deploy my_app --replace

CI/CD Deployment

See references/ci-cd.md for GitHub Actions workflow template.

Marketplace Publishing (Native App)

To publish your Streamlit app to Snowflake Marketplace:

Convert to Native App - Use templates-native-app/ templates
Create Provider Profile - Required for Marketplace listings
Submit for Approval - Snowflake reviews before publishing

See templates-native-app/README.md for complete workflow.

Native App Structure
my-native-app/
├── manifest.yml            # Native App manifest
├── setup.sql               # Installation script
├── streamlit/
│   ├── environment.yml
│   ├── streamlit_app.py
│   └── pages/
└── README.md

Package Availability

Only packages from the Snowflake Anaconda Channel are available:

-- Query available packages
SELECT * FROM information_schema.packages
WHERE language = 'python'
ORDER BY package_name;

-- Search for specific package
SELECT * FROM information_schema.packages
WHERE language = 'python'
AND package_name ILIKE '%plotly%';


Common available packages:

pandas, numpy, scipy
plotly, altair (4.0), matplotlib
scikit-learn, xgboost
snowflake-snowpark-python
streamlit (1.22.0 default, 1.35.0 with explicit version)

Not available:

Packages from conda-forge
Custom/private packages
Packages requiring native compilation

See: Snowpark Python Packages Explorer

Known Limitations
Data & Size Limits
32 MB message size between backend/frontend (affects large st.dataframe)
200 MB file upload limit via st.file_uploader
No .so files - Native compiled libraries unsupported
No external stages - Internal stages only (client-side encryption)
UI Restrictions
st.set_page_config - page_title, page_icon, menu_items not supported
st.bokeh_chart - Not supported
Custom Streamlit components - Only components without external service calls
Content Security Policy - Blocks external scripts, styles, fonts, iframes
eval() blocked - CSP prevents unsafe JavaScript execution
Caching (Warehouse Runtime)
Session-scoped only - st.cache_data and st.cache_resource don't persist across users
Container runtime has full caching support across viewers
Package Restrictions (Warehouse Runtime)
Snowflake Anaconda Channel only - No conda-forge, no pip
Container runtime allows PyPI packages
Network & Access
No Azure Private Link / GCP Private Service Connect
No replication of Streamlit objects
Authentication (Important - 2026 Deadline)

Password-only authentication is being deprecated:

Milestone	Date	Requirement
Milestone 1	Sept 2025 - Jan 2026	MFA required for Snowsight users
Milestone 2	May - July 2026	All new users must use MFA
Milestone 3	Aug - Oct 2026	All users must use MFA or key-pair/OAuth

Recommended authentication methods:

Key-pair authentication (for service accounts)
OAuth client credentials (for M2M)
Workload Identity Federation (for cloud-native apps)

See references/authentication.md for implementation patterns.

Resources
Official Documentation
Streamlit in Snowflake
Snowflake CLI Streamlit Commands
Native Apps with Streamlit
Marketplace Publishing
Examples
snowflake-demo-streamlit
native-apps-templates
GitLab's Streamlit Framework
Tools
Snowpark Python Packages Explorer
Snowflake MCP Server (for Claude integration)
Weekly Installs
324
Repository
jezweb/claude-skills
GitHub Stars
759
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass