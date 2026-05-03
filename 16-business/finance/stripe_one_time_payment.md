---
title: stripe-one-time-payment
url: https://skills.sh/eng0ai/eng0-template-skills/stripe-one-time-payment
---

# stripe-one-time-payment

skills/eng0ai/eng0-template-skills/stripe-one-time-payment
stripe-one-time-payment
Installation
$ npx skills add https://github.com/eng0ai/eng0-template-skills --skill stripe-one-time-payment
SKILL.md
Stripe One-Time Payment

Stripe Checkout integration for accepting one-time payments. No webhook configuration required.

Tech Stack
Backend: Express.js
Payments: Stripe Checkout
Language: JavaScript
Package Manager: npm
Port: 4242
Setup
1. Clone the Template
git clone --depth 1 https://github.com/Eng0AI/stripe-one-time-payment.git .


If the directory is not empty:

git clone --depth 1 https://github.com/Eng0AI/stripe-one-time-payment.git _temp_template
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

Optional:

PRICE - Price ID from Stripe Dashboard. If not set, a $20 sample product will be auto-created.
5. Start the Server
npm start


Server runs at http://localhost:4242. If PRICE is not set, it auto-creates a sample product.

Deploy to Vercel
Step 1: Create Serverless API Wrapper

Create api/index.js with the Stripe checkout logic (see full deploy guide).

Step 2: Create Vercel Config

Create vercel.json:

{
  "version": 2,
  "buildCommand": "",
  "outputDirectory": "client/html",
  "rewrites": [
    { "source": "/config", "destination": "/api" },
    { "source": "/checkout-session", "destination": "/api" },
    { "source": "/create-checkout-session", "destination": "/api" }
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

Any future expiry date and any 3-digit CVC will work.

Going Live
Replace test keys with live keys (sk_live_/pk_live_)
Create products in Stripe Dashboard Live mode
Complete Stripe account verification (KYC)
Test with a real payment
Weekly Installs
36
Repository
eng0ai/eng0-tem…e-skills
GitHub Stars
4
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail