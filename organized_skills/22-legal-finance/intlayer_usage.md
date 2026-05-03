---
rating: ⭐⭐
title: intlayer-usage
url: https://skills.sh/aymericzip/intlayer/intlayer-usage
---

# intlayer-usage

skills/aymericzip/intlayer/intlayer-usage
intlayer-usage
Installation
$ npx skills add https://github.com/aymericzip/intlayer --skill intlayer-usage
SKILL.md
Intlayer Usage

To use Intlayer effectively:

Retrieve Locales: Check intlayer.config.{ts,js,json,json5,jsonc,cjs,mjs}, .intlayerrc to see the configured locales.

Declare Content: We recommend creating one content declaration file per component, located alongside the component file. This keeps translations close to the code.

Consume Content: Use the provided hooks and functions to access your content.

Intlayer Exports
React Intlayer Exports

Common Packages:

intlayer: Core package for content declaration and utility functions.
react-intlayer: React components and hooks (e.g., useIntlayer).
vite-intlayer: Vite plugin for integration.

CLI Commands: Useful commands for managing your content:

npx intlayer build: Build the dictionaries from your content declarations.
References
Get Started
How Intlayer Works
Why Intlayer
Per-locale File
Website
Doc
Weekly Installs
33
Repository
aymericzip/intlayer
GitHub Stars
692
First Seen
Feb 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketFail
SnykPass