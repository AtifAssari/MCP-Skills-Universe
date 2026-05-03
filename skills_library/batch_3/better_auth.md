---
title: better-auth
url: https://skills.sh/giuseppe-trisciuoglio/developer-kit/better-auth
---

# better-auth

skills/giuseppe-trisciuoglio/developer-kit/better-auth
better-auth
Installation
$ npx skills add https://github.com/giuseppe-trisciuoglio/developer-kit --skill better-auth
SKILL.md
Better Auth Integration Guide
Overview

Better Auth is a type-safe authentication framework for TypeScript supporting multiple providers, 2FA, SSO, organizations, and passkeys. This skill covers integration patterns for NestJS backend with Drizzle ORM + PostgreSQL and Next.js App Router frontend.

When to Use
Setting up Better Auth with NestJS backend
Integrating Next.js App Router frontend
Configuring Drizzle ORM schema with PostgreSQL
Implementing social login (GitHub, Google, Facebook, Microsoft)
Adding MFA/2FA with TOTP, passkey passwordless auth, or magic links
Managing trusted devices and backup codes for account recovery
Building multi-tenant apps with organizations or SSO
Creating protected routes with session management
Quick Start
Installation
# Backend (NestJS)
npm install better-auth @auth/drizzle-adapter drizzle-orm pg
npm install -D drizzle-kit

# Frontend (Next.js)
npm install better-auth

4-Phase Setup
Database: Install Drizzle, configure schema, run migrations
Backend: Create Better Auth instance with NestJS module
Frontend: Configure auth client, create pages, add middleware
Plugins: Add 2FA, passkey, organizations as needed

See references/nestjs-setup.md for complete backend setup, references/plugins.md for plugin configuration.

Instructions
Phase 1: Database Setup

Install dependencies

npm install drizzle-orm pg @auth/drizzle-adapter better-auth
npm install -D drizzle-kit


Create Drizzle config (drizzle.config.ts)

import { defineConfig } from 'drizzle-kit';
export default defineConfig({
  schema: './src/auth/schema.ts',
  out: './drizzle',
  dialect: 'postgresql',
  dbCredentials: { url: process.env.DATABASE_URL! },
});


Generate and run migrations

npx drizzle-kit generate
npx drizzle-kit migrate


Checkpoint: Verify tables created: psql $DATABASE_URL -c "\dt" should show user, account, session, verification_token tables.

Phase 2: Backend Setup (NestJS)

Create database module - Set up Drizzle connection service

Configure Better Auth instance

// src/auth/auth.instance.ts
import { betterAuth } from 'better-auth';
import { drizzleAdapter } from '@auth/drizzle-adapter';
import * as schema from './schema';

export const auth = betterAuth({
  database: drizzleAdapter(schema, { provider: 'postgresql' }),
  emailAndPassword: { enabled: true },
  socialProviders: {
    github: {
      clientId: process.env.AUTH_GITHUB_CLIENT_ID!,
      clientSecret: process.env.AUTH_GITHUB_CLIENT_SECRET!,
    }
  }
});


Create auth controller

@Controller('auth')
export class AuthController {
  @All('*')
  async handleAuth(@Req() req: Request, @Res() res: Response) {
    return auth.handler(req);
  }
}


Checkpoint: Test endpoint GET /auth/get-session returns { session: null } when unauthenticated (no error).

Phase 3: Frontend Setup (Next.js)

Configure auth client (lib/auth.ts)

import { createAuthClient } from 'better-auth/client';
export const authClient = createAuthClient({
  baseURL: process.env.NEXT_PUBLIC_APP_URL!
});


Add middleware (middleware.ts)

import { auth } from '@/lib/auth';
export default auth((req) => {
  if (!req.auth && req.nextUrl.pathname.startsWith('/dashboard')) {
    return Response.redirect(new URL('/sign-in', req.nextUrl.origin));
  }
});
export const config = { matcher: ['/dashboard/:path*'] };


Create sign-in page with form or social buttons

Checkpoint: Navigating to /dashboard when logged out should redirect to /sign-in.

Phase 4: Advanced Features

Add plugins from references/plugins.md:

2FA: twoFactor({ issuer: 'AppName', otpOptions: { sendOTP } })

Passkey: passkey({ rpID: 'domain.com', rpName: 'App' })

Organizations: organization({ avatar: { enabled: true } })

Magic Link: magicLink({ sendMagicLink })

SSO: sso({ saml: { enabled: true } })

Checkpoint: After adding plugins, re-run migrations and verify new tables exist.

Examples
Example 1: Server Component with Session

Input: Display user data in a Next.js Server Component.

// app/dashboard/page.tsx
import { auth } from '@/lib/auth';
import { redirect } from 'next/navigation';

export default async function DashboardPage() {
  const session = await auth();

  if (!session) {
    redirect('/sign-in');
  }

  return (
    <div>
      <h1>Welcome, {session.user.name}</h1>
      <p>Email: {session.user.email}</p>
    </div>
  );
}


Output: Renders user info for authenticated users; redirects unauthenticated to sign-in.

Example 2: 2FA TOTP Verification with Trusted Device

Input: User has 2FA enabled and wants to sign in, marking device as trusted.

// Server: Configure 2FA with OTP sending
export const auth = betterAuth({
  plugins: [
    twoFactor({
      issuer: 'MyApp',
      otpOptions: {
        async sendOTP({ user, otp }, ctx) {
          await sendEmail({
            to: user.email,
            subject: 'Your verification code',
            body: `Code: ${otp}`
          });
        }
      }
    })
  ]
});

// Client: Verify TOTP and trust device
const verify2FA = async (code: string) => {
  const { data } = await authClient.twoFactor.verifyTotp({
    code,
    trustDevice: true  // Device trusted for 30 days
  });

  if (data) {
    router.push('/dashboard');
  }
};


Output: User authenticated; device trusted for 30 days without 2FA prompt.

Example 3: Passkey Registration and Login

Input: Enable passkey (WebAuthn) authentication for passwordless login.

// Server
import { passkey } from '@better-auth/passkey';
export const auth = betterAuth({
  plugins: [
    passkey({
      rpID: 'example.com',
      rpName: 'My App',
    })
  ]
});

// Client: Register passkey
const registerPasskey = async () => {
  const { data } = await authClient.passkey.register({
    name: 'My Device'
  });
};

// Client: Sign in with autofill
const signInWithPasskey = async () => {
  await authClient.signIn.passkey({
    autoFill: true,  // Browser suggests passkey
  });
};


Output: Users can register and authenticate with biometrics, PIN, or security keys.

For more examples (backup codes, organizations, magic link, conditional UI), see references/plugins.md and references/passkey.md.

Best Practices
Environment Variables: Store all secrets in .env, add to .gitignore
Secret Generation: Use openssl rand -base64 32 for BETTER_AUTH_SECRET
HTTPS Required: OAuth callbacks need HTTPS (use ngrok for local testing)
Session Expiration: Configure based on security requirements (7 days default)
Database Indexing: Add indexes on email, userId for performance
Error Handling: Return generic errors without exposing sensitive details
Rate Limiting: Add to auth endpoints to prevent brute force attacks
Type Safety: Use npx better-auth typegen for full TypeScript coverage
Constraints and Warnings
Security Notes
Never commit secrets: Add .env to .gitignore; never commit OAuth secrets or DB credentials
Validate redirect URLs: Always validate OAuth redirect URLs to prevent open redirects
Hash passwords: Better Auth handles password hashing automatically; never implement custom hashing
Session storage: For production, use Redis or another scalable session store
HTTPS Only: Always use HTTPS for authentication in production
Email Verification: Always implement email verification for password-based auth
Known Limitations
Better Auth requires Node.js 18+ for Next.js App Router support
Some OAuth providers require specific redirect URL formats
Passkeys require HTTPS and compatible browsers
Organization features require additional database tables
Resources
Documentation
Better Auth - Official documentation
Drizzle ORM - Database ORM
NestJS - Backend framework
Next.js - Frontend framework
Reference Implementations
references/nestjs-setup.md - Complete NestJS backend setup
references/nextjs-setup.md - Complete Next.js frontend setup
references/plugins.md - Plugin configuration (2FA, passkey, organizations, SSO, magic link)
references/mfa-2fa.md - Detailed MFA/2FA guide
references/passkey.md - Detailed passkey implementation
references/schema.md - Drizzle schema reference
references/social-providers.md - Social provider configuration
Weekly Installs
560
Repository
giuseppe-trisci…oper-kit
GitHub Stars
233
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass