---
title: vicinae
url: https://skills.sh/knoopx/pi/vicinae
---

# vicinae

skills/knoopx/pi/vicinae
vicinae
Installation
$ npx skills add https://github.com/knoopx/pi --skill vicinae
SKILL.md
Vicinae Extensions

Extensions for Vicinae launcher using TypeScript and React.

Contents
Core Concepts
Quick Start
Project Structure
Command Types
Development Workflow
Advanced: UX Patterns
Advanced: API Reference
Advanced: Keyboard Shortcuts
Core Concepts
Concept	Description
Extension	Package adding commands to the launcher
View Command	Displays React UI (mode: "view")
No-View Command	Executes action without UI (mode: "no-view")
Manifest	package.json with extension metadata
Quick Start

Recommended: Use Vicinae's built-in "Create Extension" command.

Manual:

mkdir my-extension && cd my-extension
npm init -y
npm install @vicinae/api typescript @types/react @types/node
mkdir src && touch src/command.tsx

Project Structure
my-extension/
├── package.json          # Manifest with commands
├── tsconfig.json
├── src/
│   ├── command.tsx       # View commands
│   └── action.ts         # No-view commands
└── assets/               # Icons

Manifest (package.json)
{
  "name": "my-extension",
  "title": "My Extension",
  "version": "1.0.0",
  "commands": [
    {
      "name": "my-command",
      "title": "My Command",
      "description": "What this command does",
      "mode": "view"
    }
  ],
  "dependencies": {
    "@vicinae/api": "^0.8.2"
  }
}

Command Types
View Command (src/command.tsx)
import { List, ActionPanel, Action, Icon } from "@vicinae/api";

export default function MyCommand() {
  return (
    <List searchBarPlaceholder="Search items...">
      <List.Item
        title="Item"
        icon={Icon.Document}
        actions={
          <ActionPanel>
            <Action
              icon={Icon.Eye}
              title="View"
              onAction={() => console.log("viewed")}
            />
          </ActionPanel>
        }
      />
    </List>
  );
}


Important: All actions must have an icon prop.

No-View Command (src/action.ts)
import { showToast } from "@vicinae/api";

export default async function QuickAction() {
  await showToast({ title: "Done!" });
}

Development Workflow
npm run build         # Production build
npx tsc --noEmit      # Type check

# Run Vicinae dev server in tmux
# Creates the session only if it does not exist
tmux has -t vicinae-dev || tmux new-session -d -s vicinae-dev 'bunx vici develop'

# Read logs
tmux capture-pane -t vicinae-dev -p -S -

Common APIs
import {
  // UI Components
  List,
  Detail,
  Form,
  Grid,
  ActionPanel,
  Action,
  Icon,
  Color,
  // Utilities
  showToast,
  Toast,
  Clipboard,
  open,
  closeMainWindow,
  getPreferenceValues,
  useNavigation,
} from "@vicinae/api";

Keyboard Shortcuts

Common shortcuts: Ctrl+R (refresh), Ctrl+N (new), Ctrl+E (edit), Shift+Delete (delete).

See Keyboard Shortcuts for full reference and implementation examples.

Navigation
function ListView() {
  const { push, pop } = useNavigation();

  return (
    <List.Item
      title="Go to Detail"
      icon={Icon.Document}
      actions={
        <ActionPanel>
          <Action
            icon={Icon.Eye}
            title="View"
            onAction={() => push(<DetailView />)}
          />
        </ActionPanel>
      }
    />
  );
}

Preferences

Define in manifest:

{
  "preferences": [
    {
      "name": "apiKey",
      "title": "API Key",
      "type": "password",
      "required": true
    }
  ]
}


Access in code:

const { apiKey } = getPreferenceValues();

Related Skills
typescript: Type safety for extensions
Weekly Installs
31
Repository
knoopx/pi
GitHub Stars
45
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass