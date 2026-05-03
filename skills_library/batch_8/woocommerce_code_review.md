---
title: woocommerce-code-review
url: https://skills.sh/woocommerce/woocommerce/woocommerce-code-review
---

# woocommerce-code-review

skills/woocommerce/woocommerce/woocommerce-code-review
woocommerce-code-review
Installation
$ npx skills add https://github.com/woocommerce/woocommerce --skill woocommerce-code-review
SKILL.md
WooCommerce Code Review

Review code changes against WooCommerce coding standards and conventions.

Critical Violations to Flag
Backend PHP Code

Consult the woocommerce-backend-dev skill for detailed standards. Using these standards as guidance, flag these violations and other similar ones:

Architecture & Structure:

❌ Standalone functions - Must use class methods (file-entities.md)
❌ Using new for DI-managed classes - Classes in src/ must use $container->get() (dependency-injection.md)
❌ Classes outside src/Internal/ - Default location unless explicitly public (file-entities.md)

Naming & Conventions:

❌ camelCase naming - Must use snake_case for methods/variables/hooks (code-entities.md)
❌ Yoda condition violations - Must follow WordPress Coding Standards (coding-conventions.md)

Documentation:

❌ Missing @since annotations - Required for public/protected methods and hooks (code-entities.md)
❌ Missing docblocks - Required for all hooks and methods (code-entities.md)
❌ Verbose docblocks - Keep concise, one line is ideal (code-entities.md)

Data Integrity:

❌ Missing validation - Must verify state before deletion/modification (data-integrity.md)

Testing:

❌ Using $instance in tests - Must use $sut variable name (unit-tests.md)
❌ Missing @testdox - Required in test method docblocks (unit-tests.md)
❌ Test file naming - Must follow convention for includes/ vs src/ (unit-tests.md)
UI Text & Copy

Consult the woocommerce-copy-guidelines skill. Flag:

❌ Title Case in UI - Must use sentence case (sentence-case.md)
Wrong: "Save Changes", "Order Details", "Payment Options"
Correct: "Save changes", "Order details", "Payment options"
Exceptions: Proper nouns (WooPayments), acronyms (API), brand names
Review Approach
Scan for critical violations listed above
Cite specific skill files when flagging issues
Provide correct examples from the skill documentation
Group related issues for clarity
Be constructive - explain why the standard exists when relevant
Output Format

For each violation found:

❌ [Issue Type]: [Specific problem]
Location: [File path and line number]
Standard: [Link to relevant skill file]
Fix: [Brief explanation or example]

Notes
All detailed standards are in the woocommerce-backend-dev, woocommerce-dev-cycle, and woocommerce-copy-guidelines skills
Consult those skills for complete context and examples
When in doubt, refer to the specific skill documentation linked above
Weekly Installs
402
Repository
woocommerce/woocommerce
GitHub Stars
10.3K
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass