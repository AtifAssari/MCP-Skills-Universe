---
rating: ⭐⭐⭐
title: graalvm-native-image
url: https://skills.sh/giuseppe-trisciuoglio/developer-kit/graalvm-native-image
---

# graalvm-native-image

skills/giuseppe-trisciuoglio/developer-kit/graalvm-native-image
graalvm-native-image
Installation
$ npx skills add https://github.com/giuseppe-trisciuoglio/developer-kit --skill graalvm-native-image
SKILL.md
GraalVM Native Image for Java Applications

Expert skill for building high-performance native executables from Java applications using GraalVM Native Image, dramatically reducing startup time and memory consumption.

Overview

GraalVM Native Image compiles Java applications ahead-of-time (AOT) into standalone native executables. These executables start in milliseconds, require significantly less memory than JVM-based deployments, and are ideal for serverless functions, CLI tools, and microservices where fast startup and low resource usage are critical.

This skill provides a structured workflow to migrate JVM applications to native binaries, covering build tool configuration, framework-specific patterns, reflection metadata management, and an iterative approach to resolving native build failures.

When to Use

Use this skill when:

Converting a JVM-based Java application to a GraalVM native executable
Optimizing cold start times for serverless or containerized deployments
Reducing memory footprint (RSS) of Java microservices
Configuring Maven or Gradle with GraalVM Native Build Tools
Resolving ClassNotFoundException, NoSuchMethodException, or missing resource errors in native builds
Generating or editing reflect-config.json, resource-config.json, or other GraalVM metadata files
Using the GraalVM tracing agent to collect reachability metadata
Implementing RuntimeHints for Spring Boot native support
Building native images with Quarkus or Micronaut
Instructions
1. Contextual Project Analysis

Before any configuration, analyze the project to determine the build tool, framework, and dependencies:

Detect the build tool:

# Check for Maven
if [ -f "pom.xml" ]; then
    echo "Build tool: Maven"
    # Check for Maven wrapper
    [ -f "mvnw" ] && echo "Maven wrapper available"
fi

# Check for Gradle
if [ -f "build.gradle" ] || [ -f "build.gradle.kts" ]; then
    echo "Build tool: Gradle"
    [ -f "build.gradle.kts" ] && echo "Kotlin DSL"
    [ -f "gradlew" ] && echo "Gradle wrapper available"
fi


Detect the framework by analyzing dependencies:

Spring Boot: Look for spring-boot-starter-* in pom.xml or build.gradle
Quarkus: Look for quarkus-* dependencies
Micronaut: Look for micronaut-* dependencies
Plain Java: No framework dependencies detected

Check the Java version:

java -version 2>&1
# GraalVM Native Image requires Java 17+ (recommended: Java 21+)


Identify potential native image challenges:

Reflection-heavy libraries (Jackson, Hibernate, JAXB)
Dynamic proxy usage (JDK proxies, CGLIB)
Resource bundles and classpath resources
JNI or native library dependencies
Serialization requirements
2. Build Tool Configuration

Configure the appropriate build tool plugin based on the detected environment.

For Maven projects, add a dedicated native profile to keep the standard build clean. See the Maven Native Profile Reference for full configuration.

Key Maven setup:

<profiles>
  <profile>
    <id>native</id>
    <build>
      <plugins>
        <plugin>
          <groupId>org.graalvm.buildtools</groupId>
          <artifactId>native-maven-plugin</artifactId>
          <version>0.10.6</version>
          <extensions>true</extensions>
          <executions>
            <execution>
              <id>build-native</id>
              <goals>
                <goal>compile-no-fork</goal>
              </goals>
              <phase>package</phase>
            </execution>
          </executions>
          <configuration>
            <imageName>${project.artifactId}</imageName>
            <buildArgs>
              <buildArg>--no-fallback</buildArg>
            </buildArgs>
          </configuration>
        </plugin>
      </plugins>
    </build>
  </profile>
</profiles>


Build with: ./mvnw -Pnative package

For Gradle projects, apply the org.graalvm.buildtools.native plugin. See the Gradle Native Plugin Reference for full configuration.

Key Gradle setup (Kotlin DSL):

plugins {
    id("org.graalvm.buildtools.native") version "0.10.6"
}

graalvmNative {
    binaries {
        named("main") {
            imageName.set(project.name)
            buildArgs.add("--no-fallback")
        }
    }
}


Build with: ./gradlew nativeCompile

3. Framework-Specific Configuration

Each framework has its own AOT strategy. Apply the correct configuration based on the detected framework.

Spring Boot (3.x+): Spring Boot has built-in GraalVM support with AOT processing. See the Spring Boot Native Reference for patterns including RuntimeHints, @RegisterReflectionForBinding, and test support.

Key points:

Use spring-boot-starter-parent 3.x+ which includes the native profile
Register reflection hints via RuntimeHintsRegistrar
Run AOT processing with process-aot goal
Build with: ./mvnw -Pnative native:compile or ./gradlew nativeCompile

Quarkus and Micronaut: These frameworks are designed native-first and require minimal additional configuration. See the Quarkus & Micronaut Reference.

4. GraalVM Reachability Metadata

Native Image uses a closed-world assumption — all code paths must be known at build time. Dynamic features like reflection, resources, and proxies require explicit metadata configuration.

Metadata files are placed in META-INF/native-image/<group.id>/<artifact.id>/:

File	Purpose
reachability-metadata.json	Unified metadata (reflection, resources, JNI, proxies, bundles, serialization)
reflect-config.json	Legacy: Reflection registration
resource-config.json	Legacy: Resource inclusion patterns
proxy-config.json	Legacy: Dynamic proxy interfaces
serialization-config.json	Legacy: Serialization registration
jni-config.json	Legacy: JNI access registration

See the Reflection & Resource Config Reference for complete format and examples.

5. The Iterative Fix Engine

Native image builds often fail due to missing metadata. Follow this iterative approach:

Step 1 — Execute the native build:

# Maven
./mvnw -Pnative package 2>&1 | tee native-build.log

# Gradle
./gradlew nativeCompile 2>&1 | tee native-build.log


Step 2 — Parse build errors and identify the root cause:

Common error patterns and their fixes:

Error Pattern	Cause	Fix
ClassNotFoundException: com.example.MyClass	Missing reflection metadata	Add to reflect-config.json or use @RegisterReflectionForBinding
NoSuchMethodException	Method not registered for reflection	Add method to reflection config
MissingResourceException	Resource not included in native image	Add to resource-config.json
Proxy class not found	Dynamic proxy not registered	Add interface list to proxy-config.json
UnsupportedFeatureException: Serialization	Missing serialization metadata	Add to serialization-config.json

Step 3 — Apply fixes by updating the appropriate metadata file or using framework annotations.

Step 4 — Rebuild and verify. Repeat until the build succeeds.

Step 5 — If manual fixes are insufficient, use the GraalVM tracing agent to collect reachability metadata automatically. See the Tracing Agent Reference.

6. Validation and Benchmarking

Once the native build succeeds:

Verify the executable runs correctly:

# Run the native executable
./target/<app-name>

# For Spring Boot, verify the application context loads
curl http://localhost:8080/actuator/health


Measure startup time:

# Time the startup
time ./target/<app-name>

# For Spring Boot, check the startup log
./target/<app-name> 2>&1 | grep "Started .* in"


Measure memory footprint (RSS):

# On Linux
ps -o rss,vsz,comm -p $(pgrep <app-name>)

# On macOS
ps -o rss,vsz,comm -p $(pgrep <app-name>)


Compare with JVM baseline:

Metric	JVM	Native	Improvement
Startup time	~2-5s	~50-200ms	10-100x
Memory (RSS)	~200-500MB	~30-80MB	3-10x
Binary size	JRE + JARs	Single binary	Simplified
7. Docker Integration

Build minimal container images with native executables:

# Multi-stage build
FROM ghcr.io/graalvm/native-image-community:21 AS builder
WORKDIR /app
COPY . .
RUN ./mvnw -Pnative package -DskipTests

# Minimal runtime image
FROM debian:bookworm-slim
COPY --from=builder /app/target/<app-name> /app/<app-name>
EXPOSE 8080
ENTRYPOINT ["/app/<app-name>"]


For Spring Boot applications, use paketobuildpacks/builder-jammy-tiny with Cloud Native Buildpacks:

./mvnw -Pnative spring-boot:build-image

Best Practices
Start with the tracing agent on complex projects to generate an initial metadata baseline
Use the native profile to keep native-specific config separate from standard builds
Prefer --no-fallback to ensure a true native build (no JVM fallback)
Test with nativeTest to run JUnit tests in native mode
Use GraalVM Reachability Metadata Repository for third-party library metadata
Minimize reflection — prefer constructor injection and compile-time DI where possible
Include resource patterns explicitly rather than relying on classpath scanning
Profile before and after — always measure startup and memory improvements
Use Java 21+ for the best GraalVM compatibility and performance
Keep GraalVM and Native Build Tools versions aligned
Examples
Example 1: Adding Native Support to a Spring Boot Maven Project

Scenario: You have a Spring Boot 3.x REST API and want to compile it to a native executable.

Step 1 — Add the native profile to pom.xml:

<profiles>
  <profile>
    <id>native</id>
    <build>
      <plugins>
        <plugin>
          <groupId>org.springframework.boot</groupId>
          <artifactId>spring-boot-maven-plugin</artifactId>
          <executions>
            <execution>
              <id>process-aot</id>
              <goals>
                <goal>process-aot</goal>
              </goals>
            </execution>
          </executions>
        </plugin>
        <plugin>
          <groupId>org.graalvm.buildtools</groupId>
          <artifactId>native-maven-plugin</artifactId>
        </plugin>
      </plugins>
    </build>
  </profile>
</profiles>


Step 2 — Register reflection hints for DTOs:

@RestController
@RegisterReflectionForBinding({UserDto.class, OrderDto.class})
public class UserController {

    @GetMapping("/users/{id}")
    public UserDto getUser(@PathVariable Long id) {
        return userService.findById(id);
    }
}


Step 3 — Build and run:

./mvnw -Pnative native:compile
./target/myapp
# Started MyApplication in 0.089 seconds

Example 2: Resolving a Reflection Error in Native Build

Scenario: Native build fails with ClassNotFoundException for a Jackson-serialized DTO.

Error output:

com.oracle.svm.core.jdk.UnsupportedFeatureError:
  Reflection registration missing for class com.example.dto.PaymentResponse


Fix — Add to src/main/resources/META-INF/native-image/reachability-metadata.json:

{
  "reflection": [
    {
      "type": "com.example.dto.PaymentResponse",
      "allDeclaredConstructors": true,
      "allDeclaredMethods": true,
      "allDeclaredFields": true
    }
  ]
}


Or use the Spring Boot annotation approach:

@RegisterReflectionForBinding(PaymentResponse.class)
@Service
public class PaymentService { /* ... */ }

Example 3: Using the Tracing Agent for a Complex Project

Scenario: A project with many third-party libraries needs comprehensive reachability metadata.

# 1. Build the JAR
./mvnw package -DskipTests

# 2. Run with the tracing agent
java -agentlib:native-image-agent=config-output-dir=src/main/resources/META-INF/native-image \
    -jar target/myapp.jar

# 3. Exercise all endpoints
curl http://localhost:8080/api/users
curl -X POST http://localhost:8080/api/orders -H 'Content-Type: application/json' -d '{"item":"test"}'
curl http://localhost:8080/actuator/health

# 4. Stop the application (Ctrl+C), then build native
./mvnw -Pnative native:compile

# 5. Verify
./target/myapp

Constraints and Warnings
Critical Constraints
GraalVM Native Image requires Java 17+ (Java 21+ recommended for best compatibility)
Closed-world assumption: All code paths must be known at build time — dynamic class loading, runtime bytecode generation, and MethodHandles.Lookup may not work
Build time and memory: Native compilation is resource-intensive — expect 2-10 minutes and 4-8 GB RAM for typical projects
Not all libraries are compatible: Libraries relying heavily on reflection, dynamic proxies, or CGLIB may require extensive metadata configuration
AOT profiles are fixed at build time: Spring Boot @Profile and @ConditionalOnProperty are evaluated during AOT processing, not at runtime
Common Pitfalls
Forgetting --no-fallback: Without this flag, the build may silently produce a JVM fallback image instead of a true native executable
Incomplete tracing agent coverage: The agent only captures code paths exercised during the run — ensure all features are tested
Version mismatches: Keep GraalVM JDK, Native Build Tools plugin, and framework versions aligned to avoid incompatibilities
Classpath differences: The classpath at AOT/build time must match runtime — adding/removing JARs after native compilation causes failures
Security Considerations
Native executables are harder to decompile than JARs, but are not tamper-proof
Ensure secrets are not embedded in the native image at build time
Use environment variables or external config for sensitive data
Troubleshooting
Issue	Solution
Build runs out of memory	Increase build memory: -J-Xmx8g in buildArgs
Build takes too long	Use build cache, reduce classpath, enable quick build mode for dev
Application crashes at runtime	Missing reflection/resource metadata — run tracing agent
Spring Boot context fails to load	Check @Conditional beans and profile-dependent config
Third-party library not compatible	Check GraalVM Reachability Metadata repo or add manual hints
Weekly Installs
460
Repository
giuseppe-trisci…oper-kit
GitHub Stars
233
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass