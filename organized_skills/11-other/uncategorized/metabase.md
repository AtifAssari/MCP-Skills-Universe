---
rating: ⭐⭐
title: metabase
url: https://skills.sh/vm0-ai/vm0-skills/metabase
---

# metabase

skills/vm0-ai/vm0-skills/metabase
metabase
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill metabase
SKILL.md
Troubleshooting

If requests fail, run zero doctor check-connector --env-name METABASE_TOKEN or zero doctor check-connector --url https://your-metabase.example.com/api/user/current --method GET

How to Use

All examples below assume you have METABASE_TOKEN set. Authentication uses the x-api-key header.

1. Get Current User Info

Retrieve information about the authenticated user.

curl -s "$METABASE_BASE_URL/api/user/current" --header "x-api-key: $METABASE_TOKEN" | jq .

2. List Databases

Retrieve all connected databases.

curl -s "$METABASE_BASE_URL/api/database" --header "x-api-key: $METABASE_TOKEN" | jq '.data[] | {id, name, engine}'

3. Get Database Details

Retrieve details of a specific database including its tables.

curl -s "$METABASE_BASE_URL/api/database/DATABASE_ID?include=tables" --header "x-api-key: $METABASE_TOKEN" | jq .

4. Run a Query (Dataset)

Execute a query and return results. This is the primary endpoint for running queries.

Write to /tmp/metabase_request.json:

{
  "database": 1,
  "type": "native",
  "native": {
    "query": "SELECT * FROM orders LIMIT 10"
  }
}


Then run:

curl -s -X POST "$METABASE_BASE_URL/api/dataset" --header "Content-Type: application/json" --header "x-api-key: $METABASE_TOKEN" -d @/tmp/metabase_request.json | jq '{columns: [.data.cols[].name], row_count: .row_count}'

5. List Cards (Saved Questions)

Retrieve all saved questions.

curl -s "$METABASE_BASE_URL/api/card" --header "x-api-key: $METABASE_TOKEN" | jq '.[] | {id, name, display, database_id}'

6. Get Card Details

Retrieve a specific card (question) by ID.

curl -s "$METABASE_BASE_URL/api/card/CARD_ID" --header "x-api-key: $METABASE_TOKEN" | jq '{id, name, display, dataset_query}'

7. Run a Card Query

Execute a saved question and return its results.

curl -s -X POST "$METABASE_BASE_URL/api/card/CARD_ID/query" --header "x-api-key: $METABASE_TOKEN" | jq '{columns: [.data.cols[].name], row_count: .row_count}'

8. Create a Card (Question)

Create a new saved question.

Write to /tmp/metabase_request.json:

{
  "name": "Total Orders by Status",
  "dataset_query": {
    "database": 1,
    "type": "native",
    "native": {
      "query": "SELECT status, COUNT(*) as total FROM orders GROUP BY status"
    }
  },
  "display": "table",
  "visualization_settings": {},
  "collection_id": null
}


Then run:

curl -s -X POST "$METABASE_BASE_URL/api/card" --header "Content-Type: application/json" --header "x-api-key: $METABASE_TOKEN" -d @/tmp/metabase_request.json | jq '{id, name}'

9. Update a Card

Update a saved question's properties.

Write to /tmp/metabase_request.json:

{
  "name": "Updated Question Name",
  "description": "Updated description"
}


Then run:

curl -s -X PUT "$METABASE_BASE_URL/api/card/CARD_ID" --header "Content-Type: application/json" --header "x-api-key: $METABASE_TOKEN" -d @/tmp/metabase_request.json | jq .

10. List Dashboards

Retrieve all dashboards.

curl -s "$METABASE_BASE_URL/api/dashboard" --header "x-api-key: $METABASE_TOKEN" | jq '.[] | {id, name, collection_id}'

11. Get Dashboard Details

Retrieve a dashboard with all its cards.

curl -s "$METABASE_BASE_URL/api/dashboard/DASHBOARD_ID" --header "x-api-key: $METABASE_TOKEN" | jq '{id, name, dashcards: [.dashcards[] | {id, card_id, card: .card.name}]}'

12. Create a Dashboard

Create a new dashboard.

curl -s -X POST "$METABASE_BASE_URL/api/dashboard" --header "Content-Type: application/json" --header "x-api-key: $METABASE_TOKEN" -d '{"name":"My Dashboard","collection_id":null}' | jq '{id, name}'

13. Add a Card to Dashboard

Add an existing saved question to a dashboard.

Write to /tmp/metabase_request.json:

{
  "cardId": 1,
  "row": 0,
  "col": 0,
  "size_x": 6,
  "size_y": 4
}


Then run:

curl -s -X POST "$METABASE_BASE_URL/api/dashboard/DASHBOARD_ID/cards" --header "Content-Type: application/json" --header "x-api-key: $METABASE_TOKEN" -d @/tmp/metabase_request.json | jq .

14. List Collections

Retrieve all collections (folders for organizing content).

curl -s "$METABASE_BASE_URL/api/collection" --header "x-api-key: $METABASE_TOKEN" | jq '.[] | {id, name, location}'

15. Get Collection Items

Retrieve all items in a specific collection.

curl -s "$METABASE_BASE_URL/api/collection/COLLECTION_ID/items" --header "x-api-key: $METABASE_TOKEN" | jq '.data[] | {id, name, model}'

16. Create a Collection

Create a new collection for organizing dashboards and questions.

curl -s -X POST "$METABASE_BASE_URL/api/collection" --header "Content-Type: application/json" --header "x-api-key: $METABASE_TOKEN" -d '{"name":"My Collection","parent_id":null}' | jq '{id, name}'

17. Search

Search across cards, dashboards, and collections.

curl -s "$METABASE_BASE_URL/api/search?q=revenue" --header "x-api-key: $METABASE_TOKEN" | jq '.data[] | {id, name, model, collection}'


Filter by model type:

curl -s "$METABASE_BASE_URL/api/search?q=revenue&models=card" --header "x-api-key: $METABASE_TOKEN" | jq '.data[] | {id, name}'

18. List Users

Retrieve all users in the Metabase instance.

curl -s "$METABASE_BASE_URL/api/user" --header "x-api-key: $METABASE_TOKEN" | jq '.data[] | {id, email, first_name, last_name, is_active}'

19. Get Permission Groups

List all permission groups.

curl -s "$METABASE_BASE_URL/api/permissions/group" --header "x-api-key: $METABASE_TOKEN" | jq '.[] | {id, name, member_count}'

20. Get Table Metadata

Retrieve metadata for a specific table including columns and types.

curl -s "$METABASE_BASE_URL/api/table/TABLE_ID/query_metadata" --header "x-api-key: $METABASE_TOKEN" | jq '{name, fields: [.fields[] | {name, base_type, semantic_type}]}'

Guidelines
Instance URL: Set METABASE_BASE_URL to your Metabase instance URL
API keys vs sessions: API keys (via x-api-key header) are recommended over session tokens for programmatic access
Database IDs: Most query operations require a database ID. Use the list databases endpoint to find IDs
Native vs structured queries: The dataset endpoint supports both native (raw SQL) and query (structured MBQL) query types
Card terminology: In the Metabase API, "cards" refer to saved questions, not dashboard cards. Dashboard cards are referred to as "dashcards"
Collection organization: Use collections to organize dashboards and cards. The root collection has id: "root"
Query results format: Query results include data.cols (column metadata) and data.rows (row data as arrays)
Live API docs: Access interactive OpenAPI documentation at your instance's /api/docs endpoint for the complete API reference
Weekly Installs
39
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