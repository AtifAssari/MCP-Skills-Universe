---
title: joomla-template-overrides
url: https://skills.sh/nicolasflores9/skills/joomla-template-overrides
---

# joomla-template-overrides

skills/nicolasflores9/skills/joomla-template-overrides
joomla-template-overrides
Installation
$ npx skills add https://github.com/nicolasflores9/skills --skill joomla-template-overrides
SKILL.md
Joomla Template Overrides - Complete System
Introduction

Template overrides allow you to customize the output of components, modules, and plugins without modifying core files. They are stored in /templates/[name]/html/ and are automatically loaded in place of the original files.

Covers: Joomla 5.x, 6.x | Requirements: Basic knowledge of PHP, Joomla folder structure

Fundamental Concepts
Why Use Overrides?
Customize presentation without modifying core
Maintain functionality when updating Joomla
Reuse code across views
Separate presentation logic
Loading Hierarchy

Joomla looks for files in this order:

/templates/[active]/html/[path] → Custom override
/[component]/views/[view]/tmpl/ → Original file
/html/ Folder Structure
/templates/cassiopeia/html/
├── com_content/              # Components (com_)
│   ├── article/
│   │   └── default.php
│   └── category/
│       ├── blog.php
│       ├── blog_item.php
│       └── default.php
├── mod_login/                # Modules (mod_)
│   ├── default.php
│   └── slim.php
├── plg_content_pagenavigation/ # Plugins (plg_)
│   └── default.php
└── layouts/                  # Reusable JLayouts
    └── joomla/
        └── content/
            ├── intro_image.php
            └── info_block.php


Naming Convention:

com_[component] → components
mod_[module] → modules
plg_[group]_[plugin] → plugins
Component Overrides - com_content
Single Article (article/default.php)

Original Location: /components/com_content/views/article/tmpl/default.php Override: /templates/cassiopeia/html/com_content/article/default.php

Available variables:

$this->item → article object
$this->params → parameters
$this->item->jcfields → custom fields
<?php defined('_JEXEC') or die; ?>
<article class="article-container">
    <header class="article-header">
        <h1><?php echo htmlspecialchars($this->item->title); ?></h1>
    </header>

    <section class="article-body">
        <?php if (!empty($this->item->images)): ?>
            <?php echo JLayoutHelper::render('joomla.content.intro_image',
                ['item' => $this->item]); ?>
        <?php endif; ?>

        <?php echo $this->item->text; ?>
    </section>

    <?php if (!empty($this->item->jcfields)): ?>
        <section class="article-custom-fields">
            <?php foreach ($this->item->jcfields as $field): ?>
                <div class="field-<?php echo htmlspecialchars($field->type); ?>">
                    <strong><?php echo htmlspecialchars($field->label); ?></strong>
                    <?php echo $field->rawvalue; ?>
                </div>
            <?php endforeach; ?>
        </section>
    <?php endif; ?>
</article>

Category Blog Mode - blog_item.php

Location: /templates/cassiopeia/html/com_content/category/blog_item.php

Renders each article in the blog:

<?php defined('_JEXEC') or die;
$item = $this->item; ?>

<article class="blog-item">
    <h2 class="item-title">
        <?php echo JHtml::_('link', JRoute::_($item->link),
            htmlspecialchars($item->title)); ?>
    </h2>

    <?php if (!empty($item->images)): ?>
        <?php echo JLayoutHelper::render('joomla.content.intro_image',
            ['item' => $item]); ?>
    <?php endif; ?>

    <div class="item-content">
        <?php echo $item->introtext; ?>
    </div>

    <a href="<?php echo JRoute::_($item->link); ?>" class="read-more">
        Read more
    </a>
</article>

Category List Mode - default.php

Location: /templates/cassiopeia/html/com_content/category/default.php

Main container with article table.

Module Overrides
Structure

Location: /templates/[template]/html/mod_[module]/[layout].php

Common modules:

mod_login → login form
mod_menu → menus
mod_custom → custom content
mod_articles_latest → latest articles
mod_breadcrumbs → breadcrumbs
Example: mod_login Override

Location: /templates/cassiopeia/html/mod_login/default.php

<?php defined('_JEXEC') or die;
$params = $this->params; ?>

<form action="<?php echo JRoute::_('index.php'); ?>" method="post" class="login-form">
    <div class="form-group">
        <label for="login-username">Username</label>
        <input type="text" name="username" id="login-username"
               class="form-control" required>
    </div>

    <div class="form-group">
        <label for="login-password">Password</label>
        <input type="password" name="password" id="login-password"
               class="form-control" required>
    </div>

    <button type="submit" class="btn btn-primary">Log In</button>

    <input type="hidden" name="option" value="com_users">
    <input type="hidden" name="task" value="user.login">
    <input type="hidden" name="return" value="<?php echo base64_encode(JUri::current()); ?>">
    <?php echo JHtml::_('form.token'); ?>
</form>

Alternative Layouts

Selectable variations without fully replacing the view.

Difference vs Template Override
Aspect	Override	Alternative Layout
Application	Automatic site-wide	Selectable per module
File	default.php (replaces)	Unique name (e.g.: grid.php)
Usage	Replaces original view	Option alongside original
Creating an Alternative Layout

For modules: Multiple files in /html/mod_[module]/

// /templates/cassiopeia/html/mod_login/grid.php
// Alternative grid layout for mod_login
<?php defined('_JEXEC') or die; ?>
<div class="login-grid">
    <!-- grid structure -->
</div>


For components: In menu select "Alternative Layout"

Naming rules:

Do not use underscores
Descriptive names: grid.php, minimal.php, card.php
default.php = original layout
JLayout - Reusable Components

System for creating reusable fragments.

Joomla layouts location: /layouts/joomla/[group]/[layout].php

Override: /templates/cassiopeia/html/layouts/joomla/[group]/[layout].php

Creating a Custom Layout
// /templates/cassiopeia/html/layouts/joomla/custom/article-card.php
<?php defined('_JEXEC') or die;
$title = $displayData['title'] ?? '';
$content = $displayData['content'] ?? '';
$image = $displayData['image'] ?? '';
$link = $displayData['link'] ?? '#';
?>

<article class="card">
    <?php if ($image): ?>
        <figure class="card-image">
            <img src="<?php echo htmlspecialchars($image); ?>"
                 alt="<?php echo htmlspecialchars($title); ?>">
        </figure>
    <?php endif; ?>

    <div class="card-body">
        <h3><?php echo htmlspecialchars($title); ?></h3>
        <div class="card-content">
            <?php echo $content; ?>
        </div>
        <a href="<?php echo htmlspecialchars($link); ?>" class="card-link">
            View more
        </a>
    </div>
</article>

Usage in blog_item.php
<?php echo JLayoutHelper::render('joomla.custom.article-card', [
    'title' => $this->item->title,
    'content' => $this->item->introtext,
    'image' => json_decode($this->item->images)->image_intro ?? '',
    'link' => JRoute::_($this->item->link),
]); ?>

Child Templates

A template that inherits from a parent, only storing changes.

Creating a Child Template

Structure:

/templates/cassiopeia-child/
├── html/
│   └── com_content/article/default.php  (custom override)
├── css/
│   └── custom.css
└── templateDetails.xml


templateDetails.xml:

<?xml version="1.0" encoding="utf-8"?>
<extension type="template" client="site">
    <name>Cassiopeia Child</name>
    <version>1.0.0</version>
    <description>Child template based on Cassiopeia</description>
    <parent>cassiopeia</parent>

    <files>
        <folder>html</folder>
        <folder>css</folder>
        <filename>templateDetails.xml</filename>
    </files>

    <positions>
        <position>header</position>
        <position>sidebar</position>
        <position>footer</position>
    </positions>
</extension>


Advantages:

Automatically inherits non-customized files
Only stores modified files
Simplifies maintenance and updates
Allows multiple variations of the same parent
Field Overrides - Custom Fields

Override how custom fields are displayed.

Location: /templates/[template]/html/layouts/com_fields/field/[layout].php

// /templates/cassiopeia/html/layouts/com_fields/field/render.php
<?php defined('_JEXEC') or die;
$field = $displayData['field'] ?? null;
$value = $displayData['value'] ?? null;

if (!$field || !$value) return;
?>

<div class="field-container" data-field-id="<?php echo (int)$field->id; ?>">
    <label class="field-label">
        <?php echo htmlspecialchars($field->label); ?>
    </label>
    <div class="field-value">
        <?php echo $value; ?>
    </div>
</div>


Select in backend: Field Edit > Render Options > Layout

Template Manager - Creating Overrides

Backend: Extensions > Templates > [Template] > Create Overrides

Advantages:

Intuitive visual interface
Automatically copies files
No manual searching required
Ensures correct structure
Best Practices
Code Documentation
<?php
/**
 * Override: Custom article
 *
 * Component: com_content
 * Original view: article/tmpl/default.php
 *
 * CHANGES:
 * - Improved semantic structure
 * - Added custom fields
 * - Reordered metadata
 *
 * DEPENDENCIES: Custom field 'author-bio'
 * JOOMLA: 5.0+
 * DATE: 2024-03-06
 */
defined('_JEXEC') or die;

Security - Escaping
// GOOD: Escape outputs
<?php echo htmlspecialchars($item->title, ENT_QUOTES, 'UTF-8'); ?>
<?php echo JHtml::_('string.truncate', $item->text, 100); ?>

// GOOD: URLs with JRoute
<?php echo JRoute::_('index.php?option=com_content&view=article&id=' . $item->id); ?>

// BAD: Unescaped output
<?php echo $item->title; ?>

Post-Update Testing
# Compare overrides with core files
diff -u /components/com_content/views/article/tmpl/default.php \
         /templates/cassiopeia/html/com_content/article/default.php

# Backup overrides before updating
cp -r templates/cassiopeia/html templates/cassiopeia/html.backup

Avoid Unnecessary Overrides
Only override if you modify the view
Use alternative layouts for variations
Use JLayout for reusable components
Maintain change tracking (git, documentation)
Troubleshooting
Override Not Working
Verify correct path in /templates/[active]/html/
Clear cache (System > Clear Cache)
Verify file permissions (755 folders, 644 files)
Verify PHP syntax (php -l file.php)
Check error logs in /logs/
File Permissions
# Folders: read+execute
chmod 755 /templates/cassiopeia/html/

# Files: read
chmod 644 /templates/cassiopeia/html/com_content/article/default.php

Caching Issues
Clear cache in backend: System > Clear Cache
Template option: Style Edit > Caching
Verify router cache in configuration.php
Practical Case: Featured Articles

Objective: Display featured articles in card format

Steps:

Create override: com_content/article/featured.php
Create JLayout: layouts/joomla/custom/featured-card.php
Use in override with JLayoutHelper::render()
Assign custom CSS

See complete examples in /referencias/

Quick Reference
Common Paths
Element	Original	Override
Article	com_content/views/article/tmpl/default.php	html/com_content/article/default.php
Blog item	com_content/views/category/tmpl/blog_item.php	html/com_content/category/blog_item.php
Category list	com_content/views/category/tmpl/default.php	html/com_content/category/default.php
Login module	modules/mod_login/tmpl/default.php	html/mod_login/default.php
JLayout image	layouts/joomla/content/intro_image.php	html/layouts/joomla/content/intro_image.php
Nav plugin	plugins/content/pagenavigation/tmpl/default.php	html/plg_content_pagenavigation/default.php
Checklist - Creating an Override
 Locate original file in core
 Create /html/ structure in template
 Copy file to override location
 Make modifications
 Escape outputs correctly
 Document changes in header
 Test in browser
 Clear cache
 Verify at different resolutions
 Use Template Manager to verify structure
Useful Variables
// Articles
$this->item->id
$this->item->title
$this->item->introtext
$this->item->text
$this->item->images (JSON)
$this->item->jcfields (custom fields)

// Parameters
$this->params->get('show_author')
$this->params->get('show_category')

// Modules
$this->module->id
$this->module->title
$this->params

// JLayout
$displayData (array of passed data)

Additional Resources
Joomla Documentation - Template Overrides
[Template Manager in Backend](Extensions > Templates)
Joomla Magazine - Child Templates
Debugging - developer.joomla.org
Weekly Installs
14
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