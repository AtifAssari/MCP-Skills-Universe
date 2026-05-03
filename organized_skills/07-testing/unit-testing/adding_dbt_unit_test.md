---
rating: ⭐⭐⭐
title: adding-dbt-unit-test
url: https://skills.sh/dbt-labs/dbt-agent-skills/adding-dbt-unit-test
---

# adding-dbt-unit-test

skills/dbt-labs/dbt-agent-skills/adding-dbt-unit-test
adding-dbt-unit-test
Installation
$ npx skills add https://github.com/dbt-labs/dbt-agent-skills --skill adding-dbt-unit-test
SKILL.md
Add unit test for a dbt model
Additional Resources
Spec Reference - All required and optional YAML keys for unit tests
Examples - Unit test examples across formats (dict, csv, sql)
Incremental Models - Unit testing incremental models
Ephemeral Dependencies - Unit testing models depending on ephemeral models
Special Case Overrides - Introspective macros, project variables, environment variables
Versioned Models - Unit testing versioned SQL models
BigQuery Caveats - BigQuery-specific caveats
BigQuery Data Types - BigQuery data type handling
Postgres Data Types - Postgres data type handling
Redshift Caveats - Redshift-specific caveats
Redshift Data Types - Redshift data type handling
Snowflake Data Types - Snowflake data type handling
Spark Data Types - Spark data type handling
What are unit tests in dbt

dbt unit tests validate SQL modeling logic on static inputs before materializing in production. If any unit test for a model fails, dbt will not materialize that model.

When to use

You should unit test a model:

Adding Model-Input-Output scenarios for the intended functionality of the model as well as edge cases to prevent regressions if the model logic is changed at a later date.
Verifying that a bug fix solves a bug report for an existing dbt model.

More examples:

When your SQL contains complex logic:
Regex
Date math
Window functions
case when statements when there are many whens
Truncation
Complex joins (multiple joins, self-joins, or joins with non-trivial conditions)
When you're writing custom logic to process input data, similar to creating a function.
Logic for which you had bugs reported before.
Edge cases not yet seen in your actual data that you want to be confident you are handling properly.
Prior to refactoring the transformation logic (especially if the refactor is significant).
Models with high "criticality" (public, contracted models or models directly upstream of an exposure).
When not to use

Cases we don't recommend creating unit tests for:

Built-in functions that are tested extensively by the warehouse provider. If an unexpected issue arises, it's more likely a result of issues in the underlying data rather than the function itself. Therefore, fixture data in the unit test won't provide valuable information.
common SQL spec functions like min(), etc.
General format

dbt unit test uses a trio of the model, given inputs, and expected outputs (Model-Inputs-Outputs):

model - when building this model
given inputs - given a set of source, seeds, and models as preconditions
expect output - then expect this row content of the model as a postcondition
Workflow
1. Choose the model to test

Self explanatory -- the title says it all!

2. Mock the inputs
Create an input for each of the nodes the model depends on.
Specify the mock data it should use.
Specify the format if different than the default (YAML dict).
See the "Data formats for unit tests" section below to determine which format to use.
The mock data only needs include the subset of columns used within this test case.

Tip: Use dbt show to explore existing data from upstream models or sources. This helps you understand realistic input structures. However, always sanitize the sample data to remove any sensitive or PII information before using it in your unit test fixtures.

# Preview upstream model data
dbt show --select upstream_model --limit 5

3. Mock the output
Specify the data that you expect the model to create given those inputs.
Specify the format if different than the default (YAML dict).
See the "Data formats for unit tests" section below to determine which format to use.
The mock data only needs include the subset of columns used within this test case.
4. Ensure upstream models exist before running

Unit tests require direct parent models to exist in the warehouse. Before running unit tests standalone (dbt test), verify that upstream models already exist first:

# Check if upstream models exist in the warehouse
dbt list --select +my_model --exclude my_model --resource-type model
# Then verify the tables/views actually exist in the warehouse via dbt show or your SQL client
dbt show --select upstream_model --limit 1


If upstream models do not exist, or exist but have been modified and not yet refreshed, build them using --empty to create schema-only versions:

# Build upstream models cheaply (schema only, no data read)
dbt run --select +my_model --exclude my_model --empty


Warning: --empty overwrites existing models with schema-only (zero-row) versions. Only use it when models don't exist yet, or when schema changes need to be applied. Do not use it if upstream models contain data you want to preserve — it will wipe that data.

Skip this step if using dbt build --select my_model (recommended) — it handles the full pipeline including unit tests.

Minimal unit test

Suppose you have this model:

-- models/hello_world.sql

select 'world' as hello


Minimal unit test for that model:

# models/_properties.yml

unit_tests:
  - name: test_hello_world

    # Always only one transformation to test
    model: hello_world

    # No inputs needed this time!
    # Most unit tests will have inputs -- see the "real world example" section below
    given: []

    # Expected output can have zero to many rows
    expect:
      rows:
        - {hello: world}

Executing unit tests

Run the unit tests, build the model, and run the data tests for the hello_world model:

dbt build --select hello_world


This saves on warehouse spend as the model will only be materialized and move on to the data tests if the unit tests pass successfully.

Or only run the unit tests without building the model or running the data tests:

dbt test --select "hello_world,test_type:unit"


Or choose a specific unit test by name:

dbt test --select test_is_valid_email_address

Excluding unit tests from production builds

dbt Labs strongly recommends only running unit tests in development or CI environments. Since the inputs of the unit tests are static, there's no need to use additional compute cycles running them in production. Use them when doing development for a test-driven approach and CI to ensure changes don't break them.

Use the --resource-type flag --exclude-resource-type or the DBT_EXCLUDE_RESOURCE_TYPES environment variable to exclude unit tests from your production builds and save compute.

More realistic example
unit_tests:

  - name: test_order_items_count_drink_items_with_zero_drinks
    description: >
      Scenario: Order without any drinks
        When the `order_items_summary` table is built
        Given an order with nothing but 1 food item
        Then the count of drink items is 0

    # Model
    model: order_items_summary

    # Inputs
    given:
      - input: ref('order_items')
        rows:
          - {
              order_id: 76,
              order_item_id: 3,
              is_drink_item: false,
            }
      - input: ref('stg_orders')
        rows:
          - { order_id: 76 }

    # Output
    expect:
      rows:
        - {
            order_id: 76,
            count_drink_items: 0,
          }


For more examples of unit tests, see references/examples.md

Supported and unsupported scenarios
dbt only supports unit testing SQL models.
Unit testing Python models is not supported.
Unit testing non-model nodes like snapshots, seeds, sources, analyses, etc. is not supported.
dbt only supports adding unit tests to models in your current project.
Unit testing cross-project models or models imported from a package is not supported.
dbt does not support unit testing models that use the materialized view materialization.
dbt does not support unit testing models that use recursive SQL.
dbt does not support unit testing models that use introspective queries.
dbt does not support an expect output for final state of the database table after inserting/merging for incremental models.
dbt does support an expect output for what will be merged/inserted for incremental models.
Handy to know
Unit tests must be defined in a YAML file in your model-paths directory (models/ by default)
Fixture files for unit tests must be defined in a SQL or CSV file in your test-paths directory (tests/fixtures by default)
Include all ref or source model references in the unit test configuration as inputs to avoid "node not found" errors during compilation.
If your model has multiple versions, by default the unit test will run on all versions of your model.
If you want to unit test a model that depends on an ephemeral model, you must use format: sql for the ephemeral model input.
Table names within the model must be aliased in order to unit test join logic
YAML for specifying unit tests
For all the required and optional keys in the YAML definition of unit tests, see references/spec.md
Inputs for unit tests

Use inputs in your unit tests to reference a specific model or source for the test:

For input:, use a string that represents a ref or source call:
ref('my_model') or ref('my_model', v='2') or ref('dougs_project', 'users')
source('source_schema', 'source_name')
For seed inputs:
If you do not supply an input for a seed, we will use the seed's CSV file as the input.
If you do supply an input for a seed, we will use that input instead.
Use “empty” inputs by setting rows to an empty list rows: []
This is useful if the model has a ref or source dependency, but its values are irrelevant to this particular unit test. Just beware if the model has a join on that input that would cause rows to drop out!

models/schema.yml

unit_tests:
  - name: test_is_valid_email_address  # this is the unique name of the test
    model: dim_customers  # name of the model I'm unit testing
    given:  # the mock data for your inputs
      - input: ref('stg_customers')
        rows:
         - {email: cool@example.com,     email_top_level_domain: example.com}
         - {email: cool@unknown.com,     email_top_level_domain: unknown.com}
         - {email: badgmail.com,         email_top_level_domain: gmail.com}
         - {email: missingdot@gmailcom,  email_top_level_domain: gmail.com}
      - input: ref('top_level_email_domains')
        rows:
         - {tld: example.com}
         - {tld: gmail.com}
      - input: ref('irrelevant_dependency')  # dependency that we need to acknowlege, but does not need any data
        rows: []
...


Data formats for unit tests
dict is the default format — always start here

Unless you have a specific reason to use another format, use dict (inline YAML). It is the default when format: is omitted.

given:
  - input: ref('orders')
    # no format: key needed — dict is the default
    rows:
      - {order_id: 1, status: completed, amount: 100}
      - {order_id: 2, status: pending, amount: 50}

How to choose the format
Use dict (default)	Use sql	Use csv
Everything else — this is the starting point	Model depends on an ephemeral model	Using an external fixture file
	Column data type not supported by dict/csv	Column data type not supported by dict
	External fixture file with unsupported types	

Critical sql note: sql format requires specifying ALL columns in the mock data. dict and csv only require the columns relevant to the test — much more concise.

Critical sql requirement: If any of your model's ref() or source() inputs are ephemeral models, you must use sql format for those inputs. dict and csv will fail.

dbt supports three formats for mock data within unit tests:

dict (default): Inline YAML dictionary values.
csv: Inline CSV values or a CSV file.
sql: Inline SQL query or a SQL file.

To see examples of each of the formats, see references/examples.md

Notes:

For the sql format you must supply mock data for all columns whereas dict and csv may supply only a subset.
Only the sql format allows you to unit test a model that depends on an ephemeral model -- dict and csv can't be used in that case.
There are no formats that support Jinja.
Fixture files

The dict format only supports inline YAML mock data, but you can also use csv or sql either inline or in a separate fixture file. Store your fixture files in a fixtures subdirectory in any of your test-paths. For example, tests/fixtures/my_unit_test_fixture.sql.

When using the dict or csv format, you only have to define the mock data for the columns relevant to you. This enables you to write succinct and specific unit tests. For the sql format all columns need to be defined.

Special cases
Unit testing incremental models. See references/special-cases-incremental-model.md.
Unit testing a model that depends on ephemeral model(s). See references/special-cases-ephemeral-dependency.md.
Unit test a model that depends on any introspective macros, project variables, or environment variables. See references/special-cases-special-case-overrides.md.
Unit testing versioned SQL models. See references/special-cases-versioned-model.md.
Platform/adapter-specific caveats

There are platform-specific details required if implementing on (Redshift, BigQuery, etc). Read the caveats file for your database (if it exists):

references/warehouse-bigquery-caveats.md
references/warehouse-redshift-caveats.md
Platform/adapter-specific data types

Unit tests are designed to test for the expected values, not for the data types themselves. dbt takes the value you provide and attempts to cast it to the data type as inferred from the input and output models.

How you specify input and expected values in your unit test YAML definitions are largely consistent across data warehouses, with some variation for more complex data types.

Read the data types file for your database:

references/warehouse-bigquery-data-types.md
references/warehouse-postgres-data-types.md
references/warehouse-redshift-data-types.md
references/warehouse-snowflake-data-types.md
references/warehouse-spark-data-types.md
Disabling a unit test

By default, all specified unit tests are enabled and will be included according to the --select flag.

To disable a unit test from being executed, set:

    config: 
      enabled: false


This is helpful if a unit test is incorrectly failing and it needs to be disabled until it is fixed.

When a unit test fails

When a unit test fails, there will be a log message of "actual differs from expected", and it will show a "data diff" between the two:

actual differs from expected:

@@ ,email           ,is_valid_email_address
→  ,cool@example.com,True→False
   ,cool@unknown.com,False


There are two main possibilities when a unit test fails:

There was an error in the way the unit test was constructed (false positive)
There is an bug is the model (true positive)

It takes expert judgement to determine one from the other.

The --empty flag

The direct parents of the model that you’re unit testing need to exist in the warehouse before you can execute the unit test. The run and build commands supports the --empty flag for building schema-only dry runs. The --empty flag limits the refs and sources to zero rows. dbt will still execute the model SQL against the target data warehouse but will avoid expensive reads of input data. This validates dependencies and ensures your models will build properly.

Use the --empty flag to build an empty version of the models to save warehouse spend.


dbt run --select "stg_customers top_level_email_domains" --empty


Common Mistakes
Mistake	Fix
Testing simple SQL using built-in functions	Only unit test complex logic: regex, date math, window functions, multi-condition case statements
Mocking all columns in input data	Only include columns relevant to the test case
Using sql format when dict works	Prefer dict (most readable), fall back to csv or sql only when needed
Missing input for a ref or source	Include all model dependencies to avoid "node not found" errors
Testing Python models or snapshots	Unit tests only support SQL models
Weekly Installs
265
Repository
dbt-labs/dbt-ag…t-skills
GitHub Stars
450
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass