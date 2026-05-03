---
rating: ⭐⭐⭐
title: inktui
url: https://skills.sh/delexw/claude-code-misc/inktui
---

# inktui

skills/delexw/claude-code-misc/inktui
inktui
Installation
$ npx skills add https://github.com/delexw/claude-code-misc --skill inktui
SKILL.md
Ink — React for CLIs

Ink is a React renderer for terminal applications. It uses Yoga (flexbox) for layout and renders to stdout. Every element is a flex container — think <div style="display: flex"> for the terminal.

Quick Start
# Scaffold a new project
npx create-ink-app my-cli              # JavaScript
npx create-ink-app --typescript my-cli # TypeScript


Or add to an existing project:

npm install ink react
npm install @inkjs/ui  # Optional: pre-built UI components

Core Architecture

Ink apps are React component trees rendered via render(). The process stays alive while there's work in the event loop. Exit via Ctrl+C, useApp().exit(), or instance.unmount().

import React, {useState} from 'react';
import {render, Text, Box} from 'ink';

function App() {
  const [count, setCount] = useState(0);
  return (
    <Box flexDirection="column">
      <Text>Count: {count}</Text>
      <Text color="green">Press q to quit</Text>
    </Box>
  );
}

render(<App />);

Reference Files

Read these for detailed API documentation and examples:

references/components.md — All Ink core components (Box, Text, Newline, Spacer, Static, Transform) with full props
references/hooks.md — All hooks (useInput, useApp, useFocus, useFocusManager, useStdin, useStdout, useStderr, useWindowSize, useBoxMetrics, useCursor, usePaste)
references/ink-ui.md — All @inkjs/ui components (TextInput, Select, MultiSelect, Spinner, ProgressBar, Alert, Badge, StatusMessage, ConfirmInput, EmailInput, PasswordInput, OrderedList, UnorderedList) with props and theming
references/patterns.md — Common patterns: multi-step wizards, loading states, tables, command routing, testing, fullscreen apps, and real-world examples
Key Concepts
Layout is Flexbox

Every element is a flex container. Use <Box> for layout with standard flex props: flexDirection, justifyContent, alignItems, gap, padding, margin, etc. Percentage widths/heights are supported.

Text Must Be in <Text>

All string content must be wrapped in <Text>. Direct string children of <Box> will error. Nest <Text> inside <Text> for inline styling:

<Text>
  Hello <Text bold color="green">World</Text>
</Text>

<Static> for Permanent Output

Use <Static> for output that should persist above the interactive area (like log lines). Content rendered in <Static> is written once and never re-rendered:

<Static items={logs}>
  {(log, i) => <Text key={i}>{log}</Text>}
</Static>

Input Handling

Use useInput hook — not DOM events:

import {useInput, useApp} from 'ink';

function App() {
  const {exit} = useApp();
  useInput((input, key) => {
    if (input === 'q') exit();
    if (key.return) handleSubmit();
  });
  return <Text>Press q to quit</Text>;
}

Borders

<Box> supports border styles: "single", "double", "round", "bold", "singleDouble", "doubleSingle", "classic".

<Box borderStyle="round" borderColor="green" padding={1}>
  <Text>Bordered content</Text>
</Box>

Testing

Use ink-testing-library:

import {render} from 'ink-testing-library';

const {lastFrame, stdin} = render(<App />);
expect(lastFrame()).toContain('Hello');
stdin.write('q'); // simulate input

render() Options
const instance = render(<App />, {
  stdout: process.stdout,        // custom writable stream
  stdin: process.stdin,          // custom readable stream
  stderr: process.stderr,        // custom writable stream
  exitOnCtrlC: true,             // default
  patchConsole: true,            // intercept console.log
  debug: false,
  maxFps: 30,
  incrementalRendering: false,   // only re-render changed lines
  concurrent: false,             // React concurrent mode (Suspense, useTransition)
  interactive: true,             // auto-detected; false in CI
  isScreenReaderEnabled: false,  // or set INK_SCREEN_READER=true
  onRender: ({renderTime}) => {},// callback after each render
  kittyKeyboard: {mode: 'auto'}, // 'auto' | 'enabled' | 'disabled'
});

await instance.waitUntilExit();

renderToString() for Snapshots
import {renderToString} from 'ink';
const output = renderToString(<App />, {columns: 80});

Common Mistakes to Avoid
Bare strings in <Box> — Always wrap text in <Text>
Using DOM events — Use useInput hook instead
Forgetting key prop in <Static> — Items need unique keys
Not handling raw mode — useInput requires raw mode (automatic in render(), but manual in tests)
Infinite re-renders — Same React rules apply; memoize callbacks, avoid setting state in render
Multiple active inputs — Use isDisabled prop on ink-ui components or isActive on useInput/useFocus to manage which component receives input
Weekly Installs
9
Repository
delexw/claude-code-misc
GitHub Stars
1
First Seen
Mar 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass