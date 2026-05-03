---
title: health-data
url: https://skills.sh/9qwnkc6s79-a11y/troy-mission-control/health-data
---

# health-data

skills/9qwnkc6s79-a11y/troy-mission-control/health-data
health-data
Installation
$ npx skills add https://github.com/9qwnkc6s79-a11y/troy-mission-control --skill health-data
SKILL.md
Health Data Integration

Real-time access to iPhone health data through OpenClaw. Query your health metrics conversationally and get coaching insights.

How It Works
iOS Shortcuts exports health data from Apple Health app
Auto-sync via iCloud to OpenClaw workspace
Query interface allows natural language health questions
Trend analysis provides coaching insights over time
Quick Start

Ask conversational questions:

"What's my weight today?"
"How many steps have I taken?"
"What workouts did I do this week?"
"What's my weight trend this week?"
"Any concerning health patterns?"


Get current data:

python scripts/query_health.py --current


Generate insights:

python scripts/query_health.py --insights --days 7

Core Capabilities
1. Real-time Health Queries
Current weight, steps, calories, heart rate
Today's workouts and activity summary
Sleep data and recovery metrics
Instant answers to health questions
2. Trend Analysis
7-day, 30-day, 90-day health patterns
Weight loss/gain trends and rates
Workout frequency and consistency
Activity level changes over time
3. Coaching Insights
Personalized recommendations based on data
Health goal progress tracking
Warning alerts for concerning patterns
Actionable advice for improvement
4. Nutrition Integration
Links health metrics with food tracking
Calorie burn vs intake analysis
Body composition trends
Macro nutrient recommendations
Data Sources

All data flows through Apple Health as the central hub:

Weight: RENPHO scale → Apple Health
Workouts: Fitbod app → Apple Health
Steps/Activity: iPhone + Apple Watch → Apple Health
Heart Rate: Apple Watch → Apple Health
Sleep: Apple Watch → Apple Health
Nutrition: MyFitnessPal/other apps → Apple Health
Query Examples

Current Metrics:

"What's my weight today?"
"How many steps have I taken today?"
"What's my current heart rate?"
"Did I work out today?"

Historical Trends:

"What's my weight trend this week?"
"Am I meeting my step goals consistently?"
"How many workouts did I do this month?"
"What's my average daily calorie burn?"

Health Insights:

"Any health concerns I should know about?"
"What should I focus on this week?"
"How's my fitness progress?"
"Am I losing weight too fast?"
Resources
scripts/
query_health.py - Main query interface for conversational health questions
sync_health_data.py - Sync latest data from iOS Shortcuts export
generate_insights.py - Analyze trends and generate coaching recommendations
references/
setup_guide.md - Complete iOS Shortcuts setup instructions
healthkit_schema.md - Apple Health data structure and available metrics
coaching_algorithms.md - How health insights and recommendations are generated

Setup Required: The health sync system needs iOS Shortcuts configured. See references/setup_guide.md for 15-minute setup process.

Weekly Installs
16
Repository
9qwnkc6s79-a11y…-control
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketFail
SnykPass