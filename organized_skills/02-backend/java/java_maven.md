---
rating: ⭐⭐⭐
title: java-maven
url: https://skills.sh/pluginagentmarketplace/custom-plugin-java/java-maven
---

# java-maven

skills/pluginagentmarketplace/custom-plugin-java/java-maven
java-maven
Installation
$ npx skills add https://github.com/pluginagentmarketplace/custom-plugin-java --skill java-maven
Summary

Apache Maven configuration, dependency management, and multi-module project setup for Java builds.

Covers POM structure, lifecycle phases (validate through deploy), and plugin configuration with practical examples
Supports single-module, multi-module, and library project types with BOM-based dependency management
Includes troubleshooting guidance for common issues like dependency conflicts, version mismatches, and build memory problems
Provides Maven commands for dependency analysis, version checking, and effective POM inspection
SKILL.md
Java Maven Skill

Master Apache Maven for Java project builds and dependency management.

Overview

This skill covers Maven configuration including POM structure, lifecycle phases, plugin configuration, dependency management with BOMs, and multi-module projects.

When to Use This Skill

Use when you need to:

Configure Maven POM files
Manage dependencies with BOMs
Set up build plugins
Create multi-module projects
Troubleshoot build issues
Quick Reference
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>my-app</artifactId>
    <version>1.0.0-SNAPSHOT</version>

    <properties>
        <java.version>21</java.version>
        <maven.compiler.source>${java.version}</maven.compiler.source>
        <maven.compiler.target>${java.version}</maven.compiler.target>
    </properties>

    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-dependencies</artifactId>
                <version>3.2.1</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-enforcer-plugin</artifactId>
                <version>3.4.1</version>
            </plugin>
        </plugins>
    </build>
</project>

Lifecycle Phases
validate → compile → test → package → verify → install → deploy

Useful Commands
mvn dependency:tree                    # View dependencies
mvn dependency:analyze                 # Find unused/undeclared
mvn versions:display-dependency-updates  # Check updates
mvn help:effective-pom                 # View effective POM
mvn -B verify                          # Batch mode build

Troubleshooting
Problem	Solution
Dependency not found	Check repository, version
Version conflict	Use BOM or enforcer
Build OOM	Set MAVEN_OPTS=-Xmx1g
Usage
Skill("java-maven")

Weekly Installs
505
Repository
pluginagentmark…gin-java
GitHub Stars
34
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass