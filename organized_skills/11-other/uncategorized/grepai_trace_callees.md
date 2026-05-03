---
rating: ⭐⭐⭐
title: grepai-trace-callees
url: https://skills.sh/yoanbernabeu/grepai-skills/grepai-trace-callees
---

# grepai-trace-callees

skills/yoanbernabeu/grepai-skills/grepai-trace-callees
grepai-trace-callees
Installation
$ npx skills add https://github.com/yoanbernabeu/grepai-skills --skill grepai-trace-callees
SKILL.md
GrepAI Trace Callees

This skill covers using grepai trace callees to find all functions called by a specific function.

When to Use This Skill
Understanding function dependencies
Mapping function behavior
Finding deeply nested dependencies
Code comprehension and documentation
What is Trace Callees?

grepai trace callees answers: "What does this function call?"

func ProcessOrder(order) {
    validateOrder(order)
    calculateTotal(order)
    sendConfirmation(order.email)
}
        │
        ↓
┌───────┴───────────────────┐
│  What does ProcessOrder   │
│  call?                    │
├───────────────────────────┤
│ • validateOrder           │
│ • calculateTotal          │
│ • sendConfirmation        │
└───────────────────────────┘

Basic Usage
grepai trace callees "FunctionName"

Example
grepai trace callees "ProcessOrder"


Output:

🔍 Callees of "ProcessOrder"

Found 4 callees:

1. validateOrder
   File: services/order.go:45
   Context: validateOrder(order)

2. calculateTotal
   File: services/order.go:48
   Context: total := calculateTotal(order.Items)

3. applyDiscount
   File: services/order.go:51
   Context: total = applyDiscount(total, order.Coupon)

4. sendConfirmation
   File: services/order.go:55
   Context: sendConfirmation(order.Email, total)

JSON Output
grepai trace callees "ProcessOrder" --json


Output:

{
  "query": "ProcessOrder",
  "mode": "callees",
  "count": 4,
  "results": [
    {
      "file": "services/order.go",
      "line": 45,
      "callee": "validateOrder",
      "context": "validateOrder(order)"
    },
    {
      "file": "services/order.go",
      "line": 48,
      "callee": "calculateTotal",
      "context": "total := calculateTotal(order.Items)"
    },
    {
      "file": "services/order.go",
      "line": 51,
      "callee": "applyDiscount",
      "context": "total = applyDiscount(total, order.Coupon)"
    },
    {
      "file": "services/order.go",
      "line": 55,
      "callee": "sendConfirmation",
      "context": "sendConfirmation(order.Email, total)"
    }
  ]
}

Compact JSON (AI Optimized)
grepai trace callees "ProcessOrder" --json --compact


Output:

{
  "q": "ProcessOrder",
  "m": "callees",
  "c": 4,
  "r": [
    {"f": "services/order.go", "l": 45, "fn": "validateOrder"},
    {"f": "services/order.go", "l": 48, "fn": "calculateTotal"},
    {"f": "services/order.go", "l": 51, "fn": "applyDiscount"},
    {"f": "services/order.go", "l": 55, "fn": "sendConfirmation"}
  ]
}

TOON Output (v0.26.0+)

TOON format offers ~50% fewer tokens than JSON:

grepai trace callees "ProcessOrder" --toon


Note: --json and --toon are mutually exclusive.

Extraction Modes
Fast Mode (Default)
grepai trace callees "ProcessOrder" --mode fast

Precise Mode
grepai trace callees "ProcessOrder" --mode precise

Mode	Speed	Accuracy	Dependencies
fast	⚡⚡⚡	Good	None
precise	⚡⚡	Excellent	tree-sitter
Use Cases
Understanding Function Behavior
# What does this complex function do?
grepai trace callees "handleRequest"

# Map the data flow
grepai trace callees "processPayment"

Finding Dependencies
# What external services does this call?
grepai trace callees "syncData"

# What database operations happen?
grepai trace callees "saveUser"

Code Review
# What side effects does this function have?
grepai trace callees "updateProfile"

# Is this function doing too much?
grepai trace callees "doEverything"  # Lots of callees = code smell

Documentation
# Generate dependency list for docs
grepai trace callees "initialize" --json | jq '.results[].callee'

Callers vs Callees
Command	Question	Use Case
trace callers	Who calls me?	Impact analysis
trace callees	What do I call?	Behavior analysis
# Combined analysis
grepai trace callers "processOrder"   # Who uses this?
grepai trace callees "processOrder"   # What does it do?

Filtering Results
By File Type
# Get callees and filter to only .go files
grepai trace callees "main" --json | jq '.results[] | select(.file | endswith(".go"))'

Exclude Test Functions
grepai trace callees "Login" --json | jq '.results[] | select(.callee | startswith("Test") | not)'

Count by Category
# Count how many database vs. API calls
grepai trace callees "processOrder" --json | jq '.results[].callee' | grep -c "db"

What Callees Includes

The trace finds:

Direct function calls
Method calls
Built-in function calls (depending on mode)
Example
func ProcessOrder(order Order) error {
    // Direct call
    validateOrder(order)

    // Method call
    order.Validate()

    // Package function
    utils.Log("processing")

    // Built-in (may or may not be captured)
    fmt.Println("done")

    return nil
}


Callees found:

validateOrder
Validate (method)
Log (from utils)
Println (depending on mode)
Limitations
What Callees Might Miss
Dynamic/runtime calls
Callbacks and closures
Interface method calls (may show interface, not implementation)
Reflection-based calls
Example of Undetected Call
func process(fn func()) {
    fn()  // Callee is unknown at static analysis time
}

Combining with Trace Graph

For recursive dependency analysis, use trace graph:

# Direct callees only
grepai trace callees "main"

# Full dependency tree (recursive)
grepai trace graph "main" --depth 3

Scripting Examples
List All Callees
grepai trace callees "main" --json | jq -r '.results[].callee' | sort -u

Check for Specific Callee
# Does processOrder call sendEmail?
grepai trace callees "processOrder" --json | jq -e '.results[] | select(.callee == "sendEmail")' && echo "Yes" || echo "No"

Generate Dependency Report
#!/bin/bash
echo "# Function Dependencies Report"
echo ""
for fn in main initialize processOrder; do
    echo "## $fn"
    grepai trace callees "$fn" --json | jq -r '.results[].callee' | sed 's/^/- /'
    echo ""
done

Common Issues

❌ Problem: Function not found ✅ Solution: Check spelling and ensure function exists in indexed files

❌ Problem: No callees found (but function has calls) ✅ Solutions:

Try --mode precise
Check language is in enabled_languages
Ensure symbols.gob is up to date (grepai watch)

❌ Problem: Missing some callees ✅ Solution: Use --mode precise for better accuracy

Best Practices
Use for understanding: Great for learning new codebases
Combine with callers: Full dependency picture
Use graph for deep analysis: When you need recursion
Filter results: Focus on relevant callees
Document findings: Export to markdown for docs
Output Format

Trace callees result:

🔍 Callees of "ProcessOrder"

Mode: fast
Function found in: services/order.go:40

Found 4 callees:

1. validateOrder
   File: services/order.go:45
   Context: validateOrder(order)

2. calculateTotal
   File: services/order.go:48
   Context: total := calculateTotal(order.Items)

3. applyDiscount
   File: services/order.go:51
   Context: total = applyDiscount(total, order.Coupon)

4. sendConfirmation
   File: services/order.go:55
   Context: sendConfirmation(order.Email, total)

Tip: Use 'grepai trace graph ProcessOrder' for recursive analysis

Weekly Installs
476
Repository
yoanbernabeu/gr…i-skills
GitHub Stars
16
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass