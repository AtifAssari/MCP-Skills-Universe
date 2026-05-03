---
title: hyva-cms-components-dump
url: https://skills.sh/hyva-themes/hyva-ai-tools/hyva-cms-components-dump
---

# hyva-cms-components-dump

skills/hyva-themes/hyva-ai-tools/hyva-cms-components-dump
hyva-cms-components-dump
Installation
$ npx skills add https://github.com/hyva-themes/hyva-ai-tools --skill hyva-cms-components-dump
SKILL.md
Hyvä CMS Component Dump

Locates all components.json files from Hyvä CMS modules and outputs a merged JSON object containing all component definitions from active modules.

Usage

Important: Execute this script from the Magento project root directory.

Run the dump script:

php <skill_path>/scripts/dump_cms_components.php


Where <skill_path> is the directory containing this SKILL.md file (e.g., .claude/skills/hyva-cms-components-dump).

Output format: A single JSON object containing all merged CMS component definitions.

How It Works
Reads module configuration from app/etc/config.php to get the ordered list of modules
Filters active modules - only modules with value 1 are included (disabled modules are skipped)
Locates components.json files in:
app/code/{Vendor}/{Module}/etc/hyva_cms/components.json
vendor/{vendor-name}/{package-name}/*/etc/hyva_cms/components.json
Maps paths to module names by reading each module's etc/module.xml
Merges JSON objects in module load order as declared in config.php
Outputs the result as formatted JSON
Module Load Order

Components are merged in the exact order modules appear in app/etc/config.php. Later modules can override components from earlier modules by using the same component key.

Example Output
{
    "text_block": {
        "label": "Text Block",
        "category": "Content",
        "template": "Hyva_CmsBase::elements/text-block.phtml",
        ...
    },
    "feature_card": {
        "label": "Feature Card",
        "category": "Elements",
        "template": "Custom_Module::elements/feature-card.phtml",
        ...
    }
}

Integration with Other Skills

This skill can be used to:

Debug which components are available in the CMS editor
Verify component registration after creating new components
Check for component name conflicts between modules
Export component definitions for documentation
Weekly Installs
282
Repository
hyva-themes/hyv…ai-tools
GitHub Stars
65
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass