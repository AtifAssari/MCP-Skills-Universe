---
rating: ⭐⭐⭐
title: joomla-frontend-integration
url: https://skills.sh/nicolasflores9/skills/joomla-frontend-integration
---

# joomla-frontend-integration

skills/nicolasflores9/skills/joomla-frontend-integration
joomla-frontend-integration
Installation
$ npx skills add https://github.com/nicolasflores9/skills --skill joomla-frontend-integration
SKILL.md
Frontend Integration in Joomla 5/6 with Helix Framework

Comprehensive guide to mastering CSS/JavaScript, WebAssetManager, and responsive design in Joomla 5/6 using Helix Framework and Bootstrap 5.

1. WebAssetManager: The Modern System

The WebAssetManager (\Joomla\CMS\WebAsset\WebAssetManager) is the official way to manage assets in Joomla 5/6. It replaces HTMLHelper and Document API (deprecated in 5.3+).

Lifecycle
Registered: Asset declared in joomla.asset.json
Used: Activated with $wa->useScript() or $wa->useStyle()
Rendered: Inserted into HTML by <jdoc:include type="head" />
Loaded: Downloaded by browser with automatic versioning
Getting an Instance
$wa = \Joomla\CMS\Factory::getApplication()
      ->getDocument()
      ->getWebAssetManager();

// Load assets
$wa->useScript('jquery');
$wa->useStyle('bootstrap');

Loading Levels in Joomla
1. media/vendor/joomla.asset.json
2. media/system/joomla.asset.json
3. media/legacy/joomla.asset.json
4. media/com_active/joomla.asset.json
5. templates/active_template/joomla.asset.json

2. joomla.asset.json Structure

JSON file that declares all assets in a centralized way. It is loaded automatically.

Basic Structure
{
  "$schema": "https://json.schemastore.org/joomla-manifest-schema.json",
  "name": "myext",
  "version": "1.0.0",
  "assets": [
    {
      "name": "my-script",
      "type": "script",
      "uri": "js/myfile.js",
      "dependencies": ["jquery"],
      "attributes": {
        "defer": true,
        "async": false
      },
      "version": "auto"
    },
    {
      "name": "my-style",
      "type": "style",
      "uri": "css/myfile.css",
      "dependencies": [],
      "version": "auto"
    }
  ]
}

Locations by Type
Module: /mod_mymod/joomla.asset.json
Component: /com_mycomp/joomla.asset.json
Plugin: /plg_group_name/joomla.asset.json
Template: /templates/mytemplate/joomla.asset.json
Automatic Versioning
"version": "auto"  // Uses last modification date
"version": "1.0.0" // Manual version

3. Loading CSS and JavaScript Correctly
Method 1: WebAssetManager (RECOMMENDED)
// In helper.php, layout, or component
$wa = \Joomla\CMS\Factory::getApplication()
      ->getDocument()
      ->getWebAssetManager();

// Scripts
$wa->useScript('jquery');
$wa->useScript('bootstrap');
$wa->useScript('my-custom-script');

// Styles
$wa->useStyle('bootstrap');
$wa->useStyle('my-custom-style');

Alternatives (Dynamic, CDN, Legacy)
// Register dynamically
$wa->registerAndUseScript('my-dynamic', 'js/dynamic.js',
    ['dependencies' => ['jquery']], ['defer' => true]);

// From CDN in joomla.asset.json
{"name": "lib", "type": "script",
 "uri": "https://cdn.example.com/lib.min.js"}

// Legacy (avoid)
\Joomla\CMS\HTML\HTMLHelper::script('js/file.js');

4. Bootstrap 5 with Helix Framework

Helix includes Bootstrap 5.2.3+ automatically. 12-column grid, flexbox, utilities.

Responsive Grid
<!-- Integrated Bootstrap grid -->
<div class="container">
  <div class="row">
    <div class="col-12 col-md-6 col-lg-4">
      <!-- Content: 100% mobile, 50% tablet, 33% desktop -->
    </div>
  </div>
</div>

Bootstrap Breakpoints
/* xs: 0px (mobile first) */
/* sm: 576px (landscape phones) */
/* md: 768px (tablets) */
/* lg: 992px (desktops) */
/* xl: 1200px (large desktops) */
/* xxl: 1400px (very large) */

Media Queries
/* Mobile first: base styles for mobile */
.card {
  padding: 1rem;
  font-size: 14px;
}

/* Enhance for tablets */
@media (min-width: 768px) {
  .card {
    padding: 2rem;
    font-size: 16px;
  }
}

/* Enhance for desktops */
@media (min-width: 992px) {
  .card {
    padding: 3rem;
    font-size: 18px;
  }
}

Do Not Break Bootstrap
/* INCORRECT: overriding Bootstrap classes */
.btn { background: red; }

/* CORRECT: create custom classes */
.btn-custom { background: red; }
.btn-custom:hover { background: darkred; }

5. Custom Modules with Assets

Structure:

/mod_mymodule/
  ├── joomla.asset.json
  ├── helper.php
  ├── mod_mymodule.php
  ├── tmpl/default.php
  ├── js/module.js
  └── css/module.css


Activate in helper.php or template:

$wa = \Joomla\CMS\Factory::getApplication()
      ->getDocument()
      ->getWebAssetManager();
$wa->useScript('mod_mymodule.script');
$wa->useStyle('mod_mymodule.style');


See complete example in references/02-modulo-testimonios-completo.php.

6. SP Page Builder: Assets in Addons

Native CSS: Row/Column > Custom CSS (CodeMirror editor available).

Custom JS: Create a sppagebuilder type plugin (native JS not supported).

See complete example in references/06-sp-page-builder-addon-plugin.php.

7. Dependencies Between Assets

Automatic load order resolution system.

Simple Dependency
{
  "name": "my-plugin",
  "type": "script",
  "uri": "js/plugin.js",
  "dependencies": ["jquery"]
}

Multiple Dependencies
{
  "name": "advanced-plugin",
  "type": "script",
  "uri": "js/advanced.js",
  "dependencies": [
    "jquery",
    "bootstrap.util",
    "popper"
  ]
}

Dependency with Specific Type
{
  "name": "my-component",
  "type": "script",
  "uri": "js/component.js",
  "dependencies": [
    "jquery#script",
    "bootstrap.util#script",
    "theme-dark#style"
  ]
}

Preset (Dependency Group)
{
  "name": "admin-bundle",
  "type": "preset",
  "uri": "",
  "dependencies": [
    "jquery#script",
    "popper#script",
    "bootstrap#script",
    "bootstrap#style"
  ]
}

8. Inline Scripts and Styles

For small or dynamic code.

Inline Script
$wa = Factory::getApplication()
      ->getDocument()
      ->getWebAssetManager();

$wa->addInlineScript('
  document.addEventListener("DOMContentLoaded", function() {
    console.log("Inline script executed");
  });
');

Inline Style
$wa->addInlineStyle('
  .banner-custom {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 20px;
  }
');

Named Inline (as a Dependency)
$wa->registerAndUseScript(
    'my-init',
    'document.addEventListener("DOMContentLoaded", function() { /* init */ });'
);

// Use as a dependency
$wa->registerAndUseScript(
    'my-app',
    'js/app.js',
    ['dependencies' => ['my-init']]
);

9. Defer, Async, and Optimization

Critical attributes for performance.

Defer

Executes AFTER HTML is loaded. Recommended for most cases.

{
  "name": "my-script",
  "type": "script",
  "uri": "js/my-script.js",
  "attributes": {
    "defer": true,
    "async": false
  }
}


Use for:

jQuery
Bootstrap
Custom scripts that depend on jQuery
Async

Executes WHEN ready. For independent code.

{
  "name": "analytics",
  "type": "script",
  "uri": "https://analytics.example.com/track.js",
  "attributes": {
    "defer": false,
    "async": true
  }
}


Use for:

Google Analytics
Tracking scripts
Chat widgets
Independent code
Decision Matrix
jQuery / Bootstrap          -> defer: true, async: false
Custom JS that uses jQuery  -> defer: true, async: false
Analytics / Tracking        -> defer: false, async: true
3rd party widget            -> async: true

10. Web Components

Native W3C standard. Joomla includes joomla-core-loader.

// Create Web Component
class MyComponent extends HTMLElement {
  connectedCallback() {
    this.innerHTML = `<div>${this.getAttribute('title')}</div>`;
  }
}
customElements.define('my-component', MyComponent);

// Register in joomla.asset.json
// {"name": "my-comp", "type": "script", "uri": "js/my-comp.js",
//  "attributes": {"type": "module", "defer": true}}


See complete example in references/07-web-component-custom.js.

11. Custom Code in Helix

Admin > Templates > [Your Template] > Template Options > Custom Code tab.

Global CSS:

.site-header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
.custom-button {
  padding: 12px 24px;
  border-radius: 4px;
  transition: all 0.3s ease;
}


Global JS & Google Fonts: See examples in references/08-template-helix-custom.css and references/10-ejemplos-codigo-rapido.md.

12. Best Practices: Do Not Break Helix
NEVER Edit
/template/css/template.css        X
/template/css/bootstrap.css        X
/template/js/template.js           X

ALWAYS Create/Use
/template/css/custom.css           OK
/template/scss/custom.scss         OK
/template/js/custom.js             OK
Custom Code section in admin       OK

Safe CSS Cascade
/* template.css loads first */
.btn { padding: 8px 12px; }

/* custom.css loads last - has priority */
.btn { padding: 10px 16px; }

Preserve Bootstrap Classes
/* INCORRECT: modifies Bootstrap class */
.btn { background: purple; }

/* CORRECT: creates custom class */
.btn-primary-custom { background: purple; }

<!-- Use custom class -->
<button class="btn btn-primary-custom">Button</button>

13. Quick Troubleshooting

Assets not loading: Check <jdoc:include type="head" /> in template, path in joomla.asset.json, permissions (755), Joomla cache.

Incorrect order: Verify dependencies, check Network tab in DevTools.

Bootstrap not working: Confirm $wa->useStyle('bootstrap'), do not override variables, use classes correctly.

Helix breaks: Do not edit core files, use custom.css, check Custom Code.

More details in references/09-checklist-desarrollo.md.

14. Quick References and Resources

See references/09-checklist-desarrollo.md and references/10-ejemplos-codigo-rapido.md for detailed guides and additional examples.

Weekly Installs
12
Repository
nicolasflores9/skills
GitHub Stars
1
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass