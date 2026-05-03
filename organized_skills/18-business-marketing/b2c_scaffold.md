---
rating: ⭐⭐⭐
title: b2c-scaffold
url: https://skills.sh/salesforcecommercecloud/b2c-developer-tooling/b2c-scaffold
---

# b2c-scaffold

skills/salesforcecommercecloud/b2c-developer-tooling/b2c-scaffold
b2c-scaffold
Installation
$ npx skills add https://github.com/salesforcecommercecloud/b2c-developer-tooling --skill b2c-scaffold
SKILL.md
B2C Scaffold Skill

Use the b2c scaffold commands to generate B2C Commerce components from templates.

Tip: If b2c is not installed globally, use npx @salesforce/b2c-cli instead.

Examples
List Available Scaffolds
# list all scaffolds
b2c scaffold list

# list only cartridge scaffolds
b2c scaffold list --category cartridge

# show extended info (description, tags)
b2c scaffold list -x

Generate a Cartridge
# generate interactively
b2c scaffold cartridge

# generate with name
b2c scaffold cartridge --name app_custom

# generate to specific directory
b2c scaffold cartridge --name app_custom --output ./src/cartridges

# skip prompts, use defaults
b2c scaffold cartridge --name app_custom --force

# preview without creating files
b2c scaffold cartridge --name app_custom --dry-run

Generate a Controller
# generate interactively (prompts for cartridge selection)
b2c scaffold controller

# generate with all options
b2c scaffold controller \
  --option controllerName=Account \
  --option cartridgeName=app_custom \
  --option routes=Show,Submit

Generate a Hook
# generate a system hook
b2c scaffold hook \
  --option hookName=validateBasket \
  --option hookType=system \
  --option hookPoint=dw.order.calculate \
  --option cartridgeName=app_custom

# generate an OCAPI hook
b2c scaffold hook \
  --option hookName=modifyBasket \
  --option hookType=ocapi \
  --option hookPoint=dw.ocapi.shop.basket.beforePOST \
  --option cartridgeName=app_custom

Generate a Custom API
# generate a shopper API
b2c scaffold custom-api \
  --option apiName=loyalty-points \
  --option apiType=shopper \
  --option cartridgeName=app_custom

# generate an admin API
b2c scaffold custom-api \
  --option apiName=inventory-sync \
  --option apiType=admin \
  --option cartridgeName=app_custom

Generate a Job Step
# generate a task-based job step
b2c scaffold job-step \
  --option stepId=custom.CleanupOrders \
  --option stepType=task \
  --option cartridgeName=app_custom

# generate a chunk-based job step
b2c scaffold job-step \
  --option stepId=custom.ImportProducts \
  --option stepType=chunk \
  --option cartridgeName=app_custom

Generate a Page Designer Component
b2c scaffold page-designer-component \
  --option componentId=heroCarousel \
  --option componentName="Hero Carousel" \
  --option componentGroup=content \
  --option cartridgeName=app_custom

Get Scaffold Info
# see parameters and usage for a scaffold
b2c scaffold info cartridge
b2c scaffold info controller

Search Scaffolds
# search by keyword
b2c scaffold search api

# search within a category
b2c scaffold search template --category page-designer

Create Custom Scaffolds
# create a project-local scaffold
b2c scaffold init my-component --project

# create a user scaffold
b2c scaffold init my-component --user

# validate a custom scaffold
b2c scaffold validate ./.b2c/scaffolds/my-component

Built-in Scaffolds
Scaffold	Category	Description
cartridge	cartridge	B2C cartridge with standard structure
controller	cartridge	SFRA controller with routes and middleware
hook	cartridge	Hook with hooks.json registration
custom-api	custom-api	Custom SCAPI with OAS 3.0 schema
job-step	job	Job step with steptypes.json registration
page-designer-component	page-designer	Page Designer component
Related Skills
b2c-cli:b2c-code - Deploy generated cartridges to B2C instances
b2c:b2c-controllers - SFRA controller patterns and best practices
b2c:b2c-hooks - B2C hook extension points
b2c:b2c-custom-api-development - Custom API development guide
b2c:b2c-custom-job-steps - Job step implementation patterns
b2c:b2c-page-designer - Page Designer component development
Weekly Installs
73
Repository
salesforcecomme…-tooling
GitHub Stars
39
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass