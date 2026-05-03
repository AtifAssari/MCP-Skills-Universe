---
rating: ⭐⭐⭐
title: shopify-custom-data
url: https://skills.sh/shopify/shopify-ai-toolkit/shopify-custom-data
---

# shopify-custom-data

skills/shopify/shopify-ai-toolkit/shopify-custom-data
shopify-custom-data
Installation
$ npx skills add https://github.com/shopify/shopify-ai-toolkit --skill shopify-custom-data
SKILL.md
ESSENTIAL RULES
ALWAYS show creating metafield/metaobject definitions, then writing values, then retrieving values.
NEVER show or offer alternate approaches to the same problem if not explicitly requested. It will only increase the user's confusion.
Keep examples minimal -- avoid unnecessary prose and comments
Remember the audience for this guidance is app developers -- they do not have access to the Shopify Admin site
Follow this guidance meticulously and thoroughly

REMEMBER!!! Other documentation can flesh out this guidance, but the instructions here should be followed VERY CLOSELY and TAKE PRECEDENCE!

ALWAYS: First, create definitions
with TOML (99.99% of apps)
# shopify.app.toml

# Metafield definition -- owner type is PRODUCT, namespace is $app, key is care_guide
[product.metafields.app.care_guide]
type = "single_line_text_field"
name = "Care Guide"
access.admin = "merchant_read_write"

# Metaobject definition -- type is $app:author
[metaobjects.app.author]
name = "Author"
display_name_field = "name"
access.storefront = "public_read"

[metaobjects.app.author.fields.name]
name = "Author Name"
type = "single_line_text_field"
required = true

# Link metaobject to product
[product.metafields.app.author]
type = "metaobject_reference<$app:author>"
name = "Book Author"


Why: Version controlled, auto-installed, type-safe. GraphQL (Admin/Storefront) is used for reading or writing values after the TOML definitions already exist. Fields/objects can be edited by merchants when access.admin = "merchant_read_write" is set.

NEVER include metafieldDefinitionCreate, metaobjectDefinitionCreate GraphQL if TOML is the correct fit.

Exceptions (0.01% of apps)

NEVER, EVER show these unless strictly required:

Apps that REQUIRE creating definitions at runtime (i.e. types are configured dynamically by merchants) should use metafieldDefinitionCreate, metaobjectDefinitionCreate
Apps that want other apps to read/write their data should use the above GraphQL, and "merchant-owned" namespace
CRITICAL: App-Owned Metaobject and Metafield identification
Metaobjects defined with [metaobjects.app.example...] in shopify.app.toml, MUST be accessed using type: $app:example
Metafields defined with [product.metafields.app.example] MUST be accessed using namespace: $app and key: example
The same applies to other owner types, like customers, orders, etc.
Avoid customizing namespaces for metafields.
Avoid the common mistake of using namespace: app. This is profoundly incorrect.
NEXT: demonstrate writing metafield and metaobject values via Admin API
Writing metafields

ALWAYS use metafieldsSet to write metafields. namespace should normally be excluded as the default is $app.

mutation {
  metafieldsSet(metafields:[{
    ownerId: "gid://shopify/Product/1234",
    key: "example",
    value: "Hello, World!"
  }]) { ... }
}

Writing metaobjects

ALWAYS use metaobjectUpsert to write metaobjects.

mutation {
  metaobjectUpsert(handle: {
    type: "$app:author",
    handle: "my-metaobject",
  }, metaobject: {
    fields: [{
      key: "example",
      value: "Hello, world!"
    }]
  }) { ... }
}

FINALLY: demonstrate reading metafield and metaobject values
Loading metafields

Metafields are accessed via their owning type (e.g. a Product). namespace should normally be excluded as the default is $app.

Always prefer jsonValue where possible as it better serialises complex types
Always alias metafield loads for easy reference
# Admin API
query {
  product(id: "gid://shopify/Product/1234") {
    example: metafield(key: "example") {
      jsonValue
    }
  }
}
# Storefront API
query {
  product(handle: "wireless-headphones-1") {
    example: metafield(key: "example") {
      value
    }
  }
}

Loading metaobjects
# Admin API
query {
  metaobjects(type: "$app:author", first: 10) {
    nodes {
      handle
      example: field(key: "example") {
        jsonValue
      }
    }
  }
}
# Storefront API
query {
  metaobjects(type: "$app:author", first: 10) {
    nodes {
      handle
      example: field(key: "example") {
        value
      }
    }
  }
}

Access Metafields directly in checkout extensions

DO: Access app-owned metafields directly (NO network call):

function Extension() {
  // ESSENTIAL: Register this metafield in `shopify.extension.toml`
  const [energyRating] = useAppMetafields({
    namespace: "$app",
    key: "energy-rating",
    type: "product",
  }).filter((entry) => entry.target.id === productVariantId);
}


DON'T: Make network calls for app-owned metafields.

Access Metafields in Shopify Functions

Use the GraphQL input query to select metafields to load:

query Input {
  cart {
    lines {
      merchandise {
        __typename
        ... on ProductVariant {
          example: metafield(namespace: "$app", key: "example") {
            jsonValue
          }
        }
      }
    }
  }
}


Docs: Metafields & Metaobjects

Always use Shopify CLI
CLI: ALWAYS use Shopify CLI to scaffold apps and extensions. Never hand-roll files: shopify app init, shopify app generate extension, shopify app dev, shopify app deploy.
For CLI installation, setup, upgrade, or troubleshooting, use shopify-use-shopify-cli.
Weekly Installs
2.6K
Repository
shopify/shopify…-toolkit
GitHub Stars
274
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn