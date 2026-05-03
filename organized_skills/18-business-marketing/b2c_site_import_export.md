---
rating: ⭐⭐⭐
title: b2c-site-import-export
url: https://skills.sh/salesforcecommercecloud/b2c-developer-tooling/b2c-site-import-export
---

# b2c-site-import-export

skills/salesforcecommercecloud/b2c-developer-tooling/b2c-site-import-export
b2c-site-import-export
Installation
$ npx skills add https://github.com/salesforcecommercecloud/b2c-developer-tooling --skill b2c-site-import-export
SKILL.md
Site Import/Export Skill

Use the b2c CLI plugin to import and export site archives on Salesforce B2C Commerce instances.

Tip: If b2c is not installed globally, use npx @salesforce/b2c-cli instead (e.g., npx @salesforce/b2c-cli job import).

Import Commands
Import Local Directory
# Import a local directory as a site archive (waits for completion by default)
b2c job import ./my-site-data

# Import and return immediately without waiting
b2c job import ./my-site-data --no-wait

# Import a local zip file
b2c job import ./export.zip

# Keep the archive on the instance after import
b2c job import ./my-site-data --keep-archive

# Show job log if the import fails
b2c job import ./my-site-data --show-log

Import Remote Archive
# Import an archive that already exists on the instance (in Impex/src/instance/)
b2c job import existing-archive.zip --remote

Export Commands
# Export global metadata (waits for completion by default)
b2c job export --global-data meta_data

# Export a site with specific data units
b2c job export --site RefArch --site-data content,site_preferences

Common Workflows
Adding a Custom Attribute to Products
Create the metadata XML file:

meta/system-objecttype-extensions.xml:

<?xml version="1.0" encoding="UTF-8"?>
<metadata xmlns="http://www.demandware.com/xml/impex/metadata/2006-10-31">
    <type-extension type-id="Product">
        <custom-attribute-definitions>
            <attribute-definition attribute-id="vendorSKU">
                <display-name xml:lang="x-default">Vendor SKU</display-name>
                <type>string</type>
                <mandatory-flag>false</mandatory-flag>
                <externally-managed-flag>true</externally-managed-flag>
            </attribute-definition>
        </custom-attribute-definitions>
        <group-definitions>
            <attribute-group group-id="CustomAttributes">
                <display-name xml:lang="x-default">Custom Attributes</display-name>
                <attribute attribute-id="vendorSKU"/>
            </attribute-group>
        </group-definitions>
    </type-extension>
</metadata>

Create the directory structure:
my-import/
└── meta/
    └── system-objecttype-extensions.xml

Import:
b2c job import ./my-import

Adding Site Preferences
Create metadata for the preference:

meta/system-objecttype-extensions.xml:

<?xml version="1.0" encoding="UTF-8"?>
<metadata xmlns="http://www.demandware.com/xml/impex/metadata/2006-10-31">
    <type-extension type-id="SitePreferences">
        <custom-attribute-definitions>
            <attribute-definition attribute-id="enableFeatureX">
                <display-name xml:lang="x-default">Enable Feature X</display-name>
                <type>boolean</type>
                <default-value>false</default-value>
            </attribute-definition>
        </custom-attribute-definitions>
    </type-extension>
</metadata>

Create preference values:

sites/MySite/preferences.xml:

<?xml version="1.0" encoding="UTF-8"?>
<preferences xmlns="http://www.demandware.com/xml/impex/preferences/2007-03-31">
    <custom-preferences>
        <all-instances>
            <preference preference-id="enableFeatureX">true</preference>
        </all-instances>
    </custom-preferences>
</preferences>

Directory structure:
my-import/
├── meta/
│   └── system-objecttype-extensions.xml
└── sites/
    └── MySite/
        └── preferences.xml

Import:
b2c job import ./my-import

Creating a Custom Object Type
Define the custom object:

meta/custom-objecttype-definitions.xml:

<?xml version="1.0" encoding="UTF-8"?>
<metadata xmlns="http://www.demandware.com/xml/impex/metadata/2006-10-31">
    <custom-type type-id="APIConfiguration">
        <display-name xml:lang="x-default">API Configuration</display-name>
        <staging-mode>source-to-target</staging-mode>
        <storage-scope>site</storage-scope>
        <key-definition attribute-id="configId">
            <display-name xml:lang="x-default">Config ID</display-name>
            <type>string</type>
            <min-length>1</min-length>
        </key-definition>
        <attribute-definitions>
            <attribute-definition attribute-id="endpoint">
                <display-name xml:lang="x-default">API Endpoint</display-name>
                <type>string</type>
            </attribute-definition>
            <attribute-definition attribute-id="apiKey">
                <display-name xml:lang="x-default">API Key</display-name>
                <type>password</type>
            </attribute-definition>
            <attribute-definition attribute-id="isActive">
                <display-name xml:lang="x-default">Active</display-name>
                <type>boolean</type>
                <default-value>true</default-value>
            </attribute-definition>
        </attribute-definitions>
    </custom-type>
</metadata>

Import:
b2c job import ./my-import

Importing Custom Object Data

customobjects/APIConfiguration.xml:

<?xml version="1.0" encoding="UTF-8"?>
<custom-objects xmlns="http://www.demandware.com/xml/impex/customobject/2006-10-31">
    <custom-object type-id="APIConfiguration" object-id="payment-gateway">
        <object-attribute attribute-id="endpoint">https://api.payment.com/v2</object-attribute>
        <object-attribute attribute-id="isActive">true</object-attribute>
    </custom-object>
</custom-objects>

Site Archive Structure
site-archive/
├── services.xml                           # Service configurations (credentials, profiles, services)
├── meta/
│   ├── system-objecttype-extensions.xml   # Custom attributes on system objects
│   └── custom-objecttype-definitions.xml  # Custom object type definitions
├── sites/
│   └── {SiteID}/
│       ├── preferences.xml                # Site preference values
│       └── library/
│           └── content/
│               └── content.xml            # Content assets
├── catalogs/
│   └── {CatalogID}/
│       └── catalog.xml                    # Products and categories
├── pricebooks/
│   └── {PriceBookID}/
│       └── pricebook.xml                  # Price definitions
├── customobjects/
│   └── {ObjectTypeID}.xml                 # Custom object instances
└── inventory-lists/
    └── {InventoryListID}/
        └── inventory.xml                  # Inventory records

Tips
Checking Job Status
# Search for recent job executions
b2c job search

# Wait for a specific job execution
b2c job wait <job-id> <execution-id>

# View job logs on failure
b2c job import ./my-data --show-log

Best Practices
Test imports on sandbox first before importing to staging/production
Import waits for completion by default — use --no-wait only when you want to return immediately
Use --show-log to debug failed imports
Keep archives organized by feature or change type
Version control your metadata XML files
Configuring External Services

For service configurations (HTTP, FTP, SOAP services), see the b2c:b2c-webservices skill which includes:

Complete services.xml examples
Credential, profile, and service element patterns
Import/export workflows

Quick example:

# Import service configuration
b2c job import ./services-folder


Where services-folder/services.xml follows the patterns in the b2c:b2c-webservices skill.

Detailed Reference
Metadata XML Patterns - Common XML patterns for imports
Related Skills
b2c:b2c-webservices - Service configurations (HTTP, FTP, SOAP), services.xml format
b2c:b2c-metadata - System object extensions and custom object definitions
b2c-cli:b2c-job - Running jobs and monitoring import status
Weekly Installs
78
Repository
salesforcecomme…-tooling
GitHub Stars
39
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass