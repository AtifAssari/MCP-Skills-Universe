---
title: nextjs-supabase-saas-planner
url: https://skills.sh/sitechfromgeorgia/georgian-distribution-system/nextjs-supabase-saas-planner
---

# nextjs-supabase-saas-planner

skills/sitechfromgeorgia/georgian-distribution-system/nextjs-supabase-saas-planner
nextjs-supabase-saas-planner
Installation
$ npx skills add https://github.com/sitechfromgeorgia/georgian-distribution-system --skill nextjs-supabase-saas-planner
SKILL.md
Next.js + Supabase SaaS Planner
Overview

Expert SaaS planning assistant that transforms product ideas into actionable technical roadmaps. Specializes in the Next.js 15 + Supabase stack, covering architecture design, database schemas, authentication patterns, multi-tenancy, billing integration, and launch strategies.

When to use this skill:

Planning a new SaaS product from scratch
Converting a product idea into technical specifications
Designing database schemas for SaaS applications
Setting up authentication and authorization
Implementing multi-tenant architecture
Integrating subscription billing (Stripe, Paddle)
Planning feature rollout and MVP priorities
Creating development roadmaps and timelines
Planning Workflow
Phase 1: Discovery and Requirements

Ask these questions first:

Product Overview

What problem does your SaaS solve?
Who is your target user?
What's your unique value proposition?

Scale Expectations

How many users in first year? (0-1K, 1K-10K, 10K-100K, 100K+)
Expected growth rate?
Geographic distribution?

Team and Timeline

Team size and skills?
Launch timeline? (MVP date)
Budget constraints?

Business Model

Pricing tiers?
Free trial or freemium?
What features differentiate paid tiers?

Core Features

Must-have features for MVP?
Nice-to-have features for v1.1?
Future roadmap ideas?
Phase 2: Technical Architecture Planning

Based on requirements, create:

System Architecture Diagram
Database Schema
File/Folder Structure
Authentication Flow
Multi-Tenancy Strategy (if applicable)
Billing Integration Plan
Deployment Architecture
Phase 3: Development Roadmap

Create week-by-week plan:

Week 1-2: Setup and infrastructure
Week 3-4: Core features
Week 5-6: Authentication and billing
Week 7-8: Polish and testing
Week 9: Launch preparation
Next.js 15 + Supabase Stack (2025)
Recommended Tech Stack
Frontend:
├─ Next.js 15 (App Router)
├─ React 19
├─ TypeScript
├─ Tailwind CSS
└─ shadcn/ui components

Backend:
├─ Next.js API Routes (Server Actions)
├─ Supabase Edge Functions (when needed)
└─ Stripe/Paddle webhooks

Database:
├─ PostgreSQL (Supabase)
├─ Row Level Security (RLS)
└─ Supabase Realtime (optional)

Authentication:
├─ Supabase Auth
├─ OAuth providers (Google, GitHub, etc.)
└─ Magic links

Storage:
└─ Supabase Storage (files, images)

Deployment:
├─ Vercel (frontend + API)
├─ Supabase (database, auth, storage)
└─ Cloudflare (CDN, DNS)

Payments:
├─ Stripe (recommended)
└─ Paddle (alternative)

Monitoring:
├─ Vercel Analytics
├─ Sentry (error tracking)
└─ PostHog (product analytics - optional)

Why This Stack?

Next.js 15:

Server Components for performance
Server Actions for mutations
Built-in caching strategies
Excellent DX and fast iteration

Supabase:

Instant REST API
Real-time subscriptions
Built-in authentication
Row-level security
Open source (no vendor lock-in risk)

TypeScript:

Type safety reduces bugs
Better IDE support
Self-documenting code

Stripe:

Industry standard for payments
Excellent documentation
Subscription management
Invoice handling
File Structure Template
my-saas/
├─ app/
│  ├─ (auth)/
│  │  ├─ login/
│  │  │  └─ page.tsx
│  │  ├─ signup/
│  │  │  └─ page.tsx
│  │  ├─ forgot-password/
│  │  │  └─ page.tsx
│  │  └─ layout.tsx
│  │
│  ├─ (marketing)/
│  │  ├─ page.tsx                 # Landing page
│  │  ├─ pricing/
│  │  │  └─ page.tsx
│  │  ├─ about/
│  │  │  └─ page.tsx
│  │  └─ layout.tsx
│  │
│  ├─ (dashboard)/
│  │  ├─ dashboard/
│  │  │  └─ page.tsx
│  │  ├─ settings/
│  │  │  ├─ profile/
│  │  │  │  └─ page.tsx
│  │  │  ├─ billing/
│  │  │  │  └─ page.tsx
│  │  │  └─ team/
│  │  │     └─ page.tsx
│  │  └─ layout.tsx
│  │
│  ├─ api/
│  │  ├─ webhooks/
│  │  │  └─ stripe/
│  │  │     └─ route.ts
│  │  └─ og/                     # Open Graph images
│  │     └─ route.tsx
│  │
│  ├─ layout.tsx                  # Root layout
│  └─ globals.css
│
├─ components/
│  ├─ ui/                         # shadcn components
│  │  ├─ button.tsx
│  │  ├─ card.tsx
│  │  ├─ dialog.tsx
│  │  └─ ...
│  ├─ auth/
│  │  ├─ login-form.tsx
│  │  └─ signup-form.tsx
│  ├─ dashboard/
│  │  ├─ sidebar.tsx
│  │  └─ navbar.tsx
│  ├─ marketing/
│  │  ├─ hero.tsx
│  │  ├─ features.tsx
│  │  └─ pricing-cards.tsx
│  └─ shared/
│     ├─ user-avatar.tsx
│     └─ loading-spinner.tsx
│
├─ lib/
│  ├─ supabase/
│  │  ├─ client.ts              # Client-side Supabase
│  │  ├─ server.ts              # Server-side Supabase
│  │  └─ middleware.ts          # Auth middleware
│  ├─ stripe/
│  │  ├─ client.ts
│  │  └─ server.ts
│  ├─ db/
│  │  └─ queries.ts             # Database queries
│  ├─ auth.ts                   # Auth helpers
│  └─ utils.ts                  # General utilities
│
├─ hooks/
│  ├─ use-user.ts               # User session hook
│  ├─ use-subscription.ts       # Subscription status
│  └─ use-toast.ts
│
├─ actions/                      # Server Actions
│  ├─ auth/
│  │  ├─ login.ts
│  │  ├─ signup.ts
│  │  └─ logout.ts
│  ├─ billing/
│  │  ├─ create-checkout.ts
│  │  └─ cancel-subscription.ts
│  └─ profile/
│     └─ update-profile.ts
│
├─ types/
│  ├─ database.ts               # Generated from Supabase
│  ├─ supabase.ts
│  └─ stripe.ts
│
├─ supabase/
│  ├─ migrations/               # Database migrations
│  │  └─ 20250101000000_initial.sql
│  ├─ functions/                # Edge Functions (optional)
│  └─ config.toml
│
├─ public/
│  ├─ images/
│  └─ icons/
│
├─ middleware.ts                 # Next.js middleware (auth)
├─ next.config.js
├─ tailwind.config.js
├─ tsconfig.json
├─ package.json
└─ .env.local

Database Schema Patterns
Core Tables for SaaS
-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Users table (extended from Supabase auth.users)
CREATE TABLE profiles (
  id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  email TEXT UNIQUE NOT NULL,
  full_name TEXT,
  avatar_url TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Organizations/Teams (multi-tenant)
CREATE TABLE organizations (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  name TEXT NOT NULL,
  slug TEXT UNIQUE NOT NULL,
  logo_url TEXT,
  subscription_tier TEXT DEFAULT 'free',
  subscription_status TEXT DEFAULT 'active',
  stripe_customer_id TEXT UNIQUE,
  stripe_subscription_id TEXT UNIQUE,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Organization memberships
CREATE TABLE organization_members (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  organization_id UUID REFERENCES organizations(id) ON DELETE CASCADE,
  user_id UUID REFERENCES profiles(id) ON DELETE CASCADE,
  role TEXT NOT NULL DEFAULT 'member', -- 'owner', 'admin', 'member'
  invited_by UUID REFERENCES profiles(id),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  UNIQUE(organization_id, user_id)
);

-- Subscription plans
CREATE TABLE plans (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  name TEXT NOT NULL,
  description TEXT,
  price_monthly DECIMAL(10,2),
  price_yearly DECIMAL(10,2),
  stripe_price_id_monthly TEXT,
  stripe_price_id_yearly TEXT,
  features JSONB,
  limits JSONB, -- { "users": 5, "projects": 10 }
  is_active BOOLEAN DEFAULT true,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Subscription usage tracking
CREATE TABLE usage_records (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  organization_id UUID REFERENCES organizations(id) ON DELETE CASCADE,
  metric TEXT NOT NULL, -- 'api_calls', 'storage_mb', 'users'
  value INTEGER NOT NULL,
  period_start DATE NOT NULL,
  period_end DATE NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Invitations
CREATE TABLE invitations (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  organization_id UUID REFERENCES organizations(id) ON DELETE CASCADE,
  email TEXT NOT NULL,
  role TEXT NOT NULL DEFAULT 'member',
  token TEXT UNIQUE NOT NULL,
  invited_by UUID REFERENCES profiles(id),
  expires_at TIMESTAMP WITH TIME ZONE NOT NULL,
  accepted_at TIMESTAMP WITH TIME ZONE,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Audit log (optional but recommended)
CREATE TABLE audit_logs (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  organization_id UUID REFERENCES organizations(id),
  user_id UUID REFERENCES profiles(id),
  action TEXT NOT NULL,
  resource_type TEXT,
  resource_id UUID,
  metadata JSONB,
  ip_address INET,
  user_agent TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_org_members_org ON organization_members(organization_id);
CREATE INDEX idx_org_members_user ON organization_members(user_id);
CREATE INDEX idx_usage_org_period ON usage_records(organization_id, period_start, period_end);
CREATE INDEX idx_invitations_token ON invitations(token);
CREATE INDEX idx_audit_logs_org ON audit_logs(organization_id);

Row Level Security (RLS) Policies
-- Enable RLS
ALTER TABLE profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE organizations ENABLE ROW LEVEL SECURITY;
ALTER TABLE organization_members ENABLE ROW LEVEL SECURITY;

-- Profiles: Users can read and update their own profile
CREATE POLICY "Users can view own profile"
  ON profiles FOR SELECT
  USING (auth.uid() = id);

CREATE POLICY "Users can update own profile"
  ON profiles FOR UPDATE
  USING (auth.uid() = id);

-- Organizations: Members can read their organizations
CREATE POLICY "Members can view their organizations"
  ON organizations FOR SELECT
  USING (
    id IN (
      SELECT organization_id 
      FROM organization_members 
      WHERE user_id = auth.uid()
    )
  );

-- Only owners can update organizations
CREATE POLICY "Owners can update organizations"
  ON organizations FOR UPDATE
  USING (
    id IN (
      SELECT organization_id 
      FROM organization_members 
      WHERE user_id = auth.uid() AND role = 'owner'
    )
  );

-- Organization members: Members can view other members
CREATE POLICY "Members can view team members"
  ON organization_members FOR SELECT
  USING (
    organization_id IN (
      SELECT organization_id 
      FROM organization_members 
      WHERE user_id = auth.uid()
    )
  );

Authentication Setup
Supabase Auth Configuration
// lib/supabase/client.ts
import { createBrowserClient } from '@supabase/ssr';

export function createClient() {
  return createBrowserClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
  );
}

// lib/supabase/server.ts
import { createServerClient, type CookieOptions } from '@supabase/ssr';
import { cookies } from 'next/headers';

export async function createClient() {
  const cookieStore = await cookies();

  return createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    {
      cookies: {
        get(name: string) {
          return cookieStore.get(name)?.value;
        },
        set(name: string, value: string, options: CookieOptions) {
          cookieStore.set({ name, value, ...options });
        },
        remove(name: string, options: CookieOptions) {
          cookieStore.set({ name, value: '', ...options });
        },
      },
    }
  );
}

Auth Middleware
// middleware.ts
import { createServerClient, type CookieOptions } from '@supabase/ssr';
import { NextResponse, type NextRequest } from 'next/server';

export async function middleware(request: NextRequest) {
  let response = NextResponse.next({
    request: {
      headers: request.headers,
    },
  });

  const supabase = createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    {
      cookies: {
        get(name: string) {
          return request.cookies.get(name)?.value;
        },
        set(name: string, value: string, options: CookieOptions) {
          response.cookies.set({
            name,
            value,
            ...options,
          });
        },
        remove(name: string, options: CookieOptions) {
          response.cookies.set({
            name,
            value: '',
            ...options,
          });
        },
      },
    }
  );

  const { data: { user } } = await supabase.auth.getUser();

  // Redirect to login if not authenticated
  if (!user && request.nextUrl.pathname.startsWith('/dashboard')) {
    return NextResponse.redirect(new URL('/login', request.url));
  }

  // Redirect to dashboard if already authenticated
  if (user && (
    request.nextUrl.pathname === '/login' ||
    request.nextUrl.pathname === '/signup'
  )) {
    return NextResponse.redirect(new URL('/dashboard', request.url));
  }

  return response;
}

export const config = {
  matcher: [
    '/((?!_next/static|_next/image|favicon.ico|.*\\.(?:svg|png|jpg|jpeg|gif|webp)$).*)',
  ],
};

Stripe Integration
Setup
// lib/stripe/server.ts
import Stripe from 'stripe';

export const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!, {
  apiVersion: '2024-11-20.acacia',
});

// Create checkout session
export async function createCheckoutSession(
  organizationId: string,
  priceId: string,
  userId: string
) {
  const session = await stripe.checkout.sessions.create({
    mode: 'subscription',
    payment_method_types: ['card'],
    line_items: [
      {
        price: priceId,
        quantity: 1,
      },
    ],
    success_url: `${process.env.NEXT_PUBLIC_APP_URL}/dashboard/billing?success=true`,
    cancel_url: `${process.env.NEXT_PUBLIC_APP_URL}/pricing`,
    client_reference_id: organizationId,
    metadata: {
      organizationId,
      userId,
    },
  });

  return session;
}

Webhook Handler
// app/api/webhooks/stripe/route.ts
import { headers } from 'next/headers';
import { NextResponse } from 'next/server';
import Stripe from 'stripe';
import { stripe } from '@/lib/stripe/server';
import { createClient } from '@/lib/supabase/server';

export async function POST(req: Request) {
  const body = await req.text();
  const signature = (await headers()).get('stripe-signature')!;

  let event: Stripe.Event;

  try {
    event = stripe.webhooks.constructEvent(
      body,
      signature,
      process.env.STRIPE_WEBHOOK_SECRET!
    );
  } catch (err) {
    return NextResponse.json({ error: 'Invalid signature' }, { status: 400 });
  }

  const supabase = await createClient();

  switch (event.type) {
    case 'checkout.session.completed':
      const session = event.data.object as Stripe.Checkout.Session;
      
      await supabase
        .from('organizations')
        .update({
          stripe_customer_id: session.customer as string,
          stripe_subscription_id: session.subscription as string,
          subscription_status: 'active',
        })
        .eq('id', session.metadata?.organizationId);
      break;

    case 'customer.subscription.updated':
      const subscription = event.data.object as Stripe.Subscription;
      
      await supabase
        .from('organizations')
        .update({
          subscription_status: subscription.status,
        })
        .eq('stripe_subscription_id', subscription.id);
      break;

    case 'customer.subscription.deleted':
      const deletedSub = event.data.object as Stripe.Subscription;
      
      await supabase
        .from('organizations')
        .update({
          subscription_status: 'canceled',
          subscription_tier: 'free',
        })
        .eq('stripe_subscription_id', deletedSub.id);
      break;
  }

  return NextResponse.json({ received: true });
}

Multi-Tenancy Patterns
Organization-Based (Recommended)

Pattern: Each organization has its own data space.

Benefits:

Clear data isolation
Easy to implement
Scalable per organization
Simple billing per organization

Implementation:

// All queries include organization_id
const { data } = await supabase
  .from('projects')
  .select('*')
  .eq('organization_id', currentOrgId);

Subdomain-Based (Advanced)

Pattern: Each organization has its own subdomain (e.g., acme.yourapp.com).

Benefits:

Better branding
Clear isolation
Professional appearance

Challenges:

DNS management
SSL certificates
More complex routing

Implementation:

// middleware.ts
export function middleware(request: NextRequest) {
  const hostname = request.headers.get('host')!;
  const subdomain = hostname.split('.')[0];
  
  // Fetch organization by subdomain
  // Set in request context
}

MVP Feature Prioritization
Week 1-2: Foundation
 Project setup (Next.js + Supabase)
 Database schema creation
 Authentication (email + OAuth)
 Basic layouts and routing
 Landing page
Week 3-4: Core Features
 Dashboard layout
 First core feature (main value prop)
 User profile management
 Organization/team creation
 Team member invitations
Week 5-6: Monetization
 Pricing page
 Stripe integration
 Subscription management
 Usage limits enforcement
 Billing page
Week 7-8: Polish
 Email notifications
 Error handling
 Loading states
 Responsive design
 SEO optimization
Week 9: Launch Prep
 Testing (E2E, unit)
 Security audit
 Performance optimization
 Documentation
 Deployment scripts
Environment Variables
# .env.local

# Supabase
NEXT_PUBLIC_SUPABASE_URL=https://xxxxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-service-key

# Stripe
STRIPE_SECRET_KEY=sk_test_xxxxx
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_test_xxxxx
STRIPE_WEBHOOK_SECRET=whsec_xxxxx

# App
NEXT_PUBLIC_APP_URL=http://localhost:3000

# Optional
SENTRY_DSN=your-sentry-dsn
POSTHOG_KEY=your-posthog-key

Deployment Checklist
Pre-Launch
 Environment variables configured
 Database migrations run
 RLS policies tested
 Stripe webhooks configured
 Domain configured
 SSL certificates active
 Analytics setup
 Error tracking (Sentry)
 Email service configured
 Terms of Service + Privacy Policy pages
Post-Launch
 Monitor error rates
 Check subscription flows
 Test webhook delivery
 Monitor database performance
 Set up backups
 Create status page
 Implement feature flags
Best Practices
Performance
Use Server Components by default
Implement proper caching strategies
Optimize images with next/image
Use React Server Actions for mutations
Lazy load heavy components
Security
Always use RLS policies
Validate inputs on server
Never expose service role key to client
Use prepared statements (Supabase handles this)
Implement rate limiting for sensitive endpoints
Development
Use TypeScript strictly
Write tests for critical paths
Use database migrations (never manual changes)
Version your API
Document complex logic
User Experience
Add loading states everywhere
Implement optimistic updates
Show clear error messages
Make onboarding smooth
Add helpful empty states
Common Patterns Reference

For detailed implementation patterns, see reference documents:

AUTHENTICATION_PATTERNS.md - OAuth, magic links, MFA
BILLING_PATTERNS.md - Stripe integration, webhooks, metering
MULTI_TENANT_PATTERNS.md - Organization structures, data isolation
DEPLOYMENT_STRATEGIES.md - CI/CD, environments, monitoring
Example Output Format

When planning a SaaS, provide:

Executive Summary

Product overview
Target users
Key features

Technical Architecture

System diagram
Tech stack rationale
Database schema

File Structure

Complete folder organization
Key file descriptions

Development Roadmap

Week-by-week breakdown
Feature prioritization
Estimated effort

Deployment Plan

Infrastructure setup
Environment configuration
Launch checklist

Next Steps

Immediate actions
Setup commands
Documentation links
Success Criteria

A well-planned SaaS should have:

✅ Clear database schema with RLS
✅ Secure authentication flow
✅ Scalable architecture
✅ Working billing integration
✅ Organized file structure
✅ Realistic timeline
✅ Clear MVP scope
✅ Deployment strategy
Weekly Installs
37
Repository
sitechfromgeorg…n-system
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn