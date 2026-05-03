---
title: laravel:iterating-on-code
url: https://skills.sh/jpcaparas/superpowers-laravel/laravel:iterating-on-code
---

# laravel:iterating-on-code

skills/jpcaparas/superpowers-laravel/laravel:iterating-on-code
laravel:iterating-on-code
Installation
$ npx skills add https://github.com/jpcaparas/superpowers-laravel --skill laravel:iterating-on-code
SKILL.md
Iterating on Code

AI-generated code rarely perfect on first try. Effective iteration gets you from "close" to "exactly right."

Incorrect Code
Vague Feedback

"This doesn't work"

Specific Feedback

"The validation is incorrect:

Current code:

'email' => 'required|email|unique:users'


Problem: This allows updating a user's email to another user's existing email. The unique rule needs to ignore the current user.

Fix:

'email' => [
    'required',
    'email',
    Rule::unique('users')->ignore($this->user()->id)
]


This allows the user to keep their own email but prevents duplicates with other users."

Why it works: Identifies the specific problem, explains why it's wrong, shows the correct solution.

Incomplete Code
Vague

"Something's missing"

Specific

"The OrderService is missing error handling:

Current implementation:

public function createOrder(array $data): Order
{
    $order = Order::create($data);
    $this->processPayment($order);
    return $order;
}


Missing:

Transaction wrapping (payment and order creation should be atomic)
Payment failure handling
Inventory validation before creating order
Event dispatching after successful creation

Add:

DB::transaction(function () use ($data) {
    $this->validateInventory($data['items']);
    $order = Order::create($data);
    $this->processPayment($order);
    event(new OrderCreated($order));
    return $order;
});


Plus add try/catch for payment failures."

Why it works: Lists specific missing pieces with context and shows how to add them.

Refinement Needed
Vague

"Make it better"

Specific

"Refine the query for better performance:

Current:

$products = Product::all()->filter(function ($product) {
    return $product->isActive() && $product->inStock();
});


Issues:

Loads all products into memory (inefficient for large datasets)
Filters in PHP instead of database
Calls methods on each product (N+1 potential)

Refined:

$products = Product::query()
    ->where('active', true)
    ->where('stock_quantity', '>', 0)
    ->get();


Move filtering to database, use indexed columns, avoid loading unnecessary data."

Why it works: Explains what needs refinement and why, shows the improved version.

Style Issues
Vague

"Follow our style guide"

Specific

"Update to match our coding standards:

Current:

public function get_user_orders($userId) {
    return Order::where('user_id', $userId)->get();
}


Style issues:

Method name should be camelCase: getUserOrders
Parameter should be camelCase: $userId ✓ (already correct)
Missing return type hint
Missing docblock for complex queries

Corrected:

/**
 * Get all orders for a specific user.
 */
public function getUserOrders(int $userId): Collection
{
    return Order::where('user_id', $userId)->get();
}


See our style guide: docs/coding-standards.md"

Why it works: Points to specific style violations, shows corrections, references the style guide.

Incremental Validation
Bad Approach

"Change the validation, add error handling, refactor the service, update the tests, and add logging"

Good Approach

"Let's iterate step by step:

Step 1: Fix the validation issue first

'email' => Rule::unique('users')->ignore($this->user()->id)


Let's verify this works before moving on."

[After validation confirmed working]

"Step 2: Now add error handling for the payment processing

try {
    $this->processPayment($order);
} catch (PaymentException $e) {
    Log::error('Payment failed', ['order' => $order->id]);
    throw new OrderProcessingException('Payment failed', previous: $e);
}


Test this before we continue."

Why it works: One change at a time, validate each step, build confidence incrementally.

Feedback Patterns
Pattern: Point Out + Explain + Show Fix
"The relationship is incorrect:

**Current:** `return $this->hasMany(Post::class);`

**Problem:** A User has many Posts, but you're defining this in the Post model. This creates a circular relationship.

**Fix:** Move this to the User model, or if you meant Post belongs to User:
```php
// In Post model
public function user(): BelongsTo
{
    return $this->belongsTo(User::class);
}
```"

Pattern: Missing + Why It Matters + How to Add
"Missing authorization check:

**Why it matters:** Any authenticated user can delete any order, not just their own.

**Add this to OrderController@destroy:**
```php
$this->authorize('delete', $order);


And create the policy method:

// In OrderPolicy
public function delete(User $user, Order $order): bool
{
    return $user->id === $order->user_id;
}
```"

Pattern: Current + Issues + Improved
"Current implementation has issues:

**Current:**
```php
foreach ($orders as $order) {
    $order->load('items', 'customer', 'shipping');
}


Issues:

N+1 queries (loads relationships in loop)
Inefficient for large datasets

Improved:

$orders = Order::with(['items', 'customer', 'shipping'])->get();


Single query with eager loading."


## Quick Reference

Iterate effectively:
- **Be specific** - Point to exact lines, explain exact problems
- **Show, don't just tell** - Provide corrected code
- **Explain why** - Help the AI understand the reasoning
- **One change at a time** - Validate incrementally
- **Reference standards** - Point to style guides, docs, examples

Specific feedback = better iterations = code that fits your needs.

Weekly Installs
48
Repository
jpcaparas/super…-laravel
GitHub Stars
131
First Seen
Jan 21, 2026