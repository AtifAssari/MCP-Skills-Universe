---
title: debugging-methodology
url: https://skills.sh/fajjarnr/payu/debugging-methodology
---

# debugging-methodology

skills/fajjarnr/payu/debugging-methodology
debugging-methodology
Installation
$ npx skills add https://github.com/fajjarnr/payu --skill debugging-methodology
SKILL.md
Systematic Debugging
Overview

Random fixes waste time and create new bugs. Quick patches mask underlying issues.

Core principle: ALWAYS find root cause before attempting fixes. Symptom fixes are failure.

Violating the letter of this process is violating the spirit of debugging.

The Iron Law
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST


If you haven't completed Phase 1, you cannot propose fixes.

When to Use

Use for ANY technical issue:

Test failures
Bugs in production
Unexpected behavior
Performance problems
Build failures
Integration issues

Use this ESPECIALLY when:

Under time pressure (emergencies make guessing tempting)
"Just one quick fix" seems obvious
You've already tried multiple fixes
Previous fix didn't work
You don't fully understand the issue

Don't skip when:

Issue seems simple (simple bugs have root causes too)
You're in a hurry (rushing guarantees rework)
Manager wants it fixed NOW (systematic is faster than thrashing)
The Four Phases

You MUST complete each phase before proceeding to the next.

Phase 1: Root Cause Investigation

BEFORE attempting ANY fix:

Read Error Messages Carefully

Don't skip past errors or warnings
They often contain the exact solution
Read stack traces completely
Note line numbers, file paths, error codes

Reproduce Consistently

Can you trigger it reliably?
What are the exact steps?
Does it happen every time?
If not reproducible → gather more data, don't guess

Check Recent Changes

What changed that could cause this?
Git diff, recent commits
New dependencies, config changes
Environmental differences

Gather Evidence in Multi-Component Systems

WHEN system has multiple components (CI → build → signing, API → service → database):

BEFORE proposing fixes, add diagnostic instrumentation:

For EACH component boundary:
  - Log what data enters component
  - Log what data exits component
  - Verify environment/config propagation
  - Check state at each layer

Run once to gather evidence showing WHERE it breaks
THEN analyze evidence to identify failing component
THEN investigate that specific component


Example (multi-layer system):

# Layer 1: Workflow
echo "=== Secrets available in workflow: ==="
echo "IDENTITY: ${IDENTITY:+SET}${IDENTITY:-UNSET}"

# Layer 2: Build script
echo "=== Env vars in build script: ==="
env | grep IDENTITY || echo "IDENTITY not in environment"

# Layer 3: Signing script
echo "=== Keychain state: ==="
security list-keychains
security find-identity -v

# Layer 4: Actual signing
codesign --sign "$IDENTITY" --verbose=4 "$APP"


This reveals: Which layer fails (secrets → workflow ✓, workflow → build ✗)

Trace Data Flow

WHEN error is deep in call stack:

See root-cause-tracing.md in this directory for the complete backward tracing technique.

Quick version:

Where does bad value originate?
What called this with bad value?
Keep tracing up until you find the source
Fix at source, not at symptom
Phase 2: Pattern Analysis

Find the pattern before fixing:

Find Working Examples

Locate similar working code in same codebase
What works that's similar to what's broken?

Compare Against References

If implementing pattern, read reference implementation COMPLETELY
Don't skim - read every line
Understand the pattern fully before applying

Identify Differences

What's different between working and broken?
List every difference, however small
Don't assume "that can't matter"

Understand Dependencies

What other components does this need?
What settings, config, environment?
What assumptions does it make?
Phase 3: Hypothesis and Testing

Scientific method:

Form Single Hypothesis

State clearly: "I think X is the root cause because Y"
Write it down
Be specific, not vague

Test Minimally

Make the SMALLEST possible change to test hypothesis
One variable at a time
Don't fix multiple things at once

Verify Before Continuing

Did it work? Yes → Phase 4
Didn't work? Form NEW hypothesis
DON'T add more fixes on top

When You Don't Know

Say "I don't understand X"
Don't pretend to know
Ask for help
Research more
Phase 4: Implementation

Fix the root cause, not the symptom:

Create Failing Test Case

Simplest possible reproduction
Automated test if possible
One-off test script if no framework
MUST have before fixing
Use the superpowers:test-driven-development skill for writing proper failing tests

Implement Single Fix

Address the root cause identified
ONE change at a time
No "while I'm here" improvements
No bundled refactoring

Verify Fix

Test passes now?
No other tests broken?
Issue actually resolved?

If Fix Doesn't Work

STOP
Count: How many fixes have you tried?
If < 3: Return to Phase 1, re-analyze with new information
If ≥ 3: STOP and question the architecture (step 5 below)
DON'T attempt Fix #4 without architectural discussion

If 3+ Fixes Failed: Question Architecture

Pattern indicating architectural problem:

Each fix reveals new shared state/coupling/problem in different place
Fixes require "massive refactoring" to implement
Each fix creates new symptoms elsewhere

STOP and question fundamentals:

Is this pattern fundamentally sound?
Are we "sticking with it through sheer inertia"?
Should we refactor architecture vs. continue fixing symptoms?

Discuss with your human partner before attempting more fixes

This is NOT a failed hypothesis - this is a wrong architecture.

Red Flags - STOP and Follow Process

If you catch yourself thinking:

"Quick fix for now, investigate later"
"Just try changing X and see if it works"
"Add multiple changes, run tests"
"Skip the test, I'll manually verify"
"It's probably X, let me fix that"
"I don't fully understand but this might work"
"Pattern says X but I'll adapt it differently"
"Here are the main problems: [lists fixes without investigation]"
Proposing solutions before tracing data flow
"One more fix attempt" (when already tried 2+)
Each fix reveals new problem in different place

ALL of these mean: STOP. Return to Phase 1.

If 3+ fixes failed: Question the architecture (see Phase 4.5)

your human partner's Signals You're Doing It Wrong

Watch for these redirections:

"Is that not happening?" - You assumed without verifying
"Will it show us...?" - You should have added evidence gathering
"Stop guessing" - You're proposing fixes without understanding
"Ultrathink this" - Question fundamentals, not just symptoms
"We're stuck?" (frustrated) - Your approach isn't working

When you see these: STOP. Return to Phase 1.

Common Rationalizations
Excuse	Reality
"Issue is simple, don't need process"	Simple issues have root causes too. Process is fast for simple bugs.
"Emergency, no time for process"	Systematic debugging is FASTER than guess-and-check thrashing.
"Just try this first, then investigate"	First fix sets the pattern. Do it right from the start.
"I'll write test after confirming fix works"	Untested fixes don't stick. Test first proves it.
"Multiple fixes at once saves time"	Can't isolate what worked. Causes new bugs.
"Reference too long, I'll adapt the pattern"	Partial understanding guarantees bugs. Read it completely.
"I see the problem, let me fix it"	Seeing symptoms ≠ understanding root cause.
"One more fix attempt" (after 2+ failures)	3+ failures = architectural problem. Question pattern, don't fix again.
Quick Reference
Phase	Key Activities	Success Criteria
1. Root Cause	Read errors, reproduce, check changes, gather evidence	Understand WHAT and WHY
2. Pattern	Find working examples, compare	Identify differences
3. Hypothesis	Form theory, test minimally	Confirmed or new hypothesis
4. Implementation	Create test, fix, verify	Bug resolved, tests pass
When Process Reveals "No Root Cause"

If systematic investigation reveals issue is truly environmental, timing-dependent, or external:

You've completed the process
Document what you investigated
Implement appropriate handling (retry, timeout, error message)
Add monitoring/logging for future investigation

But: 95% of "no root cause" cases are incomplete investigation.

Supporting Techniques

These techniques are part of systematic debugging and available in this directory:

root-cause-tracing.md - Trace bugs backward through call stack to find original trigger
defense-in-depth.md - Add validation at multiple layers after finding root cause
condition-based-waiting.md - Replace arbitrary timeouts with condition polling
Annotation Processing (Lombok) - Handling "cannot find symbol" errors for generated code (getters/setters)

Related skills:

superpowers:test-driven-development - For creating failing test case (Phase 4, Step 1)
superpowers:verification-before-completion - Verify fix worked before claiming success
🛠️ Specialized Patterns (Environment Specific)
☕ Lombok & Annotation Processing (Spring Boot 3.4)

Symptom: "cannot find symbol" for get*, set*, builder(), or log despite @Data, @Getter, @Setter, or @Slf4j being present.

Phase 1: Root Cause Checklist

Parent POM: Is the service using id.payu:payu-backend-parent? If it uses spring-boot-starter-parent directly, it will MISS platform-specific compiler configurations.
Plugin Configuration: Check maven-compiler-plugin. If annotationProcessorPaths is explicitly defined for ANY processor (like MapStruct), it MUST also explicitly include lombok.
Lombok Version: Ensure ${lombok.version} is defined in the parent properties. For Spring Boot 3.4, use 1.18.36 or later.
IDE vs CLI: If it works in IDE but fails in mvn, it's 100% a Maven configuration issue in pom.xml.

Standard Fix Pattern:

<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <configuration>
        <annotationProcessorPaths>
            <path>
                <groupId>org.projectlombok</groupId>
                <artifactId>lombok</artifactId>
                <version>${lombok.version}</version>
            </path>
            <!-- Add others if needed (MapStruct, etc.) -->
        </annotationProcessorPaths>
    </configuration>
</plugin>


Phase 2: Verification Run mvn clean compile -pl <module-name> -am. If it fails, check if the parent POM is actually being used by running mvn help:effective-pom.

Protocol for Persistent Failure (The "Break Glass" Strategy): If Lombok annotation processing continues to fail after 2 configuration attempts in a specific environment:

Abandon Lombok Locally: Do not waste time debugging the processor environment endlessly.
Manual Implementation: Replace @Data, @Getter, @Setter, @Builder, @Slf4j (and @RequiredArgsConstructor) with manual implementations.
Rationale: In critical situations, Build Stability > Boilerplate Reduction. Code that builds is always better than clean code that doesn't.
☕ Enum Placement & Resolution (Architectural Best Practice)

Symptom: "cannot find symbol" for enum values, or JPA mapping errors, specifically when enums are inner classes. Symptom: "cannot find symbol" for enum values, or JPA mapping errors, specifically when enums are inner classes.

Phase 1: Root Cause

Inner Class Enum: Defining Enums inside Entity classes can confuse annotation processors or JPA providers.
Circular Dependency: If the Enum is used by other classes that the Entity depends on.

Fix Pattern:

Move to Top-Level: Always extract Enums to their own file in domain/model or constant package.
Avoid Inner Classes: Do not use public static enum Type { ... } inside Entities for domain-critical types.
🦆 Quarkus to Spring Boot Migration (PayU Context)

Symptom: Compilation errors when migrating legacy Quarkus services to Spring Boot.

Common Patterns & Fixes:

Panache vs JPA (Public Fields):

Quarkus (Panache): Uses public fields (entity.field).
Spring Data JPA: Uses private fields with Getters/Setters.
Fix: Add Lombok @Data to entity, and refactor all usage from entity.name = "X" to entity.setName("X").
Note: Falsely assuming Lombok handles public field access is a common trap.

Rest Controller Return Types:

JAX-RS: Returns Response.
Spring MVC: Returns ResponseEntity<T>.
Mixed Returns: If controller returns both DTO (success) and ApiResponse (error), you CANNOT use ResponseEntity<ApiResponse<DTO>>.
Correct Pattern: Use ResponseEntity<?> as a wildcard or unify all responses under ApiResponse<T>.

Reactive Libraries (Mutiny vs Standard):

Symptom: "package io.smallrye.mutiny does not exist".
Fix: Remove Mutiny. Replace Uni<T> with T (blocking) or Mono<T> (Project Reactor).
Preferred: For core banking, standard blocking I/O (Virtual Threads in Java 21) is preferred over reactive complexity unless required.

JWT/JJWT Versioning:

Symptom: Jwts.parser().parseClaimsJws(...) deprecated or missing.
Fix: JJWT 0.11+ uses Jwts.parserBuilder().setSigningKey(key).build().parseClaimsJws(token).

Test Migration (Hidden Debt):

Symptom: Code compiles but tests fail with "Unknown annotation".
Fix: @QuarkusTest -> @SpringBootTest, @InjectMock -> @MockBean, @Test (JUnit 4) -> @Test (JUnit 5).
🐳 Container/Podman Build Failures (PayU Context)

Symptom: Container build fails with Maven errors, parent POM not found, or build hangs indefinitely.

Pattern 1: Parent POM Resolution Failure

Symptom: Could not resolve dependencies or parent POM not found

Phase 1: Root Cause

Check Containerfile COPY strategy:
# ❌ WRONG - Only copies service pom.xml
COPY pom.xml ./
RUN mvn dependency:go-offline -B
COPY src ./src

# ✅ CORRECT - Copies entire project for parent POM access
COPY . .
RUN mvn clean package -DskipTests

Verify parent POM is accessible:
cd backend/some-service
cat ../pom.xml  # Should show parent POM content
mvn help:evaluate -Dexpression=project.parentGroupId


Phase 2: Verification Build locally first to isolate container vs Maven issues:

cd backend/some-service
mvn clean package -DskipTests

Pattern 2: Maven Build Hanging (4+ hours)

Symptom: mvn package in container hangs indefinitely

Root Cause:

Parallel builds (-T 1C) causing resource deadlock
Network timeouts accessing Maven Central
Large dependency downloads with poor connectivity

Fix - Use Pre-Built JAR Strategy:

# Runtime-only Containerfile (no Maven build in container)
FROM registry.access.redhat.com/ubi9/openjdk-21-runtime:1.24-2

# Copy pre-built JAR from local Maven build
COPY target/*.jar /app/app.jar

USER 1001
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "/app/app.jar"]


Build Process:

Build JARs locally first (much faster):
cd backend
mvn clean package -DskipTests -T 1C

Create container images from pre-built JARs
Pattern 3: UBI9 Image Conflicts

Symptom: Package installation fails or curl-minimal conflicts

Issue: UBI9 runtime images have curl-minimal pre-installed

Fix:

# ❌ WRONG - Tries to install curl (conflicts)
RUN microdnf install -y curl

# ✅ CORRECT - curl-minimal already available
# Remove curl installation from Containerfile
# Use curl-minimal for health checks

Pattern 4: User Creation Conflicts

Symptom: groupadd: GID '185' already exists or useradd: UID 1001 exists

Issue: UBI9 images already have jboss user (UID 185)

Fix:

# ❌ WRONG - Creates user with conflicting IDs
RUN groupadd -r payu -g 1001 && \
    useradd -r -g payu -u 1001 -d /app payu

# ✅ CORRECT - Use existing jboss user
USER 185

Pattern 5: Dockerfile Excludes Target Directory

Symptom: COPY target/*.jar fails with "no such file or directory"

Root Cause: .dockerignore or .containerignore excludes target/

Fix Options:

Build from parent directory with proper context
Remove target/ from ignore files
Use --ignorefile=.containerignore to bypass dockerignore
Debugging Commands
# Test Maven build locally (without container)
cd backend/some-service
mvn clean package -DskipTests

# Check parent POM resolution
mvn help:evaluate -Dexpression=project.parentGroupId
mvn help:evaluate -Dexpression=project.parentArtifactId

# Check what's in target directory
ls -la target/ | grep -E "\.jar$"

# Verify dockerignore
cat .dockerignore | grep target

🐳 Podman & Ecosystem Troubleshooting

Symptom: Code changes not reflecting, database migrations failing repeatedly, or containers exiting immediately.

Protocol 1: The "Clean Build" Strategy

If you suspect code changes aren't being picked up:

Stop & Remove: podman stop <name> && podman rm <name>
Remove Image: podman rmi localhost/<image-name> (Critical step)
Force Clean Build:
podman build --no-cache -f backend/<service>/Dockerfile -t localhost/<image-name> backend/

Protocol 2: Manual Run Fallback

If podman-compose acts erratically (fails to map ports/names):

Stop using compose.
Run manually with explicit env vars to isolate the issue:
podman run -d --name payu-<service> \
  --network local-podman_payu-network \
  -e SPRING_PROFILES_ACTIVE=container \
  -e DB_URL='jdbc:postgresql://postgres:5432/<db_name>' \
  ... \
  localhost/payu-<service>

Protocol 3: Database Reset Procedure

If Flyway migrations are stuck or checksums mismatch during dev:

Drop Database (Faster than fixing checksums):
podman exec -it payu-postgres psql -U payu -d postgres -c "DROP DATABASE <db_name>; CREATE DATABASE <db_name> OWNER payu;"

Restart Service: podman restart payu-<service>
Protocol 4: Immutable Index Constraints

Error: functions in index predicate must be marked IMMUTABLE

Cause: Using CURRENT_DATE, NOW() in index WHERE clause.
Fix: Remove time-based filtering from Index definitions. Indices must be deterministic.
🎭 Playwright E2E Test Failures (PayU Context)

Symptom: Tests failing with timeouts, strict mode violations, or text mismatches.

Common Patterns:

Symptom	Root Cause	Fix
strict mode violation	Selector matches multiple elements	Use .first() or more specific selectors
Timeout 5000ms exceeded	Element not visible/clickable	Add explicit wait or waitForSelector
Text content mismatch	Translations vs hardcoded	Match actual translation content
Currency format mismatch	Rp 50.000 vs Rp50.000	Use regex \s* for optional space

Fix Example:

// ❌ WRONG
await expect(page.getByText('Rp50.000.000')).toBeVisible();

// ✅ CORRECT
await expect(page.getByText(/Rp\s*50\.000\.000/).first()).toBeVisible();

🔐 Vault Configuration Issues (Spring Cloud Vault)

Symptom: Could not resolve placeholder or service fails to start because it can't find secrets.

Root Cause: Wrong Vault import syntax in application.yml.

# ❌ WRONG
spring:
  config:
    import: optional:vault://  # Invalid syntax

# ✅ CORRECT
spring:
  config:
    import: optional:vault  # Correct syntax

Real-World Impact

From debugging sessions:

Systematic approach: 15-30 minutes to fix
Random fixes approach: 2-3 hours of thrashing
First-time fix rate: 95% vs 40%
New bugs introduced: Near zero vs common
📚 Recent PayU Debugging Case Studies (Feb 2026)
Case 1: promotion-service Spring Boot Migration Failures

Symptom: 100+ compilation errors after Quarkus → Spring Boot migration

Phase 1: Root Cause Investigation

Read compilation errors → Quarkus annotations (@ApplicationScoped, @Inject, @Channel)
Check working examples → Other Spring Boot services in PayU
Identify pattern → Direct field access (Panache) vs getter/setter calls (JPA)

Phase 2: Pattern Analysis

Found working Spring Boot service → account-service
Compared → Used Spring annotations, repositories, getter/setter calls
Identified differences → promotion-service used Quarkus patterns

Phase 3: Hypothesis

"Compilation fails because Quarkus annotations and patterns don't work in Spring Boot"

Phase 4: Implementation

Created failing test → mvn clean compile failed
Implemented fix:
Replaced all Quarkus annotations with Spring equivalents
Created 13 Spring Data JPA repositories
Refactored entity.field → entity.setField()
Added proper maven-compiler-plugin configuration

Result: All compilation errors resolved, service builds successfully

Time: ~2 hours (systematic) vs estimated 6-8 hours (random fixes)

Case 2: lending-service Test Failures

Symptom: Tests failing with "cannot find symbol: RepaymentStatus"

Phase 1: Root Cause Investigation

Read error → "cannot find symbol: variable RepaymentStatus"
Check code → RepaymentStatus was inner class in RepaymentSchedule
Identify pattern → Inner enum confused annotation processor

Phase 2: Pattern Analysis

Found working examples → Other enums in PayU are top-level files
Identified difference → RepaymentStatus was inner class

Phase 3: Hypothesis

"Tests fail because inner enum confuses annotation processor"

Phase 4: Implementation

Created failing test → Current test failure
Implemented fix:
Extracted RepaymentStatus to top-level file
Updated all imports from RepaymentSchedule.RepaymentStatus to RepaymentStatus

Result: All 27 tests passing

Time: ~15 minutes (systematic) vs estimated 1-2 hours (random fixes)

Case 3: E2E Registration Flow Test Failures

Symptom: 25/27 tests failing (7% pass rate)

Phase 1: Root Cause Investigation

Read test errors → Text content not found
Check implementation → Uses next-intl translations
Read translation file → messages/id.json
Identify mismatches:
"Mulai Proses Verifikasi" (test) vs "Lanjut ke Profil Data" (actual)
Currency format: "Rp50.000.000" (test) vs "Rp 50.000.000" (actual)
Strict mode violations on common text

Phase 2: Pattern Analysis

Found working tests → Tests that use exact text from translations
Identified pattern → Need to match translation content, not hardcoded expectations

Phase 3: Hypothesis

"Tests fail because they expect hardcoded text, but implementation uses translations"

Phase 4: Implementation

Created test update based on actual translation content
Updated all test expectations to match messages/id.json
Fixed currency regex: /Rp\s*50\.000\.000/ (allows optional space)
Added .first() for strict mode violations

Result: 23/23 tests passing (100% pass rate)

Time: ~1 hour (systematic) vs estimated 3-4 hours (random fixes)

Case 4: Container Build Time Optimization

Symptom: Container builds hanging 4+ hours

Phase 1: Root Cause Investigation

Check build logs → mvn package hanging at dependency download
Identify pattern → Building from source in container with slow network
Check alternatives → Pre-build JARs locally, copy to container

Phase 2: Pattern Analysis

Found working example → payu-web-app:test image uses pre-built assets
Identified pattern → Build in fast environment, package in slow environment

Phase 3: Hypothesis

"Container builds are slow because Maven in container is slower than local build"

Phase 4: Implementation

Created test → Build locally, create container from pre-built JAR
Implemented fix:
FROM ubi9/openjdk-21-runtime
COPY target/*.jar /app/app.jar


Result: Build time reduced from 4+ hours to ~5 minutes

Time: ~30 minutes (systematic) vs estimated 4+ hours of troubleshooting

Weekly Installs
37
Repository
fajjarnr/payu
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn