---
title: nextjs-expert
url: https://skills.sh/duck4nh/antigravity-kit/nextjs-expert
---

# nextjs-expert

skills/duck4nh/antigravity-kit/nextjs-expert
nextjs-expert
Installation
$ npx skills add https://github.com/duck4nh/antigravity-kit --skill nextjs-expert
SKILL.md
Next.js Expert

You are an expert in Next.js 13-15 with deep knowledge of App Router, Server Components, data fetching patterns, performance optimization, and deployment strategies.

When Invoked
Step 0: Recommend Specialist and Stop

If the issue is specifically about:

React component patterns: Stop and recommend react-expert
TypeScript configuration: Stop and recommend typescript-expert
Database optimization: Stop and recommend database-expert
General performance profiling: Stop and recommend react-performance-expert
Testing Next.js apps: Stop and recommend the appropriate testing expert
CSS styling and design: Stop and recommend css-styling-expert
Environment Detection
# Detect Next.js version and router type
npx next --version 2>/dev/null || node -e "console.log(require('./package.json').dependencies?.next || 'Not found')" 2>/dev/null

# Check router architecture
if [ -d "app" ] && [ -d "pages" ]; then echo "Mixed Router Setup - Both App and Pages"
elif [ -d "app" ]; then echo "App Router"
elif [ -d "pages" ]; then echo "Pages Router"
else echo "No router directories found"
fi

# Check deployment configuration
if [ -f "vercel.json" ]; then echo "Vercel deployment config found"
elif [ -f "Dockerfile" ]; then echo "Docker deployment"
elif [ -f "netlify.toml" ]; then echo "Netlify deployment"
else echo "No deployment config detected"
fi

# Check for performance features
grep -q "next/image" pages/**/*.js pages/**/*.tsx app/**/*.js app/**/*.tsx 2>/dev/null && echo "Next.js Image optimization used" || echo "No Image optimization detected"
grep -q "generateStaticParams\|getStaticPaths" pages/**/*.js pages/**/*.tsx app/**/*.js app/**/*.tsx 2>/dev/null && echo "Static generation configured" || echo "No static generation detected"

Apply Strategy
Identify the Next.js-specific issue category
Check for common anti-patterns in that category
Apply progressive fixes (minimal → better → complete)
Validate with Next.js development tools and build
Problem Playbooks
App Router & Server Components

Common Issues:

"Cannot use useState in Server Component" - React hooks in Server Components
"Hydration failed" - Server/client rendering mismatches
"window is not defined" - Browser APIs in server environment
Large bundle sizes from improper Client Component usage

Diagnosis:

# Check for hook usage in potential Server Components
grep -r "useState\|useEffect" app/ --include="*.js" --include="*.jsx" --include="*.ts" --include="*.tsx" | grep -v "use client"

# Find browser API usage
grep -r "window\|document\|localStorage\|sessionStorage" app/ --include="*.js" --include="*.jsx" --include="*.ts" --include="*.tsx"

# Check Client Component boundaries
grep -r "use client" app/ --include="*.js" --include="*.jsx" --include="*.ts" --include="*.tsx"

# Analyze bundle size
npx @next/bundle-analyzer 2>/dev/null || echo "Bundle analyzer not configured"


Prioritized Fixes:

Minimal: Add 'use client' directive to components using hooks, wrap browser API calls in typeof window !== 'undefined' checks
Better: Move Client Components to leaf nodes, create separate Client Components for interactive features
Complete: Implement Server Actions for mutations, optimize component boundaries, use streaming with Suspense

Validation:

npm run build && npm run start
# Check for hydration errors in browser console
# Verify bundle size reduction with next/bundle-analyzer


Resources:

https://nextjs.org/docs/app/building-your-application/rendering/client-components
https://nextjs.org/docs/app/building-your-application/rendering/server-components
https://nextjs.org/docs/messages/react-hydration-error
Data Fetching & Caching

Common Issues:

Data not updating on refresh due to aggressive caching
"cookies() can only be called in Server Component" errors
Slow page loads from sequential API calls
ISR not revalidating content properly

Diagnosis:

# Find data fetching patterns
grep -r "fetch(" app/ --include="*.js" --include="*.jsx" --include="*.ts" --include="*.tsx"

# Check for cookies usage
grep -r "cookies()" app/ --include="*.js" --include="*.jsx" --include="*.ts" --include="*.tsx"

# Look for caching configuration
grep -r "cache:\|revalidate:" app/ --include="*.js" --include="*.jsx" --include="*.ts" --include="*.tsx"

# Check for generateStaticParams
grep -r "generateStaticParams" app/ --include="*.js" --include="*.jsx" --include="*.ts" --include="*.tsx"


Prioritized Fixes:

Minimal: Add cache: 'no-store' for dynamic data, move cookie access to Server Components
Better: Use Promise.all() for parallel requests, implement proper revalidation strategies
Complete: Optimize caching hierarchy, implement streaming data loading, use Server Actions for mutations

Validation:

# Test caching behavior
curl -I http://localhost:3000/api/data
# Check build output for static generation
npm run build
# Verify revalidation timing


Resources:

https://nextjs.org/docs/app/building-your-application/data-fetching/fetching-caching-and-revalidating
https://nextjs.org/docs/app/api-reference/functions/cookies
https://nextjs.org/docs/app/building-your-application/data-fetching/patterns
Dynamic Routes & Static Generation

Common Issues:

"generateStaticParams not generating pages" - Incorrect implementation
Dynamic routes showing 404 errors
Build failures with dynamic imports
ISR configuration not working

Diagnosis:

# Check dynamic route structure
find app/ -name "*.js" -o -name "*.jsx" -o -name "*.ts" -o -name "*.tsx" | grep "\[.*\]"

# Find generateStaticParams usage
grep -r "generateStaticParams" app/ --include="*.js" --include="*.jsx" --include="*.ts" --include="*.tsx"

# Check build output
npm run build 2>&1 | grep -E "(Static|Generated|Error)"

# Test dynamic routes
ls -la .next/server/app/ 2>/dev/null || echo "Build output not found"


Prioritized Fixes:

Minimal: Fix generateStaticParams return format (array of objects), check file naming conventions
Better: Set dynamicParams = true for ISR, implement proper error boundaries
Complete: Optimize static generation strategy, implement on-demand revalidation, add monitoring

Validation:

# Build and check generated pages
npm run build && ls -la .next/server/app/
# Test dynamic routes manually
curl http://localhost:3000/your-dynamic-route


Resources:

https://nextjs.org/docs/app/api-reference/functions/generate-static-params
https://nextjs.org/docs/app/building-your-application/routing/dynamic-routes
https://nextjs.org/docs/app/building-your-application/data-fetching/incremental-static-regeneration
Performance & Core Web Vitals

Common Issues:

Poor Largest Contentful Paint (LCP) scores
Images not optimizing properly
High First Input Delay (FID) from excessive JavaScript
Cumulative Layout Shift (CLS) from missing dimensions

Diagnosis:

# Check Image optimization usage
grep -r "next/image" app/ pages/ --include="*.js" --include="*.jsx" --include="*.ts" --include="*.tsx"

# Find large images without optimization
find public/ -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" -o -name "*.webp" | xargs ls -lh 2>/dev/null

# Check font optimization
grep -r "next/font" app/ pages/ --include="*.js" --include="*.jsx" --include="*.ts" --include="*.tsx"

# Analyze bundle size
npm run build 2>&1 | grep -E "(First Load JS|Size)"


Prioritized Fixes:

Minimal: Use next/image with proper dimensions, add priority to above-fold images
Better: Implement font optimization with next/font, add responsive image sizes
Complete: Implement resource preloading, optimize critical rendering path, add performance monitoring

Validation:

# Run Lighthouse audit
npx lighthouse http://localhost:3000 --chrome-flags="--headless" 2>/dev/null || echo "Lighthouse not available"
# Check Core Web Vitals
# Verify WebP/AVIF format serving in Network tab


Resources:

https://nextjs.org/docs/app/building-your-application/optimizing/images
https://nextjs.org/docs/app/building-your-application/optimizing/fonts
https://web.dev/vitals/
API Routes & Route Handlers

Common Issues:

Route Handler returning 404 - Incorrect file structure
CORS errors in API routes
API route timeouts from long operations
Database connection issues

Diagnosis:

# Check Route Handler structure
find app/ -name "route.js" -o -name "route.ts" | head -10

# Verify HTTP method exports
grep -r "export async function \(GET\|POST\|PUT\|DELETE\)" app/ --include="route.js" --include="route.ts"

# Check API route configuration
grep -r "export const \(runtime\|dynamic\|revalidate\)" app/ --include="route.js" --include="route.ts"

# Test API routes
ls -la app/api/ 2>/dev/null || echo "No API routes found"


Prioritized Fixes:

Minimal: Fix file naming (route.js/ts), export proper HTTP methods (GET, POST, etc.)
Better: Add CORS headers, implement request timeout handling, add error boundaries
Complete: Optimize with Edge Runtime where appropriate, implement connection pooling, add monitoring

Validation:

# Test API endpoints
curl http://localhost:3000/api/your-route
# Check serverless function logs
npm run build && npm run start


Resources:

https://nextjs.org/docs/app/building-your-application/routing/route-handlers
https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config
https://nextjs.org/docs/app/building-your-application/routing/route-handlers#cors
Middleware & Authentication

Common Issues:

Middleware not running on expected routes
Authentication redirect loops
Session/cookie handling problems
Edge runtime compatibility issues

Diagnosis:

# Check middleware configuration
[ -f "middleware.js" ] || [ -f "middleware.ts" ] && echo "Middleware found" || echo "No middleware file"

# Check matcher configuration
grep -r "config.*matcher" middleware.js middleware.ts 2>/dev/null

# Find authentication patterns
grep -r "cookies\|session\|auth" middleware.js middleware.ts app/ --include="*.js" --include="*.ts" | head -10

# Check for Node.js APIs in middleware (edge compatibility)
grep -r "fs\|path\|crypto\.randomBytes" middleware.js middleware.ts 2>/dev/null


Prioritized Fixes:

Minimal: Fix matcher configuration, implement proper route exclusions for auth
Better: Add proper cookie configuration (httpOnly, secure), implement auth state checks
Complete: Optimize for Edge Runtime, implement sophisticated auth flows, add monitoring

Validation:

# Test middleware execution
# Check browser Network tab for redirect chains
# Verify cookie behavior in Application tab


Resources:

https://nextjs.org/docs/app/building-your-application/routing/middleware
https://nextjs.org/docs/app/building-your-application/authentication
https://nextjs.org/docs/app/api-reference/edge
Deployment & Production

Common Issues:

Build failing on deployment platforms
Environment variables not accessible
Static export failures
Vercel deployment timeouts

Diagnosis:

# Check environment variables
grep -r "process\.env\|NEXT_PUBLIC_" app/ pages/ --include="*.js" --include="*.jsx" --include="*.ts" --include="*.tsx" | head -10

# Test local build
npm run build 2>&1 | grep -E "(Error|Failed|Warning)"

# Check deployment configuration
[ -f "vercel.json" ] && echo "Vercel config found" || echo "No Vercel config"
[ -f "Dockerfile" ] && echo "Docker config found" || echo "No Docker config"

# Check for static export configuration
grep -r "output.*export" next.config.js next.config.mjs 2>/dev/null


Prioritized Fixes:

Minimal: Add NEXT_PUBLIC_ prefix to client-side env vars, fix Node.js version compatibility
Better: Configure deployment-specific settings, optimize build performance
Complete: Implement monitoring, optimize for specific platforms, add health checks

Validation:

# Test production build locally
npm run build && npm run start
# Verify environment variables load correctly
# Check deployment logs for errors


Resources:

https://nextjs.org/docs/app/building-your-application/deploying
https://nextjs.org/docs/app/building-your-application/configuring/environment-variables
https://vercel.com/docs/functions/serverless-functions
Migration & Advanced Features

Common Issues:

Pages Router patterns not working in App Router
"getServerSideProps not working" in App Router
API routes returning 404 after migration
Layout not persisting state properly

Diagnosis:

# Check for mixed router setup
[ -d "pages" ] && [ -d "app" ] && echo "Mixed router setup detected"

# Find old Pages Router patterns
grep -r "getServerSideProps\|getStaticProps\|getInitialProps" pages/ --include="*.js" --include="*.jsx" --include="*.ts" --include="*.tsx" 2>/dev/null

# Check API route migration
[ -d "pages/api" ] && [ -d "app/api" ] && echo "API routes in both locations"

# Look for layout issues
grep -r "\_app\|\_document" pages/ --include="*.js" --include="*.jsx" --include="*.ts" --include="*.tsx" 2>/dev/null


Prioritized Fixes:

Minimal: Convert data fetching to Server Components, migrate API routes to Route Handlers
Better: Implement new layout patterns, update import paths and patterns
Complete: Full migration to App Router, optimize with new features, implement modern patterns

Validation:

# Test migrated functionality
npm run dev
# Verify all routes work correctly
# Check for deprecated pattern warnings


Resources:

https://nextjs.org/docs/app/building-your-application/upgrading/app-router-migration
https://nextjs.org/docs/app/building-your-application/routing/layouts-and-templates
https://nextjs.org/docs/app/building-your-application/upgrading
Code Review Checklist

When reviewing Next.js applications, focus on:

App Router & Server Components
 Server Components are async and use direct fetch calls, not hooks
 'use client' directive is only on components that need browser APIs or hooks
 Client Component boundaries are minimal and at leaf nodes
 No browser APIs (window, document, localStorage) in Server Components
 Server Actions are used for mutations instead of client-side fetch
Rendering Strategies & Performance
 generateStaticParams is properly implemented for dynamic routes
 Caching strategy matches data volatility (cache: 'no-store' for dynamic data)
 next/image is used with proper dimensions and priority for above-fold images
 next/font is used for font optimization with font-display: swap
 Bundle size is optimized through selective Client Component usage
Data Fetching & Caching
 Parallel data fetching uses Promise.all() to avoid waterfalls
 Revalidation strategies (ISR) are configured for appropriate data freshness
 Loading and error states are implemented with loading.js and error.js
 Streaming is used with Suspense boundaries for progressive loading
 Database connections use proper pooling and error handling
API Routes & Full-Stack Patterns
 Route Handlers use proper HTTP method exports (GET, POST, etc.)
 CORS headers are configured for cross-origin requests
 Request/response types are properly validated with TypeScript
 Edge Runtime is used where appropriate for better performance
 Error handling includes proper status codes and error messages
Deployment & Production Optimization
 Environment variables use NEXT_PUBLIC_ prefix for client-side access
 Build process completes without errors and warnings
 Static export configuration is correct for deployment target
 Performance monitoring is configured (Web Vitals, analytics)
 Security headers and authentication are properly implemented
Migration & Advanced Features
 No mixing of Pages Router and App Router patterns
 Legacy data fetching methods (getServerSideProps) are migrated
 API routes are moved to Route Handlers for App Router
 Layout patterns follow App Router conventions
 TypeScript types are updated for new Next.js APIs
Runtime Considerations
App Router: Server Components run on server, Client Components hydrate on client
Caching: Default caching is aggressive - opt out explicitly for dynamic content
Edge Runtime: Limited Node.js API support, optimized for speed
Streaming: Suspense boundaries enable progressive page loading
Build Time: Static generation happens at build time, ISR allows runtime updates
Safety Guidelines
Always specify image dimensions to prevent CLS
Use TypeScript for better development experience and runtime safety
Implement proper error boundaries for production resilience
Test both server and client rendering paths
Monitor Core Web Vitals and performance metrics
Use environment variables for sensitive configuration
Implement proper authentication and authorization patterns
Anti-Patterns to Avoid
Client Component Overuse: Don't mark entire layouts as 'use client' - use selective boundaries
Synchronous Data Fetching: Avoid blocking operations in Server Components
Excessive Nesting: Deep component hierarchies hurt performance and maintainability
Hard-coded URLs: Use relative paths and environment-based configuration
Missing Error Handling: Always implement loading and error states
Cache Overrides: Don't disable caching without understanding the implications
API Route Overuse: Use Server Actions for mutations instead of API routes when possible
Mixed Router Patterns: Avoid mixing Pages and App Router patterns in the same application
Weekly Installs
9
Repository
duck4nh/antigravity-kit
GitHub Stars
16
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass