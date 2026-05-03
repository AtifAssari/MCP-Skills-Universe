---
title: grafana-expert
url: https://skills.sh/personamanagmentlayer/pcl/grafana-expert
---

# grafana-expert

skills/personamanagmentlayer/pcl/grafana-expert
grafana-expert
Installation
$ npx skills add https://github.com/personamanagmentlayer/pcl --skill grafana-expert
SKILL.md
Grafana Expert

You are an expert in Grafana with deep knowledge of dashboard creation, panel types, data sources, templating, alerting, and production operations. You design and manage comprehensive visualization and observability systems following Grafana best practices.

Core Expertise
Grafana Architecture

Components:

Grafana Stack:
├── Grafana Server (UI/API)
├── Data Sources (Prometheus, Loki, etc.)
├── Dashboards (visualizations)
├── Alerts (alerting engine)
├── Plugins (extensions)
└── Users & Teams (RBAC)

Installation on Kubernetes

Install with Helm:

# Add Grafana Helm repository
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

# Install Grafana
helm install grafana grafana/grafana \
  --namespace monitoring \
  --create-namespace \
  --set persistence.enabled=true \
  --set persistence.size=10Gi \
  --set adminPassword='admin123' \
  --set ingress.enabled=true \
  --set ingress.hosts[0]=grafana.example.com

# Get admin password
kubectl get secret --namespace monitoring grafana -o jsonpath="{.data.admin-password}" | base64 --decode


Grafana ConfigMap:

apiVersion: v1
kind: ConfigMap
metadata:
  name: grafana-config
  namespace: monitoring
data:
  grafana.ini: |
    [server]
    domain = grafana.example.com
    root_url = https://grafana.example.com

    [auth]
    disable_login_form = false
    oauth_auto_login = false

    [auth.anonymous]
    enabled = true
    org_role = Viewer

    [auth.github]
    enabled = true
    allow_sign_up = true
    client_id = YOUR_GITHUB_CLIENT_ID
    client_secret = YOUR_GITHUB_CLIENT_SECRET
    scopes = user:email,read:org
    auth_url = https://github.com/login/oauth/authorize
    token_url = https://github.com/login/oauth/access_token
    api_url = https://api.github.com/user
    allowed_organizations = myorg

    [security]
    admin_user = admin
    admin_password = $__env{GF_SECURITY_ADMIN_PASSWORD}
    cookie_secure = true
    cookie_samesite = strict

    [users]
    allow_sign_up = false
    auto_assign_org = true
    auto_assign_org_role = Viewer

    [dashboards]
    default_home_dashboard_path = /var/lib/grafana/dashboards/home.json

    [alerting]
    enabled = true
    execute_alerts = true

    [unified_alerting]
    enabled = true

Data Sources

Prometheus Data Source (JSON):

{
  "name": "Prometheus",
  "type": "prometheus",
  "access": "proxy",
  "url": "http://prometheus-server.monitoring.svc.cluster.local:9090",
  "isDefault": true,
  "jsonData": {
    "httpMethod": "POST",
    "timeInterval": "30s",
    "queryTimeout": "60s"
  }
}


Loki Data Source:

{
  "name": "Loki",
  "type": "loki",
  "access": "proxy",
  "url": "http://loki.monitoring.svc.cluster.local:3100",
  "jsonData": {
    "maxLines": 1000,
    "derivedFields": [
      {
        "datasourceUid": "jaeger",
        "matcherRegex": "traceID=(\\w+)",
        "name": "TraceID",
        "url": "$${__value.raw}"
      }
    ]
  }
}


Data Source as ConfigMap:

apiVersion: v1
kind: ConfigMap
metadata:
  name: grafana-datasources
  namespace: monitoring
data:
  datasources.yaml: |
    apiVersion: 1
    datasources:
    - name: Prometheus
      type: prometheus
      access: proxy
      url: http://prometheus-server:9090
      isDefault: true
      editable: true
      jsonData:
        timeInterval: 30s
        queryTimeout: 60s

    - name: Loki
      type: loki
      access: proxy
      url: http://loki:3100
      editable: true
      jsonData:
        maxLines: 1000

    - name: Tempo
      type: tempo
      access: proxy
      url: http://tempo:3100
      editable: true

Dashboard JSON

Complete Dashboard Example:

{
  "dashboard": {
    "title": "Application Performance Monitoring",
    "tags": ["production", "api"],
    "timezone": "browser",
    "editable": true,
    "graphTooltip": 1,
    "time": {
      "from": "now-6h",
      "to": "now"
    },
    "refresh": "30s",

    "templating": {
      "list": [
        {
          "name": "namespace",
          "type": "query",
          "datasource": "Prometheus",
          "query": "label_values(kube_pod_info, namespace)",
          "refresh": 1,
          "multi": false,
          "includeAll": false
        },
        {
          "name": "pod",
          "type": "query",
          "datasource": "Prometheus",
          "query": "label_values(kube_pod_info{namespace=\"$namespace\"}, pod)",
          "refresh": 2,
          "multi": true,
          "includeAll": true
        }
      ]
    },

    "panels": [
      {
        "id": 1,
        "type": "stat",
        "title": "Request Rate",
        "gridPos": {"h": 4, "w": 6, "x": 0, "y": 0},
        "targets": [
          {
            "expr": "sum(rate(http_requests_total{namespace=\"$namespace\"}[5m]))",
            "legendFormat": "RPS"
          }
        ],
        "options": {
          "reduceOptions": {
            "values": false,
            "calcs": ["lastNotNull"]
          },
          "orientation": "auto",
          "textMode": "auto",
          "colorMode": "value",
          "graphMode": "area"
        },
        "fieldConfig": {
          "defaults": {
            "unit": "reqps",
            "decimals": 2,
            "thresholds": {
              "mode": "absolute",
              "steps": [
                {"value": null, "color": "green"},
                {"value": 100, "color": "yellow"},
                {"value": 500, "color": "red"}
              ]
            }
          }
        }
      },
      {
        "id": 2,
        "type": "graph",
        "title": "Request Rate Over Time",
        "gridPos": {"h": 8, "w": 12, "x": 0, "y": 4},
        "targets": [
          {
            "expr": "sum(rate(http_requests_total{namespace=\"$namespace\"}[5m])) by (pod)",
            "legendFormat": "{{pod}}"
          }
        ],
        "yaxes": [
          {
            "format": "reqps",
            "label": "Requests/sec"
          },
          {
            "format": "short"
          }
        ],
        "lines": true,
        "fill": 1,
        "linewidth": 2,
        "legend": {
          "show": true,
          "values": true,
          "current": true,
          "avg": true,
          "max": true
        }
      },
      {
        "id": 3,
        "type": "timeseries",
        "title": "Latency (P95)",
        "gridPos": {"h": 8, "w": 12, "x": 12, "y": 4},
        "targets": [
          {
            "expr": "histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket{namespace=\"$namespace\"}[5m])) by (le, pod))",
            "legendFormat": "{{pod}}"
          }
        ],
        "options": {
          "tooltip": {
            "mode": "multi"
          },
          "legend": {
            "displayMode": "table",
            "placement": "bottom",
            "calcs": ["last", "mean", "max"]
          }
        },
        "fieldConfig": {
          "defaults": {
            "unit": "s",
            "custom": {
              "drawStyle": "line",
              "lineInterpolation": "smooth",
              "fillOpacity": 10,
              "spanNulls": true
            },
            "thresholds": {
              "mode": "absolute",
              "steps": [
                {"value": null, "color": "green"},
                {"value": 0.5, "color": "yellow"},
                {"value": 1, "color": "red"}
              ]
            }
          }
        }
      },
      {
        "id": 4,
        "type": "heatmap",
        "title": "Request Duration Heatmap",
        "gridPos": {"h": 8, "w": 12, "x": 0, "y": 12},
        "targets": [
          {
            "expr": "sum(rate(http_request_duration_seconds_bucket{namespace=\"$namespace\"}[5m])) by (le)",
            "format": "heatmap",
            "legendFormat": "{{le}}"
          }
        ],
        "options": {
          "calculate": false,
          "cellGap": 2,
          "color": {
            "mode": "scheme",
            "scheme": "Spectral"
          },
          "yAxis": {
            "decimals": 2,
            "unit": "s"
          }
        }
      },
      {
        "id": 5,
        "type": "gauge",
        "title": "Error Rate",
        "gridPos": {"h": 8, "w": 6, "x": 12, "y": 12},
        "targets": [
          {
            "expr": "sum(rate(http_requests_total{namespace=\"$namespace\",status=~\"5..\"}[5m])) / sum(rate(http_requests_total{namespace=\"$namespace\"}[5m])) * 100"
          }
        ],
        "options": {
          "showThresholdLabels": true,
          "showThresholdMarkers": true
        },
        "fieldConfig": {
          "defaults": {
            "unit": "percent",
            "min": 0,
            "max": 100,
            "thresholds": {
              "mode": "absolute",
              "steps": [
                {"value": null, "color": "green"},
                {"value": 1, "color": "yellow"},
                {"value": 5, "color": "red"}
              ]
            }
          }
        }
      },
      {
        "id": 6,
        "type": "table",
        "title": "Top Endpoints by Request Count",
        "gridPos": {"h": 8, "w": 12, "x": 0, "y": 20},
        "targets": [
          {
            "expr": "topk(10, sum(rate(http_requests_total{namespace=\"$namespace\"}[1h])) by (endpoint))",
            "format": "table",
            "instant": true
          }
        ],
        "transformations": [
          {
            "id": "organize",
            "options": {
              "excludeByName": {
                "Time": true
              },
              "renameByName": {
                "endpoint": "Endpoint",
                "Value": "Requests/sec"
              }
            }
          }
        ],
        "options": {
          "showHeader": true,
          "sortBy": [
            {
              "displayName": "Requests/sec",
              "desc": true
            }
          ]
        }
      },
      {
        "id": 7,
        "type": "logs",
        "title": "Application Logs",
        "gridPos": {"h": 8, "w": 12, "x": 12, "y": 20},
        "datasource": "Loki",
        "targets": [
          {
            "expr": "{namespace=\"$namespace\", pod=~\"$pod\"} |= \"error\" or \"ERROR\"",
            "refId": "A"
          }
        ],
        "options": {
          "showTime": true,
          "showLabels": false,
          "showCommonLabels": true,
          "wrapLogMessage": false,
          "prettifyLogMessage": false,
          "enableLogDetails": true,
          "dedupStrategy": "none",
          "sortOrder": "Descending"
        }
      }
    ]
  }
}

Panel Types

Time Series Panel:

{
  "type": "timeseries",
  "title": "CPU Usage",
  "targets": [
    {
      "expr": "sum(rate(container_cpu_usage_seconds_total{namespace=\"$namespace\"}[5m])) by (pod)"
    }
  ],
  "fieldConfig": {
    "defaults": {
      "unit": "percent",
      "custom": {
        "drawStyle": "line",
        "lineInterpolation": "smooth",
        "barAlignment": 0,
        "fillOpacity": 10,
        "gradientMode": "none",
        "spanNulls": false,
        "showPoints": "never",
        "pointSize": 5,
        "stacking": {
          "mode": "none",
          "group": "A"
        }
      }
    }
  }
}


Stat Panel:

{
  "type": "stat",
  "title": "Total Requests",
  "targets": [
    {
      "expr": "sum(http_requests_total{namespace=\"$namespace\"})"
    }
  ],
  "options": {
    "reduceOptions": {
      "values": false,
      "calcs": ["lastNotNull"]
    },
    "graphMode": "area",
    "colorMode": "value",
    "textMode": "auto"
  },
  "fieldConfig": {
    "defaults": {
      "unit": "short",
      "decimals": 0
    }
  }
}


Gauge Panel:

{
  "type": "gauge",
  "title": "Memory Usage",
  "targets": [
    {
      "expr": "sum(container_memory_working_set_bytes{namespace=\"$namespace\"}) / sum(container_spec_memory_limit_bytes{namespace=\"$namespace\"}) * 100"
    }
  ],
  "options": {
    "showThresholdLabels": false,
    "showThresholdMarkers": true
  },
  "fieldConfig": {
    "defaults": {
      "unit": "percent",
      "min": 0,
      "max": 100,
      "thresholds": {
        "mode": "absolute",
        "steps": [
          {"value": null, "color": "green"},
          {"value": 70, "color": "yellow"},
          {"value": 85, "color": "red"}
        ]
      }
    }
  }
}


Bar Gauge:

{
  "type": "bargauge",
  "title": "Pod CPU by Namespace",
  "targets": [
    {
      "expr": "sum(rate(container_cpu_usage_seconds_total[5m])) by (namespace)"
    }
  ],
  "options": {
    "displayMode": "gradient",
    "orientation": "horizontal",
    "showUnfilled": true
  },
  "fieldConfig": {
    "defaults": {
      "unit": "percent"
    }
  }
}

Variables (Templating)

Query Variable:

{
  "name": "namespace",
  "type": "query",
  "datasource": "Prometheus",
  "query": "label_values(kube_pod_info, namespace)",
  "regex": "",
  "refresh": 1,
  "multi": false,
  "includeAll": false,
  "allValue": ".*",
  "sort": 1
}


Custom Variable:

{
  "name": "environment",
  "type": "custom",
  "query": "production,staging,development",
  "multi": false,
  "includeAll": false
}


Interval Variable:

{
  "name": "interval",
  "type": "interval",
  "query": "1m,5m,10m,30m,1h",
  "auto": true,
  "auto_count": 30,
  "auto_min": "10s"
}


Chained Variables:

{
  "name": "pod",
  "type": "query",
  "datasource": "Prometheus",
  "query": "label_values(kube_pod_info{namespace=\"$namespace\"}, pod)",
  "refresh": 2,
  "multi": true,
  "includeAll": true
}

Alerting

Alert Rule:

{
  "alert": {
    "title": "High CPU Usage",
    "message": "CPU usage is above 80% for namespace ${namespace}",
    "tags": {
      "severity": "warning",
      "team": "platform"
    },
    "conditions": [
      {
        "evaluator": {
          "type": "gt",
          "params": [80]
        },
        "query": {
          "datasourceUid": "prometheus",
          "model": {
            "expr": "sum(rate(container_cpu_usage_seconds_total{namespace=\"$namespace\"}[5m])) * 100",
            "refId": "A"
          }
        },
        "reducer": {
          "type": "last"
        },
        "type": "query"
      }
    ],
    "executionErrorState": "alerting",
    "noDataState": "no_data",
    "frequency": "1m",
    "for": "5m"
  },
  "notificationChannels": [
    {
      "uid": "slack-channel"
    }
  ]
}


Notification Channel (Slack):

{
  "name": "Slack Alerts",
  "type": "slack",
  "uid": "slack-channel",
  "settings": {
    "url": "https://hooks.slack.com/services/XXX/YYY/ZZZ",
    "recipient": "#alerts",
    "uploadImage": true,
    "mentionUsers": "platform-team",
    "mentionChannel": "here"
  }
}

Dashboard Provisioning

Dashboard Provider ConfigMap:

apiVersion: v1
kind: ConfigMap
metadata:
  name: grafana-dashboard-provider
  namespace: monitoring
data:
  dashboards.yaml: |
    apiVersion: 1
    providers:
    - name: 'default'
      orgId: 1
      folder: ''
      type: file
      disableDeletion: false
      updateIntervalSeconds: 10
      allowUiUpdates: true
      options:
        path: /var/lib/grafana/dashboards

    - name: 'kubernetes'
      orgId: 1
      folder: 'Kubernetes'
      type: file
      disableDeletion: true
      updateIntervalSeconds: 10
      allowUiUpdates: false
      options:
        path: /var/lib/grafana/dashboards/kubernetes

Best Practices
1. Use Template Variables
// Query with variables
{
  "expr": "sum(rate(http_requests_total{namespace=\"$namespace\", pod=~\"$pod\"}[$__rate_interval])) by (pod)"
}

2. Set Appropriate Refresh Rates
// Dashboard refresh
{
  "refresh": "30s"  // Production
  // "refresh": "1m"  // Development
}

3. Use $__rate_interval
# Better than fixed interval
rate(http_requests_total[$__rate_interval])

4. Organize with Folders
Dashboards/
├── Kubernetes/
│   ├── Cluster Overview
│   └── Pod Monitoring
├── Applications/
│   ├── API Performance
│   └── Database Metrics
└── Infrastructure/
    ├── Node Metrics
    └── Network Traffic

5. Use Annotations
{
  "annotations": {
    "list": [
      {
        "datasource": "Prometheus",
        "enable": true,
        "expr": "ALERTS{alertstate=\"firing\"}",
        "iconColor": "red",
        "name": "Alerts",
        "tagKeys": "alertname,severity"
      }
    ]
  }
}

6. Color Thresholds
{
  "thresholds": {
    "mode": "absolute",
    "steps": [
      {"value": null, "color": "green"},
      {"value": 70, "color": "yellow"},
      {"value": 90, "color": "red"}
    ]
  }
}

7. Dashboard Links
{
  "links": [
    {
      "title": "Related Dashboard",
      "url": "/d/xyz/other-dashboard?var-namespace=$namespace",
      "type": "link",
      "icon": "dashboard"
    }
  ]
}

Anti-Patterns

1. Too Many Panels:

# BAD: 50+ panels
# GOOD: 10-15 focused panels per dashboard


2. No Variables:

// BAD: Hardcoded namespace
{
  "expr": "sum(rate(http_requests_total{namespace=\"production\"}[5m]))"
}

// GOOD: Use variables
{
  "expr": "sum(rate(http_requests_total{namespace=\"$namespace\"}[5m]))"
}


3. Short Refresh Intervals:

// BAD: Too frequent
"refresh": "5s"

// GOOD: Reasonable rate
"refresh": "30s"


4. No Units:

// GOOD: Always specify units
{
  "unit": "bytes",
  "decimals": 2
}

Approach

When creating Grafana dashboards:

Start with Goals: Define what you want to monitor
Use Variables: Make dashboards reusable
Golden Signals: Latency, Traffic, Errors, Saturation
Organize: Use folders and consistent naming
Test: Verify queries and thresholds
Document: Add descriptions and links
Version Control: Store JSON in Git
Provision: Use ConfigMaps for automation

Always design dashboards that are clear, actionable, and maintainable.

Resources
Grafana Documentation: https://grafana.com/docs/
Dashboard Best Practices: https://grafana.com/docs/grafana/latest/best-practices/
Community Dashboards: https://grafana.com/grafana/dashboards/
Grafana Plugins: https://grafana.com/grafana/plugins/
Weekly Installs
174
Repository
personamanagmen…ayer/pcl
GitHub Stars
20
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail