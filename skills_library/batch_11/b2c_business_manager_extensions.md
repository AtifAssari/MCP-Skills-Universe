---
title: b2c-business-manager-extensions
url: https://skills.sh/salesforcecommercecloud/b2c-developer-tooling/b2c-business-manager-extensions
---

# b2c-business-manager-extensions

skills/salesforcecommercecloud/b2c-developer-tooling/b2c-business-manager-extensions
b2c-business-manager-extensions
Installation
$ npx skills add https://github.com/salesforcecommercecloud/b2c-developer-tooling --skill b2c-business-manager-extensions
SKILL.md
Business Manager Extensions Skill

This skill guides you through creating Business Manager (BM) extension cartridges to customize the admin interface.

Overview

BM extensions allow you to add custom functionality to Business Manager:

Extension Type	Purpose
Menu Items	Add top-level menu sections
Menu Actions	Add functional links under menus
Dialog Actions	Add buttons to existing BM pages
Form Extensions	Add fields to existing forms
File Structure
/bm_my_extension
    /cartridge
        bm_extensions.xml           # Extension definitions (required)
        /controllers
            MyExtension.js          # Controller for menu actions
        /templates
            /default
                /extensions
                    mypage.isml     # Custom BM pages
        /static
            /default
                /icons
                    my-icon.gif     # Menu icons

Basic bm_extensions.xml
<?xml version="1.0" encoding="UTF-8"?>
<extensions xmlns="http://www.demandware.com/xml/extensibility/2013-04-24">
    <!-- Menu Item: Creates section in navigation -->
    <menuitem id="my-tools" name="label.menu.mytools"
              site="false" position="10">
        <icon path="icons/my-icon.gif"/>
    </menuitem>

    <!-- Menu Action: Creates link under menu item -->
    <menuaction id="my-dashboard" menupath="my-tools"
                name="label.action.dashboard">
        <exec pipeline="MyExtension" node="Dashboard"/>
        <sub-pipelines>
            <pipeline name="MyExtension"/>
        </sub-pipelines>
    </menuaction>
</extensions>

Menu Items

Create top-level navigation sections:

<menuitem id="custom-tools"
          name="label.menu.customtools"
          site="false"
          position="10">
    <description>Custom administration tools</description>
    <icon path="icons/tools-icon.gif"/>
</menuitem>

Attribute	Required	Description
id	Yes	Unique identifier
name	Yes	Resource key for display name
site	No	true = Site menu, false = Admin menu (default: true)
position	No	Sort order (higher = higher in list)
Menu Actions

Add functional pages under menu items:

<menuaction id="product-export"
            menupath="custom-tools"
            name="label.action.productexport">
    <description>Export products to CSV</description>
    <exec pipeline="ProductExport" node="Start"/>
    <sub-pipelines>
        <pipeline name="ProductExport"/>
    </sub-pipelines>
    <icon path="icons/export-icon.gif"/>
</menuaction>

Attribute	Required	Description
id	Yes	Unique identifier
menupath	No	Parent menu item ID
name	Yes	Resource key for display name

Note: For controllers, use pipeline="ControllerName" and node="ActionName".

Dialog Actions

Add buttons to existing BM pages:

<dialogaction id="order-export-btn"
              menuaction-ref="order-search"
              xp-ref="OrderPage-OrderDetails">
    <exec pipeline="OrderExport" node="Export"/>
    <icon path="icons/export.gif"/>
    <parameters>
        <parameter name="OrderNo"/>
    </parameters>
</dialogaction>

Attribute	Required	Description
id	Yes	Unique identifier
menuaction-ref	Yes	Parent menu action ID
xp-ref	Yes	Extension point ID

Common extension points: OrderPage-OrderDetails, ProductPage-Details, CustomerPage-Profile

Form Extensions

Add fields to existing BM forms:

<formextension id="order-search-extension">
    <valueinput type="string" name="customOrderField">
        <label xml:lang="x-default">Custom Field</label>
        <label xml:lang="de">Benutzerdefiniertes Feld</label>
    </valueinput>
    <valueinput type="string" name="exportStatus">
        <label xml:lang="x-default">Export Status</label>
        <option>Pending</option>
        <option>Exported</option>
        <option>Failed</option>
    </valueinput>
</formextension>

Controller Example
'use strict';

var ISML = require('dw/template/ISML');
var URLUtils = require('dw/web/URLUtils');

exports.Dashboard = function () {
    ISML.renderTemplate('extensions/dashboard', {
        title: 'My Dashboard',
        data: getReportData()
    });
};
exports.Dashboard.public = true;

exports.ProcessAction = function () {
    var params = request.httpParameterMap;
    var itemId = params.itemId.stringValue;

    // Process the action
    var result = processItem(itemId);

    // Redirect back or show result
    response.redirect(URLUtils.url('MyExtension-Dashboard', 'result', result));
};
exports.ProcessAction.public = true;

Template Example
<!DOCTYPE html>
<html>
<head>
    <title>${pdict.title}</title>
    <link rel="stylesheet" href="${URLUtils.staticURL('/css/bm-custom.css')}"/>
</head>
<body>
    <div class="bm-content">
        <h1>${pdict.title}</h1>

        <table class="bm-table">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <isloop items="${pdict.data}" var="item">
                    <tr>
                        <td>${item.id}</td>
                        <td>${item.name}</td>
                        <td>
                            <a href="${URLUtils.url('MyExtension-ProcessAction', 'itemId', item.id)}">
                                Process
                            </a>
                        </td>
                    </tr>
                </isloop>
            </tbody>
        </table>
    </div>
</body>
</html>

Localization

Add resource bundles for labels:

templates/resources/bm_extensions.properties:

label.menu.customtools=Custom Tools
label.action.dashboard=Dashboard
label.action.productexport=Product Export


templates/resources/bm_extensions_de.properties:

label.menu.customtools=Benutzerdefinierte Werkzeuge
label.action.dashboard=Instrumententafel
label.action.productexport=Produktexport

Enabling the Extension

Add cartridge to Business Manager site's cartridge path:

Administration > Sites > Manage Sites > Business Manager
Add cartridge ID to cartridge path

Grant permissions to roles:

Administration > Organization > Roles
Select role > Business Manager Modules
Enable your custom modules
Best Practices
Prefix IDs with your organization name to avoid conflicts
Use resource keys for all displayed text (localization)
Keep cartridge separate - don't mix with storefront cartridges
Test permissions with different user roles
Don't reference internal BM URLs - they may change
Detailed Reference
Extensions XML Reference - Complete XML schema and examples
Weekly Installs
78
Repository
salesforcecomme…-tooling
GitHub Stars
39
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass