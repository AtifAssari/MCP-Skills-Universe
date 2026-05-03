---
rating: ⭐⭐
title: sap-commerce
url: https://skills.sh/emenowicz/sap-commerce-skill/sap-commerce
---

# sap-commerce

skills/emenowicz/sap-commerce-skill/sap-commerce
sap-commerce
Installation
$ npx skills add https://github.com/emenowicz/sap-commerce-skill --skill sap-commerce
SKILL.md
SAP Commerce Development
Overview

SAP Commerce Cloud (formerly Hybris) is an enterprise e-commerce platform built on Java and Spring. This skill provides guidance for extension development, type system modeling, service layer implementation, data management, API customization, and accelerator patterns for both Cloud (CCv2) and On-Premise deployments.

Core Architecture
Type System

Data modeling via items.xml defines item types, attributes, relations, and enumerations. Types are compiled into Java classes during build. See type-system.md for syntax and patterns.

Extensions

Modular architecture where functionality lives in extensions. Each extension has extensioninfo.xml for metadata, items.xml for types, and *-spring.xml for beans. See extension-development.md.

Service Layer

Four-layer architecture: Facade (API for controllers) → Service (business logic) → DAO (data access) → Model (generated from types). See service-layer-architecture.md.

Data Management

ImpEx: Scripting language for data import/export. See impex-guide.md. FlexibleSearch: SQL-like query language for items. See flexiblesearch-reference.md.

OCC API

RESTful web services exposing commerce functionality. Controllers use DataMapper for DTO conversion. See occ-api-development.md.

Accelerators

Pre-built storefronts: B2C (retail) and B2B (enterprise with approval workflows). See accelerator-customization.md.

CronJobs & Task Engine

Scheduled and asynchronous job execution. Define AbstractJobPerformable implementations, configure via ServicelayerJob + CronJob + Trigger in ImpEx. See cronjob-task-engine.md.

Business Processes

Stateful workflows for order processing, returns, approvals, and custom flows. XML process definitions with action beans (AbstractSimpleDecisionAction, AbstractAction), wait states, and event triggers. See business-process.md.

Solr Search

Product search and faceted navigation powered by Apache Solr. Configure indexed types, properties, value providers, and boost rules. See solr-search-configuration.md.

Promotions & Rule Engine

Drools-based promotion rules with conditions and actions. Supports order/product/customer promotions, coupons, and custom actions. See promotions-rule-engine.md.

Caching

Multi-layered caching: platform region caches (entity, query, typesystem), Spring @Cacheable, and cluster-aware invalidation. See caching-guide.md.

Backoffice

Administration UI customization via cockpitng: widget configuration, custom editors, search/list views, wizards, and deep links. See backoffice-configuration.md.

Common Workflows
Create a Custom Extension
Generate structure with ant extgen or use template from assets/extension-structure/
Configure extensioninfo.xml with dependencies
Define types in items.xml
Configure beans in *-spring.xml
Add to localextensions.xml
Build: ant clean all

Reference: extension-development.md | Template: assets/extension-structure/

Define Custom Item Types
Create or modify *-items.xml in extension
Define itemtype with attributes, relations
Build to generate model classes
Use in services/DAOs

Reference: type-system.md | Templates: assets/item-type-definition/

Implement Service Layer
Create DTO class for data transfer
Create DAO interface and implementation with FlexibleSearch
Create Service interface and implementation with business logic
Create Facade interface and implementation for external API
Configure beans in *-spring.xml

Reference: service-layer-architecture.md | Templates: assets/service-layer/

Import Data with ImpEx
Create .impex file with header and data rows
Use INSERT_UPDATE for create/modify operations
Define macros for reusable values
Import via HAC or ant importImpex

Reference: impex-guide.md | Templates: assets/impex-scripts/

Query with FlexibleSearch
SELECT {pk} FROM {Product} WHERE {code} = ?code
SELECT {p.pk} FROM {Product AS p JOIN Category AS c ON {p.supercategories} = {c.pk}} WHERE {c.code} = ?category


Reference: flexiblesearch-reference.md | Examples: assets/flexiblesearch-queries/

Customize OCC API
Create controller with @Controller and @RequestMapping
Create WsDTO for response data
Create populator for model-to-DTO conversion
Register in *-web-spring.xml

Reference: occ-api-development.md | Templates: assets/occ-customization/

Extend Accelerator Checkout
Create custom checkout step implementing CheckoutStep
Configure in checkout flow XML
Create JSP for step UI
Register beans in *-spring.xml

Reference: accelerator-customization.md | Templates: assets/checkout-customization/

Create a Scheduled Job (CronJob)
Implement AbstractJobPerformable<CronJobModel> with perform() method
Register Spring bean with parent="abstractJobPerformable"
Create ServicelayerJob, CronJob, and Trigger via ImpEx
Test via HAC > Platform > CronJobs

Reference: cronjob-task-engine.md | Templates: assets/cronjob/

Define a Business Process
Create process definition XML in resources/processes/
Implement action beans extending AbstractSimpleDecisionAction
Register action beans in Spring with parent="abstractAction"
Register process definition via ProcessDefinitionResource Spring bean
Start process via BusinessProcessService.createProcess() and startProcess()

Reference: business-process.md | Templates: assets/business-process/

Configure Solr Product Search
Set up SolrFacetSearchConfig with server, languages, currencies, catalog versions
Define SolrIndexedType for Product
Configure SolrIndexedProperty entries (searchable, facet, sortable)
Set up indexer CronJobs (full nightly, incremental every 5 min)
Test search via HAC > Platform > Solr

Reference: solr-search-configuration.md | Templates: assets/solr-configuration/

Set Up Promotions
Create PromotionGroup for your store
Define PromotionSourceRule with conditions and actions
Configure coupons (SingleCodeCoupon / MultiCodeCoupon) if needed
Publish rules to activate them
Test in Backoffice > Marketing > Promotion Rules

Reference: promotions-rule-engine.md | Templates: assets/promotions/

Quick Reference
Task	Reference	Assets	Script
Extension setup	extension-development.md	assets/extension-structure/	scripts/generate-extension.sh
Type definitions	type-system.md	assets/item-type-definition/	-
Service layer	service-layer-architecture.md	assets/service-layer/	-
Data import	impex-guide.md	assets/impex-scripts/	scripts/validate-impex.sh
Queries	flexiblesearch-reference.md	assets/flexiblesearch-queries/	scripts/query-items.sh
API customization	occ-api-development.md	assets/occ-customization/	-
Checkout/Storefront	accelerator-customization.md	assets/checkout-customization/	-
Spring config	spring-configuration.md	-	-
Data patterns	data-modeling-patterns.md	-	-
Troubleshooting	troubleshooting-guide.md	-	-
CronJobs	cronjob-task-engine.md	assets/cronjob/	-
Business processes	business-process.md	assets/business-process/	-
Solr search	solr-search-configuration.md	assets/solr-configuration/	-
Promotions	promotions-rule-engine.md	assets/promotions/	-
Caching	caching-guide.md	-	-
Backoffice	backoffice-configuration.md	-	-
Resources
scripts/

Utility scripts for common tasks:

generate-extension.sh - Scaffold new extension structure
validate-impex.sh - Validate ImpEx syntax before import
query-items.sh - Execute FlexibleSearch queries via HAC
references/

Detailed guides for each topic area. Load as needed for in-depth information.

assets/

Production-quality code templates ready to copy and customize. Organized by domain (service-layer, impex-scripts, etc.).

Weekly Installs
14
Repository
emenowicz/sap-c…ce-skill
GitHub Stars
6
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass