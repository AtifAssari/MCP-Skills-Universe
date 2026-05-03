---
title: joomla-plugin-development
url: https://skills.sh/nicolasflores9/skills/joomla-plugin-development
---

# joomla-plugin-development

skills/nicolasflores9/skills/joomla-plugin-development
joomla-plugin-development
Installation
$ npx skills add https://github.com/nicolasflores9/skills --skill joomla-plugin-development
SKILL.md
Joomla 5/6 Plugin Development: Complete Guide
1. Introduction

Plugins in Joomla 5/6 represent the most modern evolution of the framework. This knowledge set provides everything you need to create robust, efficient, and maintainable extensions following current patterns.

1.1 What You Will Learn
Modern Joomla 5/6 plugin architecture
SubscriberInterface and getSubscribedEvents() implementation
System, content, and user event handling
Event Classes with type hints
Dependency injection
PSR-4 namespaces and automatic autoloading
Security and performance best practices
Practical and complete examples
1.2 Prerequisites
Working Joomla 5 or 6 installation
Intermediate PHP knowledge
Familiarity with namespaces and composition
Administrator access to Joomla
Code editor (VS Code, PhpStorm, etc.)
2. Modern Plugin Structure
2.1 Standard Directory Tree

Every modern plugin follows this structure:

plg_system_myexample/
├── manifest.xml              # Configuration and installation
├── services/
│   └── provider.php          # Dependency injection
├── src/
│   ├── Extension/
│   │   └── MyExample.php     # Main class
│   ├── Event/                # (Optional) Custom event classes
│   └── Helper/               # (Optional) Helper classes
└── language/
    └── en-GB/
        ├── plg_system_myexample.ini      # Frontend translations
        └── plg_system_myexample.sys.ini  # System translations


Critical naming conventions:

Prefix: plg_ (always plugin)
Group: system, content, user, etc.
Name: lowercase without spaces
Example: plg_content_shortcodes = content plugin named "shortcodes"
2.2 manifest.xml File

The manifest is the installation entry point:

<?xml version="1.0" encoding="utf-8"?>
<extension type="plugin" group="system">
    <name>PLG_SYSTEM_MYEXAMPLE</name>
    <author>Your Name</author>
    <creationDate>2025-03-06</creationDate>
    <copyright>Copyright 2025</copyright>
    <license>GNU General Public License version 2 or later</license>
    <version>1.0.0</version>
    <description>PLG_SYSTEM_MYEXAMPLE_DESCRIPTION</description>
    <targetPlatform version="5.0" />

    <!-- CRITICAL: Defines PSR-4 namespace -->
    <namespace path="src">MyCompany\Plugin\System\MyExample</namespace>

    <!-- File declarations -->
    <files>
        <file>manifest.xml</file>
        <folder plugin="myexample">services</folder>
        <folder>src</folder>
        <folder>language</folder>
    </files>

    <!-- Parameter configuration (optional) -->
    <config>
        <fields name="params">
            <fieldset name="basic">
                <field
                    name="enabled"
                    type="checkbox"
                    label="Enable plugin"
                    default="1"
                />
            </fieldset>
        </fields>
    </config>
</extension>


Critical elements:

<namespace path="src">: Defines the namespace prefix. MUST match exactly in provider.php and Extension
<folder plugin="myexample">: The attribute must be the plugin name (matches manifest.xml)
type="plugin" and group="...": Identifies type and category
2.3 Service Provider (services/provider.php)

This file registers your plugin in the dependency injection container:

<?php
namespace MyCompany\Plugin\System\MyExample;

use Joomla\CMS\Extension\PluginInterface;
use Joomla\CMS\Plugin\PluginHelper;
use Joomla\DI\Container;
use Joomla\DI\ServiceProviderInterface;

class ServiceProvider implements ServiceProviderInterface
{
    public function register(Container $container)
    {
        $container->set(
            PluginInterface::class,
            function (Container $c) {
                $plugin = new Extension(
                    $c->get('dispatcher'),
                    (array) PluginHelper::getPlugin('system', 'myexample')
                );
                return $plugin;
            }
        );
    }
}


Key points:

The namespace MUST match exactly with manifest.xml
PluginHelper::getPlugin() retrieves the plugin configuration
The dispatcher is Joomla's event manager
The Extension class is registered as PluginInterface
3. Extension Class: The Heart of the Plugin

The main class implements SubscriberInterface:

<?php
namespace MyCompany\Plugin\System\MyExample;

use Joomla\CMS\Plugin\CMSPlugin;
use Joomla\Event\SubscriberInterface;
use Joomla\CMS\Event\System\AfterInitialiseEvent;

class Extension extends CMSPlugin implements SubscriberInterface
{
    protected $autoloadLanguage = true;
    protected $allowLegacyListeners = false;

    /**
     * Declares subscribed events
     * This static method is MANDATORY
     */
    public static function getSubscribedEvents(): array
    {
        return [
            'onAfterInitialise' => 'onAfterInitialise',
        ];
    }

    /**
     * Handles the onAfterInitialise event
     */
    public function onAfterInitialise(AfterInitialiseEvent $event)
    {
        // Your logic here
    }
}


Important properties:

$autoloadLanguage = true: Automatically loads .ini language files
$allowLegacyListeners = false: Improves performance, disables Reflection-based lookup
Extends CMSPlugin which provides $params, $app, etc.
4. SubscriberInterface and getSubscribedEvents()
4.1 Modern vs Legacy Pattern

Legacy (Joomla 3-4):

public function onContentPrepare($context, &$article, &$params, $page = 0)
{
    // Logic
}


Modern (Joomla 5+):

public static function getSubscribedEvents(): array
{
    return ['onContentPrepare' => 'onContentPrepare'];
}

public function onContentPrepare(ContentPrepareEvent $event)
{
    $article = $event->getArgument('0');
    // Logic with type hints
}

4.2 getSubscribedEvents() Formats
// Basic format
public static function getSubscribedEvents(): array
{
    return [
        'onContentPrepare' => 'onContentPrepare',
        'onContentAfterTitle' => 'onContentAfterTitle',
    ];
}

// With priorities (lower number = executes first)
public static function getSubscribedEvents(): array
{
    return [
        'onContentPrepare' => ['onContentPrepare', 5],
        'onContentAfterTitle' => 'onContentAfterTitle',
    ];
}

// Multiple listeners for one event
public static function getSubscribedEvents(): array
{
    return [
        'onContentPrepare' => [
            ['primaryHandler', 0],
            ['secondaryHandler', 10],
        ],
    ];
}

5. Main Event Types
5.1 System Events

Triggered on every page load:

Event	When it fires
onAfterInitialise	After Joomla initialization
onAfterRoute	After route resolution
onAfterDispatch	After component execution
onBeforeRender	Before page rendering
onBeforeCompileHead	Before compiling head tags
onAfterRender	After rendering
5.2 Content Events

Triggered during article read/write cycle:

Event	Description
onContentPrepare	Before displaying articles
onContentAfterTitle	After the title
onContentBeforeSave	Pre-save validation
onContentAfterSave	Post-processing
onContentBeforeDelete	Pre-delete cleanup
onContentAfterDelete	Post-delete cleanup
5.3 User Events

User management:

Event	Description
onUserBeforeSave	Before saving user
onUserAfterSave	After saving user
onUserLogin	After successful login
onUserLogout	After logout
6. Event Classes (Joomla 5.2+)

Event Classes provide type safety and better structure:

// Legacy
public function onContentPrepare($context, &$article, &$params, $page = 0)
{
    $text = $article->text;
}

// Modern with Event Class
use Joomla\CMS\Event\Content\ContentPrepareEvent;

public function onContentPrepare(ContentPrepareEvent $event)
{
    // Access by index
    $article = $event->getArgument('0');

    // Or use specific methods (if available)
    $article = $event->getArticle();

    // Modify
    $event->setArgument('0', $modifiedArticle);
}


Event Classes location:

\Joomla\CMS\Event\Content\* for content events
\Joomla\CMS\Event\System\* for system events
\Joomla\CMS\Event\User\* for user events
7. Dependency Injection
7.1 Accessing Basic Services
<?php
namespace MyCompany\Plugin\Content\Example;

use Joomla\CMS\Plugin\CMSPlugin;
use Joomla\Event\SubscriberInterface;
use Joomla\DI\Traits\ContainerAwareTrait;
use Joomla\Database\DatabaseInterface;

class Extension extends CMSPlugin implements SubscriberInterface
{
    use ContainerAwareTrait;

    public static function getSubscribedEvents(): array
    {
        return ['onContentPrepare' => 'onContentPrepare'];
    }

    public function onContentPrepare($event)
    {
        // Access the container
        $container = $this->getContainer();

        // Get the database
        $db = $container->get(DatabaseInterface::class);

        // Execute query
        $query = $db->getQuery(true)
            ->select('*')
            ->from($db->quoteName('#__articles'));

        $db->setQuery($query);
        $results = $db->loadObjectList();
    }
}

7.2 In Service Provider
<?php
namespace MyCompany\Plugin\Content\Example;

use Joomla\CMS\Extension\PluginInterface;
use Joomla\CMS\Plugin\PluginHelper;
use Joomla\DI\Container;
use Joomla\DI\ServiceProviderInterface;
use Joomla\Database\DatabaseInterface;

class ServiceProvider implements ServiceProviderInterface
{
    public function register(Container $container)
    {
        $container->set(
            PluginInterface::class,
            function (Container $c) {
                $plugin = new Extension(
                    $c->get('dispatcher'),
                    (array) PluginHelper::getPlugin('content', 'example')
                );

                // Inject the container
                $plugin->setContainer($c);

                return $plugin;
            }
        );
    }
}

8. Your First Plugin: "Hello World"
8.1 Minimal Structure
plg_system_helloworld/
├── manifest.xml
├── services/
│   └── provider.php
├── src/
│   └── Extension/
│       └── Helloworld.php
└── language/
    └── en-GB/
        ├── plg_system_helloworld.ini
        └── plg_system_helloworld.sys.ini

8.2 manifest.xml
<?xml version="1.0" encoding="utf-8"?>
<extension type="plugin" group="system">
    <name>PLG_SYSTEM_HELLOWORLD</name>
    <author>Your Name</author>
    <creationDate>2025-03-06</creationDate>
    <copyright>Copyright 2025</copyright>
    <license>GNU General Public License version 2 or later</license>
    <version>1.0.0</version>
    <description>PLG_SYSTEM_HELLOWORLD_DESCRIPTION</description>
    <targetPlatform version="5.0" />

    <namespace path="src">MyCompany\Plugin\System\Helloworld</namespace>

    <files>
        <file>manifest.xml</file>
        <folder plugin="helloworld">services</folder>
        <folder>src</folder>
        <folder>language</folder>
    </files>
</extension>

8.3 services/provider.php
<?php
namespace MyCompany\Plugin\System\Helloworld;

use Joomla\CMS\Extension\PluginInterface;
use Joomla\CMS\Plugin\PluginHelper;
use Joomla\DI\Container;
use Joomla\DI\ServiceProviderInterface;

class ServiceProvider implements ServiceProviderInterface
{
    public function register(Container $container)
    {
        $container->set(
            PluginInterface::class,
            function (Container $c) {
                $plugin = new Extension(
                    $c->get('dispatcher'),
                    (array) PluginHelper::getPlugin('system', 'helloworld')
                );
                return $plugin;
            }
        );
    }
}

8.4 src/Extension/Helloworld.php
<?php
namespace MyCompany\Plugin\System\Helloworld;

use Joomla\CMS\Plugin\CMSPlugin;
use Joomla\Event\SubscriberInterface;
use Joomla\CMS\Event\System\AfterInitialiseEvent;

class Extension extends CMSPlugin implements SubscriberInterface
{
    protected $autoloadLanguage = true;
    protected $allowLegacyListeners = false;

    public static function getSubscribedEvents(): array
    {
        return [
            'onAfterInitialise' => 'onAfterInitialise',
        ];
    }

    public function onAfterInitialise(AfterInitialiseEvent $event)
    {
        $app = $this->getApplication();
        $app->getLogger()->info('Hello World! The plugin is working.');
    }
}

8.5 Language Files

language/en-GB/plg_system_helloworld.ini:

PLG_SYSTEM_HELLOWORLD="Hello World Plugin"


language/en-GB/plg_system_helloworld.sys.ini:

PLG_SYSTEM_HELLOWORLD="Hello World Plugin"
PLG_SYSTEM_HELLOWORLD_DESCRIPTION="A sample plugin that displays 'Hello World'"

8.6 Installation
Create folder: plugins/system/helloworld
Copy all files
Go to Control Panel > Extensions > Plugins
Search for "Hello World Plugin"
Enable it
Verify in logs: logs/joomla.log
9. Advanced Plugin: Content Shortcodes
9.1 Manifest.xml with Parameters
<?xml version="1.0" encoding="utf-8"?>
<extension type="plugin" group="content" method="upgrade">
    <name>PLG_CONTENT_SHORTCODES</name>
    <author>Your Name</author>
    <creationDate>2025-03-06</creationDate>
    <copyright>Copyright 2025</copyright>
    <license>GNU General Public License version 2 or later</license>
    <version>1.0.0</version>
    <description>PLG_CONTENT_SHORTCODES_DESCRIPTION</description>
    <targetPlatform version="5.0" />

    <namespace path="src">MyCompany\Plugin\Content\Shortcodes</namespace>

    <files>
        <file>manifest.xml</file>
        <folder plugin="shortcodes">services</folder>
        <folder>src</folder>
        <folder>language</folder>
    </files>

    <config>
        <fields name="params">
            <fieldset name="basic">
                <field
                    name="process_shortcodes"
                    type="checkbox"
                    label="PLG_CONTENT_SHORTCODES_ENABLED"
                    default="1"
                />
            </fieldset>
        </fields>
    </config>
</extension>

9.2 Complete Extension Class
<?php
namespace MyCompany\Plugin\Content\Shortcodes;

use Joomla\CMS\Plugin\CMSPlugin;
use Joomla\Event\SubscriberInterface;
use Joomla\CMS\Event\Content\ContentPrepareEvent;
use Joomla\CMS\Factory;

class Extension extends CMSPlugin implements SubscriberInterface
{
    protected $autoloadLanguage = true;
    protected $allowLegacyListeners = false;

    public static function getSubscribedEvents(): array
    {
        return [
            'onContentPrepare' => 'onContentPrepare',
        ];
    }

    public function onContentPrepare(ContentPrepareEvent $event)
    {
        // Check if enabled
        if (!$this->params->get('process_shortcodes', true)) {
            return;
        }

        $article = $event->getArgument('0');

        if (!isset($article) || !isset($article->text)) {
            return;
        }

        // Process shortcodes
        $article->text = $this->processShortcodes($article->text);
    }

    protected function processShortcodes($text)
    {
        $config = Factory::getConfig();

        // Replace {sitename}
        $text = str_replace(
            '{sitename}',
            $config->get('sitename'),
            $text
        );

        // Replace {siteurl}
        $text = str_replace(
            '{siteurl}',
            $config->get('live_site'),
            $text
        );

        // Replace {year}
        $text = str_replace(
            '{year}',
            date('Y'),
            $text
        );

        return $text;
    }
}

9.3 Service Provider
<?php
namespace MyCompany\Plugin\Content\Shortcodes;

use Joomla\CMS\Extension\PluginInterface;
use Joomla\CMS\Plugin\PluginHelper;
use Joomla\DI\Container;
use Joomla\DI\ServiceProviderInterface;

class ServiceProvider implements ServiceProviderInterface
{
    public function register(Container $container)
    {
        $container->set(
            PluginInterface::class,
            function (Container $c) {
                $plugin = new Extension(
                    $c->get('dispatcher'),
                    (array) PluginHelper::getPlugin('content', 'shortcodes')
                );
                return $plugin;
            }
        );
    }
}

9.4 Language Files

language/en-GB/plg_content_shortcodes.ini:

PLG_CONTENT_SHORTCODES="Content Shortcodes"
PLG_CONTENT_SHORTCODES_ENABLED="Process Shortcodes"


language/en-GB/plg_content_shortcodes.sys.ini:

PLG_CONTENT_SHORTCODES="Content Shortcodes"
PLG_CONTENT_SHORTCODES_DESCRIPTION="Replace shortcodes like {sitename} with site configuration values"

10. Best Practices
10.1 Security
// ALWAYS validate input
use Joomla\CMS\Filter\InputFilter;

$filter = InputFilter::getInstance();
$safe_input = $filter->clean($_GET['data'], 'STRING');

// ALWAYS escape output
use Joomla\CMS\HTML\HTMLHelper;

echo HTMLHelper::_('common.escape', $user_content);

// Check permissions
$user = Factory::getUser();
if (!$user->authorise('core.manage', 'com_example')) {
    return;
}

10.2 Performance
// Use cache
$cache = Factory::getCache('_system');
$key = 'plugin_example_data_' . $article_id;

if ($data = $cache->get($key)) {
    return $data;
}

// Processing
$data = $this->expensiveOperation();

// Store in cache (3600 seconds = 1 hour)
$cache->store($data, $key, '_system', 3600);

// Be selective with events - DO NOT subscribe to all of them
public static function getSubscribedEvents(): array
{
    return [
        'onContentPrepare' => 'onContentPrepare',
        // NO: 'onAfterRender', 'onBeforeRender', etc.
    ];
}

10.3 Namespace and PSR-4

CORRECT:

manifest.xml: <namespace path="src">MyCompany\Plugin\Content\Shortcodes</namespace>
services/provider.php: namespace MyCompany\Plugin\Content\Shortcodes;
src/Extension/Shortcodes.php: namespace MyCompany\Plugin\Content\Shortcodes;

INCORRECT:

Mismatching namespaces
Not including path="src" in manifest
Using incorrect paths in files
11. Common Troubleshooting
11.1 Plugin does not appear in the list

Solutions:

Verify that manifest.xml is in the root of the plugin folder
Check that the XML is valid (no special characters)
Clear cache: Control Panel > System > Cache > Clear Cache
Verify folder permissions (755)
11.2 Event does not fire

Solutions:

Verify that getSubscribedEvents() correctly declares the event
Make sure the plugin is enabled
Check that $allowLegacyListeners = false
Check logs at logs/joomla.log
11.3 Namespace error

Solutions:

Match EXACTLY the namespace in manifest, provider, and Extension
Use semicolon at the end of namespace
Verify path in <folder plugin="pluginname">services</folder>
Clear autoload cache: administrator/cache/autoload_psr4.php
12. Installation Verification

After installing a plugin, verify:

Control Panel > Extensions > Plugins
Search for the plugin by name
Verify it appears in the list
Enable it (green status)
Check logs at logs/joomla.log for messages
Test functionality according to the plugin type
13. Additional Resources
Official Joomla Manual Documentation
Joomla Event Classes Documentation
API Reference
Joomla Community - Forum
Weekly Installs
16
Repository
nicolasflores9/skills
GitHub Stars
1
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn