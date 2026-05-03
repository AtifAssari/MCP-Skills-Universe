---
title: nextauth-authentication
url: https://skills.sh/mindrally/skills/nextauth-authentication
---

# nextauth-authentication

skills/mindrally/skills/nextauth-authentication
nextauth-authentication
Installation
$ npx skills add https://github.com/mindrally/skills --skill nextauth-authentication
SKILL.md
NextAuth Authentication

You are an expert in NextAuth.js (Auth.js v5) authentication implementation. Follow these guidelines when integrating authentication in Next.js applications.

Core Principles
Use Auth.js v5 patterns and the universal auth() function
Implement proper session management strategy based on your needs
Always validate sessions server-side for sensitive operations
Configure environment variables correctly with the AUTH_ prefix
Installation
npm install next-auth@beta

Environment Variables
# Required
AUTH_SECRET=your-32-byte-secret-here  # Generate with: openssl rand -base64 32

# Provider credentials (auto-detected if named correctly)
AUTH_GITHUB_ID=your-github-client-id
AUTH_GITHUB_SECRET=your-github-client-secret

AUTH_GOOGLE_ID=your-google-client-id
AUTH_GOOGLE_SECRET=your-google-client-secret

# Optional: Custom URL (auto-detected in most environments)
AUTH_URL=https://your-domain.com

Basic Configuration
auth.ts (Root Configuration)
import NextAuth from 'next-auth';
import GitHub from 'next-auth/providers/github';
import Google from 'next-auth/providers/google';
import Credentials from 'next-auth/providers/credentials';
import { PrismaAdapter } from '@auth/prisma-adapter';
import { prisma } from '@/lib/prisma';

export const { handlers, auth, signIn, signOut } = NextAuth({
  adapter: PrismaAdapter(prisma),
  providers: [
    GitHub, // Credentials auto-detected from AUTH_GITHUB_ID/SECRET
    Google,
    Credentials({
      credentials: {
        email: { label: 'Email', type: 'email' },
        password: { label: 'Password', type: 'password' },
      },
      async authorize(credentials) {
        // Validate credentials
        const user = await validateCredentials(credentials);
        if (!user) return null;
        return user;
      },
    }),
  ],
  session: {
    strategy: 'jwt', // or 'database'
    maxAge: 30 * 24 * 60 * 60, // 30 days
  },
  pages: {
    signIn: '/auth/signin',
    error: '/auth/error',
  },
  callbacks: {
    async jwt({ token, user, account }) {
      if (user) {
        token.id = user.id;
        token.role = user.role;
      }
      return token;
    },
    async session({ session, token }) {
      if (token) {
        session.user.id = token.id as string;
        session.user.role = token.role as string;
      }
      return session;
    },
    async authorized({ auth, request }) {
      const isAuthenticated = !!auth?.user;
      const isProtectedRoute = request.nextUrl.pathname.startsWith('/dashboard');

      if (isProtectedRoute && !isAuthenticated) {
        return false; // Redirect to sign-in
      }

      return true;
    },
  },
});

Route Handlers (app/api/auth/[...nextauth]/route.ts)
import { handlers } from '@/auth';

export const { GET, POST } = handlers;

Middleware (middleware.ts)
import { auth } from '@/auth';

export default auth((req) => {
  const isAuthenticated = !!req.auth;
  const isAuthPage = req.nextUrl.pathname.startsWith('/auth');
  const isProtectedRoute = req.nextUrl.pathname.startsWith('/dashboard');

  // Redirect authenticated users away from auth pages
  if (isAuthenticated && isAuthPage) {
    return Response.redirect(new URL('/dashboard', req.nextUrl));
  }

  // Redirect unauthenticated users from protected routes
  if (!isAuthenticated && isProtectedRoute) {
    return Response.redirect(new URL('/auth/signin', req.nextUrl));
  }
});

export const config = {
  matcher: ['/((?!api|_next/static|_next/image|favicon.ico).*)'],
};

Session Strategies
JWT Strategy (Default without adapter)

Best for: Serverless, Edge runtime, minimal database queries

export const { auth } = NextAuth({
  session: {
    strategy: 'jwt',
    maxAge: 30 * 24 * 60 * 60, // 30 days
  },
});


Characteristics:

Sessions stored in encrypted cookies
No database query per request
Cannot be invalidated before expiration
Works with Edge middleware
Database Strategy

Best for: Immediate session invalidation, "sign out everywhere"

export const { auth } = NextAuth({
  adapter: PrismaAdapter(prisma),
  session: {
    strategy: 'database',
    maxAge: 30 * 24 * 60 * 60, // 30 days
  },
});


Characteristics:

Sessions stored in database
Database query on every request
Can be invalidated immediately
Incompatible with Edge middleware (use split config)
Split Configuration for Edge + Database
// auth.config.ts - Edge-compatible config
import type { NextAuthConfig } from 'next-auth';

export const authConfig: NextAuthConfig = {
  pages: {
    signIn: '/auth/signin',
  },
  callbacks: {
    authorized({ auth, request }) {
      return !!auth?.user;
    },
  },
  providers: [], // Configured in auth.ts
};

// auth.ts - Full config with adapter
import NextAuth from 'next-auth';
import { PrismaAdapter } from '@auth/prisma-adapter';
import { authConfig } from './auth.config';

export const { handlers, auth, signIn, signOut } = NextAuth({
  ...authConfig,
  adapter: PrismaAdapter(prisma),
  providers: [GitHub, Google],
});

// middleware.ts - Uses edge-compatible config
import NextAuth from 'next-auth';
import { authConfig } from './auth.config';

export default NextAuth(authConfig).auth;

Authentication in Components
Server Components
import { auth } from '@/auth';
import { redirect } from 'next/navigation';

export default async function DashboardPage() {
  const session = await auth();

  if (!session?.user) {
    redirect('/auth/signin');
  }

  return (
    <div>
      <h1>Welcome, {session.user.name}!</h1>
      <p>Email: {session.user.email}</p>
    </div>
  );
}

Client Components
'use client';

import { useSession } from 'next-auth/react';

export function UserProfile() {
  const { data: session, status } = useSession();

  if (status === 'loading') {
    return <Skeleton />;
  }

  if (status === 'unauthenticated') {
    return <SignInPrompt />;
  }

  return (
    <div>
      <img src={session.user.image} alt={session.user.name} />
      <p>{session.user.name}</p>
    </div>
  );
}

Session Provider Setup
// app/providers.tsx
'use client';

import { SessionProvider } from 'next-auth/react';

export function Providers({ children }: { children: React.ReactNode }) {
  return <SessionProvider>{children}</SessionProvider>;
}

// app/layout.tsx
import { Providers } from './providers';

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}

Server Actions
'use server';

import { auth, signIn, signOut } from '@/auth';

// Sign in action
export async function handleSignIn(provider: string) {
  await signIn(provider, { redirectTo: '/dashboard' });
}

// Sign out action
export async function handleSignOut() {
  await signOut({ redirectTo: '/' });
}

// Protected action
export async function createPost(formData: FormData) {
  const session = await auth();

  if (!session?.user) {
    throw new Error('Unauthorized');
  }

  const title = formData.get('title') as string;

  await prisma.post.create({
    data: {
      title,
      authorId: session.user.id,
    },
  });

  revalidatePath('/posts');
}

API Route Protection
import { auth } from '@/auth';
import { NextResponse } from 'next/server';

export async function GET() {
  const session = await auth();

  if (!session?.user) {
    return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
  }

  const data = await fetchUserData(session.user.id);
  return NextResponse.json(data);
}

Role-Based Access Control
Type Extensions
// types/next-auth.d.ts
import { DefaultSession, DefaultUser } from 'next-auth';
import { JWT, DefaultJWT } from 'next-auth/jwt';

declare module 'next-auth' {
  interface Session {
    user: {
      id: string;
      role: string;
    } & DefaultSession['user'];
  }

  interface User extends DefaultUser {
    role: string;
  }
}

declare module 'next-auth/jwt' {
  interface JWT extends DefaultJWT {
    id: string;
    role: string;
  }
}

Role Check Utility
import { auth } from '@/auth';

export async function requireRole(allowedRoles: string[]) {
  const session = await auth();

  if (!session?.user) {
    throw new Error('Unauthorized');
  }

  if (!allowedRoles.includes(session.user.role)) {
    throw new Error('Forbidden');
  }

  return session;
}

// Usage
export default async function AdminPage() {
  const session = await requireRole(['admin']);

  return <AdminDashboard user={session.user} />;
}

OAuth Providers Configuration
GitHub
import GitHub from 'next-auth/providers/github';

GitHub({
  clientId: process.env.AUTH_GITHUB_ID,
  clientSecret: process.env.AUTH_GITHUB_SECRET,
  authorization: {
    params: {
      scope: 'read:user user:email',
    },
  },
});

Google
import Google from 'next-auth/providers/google';

Google({
  clientId: process.env.AUTH_GOOGLE_ID,
  clientSecret: process.env.AUTH_GOOGLE_SECRET,
  authorization: {
    params: {
      prompt: 'consent',
      access_type: 'offline',
      response_type: 'code',
    },
  },
});

Credentials Provider
import Credentials from 'next-auth/providers/credentials';
import bcrypt from 'bcryptjs';

Credentials({
  name: 'credentials',
  credentials: {
    email: { label: 'Email', type: 'email' },
    password: { label: 'Password', type: 'password' },
  },
  async authorize(credentials) {
    if (!credentials?.email || !credentials?.password) {
      return null;
    }

    const user = await prisma.user.findUnique({
      where: { email: credentials.email },
    });

    if (!user || !user.hashedPassword) {
      return null;
    }

    const isValid = await bcrypt.compare(credentials.password, user.hashedPassword);

    if (!isValid) {
      return null;
    }

    return {
      id: user.id,
      email: user.email,
      name: user.name,
      role: user.role,
    };
  },
});

Security Best Practices
1. Always Use AUTH_SECRET in Production
# Generate a secure secret
openssl rand -base64 32

2. Cookie Configuration
export const { auth } = NextAuth({
  cookies: {
    sessionToken: {
      name: `__Secure-authjs.session-token`,
      options: {
        httpOnly: true,
        sameSite: 'lax',
        path: '/',
        secure: process.env.NODE_ENV === 'production',
      },
    },
  },
});

3. CSRF Protection

Auth.js handles CSRF protection automatically. Ensure you:

Use POST for sign-in/sign-out
Don't disable built-in protections
4. Validate Sessions Server-Side
// Always verify on the server for sensitive operations
export async function sensitiveOperation() {
  const session = await auth();

  if (!session?.user) {
    throw new Error('Unauthorized');
  }

  // Double-check user exists in database
  const user = await prisma.user.findUnique({
    where: { id: session.user.id },
  });

  if (!user || user.banned) {
    throw new Error('Access denied');
  }

  // Proceed with operation
}

Session Refresh and Polling
'use client';

import { SessionProvider } from 'next-auth/react';

export function Providers({ children }: { children: React.ReactNode }) {
  return (
    <SessionProvider
      refetchInterval={5 * 60} // Refetch every 5 minutes
      refetchOnWindowFocus={true}
    >
      {children}
    </SessionProvider>
  );
}

Error Handling
Custom Error Page
// app/auth/error/page.tsx
export default function AuthErrorPage({
  searchParams,
}: {
  searchParams: { error?: string };
}) {
  const errorMessages: Record<string, string> = {
    Configuration: 'There is a problem with the server configuration.',
    AccessDenied: 'You do not have permission to sign in.',
    Verification: 'The verification link has expired or has already been used.',
    Default: 'An error occurred during authentication.',
  };

  const error = searchParams.error || 'Default';
  const message = errorMessages[error] || errorMessages.Default;

  return (
    <div>
      <h1>Authentication Error</h1>
      <p>{message}</p>
      <a href="/auth/signin">Try again</a>
    </div>
  );
}

Testing
// Mock auth for testing
import { auth } from '@/auth';

jest.mock('@/auth', () => ({
  auth: jest.fn(),
}));

describe('Protected API', () => {
  it('returns 401 for unauthenticated requests', async () => {
    (auth as jest.Mock).mockResolvedValue(null);

    const response = await GET();
    expect(response.status).toBe(401);
  });

  it('returns data for authenticated requests', async () => {
    (auth as jest.Mock).mockResolvedValue({
      user: { id: '1', email: 'test@example.com' },
    });

    const response = await GET();
    expect(response.status).toBe(200);
  });
});

Common Issues and Solutions
Session Disappears on Refresh
Ensure AUTH_SECRET is set in production
Check cookie configuration
Verify HTTPS in production
Edge Runtime Compatibility

Use split configuration if using database adapter with Edge middleware.

Type Errors with Custom Properties

Extend the types in types/next-auth.d.ts.

Common Anti-Patterns to Avoid
Using NEXTAUTH_ prefix (use AUTH_ in v5)
Not setting AUTH_SECRET in production
Relying on client-side session checks for authorization
Not handling loading states in client components
Using database strategy with Edge middleware
Not validating sessions in server actions
Exposing sensitive data in JWT tokens
Weekly Installs
517
Repository
mindrally/skills
GitHub Stars
88
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass