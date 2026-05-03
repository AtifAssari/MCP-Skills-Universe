---
rating: ⭐⭐
title: shopify-admin-graphql
url: https://skills.sh/tamiror6/shopify-app-skills/shopify-admin-graphql
---

# shopify-admin-graphql

skills/tamiror6/shopify-app-skills/shopify-admin-graphql
shopify-admin-graphql
Installation
$ npx skills add https://github.com/tamiror6/shopify-app-skills --skill shopify-admin-graphql
SKILL.md
Shopify Admin GraphQL

Use this skill when adding or changing code that talks to the Shopify Admin API via GraphQL.

When to Use
Querying Shopify data (shop, customers, orders, products, inventory)
Mutating Shopify data (creating/updating customers, orders, products)
Implementing pagination for large datasets
Handling API throttling and rate limits
Working with metafields or other Shopify resources
Getting the GraphQL Client
In Remix Loaders/Actions (Recommended)

Use authenticate.admin() from @shopify/shopify-app-remix:

import { authenticate } from "../shopify.server";

export const loader = async ({ request }: LoaderFunctionArgs) => {
  const { admin } = await authenticate.admin(request);
  
  const response = await admin.graphql(`
    query GetShopDetails {
      shop {
        id
        name
        myshopifyDomain
        plan {
          displayName
        }
      }
    }
  `);
  
  const { data } = await response.json();
  return json({ shop: data.shop });
};

With Variables
export const action = async ({ request }: ActionFunctionArgs) => {
  const { admin } = await authenticate.admin(request);
  const formData = await request.formData();
  const email = formData.get("email") as string;
  
  // Validate email format to prevent query manipulation
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!email || !emailRegex.test(email)) {
    return json({ error: "Invalid email format" }, { status: 400 });
  }
  
  // Escape quotes and wrap in quotes to treat as literal value
  const sanitizedEmail = email.replace(/"/g, '\\"');
  
  const response = await admin.graphql(`
    query FindCustomerByEmail($query: String!) {
      customers(first: 1, query: $query) {
        edges {
          node {
            id
            email
            phone
            firstName
            lastName
          }
        }
      }
    }
  `, {
    variables: { query: `email:"${sanitizedEmail}"` }
  });
  
  const { data } = await response.json();
  return json({ customer: data.customers.edges[0]?.node });
};

Background Jobs / Webhooks (Offline Access)

When you don't have a request context, use offline session tokens:

import { unauthenticated } from "../shopify.server";

export async function processWebhook(shop: string) {
  const { admin } = await unauthenticated.admin(shop);
  
  const response = await admin.graphql(`
    query GetShop {
      shop {
        name
      }
    }
  `);
  
  const { data } = await response.json();
  return data.shop;
}

Common Query Patterns
Shop Details
query GetShopDetails {
  shop {
    id
    name
    email
    myshopifyDomain
    primaryDomain {
      url
    }
    plan {
      displayName
    }
    currencyCode
    timezoneAbbreviation
  }
}

Products with Pagination
query GetProducts($first: Int!, $after: String) {
  products(first: $first, after: $after) {
    pageInfo {
      hasNextPage
      endCursor
    }
    edges {
      node {
        id
        title
        handle
        status
        variants(first: 10) {
          edges {
            node {
              id
              title
              price
              sku
            }
          }
        }
      }
    }
  }
}

Customer Lookup
query FindCustomer($query: String!) {
  customers(first: 1, query: $query) {
    edges {
      node {
        id
        email
        phone
        firstName
        lastName
        ordersCount
        totalSpent
      }
    }
  }
}

Order by ID
query GetOrder($id: ID!) {
  order(id: $id) {
    id
    name
    email
    phone
    totalPriceSet {
      shopMoney {
        amount
        currencyCode
      }
    }
    lineItems(first: 50) {
      edges {
        node {
          title
          quantity
          variant {
            id
            sku
          }
        }
      }
    }
    shippingAddress {
      address1
      city
      country
    }
  }
}

Handling Throttling

Shopify uses a leaky bucket algorithm for rate limiting. For bulk operations or background jobs, implement retry logic:

interface RetryOptions {
  maxRetries?: number;
  initialDelay?: number;
  maxDelay?: number;
}

async function executeWithRetry<T>(
  admin: AdminApiContext,
  query: string,
  variables?: Record<string, unknown>,
  options: RetryOptions = {}
): Promise<T> {
  const { maxRetries = 3, initialDelay = 1000, maxDelay = 10000 } = options;
  
  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      const response = await admin.graphql(query, { variables });
      const result = await response.json();
      
      if (result.errors?.some((e: any) => e.extensions?.code === "THROTTLED")) {
        throw new Error("THROTTLED");
      }
      
      return result.data as T;
    } catch (error) {
      if (attempt === maxRetries) throw error;
      
      const delay = Math.min(initialDelay * Math.pow(2, attempt), maxDelay);
      await new Promise(resolve => setTimeout(resolve, delay));
    }
  }
  
  throw new Error("Max retries exceeded");
}

Error Handling
const response = await admin.graphql(query, { variables });
const { data, errors } = await response.json();

if (errors) {
  // Handle GraphQL errors
  console.error("GraphQL errors:", errors);
  
  // Check for specific error types
  const throttled = errors.some((e: any) => 
    e.extensions?.code === "THROTTLED"
  );
  
  const notFound = errors.some((e: any) => 
    e.message?.includes("not found")
  );
  
  if (throttled) {
    // Retry with backoff
  }
}

Best Practices
Use operation names for debugging: query GetShopDetails { ... }
Request only needed fields to reduce response size and improve performance
Use pagination for lists - never request unbounded data
Handle errors gracefully - check for both errors array and HTTP errors
Implement retries with exponential backoff for background jobs
Use fragments for repeated field selections across queries
Prefer GraphQL over REST for complex queries with relationships
References
Shopify Admin GraphQL API
GraphQL Basics
Rate Limits
@shopify/shopify-app-remix
Weekly Installs
84
Repository
tamiror6/shopif…p-skills
GitHub Stars
34
First Seen
Feb 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass