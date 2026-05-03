---
title: stripe-subscription
url: https://skills.sh/eng0ai/eng0-template-skills/stripe-subscription
---

# stripe-subscription

skills/eng0ai/eng0-template-skills/stripe-subscription
stripe-subscription
Installation
$ npx skills add https://github.com/eng0ai/eng0-template-skills --skill stripe-subscription
SKILL.md
Stripe Subscription

Stripe Checkout integration for recurring subscriptions with Customer Portal. No webhook configuration required.

Tech Stack
Backend: Express.js
Payments: Stripe Checkout + Customer Portal
Language: JavaScript
Package Manager: npm
Port: 4242
Setup
1. Clone the Template
git clone --depth 1 https://github.com/Eng0AI/stripe-subscription.git .


If the directory is not empty:

git clone --depth 1 https://github.com/Eng0AI/stripe-subscription.git _temp_template
mv _temp_template/* _temp_template/.* . 2>/dev/null || true
rm -rf _temp_template

2. Remove Git History (Optional)
rm -rf .git
git init

3. Install Dependencies
npm install

4. Setup Environment Variables
cp .env.example .env


Required:

STRIPE_SECRET_KEY - Your Stripe secret key (sk_test_xxx)
STRIPE_PUBLISHABLE_KEY - Your Stripe publishable key (pk_test_xxx)

Optional (auto-created if not set):

BASIC_PRICE - Price ID for Starter plan ($12/month default)
PRO_PRICE - Price ID for Professional plan ($18/month default)
5. Start the Server
npm start


Server runs at http://localhost:4242. If price IDs are not set, it auto-creates subscription plans.

Deploy to Vercel
Step 1: Create Serverless API Wrapper

Create api/index.js with the Stripe subscription logic (see full deploy guide).

Step 2: Create Vercel Config

Create vercel.json:

{
  "version": 2,
  "buildCommand": "",
  "outputDirectory": "client/html",
  "rewrites": [
    { "source": "/config", "destination": "/api" },
    { "source": "/checkout-session", "destination": "/api" },
    { "source": "/create-checkout-session", "destination": "/api" },
    { "source": "/customer-portal", "destination": "/api" }
  ]
}

Step 3: Set Environment Variables
printf "YOUR_SECRET_KEY" | vercel env add STRIPE_SECRET_KEY production -t $VERCEL_TOKEN
printf "YOUR_PUBLISHABLE_KEY" | vercel env add STRIPE_PUBLISHABLE_KEY production -t $VERCEL_TOKEN

Step 4: Deploy
vercel --prod -t $VERCEL_TOKEN --yes

Deploy to Netlify

Create netlify/functions/api.js and netlify.toml with similar configuration, then:

netlify deploy --prod

Testing

Use test card numbers:

Success: 4242 4242 4242 4242
Decline: 4000 0000 0000 0002
Customer Portal Configuration

Before going live, configure at Stripe Dashboard > Settings > Billing > Customer Portal:

Enable: Update payment method, Cancel subscription, Switch plans
Going Live
Replace test keys with live keys (sk_live_/pk_live_)
Create subscription products in Stripe Dashboard Live mode
Complete Stripe account verification (KYC)
Configure Customer Portal for live mode
Test with a real subscription
Weekly Installs
40
Repository
eng0ai/eng0-tem…e-skills
GitHub Stars
4
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn