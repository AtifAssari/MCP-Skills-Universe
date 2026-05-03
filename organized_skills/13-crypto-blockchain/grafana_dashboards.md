---
rating: ⭐⭐
title: grafana-dashboards
url: https://skills.sh/wshobson/agents/grafana-dashboards
---

# grafana-dashboards

skills/wshobson/agents/grafana-dashboards
grafana-dashboards
Installation
$ npx skills add https://github.com/wshobson/agents --skill grafana-dashboards
Summary

Production-ready Grafana dashboards for system and application metrics visualization.

Covers RED method (Rate, Errors, Duration) for services and USE method (Utilization, Saturation, Errors) for resources
Supports multiple panel types including stat panels, time series graphs, tables, and heatmaps with Prometheus queries
Includes templating with query variables for dynamic filtering by namespace, service, and other dimensions
Provides dashboard provisioning via YAML configuration and infrastructure-as-code patterns using Terraform and Ansible
Demonstrates common patterns for API, infrastructure, database, and application monitoring dashboards with alert configuration
SKILL.md
Grafana Dashboards

Create and manage production-ready Grafana dashboards for comprehensive system observability.

Purpose

Design effective Grafana dashboards for monitoring applications, infrastructure, and business metrics.

When to Use
Visualize Prometheus metrics
Create custom dashboards
Implement SLO dashboards
Monitor infrastructure
Track business KPIs
Dashboard Design Principles
1. Hierarchy of Information
┌─────────────────────────────────────┐
│  Critical Metrics (Big Numbers)     │
├─────────────────────────────────────┤
│  Key Trends (Time Series)           │
├─────────────────────────────────────┤
│  Detailed Metrics (Tables/Heatmaps) │
└─────────────────────────────────────┘

2. RED Method (Services)
Rate - Requests per second
Errors - Error rate
Duration - Latency/response time
3. USE Method (Resources)
Utilization - % time resource is busy
Saturation - Queue length/wait time
Errors - Error count
Dashboard Structure
API Monitoring Dashboard
{
  "dashboard": {
    "title": "API Monitoring",
    "tags": ["api", "production"],
    "timezone": "browser",
    "refresh": "30s",
    "panels": [
      {
        "title": "Request Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "sum(rate(http_requests_total[5m])) by (service)",
            "legendFormat": "{{service}}"
          }
        ],
        "gridPos": { "x": 0, "y": 0, "w": 12, "h": 8 }
      },
      {
        "title": "Error Rate %",
        "type": "graph",
        "targets": [
          {
            "expr": "(sum(rate(http_requests_total{status=~\"5..\"}[5m])) / sum(rate(http_requests_total[5m]))) * 100",
            "legendFormat": "Error Rate"
          }
        ],
        "alert": {
          "conditions": [
            {
              "evaluator": { "params": [5], "type": "gt" },
              "operator": { "type": "and" },
              "query": { "params": ["A", "5m", "now"] },
              "type": "query"
            }
          ]
        },
        "gridPos": { "x": 12, "y": 0, "w": 12, "h": 8 }
      },
      {
        "title": "P95 Latency",
        "type": "graph",
        "targets": [
          {
            "expr": "histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[5m])) by (le, service))",
            "legendFormat": "{{service}}"
          }
        ],
        "gridPos": { "x": 0, "y": 8, "w": 24, "h": 8 }
      }
    ]
  }
}


Reference: See assets/api-dashboard.json

Panel Types
1. Stat Panel (Single Value)
{
  "type": "stat",
  "title": "Total Requests",
  "targets": [
    {
      "expr": "sum(http_requests_total)"
    }
  ],
  "options": {
    "reduceOptions": {
      "values": false,
      "calcs": ["lastNotNull"]
    },
    "orientation": "auto",
    "textMode": "auto",
    "colorMode": "value"
  },
  "fieldConfig": {
    "defaults": {
      "thresholds": {
        "mode": "absolute",
        "steps": [
          { "value": 0, "color": "green" },
          { "value": 80, "color": "yellow" },
          { "value": 90, "color": "red" }
        ]
      }
    }
  }
}

2. Time Series Graph
{
  "type": "graph",
  "title": "CPU Usage",
  "targets": [
    {
      "expr": "100 - (avg by (instance) (rate(node_cpu_seconds_total{mode=\"idle\"}[5m])) * 100)"
    }
  ],
  "yaxes": [
    { "format": "percent", "max": 100, "min": 0 },
    { "format": "short" }
  ]
}

3. Table Panel
{
  "type": "table",
  "title": "Service Status",
  "targets": [
    {
      "expr": "up",
      "format": "table",
      "instant": true
    }
  ],
  "transformations": [
    {
      "id": "organize",
      "options": {
        "excludeByName": { "Time": true },
        "indexByName": {},
        "renameByName": {
          "instance": "Instance",
          "job": "Service",
          "Value": "Status"
        }
      }
    }
  ]
}

4. Heatmap
{
  "type": "heatmap",
  "title": "Latency Heatmap",
  "targets": [
    {
      "expr": "sum(rate(http_request_duration_seconds_bucket[5m])) by (le)",
      "format": "heatmap"
    }
  ],
  "dataFormat": "tsbuckets",
  "yAxis": {
    "format": "s"
  }
}

Variables
Query Variables
{
  "templating": {
    "list": [
      {
        "name": "namespace",
        "type": "query",
        "datasource": "Prometheus",
        "query": "label_values(kube_pod_info, namespace)",
        "refresh": 1,
        "multi": false
      },
      {
        "name": "service",
        "type": "query",
        "datasource": "Prometheus",
        "query": "label_values(kube_service_info{namespace=\"$namespace\"}, service)",
        "refresh": 1,
        "multi": true
      }
    ]
  }
}

Use Variables in Queries
sum(rate(http_requests_total{namespace="$namespace", service=~"$service"}[5m]))

Alerts in Dashboards
{
  "alert": {
    "name": "High Error Rate",
    "conditions": [
      {
        "evaluator": {
          "params": [5],
          "type": "gt"
        },
        "operator": { "type": "and" },
        "query": {
          "params": ["A", "5m", "now"]
        },
        "reducer": { "type": "avg" },
        "type": "query"
      }
    ],
    "executionErrorState": "alerting",
    "for": "5m",
    "frequency": "1m",
    "message": "Error rate is above 5%",
    "noDataState": "no_data",
    "notifications": [{ "uid": "slack-channel" }]
  }
}

Dashboard Provisioning

dashboards.yml:

apiVersion: 1

providers:
  - name: "default"
    orgId: 1
    folder: "General"
    type: file
    disableDeletion: false
    updateIntervalSeconds: 10
    allowUiUpdates: true
    options:
      path: /etc/grafana/dashboards

Common Dashboard Patterns
Infrastructure Dashboard

Key Panels:

CPU utilization per node
Memory usage per node
Disk I/O
Network traffic
Pod count by namespace
Node status

Reference: See assets/infrastructure-dashboard.json

Database Dashboard

Key Panels:

Queries per second
Connection pool usage
Query latency (P50, P95, P99)
Active connections
Database size
Replication lag
Slow queries

Reference: See assets/database-dashboard.json

Application Dashboard

Key Panels:

Request rate
Error rate
Response time (percentiles)
Active users/sessions
Cache hit rate
Queue length
Best Practices
Start with templates (Grafana community dashboards)
Use consistent naming for panels and variables
Group related metrics in rows
Set appropriate time ranges (default: Last 6 hours)
Use variables for flexibility
Add panel descriptions for context
Configure units correctly
Set meaningful thresholds for colors
Use consistent colors across dashboards
Test with different time ranges
Dashboard as Code
Terraform Provisioning
resource "grafana_dashboard" "api_monitoring" {
  config_json = file("${path.module}/dashboards/api-monitoring.json")
  folder      = grafana_folder.monitoring.id
}

resource "grafana_folder" "monitoring" {
  title = "Production Monitoring"
}

Ansible Provisioning
- name: Deploy Grafana dashboards
  copy:
    src: "{{ item }}"
    dest: /etc/grafana/dashboards/
  with_fileglob:
    - "dashboards/*.json"
  notify: restart grafana

Related Skills
prometheus-configuration - For metric collection
slo-implementation - For SLO dashboards
Weekly Installs
6.8K
Repository
wshobson/agents
GitHub Stars
34.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn