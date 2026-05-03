---
rating: ⭐⭐
title: google-cloud-recipe-onboarding
url: https://skills.sh/google/skills/google-cloud-recipe-onboarding
---

# google-cloud-recipe-onboarding

skills/google/skills/google-cloud-recipe-onboarding
google-cloud-recipe-onboarding
Installation
$ npx skills add https://github.com/google/skills --skill google-cloud-recipe-onboarding
SKILL.md
Onboarding to Google Cloud

This skill provides a streamlined "happy path" for a singleton developer to get started with Google Cloud. It covers everything from initial account setup to deploying your first cloud resource.

Overview

For an individual developer, onboarding to Google Cloud involves establishing a personal identity, setting up a billing method, and creating a workspace (Project) where resources can be managed. Google Cloud offers a Free Tier and Free Trial for multiple products. Learn more here.

Clarifying Questions

Before proceeding, the agent should clarify the user's current status:

Do you already have a Google Account (Gmail or Google Workspace)?
Are you looking to set up a personal account for learning/experimentation, or are you part of an organization with existing infrastructure?
Are you an IT admin within a larger enterprise, setting up Google Cloud for your organization?
What is the first type of resource or application you are interested in building (e.g., a website, a data pipeline, a virtual machine)?
Do you prefer to use the command line (CLI), an IDE (e.g. VSCode, Antigravity), or do you prefer using the web-based Google Cloud console?
Prerequisites
A Google Account (e.g., @gmail.com).
A valid payment method (credit card or bank account) for billing verification (even for the free trial).
Steps
1. Sign Up and Activate Free Credit
Go to the Google Cloud Console.
Sign in with your Google Account. This will "Activate" your $300 free credit.
2. Create Your First Google Cloud Project

Google Cloud resources are organized into Projects.

In the Google Cloud console, click the project picker dropdown at the top of the page.
Click New Project.
Enter a Project Name (e.g., my-first-gcp-project).
Note the generated Project ID; you will use this for CLI and API interactions.
Click Create.
3. Set Up Billing

Ensure your project is linked to your Free Trial Cloud Billing account.

Go to the Billing section in the console.
Confirm that your new project is listed under "Projects linked to this billing account."
4. Install and Initialize the Google Cloud CLI

The Google Cloud CLI (gcloud CLI) is the primary tool for interacting with Google Cloud from your local machine.

Download and install the Google Cloud CLI.
Open your terminal and run: gcloud init
Follow the prompts to log in and select your project.
5. Enable Necessary APIs

Most services require their specific API to be enabled before use. For example, to use Cloud Run, run: gcloud services enable run.googleapis.com

Note that some Google Cloud APIs, including Cloud Logging, are enabled by default.

6. Deploy Your First Resource

Choose a simple entry point based on your needs: - Cloud Run (Recommended for Apps): Deploy a containerized "Hello World" app. - Compute Engine: Create a small Linux VM (e.g., e2-micro which is part of the Always Free tier in certain regions). - Cloud Storage: Create a bucket to store files.

Example (Cloud Run):

    gcloud run deploy hello-world \
    --image=gcr.io/cloudrun/hello \ --platform=managed \ --region=us-central1 \
    --allow-unauthenticated


This command will output a public URL, that you can reach in a web browser. Congrats - you just deployed your first Google Cloud resource!

7. Next Steps
Explore the Google Cloud Free Program to see what else you can do with your free credit.
Read the Google Cloud Overview
See the full list of 150+ Google Cloud products
Explore the Enterprise Setup Guide for information on setting up Google Cloud for a team or organization.
Compare AWS and Azure products to Google Cloud
Validation Logic

Use this logic to determine if the user has successfully completed the Google Cloud onboarding process:

Project Created: Does the user have a Project ID?
Billing Linked: Is the project associated with a billing account (check via gcloud beta billing projects describe PROJECT_ID)?
CLI Authenticated: Does gcloud config list show the correct account and project?
Resource Verified: Can the user access the URL or IP of the deployed resource?
Weekly Installs
1.5K
Repository
google/skills
GitHub Stars
6.3K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass