---
rating: ⭐⭐⭐
title: typo3-ckeditor5
url: https://skills.sh/netresearch/typo3-ckeditor5-skill/typo3-ckeditor5
---

# typo3-ckeditor5

skills/netresearch/typo3-ckeditor5-skill/typo3-ckeditor5
typo3-ckeditor5
Installation
$ npx skills add https://github.com/netresearch/typo3-ckeditor5-skill --skill typo3-ckeditor5
SKILL.md
TYPO3 CKEditor 5 Skill

CKEditor 5 integration patterns for TYPO3: custom plugins, configuration, and migration.

Expertise Areas
Architecture: Plugin system, schema/conversion, commands, UI components
TYPO3 Integration: YAML configuration, plugin registration, content elements
Migration: CKEditor 4->5 complete rewrite (no compatibility layer exists)
Reference Files
references/ckeditor5-architecture.md - Core MVC, schema, conversion
references/typo3-integration.md - TYPO3-specific patterns
references/plugin-development.md - Custom plugin guide
references/migration-guide.md - CKEditor 4->5 migration
Quick Reference
Plugin Registration (ext_localconf.php)
$GLOBALS['TYPO3_CONF_VARS']['RTE']['Presets']['my_preset'] = 'EXT:my_ext/Configuration/RTE/MyPreset.yaml';
$GLOBALS['TYPO3_CONF_VARS']['SYS']['ckeditor5']['plugins']['my-plugin'] = [
    'entryPoint' => 'EXT:my_ext/Resources/Public/JavaScript/Ckeditor/my-plugin.js',
];

Plugin Structure (Editing/UI Split Required)
packages/my-plugin/src/
├── myplugin.js           # Main: requires Editing + UI
├── mypluginediting.js    # Schema, converters, commands
├── mypluginui.js         # Toolbar buttons (ButtonView, componentFactory)
└── myplugincommand.js    # Command: execute() + refresh()

Key Patterns
// Schema: always register with allowIn/allowAttributes
schema.register('myElement', { inheritAllFrom: '$block', allowAttributes: ['type'] });

// Converters: both upcast + downcast required
conversion.for('upcast').elementToElement({ view: { name: 'div', classes: 'my-el' }, model: 'myElement' });
conversion.for('downcast').elementToElement({ model: 'myElement', view: 'div' });

// Command: must implement execute() AND refresh()
class MyCommand extends Command {
  refresh() { this.isEnabled = /* check model state */; }
  execute() { this.editor.model.change(writer => { /* ... */ }); }
}

jQuery Removal (Critical)

TYPO3 backend JS is dropping jQuery without deprecation period. CKEditor 5 plugins must use native APIs only:

querySelector/querySelectorAll instead of $()
fetch() + async/await instead of $.ajax/$.getJSON
Promise instead of $.Deferred
Backend Integration

Property name mismatch is the #1 bug. Frontend JS must match exact backend response property names.

// Backend returns: { content: "...", model: "...", usage: {...} }
const text = result.content;  // CORRECT (not result.completion)

Migration (CKE4 -> CKE5)

CKEditor 5 is a complete rewrite -- no compatibility layer. Migration requires full plugin rewrite:

 Audit CKE4 plugins, map features to CKE5 equivalents
 Convert CKEDITOR.plugins.add() to class-based extends Plugin
 Replace editor.widgets.add() with schema + converters + commands
 Convert PageTSConfig to YAML preset (Configuration/RTE/*.yaml)
 Use ES6 modules (no AMD/CommonJS)
 Remove all jQuery dependencies
 Verify backend response property names match frontend usage
Verification
./scripts/verify-ckeditor5.sh /path/to/extension


Contributing: https://github.com/netresearch/typo3-ckeditor5-skill

Weekly Installs
23
Repository
netresearch/typ…r5-skill
GitHub Stars
2
First Seen
Mar 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass