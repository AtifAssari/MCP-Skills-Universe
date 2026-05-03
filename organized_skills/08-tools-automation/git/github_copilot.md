---
rating: ⭐⭐
title: github-copilot
url: https://skills.sh/vm0-ai/vm0-skills/github-copilot
---

# github-copilot

skills/vm0-ai/vm0-skills/github-copilot
github-copilot
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill github-copilot
SKILL.md
Troubleshooting

If requests fail, run zero doctor check-connector --env-name GITHUB_TOKEN or zero doctor check-connector --url https://api.github.com/orgs/your-org/copilot/billing --method GET

How to Use

All examples below assume you have GITHUB_TOKEN set.

Base URL: https://api.github.com

Required headers:

Authorization: Bearer ${GITHUB_TOKEN}
Accept: application/vnd.github+json
X-GitHub-Api-Version: 2022-11-28
1. Get Copilot Billing Information

Get seat breakdown and settings for an organization. Replace your-org-name with your organization name:

curl -s -X GET "https://api.github.com/orgs/your-org-name/copilot/billing" --header "Authorization: Bearer $GITHUB_TOKEN" --header "Accept: application/vnd.github+json" --header "X-GitHub-Api-Version: 2022-11-28"


Response:

{
  "seat_breakdown": {
  "total": 12,
  "added_this_cycle": 2,
  "pending_cancellation": 0,
  "pending_invitation": 1,
  "active_this_cycle": 12,
  "inactive_this_cycle": 0
  },
  "seat_management_setting": "assign_selected",
  "public_code_suggestions": "block"
}

2. List All Copilot Seat Assignments

Get all users with Copilot seats. Replace your-org-name with your organization name:

curl -s -X GET "https://api.github.com/orgs/your-org-name/copilot/billing/seats?per_page=50" --header "Authorization: Bearer $GITHUB_TOKEN" --header "Accept: application/vnd.github+json" --header "X-GitHub-Api-Version: 2022-11-28" | jq '.seats[] | {login: .assignee.login, last_activity: .last_activity_at}'

3. Get Copilot Seat Details for a User

Get specific user's Copilot seat information. Replace your-org-name with your organization name and username with the target username:

curl -s -X GET "https://api.github.com/orgs/your-org-name/members/username/copilot" --header "Authorization: Bearer $GITHUB_TOKEN" --header "Accept: application/vnd.github+json" --header "X-GitHub-Api-Version: 2022-11-28"

4. Add Users to Copilot Subscription

Assign Copilot seats to specific users. Replace your-org-name with your organization name:

Write to /tmp/github_copilot_request.json:

{
  "selected_usernames": ["user1", "user2"]
}


Then run:

curl -s -X POST "https://api.github.com/orgs/your-org-name/copilot/billing/selected_users" --header "Authorization: Bearer $GITHUB_TOKEN" --header "Accept: application/vnd.github+json" --header "X-GitHub-Api-Version: 2022-11-28" --header "Content-Type: application/json" -d @/tmp/github_copilot_request.json


Response:

{
  "seats_created": 2
}

5. Remove Users from Copilot Subscription

Remove Copilot seats from specific users. Replace your-org-name with your organization name:

Write to /tmp/github_copilot_request.json:

{
  "selected_usernames": ["user1", "user2"]
}


Then run:

curl -s -X DELETE "https://api.github.com/orgs/your-org-name/copilot/billing/selected_users" --header "Authorization: Bearer $GITHUB_TOKEN" --header "Accept: application/vnd.github+json" --header "X-GitHub-Api-Version: 2022-11-28" --header "Content-Type: application/json" -d @/tmp/github_copilot_request.json


Response:

{
  "seats_cancelled": 2
}

6. Add Teams to Copilot Subscription

Assign Copilot to entire teams. Replace your-org-name with your organization name:

Write to /tmp/github_copilot_request.json:

{
  "selected_teams": ["engineering", "design"]
}


Then run:

curl -s -X POST "https://api.github.com/orgs/your-org-name/copilot/billing/selected_teams" --header "Authorization: Bearer $GITHUB_TOKEN" --header "Accept: application/vnd.github+json" --header "X-GitHub-Api-Version: 2022-11-28" --header "Content-Type: application/json" -d @/tmp/github_copilot_request.json

7. Remove Teams from Copilot Subscription

Remove Copilot from teams. Replace your-org-name with your organization name:

Write to /tmp/github_copilot_request.json:

{
  "selected_teams": ["engineering"]
}


Then run:

curl -s -X DELETE "https://api.github.com/orgs/your-org-name/copilot/billing/selected_teams" --header "Authorization: Bearer $GITHUB_TOKEN" --header "Accept: application/vnd.github+json" --header "X-GitHub-Api-Version: 2022-11-28" --header "Content-Type: application/json" -d @/tmp/github_copilot_request.json

8. Get Copilot Usage Metrics for Organization

Get usage statistics (requires 5+ active users). Replace your-org-name with your organization name:

curl -s -X GET "https://api.github.com/orgs/your-org-name/copilot/metrics?per_page=7" --header "Authorization: Bearer $GITHUB_TOKEN" --header "Accept: application/vnd.github+json" --header "X-GitHub-Api-Version: 2022-11-28" | jq '.[] | {date, total_active_users, total_engaged_users}'


Response:

{
  "date": "2024-06-24",
  "total_active_users": 24,
  "total_engaged_users": 20
}

9. Get Copilot Metrics for a Team

Get team-specific usage metrics. Replace your-org-name with your organization name and team-name with the target team:

curl -s -X GET "https://api.github.com/orgs/your-org-name/team/team-name/copilot/metrics" --header "Authorization: Bearer $GITHUB_TOKEN" --header "Accept: application/vnd.github+json" --header "X-GitHub-Api-Version: 2022-11-28"

Metrics Data Structure

The metrics response includes:

Field	Description
total_active_users	Users with Copilot activity
total_engaged_users	Users who accepted suggestions
copilot_ide_code_completions	Code completion stats by language/editor
copilot_ide_chat	IDE chat usage stats
copilot_dotcom_chat	GitHub.com chat usage
copilot_dotcom_pull_requests	PR summary usage
Guidelines
Requires Copilot Business/Enterprise: Free tier users cannot use this API
Metrics need 5+ users: Usage metrics only available with 5+ active Copilot users
Data retention: Metrics available for up to 100 days
Rate limits: Standard GitHub API rate limits apply
API in preview: Some endpoints may change
Weekly Installs
65
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn