---
rating: ⭐⭐⭐⭐⭐
title: markdown-documentation
url: https://skills.sh/arielperez82/agents-and-skills/markdown-documentation
---

# markdown-documentation

skills/arielperez82/agents-and-skills/markdown-documentation
markdown-documentation
Installation
$ npx skills add https://github.com/arielperez82/agents-and-skills --skill markdown-documentation
SKILL.md
Markdown Documentation

Best practices for writing effective technical documentation in markdown.

README Structure
Minimal README
# Project Name

Brief description of what this project does.

## Installation

Instructions to install.

## Usage

Basic usage example.

## License

MIT

Comprehensive README
# Project Name

![Build Status](badge-url)
![Version](badge-url)

One-paragraph description of the project.

## Features

- Feature one
- Feature two
- Feature three

## Installation

### Prerequisites

- Requirement 1
- Requirement 2

### Steps

Instructions...

## Usage

### Basic Example

Code example...

### Advanced Usage

More examples...

## Configuration

Configuration options...

## API Reference

API documentation...

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

## License

MIT License - see [LICENSE](LICENSE)

Document Organization
File Naming
docs/
├── README.md           # Entry point
├── CONTRIBUTING.md     # Contribution guidelines
├── CHANGELOG.md        # Version history
├── CODE_OF_CONDUCT.md  # Community guidelines
├── getting-started.md  # Onboarding guide
├── api/
│   ├── README.md       # API overview
│   └── endpoints.md    # Endpoint reference
└── guides/
    ├── installation.md
    └── configuration.md

Linking Between Documents
See the [installation guide](./guides/installation.md) for details.

For API reference, check [endpoints](./api/endpoints.md#authentication).

Writing Style
Be Concise
<!-- Bad -->
In order to install the application, you will need to run the following command.

<!-- Good -->
Install the application:

Use Active Voice
<!-- Bad -->
The configuration file should be created in the home directory.

<!-- Good -->
Create the configuration file in your home directory.

Address the Reader
<!-- Bad -->
Users can configure the timeout setting.

<!-- Good -->
You can configure the timeout setting.

Code Documentation
Inline Code vs Code Blocks
Use `npm install` to install dependencies.

For multiple commands, use a code block:

```bash
npm install
npm run build
npm start


### Command Examples

Show both command and output:

```bash
$ npm --version
10.2.0

Configuration Examples

Always show complete, valid examples:

Create config.json:

{
  "port": 3000,
  "debug": true,
  "database": {
    "host": "localhost",
    "name": "myapp"
  }
}

Admonitions and Callouts
GitHub-Style Alerts
> [!NOTE]
> Useful information that users should know.

> [!TIP]
> Helpful advice for doing things better.

> [!IMPORTANT]
> Key information users need to know.

> [!WARNING]
> Urgent info that needs immediate attention.

> [!CAUTION]
> Advises about risks or negative outcomes.

Custom Callouts (Emoji-Based)
⚠️ **Warning**: This action cannot be undone.

💡 **Tip**: Use environment variables for sensitive data.

📝 **Note**: This feature requires version 2.0+.

API Documentation
Endpoint Documentation
Create User

Creates a new user account.

Request: POST /api/users

Headers:

Header	Value	Required
Content-Type	application/json	✅
Authorization	Bearer {token}	✅

Body:

{
  "name": "John Doe",
  "email": "john@example.com"
}


Response (201):

{
  "id": "abc123",
  "name": "John Doe",
  "email": "john@example.com"
}


Error (400):

{
  "error": "Invalid email format"
}

Function Documentation
parseConfig(path, options?)

Parses a configuration file.

Parameters:

Name	Type	Default	Description
path	string	—	Path to config file
options.strict	boolean	false	Throw on unknown keys
options.env	boolean	true	Expand environment variables

Returns: Config - Parsed configuration object

Throws:

FileNotFoundError - Config file doesn't exist
ParseError - Invalid JSON/YAML syntax

Example:

const config = parseConfig('./config.json', { strict: true });

Changelogs
Keep a Changelog Format
# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added
- New feature X

### Changed
- Updated dependency Y

## [1.2.0] - 2024-01-15

### Added
- Feature A
- Feature B

### Fixed
- Bug in feature C

### Deprecated
- Old API endpoint

## [1.1.0] - 2024-01-01

### Added
- Initial release

Diagrams
Mermaid (GitHub Supported)
```mermaid
graph LR
    A[Start] --> B{Decision}
    B -->|Yes| C[Action 1]
    B -->|No| D[Action 2]
    C --> E[End]
    D --> E
```

ASCII Diagrams
```
┌─────────┐     ┌─────────┐     ┌─────────┐
│ Client  │────▶│ Server  │────▶│Database │
└─────────┘     └─────────┘     └─────────┘
```

Best Practices
Start with why: Explain what the project does and why it exists
Show, don't tell: Provide working code examples
Keep it current: Update docs when code changes
Test examples: Ensure code samples actually work
Use consistent terminology: Define terms and use them consistently
Provide context: Link to prerequisites and related docs
Consider your audience: Write for your users' skill level
Include troubleshooting: Document common errors and solutions
Common Documentation Files
File	Purpose
README.md	Project overview and quick start
CONTRIBUTING.md	How to contribute
CHANGELOG.md	Version history
LICENSE	Legal terms
CODE_OF_CONDUCT.md	Community guidelines
SECURITY.md	Security policy
SUPPORT.md	How to get help
Weekly Installs
13
Repository
arielperez82/ag…d-skills
First Seen
Mar 2, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass