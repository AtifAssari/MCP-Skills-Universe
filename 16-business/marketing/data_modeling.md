---
title: data modeling
url: https://skills.sh/danhvb/my-ba-skills/data-modeling
---

# data modeling

skills/danhvb/my-ba-skills/Data Modeling
Data Modeling
Installation
$ npx skills add https://github.com/danhvb/my-ba-skills --skill 'Data Modeling'
SKILL.md
Data Modeling Skill
Purpose

Create clear data models that document data structures, relationships, and business rules for system design and development.

When to Use
Designing new database structures
Documenting existing data for analysis
Defining data requirements in FRS
Integration design between systems
Data migration planning
Data Modeling Concepts
Entity Relationship Diagram (ERD)

Entities: Objects/things we store data about (e.g., Customer, Order, Product) Attributes: Properties of entities (e.g., customer_name, order_date) Relationships: How entities relate to each other

Relationship Types

One-to-One (1:1) Example: User ↔ UserProfile

One user has exactly one profile
One profile belongs to exactly one user

One-to-Many (1:N) Example: Customer → Orders

One customer can have many orders
One order belongs to one customer

Many-to-Many (M:N) Example: Products ↔ Categories

One product can be in many categories
One category can have many products
Requires junction/bridge table
Cardinality Notation (Crow's Foot)
||──────|| : One and only one (1:1)
||──────<  : One-to-Many (1:N)
>──────<   : Many-to-Many (M:N)
o|──────<  : Zero or one to Many
||──────o< : One to Zero or Many

ERD Examples
E-commerce ERD (Mermaid)
erDiagram
    CUSTOMER ||--o{ ORDER : places
    CUSTOMER {
        uuid customer_id PK
        string email UK
        string first_name
        string last_name
        string phone
        datetime created_at
    }
    ORDER ||--|{ ORDER_ITEM : contains
    ORDER {
        uuid order_id PK
        uuid customer_id FK
        string order_number UK
        decimal subtotal
        decimal tax
        decimal shipping
        decimal total
        string status
        datetime order_date
    }
    ORDER_ITEM {
        uuid item_id PK
        uuid order_id FK
        uuid product_id FK
        int quantity
        decimal unit_price
        decimal total_price
    }
    PRODUCT ||--o{ ORDER_ITEM : "included in"
    PRODUCT {
        uuid product_id PK
        string sku UK
        string name
        text description
        decimal price
        int stock_quantity
        string status
    }
    PRODUCT }|--|| CATEGORY : "belongs to"
    CATEGORY {
        uuid category_id PK
        string name
        uuid parent_id FK
    }

CRM ERD
erDiagram
    ACCOUNT ||--o{ CONTACT : has
    ACCOUNT ||--o{ OPPORTUNITY : has
    ACCOUNT {
        uuid account_id PK
        string name
        string industry
        string website
        int employee_count
        decimal annual_revenue
        uuid owner_id FK
    }
    CONTACT {
        uuid contact_id PK
        uuid account_id FK
        string first_name
        string last_name
        string email UK
        string phone
        string title
    }
    OPPORTUNITY }o--|| CONTACT : "primary contact"
    OPPORTUNITY {
        uuid opportunity_id PK
        uuid account_id FK
        uuid contact_id FK
        string name
        string stage
        decimal amount
        date close_date
        int probability
        uuid owner_id FK
    }
    LEAD {
        uuid lead_id PK
        string first_name
        string last_name
        string email
        string company
        string source
        int score
        string status
    }

Data Dictionary
Template
Attribute	Data Type	Size	Required	Default	Description	Validation
customer_id	UUID	-	Yes	Auto-gen	Unique identifier	UUID format
email	VARCHAR	255	Yes	-	Customer email	Valid email
status	ENUM	-	Yes	'active'	Account status	active, inactive, suspended
Example: Order Entity
Attribute	Type	Size	Required	Default	Description	Rules
order_id	UUID	-	Yes	Auto	Primary key	Unique
order_number	VARCHAR	20	Yes	Generated	Display number	Format: ORD-YYYYMMDD-XXXX
customer_id	UUID	-	Yes	-	FK to Customer	Must exist
order_date	DATETIME	-	Yes	NOW()	When order placed	Cannot be future
status	ENUM	-	Yes	'pending'	Order status	pending, processing, shipped, delivered, cancelled
subtotal	DECIMAL	10,2	Yes	0.00	Sum of items	>= 0
tax	DECIMAL	10,2	Yes	0.00	Calculated tax	>= 0
shipping_cost	DECIMAL	10,2	Yes	0.00	Shipping fee	>= 0
total	DECIMAL	10,2	Yes	-	Final total	= subtotal + tax + shipping
shipping_address	JSON	-	Yes	-	Delivery address	Valid address
billing_address	JSON	-	Yes	-	Billing address	Valid address
notes	TEXT	-	No	NULL	Order notes	Max 2000 chars
created_at	DATETIME	-	Yes	NOW()	Record created	Immutable
updated_at	DATETIME	-	Yes	NOW()	Last modified	Auto-update
Normalization
First Normal Form (1NF)
Eliminate repeating groups
Each cell contains single value
Each record is unique

❌ Bad: customer_phones = "123-456, 789-012" ✅ Good: Separate phone table with customer_id FK

Second Normal Form (2NF)
Meet 1NF
No partial dependencies (all non-key attributes depend on entire primary key)
Third Normal Form (3NF)
Meet 2NF
No transitive dependencies (non-key attributes don't depend on other non-key attributes)

❌ Bad: Order has customer_email (depends on customer_id, not order) ✅ Good: Get customer_email via Customer table join

Domain-Specific Data Patterns
E-commerce
Products with variants (SKU per variant)
Hierarchical categories
Shopping cart → Order transition
Address normalization
Price history tracking
ERP
Chart of Accounts structure
Multi-company data isolation
Master data (customer, vendor, product)
Transaction tables with journals
Audit trails
CRM
Lead → Contact → Account conversion
Activity logging (calls, emails, meetings)
Opportunity → Quote → Order pipeline
Campaign → Member → Response tracking
CDP
Customer identity resolution
Event/behavioral data (time-series)
Profile attributes (unified)
Segment membership
Consent tracking
Best Practices

✅ Do:

Use consistent naming conventions (snake_case)
Include audit fields (created_at, updated_at, created_by)
Define primary keys explicitly
Document foreign key relationships
Include data types and constraints
Consider soft deletes vs. hard deletes
Plan for data growth

❌ Don't:

Store calculated values (unless for performance)
Use ambiguous names
Skip documentation
Ignore data validation rules
Forget about NULL handling
Tools
Figma: Visual ERD design
Mermaid: Code-based diagrams in docs
dbdiagram.io: Quick ERD creation
Lucidchart: Professional diagrams
Next Steps

After data modeling:

Review with technical team
Include in FRS documentation
Create migration scripts
Plan data validation rules
Design API contracts based on data model
References
Database Normalization (1NF, 2NF, 3NF)
Entity Relationship Modeling
Data Dictionary Standards
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