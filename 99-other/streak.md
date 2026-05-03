---
title: streak
url: https://skills.sh/vm0-ai/vm0-skills/streak
---

# streak

skills/vm0-ai/vm0-skills/streak
streak
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill streak
SKILL.md
Troubleshooting

If requests fail, run zero doctor check-connector --env-name STREAK_TOKEN or zero doctor check-connector --url https://api.streak.com/api/v1/users/me --method GET

How to Use
Authentication

Streak uses HTTP Basic Auth with your API key as the username and no password. In curl, use -u "$STREAK_TOKEN:" (note the trailing colon).

1. Get Current User
curl -s -X GET "https://api.streak.com/api/v1/users/me" -u "$STREAK_TOKEN:"

2. List All Pipelines

Pipelines represent business processes (Sales, Hiring, Projects, etc.).

curl -s -X GET "https://api.streak.com/api/v1/pipelines" -u "$STREAK_TOKEN:"

3. Get a Pipeline
curl -s -X GET "https://api.streak.com/api/v1/pipelines/{pipelineKey}" -u "$STREAK_TOKEN:"

4. Create a Pipeline

Write to /tmp/streak_request.json:

{
  "name": "New Sales Pipeline"
}


Then run:

curl -s -X PUT "https://api.streak.com/api/v1/pipelines" -u "$STREAK_TOKEN:" --header "Content-Type: application/json" -d @/tmp/streak_request.json

5. List Boxes in Pipeline

Boxes are the core data objects (deals, leads, projects) within a pipeline.

curl -s -X GET "https://api.streak.com/api/v1/pipelines/{pipelineKey}/boxes" -u "$STREAK_TOKEN:"

6. Get a Box
curl -s -X GET "https://api.streak.com/api/v1/boxes/{boxKey}" -u "$STREAK_TOKEN:"

7. Create a Box

Write to /tmp/streak_request.json:

{
  "name": "Acme Corp Deal"
}


Then run:

curl -s -X POST "https://api.streak.com/api/v1/pipelines/{pipelineKey}/boxes" -u "$STREAK_TOKEN:" --header "Content-Type: application/json" -d @/tmp/streak_request.json

8. Update a Box

Write to /tmp/streak_request.json:

{
  "name": "Updated Deal Name",
  "stageKey": "stageKey123"
}


Then run:

curl -s -X POST "https://api.streak.com/api/v1/boxes/{boxKey}" -u "$STREAK_TOKEN:" --header "Content-Type: application/json" -d @/tmp/streak_request.json

9. List Stages in Pipeline
curl -s -X GET "https://api.streak.com/api/v1/pipelines/{pipelineKey}/stages" -u "$STREAK_TOKEN:"

10. List Fields in Pipeline
curl -s -X GET "https://api.streak.com/api/v1/pipelines/{pipelineKey}/fields" -u "$STREAK_TOKEN:"

11. Get a Contact
curl -s -X GET "https://api.streak.com/api/v1/contacts/{contactKey}" -u "$STREAK_TOKEN:"

12. Create a Contact

Write to /tmp/streak_request.json:

{
  "teamKey": "teamKey123",
  "emailAddresses": ["john@example.com"],
  "givenName": "John",
  "familyName": "Doe"
}


Then run:

curl -s -X POST "https://api.streak.com/api/v1/contacts" -u "$STREAK_TOKEN:" --header "Content-Type: application/json" -d @/tmp/streak_request.json

13. Get an Organization
curl -s -X GET "https://api.streak.com/api/v1/organizations/{organizationKey}" -u "$STREAK_TOKEN:"

14. Search Boxes, Contacts, and Organizations
curl -s -X GET "https://api.streak.com/api/v1/search?query=acme" -u "$STREAK_TOKEN:"

15. Get Tasks in a Box
curl -s -X GET "https://api.streak.com/api/v1/boxes/{boxKey}/tasks" -u "$STREAK_TOKEN:"

16. Create a Task

Write to /tmp/streak_request.json:

{
  "text": "Follow up with client",
  "dueDate": 1735689600000
}


Then run:

curl -s -X POST "https://api.streak.com/api/v1/boxes/{boxKey}/tasks" -u "$STREAK_TOKEN:" --header "Content-Type: application/json" -d @/tmp/streak_request.json

17. Get Comments in a Box
curl -s -X GET "https://api.streak.com/api/v1/boxes/{boxKey}/comments" -u "$STREAK_TOKEN:"

18. Create a Comment

Write to /tmp/streak_request.json:

{
  "message": "Spoke with client today, they are interested."
}


Then run:

curl -s -X POST "https://api.streak.com/api/v1/boxes/{boxKey}/comments" -u "$STREAK_TOKEN:" --header "Content-Type: application/json" -d @/tmp/streak_request.json

19. Get Threads in a Box

Email threads associated with a box.

curl -s -X GET "https://api.streak.com/api/v1/boxes/{boxKey}/threads" -u "$STREAK_TOKEN:"

20. Get Files in a Box
curl -s -X GET "https://api.streak.com/api/v1/boxes/{boxKey}/files" -u "$STREAK_TOKEN:"

21. Get Meetings in a Box
curl -s -X GET "https://api.streak.com/api/v1/boxes/{boxKey}/meetings" -u "$STREAK_TOKEN:"

22. Create a Meeting Note

Write to /tmp/streak_request.json:

{
  "meetingDate": 1735689600000,
  "meetingNotes": "Discussed pricing and timeline.",
  "title": "Sales Call"
}


Then run:

curl -s -X POST "https://api.streak.com/api/v1/boxes/{boxKey}/meetings" -u "$STREAK_TOKEN:" --header "Content-Type: application/json" -d @/tmp/streak_request.json

23. Get Box Timeline
curl -s -X GET "https://api.streak.com/api/v1/boxes/{boxKey}/timeline" -u "$STREAK_TOKEN:"

Guidelines
Keys: Pipeline keys, box keys, and other identifiers are alphanumeric strings returned by the API
Timestamps: Use Unix timestamps in milliseconds for date fields (e.g., dueDate, meetingDate)
Rate Limits: Be mindful of API rate limits; add delays between bulk operations
Stages: To move a box to a different stage, update the box with the new stageKey
Email Integration: Streak is tightly integrated with Gmail; threads are Gmail thread IDs
Team Key: When creating contacts, you need a teamKey which can be obtained from the teams endpoint
Weekly Installs
61
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass