---
rating: ⭐⭐⭐
title: llvm-security
url: https://skills.sh/gmh5225/awesome-llvm-security/llvm-security
---

# llvm-security

skills/gmh5225/awesome-llvm-security/llvm-security
llvm-security
Installation
$ npx skills add https://github.com/gmh5225/awesome-llvm-security --skill llvm-security
SKILL.md
LLVM Security Skill

This skill covers LLVM-based security features, sanitizers, hardening mechanisms, and secure software development practices.

Sanitizers
AddressSanitizer (ASan)

Detects memory errors: buffer overflow, use-after-free, use-after-scope.

# Compile with ASan
clang -fsanitize=address -g program.c -o program

# Key features
# - Stack buffer overflow detection
# - Heap buffer overflow detection  
# - Use-after-free detection
# - Memory leak detection

MemorySanitizer (MSan)

Detects uninitialized memory reads.

clang -fsanitize=memory -g program.c -o program

ThreadSanitizer (TSan)

Detects data races in multithreaded programs.

clang -fsanitize=thread -g program.c -o program

UndefinedBehaviorSanitizer (UBSan)

Detects undefined behavior at runtime.

clang -fsanitize=undefined -g program.c -o program

# Specific checks
clang -fsanitize=signed-integer-overflow,null program.c

Custom Sanitizer Development
// Implementing custom memory tracking
extern "C" void __asan_poison_memory_region(void const volatile *addr, size_t size);
extern "C" void __asan_unpoison_memory_region(void const volatile *addr, size_t size);

class SecureAllocator {
public:
    void* allocate(size_t size) {
        // Add red zones around allocation
        void* ptr = malloc(size + 2 * REDZONE_SIZE);
        __asan_poison_memory_region(ptr, REDZONE_SIZE);
        __asan_poison_memory_region((char*)ptr + REDZONE_SIZE + size, REDZONE_SIZE);
        return (char*)ptr + REDZONE_SIZE;
    }
};

Hardening Techniques
Stack Protection
# Stack canaries
clang -fstack-protector-strong program.c

# Stack clash protection
clang -fstack-clash-protection program.c

# Safe stack (separate stacks for safe/unsafe data)
clang -fsanitize=safe-stack program.c

Control Flow Integrity (CFI)
# Forward-edge CFI
clang -fsanitize=cfi -flto program.c

# Specific CFI schemes
clang -fsanitize=cfi-vcall      # Virtual call checks
clang -fsanitize=cfi-nvcall     # Non-virtual member call checks
clang -fsanitize=cfi-icall      # Indirect call checks

Shadow Call Stack
# Backward-edge protection (return address protection)
clang -fsanitize=shadow-call-stack program.c

Position Independent Executables
# Full ASLR support
clang -fPIE -pie program.c

# Position independent code for shared libraries
clang -fPIC -shared library.c -o library.so

Symbolic Execution
Integration with KLEE
// Mark symbolic inputs
#include <klee/klee.h>

int main() {
    int input;
    klee_make_symbolic(&input, sizeof(input), "input");
    
    if (input > 0) {
        // Path 1
    } else {
        // Path 2
    }
    return 0;
}

SymCC (Symbolic Execution via Compilation)

Compile-time instrumentation for symbolic execution:

Faster than IR interpretation
Supports complex real-world programs
Integrates with fuzzing workflows
Symbolic Analysis Tools
Caffeine: LLVM-based symbolic executor
SymSan: Symbolic execution + sanitizers
Haybale: Rust-based LLVM symbolic executor
Security-Focused Analysis
Type Checking at Runtime
// LLVM TypeSanitizer concepts
// Track type information through allocations
struct TypeInfo {
    const char* typeName;
    size_t typeSize;
    uint64_t typeHash;
};

void checkType(void* ptr, TypeInfo expected) {
    TypeInfo* actual = getTypeInfo(ptr);
    if (actual->typeHash != expected.typeHash) {
        reportTypeMismatch(ptr, actual, expected);
    }
}

Memory Leak Detection
// LeakSanitizer integration
extern "C" void __lsan_do_leak_check();
extern "C" void __lsan_disable();
extern "C" void __lsan_enable();

// Custom leak tracking
class PreciseLeakSanitizer {
    std::unordered_map<void*, AllocationInfo> allocations;
    
public:
    void recordAlloc(void* ptr, size_t size, const char* file, int line) {
        allocations[ptr] = {size, file, line, getStackTrace()};
    }
    
    void recordFree(void* ptr) {
        allocations.erase(ptr);
    }
    
    void reportLeaks() {
        for (auto& [ptr, info] : allocations) {
            fprintf(stderr, "Leak: %zu bytes at %s:%d\n", 
                    info.size, info.file, info.line);
        }
    }
};

Exploit Mitigation Implementation
Return Address Protection
; Shadow stack concept in LLVM IR
define void @protected_function() {
entry:
    %return_addr = call ptr @llvm.returnaddress(i32 0)
    call void @shadow_stack_push(ptr %return_addr)
    
    ; Function body...
    
    %saved_addr = call ptr @shadow_stack_pop()
    %current_addr = call ptr @llvm.returnaddress(i32 0)
    %match = icmp eq ptr %saved_addr, %current_addr
    br i1 %match, label %safe_return, label %attack_detected
    
safe_return:
    ret void
    
attack_detected:
    call void @abort()
    unreachable
}

Pointer Authentication (ARM)
// Using pointer authentication on ARM64
__attribute__((target("sign-return-address")))
void signed_function() {
    // Return address is cryptographically signed
}

Secure Compilation Pipeline
Build Flags Checklist
# Comprehensive hardening
CFLAGS="-O2 \
    -fstack-protector-strong \
    -fstack-clash-protection \
    -fcf-protection=full \
    -fPIE \
    -D_FORTIFY_SOURCE=2 \
    -Wformat -Wformat-security \
    -fsanitize=cfi -flto"

LDFLAGS="-pie \
    -Wl,-z,relro \
    -Wl,-z,now \
    -Wl,-z,noexecstack"

Compiler Security Checks
-Wformat-security: Format string vulnerabilities
-Warray-bounds: Array bounds violations
-Wshift-overflow: Shift operation overflows
-Wnull-dereference: Null pointer dereferences
Fuzzing Integration
libFuzzer
// Fuzz target template
extern "C" int LLVMFuzzerTestOneInput(const uint8_t *Data, size_t Size) {
    // Parse/process Data
    processInput(Data, Size);
    return 0;
}

Sanitizer + Fuzzer Combination
# Comprehensive fuzzing setup
clang -fsanitize=fuzzer,address,undefined \
      -fno-omit-frame-pointer \
      -g fuzz_target.c -o fuzzer

Windows-Specific Security
Control Flow Guard (CFG)
clang-cl /guard:cf program.c

SEH (Structured Exception Handling)
LLVM supports Windows SEH
Use for secure exception handling
Integrate with security monitoring
Resources

See Security Features, Sanitizer, and Symbolic Execution sections in README.md for comprehensive tool listings.

Getting Detailed Information

When you need detailed and up-to-date resource links, tool lists, or project references, fetch the latest data from:

https://raw.githubusercontent.com/gmh5225/awesome-llvm-security/refs/heads/main/README.md


This README contains comprehensive curated lists of:

Security features and hardening (Security Features section)
Sanitizers and memory safety tools (Sanitizer section)
Symbolic execution frameworks (Symbolic Execution section)
Memory leak detectors and runtime checkers
Weekly Installs
21
Repository
gmh5225/awesome…security
GitHub Stars
827
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn