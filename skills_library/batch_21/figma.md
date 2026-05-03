---
title: figma
url: https://skills.sh/vm0-ai/vm0-skills/figma
---

# figma

skills/vm0-ai/vm0-skills/figma
figma
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill figma
SKILL.md
Troubleshooting

If requests fail, run zero doctor check-connector --env-name FIGMA_TOKEN or zero doctor check-connector --url https://api.figma.com/v1/me --method GET

How to Use

All examples assume FIGMA_TOKEN is set.

Base URL: https://api.figma.com/v1

1. Get Current User

Get information about the authenticated user (no parameters needed):

curl -s "https://api.figma.com/v1/me" --header "Authorization: Bearer $FIGMA_TOKEN" | jq '{id, email, handle, img_url}'

2. Get File

Retrieve complete file structure including frames, components, and styles.

Replace <file-key> with your actual file key from a Figma URL.

curl -s "https://api.figma.com/v1/files/<file-key>" --header "Authorization: Bearer $FIGMA_TOKEN" | jq '{name, lastModified, version, document: .document.children[0].name}'

3. Get File Nodes

Retrieve specific nodes from a file by node IDs.

Replace <file-key> with your file key and <node-id> with actual node IDs (comma-separated for multiple, e.g., 1:2,1:3).

curl -s "https://api.figma.com/v1/files/<file-key>/nodes?ids=<node-id>" --header "Authorization: Bearer $FIGMA_TOKEN" | jq '.nodes'


Node IDs can be found in the file structure or from the Figma URL ?node-id=X-Y parameter (convert - to :).

4. Get File Images

Export nodes as images in PNG, JPG, SVG, or PDF format.

Replace <file-key> with your file key and <node-id> with actual node IDs.

curl -s "https://api.figma.com/v1/images/<file-key>?ids=<node-id>&format=png&scale=2" --header "Authorization: Bearer $FIGMA_TOKEN" | jq '.images'


Parameters:

format: png, jpg, svg, pdf (default: png)
scale: 0.5, 1, 2, 4 (default: 1)
5. Get Image Fills

Get download URLs for all images used in a file.

Replace <file-key> with your file key.

curl -s "https://api.figma.com/v1/files/<file-key>/images" --header "Authorization: Bearer $FIGMA_TOKEN" | jq '.meta.images'

6. Get File Comments

List all comments on a file.

Replace <file-key> with your file key.

curl -s "https://api.figma.com/v1/files/<file-key>/comments" --header "Authorization: Bearer $FIGMA_TOKEN" | jq '.comments[] | {id, message: .message, user: .user.handle, created_at}'

7. Post Comment

Add a comment to a file. Figma requires client_meta with a node_id to anchor the comment.

Replace <file-key> with your file key and <node-id> with an actual node ID.

Write to /tmp/figma_comment.json:

{
  "message": "This looks great!",
  "client_meta": {
    "node_id": "<node-id>",
    "node_offset": { "x": 0, "y": 0 }
  }
}

curl -s -X POST "https://api.figma.com/v1/files/<file-key>/comments" --header "Authorization: Bearer $FIGMA_TOKEN" --header "Content-Type: application/json" -d @/tmp/figma_comment.json | jq '{id, message}'

8. Get File Versions

List version history of a file.

Replace <file-key> with your file key.

curl -s "https://api.figma.com/v1/files/<file-key>/versions" --header "Authorization: Bearer $FIGMA_TOKEN" | jq '.versions[] | {id, created_at, label, description, user: .user.handle}'

9. Get Project Files

List all files in a project.

Replace <project-id> with your project ID. Project IDs can be found in Figma URLs or from team project listings.

curl -s "https://api.figma.com/v1/projects/<project-id>/files" --header "Authorization: Bearer $FIGMA_TOKEN" | jq '.files[] | {key, name, last_modified}'

10. Get Component Sets

Get component sets (variants) in a file.

Replace <file-key> with your file key.

curl -s "https://api.figma.com/v1/files/<file-key>/component_sets" --header "Authorization: Bearer $FIGMA_TOKEN" | jq '.meta.component_sets[] | {key, name, description}'

11. Get Component

Get metadata for a specific component.

Replace <component-key> with your component key from the component sets output.

curl -s "https://api.figma.com/v1/components/<component-key>" --header "Authorization: Bearer $FIGMA_TOKEN" | jq '{key, name, description, containing_frame}'

Understanding File Structure

Figma files have a hierarchical structure:

FILE
└── CANVAS (page)
    ├── FRAME
    │   ├── RECTANGLE
    │   ├── TEXT
    │   └── GROUP
    │       └── VECTOR
    └── FRAME
        └── COMPONENT


Common node types: CANVAS, FRAME, GROUP, VECTOR, BOOLEAN_OPERATION, STAR, LINE, ELLIPSE, REGULAR_POLYGON, RECTANGLE, TEXT, SLICE, COMPONENT, COMPONENT_SET, INSTANCE

Guidelines
Start with /v1/me: Always verify auth first before calling other endpoints
File key from URL: Extract the file key from Figma URLs (/design/<file-key>/...)
Node IDs: Node IDs are in format X:Y (e.g., 1:2) — in URLs they appear as X-Y, convert - to :
Rate limits: 60 requests per minute; implement backoff for 429 responses
Optimize exports: Use appropriate scale and format for image exports
Pagination: Some endpoints return paginated results; check for next_page in responses
Weekly Installs
73
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn