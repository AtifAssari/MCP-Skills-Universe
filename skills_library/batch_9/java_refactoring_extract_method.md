---
title: java-refactoring-extract-method
url: https://skills.sh/github/awesome-copilot/java-refactoring-extract-method
---

# java-refactoring-extract-method

skills/github/awesome-copilot/java-refactoring-extract-method
java-refactoring-extract-method
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill java-refactoring-extract-method
Summary

Java method extraction refactoring for improved readability and maintainability.

Identifies methods exceeding complexity thresholds (LOC > 15, statements > 10, cyclomatic complexity > 10) and extracts logical code blocks into focused helper methods
Produces fully compilable Java 17 code with descriptive method names and single-line documentation comments
Preserves all original functionality while reducing cognitive load and improving testability through smaller, single-responsibility methods
SKILL.md
Refactoring Java Methods with Extract Method
Role

You are an expert in refactoring Java methods.

Below are 2 examples (with titles code before and code after refactoring) that represents Extract Method.

Code Before Refactoring 1:
public FactLineBuilder setC_BPartner_ID_IfValid(final int bpartnerId) {
	assertNotBuild();
	if (bpartnerId > 0) {
		setC_BPartner_ID(bpartnerId);
	}
	return this;
}

Code After Refactoring 1:
public FactLineBuilder bpartnerIdIfNotNull(final BPartnerId bpartnerId) {
	if (bpartnerId != null) {
		return bpartnerId(bpartnerId);
	} else {
		return this;
	}
}
public FactLineBuilder setC_BPartner_ID_IfValid(final int bpartnerRepoId) {
	return bpartnerIdIfNotNull(BPartnerId.ofRepoIdOrNull(bpartnerRepoId));
}

Code Before Refactoring 2:
public DefaultExpander add(RelationshipType type, Direction direction) {
     Direction existingDirection = directions.get(type.name());
     final RelationshipType[] newTypes;
     if (existingDirection != null) {
          if (existingDirection == direction) {
               return this;
          }
          newTypes = types;
     } else {
          newTypes = new RelationshipType[types.length + 1];
          System.arraycopy(types, 0, newTypes, 0, types.length);
          newTypes[types.length] = type;
     }
     Map<String, Direction> newDirections = new HashMap<String, Direction>(directions);
     newDirections.put(type.name(), direction);
     return new DefaultExpander(newTypes, newDirections);
}

Code After Refactoring 2:
public DefaultExpander add(RelationshipType type, Direction direction) {
     Direction existingDirection = directions.get(type.name());
     final RelationshipType[] newTypes;
     if (existingDirection != null) {
          if (existingDirection == direction) {
               return this;
          }
          newTypes = types;
     } else {
          newTypes = new RelationshipType[types.length + 1];
          System.arraycopy(types, 0, newTypes, 0, types.length);
          newTypes[types.length] = type;
     }
     Map<String, Direction> newDirections = new HashMap<String, Direction>(directions);
     newDirections.put(type.name(), direction);
     return (DefaultExpander) newExpander(newTypes, newDirections);
}
protected RelationshipExpander newExpander(RelationshipType[] types,
          Map<String, Direction> directions) {
     return new DefaultExpander(types, directions);
}

Task

Apply Extract Method to improve readability, testability, maintainability, reusability, modularity, cohesion, low coupling, and consistency.

Always return a complete and compilable method (Java 17).

Perform intermediate steps internally:

First, analyze each method and identify those exceeding thresholds:
LOC (Lines of Code) > 15
NOM (Number of Statements) > 10
CC (Cyclomatic Complexity) > 10
For each qualifying method, identify code blocks that can be extracted into separate methods.
Extract at least one new method with a descriptive name.
Output only the refactored code inside a single java block.
Do not remove any functionality from the original method.
Include a one-line comment above each new method describing its purpose.
Code to be Refactored:

Now, assess all methods with high complexity and refactor them using Extract Method

Weekly Installs
8.6K
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