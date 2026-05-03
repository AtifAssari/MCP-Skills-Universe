---
title: filament-plugin-scaffold
url: https://skills.sh/mwguerra/claude-code-plugins/filament-plugin-scaffold
---

# filament-plugin-scaffold

skills/mwguerra/claude-code-plugins/filament-plugin-scaffold
filament-plugin-scaffold
Installation
$ npx skills add https://github.com/mwguerra/claude-code-plugins --skill filament-plugin-scaffold
SKILL.md
Filament Plugin Scaffold Skill

Creates a complete Filament plugin skeleton (panel or standalone) following Filament's official plugin development guidelines.

Usage

When the user wants to create a Filament plugin, use the scaffold script:

python3 ${SKILL_DIR}/scripts/scaffold_filament_plugin.py <vendor/plugin-name> [options]

Options
--with-resource <name> - Include a sample Resource
--with-page - Include a sample custom Page
--with-widget - Include a sample Widget
--with-livewire - Include Livewire component structure
--with-pest - Include PestPHP testing (default: yes)
--no-pest - Exclude PestPHP testing
Examples
Basic Filament plugin
python3 ${SKILL_DIR}/scripts/scaffold_filament_plugin.py mwguerra/filament-blog

Plugin with Resource
python3 ${SKILL_DIR}/scripts/scaffold_filament_plugin.py mwguerra/filament-blog --with-resource Post

Full-featured plugin
python3 ${SKILL_DIR}/scripts/scaffold_filament_plugin.py mwguerra/filament-blog --with-resource Post --with-page --with-widget

What Gets Created
Directory Structure
packages/
└── vendor/
    └── filament-plugin-name/
        ├── composer.json
        ├── README.md
        ├── LICENSE
        ├── .gitignore
        ├── phpunit.xml
        ├── config/
        │   └── filament-plugin-name.php
        ├── database/
        │   └── migrations/
        │       └── .gitkeep
        ├── resources/
        │   ├── lang/
        │   │   └── en/
        │   │       └── messages.php
        │   └── views/
        │       └── .gitkeep
        ├── src/
        │   ├── PluginNamePlugin.php
        │   ├── PluginNameServiceProvider.php
        │   ├── Facades/
        │   │   └── PluginName.php
        │   ├── Resources/
        │   │   └── .gitkeep (or generated Resource)
        │   ├── Pages/
        │   │   └── .gitkeep (or generated Page)
        │   ├── Widgets/
        │   │   └── .gitkeep (or generated Widget)
        │   ├── Livewire/
        │   │   └── .gitkeep
        │   └── Commands/
        │       └── .gitkeep
        └── tests/
            ├── Pest.php
            ├── TestCase.php
            ├── Unit/
            │   └── ExampleTest.php
            └── Feature/
                └── .gitkeep

Generated Files

composer.json

Filament ^3.3 (latest)
Livewire ^3.6 (latest)
Laravel ^11.0|^12.0 support
Orchestra Testbench ^10.0 (latest)
PestPHP ^3.8 (latest)
PSR-4 autoloading
Laravel auto-discovery

Plugin Class (PluginNamePlugin.php)

Implements Filament\Contracts\Plugin
Resource, Page, Widget registration
Panel configuration hooks

ServiceProvider

View namespace registration
Translation loading
Migration publishing
Config merging

Resource (if --with-resource)

Form schema
Table configuration
Resource pages (List, Create, Edit)

Page (if --with-page)

Custom Filament page
View and logic

Widget (if --with-widget)

Dashboard widget
Stats or chart example

Testing Setup

PestPHP configuration
Orchestra Testbench
Livewire testing utilities
After Running

Install dependencies:

composer update


Register plugin in Panel Provider:

use Vendor\PluginName\PluginNamePlugin;

public function panel(Panel $panel): Panel
{
    return $panel
        ->plugins([
            PluginNamePlugin::make(),
        ]);
}


Publish assets (if needed):

php artisan vendor:publish --tag=filament-plugin-name-config
php artisan vendor:publish --tag=filament-plugin-name-migrations


Run tests:

cd packages/vendor/filament-plugin-name
composer install
./vendor/bin/pest

Filament Plugin Best Practices
Use the Plugin Contract: Always implement Filament\Contracts\Plugin
Register in boot(): Register resources/pages/widgets in boot() method
Support Panel Configuration: Allow users to customize via ->plugin()
Translations: Use translation keys for all user-facing strings
Views: Use namespaced views (filament-plugin-name::view-name)
Testing: Test Livewire components with Livewire::test()
Weekly Installs
9
Repository
mwguerra/claude…-plugins
GitHub Stars
29
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass