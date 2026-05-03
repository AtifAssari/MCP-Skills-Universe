---
title: figma
url: https://skills.sh/johnlindquist/claude/figma
---

# figma

skills/johnlindquist/claude/figma
figma
Installation
$ npx skills add https://github.com/johnlindquist/claude --skill figma
SKILL.md
Figma Integration

Extract design data and generate code from Figma.

Prerequisites

Figma API token:

export FIGMA_ACCESS_TOKEN=figd_xxxxx


Get token from: Figma > Settings > Account > Personal Access Tokens

Optional: Install figma-export CLI for component/style exports:

bun add -g @figma-export/cli

CLI Reference (figma-export)

For exporting components and styles, use the CLI:

Export Components
# Export components to SVG
figma-export components FILE_KEY -o ./output

# With config file
figma-export use-config .figmaexportrc.js

Export Styles
# Export styles as CSS
figma-export styles FILE_KEY -o ./styles

Config File Example

Create .figmaexportrc.js:

module.exports = {
  commands: [
    ['components', {
      fileId: 'YOUR_FILE_KEY',
      onlyFromPages: ['Icons'],
      outputters: [
        require('@figma-export/output-components-as-svg')({
          output: './icons'
        })
      ]
    }]
  ]
};


Then run:

figma-export use-config

API Reference (curl)
Get File
FILE_KEY="your-file-key"  # From Figma URL
curl -H "X-Figma-Token: $FIGMA_ACCESS_TOKEN" \
  "https://api.figma.com/v1/files/$FILE_KEY" | jq

Get Specific Node
NODE_ID="1:2"  # Node ID from Figma
curl -H "X-Figma-Token: $FIGMA_ACCESS_TOKEN" \
  "https://api.figma.com/v1/files/$FILE_KEY/nodes?ids=$NODE_ID" | jq

Get Images
curl -H "X-Figma-Token: $FIGMA_ACCESS_TOKEN" \
  "https://api.figma.com/v1/images/$FILE_KEY?ids=$NODE_ID&format=png&scale=2" | jq

Get Comments
curl -H "X-Figma-Token: $FIGMA_ACCESS_TOKEN" \
  "https://api.figma.com/v1/files/$FILE_KEY/comments" | jq

Get File Versions
curl -H "X-Figma-Token: $FIGMA_ACCESS_TOKEN" \
  "https://api.figma.com/v1/files/$FILE_KEY/versions" | jq

Extract Design Tokens
Get Styles
curl -H "X-Figma-Token: $FIGMA_ACCESS_TOKEN" \
  "https://api.figma.com/v1/files/$FILE_KEY/styles" | jq

Extract Colors
#!/bin/bash
FILE_KEY=$1

# Get file with styles
STYLES=$(curl -sH "X-Figma-Token: $FIGMA_ACCESS_TOKEN" \
  "https://api.figma.com/v1/files/$FILE_KEY" | jq '.styles')

# Get style nodes
STYLE_IDS=$(echo $STYLES | jq -r 'keys | join(",")')

curl -sH "X-Figma-Token: $FIGMA_ACCESS_TOKEN" \
  "https://api.figma.com/v1/files/$FILE_KEY/nodes?ids=$STYLE_IDS" | \
  jq '.nodes | to_entries | map(select(.value.document.type == "RECTANGLE")) |
      map({
        name: .value.document.name,
        color: .value.document.fills[0].color
      })'

Extract Typography
curl -sH "X-Figma-Token: $FIGMA_ACCESS_TOKEN" \
  "https://api.figma.com/v1/files/$FILE_KEY" | \
  jq '[.. | objects | select(.type == "TEXT") |
      {
        name: .name,
        fontFamily: .style.fontFamily,
        fontSize: .style.fontSize,
        fontWeight: .style.fontWeight,
        lineHeight: .style.lineHeightPx
      }] | unique'

Component Inspection
List Components
curl -H "X-Figma-Token: $FIGMA_ACCESS_TOKEN" \
  "https://api.figma.com/v1/files/$FILE_KEY/components" | jq

Get Component Details
COMPONENT_ID="1:234"
curl -H "X-Figma-Token: $FIGMA_ACCESS_TOKEN" \
  "https://api.figma.com/v1/files/$FILE_KEY/nodes?ids=$COMPONENT_ID" | jq

Export Component as SVG
curl -H "X-Figma-Token: $FIGMA_ACCESS_TOKEN" \
  "https://api.figma.com/v1/images/$FILE_KEY?ids=$COMPONENT_ID&format=svg" | jq -r '.images | to_entries[0].value'

Generate Code
Design to Code with AI
# Get component node
NODE=$(curl -sH "X-Figma-Token: $FIGMA_ACCESS_TOKEN" \
  "https://api.figma.com/v1/files/$FILE_KEY/nodes?ids=$NODE_ID" | jq '.nodes | to_entries[0].value')

# Generate code
gemini -m pro -o text -e "" "Generate React component code from this Figma data:

$NODE

Requirements:
- Use Tailwind CSS
- TypeScript with proper types
- Match dimensions and spacing
- Include all text content
- Handle responsive behavior"

Extract Spacing Values
curl -sH "X-Figma-Token: $FIGMA_ACCESS_TOKEN" \
  "https://api.figma.com/v1/files/$FILE_KEY/nodes?ids=$NODE_ID" | \
  jq '[.. | objects | select(.type == "FRAME") |
      {
        name: .name,
        padding: {
          top: .paddingTop,
          right: .paddingRight,
          bottom: .paddingBottom,
          left: .paddingLeft
        },
        itemSpacing: .itemSpacing
      }]'

Workflow Patterns
Sync Design Tokens
#!/bin/bash
# figma-sync-tokens.sh

FILE_KEY=$1
OUTPUT=${2:-"tokens.json"}

# Fetch and extract
curl -sH "X-Figma-Token: $FIGMA_ACCESS_TOKEN" \
  "https://api.figma.com/v1/files/$FILE_KEY" | \
  jq '{
    colors: [.. | objects | select(.type == "RECTANGLE" and .name | startswith("color/")) |
      {name: .name, value: .fills[0].color}],
    typography: [.. | objects | select(.type == "TEXT" and .name | startswith("text/")) |
      {name: .name, font: .style}]
  }' > $OUTPUT

echo "Tokens saved to $OUTPUT"

Export Icons
#!/bin/bash
# export-icons.sh

FILE_KEY=$1
OUTPUT_DIR=${2:-"./icons"}

mkdir -p $OUTPUT_DIR

# Get all icon components
ICONS=$(curl -sH "X-Figma-Token: $FIGMA_ACCESS_TOKEN" \
  "https://api.figma.com/v1/files/$FILE_KEY/components" | \
  jq -r '.meta.components[] | select(.name | startswith("icon/")) | .node_id')

for icon_id in $ICONS; do
  # Get SVG URL
  SVG_URL=$(curl -sH "X-Figma-Token: $FIGMA_ACCESS_TOKEN" \
    "https://api.figma.com/v1/images/$FILE_KEY?ids=$icon_id&format=svg" | \
    jq -r '.images | to_entries[0].value')

  # Download
  NAME=$(echo $icon_id | tr ':' '-')
  curl -s "$SVG_URL" > "$OUTPUT_DIR/$NAME.svg"
  echo "Exported: $NAME.svg"
done

Best Practices
Use file key from URL - figma.com/file/FILEKEY/...
Cache responses - API has rate limits
Use node IDs - More efficient than full file
Extract at build time - Not runtime
Version your tokens - Track design changes
Validate extractions - Figma structure varies
Weekly Installs
23
Repository
johnlindquist/claude
GitHub Stars
23
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn