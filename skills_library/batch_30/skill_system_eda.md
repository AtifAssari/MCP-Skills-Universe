---
title: skill-system-eda
url: https://skills.sh/arthur0824hao/skills/skill-system-eda
---

# skill-system-eda

skills/arthur0824hao/skills/skill-system-eda
skill-system-eda
Installation
$ npx skills add https://github.com/arthur0824hao/skills --skill skill-system-eda
SKILL.md
Skill System EDA

Use scripts/eda.py for deterministic EDA artifacts. The current stable backend is tabular EDA, and the multimodal entrypoint is explore.

Core Commands
python3 scripts/eda.py detect-modality --input data_root
python3 scripts/eda.py explore --input data_or_folder
python3 scripts/eda.py detect-modality --input data_root
python3 scripts/eda.py explore --input data_or_folder --modality graph
python3 scripts/eda.py graph-viz --input data.csv --features amount,score --id-column account_id --label Class --edge-mode knn --topk 50 --normalize l2 --similarity cosine --output /tmp/eda_graph
python3 scripts/eda.py profile-dataset --input data.csv --target Class --output /tmp/eda
python3 scripts/eda.py distribution-report --input data.csv --target Class --profile /tmp/eda/profile.yaml
python3 scripts/eda.py correlation-matrix --input data.csv --target Class --profile /tmp/eda/profile.yaml
python3 scripts/eda.py anomaly-profiling --input data.csv --target Class --profile /tmp/eda/profile.yaml
python3 scripts/eda.py feature-importance-scan --input data.csv --target Class --profile /tmp/eda/profile.yaml
python3 scripts/eda.py leakage-detector --input data.csv --target Class --profile /tmp/eda/profile.yaml
python3 scripts/eda.py save-contract --profile /tmp/eda/profile.yaml --output /tmp/eda/contract.yaml
python3 scripts/eda.py validate-contract --input new_data.csv --contract /tmp/eda/contract.yaml

Output Model
profile-dataset creates profile.yaml and report.md
explore reports detected modalities and selected backend; tabular mode may immediately route into existing tabular profiling
graph-viz emits graph_viz/index.html, graph_viz/graph.json, graph_viz/sliders.json, and appends graph-viz references into profile.yaml and report.md
graph-viz records renderer_hint, preview_applied, and browser-edge limits so large-graph fallback is explicit rather than silent
later commands update profile.yaml and append sections to report.md
save-contract emits contract.yaml
validate-contract prints JSON PASS / FAIL with a violation list
Analysis Rules
Use Polars (not pandas) for data IO/aggregation/profiling flows.
Keep sampling deterministic with lazy .head(N) when --sample is used.
Treat profile.yaml as the machine-readable source of truth; report.md is the human-readable companion.
Graph visualization artifacts must stay reusable: no Esun-specific paths, feature names, or binary fraud-only assumptions in the skill contract.
Large graph behavior is first-class: when full edge count exceeds browser-safe thresholds, the viewer loads preview edges by default and reports the full edge count separately.
Use Polars + numpy + scipy for profiling, shifts, correlations, KS tests, and Cramer's V.
Use sklearn feature ranking only when available; otherwise keep tree-based importance explicitly skipped.
Use lazy scan strategy for large CSV/parquet inputs (scan_csv/scan_parquet), with materialization delayed until needed.
Apply high-cardinality guards: >50 unique skips one-hot in feature importance, and profile truncates categorical columns (>100 unique or >50% row cardinality) to top-20 values.
Memory Integration
By default, commands write a summary memory plus one memory per warning/critical finding.
Prefer skill-system-memory/scripts/mem.py store when available.
If memory writes fail or EDA_DISABLE_MEM_PY=1 is set, write fallback payloads under .memory/pending/.
Use --no-memory for deterministic tests or when no writeback is desired.
Contract Lifecycle
save-contract derives column requirements from profile.yaml.
Numeric ranges use observed bounds for tiny datasets and profile-derived percentile bounds for larger datasets.
Truncated categorical columns produce cardinality_range rules instead of allowed_values.
validate-contract fails closed and returns machine-readable violations.
Graph Viz Notes
graph-viz is a tabular-to-graph visualization flow, not a replacement for graph-native modality EDA.
graph.json is the viewer payload authority; sliders.json is the UI-control authority.
renderer_hint=canvas means the full interactive force layout is expected to be browser-safe.
renderer_hint=webgl means dataset scale or edge volume exceeded the canvas-friendly threshold; the shipped viewer still loads, but preview edges are preferred by default.
--max-browser-edges controls when preview fallback is applied. Raising it may crash Chromium on very large graphs.

Example: Esun-style feature-bank payload generalized into EDA input/output conventions:

python3 scripts/eda.py graph-viz \
  --input Work/Study/GNN/FraudDetect/esun_data/combined_features.csv \
  --features senior28_01,senior28_02,senior28_03,senior28_04 \
  --id-column account_id \
  --label is_fraud \
  --edge-mode knn \
  --topk 50 \
  --normalize l2 \
  --similarity cosine \
  --max-browser-edges 60000 \
  --output /tmp/esun_graph_viz


Example: generic customer risk dataset with a multi-class label column:

python3 scripts/eda.py graph-viz \
  --input data/customer_risk.parquet \
  --features amount,velocity_score,merchant_entropy,geo_distance \
  --id-column customer_id \
  --label segment \
  --edge-mode knn \
  --topk 25 \
  --normalize l2 \
  --similarity cosine \
  --output /tmp/customer_graph_viz

{
  "schema_version": "2.0",
  "id": "skill-system-eda",
  "version": "1.1.0",
  "capabilities": [
    "eda-detect",
    "eda-graph-viz",
    "eda-profile",
    "eda-distribution",
    "eda-correlation",
    "eda-anomaly",
    "eda-feature-importance",
    "eda-leakage",
    "eda-contract-save",
    "eda-contract-validate"
  ],
  "effects": ["fs.read", "fs.write", "proc.exec"],
  "operations": {
    "profile-dataset": {
      "description": "Profile a CSV/parquet dataset and generate profile.yaml plus report.md.",
      "input": {
        "input": { "type": "string", "required": true },
        "target": { "type": "string", "required": false },
        "output": { "type": "string", "required": true },
        "sample": { "type": "integer", "required": false },
        "no_memory": { "type": "boolean", "required": false }
      },
      "output": {
        "description": "Artifact paths for the generated EDA profile",
        "fields": { "profile": "string", "report": "string" }
      },
      "entrypoints": {
        "unix": ["python3", "scripts/eda.py", "profile-dataset", "--input", "{input}", "--output", "{output}"]
      }
    },
    "detect-modality": {
      "description": "Detect dataset modality and return all matching modality tags.",
      "input": {
        "input": { "type": "string", "required": true }
      },
      "output": {
        "description": "Detected modalities",
        "fields": { "modalities": "array", "path": "string" }
      },
      "entrypoints": {
        "unix": ["python3", "scripts/eda.py", "detect-modality", "--input", "{input}"]
      }
    },
    "explore-dataset": {
      "description": "Detect dataset modality and route to the appropriate EDA backend.",
      "input": {
        "input": { "type": "string", "required": true },
        "modality": { "type": "string", "required": false },
        "output": { "type": "string", "required": false }
      },
      "output": {
        "description": "Detected modalities, selected modality, and backend routing result",
        "fields": { "detected_modalities": "array", "selected_modality": "string", "status": "string" }
      },
      "entrypoints": {
        "unix": ["python3", "scripts/eda.py", "explore", "--input", "{input}"]
      }
    },
    "graph-viz": {
      "description": "Build reusable graph visualization artifacts for tabular or graph datasets.",
      "input": {
        "input": { "type": "string", "required": true },
        "features": { "type": "string", "required": false },
        "id_column": { "type": "string", "required": false },
        "label": { "type": "string", "required": false },
        "edge_mode": { "type": "string", "required": false },
        "edge_input": { "type": "string", "required": false },
        "topk": { "type": "integer", "required": false },
        "normalize": { "type": "string", "required": false },
        "similarity": { "type": "string", "required": false },
        "sample": { "type": "integer", "required": false },
        "output": { "type": "string", "required": true }
      },
      "output": {
        "description": "Graph visualization artifact paths and integration outputs",
        "fields": { "html": "string", "graph_json": "string", "slider_config": "string", "renderer_hint": "string", "profile": "string", "report": "string" }
      },
      "entrypoints": {
        "unix": ["python3", "scripts/eda.py", "graph-viz", "--input", "{input}", "--output", "{output}"]
      }
    },
    "distribution-report": {
      "description": "Append distribution and class-conditional analysis to an existing profile/report.",
      "input": {
        "input": { "type": "string", "required": true },
        "target": { "type": "string", "required": true },
        "profile": { "type": "string", "required": true }
      },
      "output": { "description": "Updated profile/report paths", "fields": { "profile": "string", "report": "string" } },
      "entrypoints": {
        "unix": ["python3", "scripts/eda.py", "distribution-report", "--input", "{input}", "--target", "{target}", "--profile", "{profile}"]
      }
    },
    "correlation-matrix": {
      "description": "Compute feature and target correlations and append them to profile/report.",
      "input": {
        "input": { "type": "string", "required": true },
        "target": { "type": "string", "required": false },
        "profile": { "type": "string", "required": true }
      },
      "output": { "description": "Updated profile/report paths", "fields": { "profile": "string", "report": "string" } },
      "entrypoints": {
        "unix": ["python3", "scripts/eda.py", "correlation-matrix", "--input", "{input}", "--profile", "{profile}"]
      }
    },
    "anomaly-profiling": {
      "description": "Compare class-conditional distributions and effect sizes.",
      "input": {
        "input": { "type": "string", "required": true },
        "target": { "type": "string", "required": true },
        "profile": { "type": "string", "required": true }
      },
      "output": { "description": "Updated profile/report paths", "fields": { "profile": "string", "report": "string" } },
      "entrypoints": {
        "unix": ["python3", "scripts/eda.py", "anomaly-profiling", "--input", "{input}", "--target", "{target}", "--profile", "{profile}"]
      }
    },
    "feature-importance-scan": {
      "description": "Rank features with mutual information and optional tree importances.",
      "input": {
        "input": { "type": "string", "required": true },
        "target": { "type": "string", "required": true },
        "profile": { "type": "string", "required": true }
      },
      "output": { "description": "Updated profile/report paths", "fields": { "profile": "string", "report": "string" } },
      "entrypoints": {
        "unix": ["python3", "scripts/eda.py", "feature-importance-scan", "--input", "{input}", "--target", "{target}", "--profile", "{profile}"]
      }
    },
    "leakage-detector": {
      "description": "Detect high-correlation, target-encoding, and temporal leakage indicators.",
      "input": {
        "input": { "type": "string", "required": true },
        "target": { "type": "string", "required": true },
        "profile": { "type": "string", "required": true }
      },
      "output": { "description": "Updated profile/report paths", "fields": { "profile": "string", "report": "string" } },
      "entrypoints": {
        "unix": ["python3", "scripts/eda.py", "leakage-detector", "--input", "{input}", "--target", "{target}", "--profile", "{profile}"]
      }
    },
    "save-contract": {
      "description": "Generate a data contract from a saved EDA profile.",
      "input": {
        "profile": { "type": "string", "required": true },
        "output": { "type": "string", "required": true }
      },
      "output": { "description": "Contract path", "fields": { "contract": "string" } },
      "entrypoints": {
        "unix": ["python3", "scripts/eda.py", "save-contract", "--profile", "{profile}", "--output", "{output}"]
      }
    },
    "validate-contract": {
      "description": "Validate a new dataset against a saved contract and emit PASS/FAIL JSON.",
      "input": {
        "input": { "type": "string", "required": true },
        "contract": { "type": "string", "required": true }
      },
      "output": { "description": "Validation status and violations", "fields": { "status": "string", "violations": "array" } },
      "entrypoints": {
        "unix": ["python3", "scripts/eda.py", "validate-contract", "--input", "{input}", "--contract", "{contract}"]
      }
    }
  },
  "stdout_contract": {
    "last_line_json": true
  }
}

Weekly Installs
20
Repository
arthur0824hao/skills
GitHub Stars
4
First Seen
Mar 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass