---
rating: ⭐⭐
title: process mapping
url: https://skills.sh/danhvb/my-ba-skills/process-mapping
---

# process mapping

skills/danhvb/my-ba-skills/Process Mapping
Process Mapping
Installation
$ npx skills add https://github.com/danhvb/my-ba-skills --skill 'Process Mapping'
SKILL.md
Process Mapping Skill
Purpose

Create clear, professional business process diagrams that visualize workflows, identify inefficiencies, and communicate processes to stakeholders and development teams.

When to Use
Documenting current state (As-Is) processes
Designing future state (To-Be) processes
Identifying process gaps and inefficiencies
Communicating workflows to stakeholders
System design and integration planning
Process Mapping Types
1. Flowcharts

Best for: Simple, linear processes Symbols:

⬭ Oval: Start/End
▭ Rectangle: Process/Activity
◇ Diamond: Decision
▱ Parallelogram: Input/Output
→ Arrow: Flow direction

Example - Order Processing:

Start → Receive Order → Validate Order → [Valid?]
                                           ├── Yes → Process Payment → [Paid?]
                                           │                            ├── Yes → Ship Order → End
                                           │                            └── No → Notify Customer → End
                                           └── No → Reject Order → End

2. BPMN 2.0 (Business Process Model and Notation)

Best for: Complex processes with multiple participants Key Elements:

Events: Start (○), Intermediate (◎), End (◉)
Activities: Tasks (▭), Sub-processes (▭+)
Gateways: Exclusive (◇×), Parallel (◇+), Inclusive (◇○)
Swimlanes: Pools and lanes for different actors

Example - Invoice Approval BPMN:

Pool: Invoice Approval Process
├── Lane: Requester
│   ├── Start Event
│   ├── Task: Submit Invoice
│   └── Task: Revise Invoice (if rejected)
├── Lane: Manager
│   ├── Task: Review Invoice
│   └── Gateway: Approve? (Yes/No)
├── Lane: Finance
│   ├── Task: Process Payment
│   └── End Event: Invoice Paid

3. Swimlane Diagrams

Best for: Cross-functional processes showing responsibilities Structure: Horizontal or vertical lanes for each role/department

Example - Customer Support:

| Customer        | Support Agent    | Technical Team   | Manager         |
|-----------------|------------------|------------------|-----------------|
| Submit Ticket   |                  |                  |                 |
|       ↓         |                  |                  |                 |
|                 | Receive & Triage |                  |                 |
|                 |       ↓          |                  |                 |
|                 | [Can Resolve?]   |                  |                 |
|                 | Yes: Resolve     |                  |                 |
|                 | No: ────────────→| Investigate      |                 |
|                 |                  |       ↓          |                 |
|                 |                  | [Need Escalation?]               |
|                 |                  | No: Fix & Return |                 |
|                 |                  | Yes: ───────────→| Approve Fix    |
|                 | Update Customer  |←─────────────────|                 |
| Receive Update  |←─────────────────|                  |                 |

4. Value Stream Mapping

Best for: Lean process improvement, identifying waste Elements: Process steps, wait times, value-add vs. non-value-add

Process Levels
L0: Context Diagram
High-level view of the entire system
Shows external entities and interactions
One page, executive summary level
L1: Process Area View
Major process areas/modules
Shows key inputs/outputs between areas
5-10 major processes
L2: Detailed Process Flow
Step-by-step activities within a process
Includes decisions and branches
Shows roles responsible
L3: Procedural Steps
Detailed procedures/work instructions
Screen-by-screen guidance
Used for training/SOPs
Mermaid Diagrams (Code-based)
Flowchart Example
flowchart TD
    A[Start: Customer Order] --> B{Inventory Available?}
    B -->|Yes| C[Reserve Inventory]
    B -->|No| D[Backorder]
    C --> E[Process Payment]
    E --> F{Payment Successful?}
    F -->|Yes| G[Create Shipment]
    F -->|No| H[Notify Customer]
    G --> I[Ship Order]
    I --> J[End: Order Delivered]
    D --> K[Notify Customer of Delay]
    H --> L[End: Order Cancelled]

Sequence Diagram Example
sequenceDiagram
    participant Customer
    participant WebApp
    participant PaymentAPI
    participant OrderService
    
    Customer->>WebApp: Submit Order
    WebApp->>OrderService: Create Order
    OrderService-->>WebApp: Order ID
    WebApp->>PaymentAPI: Process Payment
    PaymentAPI-->>WebApp: Payment Confirmed
    WebApp->>OrderService: Confirm Order
    OrderService-->>WebApp: Order Confirmed
    WebApp-->>Customer: Order Confirmation

State Diagram Example (Order Status)
stateDiagram-v2
    [*] --> Pending: Order Created
    Pending --> Processing: Payment Confirmed
    Pending --> Cancelled: Payment Failed
    Processing --> Shipped: Shipment Created
    Processing --> Cancelled: Customer Request
    Shipped --> Delivered: Delivery Confirmed
    Delivered --> Returned: Return Requested
    Returned --> Refunded: Refund Processed
    Delivered --> [*]
    Refunded --> [*]
    Cancelled --> [*]

Domain-Specific Process Examples
E-commerce: Checkout Flow
Start → View Cart → Enter Shipping → Select Shipping Method → 
Enter Payment → Review Order → Place Order → 
[Payment OK?] → Yes: Confirmation → End
              → No: Payment Error → Retry/Cancel

ERP: Purchase-to-Pay (P2P)
Requisition → Approval Workflow → Purchase Order → 
Goods Receipt → Invoice Receipt → 3-Way Match → 
[Match OK?] → Yes: Payment → End
           → No: Exception Handling

CRM: Lead-to-Close
Lead Capture → Lead Scoring → [Qualified?] → 
Yes: Create Opportunity → Discovery → Proposal → 
Negotiation → [Won?] → Yes: Close → Account Created
                     → No: Lost Analysis

CDP: Data Activation Flow
Data Collection → Identity Resolution → Profile Unification → 
Segmentation → Audience Building → Channel Activation → 
Campaign Execution → Response Tracking → Analytics

Best Practices
Design Principles

✅ Do:

Keep it simple and readable
Use consistent notation throughout
Include clear start and end points
Show decision points clearly
Document exceptions and error paths
Use swimlanes for multi-role processes
Add annotations for complex steps
Version control diagrams

❌ Don't:

Overcomplicate with too many details
Mix notation styles
Forget exception/error flows
Skip validation with stakeholders
Create without understanding the process first
Validation
Walk through with process owners
Verify with actual users
Test with real scenarios
Document assumptions
Get stakeholder sign-off
Tools
Figma
Design custom process diagrams
Use component libraries for BPMN symbols
Share for collaboration
Mermaid (Code-based)
Embed in markdown documentation
Version control friendly
Quick diagrams in Lark/Notion
Lucidchart/Miro
Professional BPMN diagrams
Real-time collaboration
Template libraries
Process Analysis Tips
Identify bottlenecks: Where do things slow down?
Find redundancies: What's duplicated?
Spot handoff issues: Where do things fall between cracks?
Question value: Does this step add value?
Consider automation: What can be automated?
Next Steps

After process mapping:

Gap analysis (see gap-analysis skill)
Process optimization recommendations
Requirements for system changes
UAT scenarios based on process flows
References
BPMN 2.0 Specification (OMG)
Value Stream Mapping (Lean)
Business Process Mapping best practices
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