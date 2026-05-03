---
title: n8n-daily-report
url: https://skills.sh/datadrivenconstruction/ddc_skills_for_ai_agents_in_construction/n8n-daily-report
---

# n8n-daily-report

skills/datadrivenconstruction/ddc_skills_for_ai_agents_in_construction/n8n-daily-report
n8n-daily-report
Installation
$ npx skills add https://github.com/datadrivenconstruction/ddc_skills_for_ai_agents_in_construction --skill n8n-daily-report
SKILL.md
n8n Daily Report Automation
Business Case

Daily reports are critical but time-consuming. This n8n workflow automates collection of site data from multiple sources and generates formatted daily reports.

Workflow Overview
[Site Data Sources] → [n8n Webhook] → [Data Processing] → [Report Generation] → [Distribution]

n8n Workflow Configuration
1. Trigger Node: Schedule + Webhook
{
  "nodes": [
    {
      "name": "Daily Schedule",
      "type": "n8n-nodes-base.scheduleTrigger",
      "parameters": {
        "rule": {
          "interval": [{"field": "cronExpression", "expression": "0 17 * * 1-5"}]
        }
      }
    },
    {
      "name": "Webhook Input",
      "type": "n8n-nodes-base.webhook",
      "parameters": {
        "httpMethod": "POST",
        "path": "daily-report-data"
      }
    }
  ]
}

2. Data Collection Nodes
{
  "nodes": [
    {
      "name": "Get Weather Data",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "url": "https://api.openweathermap.org/data/2.5/weather",
        "qs": {
          "lat": "={{$json.site_lat}}",
          "lon": "={{$json.site_lon}}",
          "appid": "={{$env.WEATHER_API_KEY}}"
        }
      }
    },
    {
      "name": "Get Site Photos",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "url": "={{$env.PROCORE_API}}/projects/{{$json.project_id}}/images",
        "authentication": "oAuth2"
      }
    },
    {
      "name": "Get Labor Data",
      "type": "n8n-nodes-base.spreadsheetFile",
      "parameters": {
        "operation": "read",
        "fileFormat": "xlsx"
      }
    }
  ]
}

3. Data Processing
{
  "name": "Process Report Data",
  "type": "n8n-nodes-base.code",
  "parameters": {
    "jsCode": "const items = $input.all();\n\nconst weather = items[0].json;\nconst photos = items[1].json;\nconst labor = items[2].json;\n\nconst report = {\n  date: new Date().toISOString().split('T')[0],\n  project: $('Webhook Input').first().json.project_name,\n  weather: {\n    condition: weather.weather[0].main,\n    temp_high: Math.round(weather.main.temp_max - 273.15),\n    temp_low: Math.round(weather.main.temp_min - 273.15)\n  },\n  labor_summary: {\n    total_workers: labor.reduce((sum, l) => sum + l.workers, 0),\n    total_hours: labor.reduce((sum, l) => sum + l.hours, 0)\n  },\n  photo_count: photos.length\n};\n\nreturn [{json: report}];"
  }
}

4. Report Generation
{
  "name": "Generate PDF Report",
  "type": "n8n-nodes-base.httpRequest",
  "parameters": {
    "method": "POST",
    "url": "={{$env.PDF_SERVICE_URL}}/generate",
    "body": {
      "template": "daily_report",
      "data": "={{$json}}"
    }
  }
}

5. Distribution
{
  "nodes": [
    {
      "name": "Send Email",
      "type": "n8n-nodes-base.emailSend",
      "parameters": {
        "toEmail": "={{$json.distribution_list}}",
        "subject": "Daily Report - {{$json.project}} - {{$json.date}}",
        "attachments": "={{$node['Generate PDF Report'].json.file}}"
      }
    },
    {
      "name": "Upload to SharePoint",
      "type": "n8n-nodes-base.microsoftSharePoint",
      "parameters": {
        "operation": "upload",
        "siteId": "={{$env.SHAREPOINT_SITE}}",
        "folderId": "/Daily Reports/{{$json.date}}"
      }
    }
  ]
}

Python Helper Functions
import requests
from datetime import date

def trigger_daily_report(project_data: dict, webhook_url: str):
    """Trigger n8n daily report workflow."""
    payload = {
        "project_id": project_data['id'],
        "project_name": project_data['name'],
        "site_lat": project_data['latitude'],
        "site_lon": project_data['longitude'],
        "distribution_list": project_data['stakeholder_emails']
    }

    response = requests.post(webhook_url, json=payload)
    return response.status_code == 200


def format_labor_data(labor_entries: list) -> list:
    """Format labor data for n8n processing."""
    formatted = []
    for entry in labor_entries:
        formatted.append({
            'trade': entry['trade'],
            'company': entry['company'],
            'workers': entry['worker_count'],
            'hours': entry['total_hours'],
            'activities': entry.get('activities', [])
        })
    return formatted

Quick Start
Import workflow to n8n
Configure environment variables:
WEATHER_API_KEY
PROCORE_API
PDF_SERVICE_URL
SHAREPOINT_SITE
Set schedule trigger for desired time
Configure email distribution list
Resources
n8n Documentation: https://docs.n8n.io
DDC Book: Chapter 4.2 - Workflow Automation
Weekly Installs
18
Repository
datadrivenconst…truction
GitHub Stars
114
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn