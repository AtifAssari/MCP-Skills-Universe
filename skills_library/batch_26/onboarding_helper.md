---
title: onboarding-helper
url: https://skills.sh/curiouslearner/devkit/onboarding-helper
---

# onboarding-helper

skills/curiouslearner/devkit/onboarding-helper
onboarding-helper
Installation
$ npx skills add https://github.com/curiouslearner/devkit --skill onboarding-helper
SKILL.md
Onboarding Helper Skill

Generate comprehensive onboarding documentation and guides for new developers joining your team or project.

Instructions

You are an onboarding and developer experience expert. When invoked:

Assess Onboarding Needs:

Project complexity and technology stack
Team size and structure
Development workflow and processes
Domain knowledge requirements
Common onboarding challenges

Create Onboarding Materials:

Welcome documentation
Development environment setup guides
Codebase architecture overview
First-task tutorials
Team processes and conventions

Organize Learning Path:

Day 1, Week 1, Month 1 goals
Progressive complexity
Hands-on exercises
Checkpoint milestones
Resources and references

Document Team Culture:

Communication channels
Meeting schedules
Code review practices
Decision-making processes
Team values and norms

Enable Self-Service:

FAQ sections
Troubleshooting guides
Links to resources
Who to ask for what
Common gotchas
Onboarding Documentation Structure
Complete Onboarding Guide Template
# Welcome to [Project Name]! 👋

Welcome! We're excited to have you on the team. This guide will help you get up to speed quickly and smoothly.

## Table of Contents
1. [Overview](#overview)
2. [Day 1: Getting Started](#day-1-getting-started)
3. [Week 1: Core Concepts](#week-1-core-concepts)
4. [Month 1: Making Impact](#month-1-making-impact)
5. [Team & Processes](#team--processes)
6. [Resources](#resources)
7. [FAQ](#faq)

---

## Overview

### What We're Building
We're building a modern e-commerce platform that helps small businesses sell online. Our platform handles:
- Product catalog management
- Shopping cart and checkout
- Payment processing (Stripe integration)
- Order fulfillment and tracking
- Customer relationship management

**Our Mission**: Make e-commerce accessible to businesses of all sizes.

**Our Users**: Small to medium business owners with 10-1000 products.

### Technology Stack

**Frontend**:
- React 18 with TypeScript
- Redux Toolkit for state management
- Material-UI component library
- React Query for API calls
- Vite for build tooling

**Backend**:
- Node.js with Express
- PostgreSQL database
- Redis for caching
- Stripe for payments
- AWS S3 for file storage

**Infrastructure**:
- Docker for local development
- Kubernetes for production
- GitHub Actions for CI/CD
- AWS (EC2, RDS, S3, CloudFront)
- DataDog for monitoring

### Project Statistics
- **Started**: January 2023
- **Team Size**: 12 engineers (4 frontend, 5 backend, 3 full-stack)
- **Codebase**: ~150K lines of code
- **Active Users**: 5,000+ businesses
- **Monthly Transactions**: $2M+

---

## Day 1: Getting Started

### Your First Day Checklist

- [ ] Complete HR onboarding
- [ ] Get added to communication channels
- [ ] Set up development environment
- [ ] Clone the repository
- [ ] Run the application locally
- [ ] Deploy to your personal dev environment
- [ ] Introduce yourself to the team
- [ ] Schedule 1:1s with your manager and buddy

### Access & Accounts

**Required Accounts**:
1. **GitHub** - Source code ([github.com/company/project](https://github.com))
   - Request access from @engineering-manager
2. **Slack** - Team communication
   - Channels: #engineering, #frontend, #backend, #general
3. **Jira** - Project management ([company.atlassian.net](https://company.atlassian.net))
4. **Figma** - Design files
5. **AWS Console** - Production access (read-only initially)
6. **DataDog** - Monitoring and logs

**Development Tools**:
- Docker Desktop
- Node.js 18+ (use nvm)
- PostgreSQL client (psql or pgAdmin)
- Postman or Insomnia (API testing)
- VS Code (recommended, see extensions below)

### Environment Setup

#### 1. Install Prerequisites

**macOS**:
```bash
# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Node.js via nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install 18
nvm use 18

# Install Docker Desktop
brew install --cask docker

# Install PostgreSQL client
brew install postgresql@14


Windows:

# Install using Chocolatey
choco install nodejs-lts docker-desktop postgresql14

2. Clone Repository
# Clone the repo
git clone git@github.com:company/ecommerce-platform.git
cd ecommerce-platform

# Install dependencies
npm install

# Copy environment variables
cp .env.example .env.local

3. Configure Environment Variables

Edit .env.local:

# Database (local Docker)
DATABASE_URL=postgresql://postgres:password@localhost:5432/ecommerce_dev

# Redis
REDIS_URL=redis://localhost:6379

# Stripe (use test keys)
STRIPE_SECRET_KEY=sk_test_... # Get from @backend-lead
STRIPE_PUBLISHABLE_KEY=pk_test_...

# AWS S3 (dev bucket)
AWS_ACCESS_KEY_ID=... # Get from @devops
AWS_SECRET_ACCESS_KEY=...
AWS_S3_BUCKET=ecommerce-dev-uploads

# Session
SESSION_SECRET=your-random-secret-here


Where to get credentials:

Stripe test keys: 1Password vault "Development Secrets"
AWS credentials: Request from @devops in #engineering
Session secret: Generate with openssl rand -base64 32
4. Start Development Environment
# Start Docker services (PostgreSQL, Redis)
docker-compose up -d

# Run database migrations
npm run db:migrate

# Seed database with sample data
npm run db:seed

# Start development server
npm run dev


Expected output:

✔ Database migrated successfully
✔ Seeded 100 products, 50 users
✔ Server running on http://localhost:3000
✔ API available at http://localhost:3000/api

5. Verify Installation

Open your browser to http://localhost:3000

You should see the application home page with sample products.

Test credentials:

Email: test@example.com
Password: password123

Troubleshooting:

Port 3000 in use: Kill the process with lsof -ti:3000 | xargs kill -9
Database connection failed: Check Docker is running with docker ps
Module not found: Delete node_modules and run npm install again

See Troubleshooting Guide for more help.

VS Code Setup

Recommended Extensions:

{
  "recommendations": [
    "dbaeumer.vscode-eslint",
    "esbenp.prettier-vscode",
    "bradlc.vscode-tailwindcss",
    "ms-azuretools.vscode-docker",
    "eamodio.gitlens",
    "orta.vscode-jest",
    "prisma.prisma"
  ]
}


Settings (.vscode/settings.json):

{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
  },
  "typescript.tsdk": "node_modules/typescript/lib"
}

Your First Commit

Let's make a simple change to verify your setup:

Create a branch:

git checkout -b test/your-name-setup


Add your name to the team page: Edit src/pages/About.tsx:

const teamMembers = [
  // ... existing members
  { name: 'Your Name', role: 'Software Engineer', joinedDate: '2024-01-15' }
];


Test your change:

npm run test
npm run lint


Commit and push:

git add .
git commit -m "docs: Add [Your Name] to team page"
git push origin test/your-name-setup


Create a PR:

Go to GitHub
Click "Compare & pull request"
Fill out the PR template
Request review from your buddy

Congrats on your first contribution! 🎉

End of Day 1

You should now have:

✅ Development environment running locally
✅ Application accessible in your browser
✅ First PR created
✅ Access to all team tools and channels

Questions? Ask in #engineering or DM your buddy!

Week 1: Core Concepts
Project Architecture
High-Level Architecture
┌─────────────┐
│   Browser   │
│  (React)    │
└──────┬──────┘
       │ HTTPS
       ▼
┌─────────────┐     ┌──────────────┐
│ API Gateway │────▶│  Auth Service│
│  (Express)  │     │   (JWT)      │
└──────┬──────┘     └──────────────┘
       │
       ├────▶ Product Service
       │
       ├────▶ Order Service
       │
       ├────▶ Payment Service ────▶ Stripe API
       │
       └────▶ User Service
              │
              ▼
         ┌──────────┐
         │PostgreSQL│
         └──────────┘

Directory Structure
ecommerce-platform/
├── client/                 # Frontend React app
│   ├── src/
│   │   ├── components/    # Reusable UI components
│   │   ├── pages/         # Page components
│   │   ├── hooks/         # Custom React hooks
│   │   ├── store/         # Redux store and slices
│   │   ├── api/           # API client functions
│   │   ├── utils/         # Utility functions
│   │   └── types/         # TypeScript type definitions
│   └── tests/             # Frontend tests
│
├── server/                # Backend Node.js app
│   ├── src/
│   │   ├── routes/        # Express route handlers
│   │   ├── controllers/   # Business logic
│   │   ├── services/      # External integrations
│   │   ├── models/        # Database models (Prisma)
│   │   ├── middleware/    # Express middleware
│   │   ├── utils/         # Utility functions
│   │   └── types/         # TypeScript types
│   └── tests/             # Backend tests
│
├── docs/                  # Documentation
├── scripts/               # Build and deployment scripts
├── .github/               # GitHub Actions workflows
└── docker-compose.yml     # Local development services

Key Concepts
1. Authentication Flow
// User logs in
POST /api/auth/login
{ email, password }
  ↓
// Server validates credentials
// Generates JWT token
  ↓
// Client stores token
localStorage.setItem('token', token)
  ↓
// Client includes token in requests
Authorization: Bearer <token>
  ↓
// Server validates token
// Attaches user to request
req.user = decodedToken


Code location: server/src/middleware/auth.ts

2. State Management (Redux)

We use Redux Toolkit for client-side state:

// Store structure
{
  auth: {
    user: User | null,
    isAuthenticated: boolean,
    loading: boolean
  },
  cart: {
    items: CartItem[],
    total: number
  },
  products: {
    list: Product[],
    filters: FilterState,
    loading: boolean
  }
}


Reading from store:

import { useAppSelector } from '@/hooks/redux';

const user = useAppSelector(state => state.auth.user);
const cartItems = useAppSelector(state => state.cart.items);


Dispatching actions:

import { useAppDispatch } from '@/hooks/redux';
import { addToCart } from '@/store/slices/cartSlice';

const dispatch = useAppDispatch();
dispatch(addToCart({ productId, quantity: 1 }));


Code location: client/src/store/

3. API Communication

We use React Query for server state:

import { useQuery, useMutation } from '@tanstack/react-query';
import { api } from '@/api/client';

// Fetching data
const { data, isLoading, error } = useQuery({
  queryKey: ['products'],
  queryFn: () => api.products.getAll()
});

// Mutating data
const mutation = useMutation({
  mutationFn: (product) => api.products.create(product),
  onSuccess: () => {
    queryClient.invalidateQueries(['products']);
  }
});


Code location: client/src/api/

4. Database Access (Prisma)

We use Prisma ORM for database operations:

import { prisma } from '@/lib/prisma';

// Find one
const user = await prisma.user.findUnique({
  where: { id: userId }
});

// Find many with filters
const products = await prisma.product.findMany({
  where: {
    category: 'electronics',
    price: { lt: 1000 }
  },
  include: {
    images: true,
    reviews: true
  }
});

// Create
const order = await prisma.order.create({
  data: {
    userId,
    total: 100,
    items: {
      create: [
        { productId: 1, quantity: 2, price: 50 }
      ]
    }
  }
});


Code location: server/src/models/ Schema: prisma/schema.prisma

Your First Real Task

Goal: Add a "Recently Viewed" feature to product pages.

Requirements:

Track products a user views
Display last 5 viewed products
Persist across sessions (use localStorage)
Show on product detail page

Steps:

Create a feature branch:

git checkout -b feature/recently-viewed-products


Frontend: Add hook (client/src/hooks/useRecentlyViewed.ts):

export function useRecentlyViewed() {
  const addToRecentlyViewed = (product: Product) => {
    // Get existing
    const recent = JSON.parse(localStorage.getItem('recentlyViewed') || '[]');

    // Add new (avoid duplicates)
    const updated = [
      product,
      ...recent.filter((p: Product) => p.id !== product.id)
    ].slice(0, 5);

    // Save
    localStorage.setItem('recentlyViewed', JSON.stringify(updated));
  };

  const getRecentlyViewed = (): Product[] => {
    return JSON.parse(localStorage.getItem('recentlyViewed') || '[]');
  };

  return { addToRecentlyViewed, getRecentlyViewed };
}


Frontend: Use in product page (client/src/pages/ProductDetail.tsx):

const { addToRecentlyViewed, getRecentlyViewed } = useRecentlyViewed();

useEffect(() => {
  if (product) {
    addToRecentlyViewed(product);
  }
}, [product]);

const recentProducts = getRecentlyViewed();


Frontend: Display component (client/src/components/RecentlyViewed.tsx):

export function RecentlyViewed({ currentProductId }: Props) {
  const { getRecentlyViewed } = useRecentlyViewed();
  const products = getRecentlyViewed()
    .filter(p => p.id !== currentProductId);

  if (products.length === 0) return null;

  return (
    <section>
      <h2>Recently Viewed</h2>
      <ProductGrid products={products} />
    </section>
  );
}


Add tests:

describe('useRecentlyViewed', () => {
  it('should add product to recently viewed', () => {
    const { addToRecentlyViewed, getRecentlyViewed } = useRecentlyViewed();

    addToRecentlyViewed(mockProduct);

    expect(getRecentlyViewed()).toContainEqual(mockProduct);
  });

  it('should limit to 5 products', () => {
    // Add 6 products, check only 5 remain
  });

  it('should move duplicate to front', () => {
    // Add same product twice, check it appears once at front
  });
});


Test manually:

View several products
Check localStorage in DevTools
Verify list appears on product pages
Test edge cases (empty state, single item)

Create PR:

Use PR template
Add screenshots
Request review from @frontend-team

Resources:

React Hooks Guide
LocalStorage API
Our Testing Guide
Week 1 Learning Resources

Must Read:

 Project README
 Architecture Decision Records
 API Documentation
 Contributing Guidelines

Optional Deep Dives:

 Redux Toolkit Docs
 React Query Docs
 Prisma Docs
 Our Style Guide
End of Week 1

You should now:

✅ Understand overall architecture
✅ Know key technologies and tools
✅ Have completed your first feature
✅ Understand our development workflow
✅ Feel comfortable asking questions

Checkpoint Meeting: Schedule 30min with your manager to review progress.

Month 1: Making Impact
Month 1 Goals
Ship Features: Complete 3-5 features independently
Code Reviews: Provide meaningful feedback on 10+ PRs
Fix Bugs: Tackle 2-3 bug fixes
Improve Something: Find and fix a small pain point
Learn Domain: Understand e-commerce business basics
Suggested Feature Ideas

Beginner Friendly:

Add product sorting (price, rating, newest)
Implement wishlist functionality
Create order history page
Add email notifications

Intermediate:

Implement product reviews and ratings
Add search autocomplete
Create admin dashboard for orders
Optimize image loading performance

Advanced:

Implement shopping cart abandonment recovery
Add real-time inventory tracking
Create recommendation engine
Set up A/B testing framework

Finding Tasks: Check Jira board for issues labeled good-first-issue.

Code Review Best Practices

As an Author:

Keep PRs small (< 400 lines changed)
Write clear descriptions
Add screenshots for UI changes
Respond to feedback promptly
Test thoroughly before requesting review

As a Reviewer:

Review within 24 hours
Be kind and constructive
Ask questions rather than demand changes
Highlight good practices
Approve when ready (don't nitpick)

Review Checklist:

 Code follows style guide
 Tests included and passing
 No console.logs in production code
 Error handling implemented
 Performance considerations addressed
 Security best practices followed

Resources: Code Review Guide

Testing Guidelines

What to Test:

Business logic (always)
User interactions (important flows)
Edge cases and error states
API integrations (with mocks)

Testing Pyramid:

       /\
      /  \    E2E Tests (few)
     /────\
    /      \  Integration Tests (some)
   /────────\
  /          \ Unit Tests (many)
 /────────────\


Running Tests:

# All tests
npm test

# Watch mode
npm test -- --watch

# Coverage
npm test -- --coverage

# Specific file
npm test UserService.test.ts


Writing Tests:

describe('CartService', () => {
  describe('addToCart', () => {
    it('should add item to empty cart', () => {
      // Arrange
      const cart = new Cart();
      const item = { productId: 1, quantity: 2 };

      // Act
      cart.addItem(item);

      // Assert
      expect(cart.items).toHaveLength(1);
      expect(cart.items[0]).toEqual(item);
    });

    it('should increase quantity if item exists', () => {
      // Test implementation
    });

    it('should throw error if quantity is negative', () => {
      // Test implementation
    });
  });
});


Resources: Testing Guide

Deployment Process

Environments:

Development: Your local machine
Staging: https://staging.ecommerce.example.com
Production: https://ecommerce.example.com

Deployment Flow:

main branch
    │
    ▼
CI runs (tests, lint, build)
    │
    ▼
Auto-deploy to Staging
    │
    ▼
Manual QA testing
    │
    ▼
Create release tag
    │
    ▼
Deploy to Production (gradual rollout)


You can deploy: Staging (automatic on merge to main) You cannot deploy: Production (requires approval)

Monitoring:

Logs: DataDog dashboard
Errors: Sentry alerts
Metrics: Custom dashboards
Team & Processes
Team Structure

Engineering Team:

Engineering Manager: @alice (1:1s, career growth)
Tech Lead: @bob (architecture decisions, technical direction)
Frontend Team (4 engineers): @carol, @dave, @eve, @frank
Backend Team (5 engineers): @grace, @henry, @ivy, @jack, @kate
Full-Stack (3 engineers): @liam, @maya, @noah

Adjacent Teams:

Product: @olivia (product manager)
Design: @peter, @quinn (UI/UX designers)
QA: @rachel, @sam (test engineers)
DevOps: @taylor (infrastructure)
Communication Channels

Slack Channels:

#engineering - General engineering discussions
#frontend - Frontend-specific topics
#backend - Backend-specific topics
#deploys - Deployment notifications
#incidents - Production issues
#random - Non-work chat

When to use what:

Slack: Quick questions, discussions, FYIs
Jira: Task tracking, bug reports
GitHub: Code discussions, PR reviews
Email: External communication, formal notices
Zoom: Meetings, pair programming, deep discussions
Meetings

Weekly:

Team Standup (Mon/Wed/Fri, 10am, 15min)
What you did
What you're doing
Any blockers
Sprint Planning (Monday, 1pm, 1hr)
Plan next sprint
Estimate stories
Retro (Friday, 2pm, 45min)
What went well
What could improve
Action items

Bi-weekly:

1:1 with Manager (30min)
Career growth
Feedback
Questions

Monthly:

All-Hands (First Friday, 3pm, 1hr)
Company updates
Team showcases

Meeting Norms:

Cameras on when possible
Mute when not speaking
Be on time
Come prepared
Take notes
Development Workflow

Git Workflow:

main (protected)
  ├─ feature/add-wishlist
  ├─ fix/cart-bug
  └─ refactor/payment-service


Branch Naming:

feature/description - New features
fix/description - Bug fixes
refactor/description - Code refactoring
docs/description - Documentation
test/description - Tests only

Commit Messages:

type(scope): description

feat(cart): add wishlist functionality
fix(auth): resolve token expiration issue
docs(readme): update setup instructions
test(orders): add integration tests
refactor(database): optimize queries


PR Process:

Create feature branch
Make changes
Write tests
Create PR (use template)
Request review (minimum 1 approval)
Address feedback
Merge (squash and merge)
On-Call Rotation

You won't be on-call for your first 3 months.

When you join rotation:

1 week on-call per month
Respond to PagerDuty alerts
Fix production issues
Escalate if needed

Resources: On-Call Runbook

Resources
Documentation
README - Project overview
Architecture - System design
API Docs - API reference
Contributing - How to contribute
Style Guide - Code conventions
Testing Guide - Testing practices
Deployment - Deployment process
Troubleshooting - Common issues
Learning Resources

JavaScript/TypeScript:

TypeScript Handbook
JavaScript.info
You Don't Know JS

React:

React Docs
React TypeScript Cheatsheet
Epic React by Kent C. Dodds

Node.js:

Node.js Best Practices
Express.js Guide

Databases:

Prisma Guides
PostgreSQL Tutorial

System Design:

System Design Primer
Web Architecture 101
Internal Tools
1Password: Shared credentials
Notion: Team wiki and docs
Figma: Design files
DataDog: Monitoring and logs
Sentry: Error tracking
GitHub: Code repository
Jira: Project management
Your Buddy

Your onboarding buddy is @buddy-name.

Your buddy will:

Answer day-to-day questions
Review your first few PRs
Introduce you to the team
Help you navigate processes
Meet with you weekly (first month)

Don't hesitate to ask them anything!

FAQ
Development

Q: How do I reset my local database?

npm run db:reset  # Drops all data and re-runs migrations
npm run db:seed   # Adds sample data


Q: Tests are failing locally but passing in CI. Why?

Check Node version matches (use nvm use)
Clear node_modules and reinstall
Check for environment-specific tests

Q: How do I debug the backend? Add debugger; statement and run:

node --inspect-brk server/src/index.ts


Then open Chrome DevTools.

Q: Where do I find API credentials for development? Check 1Password vault "Development Secrets" or ask in #engineering.

Code & Practices

Q: When should I create a new component vs. modify existing?

Create new: Reusable, self-contained functionality
Modify existing: Extending current component's capabilities
When in doubt, ask in PR review

Q: How much test coverage is expected?

Aim for 80% overall
100% for business-critical logic (payments, auth)
Focus on valuable tests, not just coverage numbers

Q: Can I refactor code I'm working on? Yes, but:

Keep refactoring in separate commits
Don't mix feature work with large refactors
For big refactors, create separate PR

Q: What if I disagree with PR feedback?

Discuss politely in PR comments
Explain your reasoning
Escalate to tech lead if needed
Remember: we're all learning
Process

Q: How do I report a production bug?

Post in #incidents with details
Create Jira ticket (type: Bug, priority: based on severity)
If urgent, ping on-call engineer

Q: Can I work on something not in Jira?

Small improvements: Yes, create ticket after
Large projects: Check with manager first
Tech debt: Discuss in sprint planning

Q: How do I request time off?

Add to team calendar
Message manager on Slack
Update Jira board if you have active work

Q: I'm stuck on a problem for hours. What should I do?

Try debugging and Googling (30 min)
Ask in #engineering (don't struggle alone)
Schedule pairing session with teammate
Escalate to tech lead if still stuck

Rule of thumb: Ask for help after 30 minutes of being stuck.

Career & Growth

Q: How is performance evaluated?

Quarterly reviews with manager
Based on: code quality, velocity, collaboration, growth
Transparent rubric provided

Q: How do I learn more about [specific topic]?

Ask in #engineering for recommendations
Check internal wiki for resources
Request Udemy/book budget from manager

Q: Can I switch teams/projects?

Discuss with manager after 6 months
Internal mobility encouraged
Welcome Aboard!

Remember:

Ask Questions: No question is too small
Take Breaks: Onboarding is exhausting
Be Patient: It takes 3+ months to feel productive
Have Fun: We're building something cool together!

Need help? Your buddy (@buddy-name) and manager (@manager-name) are here for you.

Welcome to the team! 🚀


## Usage Examples



@onboarding-helper @onboarding-helper --type full-guide @onboarding-helper --type quick-start @onboarding-helper --type architecture-overview @onboarding-helper --focus frontend @onboarding-helper --include-exercises


## Best Practices

### Make It Personal
- Address new team member by name
- Assign a buddy/mentor
- Include team photos and bios
- Share team culture and values

### Progressive Disclosure
- Day 1: Just get running
- Week 1: Understand basics
- Month 1: Ship features
- Month 3: Full productivity

### Make It Interactive
- Include hands-on exercises
- Provide starter tasks
- Encourage pair programming
- Set up regular check-ins

### Keep It Updated
- Review quarterly
- Get feedback from new hires
- Update for tech stack changes
- Improve based on common questions

### Make It Discoverable
- Central location (wiki, README)
- Easy to navigate
- Searchable
- Version controlled

## Notes

- Onboarding is an ongoing process, not a one-time event
- Great onboarding significantly reduces time-to-productivity
- Documentation should be discoverable and up-to-date
- Assign mentors/buddies for personal guidance
- Include both technical and cultural onboarding
- Celebrate early wins to build confidence
- Check in regularly during first 3 months
- Encourage questions and create safe learning environment
- Provide clear learning path with milestones
- Make resources easily accessible
- Update documentation based on new hire feedback

Weekly Installs
14
Repository
curiouslearner/devkit
GitHub Stars
26
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass