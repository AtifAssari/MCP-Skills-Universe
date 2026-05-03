---
rating: ⭐⭐
title: frs creation
url: https://skills.sh/danhvb/my-ba-skills/frs-creation
---

# frs creation

skills/danhvb/my-ba-skills/FRS Creation
FRS Creation
Installation
$ npx skills add https://github.com/danhvb/my-ba-skills --skill 'FRS Creation'
SKILL.md
FRS Creation Skill
Purpose

Create comprehensive Functional Requirements Specifications (FRS) that provide detailed, technical requirements for development teams to implement business solutions.

When to Use
After BRD approval
Before development begins
When technical teams need detailed specifications
For complex features requiring detailed documentation
FRS vs BRD
Aspect	BRD	FRS
Audience	Business stakeholders, executives	Technical team, developers, QA
Focus	WHAT and WHY	HOW
Detail Level	High-level business requirements	Detailed functional specifications
Language	Business language	Technical language with business context
Scope	Entire project/initiative	Specific module or feature
FRS Structure
1. Introduction
Document purpose and scope
Related documents (BRD, use cases, user stories)
Intended audience
Document conventions and terminology
2. System Overview
High-level architecture
System context diagram
Integration points
Technology stack (if known)
3. Functional Requirements

Format for Each Requirement:

FR-[MODULE]-[NUMBER]: [Requirement Title]

Description: [Detailed description of what the system shall do]

Business Rule: [Any business logic or rules]

Input: [What data/triggers initiate this function]
Process: [Step-by-step what the system does]
Output: [What the system produces/displays]

Acceptance Criteria:
- [Specific, testable criterion 1]
- [Specific, testable criterion 2]

UI/UX Notes: [Any UI specifications, wireframe references]

Dependencies: [Other requirements this depends on]

Priority: Must Have | Should Have | Could Have

Complexity: Low | Medium | High


Example - E-commerce Checkout:

FR-CHK-001: Guest Checkout

Description: System shall allow users to complete purchase without creating an account

Business Rule: 
- Guest users must provide email for order confirmation
- After purchase, system shall offer account creation
- Guest checkout not available for orders > $5000

Input: User clicks "Checkout as Guest" button
Process:
1. System validates cart is not empty
2. System checks order total < $5000
3. System displays shipping address form
4. System validates address using address verification API
5. System displays shipping options with real-time pricing
6. System displays payment form
7. System processes payment via Stripe
8. System creates order record with guest flag
9. System sends confirmation email
10. System displays order confirmation page with option to create account

Output: 
- Order confirmation number
- Email confirmation sent
- Order record created in database

Acceptance Criteria:
- Guest can complete checkout in < 2 minutes
- All form fields have proper validation
- Address verification catches invalid addresses
- Payment processing completes in < 5 seconds
- Confirmation email sent within 1 minute
- Order appears in admin system immediately

UI/UX Notes: See Figma wireframes (link)
- Single-page checkout design
- Progress indicator at top
- Order summary sticky on right side
- Mobile-responsive layout

Dependencies: FR-PAY-001 (Payment Processing), FR-ORD-001 (Order Creation)

Priority: Must Have
Complexity: High

4. Data Requirements

Entity Definitions:

Data entities and attributes
Data types and constraints
Relationships between entities
Data validation rules

Example:

Entity: Order

Attributes:
- order_id (UUID, Primary Key, Required, Auto-generated)
- customer_id (UUID, Foreign Key to Customer, Optional for guest)
- order_number (String, Unique, Format: ORD-YYYYMMDD-XXXX)
- order_date (DateTime, Required, Default: Current timestamp)
- status (Enum, Required, Values: pending|processing|shipped|delivered|cancelled)
- subtotal (Decimal(10,2), Required, Min: 0.01)
- tax (Decimal(10,2), Required, Min: 0)
- shipping_cost (Decimal(10,2), Required, Min: 0)
- total (Decimal(10,2), Required, Calculated: subtotal + tax + shipping_cost)
- shipping_address (JSON, Required)
- billing_address (JSON, Required)
- payment_method (String, Required)
- payment_status (Enum, Required, Values: pending|authorized|captured|failed|refunded)
- created_at (DateTime, Required, Auto-generated)
- updated_at (DateTime, Required, Auto-updated)

Relationships:
- One Order has many OrderItems
- One Order belongs to one Customer (optional)
- One Order has one Payment

Business Rules:
- Order number must be unique
- Total must equal subtotal + tax + shipping_cost
- Status transitions: pending → processing → shipped → delivered
- Cancelled orders cannot be modified

5. Integration Requirements

For Each Integration:

External system name and purpose
Integration type (API, File, Real-time, Batch)
Data flow direction
Authentication method
Error handling
Frequency/timing

Example:

INT-001: Stripe Payment Gateway Integration

Purpose: Process credit card payments securely

Type: REST API, Real-time

Direction: Bidirectional
- Outbound: Payment intent creation, charge capture
- Inbound: Payment confirmation, webhook notifications

Authentication: API Key (Secret key for server, Publishable key for client)

Endpoints Used:
- POST /v1/payment_intents (Create payment intent)
- POST /v1/payment_intents/{id}/confirm (Confirm payment)
- POST /v1/refunds (Process refund)

Data Mapping:
- Order.total → PaymentIntent.amount
- Order.currency → PaymentIntent.currency
- Customer.email → PaymentIntent.receipt_email

Error Handling:
- Network timeout (30 seconds): Retry up to 3 times with exponential backoff
- Payment declined: Display user-friendly error, log details
- API error: Fallback to manual payment processing, alert admin

Webhooks:
- payment_intent.succeeded → Update order status to "processing"
- payment_intent.payment_failed → Update order status to "failed", notify customer
- charge.refunded → Update order status to "refunded"

SLA: 99.9% uptime, < 2 second response time

Testing: Use Stripe test mode with test card numbers

6. Business Rules

Document all business logic and rules:

Example:

BR-001: Shipping Cost Calculation
- Orders < $50: Standard shipping $5.99, Express $12.99
- Orders $50-$99: Standard shipping $3.99, Express $9.99  
- Orders ≥ $100: Free standard shipping, Express $7.99
- International orders: Calculated by weight and destination
- Alaska/Hawaii: Add $10 to standard rates

BR-002: Discount Application
- Only one promo code per order
- Promo codes cannot be combined with sale items
- Employee discount (20%) can be combined with promo codes
- Discounts applied before tax calculation
- Minimum order value may apply per promo code

BR-003: Inventory Reservation
- Items reserved for 15 minutes when added to cart
- Reservation extended by 15 minutes on each cart update
- Reservation released after 15 minutes of inactivity
- Out-of-stock items cannot be added to cart
- Backorder items can be added if enabled for product

7. UI/UX Specifications
Screen layouts and wireframes
User workflows and navigation
Form field specifications
Validation messages
Responsive design requirements
Accessibility requirements

Example:

Screen: Checkout Page

Layout: Single-page design with 3 sections
1. Shipping Information (left column)
2. Payment Information (left column, below shipping)
3. Order Summary (right column, sticky)

Shipping Information Fields:
- Email (required, email validation, max 100 chars)
- Full Name (required, min 2 chars, max 100 chars)
- Address Line 1 (required, max 100 chars)
- Address Line 2 (optional, max 100 chars)
- City (required, max 50 chars)
- State/Province (required, dropdown)
- ZIP/Postal Code (required, format validation based on country)
- Country (required, dropdown, default: US)
- Phone (required, phone format validation)

Validation:
- Real-time validation on blur
- Error messages displayed below field in red
- Submit button disabled until all required fields valid

Error Messages:
- Email: "Please enter a valid email address"
- Name: "Name must be at least 2 characters"
- ZIP: "Please enter a valid ZIP code"

Responsive:
- Desktop: 2-column layout
- Tablet: 2-column layout, narrower
- Mobile: Single column, order summary collapsible

Accessibility:
- All form fields have labels
- Error messages associated with fields (aria-describedby)
- Keyboard navigation support
- Screen reader compatible
- Color contrast ratio ≥ 4.5:1

8. Non-Functional Requirements
Performance requirements (response time, throughput)
Security requirements
Scalability requirements
Availability requirements
Browser/device compatibility
Accessibility standards
9. Assumptions & Constraints

Same as BRD but with technical details

10. Appendices
Glossary of terms
Wireframes and mockups
Data flow diagrams
State diagrams
API specifications
Domain-Specific FRS Guidelines
E-commerce FRS

Focus: Product catalog, cart, checkout, payment, order management Key Details: Payment gateway specs, inventory logic, pricing rules, shipping calculations

ERP FRS

Focus: Module workflows, approval processes, data migration, integrations Key Details: Complex business rules, multi-company logic, reporting specs

CRM FRS

Focus: Lead/opportunity management, sales pipeline, marketing automation Key Details: Scoring algorithms, workflow automation, integration specs

CDP FRS

Focus: Data collection, identity resolution, segmentation, activation Key Details: Data mapping, matching logic, API specifications

Mobile/Web FRS

Focus: UI/UX, offline sync, performance, platform-specific features Key Details: API contracts, caching strategy, push notifications

Best Practices

✅ Do:

Be specific and detailed
Include examples and edge cases
Reference wireframes and diagrams
Define all business rules explicitly
Specify error handling
Include acceptance criteria for each requirement
Use consistent numbering and formatting

❌ Don't:

Leave requirements ambiguous
Skip error scenarios
Assume developers know business context
Mix multiple requirements in one
Forget about edge cases
Ignore non-functional requirements
Tools
Lark Docs: Collaborative FRS writing
Notion: Requirements database with linking
Figma: Wireframes and UI specifications
Mermaid: Diagrams in markdown
Next Steps

After FRS completion:

Technical review with development team
Create use cases (see use-case-documentation skill)
Write user stories (see user-story-writing skill)
Define acceptance criteria (see acceptance-criteria skill)
Plan UAT (see uat-planning skill)
References
IEEE 29148 - Requirements Engineering
BABOK® Guide - Requirements specification
ISO/IEC 25010 - Software quality requirements
Weekly Installs
–
Repository
danhvb/my-ba-skills
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn