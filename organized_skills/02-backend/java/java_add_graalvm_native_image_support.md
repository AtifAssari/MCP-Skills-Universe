---
rating: ⭐⭐
title: java-add-graalvm-native-image-support
url: https://skills.sh/github/awesome-copilot/java-add-graalvm-native-image-support
---

# java-add-graalvm-native-image-support

skills/github/awesome-copilot/java-add-graalvm-native-image-support
java-add-graalvm-native-image-support
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill java-add-graalvm-native-image-support
Summary

Automate GraalVM native image configuration, build, and error resolution for Java applications.

Detects project structure (Maven/Gradle) and framework (Spring Boot, Quarkus, Micronaut) to apply framework-specific native image setup
Adds GraalVM Native Build Tools plugins with appropriate configuration profiles and iteratively resolves build errors
Handles common native image issues including reflection, resource access, JNI, and dynamic proxy configuration through generated metadata files
Provides framework-specific guidance: Spring Boot RuntimeHints registration, Quarkus @RegisterForReflection patterns, and Micronaut @Introspected annotations
SKILL.md
GraalVM Native Image Agent

You are an expert in adding GraalVM native image support to Java applications. Your goal is to:

Analyze the project structure and identify the build tool (Maven or Gradle)
Detect the framework (Spring Boot, Quarkus, Micronaut, or generic Java)
Add appropriate GraalVM native image configuration
Build the native image
Analyze any build errors or warnings
Apply fixes iteratively until the build succeeds
Your Approach

Follow Oracle's best practices for GraalVM native images and use an iterative approach to resolve issues.

Step 1: Analyze the Project
Check if pom.xml exists (Maven) or build.gradle/build.gradle.kts exists (Gradle)
Identify the framework by checking dependencies:
Spring Boot: spring-boot-starter dependencies
Quarkus: quarkus- dependencies
Micronaut: micronaut- dependencies
Check for existing GraalVM configuration
Step 2: Add Native Image Support
For Maven Projects

Add the GraalVM Native Build Tools plugin within a native profile in pom.xml:

<profiles>
  <profile>
    <id>native</id>
    <build>
      <plugins>
        <plugin>
          <groupId>org.graalvm.buildtools</groupId>
          <artifactId>native-maven-plugin</artifactId>
          <version>[latest-version]</version>
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
            <mainClass>${main.class}</mainClass>
            <buildArgs>
              <buildArg>--no-fallback</buildArg>
            </buildArgs>
          </configuration>
        </plugin>
      </plugins>
    </build>
  </profile>
</profiles>


For Spring Boot projects, ensure the Spring Boot Maven plugin is in the main build section:

<build>
  <plugins>
    <plugin>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-maven-plugin</artifactId>
    </plugin>
  </plugins>
</build>

For Gradle Projects

Add the GraalVM Native Build Tools plugin to build.gradle:

plugins {
  id 'org.graalvm.buildtools.native' version '[latest-version]'
}

graalvmNative {
  binaries {
    main {
      imageName = project.name
      mainClass = application.mainClass.get()
      buildArgs.add('--no-fallback')
    }
  }
}


Or for Kotlin DSL (build.gradle.kts):

plugins {
  id("org.graalvm.buildtools.native") version "[latest-version]"
}

graalvmNative {
  binaries {
    named("main") {
      imageName.set(project.name)
      mainClass.set(application.mainClass.get())
      buildArgs.add("--no-fallback")
    }
  }
}

Step 3: Build the Native Image

Run the appropriate build command:

Maven:

mvn -Pnative native:compile


Gradle:

./gradlew nativeCompile


Spring Boot (Maven):

mvn -Pnative spring-boot:build-image


Quarkus (Maven):

./mvnw package -Pnative


Micronaut (Maven):

./mvnw package -Dpackaging=native-image

Step 4: Analyze Build Errors

Common issues and solutions:

Reflection Issues

If you see errors about missing reflection configuration, create or update src/main/resources/META-INF/native-image/reflect-config.json:

[
  {
    "name": "com.example.YourClass",
    "allDeclaredConstructors": true,
    "allDeclaredMethods": true,
    "allDeclaredFields": true
  }
]

Resource Access Issues

For missing resources, create src/main/resources/META-INF/native-image/resource-config.json:

{
  "resources": {
    "includes": [
      {"pattern": "application.properties"},
      {"pattern": ".*\\.yml"},
      {"pattern": ".*\\.yaml"}
    ]
  }
}

JNI Issues

For JNI-related errors, create src/main/resources/META-INF/native-image/jni-config.json:

[
  {
    "name": "com.example.NativeClass",
    "methods": [
      {"name": "nativeMethod", "parameterTypes": ["java.lang.String"]}
    ]
  }
]

Dynamic Proxy Issues

For dynamic proxy errors, create src/main/resources/META-INF/native-image/proxy-config.json:

[
  ["com.example.Interface1", "com.example.Interface2"]
]

Step 5: Iterate Until Success
After each fix, rebuild the native image
Analyze new errors and apply appropriate fixes
Use the GraalVM tracing agent to automatically generate configuration:
java -agentlib:native-image-agent=config-output-dir=src/main/resources/META-INF/native-image -jar target/app.jar

Continue until the build succeeds without errors
Step 6: Verify the Native Image

Once built successfully:

Test the native executable to ensure it runs correctly
Verify startup time improvements
Check memory footprint
Test all critical application paths
Framework-Specific Considerations
Spring Boot
Spring Boot 3.0+ has excellent native image support
Ensure you're using compatible Spring Boot version (3.0+)
Most Spring libraries provide GraalVM hints automatically
Test with Spring AOT processing enabled

When to Add Custom RuntimeHints:

Create a RuntimeHintsRegistrar implementation only if you need to register custom hints:

import org.springframework.aot.hint.RuntimeHints;
import org.springframework.aot.hint.RuntimeHintsRegistrar;

public class MyRuntimeHints implements RuntimeHintsRegistrar {
    @Override
    public void registerHints(RuntimeHints hints, ClassLoader classLoader) {
        // Register reflection hints
        hints.reflection().registerType(
            MyClass.class,
            hint -> hint.withMembers(MemberCategory.INVOKE_DECLARED_CONSTRUCTORS,
                                     MemberCategory.INVOKE_DECLARED_METHODS)
        );

        // Register resource hints
        hints.resources().registerPattern("custom-config/*.properties");

        // Register serialization hints
        hints.serialization().registerType(MySerializableClass.class);
    }
}


Register it in your main application class:

@SpringBootApplication
@ImportRuntimeHints(MyRuntimeHints.class)
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}


Common Spring Boot Native Image Issues:

Logback Configuration: Add to application.properties:

# Disable Logback's shutdown hook in native images
logging.register-shutdown-hook=false


If using custom Logback configuration, ensure logback-spring.xml is in resources and add to RuntimeHints:

hints.resources().registerPattern("logback-spring.xml");
hints.resources().registerPattern("org/springframework/boot/logging/logback/*.xml");


Jackson Serialization: For custom Jackson modules or types, register them:

hints.serialization().registerType(MyDto.class);
hints.reflection().registerType(
    MyDto.class,
    hint -> hint.withMembers(
        MemberCategory.DECLARED_FIELDS,
        MemberCategory.INVOKE_DECLARED_CONSTRUCTORS
    )
);


Add Jackson mix-ins to reflection hints if used:

hints.reflection().registerType(MyMixIn.class);


Jackson Modules: Ensure Jackson modules are on the classpath:

<dependency>
    <groupId>com.fasterxml.jackson.datatype</groupId>
    <artifactId>jackson-datatype-jsr310</artifactId>
</dependency>

Quarkus
Quarkus is designed for native images with zero configuration in most cases
Use @RegisterForReflection annotation for reflection needs
Quarkus extensions handle GraalVM configuration automatically

Common Quarkus Native Image Tips:

Reflection Registration: Use annotations instead of manual configuration:

@RegisterForReflection(targets = {MyClass.class, MyDto.class})
public class ReflectionConfiguration {
}


Or register entire packages:

@RegisterForReflection(classNames = {"com.example.package.*"})


Resource Inclusion: Add to application.properties:

quarkus.native.resources.includes=config/*.json,templates/**
quarkus.native.additional-build-args=--initialize-at-run-time=com.example.RuntimeClass


Database Drivers: Ensure you're using Quarkus-supported JDBC extensions:

<dependency>
    <groupId>io.quarkus</groupId>
    <artifactId>quarkus-jdbc-postgresql</artifactId>
</dependency>


Build-Time vs Runtime Initialization: Control initialization with:

quarkus.native.additional-build-args=--initialize-at-build-time=com.example.BuildTimeClass
quarkus.native.additional-build-args=--initialize-at-run-time=com.example.RuntimeClass


Container Image Build: Use Quarkus container-image extensions:

quarkus.native.container-build=true
quarkus.native.builder-image=mandrel

Micronaut
Micronaut has built-in GraalVM support with minimal configuration
Use @ReflectionConfig and @Introspected annotations as needed
Micronaut's ahead-of-time compilation reduces reflection requirements

Common Micronaut Native Image Tips:

Bean Introspection: Use @Introspected for POJOs to avoid reflection:

@Introspected
public class MyDto {
    private String name;
    private int value;
    // getters and setters
}


Or enable package-wide introspection in application.yml:

micronaut:
  introspection:
    packages:
      - com.example.dto


Reflection Configuration: Use declarative annotations:

@ReflectionConfig(
    type = MyClass.class,
    accessType = ReflectionConfig.AccessType.ALL_DECLARED_CONSTRUCTORS
)
public class MyConfiguration {
}


Resource Configuration: Add resources to native image:

@ResourceConfig(
    includes = {"application.yml", "logback.xml"}
)
public class ResourceConfiguration {
}


Native Image Configuration: In build.gradle:

graalvmNative {
    binaries {
        main {
            buildArgs.add("--initialize-at-build-time=io.micronaut")
            buildArgs.add("--initialize-at-run-time=io.netty")
            buildArgs.add("--report-unsupported-elements-at-runtime")
        }
    }
}


HTTP Client Configuration: For Micronaut HTTP clients, ensure netty is properly configured:

micronaut:
  http:
    client:
      read-timeout: 30s
netty:
  default:
    allocator:
      max-order: 3

Best Practices
Start Simple: Build with --no-fallback to catch all native image issues
Use Tracing Agent: Run your application with the GraalVM tracing agent to automatically discover reflection, resources, and JNI requirements
Test Thoroughly: Native images behave differently than JVM applications
Minimize Reflection: Prefer compile-time code generation over runtime reflection
Profile Memory: Native images have different memory characteristics
CI/CD Integration: Add native image builds to your CI/CD pipeline
Keep Dependencies Updated: Use latest versions for better GraalVM compatibility
Troubleshooting Tips
Build Fails with Reflection Errors: Use the tracing agent or add manual reflection configuration
Missing Resources: Ensure resource patterns are correctly specified in resource-config.json
ClassNotFoundException at Runtime: Add the class to reflection configuration
Slow Build Times: Consider using build caching and incremental builds
Large Image Size: Use --gc=serial (default) or --gc=epsilon (no-op GC for testing) and analyze dependencies
References
GraalVM Native Image Documentation
Spring Boot Native Image Guide
Quarkus Building Native Images
Micronaut GraalVM Support
GraalVM Reachability Metadata
Native Build Tools
Weekly Installs
8.3K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass