---
rating: ⭐⭐
title: golang-safety
url: https://skills.sh/samber/cc-skills-golang/golang-safety
---

# golang-safety

skills/samber/cc-skills-golang/golang-safety
golang-safety
Installation
$ npx skills add https://github.com/samber/cc-skills-golang --skill golang-safety
SKILL.md

Persona: You are a defensive Go engineer. You treat every untested assumption about nil, capacity, and numeric range as a latent crash waiting to happen.

Go Safety: Correctness & Defensive Coding

Prevents programmer mistakes — bugs, panics, and silent data corruption in normal (non-adversarial) code. Security handles attackers; safety handles ourselves.

Best Practices Summary
Prefer generics over any when the type set is known — compiler catches mismatches instead of runtime panics
Always use comma-ok for type assertions — bare assertions panic on mismatch
Typed nil pointer in an interface is not == nil — the type descriptor makes it non-nil
Writing to a nil map panics — always initialize before use
append may reuse the backing array — both slices share memory if capacity allows, silently corrupting each other
Return defensive copies from exported functions — otherwise callers mutate your internals
defer runs at function exit, not loop iteration — extract loop body to a function
Integer conversions truncate silently — int64 to int32 wraps without error
Float arithmetic is not exact — use epsilon comparison or math/big
Design useful zero values — nil map fields panic on first write; use lazy init
Use sync.Once for lazy init — guarantees exactly-once even under concurrency
Nil Safety

Nil-related panics are the most common crash in Go.

The nil interface trap

Interfaces store (type, value). An interface is nil only when both are nil. Returning a typed nil pointer sets the type descriptor, making it non-nil:

// ✗ Dangerous — interface{type: *MyHandler, value: nil} is not == nil
func getHandler() http.Handler {
    var h *MyHandler // nil pointer
    if !enabled {
        return h // interface{type: *MyHandler, value: nil} != nil
    }
    return h
}

// ✓ Good — return nil explicitly
func getHandler() http.Handler {
    if !enabled {
        return nil // interface{type: nil, value: nil} == nil
    }
    return &MyHandler{}
}

Nil map, slice, and channel behavior
Type	Read from nil	Write to nil	Len/Cap of nil	Range over nil
Map	Zero value	panic	0	0 iterations
Slice	panic (index)	panic (index)	0	0 iterations
Channel	Blocks forever	Blocks forever	0	Blocks forever
// ✗ Bad — nil map panics on write
var m map[string]int
m["key"] = 1

// ✓ Good — initialize or lazy-init in methods
m := make(map[string]int)

func (r *Registry) Add(name string, val int) {
    if r.items == nil { r.items = make(map[string]int) }
    r.items[name] = val
}


See Nil Safety Deep Dive for nil receivers, nil in generics, and nil interface performance.

Slice & Map Safety
Slice aliasing — the append trap

append reuses the backing array if capacity allows. Both slices then share memory:

// ✗ Dangerous — a and b share backing array
a := make([]int, 3, 5)
b := append(a, 4)
b[0] = 99 // also modifies a[0]

// ✓ Good — full slice expression forces new allocation
b := append(a[:len(a):len(a)], 4)

Map concurrent access

Maps MUST NOT be accessed concurrently — → see samber/cc-skills-golang@golang-concurrency for sync primitives.

See Slice and Map Deep Dive for range pitfalls, subslice memory retention, and slices.Clone/maps.Clone.

Numeric Safety
Implicit type conversions truncate silently
// ✗ Bad — silently wraps around if val > math.MaxInt32 (3B becomes -1.29B)
var val int64 = 3_000_000_000
i32 := int32(val) // -1294967296 (silent wraparound)

// ✓ Good — check before converting
if val > math.MaxInt32 || val < math.MinInt32 {
    return fmt.Errorf("value %d overflows int32", val)
}
i32 := int32(val)

Float comparison
// ✗ Bad — floating point arithmetic is not exact
0.1+0.2 == 0.3 // false

// ✓ Good — use epsilon comparison
const epsilon = 1e-9
math.Abs((0.1+0.2)-0.3) < epsilon // true

Division by zero

Integer division by zero panics. Float division by zero produces +Inf, -Inf, or NaN.

func avg(total, count int) (int, error) {
    if count == 0 {
        return 0, errors.New("division by zero")
    }
    return total / count, nil
}


For integer overflow as a security vulnerability, see the samber/cc-skills-golang@golang-security skill section.

Resource Safety
defer in loops — resource accumulation

defer runs at function exit, not loop iteration. Resources accumulate until the function returns:

// ✗ Bad — all files stay open until function returns
for _, path := range paths {
    f, _ := os.Open(path)
    defer f.Close() // deferred until function exits
    process(f)
}

// ✓ Good — extract to function so defer runs per iteration
for _, path := range paths {
    if err := processOne(path); err != nil { return err }
}
func processOne(path string) error {
    f, err := os.Open(path)
    if err != nil { return err }
    defer f.Close()
    return process(f)
}

Goroutine leaks

→ See samber/cc-skills-golang@golang-concurrency for goroutine lifecycle and leak prevention.

Immutability & Defensive Copying

Exported functions returning slices/maps SHOULD return defensive copies.

Protecting struct internals
// ✗ Bad — exported slice field, anyone can mutate
type Config struct {
    Hosts []string
}

// ✓ Good — unexported field with accessor returning a copy
type Config struct {
    hosts []string
}

func (c *Config) Hosts() []string {
    return slices.Clone(c.hosts)
}

Initialization Safety
Zero-value design

Design types so var x MyType is safe — prevents "forgot to initialize" bugs:

var mu sync.Mutex   // ✓ usable at zero value
var buf bytes.Buffer // ✓ usable at zero value

// ✗ Bad — nil map panics on write
type Cache struct { data map[string]any }

sync.Once for lazy initialization
type DB struct {
    once sync.Once
    conn *sql.DB
}

func (db *DB) connection() *sql.DB {
    db.once.Do(func() {
        db.conn, _ = sql.Open("postgres", connStr)
    })
    return db.conn
}

init() function pitfalls

→ See samber/cc-skills-golang@golang-design-patterns for why init() should be avoided in favor of explicit constructors.

Enforce with Linters

Many safety pitfalls are caught automatically by linters: errcheck, forcetypeassert, nilerr, govet, staticcheck. See the samber/cc-skills-golang@golang-lint skill for configuration and usage.

Cross-References
→ See samber/cc-skills-golang@golang-concurrency skill for concurrent access patterns and sync primitives
→ See samber/cc-skills-golang@golang-data-structures skill for slice/map internals, capacity growth, and container/ packages
→ See samber/cc-skills-golang@golang-error-handling skill for nil error interface trap
→ See samber/cc-skills-golang@golang-security skill for security-relevant safety issues (memory safety, integer overflow)
→ See samber/cc-skills-golang@golang-troubleshooting skill for debugging panics and race conditions
Common Mistakes
Mistake	Fix
Bare type assertion v := x.(T)	Panics on type mismatch, crashing the program. Use v, ok := x.(T) to handle gracefully
Returning typed nil in interface function	Interface holds (type, nil) which is != nil. Return untyped nil for the nil case
Writing to a nil map	Nil maps have no backing storage — write panics. Initialize with make(map[K]V) or lazy-init
Assuming append always copies	If capacity allows, both slices share the backing array. Use s[:len(s):len(s)] to force a copy
defer in a loop	defer runs at function exit, not loop iteration — resources accumulate. Extract body to a separate function
int64 to int32 without bounds check	Values wrap silently (3B → -1.29B). Check against math.MaxInt32/math.MinInt32 first
Comparing floats with ==	IEEE 754 representation is not exact (0.1+0.2 != 0.3). Use math.Abs(a-b) < epsilon
Integer division without zero check	Integer division by zero panics. Guard with if divisor == 0 before dividing
Returning internal slice/map reference	Callers can mutate your struct's internals through the shared backing array. Return a defensive copy
Multiple init() with ordering assumptions	init() execution order across files is unspecified. → See samber/cc-skills-golang@golang-design-patterns — use explicit constructors
Blocking forever on nil channel	Nil channels block on both send and receive. Always initialize before use
Cross-References
→ See samber/cc-skills-golang@golang-continuous-integration skill for automated AI-driven code review in CI using these guidelines
Weekly Installs
1.8K
Repository
samber/cc-skills-golang
GitHub Stars
1.5K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass