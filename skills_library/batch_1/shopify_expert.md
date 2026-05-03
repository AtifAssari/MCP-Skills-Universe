---
title: shopify-expert
url: https://skills.sh/jeffallan/claude-skills/shopify-expert
---

# shopify-expert

skills/jeffallan/claude-skills/shopify-expert
shopify-expert
Installation
$ npx skills add https://github.com/jeffallan/claude-skills --skill shopify-expert
Summary

Complete Shopify development expertise for themes, apps, headless storefronts, and checkout customization.

Covers theme development with Liquid templating, Storefront API integration, and Online Store 2.0 architecture; includes linting and deployment via Shopify CLI
Supports full-stack app development with OAuth, webhooks, Admin API authentication, and checkout UI extensions using TypeScript and Remix
Provides GraphQL query patterns, metafield handling, image optimization, and performance tuning for both traditional and headless commerce
Includes validation workflows (theme check, sandbox testing) and enforces constraints around API rate limits, GDPR compliance, and deprecated endpoint avoidance
SKILL.md
Shopify Expert

Senior Shopify developer with expertise in theme development, headless commerce, app architecture, and custom checkout solutions.

Core Workflow
Requirements analysis — Identify if theme, app, or headless approach fits needs
Architecture setup — Scaffold with shopify theme init or shopify app create; configure shopify.app.toml and theme schema
Implementation — Build Liquid templates, write GraphQL queries, or develop app features (see examples below)
Validation — Run shopify theme check for Liquid linting; if errors are found, fix them and re-run before proceeding. Run shopify app dev to verify app locally; test checkout extensions in sandbox. If validation fails at any step, resolve all reported issues before moving to deployment
Deploy and monitor — shopify theme push for themes; shopify app deploy for apps; watch Shopify error logs and performance metrics post-deploy
Reference Guide

Load detailed guidance based on context:

Topic	Reference	Load When
Liquid Templating	references/liquid-templating.md	Theme development, template customization
Storefront API	references/storefront-api.md	Headless commerce, Hydrogen, custom frontends
App Development	references/app-development.md	Building Shopify apps, OAuth, webhooks
Checkout Extensions	references/checkout-customization.md	Checkout UI extensions, Shopify Functions
Performance	references/performance-optimization.md	Theme speed, asset optimization, caching
Code Examples
Liquid — Product template with metafield access
{% comment %} templates/product.liquid {% endcomment %}
<h1>{{ product.title }}</h1>
<p>{{ product.metafields.custom.care_instructions.value }}</p>

{% for variant in product.variants %}
  <option
    value="{{ variant.id }}"
    {% unless variant.available %}disabled{% endunless %}
  >
    {{ variant.title }} — {{ variant.price | money }}
  </option>
{% endfor %}

{{ product.description | metafield_tag }}

Liquid — Collection filtering (Online Store 2.0)
{% comment %} sections/collection-filters.liquid {% endcomment %}
{% for filter in collection.filters %}
  <details>
    <summary>{{ filter.label }}</summary>
    {% for value in filter.values %}
      <label>
        <input
          type="checkbox"
          name="{{ value.param_name }}"
          value="{{ value.value }}"
          {% if value.active %}checked{% endif %}
        >
        {{ value.label }} ({{ value.count }})
      </label>
    {% endfor %}
  </details>
{% endfor %}

Storefront API — GraphQL product query
query ProductByHandle($handle: String!) {
  product(handle: $handle) {
    id
    title
    descriptionHtml
    featuredImage {
      url(transform: { maxWidth: 800, preferredContentType: WEBP })
      altText
    }
    variants(first: 10) {
      edges {
        node {
          id
          title
          price { amount currencyCode }
          availableForSale
          selectedOptions { name value }
        }
      }
    }
    metafield(namespace: "custom", key: "care_instructions") {
      value
      type
    }
  }
}

Shopify CLI — Common commands
# Theme development
shopify theme dev --store=your-store.myshopify.com   # Live preview with hot reload
shopify theme check                                   # Lint Liquid for errors/warnings
shopify theme push --only templates/ sections/        # Partial push
shopify theme pull                                    # Sync remote changes locally

# App development
shopify app create node                               # Scaffold Node.js app
shopify app dev                                       # Local dev with ngrok tunnel
shopify app deploy                                    # Submit app version
shopify app generate extension                        # Add checkout UI extension

# GraphQL
shopify app generate graphql                          # Generate typed GraphQL hooks

App — Authenticated Admin API fetch (TypeScript)
import { authenticate } from "../shopify.server";
import type { LoaderFunctionArgs } from "@remix-run/node";

export const loader = async ({ request }: LoaderFunctionArgs) => {
  const { admin } = await authenticate.admin(request);

  const response = await admin.graphql(`
    query {
      shop { name myshopifyDomain plan { displayName } }
    }
  `);

  const { data } = await response.json();
  return data.shop;
};

Constraints
MUST DO
Use Liquid 2.0 syntax for themes
Implement proper metafield handling
Use Storefront API 2024-10 or newer
Optimize images with Shopify CDN filters
Follow Shopify CLI workflows
Use App Bridge for embedded apps
Implement proper error handling for API calls
Follow Shopify theme architecture patterns
Use TypeScript for app development
Test checkout extensions in sandbox
Run shopify theme check before every theme deployment
MUST NOT DO
Hardcode API credentials in theme code
Exceed Storefront API rate limits (2000 points/sec)
Use deprecated REST Admin API endpoints
Skip GDPR compliance for customer data
Deploy untested checkout extensions
Use synchronous API calls in Liquid (deprecated)
Ignore theme performance metrics
Store sensitive data in metafields without encryption
Output Templates

When implementing Shopify solutions, provide:

Complete file structure with proper naming
Liquid/GraphQL/TypeScript code with types
Configuration files (shopify.app.toml, schema settings)
API scopes and permissions needed
Testing approach and deployment steps
Knowledge Reference

Shopify CLI 3.x, Liquid 2.0, Storefront API 2024-10, Admin API, GraphQL, Hydrogen 2024, Remix, Oxygen, Polaris, App Bridge 4.0, Checkout UI Extensions, Shopify Functions, metafields, metaobjects, theme architecture, Shopify Plus features

Documentation

Weekly Installs
2.5K
Repository
jeffallan/claude-skills
GitHub Stars
8.7K
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass