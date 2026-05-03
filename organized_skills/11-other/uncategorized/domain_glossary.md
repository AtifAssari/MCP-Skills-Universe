---
rating: ⭐⭐⭐
title: domain-glossary
url: https://skills.sh/kambleakash0/agent-skills/domain-glossary
---

# domain-glossary

skills/kambleakash0/agent-skills/domain-glossary
domain-glossary
Installation
$ npx skills add https://github.com/kambleakash0/agent-skills --skill domain-glossary
SKILL.md
Ubiquitous Language Glossary

This skill turns an ongoing conversation into a DDD-style ubiquitous language document. It scans for domain terms, resolves ambiguities, proposes canonical names, and writes a living glossary to DOMAIN_GLOSSARY.md in the working directory.

When to Use

Use this skill when:

You’re discussing a domain, feature, product, or system and want shared language.
You mention “ubiquitous language”, “domain model”, or “DDD”.
You keep tripping over overloaded terms (“account”, “user”, “customer”) and want them nailed down.

You can re-run this skill as the conversation evolves to keep the glossary up to date.

Process

Scan the conversation and context

Read the current conversation, plus any attached docs or PRDs, for domain-relevant nouns, verbs, and concepts.
Ignore generic technical terms (array, function, endpoint) unless they carry domain meaning here.

Detect language problems

Identify and note where:

The same word is used for different concepts (ambiguity).
Different words are used for the same concept (synonyms).
Terms are vague, overloaded, or inconsistently applied.

Propose a canonical glossary

Choose one canonical term per concept and be opinionated about names.
For each term, write a tight, one‑sentence definition that says what it is, not how it’s implemented.
List “aliases to avoid” so everyone sees which terms should be retired in this context.

Group terms into sections

Group related terms under headings (e.g. “Order lifecycle”, “People”, “Billing”, “Content model”).
Each group gets its own Markdown table with columns: Term, Definition, Aliases to avoid.
If everything belongs to a single cohesive cluster, one table is fine—don’t force fake groupings.

Describe relationships

Add a “Relationships” section that describes how the key terms relate to each other in plain language.
Use bold term names and, where obvious, simple cardinalities (e.g. “An Order has many Line items”).

Write an example dialogue

Add a short example conversation (3–5 exchanges) between a developer and a domain expert.
Use the canonical terms consistently and show how they interact in a realistic scenario.
Use this dialogue to clarify boundaries between easily-confused terms.

Write or update DOMAIN_GLOSSARY.md

If the file does not exist, create it with the structure described above.
If it exists, read it first, merge in new understanding, and update it in place.
Re-running

When invoked again in the same repo or conversation:

Read the existing DOMAIN_GLOSSARY.md.
Merge in new terms introduced since the last run.
Update definitions where understanding has clearly evolved.
Mark changed entries with “(updated)” and new entries with “(new)”.
Add any new ambiguities you’ve observed to “Flagged ambiguities”.
Refresh the example dialogue so it reflects the latest terms and relationships.
Output format

DOMAIN_GLOSSARY.md should roughly follow this pattern (adapt as needed):

# Ubiquitous Language

## <Domain cluster 1>

| Term | Definition | Aliases to avoid |
|------|------------|------------------|
| **Order** | A customer's request to purchase one or more items | Purchase, transaction |
| **Invoice** | A request for payment sent to a customer after delivery | Bill, payment request |

## <Domain cluster 2>

| Term | Definition | Aliases to avoid |
|------|------------|------------------|
| **Customer** | A person or organization that places orders | Client, buyer, account |
| **User** | An authentication identity in the system | Login, account |

## Relationships

- An **Invoice** belongs to exactly one **Customer**.
- An **Order** produces one or more **Invoices**.

## Example dialogue

> **Dev:** "When a **Customer** places an **Order**, do we create the **Invoice** immediately?"
> **Domain expert:** "No — an **Invoice** is generated only once a **Shipment** is fulfilled."
> ...

## Flagged ambiguities

- "account" is being used to mean both **Customer** and **User**. Prefer **Customer** for the business entity and **User** for authentication.


(Use actual terms from the current domain, not these placeholders.)

Behavior and Rules
Be opinionated. When multiple terms exist for the same concept, pick one canonical word and move others into “aliases to avoid”.
Keep definitions tight. One sentence, focused on identity (“what it is”), not procedure (“what it does”).
Only include domain terms. Skip generic infrastructure vocabulary unless it has a special meaning here.
Call out conflicts. Ambiguous or overloaded terms go into “Flagged ambiguities” with a clear recommendation.
Use the glossary going forward. After writing/updating the file, stick to the canonical terms in subsequent conversation.
Weekly Installs
10
Repository
kambleakash0/ag…t-skills
GitHub Stars
6
First Seen
Mar 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass