---
title: elasticsearch-file-ingest
url: https://skills.sh/elastic/agent-skills/elasticsearch-file-ingest
---

# elasticsearch-file-ingest

skills/elastic/agent-skills/elasticsearch-file-ingest
elasticsearch-file-ingest
Installation
$ npx skills add https://github.com/elastic/agent-skills --skill elasticsearch-file-ingest
SKILL.md
Elasticsearch File Ingest

Stream-based ingestion and transformation of large data files (NDJSON, CSV, Parquet, Arrow IPC) into Elasticsearch.

Features & Use Cases
Stream-based: Handle large files without running out of memory
High throughput: 50k+ documents/second on commodity hardware
Formats: NDJSON, CSV, Parquet, Arrow IPC
Transformations: Apply custom JavaScript transforms during ingestion (enrich, split, filter)
Batch processing: Ingest multiple files matching a pattern (e.g., logs/*.json)
Document splitting: Transform one source document into multiple targets
Prerequisites
Elasticsearch 8.x or 9.x accessible (local or remote)
Node.js 22+ installed
Setup

This skill is self-contained. The scripts/ folder and package.json live in this skill's directory. Run all commands from this directory. Use absolute paths when referencing data files located elsewhere.

Before first use, install dependencies:

npm install

Environment Configuration

Elasticsearch connection is configured by users exclusively via environment variables. Never pass credentials as command-line arguments. If the test fails, output the setup options below to the user, then stop. Do not proceed with ingestion until a successful connection test.

Option 1: Elastic Cloud (recommended for production)
export ELASTICSEARCH_CLOUD_ID="<your-cloud-id>"
export ELASTICSEARCH_API_KEY="<your-api-key>"

Option 2: Direct URL with API Key
export ELASTICSEARCH_URL="https://elasticsearch:9200"
export ELASTICSEARCH_API_KEY="<your-api-key>"

Option 3: Basic Authentication
export ELASTICSEARCH_URL="https://elasticsearch:9200"
export ELASTICSEARCH_USERNAME="<your-username>"
export ELASTICSEARCH_PASSWORD="<your-password>"

Option 4: Local Development

For local development and testing, see Run Elasticsearch locally to spin up Elasticsearch and Kibana. After setup, export the connection variables (URL and API key or credentials) as shown in Option 2 or Option 3 above.

Optional: Skip TLS verification (development only)
export ELASTICSEARCH_INSECURE="true"

Test Connection

Verify the Elasticsearch connection before ingesting data:

node scripts/ingest.js test


Always run this first. If the test fails, resolve the connection issue before proceeding.

Examples
Ingest a JSON file
node scripts/ingest.js ingest --file /absolute/path/to/data.json --target my-index

Stream NDJSON/CSV via stdin
# NDJSON
cat /absolute/path/to/data.ndjson | node scripts/ingest.js ingest --stdin --target my-index

# CSV
cat /absolute/path/to/data.csv | node scripts/ingest.js ingest --stdin --source-format csv --target my-index

Ingest CSV directly
node scripts/ingest.js ingest --file /absolute/path/to/users.csv --source-format csv --target users

Ingest Parquet directly
node scripts/ingest.js ingest --file /absolute/path/to/users.parquet --source-format parquet --target users

Ingest Arrow IPC directly
node scripts/ingest.js ingest --file /absolute/path/to/users.arrow --source-format arrow --target users

Ingest CSV with parser options
# csv-options.json
# {
#   "columns": true,
#   "delimiter": ";",
#   "trim": true
# }

node scripts/ingest.js ingest --file /absolute/path/to/users.csv --source-format csv --csv-options csv-options.json --target users

Infer mappings/pipeline from CSV

When using --infer-mappings, do not combine it with --source-format csv. Inference sends a raw sample to Elasticsearch's _text_structure/find_structure endpoint, which returns both mappings and an ingest pipeline with a CSV processor. If --source-format csv is also set, CSV is parsed client-side and server-side, resulting in an empty index. Let --infer-mappings handle everything:

node scripts/ingest.js ingest --file /absolute/path/to/users.csv --infer-mappings --target users

Infer mappings with options
# infer-options.json
# {
#   "sampleBytes": 200000,
#   "lines_to_sample": 2000
# }

node scripts/ingest.js ingest --file /absolute/path/to/users.csv --infer-mappings --infer-mappings-options infer-options.json --target users

Ingest with custom mappings
node scripts/ingest.js ingest --file /absolute/path/to/data.json --target my-index --mappings mappings.json

Ingest with transformation
node scripts/ingest.js ingest --file /absolute/path/to/data.json --target my-index --transform transform.js

Command Reference
Required Options
--target <index>         # Target index name

Source Options (choose one)
--file <path>            # Source file (supports wildcards, e.g., logs/*.json)
--stdin                  # Read NDJSON/CSV from stdin

Index Configuration
--mappings <file.json>          # Mappings file
--infer-mappings                # Infer mappings/pipeline from file/stream (do NOT combine with --source-format)
--infer-mappings-options <file> # Options for inference (JSON file)
--delete-index                  # Delete target index if exists
--pipeline <name>               # Ingest pipeline name

Processing
--transform <file.js>    # Transform function (export as default or module.exports)
--source-format <fmt>    # Source format: ndjson|csv|parquet|arrow (default: ndjson)
--csv-options <file>     # CSV parser options (JSON file)
--skip-header            # Skip first line (e.g., CSV header)

Performance
--buffer-size <kb>       # Buffer size in KB (default: 5120)
--total-docs <n>         # Total docs for progress bar (file/stream)
--stall-warn-seconds <n> # Stall warning threshold (default: 30)
--progress-mode <mode>   # Progress output: auto|line|newline (default: auto)
--debug-events           # Log pause/resume/stall events
--quiet                  # Disable progress bars

Transform Functions

Transform functions let you modify documents during ingestion. Create a JavaScript file that exports a transform function:

Basic Transform (transform.js)
// ES modules (default)
export default function transform(doc) {
  return {
    ...doc,
    full_name: `${doc.first_name} ${doc.last_name}`,
    timestamp: new Date().toISOString(),
  };
}

// Or CommonJS
module.exports = function transform(doc) {
  return {
    ...doc,
    full_name: `${doc.first_name} ${doc.last_name}`,
  };
};

Skip Documents

Return null or undefined to skip a document:

export default function transform(doc) {
  // Skip invalid documents
  if (!doc.email || !doc.email.includes("@")) {
    return null;
  }
  return doc;
}

Split Documents

Return an array to create multiple target documents from one source:

export default function transform(doc) {
  // Split a tweet into multiple hashtag documents
  const hashtags = doc.text.match(/#\w+/g) || [];
  return hashtags.map((tag) => ({
    hashtag: tag,
    tweet_id: doc.id,
    created_at: doc.created_at,
  }));
}

Mappings
Custom Mappings (mappings.json)
{
  "properties": {
    "@timestamp": { "type": "date" },
    "message": { "type": "text" },
    "user": {
      "properties": {
        "name": { "type": "keyword" },
        "email": { "type": "keyword" }
      }
    }
  }
}

node scripts/ingest.js ingest --file /absolute/path/to/data.json --target my-index --mappings mappings.json

Boundaries
Never echo, print, log, or otherwise reveal the values of credential environment variables ($ELASTICSEARCH_API_KEY, $ELASTICSEARCH_PASSWORD, $ELASTICSEARCH_CLOUD_ID, etc.). Do not run shell commands whose output would expose secret values (e.g., echo $ELASTICSEARCH_API_KEY, env | grep KEY, printenv). Exporting these variables and running scripts that read them internally is expected and safe — the restriction is on surfacing secret values in command output. The only way to verify connectivity is node scripts/ingest.js test. If the test fails, ask the user to check their environment configuration — do not attempt to diagnose credentials yourself.
Never run destructive commands (such as using the --delete-index flag or deleting existing indices and data) without explicit user confirmation.
Guidelines
Test first: Always run node scripts/ingest.js test before ingesting data. If the connection fails, ask the user to verify their environment configuration and re-test. Do not attempt ingestion until the test passes.
Never combine --infer-mappings with --source-format. Inference creates a server-side ingest pipeline that handles parsing (e.g., CSV processor). Using --source-format csv parses client-side as well, causing double-parsing and an empty index. Use --infer-mappings alone for automatic detection, or --source-format with explicit --mappings for manual control.
Use --source-format csv with --mappings when you want client-side CSV parsing with known field types.
Use --infer-mappings alone when you want Elasticsearch to detect the format, infer field types, and create an ingest pipeline automatically.
When NOT to Use

Consider alternatives for:

Reindexing or index migration: Use the elasticsearch-reindex skill for copying, migrating, or transforming existing Elasticsearch indices
Real-time ingestion: Use Filebeat or Elastic Agent
Enterprise pipelines: Use Logstash
Built-in transforms: Use Elasticsearch Transforms
Additional Resources
Common Patterns - Detailed examples for CSV loading, batch ingestion, enrichment, and more
Troubleshooting - Solutions for common issues
References
Elasticsearch Mappings
Elasticsearch Query DSL
Weekly Installs
485
Repository
elastic/agent-skills
GitHub Stars
451
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass