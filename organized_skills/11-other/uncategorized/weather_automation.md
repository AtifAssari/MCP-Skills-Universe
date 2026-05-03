---
rating: ⭐⭐⭐
title: weather automation
url: https://skills.sh/claude-office-skills/skills/weather-automation
---

# weather automation

skills/claude-office-skills/skills/Weather Automation
Weather Automation
Installation
$ npx skills add https://github.com/claude-office-skills/skills --skill 'Weather Automation'
SKILL.md
Weather Automation

Automate weather-based workflows and notifications.

Core Capabilities
Current Weather
current_weather:
  location: "San Francisco, CA"
  # or coordinates
  lat: 37.7749
  lon: -122.4194
  
  response:
    temperature: 65°F
    feels_like: 63°F
    humidity: 72%
    wind_speed: 12 mph
    conditions: "Partly Cloudy"
    uv_index: 5

Forecast
forecast:
  location: "New York, NY"
  days: 7
  
  daily:
    - date: "2024-01-20"
      high: 45°F
      low: 32°F
      conditions: "Snow"
      precipitation_chance: 80%
      
  hourly:
    interval: 3  # hours
    periods: 24

Weather Alerts
alert_rules:
  - name: "Rain Alert"
    condition:
      precipitation_chance: "> 70%"
      within_hours: 6
    action:
      notify: slack
      message: "☔ Rain expected in next 6 hours"
      
  - name: "Freeze Warning"
    condition:
      temperature: "< 32°F"
    action:
      - notify: sms
      - trigger: home_assistant
        action: protect_pipes

Workflow Examples
Morning Briefing
morning_weather:
  trigger: daily at 6:30 AM
  actions:
    - get_forecast:
        location: home
        days: 1
    - send_notification:
        channel: slack_dm
        message: |
          🌤️ Good morning! Today's weather:
          High: {{high}}°F | Low: {{low}}°F
          {{conditions}}
          {{#if rain}}☔ Bring an umbrella!{{/if}}

Event Planning
event_weather:
  trigger: calendar_event_tomorrow
  condition:
    event_type: outdoor
  actions:
    - get_forecast:
        location: "{{event.location}}"
        date: "{{event.date}}"
    - if:
        precipitation_chance: "> 50%"
      then:
        - notify: organizer
          message: "Consider backup venue - rain likely"

Best Practices
Caching: Cache frequent requests
Units: Support both metric/imperial
Accuracy: Use reliable data sources
Alerts: Set sensible thresholds
Location: Support multiple formats
Weekly Installs
–
Repository
claude-office-s…s/skills
GitHub Stars
94
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass