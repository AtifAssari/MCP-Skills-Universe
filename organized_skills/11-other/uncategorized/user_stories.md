---
rating: ⭐⭐
title: user-stories
url: https://skills.sh/phuryn/pm-skills/user-stories
---

# user-stories

skills/phuryn/pm-skills/user-stories
user-stories
Installation
$ npx skills add https://github.com/phuryn/pm-skills --skill user-stories
SKILL.md
User Stories

Create user stories following the 3 C's (Card, Conversation, Confirmation) and INVEST criteria. Generates stories with descriptions, design links, and acceptance criteria.

Use when: Writing user stories, breaking down features into stories, creating backlog items, or defining acceptance criteria.

Arguments:

$PRODUCT: The product or system name
$FEATURE: The new feature to break into stories
$DESIGN: Link to design files (Figma, Miro, etc.)
$ASSUMPTIONS: Key assumptions or context
Step-by-Step Process
Analyze the feature based on provided design and context
Identify user roles and distinct user journeys
Apply 3 C's framework:
Card: Simple title and one-liner
Conversation: Detailed discussion of intent
Confirmation: Clear acceptance criteria
Respect INVEST criteria: Independent, Negotiable, Valuable, Estimable, Small, Testable
Use plain language a primary school graduate can understand
Link to design files for visual reference
Output user stories in structured format
Story Template

Title: [Feature name]

Description: As a [user role], I want to [action], so that [benefit].

Design: [Link to design files]

Acceptance Criteria:

[Clear, testable criterion]
[Observable behavior]
[System validates correctly]
[Edge case handling]
[Performance or accessibility consideration]
[Integration point]
Example User Story

Title: Recently Viewed Section

Description: As an Online Shopper, I want to see a 'Recently viewed' section on the product page to easily revisit items I considered.

Design: [Figma link]

Acceptance Criteria:

The 'Recently viewed' section is displayed at the bottom of the product page for every user who has previously viewed at least 1 product.
It is not displayed for users visiting the first product page of their session.
The current product itself is excluded from the displayed items.
The section showcases product cards or thumbnails with images, titles, and prices.
Each product card indicates when it was viewed (e.g., 'Viewed 5 minutes ago').
Clicking on a product card leads the user to the corresponding product page.
Output Deliverables
Complete set of user stories for the feature
Each story includes title, description, design link, and 4-6 acceptance criteria
Stories are independent and can be developed in any order
Stories are sized for one sprint cycle
Stories reference related design documentation
Further Reading
How to Write User Stories: The Ultimate Guide
Weekly Installs
618
Repository
phuryn/pm-skills
GitHub Stars
10.8K
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass