---
title: market-sizing-analysis
url: https://skills.sh/wshobson/agents/market-sizing-analysis
---

# market-sizing-analysis

skills/wshobson/agents/market-sizing-analysis
market-sizing-analysis
Installation
$ npx skills add https://github.com/wshobson/agents --skill market-sizing-analysis
Summary

Comprehensive market sizing framework for calculating TAM, SAM, and SOM across three methodologies.

Provides three complementary approaches: top-down (industry reports), bottom-up (customer segment calculations), and value theory (willingness to pay), with formulas and validation techniques for each
Includes step-by-step process covering market definition, data gathering, TAM/SAM/SOM calculations, and triangulation across methods
Offers industry-specific guidance for SaaS, marketplaces, consumer, and B2B services with tailored metrics and formulas
Covers presentation strategies for investors and internal strategy, plus common pitfalls like confusing TAM with SAM or overly aggressive market capture assumptions
SKILL.md
Market Sizing Analysis

Comprehensive market sizing methodologies for calculating Total Addressable Market (TAM), Serviceable Available Market (SAM), and Serviceable Obtainable Market (SOM) for startup opportunities.

Overview

Market sizing provides the foundation for startup strategy, fundraising, and business planning. Calculate market opportunity using three complementary methodologies: top-down (industry reports), bottom-up (customer segment calculations), and value theory (willingness to pay).

Core Concepts
The Three-Tier Market Framework

TAM (Total Addressable Market)

Total revenue opportunity if achieving 100% market share
Defines the universe of potential customers
Used for long-term vision and market validation
Example: All email marketing software revenue globally

SAM (Serviceable Available Market)

Portion of TAM targetable with current product/service
Accounts for geographic, segment, or capability constraints
Represents realistic addressable opportunity
Example: AI-powered email marketing for e-commerce in North America

SOM (Serviceable Obtainable Market)

Realistic market share achievable in 3-5 years
Accounts for competition, resources, and market dynamics
Used for financial projections and fundraising
Example: 2-5% of SAM based on competitive landscape
When to Use Each Methodology

Top-Down Analysis

Use when established market research exists
Best for mature, well-defined markets
Validates market existence and growth
Starts with industry reports and narrows down

Bottom-Up Analysis

Use when targeting specific customer segments
Best for new or niche markets
Most credible for investors
Builds from customer data and pricing

Value Theory

Use when creating new market categories
Best for disruptive innovations
Estimates based on value creation
Calculates willingness to pay for problem solution
Three-Methodology Framework
Methodology 1: Top-Down Analysis

Start with total market size and narrow to addressable segments.

Process:

Identify total market category from research reports
Apply geographic filters (target regions)
Apply segment filters (target industries/customers)
Calculate competitive positioning adjustments

Formula:

TAM = Total Market Category Size
SAM = TAM × Geographic % × Segment %
SOM = SAM × Realistic Capture Rate (2-5%)


When to use: Established markets with available research (e.g., SaaS, fintech, e-commerce)

Strengths: Quick, uses credible data, validates market existence

Limitations: May overestimate for new categories, less granular

Methodology 2: Bottom-Up Analysis

Build market size from customer segment calculations.

Process:

Define target customer segments
Estimate number of potential customers per segment
Determine average revenue per customer
Calculate realistic penetration rates

Formula:

TAM = Σ (Segment Size × Annual Revenue per Customer)
SAM = TAM × (Segments You Can Serve / Total Segments)
SOM = SAM × Realistic Penetration Rate (Year 3-5)


When to use: B2B, niche markets, specific customer segments

Strengths: Most credible for investors, granular, defensible

Limitations: Requires detailed customer research, time-intensive

Methodology 3: Value Theory

Calculate based on value created and willingness to pay.

Process:

Identify problem being solved
Quantify current cost of problem (time, money, inefficiency)
Calculate value of solution (savings, gains, efficiency)
Estimate willingness to pay (typically 10-30% of value)
Multiply by addressable customer base

Formula:

Value per Customer = Problem Cost × % Solved by Solution
Price per Customer = Value × Willingness to Pay % (10-30%)
TAM = Total Potential Customers × Price per Customer
SAM = TAM × % Meeting Buy Criteria
SOM = SAM × Realistic Adoption Rate


When to use: New categories, disruptive innovations, unclear existing markets

Strengths: Shows value creation, works for new markets

Limitations: Requires assumptions, harder to validate

Step-by-Step Process
Step 1: Define the Market

Clearly specify what market is being measured.

Questions to answer:

What problem is being solved?
Who are the target customers?
What's the product/service category?
What's the geographic scope?
What's the time horizon?

Example:

Problem: E-commerce companies struggle with email marketing automation
Customers: E-commerce stores with >$1M annual revenue
Category: AI-powered email marketing software
Geography: North America initially, global expansion
Horizon: 3-5 year opportunity
Step 2: Gather Data Sources

Identify credible data for calculations.

Top-Down Sources:

Industry research reports (Gartner, Forrester, IDC)
Government statistics (Census, BLS, trade associations)
Public company filings and earnings
Market research firms (Statista, CB Insights, PitchBook)

Bottom-Up Sources:

Customer interviews and surveys
Sales data and CRM records
Industry databases (LinkedIn, ZoomInfo, Crunchbase)
Competitive intelligence
Academic research

Value Theory Sources:

Customer problem quantification
Time/cost studies
ROI case studies
Pricing research and willingness-to-pay surveys
Step 3: Calculate TAM

Apply chosen methodology to determine total market.

For Top-Down:

Find total category size from research
Document data source and year
Apply growth rate if needed
Validate with multiple sources

For Bottom-Up:

Count total potential customers
Calculate average annual revenue per customer
Multiply to get TAM
Break down by segment

For Value Theory:

Quantify total addressable customer base
Calculate value per customer
Estimate pricing based on value
Multiply for TAM
Step 4: Calculate SAM

Narrow TAM to serviceable addressable market.

Apply Filters:

Geographic constraints (regions you can serve)
Product limitations (features you currently have)
Customer requirements (size, industry, use case)
Distribution channel access
Regulatory or compliance restrictions

Formula:

SAM = TAM × (% matching all filters)


Example:

TAM: $10B global email marketing
Geographic filter: 40% (North America)
Product filter: 30% (e-commerce focus)
Feature filter: 60% (need AI capabilities)
SAM = $10B × 0.40 × 0.30 × 0.60 = $720M
Step 5: Calculate SOM

Determine realistic obtainable market share.

Consider:

Current market share of competitors
Typical market share for new entrants (2-5%)
Resources available (funding, team, time)
Go-to-market effectiveness
Competitive advantages
Time to achieve (3-5 years typically)

Conservative Approach:

SOM (Year 3) = SAM × 2%
SOM (Year 5) = SAM × 5%


Example:

SAM: $720M
Year 3 SOM: $720M × 2% = $14.4M
Year 5 SOM: $720M × 5% = $36M
Step 6: Validate and Triangulate

Cross-check using multiple methods.

Validation Techniques:

Compare top-down and bottom-up results (should be within 30%)
Check against public company revenues in space
Validate customer count assumptions
Sense-check pricing assumptions
Review with industry experts
Compare to similar market categories

Red Flags:

TAM that's too small (< $1B for VC-backed startups)
TAM that's too large (unsupported by data)
SOM that's too aggressive (> 10% in 5 years for new entrant)
Inconsistency between methodologies (> 50% difference)
Industry-Specific Considerations
SaaS Markets

Key Metrics:

Number of potential businesses in target segment
Average contract value (ACV)
Typical market penetration rates
Expansion revenue potential

TAM Calculation:

TAM = Total Target Companies × Average ACV × (1 + Expansion Rate)

Marketplace Markets

Key Metrics:

Gross Merchandise Value (GMV) of category
Take rate (% of GMV you capture)
Total transactions or users

TAM Calculation:

TAM = Total Category GMV × Expected Take Rate

Consumer Markets

Key Metrics:

Total addressable users/households
Average revenue per user (ARPU)
Engagement frequency

TAM Calculation:

TAM = Total Users × ARPU × Purchase Frequency per Year

B2B Services

Key Metrics:

Number of target companies by size/industry
Average project value or retainer
Typical buying frequency

TAM Calculation:

TAM = Total Target Companies × Average Deal Size × Deals per Year

Presenting Market Sizing
For Investors

Structure:

Market definition and problem scope
TAM/SAM/SOM with methodology
Data sources and assumptions
Growth projections and drivers
Competitive landscape context

Key Points:

Lead with bottom-up calculation (most credible)
Show triangulation with top-down
Explain conservative assumptions
Link to revenue projections
Highlight market growth rate
For Strategy

Structure:

Addressable customer segments
Prioritization by opportunity size
Entry strategy by segment
Expected penetration timeline
Resource requirements

Key Points:

Focus on SAM and SOM
Show segment-level detail
Connect to go-to-market plan
Identify expansion opportunities
Discuss competitive positioning
Common Mistakes to Avoid

Mistake 1: Confusing TAM with SAM

Don't claim entire market as addressable
Apply realistic product/geographic constraints
Be honest about serviceable market

Mistake 2: Overly Aggressive SOM

New entrants rarely capture > 5% in 5 years
Account for competition and resources
Show realistic ramp timeline

Mistake 3: Using Only Top-Down

Investors prefer bottom-up validation
Top-down alone lacks credibility
Always triangulate with multiple methods

Mistake 4: Cherry-Picking Data

Use consistent, recent data sources
Don't mix methodologies inappropriately
Document all assumptions clearly

Mistake 5: Ignoring Market Dynamics

Account for market growth/decline
Consider competitive intensity
Factor in switching costs and barriers
Quick Start

To perform market sizing analysis:

Define the market - Problem, customers, category, geography
Choose methodology - Bottom-up (preferred) or top-down + triangulation
Gather data - Industry reports, customer data, competitive intelligence
Calculate TAM - Apply methodology formula
Narrow to SAM - Apply product, geographic, segment filters
Estimate SOM - 2-5% realistic capture rate
Validate - Cross-check with alternative methods
Document - Show methodology, sources, assumptions
Present - Structure for audience (investors, strategy, operations)
Weekly Installs
5.9K
Repository
wshobson/agents
GitHub Stars
34.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass