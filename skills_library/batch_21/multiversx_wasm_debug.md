---
title: multiversx-wasm-debug
url: https://skills.sh/multiversx/mx-ai-skills/multiversx-wasm-debug
---

# multiversx-wasm-debug

skills/multiversx/mx-ai-skills/multiversx-wasm-debug
multiversx-wasm-debug
Installation
$ npx skills add https://github.com/multiversx/mx-ai-skills --skill multiversx-wasm-debug
SKILL.md
MultiversX WASM Debugging

Analyze compiled output.wasm files for size optimization, panic investigation, and source-level debugging. This skill helps troubleshoot deployment issues and runtime errors.

When to Use
Contract deployment fails due to size limits
Investigating panic/trap errors at runtime
Optimizing WASM binary size
Understanding what's in your compiled contract
Mapping WASM errors back to Rust source code
1. Binary Size Analysis
Using Twiggy

Twiggy analyzes WASM binaries to identify what consumes space:

# Install twiggy
cargo install twiggy

# Top consumers of space
twiggy top output/my-contract.wasm

# Dominators analysis (what keeps what in the binary)
twiggy dominators output/my-contract.wasm

# Paths to specific functions
twiggy paths output/my-contract.wasm "function_name"

# Full call graph
twiggy callgraph output/my-contract.wasm > graph.dot

Sample Twiggy Output
 Shallow Bytes │ Shallow % │ Item
───────────────┼───────────┼─────────────────────────────────
         12847 │    18.52% │ data[0]
          8291 │    11.95% │ "function names" subsection
          5738 │     8.27% │ core::fmt::Formatter::pad
          4521 │     6.52% │ alloc::string::String::push_str

Common Size Bloat Causes
Cause	Size Impact	Solution
Panic messages	High	Use sc_panic! or strip in release
Format strings	High	Avoid format!, use static strings
JSON serialization	Very High	Use binary encoding
Large static arrays	High	Generate at runtime or store off-chain
Unused dependencies	Variable	Audit Cargo.toml
Debug symbols	High	Build in release mode
Size Reduction Techniques
# Cargo.toml - optimize for size
[profile.release]
opt-level = "z"        # Optimize for size
lto = true             # Link-time optimization
codegen-units = 1      # Better optimization, slower compile
panic = "abort"        # Smaller panic handling
strip = true           # Strip symbols

# Build optimized release
sc-meta all build --release

# Further optimize with wasm-opt
wasm-opt -Oz output/contract.wasm -o output/contract.opt.wasm

2. Panic Analysis
Understanding Contract Traps

When a contract traps (panics), you see:

error: execution terminated with signal: abort

Common Trap Causes
Symptom	Likely Cause	Investigation
unreachable	Panic without message	Check unwrap(), expect()
out of gas	Computation limit hit	Check loops, storage access
memory access	Buffer overflow	Check array indexing
integer overflow	Math operation	Check arithmetic
Finding Panics in WASM
# List all functions in WASM
wasm-objdump -x output/contract.wasm | grep "func\["

# Disassemble to find unreachable instructions
wasm-objdump -d output/contract.wasm | grep -B5 "unreachable"

# Count panic-related code
wasm-objdump -d output/contract.wasm | grep -c "panic"

Panic Message Stripping

By default, sc_panic! includes message strings. In production:

// Development - full messages
sc_panic!("Detailed error: invalid amount {}", amount);

// Production - stripped messages
// Build with --release and wasm-opt removes strings


Or use error codes:

const ERR_INVALID_AMOUNT: u32 = 1;
const ERR_UNAUTHORIZED: u32 = 2;

// Smaller binary, less descriptive
if amount == 0 {
    sc_panic!(ERR_INVALID_AMOUNT);
}

3. DWARF Debug Information
Building with Debug Symbols
# Build debug version with source mapping
sc-meta all build --wasm-symbols

# Alternative (equivalent)
sc-meta all build --wasm-symbols

Debug Build Output

Debug builds produce:

contract.wasm - Contract bytecode
contract.wasm.map - Source map (if available)
Larger file size with DWARF sections
Using Debug Information
# View DWARF info
wasm-objdump --debug output/contract.wasm

# List debug sections
wasm-objdump -h output/contract.wasm | grep "debug"

Source-Level Debugging

With debug symbols, you can:

Map WASM instruction addresses to Rust source lines
Set breakpoints at source locations
Inspect variable values (in compatible debuggers)
# Using wasmtime for debugging
wasmtime run --invoke function_name -g output/contract.wasm

4. WASM Structure Analysis
Examining Contract Structure
# Full WASM dump
wasm-objdump -x output/contract.wasm

# Sections overview
wasm-objdump -h output/contract.wasm

# Export functions (endpoints)
wasm-objdump -j Export -x output/contract.wasm

# Import functions (VM API calls)
wasm-objdump -j Import -x output/contract.wasm

Understanding WASM Sections
Section	Purpose	Audit Focus
Type	Function signatures	API surface
Import	VM API functions used	Capabilities
Function	Internal functions	Code size
Export	Public endpoints	Attack surface
Code	Actual bytecode	Logic
Data	Static data	Embedded secrets?
Name	Debug names	Information leak
Checking Exports
# List all exported functions
wasm-objdump -j Export -x output/contract.wasm | grep "func"

# Expected exports for MultiversX:
# - init: Constructor
# - upgrade: Upgrade handler
# - callBack: Callback handler
# - <endpoint_names>: Your endpoints

5. Gas Profiling
Estimating Gas Costs
# Deploy to devnet using sc-meta or an interactor
sc-meta all deploy --proxy https://devnet-gateway.multiversx.com --chain D

# Or use a Rust interactor for programmatic deployment
# See the multiversx-sc interactor pattern for details

Identifying Gas-Heavy Code

Common gas-intensive patterns:

Storage reads/writes
Cryptographic operations
Large data serialization
Loop iterations
// Gas-expensive
for item in self.large_list().iter() {  // N storage reads
    self.process(item);
}

// Gas-optimized
let batch_size = 10;
for i in 0..batch_size {
    let item = self.large_list().get(start_index + i);
    self.process(item);
}

6. Common Debugging Scenarios
Scenario: Contract Deployment Fails
# Check binary size
ls -la output/contract.wasm
# Max size is typically 256KB for deployment

# If too large, analyze and optimize
twiggy top output/contract.wasm

Scenario: Transaction Fails with unreachable
Check for unwrap() calls
Check for array index out of bounds
Check for division by zero
Build with debug and check DWARF info
Scenario: Gas Exceeded
# Build with debug to get better error location
sc-meta all build --wasm-symbols

# Profile the specific function
# Add logging to identify which loop/storage access is expensive

Scenario: Unexpected Behavior
// Add debug logging (remove in production)
#[endpoint]
fn debug_function(&self, input: BigUint) {
    // Log to events for debugging
    self.debug_event(&input);

    // Your logic
    let result = self.compute(input);

    self.debug_event(&result);
}

#[event("debug")]
fn debug_event(&self, value: &BigUint);

7. Tools Summary
Tool	Purpose	Install
twiggy	Size analysis	cargo install twiggy
wasm-objdump	WASM inspection	Part of wabt
wasm-opt	Size optimization	cargo install wasm-opt or part of binaryen
wasmtime	WASM runtime/debug	cargo install wasmtime
sc-meta	MultiversX build tool	cargo install multiversx-sc-meta
8. Best Practices
Always check release size before deployment
Profile on devnet before mainnet deployment
Use events for debugging instead of storage (cheaper)
Strip debug info in production builds
Monitor gas costs as contract evolves
Keep twiggy reports to track size changes over time
Weekly Installs
19
Repository
multiversx/mx-ai-skills
GitHub Stars
11
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn