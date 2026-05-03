---
title: swiftdata-pro
url: https://skills.sh/twostraws/swiftdata-agent-skill/swiftdata-pro
---

# swiftdata-pro

skills/twostraws/swiftdata-agent-skill/swiftdata-pro
swiftdata-pro
Installation
$ npx skills add https://github.com/twostraws/swiftdata-agent-skill --skill swiftdata-pro
Summary

Write, review, and improve SwiftData code using modern APIs and best practices.

Validates code against core SwiftData rules including relationships, delete rules, autosaving, and FetchDescriptor patterns
Checks predicates for safety and runtime crashes, with special handling for CloudKit constraints and unsupported operations
Targets Swift 6.2+ with modern concurrency; recommends indexing strategies for iOS 18+ and class inheritance patterns for iOS 26+
Reports only genuine issues without nitpicking; organizes findings by file with before/after code examples and prioritized impact summary
SKILL.md

Write and review SwiftData code for correctness, modern API usage, and adherence to project conventions. Report only genuine problems - do not nitpick or invent issues.

Review process:

Check for core SwiftData issues using references/core-rules.md.
Check that predicates are safe and supported using references/predicates.md.
If the project uses CloudKit, check for CloudKit-specific constraints using references/cloudkit.md.
If the project targets iOS 18+, check for indexing opportunities using references/indexing.md.
If the project targets iOS 26+, check for class inheritance patterns using references/class-inheritance.md.

If doing partial work, load only the relevant reference files.

Core Instructions
Target Swift 6.2 or later, using modern Swift concurrency.
The user strongly prefers to use SwiftData across the board. Do not suggest Core Data functionality unless it is a feature that cannot be solved with SwiftData.
Do not introduce third-party frameworks without asking first.
Use a consistent project structure, with folder layout determined by app features.
Output Format

If the user asks for a review, organize findings by file. For each issue:

State the file and relevant line(s).
Name the rule being violated.
Show a brief before/after code fix.

Skip files with no issues. End with a prioritized summary of the most impactful changes to make first.

If the user asks you to write or improve code, follow the same rules above but make the changes directly instead of returning a findings report.

Example output:

Destination.swift

Line 8: Add an explicit delete rule for relationships.

// Before
var sights: [Sight]

// After
@Relationship(deleteRule: .cascade, inverse: \Sight.destination) var sights: [Sight]


Line 22: Do not use isEmpty == false in predicates – it crashes at runtime. Use ! instead.

// Before
#Predicate<Destination> { $0.sights.isEmpty == false }

// After
#Predicate<Destination> { !$0.sights.isEmpty }

DestinationListView.swift

Line 5: @Query must only be used inside SwiftUI views.

// Before
class DestinationStore {
    @Query var destinations: [Destination]
}

// After
class DestinationStore {
    var modelContext: ModelContext

    func fetchDestinations() throws -> [Destination] {
        try modelContext.fetch(FetchDescriptor<Destination>())
    }
}

Summary
Data loss (high): Missing delete rule on line 8 of Destination.swift means sights will be orphaned when a destination is deleted.
Crash (high): isEmpty == false on line 22 will crash at runtime – use !isEmpty instead.
Incorrect behavior (high): @Query on line 5 of DestinationListView.swift only works inside SwiftUI views.

End of example.

References
references/core-rules.md - autosaving, relationships, delete rules, property restrictions, and FetchDescriptor optimization.
references/predicates.md - supported predicate operations, dangerous patterns that crash at runtime, and unsupported methods.
references/cloudkit.md - CloudKit-specific constraints including uniqueness, optionality, and eventual consistency.
references/indexing.md - database indexing for iOS 18+, including single and compound property indexes.
references/class-inheritance.md - model subclassing for iOS 26+, including @available requirements, schema setup, and predicate filtering.
Weekly Installs
3.3K
Repository
twostraws/swift…nt-skill
GitHub Stars
296
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass