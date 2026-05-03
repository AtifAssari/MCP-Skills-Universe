---
title: cortex-classify-notebook
url: https://skills.sh/snowflake-labs/sfguides/cortex-classify-notebook
---

# cortex-classify-notebook

skills/snowflake-labs/sfguides/cortex-classify-notebook
cortex-classify-notebook
Installation
$ npx skills add https://github.com/snowflake-labs/sfguides --skill cortex-classify-notebook
SKILL.md
Cortex Classify Text - Notebook Deployment Skill

You are deploying the Cortex CLASSIFY_TEXT tutorial notebook to the user's Snowflake account. This skill uploads the notebook and provides a direct link to open it in Snowsight.

What This Skill Does
Fetches latest documentation to ensure current syntax
Detects or sets up the target environment (prefers SNOWFLAKE_LEARNING)
Creates a user-specific schema for the notebook
Uploads the tutorial notebook to a Snowflake stage
Creates the notebook in the user's account
Provides a direct link to open the notebook in Snowsight
Deployment Flow

Welcome the user briefly, then proceed through the steps efficiently while keeping them informed. Do NOT ask for confirmation at each step - deploy smoothly and report results.

Step 0: Fetch Latest Documentation (ALWAYS do this first)

Before starting deployment, use web_fetch to retrieve the current official documentation:

https://docs.snowflake.com/en/sql-reference/functions/classify_text-snowflake-cortex
https://docs.snowflake.com/en/user-guide/ui-snowsight/notebooks


This ensures your explanations and any troubleshooting advice are current. If the docs show new parameters or syntax, inform the user.

Step 1: Environment Detection and Setup

Run these two queries in parallel:

-- Query 1: Check if SNOWFLAKE_LEARNING environment exists
SHOW ROLES LIKE 'SNOWFLAKE_LEARNING_ROLE';

-- Query 2: Read the notebook file from assets/classify_unstructured_customer_reviews.ipynb


If SNOWFLAKE_LEARNING_ROLE exists (preferred):

USE ROLE SNOWFLAKE_LEARNING_ROLE;
USE DATABASE SNOWFLAKE_LEARNING_DB;
USE WAREHOUSE SNOWFLAKE_LEARNING_WH;


If NOT available (fallback):

USE ROLE ACCOUNTADMIN;  -- or appropriate role with CREATE DATABASE privilege
CREATE DATABASE IF NOT EXISTS CORTEX_TUTORIALS_DB;
USE DATABASE CORTEX_TUTORIALS_DB;
CREATE WAREHOUSE IF NOT EXISTS CORTEX_TUTORIALS_WH WITH WAREHOUSE_SIZE = 'XSMALL';
USE WAREHOUSE CORTEX_TUTORIALS_WH;

Step 2: Create User Schema and Stage
-- Create a schema for the notebook (named after current user)
SET schema_name = CONCAT(CURRENT_USER(), '_CORTEX_TUTORIALS');
CREATE SCHEMA IF NOT EXISTS IDENTIFIER($schema_name);
USE SCHEMA IDENTIFIER($schema_name);

-- Create internal stage for notebook files
CREATE STAGE IF NOT EXISTS notebook_stage
    DIRECTORY = (ENABLE = TRUE)
    ENCRYPTION = (TYPE = 'SNOWFLAKE_SSE');

Step 3: Capture Environment Info (CRITICAL)

IMPORTANT: After setting up the environment, you MUST query the actual values to use in subsequent steps. Do NOT guess or assume schema names based on the local username.

SELECT 
    CURRENT_USER() as current_user,
    CURRENT_SCHEMA() as current_schema, 
    CURRENT_DATABASE() as current_database,
    CURRENT_ROLE() as current_role


Store these values for use in the upload and notebook creation steps.

Step 4: Upload Notebook File to Stage

Use the snow stage copy CLI command with fully qualified stage path:

snow stage copy <local_notebook_path> @<DATABASE>.<SCHEMA>.notebook_stage --overwrite --connection <connection_name>


Example (substitute actual values from Step 3):

snow stage copy /path/to/assets/classify_unstructured_customer_reviews.ipynb @{DATABASE}.{SCHEMA}.notebook_stage --overwrite --connection {CONNECTION}


IMPORTANT:

Use the ACTUAL schema name from Step 3, NOT a guessed name based on local OS username
The local path is: assets/classify_unstructured_customer_reviews.ipynb relative to this skill's base directory
Always use --overwrite flag to handle re-deployments
Step 5: Create the Notebook

Use fully qualified names for the notebook creation:

CREATE OR REPLACE NOTEBOOK <DATABASE>.<SCHEMA>.CLASSIFY_CUSTOMER_REVIEWS
    FROM '@<DATABASE>.<SCHEMA>.notebook_stage'
    MAIN_FILE = 'classify_unstructured_customer_reviews.ipynb'
    COMMENT = 'Tutorial: Classify customer reviews with Cortex AI';


Example (substitute actual values from Step 3):

CREATE OR REPLACE NOTEBOOK {DATABASE}.{SCHEMA}.CLASSIFY_CUSTOMER_REVIEWS
    FROM '@{DATABASE}.{SCHEMA}.notebook_stage'
    MAIN_FILE = 'classify_unstructured_customer_reviews.ipynb'
    COMMENT = 'Tutorial: Classify customer reviews with Cortex AI';

Step 6: Generate Snowsight URL

Get the account identifier for the URL:

SELECT CURRENT_ORGANIZATION_NAME() || '-' || CURRENT_ACCOUNT_NAME() as account_identifier


Build the Snowsight URL:

https://app.snowflake.com/{ORG}/{ACCOUNT}/#/notebooks/{DATABASE}.{SCHEMA}.CLASSIFY_CUSTOMER_REVIEWS


Where {ORG} and {ACCOUNT} come from splitting the account_identifier on -.

Success Message

After successful deployment, provide this summary:

Notebook Deployed Successfully!

Open your notebook: Click here to open in Snowsight

Location: {DATABASE}.{SCHEMA}.CLASSIFY_CUSTOMER_REVIEWS

What the notebook covers:
Load Sample Data - Customer reviews from Tasty Bytes food trucks
Classify Text with Python - Use cortex.classify_text() on single strings and DataFrames
Classify Text with SQL - Use SNOWFLAKE.CORTEX.CLASSIFY_TEXT() directly in queries
Analyze Results - Determine if customers would recommend food trucks based on reviews
To run the tutorial:
Click the link above to open the notebook in Snowsight
Click Run All to execute all cells
Review the classification results showing "Likely", "Unlikely", or "Unsure" recommendations
Handling Issues
Schema Name Mismatch Errors

If you get "Schema does not exist" errors:

Always query CURRENT_SCHEMA() after setup to get the actual schema name
Do NOT assume the schema name matches the local OS username
Use the queried values in all subsequent commands
Stage Copy Failures

If snow stage copy fails:

Verify the stage path uses fully qualified names: @DATABASE.SCHEMA.stage_name
Ensure the connection parameter matches the user's active connection
Check that the role has WRITE privileges on the stage
Notebook Already Exists

The skill uses CREATE OR REPLACE NOTEBOOK by default, which handles existing notebooks automatically.

Insufficient Privileges

If user can't create notebooks:

Check if they have CREATE NOTEBOOK privilege on the schema
Suggest using SNOWFLAKE_LEARNING_ROLE if available
Fall back to ACCOUNTADMIN if necessary
Cortex Not Available

If Cortex functions aren't available in the region:

Check Cortex region availability
Verify account has Cortex enabled
Reference Materials
assets/classify_unstructured_customer_reviews.ipynb - The notebook file to deploy
Notebook teaches classification of customer reviews into "Likely", "Unlikely", "Unsure" categories
Weekly Installs
14
Repository
snowflake-labs/sfguides
GitHub Stars
5
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass