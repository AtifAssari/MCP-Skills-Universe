---
rating: ⭐⭐
title: use case documentation
url: https://skills.sh/danhvb/my-ba-skills/use-case-documentation
---

# use case documentation

skills/danhvb/my-ba-skills/Use Case Documentation
Use Case Documentation
Installation
$ npx skills add https://github.com/danhvb/my-ba-skills --skill 'Use Case Documentation'
SKILL.md
Use Case Documentation Skill
Purpose

Describe how a user interactions with a system to achieve a specific goal. Use cases capture functional requirements from a user-centric perspective, often used in Waterfall or Hybrid environments where detailed specification is needed before implementation.

When to Use
Complex transactional systems (banking, healthcare).
When specific alternate flows and error handling must be rigorously defined.
Regulatory compliance requires detailed documentation.
Bridging gap between business needs and technical functional specs.
Anatomy of a Use Case
Key Elements
Use Case Name: Verb-Noun phrase (e.g., "Withdraw Cash").
ID: Unique identifier (e.g., UC-ATM-01).
Actor(s): Who interacts? (Primary: Initiates; Secondary: External systems).
Description: Brief summary of goal.
Preconditions: What must be true BEFORE this starts? (e.g., "User is logged in").
Trigger: What starts the use case? (e.g., "User clicks Withdraw").
Main Success Scenario (Basic Flow): The "Happy Path" steps.
Alternative Flows (Extensions): Variations or error paths.
Postconditions: What is true AFTER reliable completion? (e.g., "Balance updated").
Business Rules: Logic links.
Use Case Template
Example: Withdraw Cash at ATM

ID: UC-ATM-01 Name: Withdraw Cash Primary Actor: Bank Customer Secondary Actor: Bank System (Backend)

Description: Customer withdraws physical cash from their checking account via ATM.

Preconditions:

ATM has sufficient cash.
ATM is online.
Customer has valid card and PIN.

Trigger: Customer inserts card.

Main Success Scenario (Happy Path):

Customer inserts debit card.
System validates card readability.
System prompts for PIN.
Customer enters PIN.
System validates PIN with Bank System.
System displays Application Menu.
Customer selects "Withdraw Cash".
System prompts for Amount.
Customer enters Amount (e.g., $100).
System checks daily limit and account balance.
System authorizes transaction.
System dispenses Cash.
System prints Receipt.
System ejects Card.
Use case ends.

Alternative Flows:

A1: Invalid PIN (at Step 5)

System displays "Invalid PIN" message.
System prompts to re-enter PIN.
Customer re-enters PIN.
Resume at Step 5.
Constraint: If PIN invalid 3 times, perform A2 (Lock Card).

A2: Lock Card (from A1)

System displays "Card Locked due to attempts".
System retains card.
Use case ends.

A3: Insufficient Funds (at Step 10)

System determines account balance < requested amount.
System displays "Insufficient Funds".
System prompts to enter lower amount or cancel.
Customer enters new amount.
Resume at Step 10.

A4: ATM Out of Cash (at Step 10)

System checks internal cash dispenser > requested amount.
System detects low cash.
System displays "Unable to dispense full amount".
Use case ends.

Postconditions:

User account debited by withdrawal amount.
Transaction log created.
Cash inventory updated.
Use Case vs. User Story
Feature	Use Case	User Story
Focus	System interaction steps	User value/goal
Detail	High (Flows, Errors)	Low (Conversation starter)
Format	Document/Structured Text	card/Post-it (Who, What, Why)
Lifecycle	Update/Maintain over time	Done and discarded/archived
Context	Waterfall/Hybrid/Complex	Agile/Scrum
Best Practices
Write in Active Voice: "System validates PIN" (not "PIN is validated").
Keep it System-Neutral UI: Don't say "User clicks blue button at top right". Say "User selects Option".
Focus on Goal: Don't get lost in technical details (e.g., "System sends JSON packet").
Link Exceptions: Ensure every error path is handled.
Tools
Lark Docs / MS Word: Standard formatting.
Visual Paradigm / UML Tools: For Use Case Diagrams.
Gherkin: Can translate Use Case flows into Gherkin scenarios for testing.
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