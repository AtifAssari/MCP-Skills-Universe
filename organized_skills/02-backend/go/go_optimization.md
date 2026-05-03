---
rating: ⭐⭐⭐
title: go-optimization
url: https://skills.sh/geoffjay/claude-plugins/go-optimization
---

# go-optimization

skills/geoffjay/claude-plugins/go-optimization
go-optimization
Installation
$ npx skills add https://github.com/geoffjay/claude-plugins --skill go-optimization
SKILL.md
Go Optimization Skill

This skill provides expert guidance on Go performance optimization, covering profiling, benchmarking, memory management, and runtime tuning for building high-performance applications.

When to Use

Activate this skill when:

Profiling application performance
Optimizing CPU-intensive operations
Reducing memory allocations
Tuning garbage collection
Writing benchmarks
Analyzing performance bottlenecks
Optimizing hot paths
Reducing lock contention
Profiling
CPU Profiling
import (
    "os"
    "runtime/pprof"
)

func main() {
    // Start CPU profiling
    f, err := os.Create("cpu.prof")
    if err != nil {
        log.Fatal(err)
    }
    defer f.Close()

    if err := pprof.StartCPUProfile(f); err != nil {
        log.Fatal(err)
    }
    defer pprof.StopCPUProfile()

    // Your code here
    runApplication()
}

// Analyze:
// go tool pprof cpu.prof
// (pprof) top10
// (pprof) list functionName
// (pprof) web

Memory Profiling
import (
    "os"
    "runtime"
    "runtime/pprof"
)

func writeMemProfile(filename string) {
    f, err := os.Create(filename)
    if err != nil {
        log.Fatal(err)
    }
    defer f.Close()

    runtime.GC() // Force GC before snapshot
    if err := pprof.WriteHeapProfile(f); err != nil {
        log.Fatal(err)
    }
}

// Analyze:
// go tool pprof -alloc_space mem.prof
// go tool pprof -inuse_space mem.prof

HTTP Profiling
import (
    _ "net/http/pprof"
    "net/http"
)

func main() {
    // Enable pprof endpoints
    go func() {
        log.Println(http.ListenAndServe("localhost:6060", nil))
    }()

    // Your application
    runServer()
}

// Access profiles:
// http://localhost:6060/debug/pprof/
// go tool pprof http://localhost:6060/debug/pprof/profile?seconds=30
// go tool pprof http://localhost:6060/debug/pprof/heap

Execution Tracing
import (
    "os"
    "runtime/trace"
)

func main() {
    f, err := os.Create("trace.out")
    if err != nil {
        log.Fatal(err)
    }
    defer f.Close()

    if err := trace.Start(f); err != nil {
        log.Fatal(err)
    }
    defer trace.Stop()

    // Your code
    runApplication()
}

// View trace:
// go tool trace trace.out

Benchmarking
Basic Benchmarks
func BenchmarkStringConcat(b *testing.B) {
    for i := 0; i < b.N; i++ {
        _ = "hello" + " " + "world"
    }
}

func BenchmarkStringBuilder(b *testing.B) {
    for i := 0; i < b.N; i++ {
        var sb strings.Builder
        sb.WriteString("hello")
        sb.WriteString(" ")
        sb.WriteString("world")
        _ = sb.String()
    }
}

// Run: go test -bench=. -benchmem

Sub-benchmarks
func BenchmarkEncode(b *testing.B) {
    data := generateTestData()

    b.Run("JSON", func(b *testing.B) {
        b.ReportAllocs()
        for i := 0; i < b.N; i++ {
            json.Marshal(data)
        }
    })

    b.Run("MessagePack", func(b *testing.B) {
        b.ReportAllocs()
        for i := 0; i < b.N; i++ {
            msgpack.Marshal(data)
        }
    })
}

Parallel Benchmarks
func BenchmarkConcurrentAccess(b *testing.B) {
    cache := NewCache()

    b.RunParallel(func(pb *testing.PB) {
        for pb.Next() {
            cache.Get("key")
        }
    })
}

Benchmark Comparison
# Run benchmarks and save results
go test -bench=. -benchmem > old.txt

# Make optimizations

# Run again and compare
go test -bench=. -benchmem > new.txt
benchstat old.txt new.txt

Memory Optimization
Escape Analysis
// Check what escapes to heap
// go build -gcflags="-m" main.go

// ✅ GOOD: Stack allocation
func stackAlloc() int {
    x := 42
    return x
}

// ❌ BAD: Heap escape
func heapEscape() *int {
    x := 42
    return &x // x escapes to heap
}

// ✅ GOOD: Interface without allocation
func noAlloc(w io.Writer, data []byte) {
    w.Write(data)
}

// ❌ BAD: Interface causes allocation
func withAlloc() io.Writer {
    var b bytes.Buffer
    return &b // &b escapes
}

Pre-allocation
// ❌ BAD: Growing slice
func badAppend(n int) []int {
    var result []int
    for i := 0; i < n; i++ {
        result = append(result, i) // Multiple allocations
    }
    return result
}

// ✅ GOOD: Pre-allocate
func goodAppend(n int) []int {
    result := make([]int, 0, n) // Single allocation
    for i := 0; i < n; i++ {
        result = append(result, i)
    }
    return result
}

// ✅ GOOD: Known length
func knownLength(n int) []int {
    result := make([]int, n)
    for i := 0; i < n; i++ {
        result[i] = i
    }
    return result
}

// ❌ BAD: String concatenation
func badConcat(strs []string) string {
    result := ""
    for _, s := range strs {
        result += s // New allocation each time
    }
    return result
}

// ✅ GOOD: strings.Builder
func goodConcat(strs []string) string {
    var sb strings.Builder
    sb.Grow(estimateSize(strs))
    for _, s := range strs {
        sb.WriteString(s)
    }
    return sb.String()
}

sync.Pool
var bufferPool = sync.Pool{
    New: func() interface{} {
        return new(bytes.Buffer)
    },
}

func processData(data []byte) []byte {
    // Get buffer from pool
    buf := bufferPool.Get().(*bytes.Buffer)
    buf.Reset()
    defer bufferPool.Put(buf)

    // Use buffer
    buf.Write(data)
    // Process...

    return buf.Bytes()
}

// String builder pool
var sbPool = sync.Pool{
    New: func() interface{} {
        return &strings.Builder{}
    },
}

func buildString(parts []string) string {
    sb := sbPool.Get().(*strings.Builder)
    sb.Reset()
    defer sbPool.Put(sb)

    for _, part := range parts {
        sb.WriteString(part)
    }
    return sb.String()
}

Zero-Copy Techniques
// Use byte slices instead of strings
func parseHeader(header []byte) (key, value []byte) {
    i := bytes.IndexByte(header, ':')
    if i < 0 {
        return nil, nil
    }
    return header[:i], header[i+1:]
}

// Reuse buffers
type Parser struct {
    buf []byte
}

func (p *Parser) Parse(data []byte) error {
    p.buf = p.buf[:0] // Reset length, keep capacity
    p.buf = append(p.buf, data...)
    // Process p.buf...
    return nil
}

// Direct writing
func writeResponse(w io.Writer, data interface{}) error {
    enc := json.NewEncoder(w) // Write directly to w
    return enc.Encode(data)
}

Garbage Collection Tuning
GC Control
import "runtime/debug"

// Adjust GC target percentage
debug.SetGCPercent(100) // Default
// Higher = less frequent GC, more memory
// Lower = more frequent GC, less memory

// Force GC (use sparingly!)
runtime.GC()

// Monitor GC stats
var stats runtime.MemStats
runtime.ReadMemStats(&stats)
fmt.Printf("Alloc = %v MB\n", stats.Alloc/1024/1024)
fmt.Printf("TotalAlloc = %v MB\n", stats.TotalAlloc/1024/1024)
fmt.Printf("Sys = %v MB\n", stats.Sys/1024/1024)
fmt.Printf("NumGC = %v\n", stats.NumGC)

GOGC Environment Variable
# Default (100%)
GOGC=100 ./myapp

# More aggressive GC (uses less memory)
GOGC=50 ./myapp

# Less frequent GC (uses more memory)
GOGC=200 ./myapp

# Disable GC (for debugging)
GOGC=off ./myapp

Concurrency Optimization
Reduce Lock Contention
// ❌ BAD: Single lock
type BadCache struct {
    mu    sync.Mutex
    items map[string]interface{}
}

// ✅ GOOD: RWMutex
type GoodCache struct {
    mu    sync.RWMutex
    items map[string]interface{}
}

func (c *GoodCache) Get(key string) interface{} {
    c.mu.RLock()
    defer c.mu.RUnlock()
    return c.items[key]
}

// ✅ BETTER: Sharded locks
type ShardedCache struct {
    shards [256]*shard
}

type shard struct {
    mu    sync.RWMutex
    items map[string]interface{}
}

func (c *ShardedCache) Get(key string) interface{} {
    shard := c.getShard(key)
    shard.mu.RLock()
    defer shard.mu.RUnlock()
    return shard.items[key]
}

Channel Buffering
// ❌ BAD: Unbuffered channel causes blocking
ch := make(chan int)

// ✅ GOOD: Buffered channel
ch := make(chan int, 100)

// Optimal buffer size depends on:
// - Producer/consumer rates
// - Memory constraints
// - Latency requirements

Atomic Operations
import "sync/atomic"

type Counter struct {
    value int64
}

func (c *Counter) Increment() {
    atomic.AddInt64(&c.value, 1)
}

func (c *Counter) Value() int64 {
    return atomic.LoadInt64(&c.value)
}

// ✅ Faster than mutex for simple operations
// ❌ Limited to basic types and operations

Algorithmic Optimization
Map Pre-sizing
// ❌ BAD: Growing map
func badMap(items []Item) map[string]Item {
    m := make(map[string]Item)
    for _, item := range items {
        m[item.ID] = item
    }
    return m
}

// ✅ GOOD: Pre-sized map
func goodMap(items []Item) map[string]Item {
    m := make(map[string]Item, len(items))
    for _, item := range items {
        m[item.ID] = item
    }
    return m
}

Avoid Unnecessary Work
// ❌ BAD: Repeated computation
func process(items []Item) {
    for _, item := range items {
        if isValid(item) {
            result := expensiveComputation(item)
            if result > threshold {
                handleResult(result)
            }
        }
    }
}

// ✅ GOOD: Early returns
func process(items []Item) {
    for _, item := range items {
        if !isValid(item) {
            continue // Skip early
        }
        result := expensiveComputation(item)
        if result <= threshold {
            continue // Skip early
        }
        handleResult(result)
    }
}

// ✅ BETTER: Fast path
func process(items []Item) {
    for _, item := range items {
        // Fast path for common case
        if item.IsSimple() {
            handleSimple(item)
            continue
        }
        // Slow path for complex case
        handleComplex(item)
    }
}

Runtime Tuning
GOMAXPROCS
import "runtime"

// Set number of OS threads
runtime.GOMAXPROCS(runtime.NumCPU())

// For CPU-bound: NumCPU
// For I/O-bound: NumCPU * 2 or more

Environment Variables
# Max OS threads
GOMAXPROCS=8 ./myapp

# GC aggressiveness
GOGC=100 ./myapp

# Memory limit (Go 1.19+)
GOMEMLIMIT=4GiB ./myapp

# Trace execution
GODEBUG=gctrace=1 ./myapp

Performance Patterns
Inline Functions
// Compiler inlines small functions automatically

//go:inline
func add(a, b int) int {
    return a + b
}

// Keep hot-path functions small for inlining

Avoid Interface Allocations
// ❌ BAD: Interface allocation
func badPrint(value interface{}) {
    fmt.Println(value) // value escapes
}

// ✅ GOOD: Type-specific functions
func printInt(value int) {
    fmt.Println(value)
}

func printString(value string) {
    fmt.Println(value)
}

Batch Operations
// ❌ BAD: Individual operations
for _, item := range items {
    db.Insert(item) // N database calls
}

// ✅ GOOD: Batch operations
db.BatchInsert(items) // 1 database call

Best Practices
Profile before optimizing - Measure, don't guess
Focus on hot paths - Optimize the 20% that matters
Reduce allocations - Reuse objects, pre-allocate
Use appropriate data structures - Map vs slice vs array
Minimize lock contention - Use RWMutex, sharding
Benchmark changes - Use benchstat for comparisons
Test with race detector - go test -race
Monitor in production - Use profiling endpoints
Balance readability and performance - Don't over-optimize
Use PGO - Profile-guided optimization (Go 1.20+)
Profile-Guided Optimization (PGO)
# 1. Build with profiling
go build -o myapp

# 2. Run and collect profile
./myapp -cpuprofile=default.pgo

# 3. Rebuild with PGO
go build -pgo=default.pgo -o myapp-optimized

# Performance improvement: 5-15% typical

Resources

Additional resources in:

assets/examples/ - Performance optimization examples
assets/benchmarks/ - Benchmark templates
references/ - Links to profiling guides and performance papers
Weekly Installs
25
Repository
geoffjay/claude-plugins
GitHub Stars
8
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass