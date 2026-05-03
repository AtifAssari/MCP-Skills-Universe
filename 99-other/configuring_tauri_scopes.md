---
title: configuring-tauri-scopes
url: https://skills.sh/dchuk/claude-code-tauri-skills/configuring-tauri-scopes
---

# configuring-tauri-scopes

skills/dchuk/claude-code-tauri-skills/configuring-tauri-scopes
configuring-tauri-scopes
Installation
$ npx skills add https://github.com/dchuk/claude-code-tauri-skills --skill configuring-tauri-scopes
SKILL.md
Tauri Command Scopes

This skill covers configuring scopes in Tauri v2 applications to control fine-grained access to commands and resources.

What Are Scopes?

Scopes are a granular authorization mechanism in Tauri that controls what specific operations a command can perform. They function as fine-grained permission boundaries beyond basic command access.

Key Characteristics
Allow scopes: Explicitly permit certain operations
Deny scopes: Explicitly restrict certain operations
Deny takes precedence: When both exist, deny rules always win
Command responsibility: The command implementation must validate and enforce scope restrictions
How Scopes Work

The scope is passed to the command during execution. The command implementation is responsible for validating against the scope and enforcing restrictions. This means developers must carefully implement scope validation to prevent bypasses.

Scope Configuration Location

Scopes are configured in capability files located at:

src-tauri/capabilities/default.json (primary)
src-tauri/capabilities/*.json (additional capability files)
Filesystem Scopes

The filesystem plugin uses glob-compatible path patterns to define accessible paths.

Basic Filesystem Scope Configuration
{
  "$schema": "../gen/schemas/desktop-schema.json",
  "identifier": "default",
  "description": "Default capability for the application",
  "windows": ["main"],
  "permissions": [
    {
      "identifier": "fs:scope",
      "allow": [{ "path": "$APPDATA" }, { "path": "$APPDATA/**" }]
    }
  ]
}

Command-Specific Scopes

Restrict individual filesystem operations rather than global access:

{
  "permissions": [
    {
      "identifier": "fs:allow-read-text-file",
      "allow": [{ "path": "$DOCUMENT/**" }]
    },
    {
      "identifier": "fs:allow-write-text-file",
      "allow": [{ "path": "$HOME/notes.txt" }]
    }
  ]
}

Combined Allow and Deny Scopes
{
  "permissions": [
    {
      "identifier": "fs:allow-rename",
      "allow": [{ "path": "$HOME/**" }],
      "deny": [{ "path": "$HOME/.config/**" }]
    }
  ]
}

Available Path Variables

Tauri provides runtime-injected variables for common system directories:

Variable	Description
$APPCONFIG	Application config directory
$APPDATA	Application data directory
$APPLOCALDATA	Application local data directory
$APPCACHE	Application cache directory
$APPLOG	Application log directory
$AUDIO	User audio directory
$CACHE	System cache directory
$CONFIG	System config directory
$DATA	System data directory
$DESKTOP	User desktop directory
$DOCUMENT	User documents directory
$DOWNLOAD	User downloads directory
$EXE	Application executable directory
$HOME	User home directory
$PICTURE	User pictures directory
$PUBLIC	Public directory
$RESOURCE	Application resource directory
$TEMP	Temporary directory
$VIDEO	User video directory
Scope Patterns

Scopes support glob patterns for flexible path matching.

Pattern Examples
{
  "permissions": [
    {
      "identifier": "fs:scope",
      "allow": [
        { "path": "$APPDATA/databases/*" },
        { "path": "$DOCUMENT/**/*.txt" },
        { "path": "$HOME/project/src/**" }
      ],
      "deny": [
        { "path": "$HOME/.ssh/**" },
        { "path": "$HOME/.gnupg/**" }
      ]
    }
  ]
}

Pattern Syntax
Pattern	Meaning
*	Matches any characters except path separator
**	Matches any characters including path separator (recursive)
?	Matches a single character
[abc]	Matches any character in brackets
Path Traversal Prevention

Tauri prevents path traversal attacks. These paths are NOT allowed:

/usr/path/to/../file
../path/to/file
HTTP Plugin Scopes

The HTTP plugin uses URL patterns to control network access.

URL Scope Configuration
{
  "permissions": [
    {
      "identifier": "http:default",
      "allow": [{ "url": "https://*.tauri.app" }],
      "deny": [{ "url": "https://private.tauri.app" }]
    }
  ]
}

URL Pattern Examples
{
  "permissions": [
    {
      "identifier": "http:default",
      "allow": [
        { "url": "https://api.example.com/*" },
        { "url": "https://*.cdn.example.com/**" }
      ]
    }
  ]
}

Defining Custom Permissions with Scopes (TOML)

For plugins or custom commands, define permissions in TOML files.

Basic Permission with Scope
# permissions/my-permission.toml
[[permission]]
identifier = "scope-appdata-recursive"
description = "Recursive access to APPDATA folder"

[[permission.scope.allow]]
path = "$APPDATA/**"

Permission with Deny Scope
[[permission]]
identifier = "deny-sensitive-data"
description = "Denies access to sensitive directories"
platforms = ["linux", "macos"]

[[permission.scope.deny]]
path = "$HOME/.ssh/**"

[[permission.scope.deny]]
path = "$HOME/.gnupg/**"

Permission Sets

Combine permissions into reusable sets:

[[set]]
identifier = "safe-appdata-access"
description = "Allows APPDATA access while denying sensitive folders"
permissions = ["scope-appdata-recursive", "deny-sensitive-data"]

Dynamic Scopes (Runtime Management)

Tauri allows runtime scope modification using the FsExt trait from Rust.

Basic Runtime Scope Expansion
use tauri_plugin_fs::FsExt;

pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_fs::init())
        .setup(|app| {
            let scope = app.fs_scope();
            // Allow a specific directory (non-recursive)
            scope.allow_directory("/path/to/directory", false)?;
            // Check what's currently allowed
            dbg!(scope.allowed());
            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}

Tauri Command for Scope Expansion
use tauri_plugin_fs::FsExt;

#[tauri::command]
fn expand_scope(
    app_handle: tauri::AppHandle,
    folder_path: std::path::PathBuf
) -> Result<(), String> {
    // Verify path before expanding scope
    if !folder_path.exists() {
        return Err("Path does not exist".to_string());
    }

    // true = allow inner directories recursively
    app_handle
        .fs_scope()
        .allow_directory(&folder_path, true)
        .map_err(|err| err.to_string())
}

Allow Specific File
#[tauri::command]
fn allow_file(
    app_handle: tauri::AppHandle,
    file_path: std::path::PathBuf
) -> Result<(), String> {
    app_handle
        .fs_scope()
        .allow_file(&file_path)
        .map_err(|err| err.to_string())
}

Security Warning

Dynamic scope expansion should be used carefully:

Validate paths before expanding scope
Prefer static configuration when possible
Never expand scope based on unvalidated user input
Remote URL Scopes (Capabilities)

Control which remote URLs can access your application's commands.

{
  "identifier": "remote-api-access",
  "description": "Allow remote access from specific domains",
  "windows": ["main"],
  "remote": {
    "urls": ["https://*.mydomain.dev", "https://app.example.com"]
  },
  "permissions": ["core:default"]
}

Complete Capability File Example
{
  "$schema": "../gen/schemas/desktop-schema.json",
  "identifier": "default",
  "description": "Default capability for desktop application",
  "windows": ["main", "settings"],
  "platforms": ["linux", "macos", "windows"],
  "permissions": [
    "core:default",
    "core:window:allow-set-title",
    {
      "identifier": "fs:default"
    },
    {
      "identifier": "fs:allow-read-text-file",
      "allow": [
        { "path": "$DOCUMENT/**/*.md" },
        { "path": "$DOCUMENT/**/*.txt" }
      ]
    },
    {
      "identifier": "fs:allow-write-text-file",
      "allow": [{ "path": "$APPDATA/notes/**" }],
      "deny": [{ "path": "$APPDATA/notes/.secret/**" }]
    },
    {
      "identifier": "http:default",
      "allow": [{ "url": "https://api.example.com/*" }]
    }
  ]
}

Security Best Practices
Minimize scope: Only allow paths and URLs that are absolutely necessary
Use deny rules: Explicitly block sensitive directories even within allowed paths
Prefer command-specific scopes: Use fs:allow-read-text-file over global fs:scope
Validate dynamic scopes: Always verify paths before runtime scope expansion
Audit scope enforcement: Command developers must implement proper scope validation
Use path variables: Prefer $APPDATA over hardcoded paths for portability
Common Scope Patterns
Read-Only Application Data
{
  "permissions": [
    {
      "identifier": "fs:allow-read-text-file",
      "allow": [{ "path": "$APPDATA/**" }]
    },
    {
      "identifier": "fs:allow-exists",
      "allow": [{ "path": "$APPDATA/**" }]
    }
  ]
}

User Document Access
{
  "permissions": [
    {
      "identifier": "fs:scope",
      "allow": [{ "path": "$DOCUMENT/**" }],
      "deny": [
        { "path": "$DOCUMENT/.hidden/**" },
        { "path": "$DOCUMENT/**/*.key" }
      ]
    }
  ]
}

API-Only HTTP Access
{
  "permissions": [
    {
      "identifier": "http:default",
      "allow": [
        { "url": "https://api.myapp.com/v1/*" },
        { "url": "https://cdn.myapp.com/**" }
      ],
      "deny": [
        { "url": "https://api.myapp.com/v1/admin/*" }
      ]
    }
  ]
}

Troubleshooting
"Path not allowed on the configured scope"

This error indicates the requested path is outside the configured scope. Solutions:

Add the path to your capability's allow list
Check for typos in path variables
Verify glob patterns match the intended paths
Check if a deny rule is blocking the path
Testing Scope Configuration

Run in development mode to test permissions:

pnpm tauri dev
# or
cargo tauri dev


Permission errors will appear in the console indicating which permissions need configuration.

References
Command Scopes Documentation
Permissions Overview
Capabilities Reference
Filesystem Plugin
HTTP Plugin
Weekly Installs
57
Repository
dchuk/claude-co…i-skills
GitHub Stars
18
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass