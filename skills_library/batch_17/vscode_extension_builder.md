---
title: vscode-extension-builder
url: https://skills.sh/kjgarza/marketplace-claude/vscode-extension-builder
---

# vscode-extension-builder

skills/kjgarza/marketplace-claude/vscode-extension-builder
vscode-extension-builder
Installation
$ npx skills add https://github.com/kjgarza/marketplace-claude --skill vscode-extension-builder
SKILL.md
VS Code Extension Builder

Build professional VS Code extensions with proper architecture, best practices, and complete tooling support.

Quick Start

For immediate extension creation:

Initialize: Run npx --package yo --package generator-code -- yo code
Choose type: New Extension (TypeScript)
Fill details: Name, identifier, description
Develop: Open in VS Code, press F5 to debug
Test: Run commands in Extension Development Host
Package: Run vsce package when ready

For detailed guidance, follow the workflow below.

Extension Types

Choose the type that matches your needs:

Command Extension: Add commands to Command Palette (simplest, most common)
Language Support: Syntax highlighting, IntelliSense, formatting
Webview Extension: Custom UI panels with HTML/CSS/JS
Tree View: Custom sidebar views with hierarchical data
Debugger: Add debugging support for languages
Theme: Color themes, file icon themes
Snippet Provider: Code snippets for languages
Core Workflow
1. Gather Requirements

Ask user about:

Purpose: What should the extension do?
Type: Which extension type? (command, language, webview, etc.)
Features: Specific functionality needed
UI: Commands, views, panels, status bar items?
Activation: When should it activate?
2. Choose Extension Type & Architecture

Based on requirements, select appropriate pattern:

Simple Command Extension (most common):

Single responsibility
Command Palette integration
Quick to build

Language Extension:

Syntax highlighting (TextMate grammar)
Language server for IntelliSense
Complex but powerful

Webview Extension:

Custom UI needed
Rich interactions
More complex state management

See extension-anatomy.md for detailed structure.

3. Initialize Project

Option A: Use Yeoman Generator (Recommended)

npx --package yo --package generator-code -- yo code


Fill in:

Type: New Extension (TypeScript)
Name: User-friendly name
Identifier: lowercase-with-hyphens
Description: Clear purpose
Git: Yes
Bundler: esbuild (recommended) or webpack
Package manager: npm

Option B: Use Templates

For specific patterns, copy from assets/templates/:

command-extension/ - Command-based extension
language-support/ - Language extension starter
webview-extension/ - Webview-based extension
4. Implement Core Functionality

For Command Extensions:

Define command in package.json:
{
  "contributes": {
    "commands": [{
      "command": "extension.commandId",
      "title": "Command Title"
    }]
  }
}

Register command in extension.ts:
export function activate(context: vscode.ExtensionContext) {
  let disposable = vscode.commands.registerCommand('extension.commandId', () => {
    vscode.window.showInformationMessage('Hello from Extension!');
  });
  context.subscriptions.push(disposable);
}


For Language Extensions: See common-apis.md for language features APIs.

For Webview Extensions: See common-apis.md for webview creation patterns.

5. Configure Activation & Contributions

Activation Events determine when your extension loads:

onCommand: When command is invoked
onLanguage: When file type opens
onView: When tree view becomes visible
*: On startup (avoid if possible)

See activation-events.md for complete reference.

Contributions declare extension capabilities in package.json:

commands: Command Palette entries
menus: Context menu items
keybindings: Keyboard shortcuts
languages: Language support
views: Tree views
configuration: Settings
6. Test & Debug

Local Testing:

Press F5 in VS Code to launch Extension Development Host
Test commands and features
Check Debug Console for logs
Set breakpoints for debugging

Automated Testing:

Unit tests: Test business logic
Integration tests: Test VS Code API interactions
Use @vscode/test-electron for testing

Common Issues:

Command not appearing: Check contributes.commands and activation events
Extension not activating: Verify activation events in package.json
API errors: Check VS Code API version compatibility
7. Package & Distribute

Prepare for Publishing:

Update README.md with features and usage
Add extension icon (128x128 PNG)
Set repository URL in package.json
Add LICENSE file
Test thoroughly

Package Extension:

npm install -g @vscode/vsce
vsce package


Creates .vsix file for distribution.

Publish to Marketplace:

vsce publish


Requires Azure DevOps personal access token.

Common Patterns
Pattern 1: Simple Command

Quick command that shows information:

vscode.commands.registerCommand('extension.showInfo', () => {
  vscode.window.showInformationMessage('Information message');
});

Pattern 2: Command with User Input

Get input before executing:

vscode.commands.registerCommand('extension.greet', async () => {
  const name = await vscode.window.showInputBox({
    prompt: 'Enter your name'
  });
  if (name) {
    vscode.window.showInformationMessage(`Hello, ${name}!`);
  }
});

Pattern 3: File Operation Command

Work with active editor:

vscode.commands.registerCommand('extension.processFile', () => {
  const editor = vscode.window.activeTextEditor;
  if (!editor) {
    vscode.window.showErrorMessage('No active editor');
    return;
  }
  
  const document = editor.document;
  const text = document.getText();
  // Process text...
});

Pattern 4: Status Bar Item

Show persistent status:

const statusBarItem = vscode.window.createStatusBarItem(
  vscode.StatusBarAlignment.Right,
  100
);
statusBarItem.text = "$(check) Ready";
statusBarItem.show();
context.subscriptions.push(statusBarItem);

Reference Navigation

Load these references as needed:

extension-anatomy.md: When you need details about:

Extension structure and file organization
package.json manifest fields
Entry point and lifecycle hooks
Extension context and disposables

common-apis.md: When implementing:

Window and editor operations
Workspace and file system access
Language features (IntelliSense, diagnostics)
Webview creation and messaging
Tree views and custom UI

activation-events.md: When configuring:

When extension should load
Performance optimization
Lazy loading strategies

best-practices.md: When considering:

UX guidelines and design patterns
Performance optimization
Security considerations
Testing strategies
Publishing guidelines
Key Principles
Performance
Lazy load: Use specific activation events, not *
Async operations: Use async/await for I/O
Dispose resources: Clean up subscriptions
Minimize startup: Defer heavy operations
User Experience
Clear commands: Descriptive titles and categories
Feedback: Show progress for long operations
Error handling: Helpful error messages
Consistent UI: Follow VS Code conventions
Code Quality
TypeScript: Use strict mode for type safety
Error handling: Try-catch for all operations
Logging: Use console.log for debugging
Testing: Write tests for critical functionality
Troubleshooting
Extension Not Appearing
Verify package.json syntax (valid JSON)
Check main field points to compiled output
Ensure activation events are correct
Reload window: Developer: Reload Window
Command Not Working
Check command ID matches in package.json and code
Verify activation event includes the command
Check Debug Console for errors
Ensure command is registered in activate()
Build Errors
Run npm install to install dependencies
Check TypeScript configuration
Verify VS Code API version compatibility
Update @types/vscode if needed
Examples by Use Case
Add Command to Format Code
Type: Command extension
Activation: onCommand
Implementation: Get editor text, format, replace
UI: Command Palette entry
Add Syntax Highlighting
Type: Language extension
Activation: onLanguage:mylang
Implementation: TextMate grammar in JSON
UI: Automatic on file open
Add Custom Sidebar View
Type: Tree view extension
Activation: onView:myView
Implementation: TreeDataProvider interface
UI: Activity bar icon + sidebar panel
Add Quick Pick Menu
Type: Command extension with UI
Activation: onCommand
Implementation: showQuickPick with items
UI: Searchable dropdown menu
Resources in This Skill
references/: Detailed documentation (load as needed)
assets/templates/: Starting templates for common patterns
Official docs: https://code.visualstudio.com/api
Related Skills

For code quality and architecture review of your extension code:

detect-code-smells: Check extension code quality
security-pattern-check: Security review for extensions
suggest-performance-fix: Optimize extension performance
Notes

This skill provides the complete workflow for VS Code extension development, from initial concept to published extension. Use progressive disclosure: start with Quick Start for simple cases, dive into references for complex requirements. Templates in assets/ provide copy-paste starting points for common patterns.

Weekly Installs
94
Repository
kjgarza/marketp…e-claude
GitHub Stars
2
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass