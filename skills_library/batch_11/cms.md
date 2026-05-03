---
title: cms
url: https://skills.sh/vercel-labs/vercel-plugin/cms
---

# cms

skills/vercel-labs/vercel-plugin/cms
cms
Installation
$ npx skills add https://github.com/vercel-labs/vercel-plugin --skill cms
SKILL.md
Headless CMS Integration

You are an expert in integrating headless CMS platforms with Vercel-deployed applications — covering Sanity (native Vercel Marketplace), Contentful, DatoCMS, Storyblok, and Builder.io.

Sanity (Native Vercel Marketplace Integration)

Sanity is the primary CMS integration on the Vercel Marketplace with first-class Visual Editing support.

Install via Marketplace
# Install Sanity from Vercel Marketplace (auto-provisions env vars)
vercel integration add sanity


Auto-provisioned environment variables:

SANITY_PROJECT_ID — Sanity project identifier
SANITY_DATASET — dataset name (usually production)
SANITY_API_TOKEN — read/write API token
NEXT_PUBLIC_SANITY_PROJECT_ID — client-side project ID
NEXT_PUBLIC_SANITY_DATASET — client-side dataset name
SDK Setup
# Install Sanity packages for Next.js
npm install next-sanity @sanity/client @sanity/image-url

# For embedded studio (optional)
npm install sanity @sanity/vision

Client Configuration
// lib/sanity.ts
import { createClient } from "next-sanity";

export const client = createClient({
  projectId: process.env.NEXT_PUBLIC_SANITY_PROJECT_ID!,
  dataset: process.env.NEXT_PUBLIC_SANITY_DATASET!,
  apiVersion: "2026-03-01",
  useCdn: true,
});

Content Schema
// schemas/post.ts
import { defineType, defineField } from "sanity";

export const post = defineType({
  name: "post",
  title: "Post",
  type: "document",
  fields: [
    defineField({ name: "title", type: "string" }),
    defineField({ name: "slug", type: "slug", options: { source: "title" } }),
    defineField({ name: "body", type: "array", of: [{ type: "block" }] }),
    defineField({ name: "mainImage", type: "image", options: { hotspot: true } }),
    defineField({ name: "publishedAt", type: "datetime" }),
  ],
});

Embedded Studio (App Router)
// app/studio/[[...tool]]/page.tsx
"use client";
import { NextStudio } from "next-sanity/studio";
import config from "@/sanity.config";

export default function StudioPage() {
  return <NextStudio config={config} />;
}

// sanity.config.ts
import { defineConfig } from "sanity";
import { structureTool } from "sanity/structure";
import { visionTool } from "@sanity/vision";
import { post } from "./schemas/post";

export default defineConfig({
  name: "default",
  title: "My Studio",
  projectId: process.env.NEXT_PUBLIC_SANITY_PROJECT_ID!,
  dataset: process.env.NEXT_PUBLIC_SANITY_DATASET!,
  plugins: [structureTool(), visionTool()],
  schema: { types: [post] },
});

Live Content with defineLive() (next-sanity v12)

Use defineLive() for automatic real-time content updates without manual revalidation. In next-sanity v11+, defineLive must be imported from the next-sanity/live subpath:

// lib/sanity.ts
import { createClient } from "next-sanity";
import { defineLive } from "next-sanity/live";

const client = createClient({
  projectId: process.env.NEXT_PUBLIC_SANITY_PROJECT_ID!,
  dataset: process.env.NEXT_PUBLIC_SANITY_DATASET!,
  apiVersion: "2026-03-01",
  useCdn: true,
});

export const { sanityFetch, SanityLive } = defineLive({
  client,
  // Required for draft content in Visual Editing — use a Viewer role token
  serverToken: process.env.SANITY_API_TOKEN,
  // Optional but recommended for faster live preview
  browserToken: process.env.SANITY_BROWSER_TOKEN,
});

// app/page.tsx
import { sanityFetch, SanityLive } from "@/lib/sanity";

export default async function Page() {
  const { data: posts } = await sanityFetch({ query: `*[_type == "post"]` });
  return (
    <>
      {posts.map((post) => <div key={post._id}>{post.title}</div>)}
      <SanityLive />
    </>
  );
}


Breaking change in v12: defineLive({fetchOptions: {revalidate}}) has been removed. defineLive({stega}) is deprecated.

Visual Editing (Presentation Mode)

Sanity Visual Editing lets content editors click-to-edit content directly on the live site preview. Requires Sanity Studio v5+ (React 19.2) and @sanity/visual-editing v5+.

npm install @sanity/visual-editing


In next-sanity v11+, VisualEditing must be imported from the next-sanity/visual-editing subpath:

// app/layout.tsx
import { VisualEditing } from "next-sanity/visual-editing";
import { draftMode } from "next/headers";

export default async function RootLayout({ children }: { children: React.ReactNode }) {
  const { isEnabled } = await draftMode();
  return (
    <html>
      <body>
        {children}
        {isEnabled && <VisualEditing />}
      </body>
    </html>
  );
}

On-Demand Revalidation Webhook
// app/api/revalidate/route.ts
import { revalidateTag } from "next/cache";
import { parseBody } from "next-sanity/webhook";

export async function POST(req: Request) {
  const { isValidSignature, body } = await parseBody<{
    _type: string;
    slug?: { current?: string };
  }>(req, process.env.SANITY_REVALIDATE_SECRET);

  if (!isValidSignature) {
    return Response.json({ message: "Invalid signature" }, { status: 401 });
  }

  if (body?._type) {
    revalidateTag(body._type);
  }

  return Response.json({ revalidated: true, now: Date.now() });
}


Configure the webhook in Sanity at Settings → API → Webhooks pointing to https://your-site.vercel.app/api/revalidate.

Contentful
npm install contentful

// lib/contentful.ts
import { createClient } from "contentful";

export const contentful = createClient({
  space: process.env.CONTENTFUL_SPACE_ID!,
  accessToken: process.env.CONTENTFUL_ACCESS_TOKEN!,
});

Fetching Entries
// app/page.tsx
import { contentful } from "@/lib/contentful";

export default async function Page() {
  const entries = await contentful.getEntries({ content_type: "blogPost" });
  return (
    <ul>
      {entries.items.map((entry) => (
        <li key={entry.sys.id}>{entry.fields.title as string}</li>
      ))}
    </ul>
  );
}

Draft Mode (Preview)

All CMS integrations should use Next.js Draft Mode for preview:

// app/api/draft/route.ts
import { draftMode } from "next/headers";

export async function GET(req: Request) {
  const { searchParams } = new URL(req.url);
  const secret = searchParams.get("secret");

  if (secret !== process.env.DRAFT_SECRET) {
    return Response.json({ message: "Invalid token" }, { status: 401 });
  }

  const draft = await draftMode();
  draft.enable();

  const slug = searchParams.get("slug") ?? "/";
  return Response.redirect(new URL(slug, req.url));
}

Environment Variables
Variable	Scope	CMS	Description
SANITY_PROJECT_ID / NEXT_PUBLIC_SANITY_PROJECT_ID	Server / Client	Sanity	Project identifier
SANITY_DATASET / NEXT_PUBLIC_SANITY_DATASET	Server / Client	Sanity	Dataset name
SANITY_API_TOKEN	Server	Sanity	Read/write token
SANITY_REVALIDATE_SECRET	Server	Sanity	Webhook secret for revalidation
CONTENTFUL_SPACE_ID	Server	Contentful	Space identifier
CONTENTFUL_ACCESS_TOKEN	Server	Contentful	Delivery API token
CONTENTFUL_PREVIEW_TOKEN	Server	Contentful	Preview API token
DATOCMS_API_TOKEN	Server	DatoCMS	Read-only API token
Cross-References
Marketplace install and env var provisioning → ⤳ skill: marketplace
On-demand revalidation and caching → ⤳ skill: runtime-cache
Draft mode and middleware patterns → ⤳ skill: routing-middleware
Environment variable management → ⤳ skill: env-vars
Image optimization → ⤳ skill: nextjs
Official Documentation
Sanity + Vercel Marketplace
next-sanity Documentation (v12)
next-sanity v11→v12 Migration
Sanity Visual Editing
Contentful JavaScript SDK
Next.js Draft Mode
Weekly Installs
30
Repository
vercel-labs/ver…l-plugin
GitHub Stars
156
First Seen
Mar 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass