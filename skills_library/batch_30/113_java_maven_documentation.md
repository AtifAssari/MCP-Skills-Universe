---
title: 113-java-maven-documentation
url: https://skills.sh/jabrena/cursor-rules-java/113-java-maven-documentation
---

# 113-java-maven-documentation

skills/jabrena/cursor-rules-java/113-java-maven-documentation
113-java-maven-documentation
Installation
$ npx skills add https://github.com/jabrena/cursor-rules-java --skill 113-java-maven-documentation
SKILL.md
Create DEVELOPER.md for the Maven projects

Generate a DEVELOPER.md file that combines a fixed base template with dynamic sections derived from analysing the project pom.xml.

What is covered in this Skill?

Base template reproduction (verbatim)
Plugin goals reference: table of ./mvnw goals per explicitly declared plugin, max 8 goals each
Maven Profiles table: profile ID, activation trigger, representative command, description
Submodules table (multi-module projects only)
Constraints

Before generating any content, read every pom.xml in the workspace. Only include plugins explicitly declared in the project POMs — never plugins inherited from parent POMs or the Maven super-POM unless redeclared.

MANDATORY: Read every pom.xml in the workspace (root and submodules) before generating any content
PLUGIN SCOPE: Only include plugins explicitly declared in <build><plugins> or <build><pluginManagement><plugins> — never plugins inherited from parent POMs or the Maven super-POM unless redeclared
SCOPE: Execute steps 1–5 in order. Omit Profiles section if no profiles; omit Submodules section if not multi-module
BEFORE APPLYING: Read the reference for the base template content, plugin catalog, and detailed constraints for each step
When to use this skill
Create DEVELOPER.md
Generate DEVELOPER.md
Maven project documentation
Add Maven documentation
Plugin goals reference
Maven Profiles table
Submodules table
Workflow
Read all POM files in workspace

Read root and every submodule pom.xml before generating content.

Read documentation reference assets

Read references/113-java-maven-documentation.md to use the base template and plugin catalog constraints exactly.

Assemble DEVELOPER.md base and dynamic sections

Generate DEVELOPER.md with verbatim base template plus dynamic sections: plugin goals, profiles (if any), and submodules (if multi-module).

Enforce plugin scope and section omission rules

Include only explicitly declared plugins and omit Profiles/Submodules sections when not applicable.

Reference

For detailed guidance, examples, and constraints, see references/113-java-maven-documentation.md.

Weekly Installs
78
Repository
jabrena/cursor-…les-java
GitHub Stars
368
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass