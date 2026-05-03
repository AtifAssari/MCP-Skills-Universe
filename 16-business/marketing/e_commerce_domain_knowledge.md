---
title: e-commerce domain knowledge
url: https://skills.sh/danhvb/my-ba-skills/e-commerce-domain-knowledge
---

# e-commerce domain knowledge

skills/danhvb/my-ba-skills/E-commerce Domain Knowledge
E-commerce Domain Knowledge
Installation
$ npx skills add https://github.com/danhvb/my-ba-skills --skill 'E-commerce Domain Knowledge'
SKILL.md
E-commerce Domain Knowledge Skill
Purpose

Equip AI assistants with comprehensive e-commerce domain knowledge to analyze requirements, ask relevant questions, and create appropriate solutions for online retail platforms.

E-commerce Business Models
B2C (Business-to-Consumer)

Examples: Amazon, Shopify stores, Nike.com Characteristics:

High volume, lower transaction value
Focus on user experience and conversion
Marketing and promotions heavy
Customer reviews and ratings important
Fast checkout essential
B2B (Business-to-Business)

Examples: Alibaba, ThomasNet, Grainger Characteristics:

Lower volume, higher transaction value
Complex pricing (volume discounts, contracts)
Quote and RFQ processes
Account-based purchasing
Approval workflows
Net payment terms (Net 30, Net 60)
C2C (Consumer-to-Consumer)

Examples: eBay, Etsy, Facebook Marketplace Characteristics:

Platform facilitates transactions between individuals
Seller verification and ratings critical
Escrow or payment protection
Dispute resolution processes
Commission-based revenue
Marketplace

Examples: Amazon Marketplace, Shopee, Lazada Characteristics:

Multiple sellers on one platform
Seller onboarding and management
Commission and fee structures
Inventory from multiple sources
Seller performance metrics
Platform vs. seller fulfillment
Core E-commerce Modules
1. Product Catalog Management

Key Concepts:

Products: Individual items for sale
Variants: Different versions (size, color, material)
SKU: Stock Keeping Unit (unique identifier)
Categories: Hierarchical organization
Attributes: Product properties (brand, material, dimensions)
Digital Assets: Images, videos, 360° views, PDFs

Common Requirements:

Support for simple and configurable products
Variant management (size, color combinations)
Bulk product import/export
Product relationships (upsells, cross-sells, related products)
Inventory tracking per variant
Product search and filtering
SEO-friendly URLs and metadata

Example Requirement:

FR-CAT-001: Configurable Product Variants

System shall support configurable products with multiple variants:
- Product: T-Shirt
- Variant Attributes: Size (S, M, L, XL), Color (Red, Blue, Green)
- Each variant has unique SKU, price, inventory count
- Customer selects variant before adding to cart
- Out-of-stock variants are disabled but visible

2. Shopping Cart

Key Concepts:

Session Cart: Temporary cart for guest users
Persistent Cart: Saved cart for logged-in users
Cart Abandonment: User leaves without purchasing
Cart Recovery: Email reminders for abandoned carts

Common Requirements:

Add/remove/update items
Real-time inventory validation
Cart expiration and cleanup
Save cart for later
Cart sharing (B2B)
Mini cart preview
Cart abandonment tracking

Business Rules:

Reserve inventory when item added to cart (time-limited)
Remove out-of-stock items automatically
Apply quantity limits per product
Minimum order value requirements
Maximum cart size limits
3. Checkout & Payment

Checkout Flow Types:

Single-Page: All steps on one page (modern, higher conversion)
Multi-Step: Separate pages for shipping, payment, review
Express Checkout: One-click with saved payment (Amazon, Apple Pay)

Key Features:

Guest checkout
Address validation and autocomplete
Multiple shipping addresses (gift orders)
Shipping method selection with real-time pricing
Payment method selection
Order review before submission
Order confirmation

Payment Methods:

Credit/Debit cards (Visa, Mastercard, Amex)
Digital wallets (PayPal, Apple Pay, Google Pay)
Buy Now Pay Later (Klarna, Afterpay, Affirm)
Bank transfer
Cash on Delivery (COD)
Cryptocurrency (emerging)

Payment Gateway Integration:

Stripe: Popular, developer-friendly, global
PayPal: Trusted, high adoption, buyer protection
Square: Good for omnichannel (online + POS)
Adyen: Enterprise, multi-currency, global
Local Gateways: VNPay (Vietnam), Razorpay (India)

Security Requirements:

PCI DSS compliance (never store card numbers)
3D Secure authentication (SCA in Europe)
Fraud detection and prevention
SSL/TLS encryption
Tokenization for saved cards
4. Order Management

Order Lifecycle:

Pending → Processing → Shipped → Delivered → Completed
         ↓
      Cancelled (before shipping)
                           ↓
                        Returned (after delivery)


Key Features:

Order creation and confirmation
Order status tracking
Order history for customers
Order search and filtering
Order details (items, shipping, payment)
Invoice generation
Packing slips
Shipping labels
Order cancellation (before shipping)
Order modification (limited)

Admin Features:

Order dashboard
Bulk order processing
Order export (CSV, Excel)
Refund processing
Order notes and communication
5. Inventory Management

Inventory Tracking Methods:

Real-time: Inventory updated immediately on order
Batch: Inventory updated periodically
Reserved: Inventory reserved when added to cart

Key Concepts:

Stock Level: Current quantity available
Low Stock Threshold: Alert when inventory low
Backorder: Allow orders when out of stock
Pre-order: Accept orders before product available
Multi-warehouse: Inventory across multiple locations

Common Requirements:

Real-time inventory updates
Low stock alerts
Backorder management
Inventory reservations
Multi-warehouse support
Inventory sync with ERP/WMS
Inventory reports and forecasting
6. Shipping & Fulfillment

Shipping Options:

Standard shipping (5-7 days)
Express shipping (2-3 days)
Overnight shipping (1 day)
In-store pickup (BOPIS - Buy Online Pickup In Store)
Curbside pickup
Same-day delivery (urban areas)

Shipping Calculation Methods:

Flat Rate: Fixed price per order
Weight-Based: Price based on total weight
Price-Based: Free shipping over threshold
Real-time Carrier Rates: API integration with carriers
Zone-Based: Price by destination zone

Carrier Integrations:

USPS, UPS, FedEx, DHL (US/Global)
Local carriers (Giao Hàng Nhanh, J&T Vietnam)
Shipping aggregators (ShipStation, EasyShip)

Tracking:

Tracking number generation
Real-time tracking updates
Customer tracking page
Email/SMS notifications
Delivery confirmation
7. Promotions & Discounts

Promotion Types:

Percentage Off: 20% off entire order
Fixed Amount: $10 off orders over $50
Buy X Get Y: Buy 2 get 1 free
Free Shipping: Free shipping over $100
Bundle Deals: Product bundles at discount
Flash Sales: Time-limited offers
Loyalty Rewards: Points-based discounts

Promo Code Features:

Single-use vs. multi-use codes
Usage limits per customer
Expiration dates
Minimum order value
Specific products/categories
Stackable vs. non-stackable

Business Rules:

Discount application order (product → cart → shipping)
Exclusions (sale items, specific brands)
Limit one promo code per order
Employee discounts
Automatic discounts vs. code-required
8. Customer Management

Customer Data:

Account information (name, email, phone)
Shipping addresses (multiple)
Billing addresses
Order history
Wishlist
Saved payment methods
Preferences and settings

Customer Segmentation:

New vs. returning customers
VIP/high-value customers
Inactive customers (re-engagement)
Geographic segments
Purchase behavior segments

Loyalty Programs:

Points accumulation
Tier-based benefits (Silver, Gold, Platinum)
Rewards redemption
Referral programs
Birthday rewards
9. Search & Navigation

Search Features:

Keyword search
Autocomplete suggestions
Search results ranking (relevance, popularity, price)
Filters (price, brand, category, rating, availability)
Faceted search (multi-select filters)
Search analytics (popular searches, no-results searches)

Navigation:

Category hierarchy (mega menu)
Breadcrumbs
Related products
Recently viewed
Trending products

Search Technologies:

Elasticsearch (powerful, scalable)
Algolia (fast, typo-tolerant, hosted)
Solr (open-source, enterprise)
10. Reviews & Ratings

Features:

Star ratings (1-5 stars)
Written reviews
Review photos/videos
Verified purchase badge
Helpful votes
Review moderation
Response from seller
Review incentives

Business Value:

Increase conversion (social proof)
Improve SEO (user-generated content)
Product feedback for improvement
Build trust and credibility
Customer Journey
Awareness → Consideration → Purchase → Retention

1. Awareness:

SEO and content marketing
Social media advertising
Email marketing
Affiliate marketing

2. Consideration:

Product browsing
Search and filtering
Product comparison
Reviews and ratings
Wishlist

3. Purchase:

Add to cart
Checkout
Payment
Order confirmation

4. Retention:

Order tracking
Delivery
Post-purchase email
Review request
Loyalty program
Re-engagement campaigns
Key Metrics (KPIs)
Conversion Metrics
Conversion Rate: (Orders / Visitors) × 100
Cart Abandonment Rate: (Carts Created - Orders) / Carts Created × 100
Average Order Value (AOV): Total Revenue / Number of Orders
Revenue Per Visitor (RPV): Total Revenue / Total Visitors
Customer Metrics
Customer Acquisition Cost (CAC): Marketing Spend / New Customers
Customer Lifetime Value (LTV): Average Order Value × Purchase Frequency × Customer Lifespan
Repeat Purchase Rate: Repeat Customers / Total Customers × 100
Customer Retention Rate: ((CE - CN) / CS) × 100
Product Metrics
Best Sellers: Top products by revenue or units
Product Views: Page views per product
Add-to-Cart Rate: Add to Cart / Product Views × 100
Return Rate: Returns / Orders × 100
Operational Metrics
Order Fulfillment Time: Time from order to shipment
Inventory Turnover: Cost of Goods Sold / Average Inventory
Stock-out Rate: Out of Stock Events / Total Products × 100
Common Requirements Patterns
Mobile Commerce (M-commerce)
Responsive design (mobile-first)
Touch-optimized UI
Mobile payment methods (Apple Pay, Google Pay)
Progressive Web App (PWA)
Native mobile app
Push notifications
Offline browsing
Internationalization
Multi-currency support
Multi-language support
Country-specific payment methods
International shipping
Tax calculation by country
Localized content
Omnichannel
Unified inventory across channels
Buy online, pickup in store (BOPIS)
Return online purchases in store
Consistent pricing across channels
Cross-channel customer data
Integration Points
Common Integrations
Payment Gateway: Stripe, PayPal, Adyen
Shipping: ShipStation, EasyShip, carrier APIs
ERP: SAP, Oracle, NetSuite (inventory, orders)
CRM: Salesforce, HubSpot (customer data)
Email Marketing: Mailchimp, Klaviyo
Analytics: Google Analytics, Mixpanel
Reviews: Yotpo, Trustpilot
Live Chat: Zendesk, Intercom
Accounting: QuickBooks, Xero
Questions to Ask Stakeholders
Business Model
What type of e-commerce? (B2C, B2B, Marketplace)
Who are your target customers?
What's your average order value?
What's your current conversion rate?
Products
How many products/SKUs?
Simple or configurable products?
Digital or physical products?
How often do products change?
Checkout
Guest checkout allowed?
What payment methods?
What shipping options?
International shipping?
Integration
Existing systems to integrate?
ERP or inventory system?
CRM system?
Email marketing platform?
Scale
Expected traffic?
Peak season considerations?
Number of orders per day?
Growth projections?
References
Shopify E-commerce Blog
BigCommerce Resources
Baymard Institute (UX research)
E-commerce Platforms documentation
Weekly Installs
–
Repository
danhvb/my-ba-skills
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass