---
rating: ⭐⭐
title: react-native-reusables
url: https://skills.sh/hairyf/skills/react-native-reusables
---

# react-native-reusables

skills/hairyf/skills/react-native-reusables
react-native-reusables
Installation
$ npx skills add https://github.com/hairyf/skills --skill react-native-reusables
SKILL.md

The skill is based on React Native Reusables (docs as of 2026-02-26), generated at 2026-02-26.

React Native Reusables brings the shadcn/ui experience to React Native: copy-paste or CLI-scaffolded components, theming via CSS variables, and RN Primitives under the hood. It supports Nativewind and Uniwind, requires a root PortalHost for overlays, and uses a Text inheritance system and an Icon wrapper for Lucide.

Core References
Topic	Description	Reference
Overview	What RNR is, differences from shadcn/ui (portals, no cascade, icons, etc.)	core-overview
Installation	CLI init vs manual setup, adding components, PortalHost, dependencies	core-installation
Customization	components.json, global.css, tailwind.config, theme.ts	core-customization
Features
Components and patterns
Topic	Description	Reference
Components overview	Button, Input, Dialog, variants, asChild, compound components	features-components-overview
Text and icons	TextClassContext inheritance, Icon wrapper with Lucide	features-text-and-icons
Forms & controls	Label, Input, Select, Checkbox, RadioGroup, compound pattern	features-forms-controls
Overlays & portals	PortalHost, Dialog/Popover/SelectContent, contentInsets	features-overlays-portals
Registry and CLI	init, add, doctor; custom registry and registryDependencies	features-registry-cli
Blocks	Auth blocks, Clerk integration, adding blocks via CLI	features-blocks
Best practices
Topic	Description	Reference
Adding components	Prefer CLI, PortalHost placement, path aliases, cn helper, manual copy	best-practices-adding-components
Troubleshooting	doctor, --log-level all, PortalHost, aliases, dependencies	best-practices-troubleshooting
Weekly Installs
142
Repository
hairyf/skills
GitHub Stars
15
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass