---
title: trigger-refactor-pipeline
url: https://skills.sh/forcedotcom/afv-library/trigger-refactor-pipeline
---

# trigger-refactor-pipeline

skills/forcedotcom/afv-library/trigger-refactor-pipeline
trigger-refactor-pipeline
Installation
$ npx skills add https://github.com/forcedotcom/afv-library --skill trigger-refactor-pipeline
SKILL.md
When to Use This Skill

Use this skill when you need to:

Modernize legacy triggers with DML/SOQL operations inside loops
Refactor triggers that lack clear separation of concerns
Implement bulk-safe patterns in existing trigger code
Generate comprehensive test coverage for refactored triggers
Prerequisites

Before starting, ensure you have:

Salesforce CLI installed and authenticated to your target org
Python 3.9 or higher installed
The baseline trigger deployed (see Setup section)
Setup

Deploy the baseline anti-pattern trigger to analyze and refactor:

// ❌ Anti-pattern: all logic stuffed into the trigger, with DML/SOQL in loops.
trigger OpportunityTrigger on Opportunity (before insert, before update, after update) {
    // BEFORE INSERT: validate Closed Won w/ low Amount
    if (Trigger.isBefore && Trigger.isInsert) {
        for (Opportunity o : Trigger.new) {
            if (o.StageName == 'Closed Won' && (o.Amount == null || o.Amount < 1000)) {
                o.addError('Closed Won opportunities must have Amount ≥ 1000.');
            }
        }
    }

    // BEFORE UPDATE: if Stage changed, overwrite Description
    if (Trigger.isBefore && Trigger.isUpdate) {
        for (Opportunity o : Trigger.new) {
            Opportunity oldO = Trigger.oldMap.get(o.Id);
            if (o.StageName != oldO.StageName) {
                o.Description = 'Stage changed from ' + oldO.StageName + ' to ' + o.StageName;
            }
        }
    }

    // AFTER UPDATE: when Stage becomes Closed Won, create a follow-up Task
    if (Trigger.isAfter && Trigger.isUpdate) {
        for (Opportunity o : Trigger.new) {
            Opportunity oldO = Trigger.oldMap.get(o.Id);
            if (o.StageName == 'Closed Won' && oldO.StageName != 'Closed Won') {
                Task t = new Task(
                    WhatId     = o.Id,
                    OwnerId    = o.OwnerId,
                    Subject    = 'Send thank-you',
                    Status     = 'Not Started',
                    Priority   = 'Normal',
                    ActivityDate = Date.today()
                );
                insert t; // ❌ DML in a loop
            }
        }
    }
}


Deploy this to your org:

sf project deploy start --source-dir force-app/main/default/triggers

Step 1: Analyze the Trigger

Run the analysis script to identify anti-patterns and generate a report:

python scripts/analyze_trigger.py OpportunityTrigger


The script will output:

DML in loops - Line numbers where DML operations occur inside iteration
SOQL in loops - Line numbers where SOQL queries occur inside iteration
Missing bulkification - Areas where collection-based processing is needed
Complexity score - Overall trigger complexity rating (1-10)
Recommended approach - Suggested handler pattern based on trigger contexts

Review the analysis report before proceeding to refactoring.

Step 2: Review Handler Patterns

Consult the handler patterns reference to understand:

Single-responsibility handlers - One handler class per trigger context
Unified handler approach - Single handler with context methods
Bulk collection strategies - How to aggregate DML/SOQL outside loops
Best practices - Error handling, test boundaries, deployment order

Choose the pattern that best fits your trigger's complexity and team conventions.

Step 3: Refactor the Trigger

Create the handler class using the appropriate pattern from the reference guide:

Extract logic into handler methods with descriptive names
Implement bulk-safe collections for DML operations
Add proper error handling using try-catch or Database methods
Update the trigger to delegate only, passing Trigger context variables
Preserve behavior - ensure the refactored code produces identical results

The trigger should be reduced to simple delegation:

trigger OpportunityTrigger on Opportunity (before insert, before update, after update) {
    OpportunityTriggerHandler handler = new OpportunityTriggerHandler();
    
    if (Trigger.isBefore && Trigger.isInsert) {
        handler.beforeInsert(Trigger.new);
    }
    
    if (Trigger.isBefore && Trigger.isUpdate) {
        handler.beforeUpdate(Trigger.new, Trigger.oldMap);
    }
    
    if (Trigger.isAfter && Trigger.isUpdate) {
        handler.afterUpdate(Trigger.new, Trigger.oldMap);
    }
}

Step 4: Generate Tests

Use the test template from assets/test_template.apex to scaffold your test class:

Copy the template and rename for your handler
Implement setup methods to create test data
Write unit tests covering each handler method:
Positive cases with valid data
Negative cases with invalid data
Boundary conditions
Add bulk tests with 200+ records to verify bulkification
Test mixed scenarios where only some records qualify for logic

Required test coverage:

Each handler method must have at least 2 test methods (positive + negative)
At least one bulk test with 200+ records
Overall code coverage must be 100%
Step 5: Deploy and Validate

Deploy the refactored trigger, handler, and tests:

# Deploy all components
sf project deploy start --source-dir force-app/main/default

# Run tests
sf apex test run --class-names OpportunityTriggerHandlerTest --result-format human --code-coverage

# Verify no regressions
sf apex test run --test-level RunLocalTests --result-format human


Validation checklist:

 All new tests pass with 100% coverage
 No new governor limit warnings in debug logs
 Existing functionality remains unchanged
 Deployment to production planned with rollback strategy
Troubleshooting

Issue: Tests fail with "System.LimitException: Too many DML statements"

Solution: Ensure handler methods collect DML operations and execute outside loops

Issue: Code coverage below 100%

Solution: Add negative test cases and verify all conditional branches are tested

Issue: Behavior differs from original trigger

Solution: Review Trigger context variables (new, old, oldMap) are passed correctly to handler
Next Steps

After successful refactoring:

Document the new handler pattern in your team's wiki
Update code review checklist to enforce handler patterns for new triggers
Identify other legacy triggers for refactoring using this skill
Consider implementing a trigger framework if managing many triggers
Weekly Installs
451
Repository
forcedotcom/afv-library
GitHub Stars
242
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass