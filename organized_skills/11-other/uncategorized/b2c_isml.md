---
rating: ⭐⭐⭐
title: b2c-isml
url: https://skills.sh/salesforcecommercecloud/b2c-developer-tooling/b2c-isml
---

# b2c-isml

skills/salesforcecommercecloud/b2c-developer-tooling/b2c-isml
b2c-isml
Installation
$ npx skills add https://github.com/salesforcecommercecloud/b2c-developer-tooling --skill b2c-isml
SKILL.md
ISML Skill

This skill guides you through creating and working with ISML (Isomorphic Markup Language) templates in Salesforce B2C Commerce. ISML templates combine HTML with dynamic server-side tags.

Overview

ISML templates are server-side templates that generate HTML. They use special tags prefixed with is and expressions in ${...} syntax to embed dynamic content.

File Location

Templates reside in the cartridge's templates directory:

/my-cartridge
    /cartridge
        /templates
            /default                    # Default locale
                /product
                    detail.isml
                    tile.isml
                /home
                    homepage.isml
                /util
                    modules.isml        # Custom tag definitions
            /fr_FR                      # French-specific templates
                /product
                    detail.isml

Essential Tags
Conditional Logic
<isif condition="${product.available}">
    <span class="in-stock">In Stock</span>
<iselseif condition="${product.preorderable}">
    <span class="preorder">Pre-order</span>
<iselse>
    <span class="out-of-stock">Out of Stock</span>
</isif>

Loops
<isloop items="${products}" var="product" status="loopstate">
    <div class="product ${loopstate.odd ? 'odd' : 'even'}">
        <span>${loopstate.count}. ${product.name}</span>
        <isif condition="${loopstate.first}">
            <span class="badge">Featured</span>
        </isif>
    </div>
</isloop>


Loop status properties:

count - Iteration number (1-based)
index - Current index (0-based)
first - Boolean, true on first iteration
last - Boolean, true on last iteration
odd - Boolean, true on odd iterations
even - Boolean, true on even iterations
Variables
<!-- Set a variable (scope is required) -->
<isset name="productName" value="${product.name}" scope="page"/>

<!-- Use the variable -->
<span>${productName}</span>

<!-- Remove a variable -->
<isremove name="productName" scope="page"/>


Scopes (required): page, request, session, pdict

Output
<!-- Basic output (HTML encoded by default) -->
<isprint value="${product.name}"/>

<!-- Unencoded output (use carefully) -->
<isprint value="${htmlContent}" encoding="off"/>

<!-- Formatted number -->
<isprint value="${price}" style="CURRENCY"/>

<!-- Formatted date -->
<isprint value="${order.creationDate}" style="DATE_SHORT"/>

Include Templates
<!-- Include local template -->
<isinclude template="product/components/price"/>

<!-- Include with URL (remote include) -->
<isinclude url="${URLUtils.url('Product-GetPrice', 'pid', product.ID)}"/>

Decorator Pattern

Base decorator (layouts/pagelayout.isml):

<!DOCTYPE html>
<html>
<head>
    <title>${pdict.pageTitle}</title>
</head>
<body>
    <header>
        <isinclude template="components/header"/>
    </header>
    <main>
        <isreplace/>  <!-- Content inserted here -->
    </main>
    <footer>
        <isinclude template="components/footer"/>
    </footer>
</body>
</html>


Page using decorator:

<isdecorate template="layouts/pagelayout">
    <isslot id="home-banner" context="global"/>
    <div class="homepage-content">
        <h1>${pdict.welcomeMessage}</h1>
    </div>
</isdecorate>

Expressions

Expressions use ${...} syntax to embed dynamic values:

<!-- Property access -->
${product.name}
${product.price.sales.value}

<!-- Method calls -->
${product.getAvailabilityModel().isInStock()}

<!-- Built-in objects -->
${pdict.myVariable}           <!-- Controller data -->
${session.customer.firstName} <!-- Session data -->
${request.httpParameterMap.pid.stringValue}

<!-- Operators -->
${price > 100 ? 'expensive' : 'affordable'}
${firstName + ' ' + lastName}
${quantity * unitPrice}

Built-in Utilities
URLUtils
<!-- Controller URL -->
<a href="${URLUtils.url('Product-Show', 'pid', product.ID)}">View</a>

<!-- HTTPS URL -->
<a href="${URLUtils.https('Account-Show')}">My Account</a>

<!-- Static resource -->
<img src="${URLUtils.staticURL('/images/logo.png')}" alt="Logo"/>

<!-- Absolute URL -->
<a href="${URLUtils.abs('Home-Show')}">Home</a>

Resource (Localization)
<!-- Get localized string -->
${Resource.msg('button.addtocart', 'product', null)}

<!-- With parameters -->
${Resource.msgf('cart.items', 'cart', null, cartCount)}

StringUtils
<!-- Truncate text -->
${StringUtils.truncate(description, 100, '...')}

<!-- Format number -->
${StringUtils.formatNumber(quantity, '###,###')}

Custom Modules

Define reusable custom tags in util/modules.isml:

<!-- Definition in util/modules.isml -->
<ismodule template="components/productcard"
          name="productcard"
          attribute="product"
          attribute="showPrice"
          attribute="showRating"/>

<!-- Usage in any template -->
<isinclude template="util/modules"/>
<isproductcard product="${product}" showPrice="${true}" showRating="${true}"/>


Component template (components/productcard.isml):

<div class="product-card">
    <img src="${product.image.url}" alt="${product.name}"/>
    <h3>${product.name}</h3>
    <isif condition="${pdict.showPrice}">
        <span class="price">${product.price.sales.formatted}</span>
    </isif>
    <isif condition="${pdict.showRating && product.rating}">
        <span class="rating">${product.rating} stars</span>
    </isif>
</div>

Caching
<!-- Cache for 24 hours -->
<iscache type="relative" hour="24"/>

<!-- Daily cache (expires at midnight) -->
<iscache type="daily" hour="0" minute="0"/>

<!-- Vary cache by parameter -->
<iscache type="relative" hour="1" varyby="price_promotion"/>


Place <iscache> at the beginning of the template.

Content Type
<!-- Set content type (must be first in template) -->
<iscontent type="text/html" charset="UTF-8"/>

<!-- For JSON responses -->
<iscontent type="application/json" charset="UTF-8"/>

<!-- For XML -->
<iscontent type="application/xml" charset="UTF-8"/>

Embedded Scripts
<isscript>
    var ProductMgr = require('dw/catalog/ProductMgr');
    var product = ProductMgr.getProduct(pdict.pid);
    var price = product.priceModel.price;
</isscript>

<span>${price.toFormattedString()}</span>


Best Practice: Keep <isscript> blocks minimal. Move complex logic to controllers or helper scripts.

Comments
<!-- HTML comment (visible in source) -->

<iscomment>
    ISML comment - stripped from output.
    Use for documentation and hiding sensitive info.
</iscomment>

Tag Location Constraints

Not all ISML tags can be used anywhere. Important constraints:

Tag	Allowed Location
<iscontent>	Must be before DOCTYPE declaration
<isredirect>	Must be before DOCTYPE declaration
<isprint>	Only in <body>
<isbreak>	Only in <body>, inside <isloop>
<iscontinue>	Only in <body>, inside <isloop>
<isnext>	Inside <isloop>
<isreplace>	Must be within <isdecorate> tags
<isactivedatahead>	Only in <head>

Tags that can be used anywhere: <isif>, <isloop>, <isinclude>, <isset>, <isremove>, <iscache>, <iscomment>, <ismodule>, <iscookie>, <isstatus>.

Best Practices
Use <iscomment> instead of HTML comments for sensitive info
Place <iscontent> first in templates that need it
Define modules in util/modules.isml for consistency
Keep templates simple - move logic to controllers/helpers
Use decorators for consistent page layouts
Enable caching on cacheable pages with <iscache>
Encode output - default encoding prevents XSS
Detailed Reference

For comprehensive tag documentation:

Tags Reference - All ISML tags with examples
Expressions Reference - Expression syntax and built-in functions
Weekly Installs
82
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