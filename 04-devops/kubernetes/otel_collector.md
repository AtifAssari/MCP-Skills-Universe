---
title: otel-collector
url: https://skills.sh/dash0hq/agent-skills/otel-collector
---

# otel-collector

skills/dash0hq/agent-skills/otel-collector
otel-collector
Installation
$ npx skills add https://github.com/dash0hq/agent-skills --skill otel-collector
SKILL.md
OpenTelemetry Collector configuration guide

Expert guidance for configuring and deploying the OpenTelemetry Collector to receive, process, and export telemetry.

Rules
Rule	Description
receivers	Receivers — OTLP, Prometheus, filelog, hostmetrics
exporters	Exporters — OTLP/gRPC to Dash0, debug, authentication
processors	Processors — memory limiter, resource detection, ordering, sending queue
pipelines	Pipelines — service section, per-signal configuration, connectors
deployment	Deployment — agent vs gateway patterns, deployment method selection
dash0-operator	Dash0 Kubernetes Operator — automated instrumentation, Collector management, Dash0 export
collector-helm-chart	Collector Helm chart — presets, modes, image selection
opentelemetry-operator	OpenTelemetry Operator — Collector CRD, auto-instrumentation, sidecar
raw-manifests	Raw Kubernetes manifests — DaemonSet, Deployment, RBAC, Docker Compose
sampling	Sampling — head, tail, load balancing
red-metrics	RED metrics — span-derived request rate, error rate, duration histograms
custom-distributions	Custom distributions — building a stripped-down Collector binary with OCB
Key principles
Processor ordering matters. Place memory_limiter first in every pipeline. Use the exporter's sending_queue with file_storage instead of the batch processor. Incorrect ordering causes memory exhaustion or data loss.
One pipeline per signal type. Define separate pipelines for traces, metrics, and logs. Mixing signals in a single pipeline breaks processing and causes runtime errors.
Every declared component must appear in a pipeline. The Collector rejects configurations that declare receivers, processors, or exporters not referenced by any pipeline.
Consistent resource enrichment across pipelines. Apply processors that enrich resource attributes like resourcedetection and k8sattributes to every signal pipeline (traces, metrics, and logs), not just one. If one pipeline enriches telemetry with k8s.namespace.name or host.name but another does not, correlation between signals is compromised by incomplete metadata.
Memory safety is non-negotiable. Always configure memory_limiter in production. Without it, a burst of telemetry can cause the Collector to OOM and crash.
Quick start

Minimal working configuration: OTLP receiver → memory limiter → OTLP/gRPC exporter to Dash0.

receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

processors:
  memory_limiter:
    check_interval: 1s
    limit_mib: 400
    spike_limit_mib: 100

exporters:
  otlp:
    endpoint: ingress.eu-west-1.aws.dash0.com:4317
    headers:
      Authorization: "Bearer ${env:DASH0_TOKEN}"
    sending_queue:
      enabled: true
      storage: file_storage

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [memory_limiter]
      exporters: [otlp]
    metrics:
      receivers: [otlp]
      processors: [memory_limiter]
      exporters: [otlp]
    logs:
      receivers: [otlp]
      processors: [memory_limiter]
      exporters: [otlp]


See exporters for full authentication and queue configuration, and processors for adding resource detection.

Configuration workflow
Write config — define receivers, processors, and exporters; wire them in service.pipelines.
Validate locally — run otelcol validate --config=config.yaml to catch structural errors before deployment.
Deploy — choose a deployment method from the deployment rule (Helm, Operator, raw manifests, or Docker Compose).
Verify — add the debug exporter to a pipeline temporarily and inspect stdout to confirm telemetry is flowing; then remove it before going to production.
Quick reference
What do you need?	Rule
Accept OTLP telemetry from applications	receivers
Scrape Prometheus endpoints	receivers
Collect log files or host metrics	receivers
Send telemetry to Dash0	exporters
Configure retry, queue, or compression	exporters
Set processor ordering	processors
Add Kubernetes or cloud metadata	processors
Wire receivers → processors → exporters	pipelines
Complete working configuration	pipelines
Validate the pipeline with the debug exporter	collector-helm-chart, opentelemetry-operator, raw-manifests, or dash0-operator
Deploy as DaemonSet or Deployment	raw-manifests
Deploy with Helm	collector-helm-chart
Deploy with the OTel Operator	opentelemetry-operator
Deploy with the Dash0 Operator	dash0-operator
Auto-instrument applications in Kubernetes	opentelemetry-operator or dash0-operator
Local development with Docker Compose	raw-manifests
Reduce trace volume	sampling
Keep errors and slow traces, drop the rest	sampling
Redact sensitive data in the pipeline	processors
Generate RED metrics from traces	red-metrics
Build a custom Collector binary	custom-distributions
Official documentation
OpenTelemetry Collector documentation
Collector configuration
Collector contrib components
Dash0 Integration Hub
Weekly Installs
170
Repository
dash0hq/agent-skills
GitHub Stars
50
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass