---
rating: ⭐⭐
title: tenzir-docs
url: https://skills.sh/tenzir/skills/tenzir-docs
---

# tenzir-docs

skills/tenzir/skills/tenzir-docs
tenzir-docs
Installation
$ npx skills add https://github.com/tenzir/skills --skill tenzir-docs
SKILL.md
Tenzir Documentation Map

The low-code data pipeline solution for security teams

Tenzir is a data pipeline engine for security teams. Run pipelines to collect, parse, transform, and route security data. Deploy nodes on-prem or in the cloud, and manage them via the Tenzir Platform.

How to use this skill

Navigate the documentation based on the type of question:

Question type	Where to look
"How do I…" tasks	Guides — step-by-step instructions organized by task
Operator or function syntax	Operator Index or Function Index, then the specific page
Integration setup (Splunk, Kafka, S3…)	Integrations — per-product setup and pipeline examples
Concepts (nodes, pipelines, deployment)	Explanations — architecture and design
Learning from scratch	Tutorials — guided lessons
TQL language rules	Language, Expressions, Statements

Always read the relevant page before answering. Prefer TQL examples from the documentation over inventing syntax.

Answer patterns

Operator syntax question — "How does where work?" → Read where, explain the syntax, show the doc's TQL examples.

Integration question — "How do I send data to Splunk?" → Read Splunk, provide the pipeline example from the page.

Task question — "How do I parse syslog?" → Read Parse delimited text and read_syslog. Combine the guide's approach with the operator reference.

Guides

Practical step-by-step explanations to help you achieve a specific goal. Start here when you're trying to get something done.

Get Started
Quickstart

Drowning in logs, alerts, and rigid tools? Meet Tenzir—your engine for taming security data. In just a few minutes, you’ll be ingesting, transforming, and enriching data on your terms, with full control. Here’s what you’ll accomplish:

Installation

This guide shows you how to install the Tenzir CLI to run pipelines locally or deploy a persistent node. The package includes two binaries:

Create account

The Tenzir Platform is a web interface for managing pipelines and nodes. Create an account to get started:

Basic Usage
Run pipelines

You can run a pipeline via the platform, on the command line using the tenzir binary, or as code via the configuration file.

Manage a pipeline

This guide shows you how to control pipeline lifecycles through the app or API. A pipeline transitions through the following states:

Setup
Node Setup

The Tenzir Node is the vehicle to run pipelines. It is light-weight server application that can be deployed on-premises or in the cloud.

Provision a node

Provisioning a node means creating one in the platform in your workspace. After provisioning, you can download configuration file with an authentication token—ready to then deploy the node.

Size a node

This guide helps you determine the CPU, RAM, and storage resources needed for a Tenzir node. Use the calculator below to get concrete estimates based on your deployment scenario.

Deploy a node

Deploying a node means spinning it up in one of the supported runtimes. The primary choice is between a containerized with Docker or a native deployment with our static binary that runs on amd64 and arm64 architectures.

Configure a node

The default node configuration is optimized for most common scenarios. But you can fine-tune the settings to match your specific requirements.

Configure TLS

Tenzir supports Transport Layer Security (TLS) for encrypting network connections. You can configure TLS settings centrally in tenzir.yaml so they apply to all compatible operators, or override them per-operator as needed.

Start the API

The node offers a REST API for CRUD-style pipeline management. By default, the API is not accessible from the outside. Only the platform can access it internaly through the existing node-to-platform connection. To enable the API for direct access, you need to configure the built in web server that exposes the API.

Tune performance

This guide covers configuration options that affect node performance. You’ll learn how to tune demand scheduling, memory usage, and throughput settings.

Platform Setup

The Tenzir Platform acts as a fleet management control plane for Tenzir Nodes. Use its web interface to explore data, create pipelines, and build dashboards.

Deploy on AWS

This guide walks you through deploying the Tenzir Platform Sovereign Edition on AWS using CloudFormation. The template automates the setup of all required infrastructure components.

Choose a scenario

We provide several examples of possible platform deployment scenarios. Pick one that best suits your needs.

Configure reverse proxy

This guide shows you how to configure a reverse proxy for the Tenzir Platform. The proxy terminates TLS and routes traffic to these four entry points:

Configure internal services

This guide shows you how to configure the three internal Tenzir services: the UI, Gateway, and Platform API. You’ll set environment variables that control authentication, connectivity, and feature settings.

Configure identity provider

The identity provider (IdP) handles authentication for the Tenzir Platform. When you click the Login button in the Tenzir UI, the system redirects you to your chosen identity provider, which creates a signed token that certifies your identity.

Configure database

A PostgreSQL database stores the internal state of the platform.

Configure blob storage

The blob storage service exists for exchanging files between the platform and nodes. It facilitates not only downloading data from nodes, but also uploading files from your browser to the platform.

Configure secret store

The Tenzir Platform provides a secret store for each workspace. All Tenzir Nodes connected to the workspace can access its secrets. You can manage secrets using the CLI or the web interface. Alternatively, you can use an external secret store.

Run the platform

This guide shows you how to start the Tenzir Platform using Docker Compose. Complete this step after configuring all services.

Platform Management
Manage organizations

This guide shows you how to create, configure, and delete organizations in the Tenzir Platform. You’ll learn how to perform these tasks through both the web and the CLI.

Manage organization members

This guide shows you how to invite people to your organization, manage existing members, and understand the role-based permission model. You’ll learn how to use both the web and the CLI for these tasks.

Manage organization workspaces

This guide shows you how to create, view, and delete workspaces that belong to an organization. You’ll learn the difference between personal and organization workspaces and how access control works for shared workspaces.

Configure workspaces

Workspaces in the platform logically group nodes, secrets, and dashboards.

Configure dashboards

You can pre-define dashboards for your static workspaces. This practice provides users with ready-to-use visualizations when they access the workspace.

Use ephemeral nodes

An ephemeral node is ideal for temporary or auto-scaling deployments. It is a temporary node that you do not have to provision manually first, and it disappears from the workspace when the connection to the platform ends.

AI Workbench

Build your own AI Workbench by bringing an AI agent and configuring it with Tenzir’s agent skills. Once set up, use it to write TQL pipelines, understand OCSF schemas, generate parsers, and create data mappings.

Use agent skills

This guide shows you how to install and manage Tenzir’s agent skills. You’ll learn how to add skills globally or per project, install individual skills, and keep them up to date.

Work with Data
Collecting

This guide provides an overview of data collection in TQL. You’ll learn about the different approaches for ingesting data from various sources.

Read and watch files

This guide shows you how to read files and monitor directories using the from_file operator. You’ll learn to read individual files, batch process directories, and set up real-time file monitoring.

Fetch via HTTP and APIs

This guide shows you how to fetch data from HTTP APIs using the from_http and http operators. You’ll learn to make GET requests, handle authentication, and implement pagination for large result sets.

Read from message brokers

This guide shows you how to receive events from message brokers using TQL. You’ll learn to subscribe to topics and queues from Apache Kafka (including Amazon MSK), AMQP-based brokers (like RabbitMQ), Amazon SQS, and Google Cloud Pub/Sub.

Get data from the network

This guide shows you how to receive data directly from network sources using TQL. You’ll learn to listen on TCP and UDP sockets for incoming data and capture raw packets from network interfaces.

Parsing
Parse delimited text

This guide shows you how to parse text streams into structured events. You’ll learn to split byte streams on newlines or custom delimiters, and parse line-based formats like JSON lines, CSV, TSV, key-value pairs, Syslog, and CEF.

Parse binary data

This guide shows you how to parse binary data formats into structured events. You’ll learn to work with columnar formats like Parquet and Feather, packet captures in PCAP format, Tenzir’s native Bitz format, and compressed data.

Parse string fields

This guide shows you how to extract structured data from string fields using TQL’s parsing functions. You’ll learn to parse JSON, YAML, XML, key-value pairs, delimited data, timestamps, and log formats like Syslog, CEF, LEEF, and Windows Event Logs. For custom formats, Grok patterns provide flexible pattern matching.

Transformation
Filter and select data

Filtering and selecting are fundamental operations when working with data streams. This guide shows you how to filter events based on conditions and select specific fields from your data.

Transform values

Transforming values is a fundamental part of data processing. This guide shows you how to convert between different data types, perform basic calculations, and manipulate simple values within your events.

Manipulate strings

String manipulation is essential for cleaning, formatting, and transforming text data. This guide covers TQL’s comprehensive string functions, from simple case changes to complex pattern matching and encoding operations.

Work with time

Time is fundamental in data analysis. Whether you’re analyzing logs, tracking events, or monitoring systems, you need to parse timestamps, calculate durations, and format dates. This guide shows you how to work with time values in TQL.

Shape lists

Lists (arrays) contain ordered sequences of values. This guide shows you how to work with lists — accessing elements, sorting and slicing, transforming values, and combining data structures.

Shape records

Records (objects) contain key-value pairs. This guide shows you how to work with records — accessing fields, extracting keys, merging, and transforming values.

Reshape complex data

Real-world data is rarely flat. It contains nested structures, arrays of objects, and deeply hierarchical information. This guide shows advanced techniques for reshaping complex data structures to meet your analysis needs.

Convert data formats

Data comes in many formats. Converting between formats is essential for integration, export, and interoperability. This guide shows you how to transform data between JSON, CSV, YAML, and other common formats using TQL’s print functions.

Normalization

This guide provides an overview of data normalization in TQL. Normalization transforms raw, inconsistent data into a clean, standardized format that’s ready for analysis, storage, and sharing.

Clean up values

This guide shows you how to clean and normalize values in your data before mapping to a schema. You’ll learn to handle null placeholders, normalize sentinel values, fix types, and provide defaults.

Map to OCSF

This guide shows you how to write OCSF mapping operators in TQL. You’ll learn to organize mappings by attribute groups, handle unmapped fields, and validate your output. The guide assumes you’ve already identified your target OCSF event class and profiles.

Map to other schemas

This guide provides brief guidance on mapping data to schemas other than OCSF. While OCSF is the recommended choice for security data, you may need to support Elastic Common Schema (ECS), Google UDM, or Microsoft ASIM for integration with specific platforms.

Enrichment
Work with lookup tables

A lookup table is a specific type of context in Tenzir’s enrichment framework. It has “two ends” in that you can use pipelines to update it, as well as pipelines to perform lookups and attach the results to events. Lookup tables live in a node and multiple pipelines can safely use the same lookup table. All update operations propagate to disk, persisting the changes and making them resilient against node restarts.

Enrich with network inventory

Tenzir’s enrichment framework features lookup tables that you can use to enrich data in your pipelines. Lookup tables have a unique property that makes them attractive for tracking information associated with CIDR subnets: when you use subnet values as keys, you can probe the lookup table with ip values and will get a longest-prefix match.

Enrich with threat intel

Tenzir has a powerful enrichment framework for real-time contextualization. The heart of the framework is a context—a stateful object that can be managed and used with pipelines.

Execute Sigma rules

Tenzir supports executing Sigma rules using the sigma operator. This allows you to run your Sigma rules in the pipeline. The operator transpiles the provided rules into an expression, and wraps matching events into a sighting record along with the matched rule.

Optimization
Slice and sample data

When working with data streams, you often need to control which events flow through your pipeline. This guide shows you how to slice event streams, sample data, and control event ordering using TQL operators.

Deduplicate events

The deduplicate operator provides a powerful mechanism to remove duplicate events in a pipeline.

Routing
Send to destinations

This guide shows you how to send data to various destinations using TQL output operators. You’ll learn about destination operators, file output patterns, and expression-based serialization.

Split and merge streams

This guide shows you how to connect pipelines using publish and subscribe operators. You’ll learn to split event streams for parallel processing and merge multiple sources into a single pipeline.

Load-balance pipelines

This guide shows you how to distribute events across multiple destinations using the load_balance operator. You’ll learn to route events to multiple endpoints for high availability and throughput.

Analytics
Aggregate and summarize data

Aggregation transforms streams of events into meaningful summaries. Whether you’re calculating statistics, counting occurrences, or finding extremes, the summarize operator combined with aggregation functions provides powerful data analysis capabilities.

Collect metrics

Tenzir keeps track of metrics about node resource usage, pipeline state, and runtime performance.

Edge Storage
Import into a node

Importing (or ingesting) data can be done by running a pipeline that ends with the import output operator. When managing a pipeline through the app or the API, all pipeline operators run within the node. When using the CLI, at least the import operator runs within the node.

Export from a node

Exporting (or querying) data can be done by running a pipeline that begins with the export input operator. When managing a pipeline through the app or the API, all pipeline operators run within the node. When using the CLI, at least the export operator runs within the node.

Show available schemas

When you write a pipeline, you often reference field names. If you do not know the shape of your data, you can look up available schemas, i.e., the record types describing top-level events.

Transform data at rest

This guide shows you how to transform data already stored in a node. You’ll learn to apply compaction, manage storage quotas, and run retroactive pipelines.

Build
Packages
Install a package

Packages provide a flexible approach for combining operators, pipelines, contexts, and examples into a unified deployable unit.

Create a package

This guide shows you how to create a package from scratch. You’ll learn how to set up the directory structure, write the manifest, and add runnable examples.

Test packages

This guide shows you how to add tests to your package. You’ll learn how to write test files, use inline inputs, and run the test harness.

Add operators

This guide shows you how to create user-defined operators (UDOs) for your package. You’ll learn how to define operators with positional and named arguments, and how to test them with the Test Framework.

Add pipelines

This guide shows you how to add deployable pipelines to your package. You’ll learn about pipeline frontmatter options and when to use pipelines versus operators.

Add contexts

This guide shows you how to add enrichment contexts to your package. You’ll learn how to define contexts in the manifest, populate them with data, and test context interactions.

Configure inputs

This guide shows you how to make packages configurable with inputs. You’ll learn how to define input variables, use templating syntax, and provide values during installation.

Maintain a changelog

This guide shows you how to manage changelog entries and publish releases with tenzir-ship. You’ll learn the complete workflow from adding your first entry to publishing a release on GitHub.

Publish a package

This guide shows you how to publish your package. You’ll learn how to contribute to the Tenzir Community Library and how to set up your own package repository with automated testing.

Testing
Run tests

This guide shows you how to run existing integration tests with the tenzir-test framework. You’ll learn how to execute the test suite, control output verbosity, select specific tests, handle flaky scenarios, and run multi-project setups.

Write tests

This guide shows you how to create integration tests with the tenzir-test framework. You’ll set up a standalone repository, write test scenarios, and record reference output to verify your pipelines work as expected. If you already have tests and want to run them, see the run tests guide.

Run fixtures

This guide shows you how to start fixtures in standalone mode without running tests. You’ll learn how to use the --fixture CLI option to bring up managed services, inspect their environment variables, and tear them down cleanly.

Create fixtures

This guide shows you how to create a fixture, wire it into the test harness, and use it from a test. You will build an HTTP echo server as a running example and then learn how to share fixtures across suites, handle missing dependencies, manage containers, add structured options, and validate test behavior with fixture assertions.

Add custom runners

Runners tell tenzir-test how to execute a discovered file. This guide shows you how to register the XXD runner from the example project so you can compare binary artifacts by dumping their hexadecimal representation with xxd.

Configure project hooks

This guide shows you how to configure tenzir-test project hooks for setup and cleanup tasks that belong next to your tests. You’ll learn how to select local Tenzir binaries before discovery, set project-scoped environment variables, and collect artifacts from failed tests.

Contribute
Contribution
Code of Conduct
Git and GitHub Workflow

The following diagram visualizes our branching model:

Documentation

The source code of the Tenzir documentation is at https://github.com/tenzir/docs. We use Astro with Starlight as our site framework.

Security Policy

Security is a serious matter for us. We want to ensure and maintain a secure environment for our customers and the open-source community.

Development
Setup syntax highlighting

This guide shows you how to set up TQL syntax highlighting in your editor. You’ll get proper colorization, language detection, and basic language support for .tql files.

Build from source

Tenzir uses CMake as build system with a C++23 compiler.

Write a node plugin

This guide shows you how to extend Tenzir with custom operators, formats, or connectors by writing a C++ plugin. The implementation requires the following steps:

Tutorials

Learning-oriented lessons that take you through a series of steps. Start here when you want to get started with Tenzir.

Fundamentals
Learn idiomatic TQL

This tutorial teaches you to write TQL that is clear, efficient, and maintainable. It assumes you already know basic TQL syntax and operators, and shows you how experienced TQL developers approach common patterns.

Write a package

This tutorial teaches you how packages bundle pipelines, operators, contexts, and examples. You’ll build a package for an SSL blacklist that detects malicious certificates. You can then install packages from the Tenzir Library or deploy them as code.

Map data to OCSF

In this tutorial you’ll learn how to map events to Open Cybersecurity Schema Framework (OCSF). We walk you through an example of events from a network monitor and show how you can use Tenzir pipelines to transform them into OCSF-compliant events.

Analytics
Plot data with charts

In this tutorial, you will learn how to use pipelines to plot data as charts.

Explanations

Big-picture explanations of higher-level concepts. Start here to build understanding of a particular topic.

Architecture
Deployment

This page explains Tenzir’s deployment architecture, which separates data processing from management through a layered design. Three primary abstractions work together:

Pipeline

A Tenzir pipeline is a chain of operators that represents a dataflow. Operators are the atomic building blocks that produce, transform, or consume data. Think of them as Unix or Powershell commands where the result from one command is feeding into the next:

Node

A node is a running process that manages and executes pipelines.

Platform

The platform provides fleet management for nodes. With an API and web interface, the platform offers user and workspace administration, authentication via external identity providers (IdP), and dashboards consisting of pipeline-powered charts.

Language

The Tenzir Query Language (TQL) is a dataflow language designed for processing of unstructured byte-streams and semi-structured events.

Concepts
Configuration

This page explains how to configure the Tenzir CLI and Node. Configuration flows through four layers, sorted by precedence:

Secrets

Operators accept secrets as parameters for sensitive values, such as authentication tokens, passwords, or even URLs.

Enrichment

Enrichment means adding contextual data to events. The purpose of this added context is to allow for making better decisions, e.g., to triage alerts and weed out false positive, to leverage country information to classify logins as malicious, or to flag a sighting of an indicator of compromise.

Packages

This page explains how packages bundle pipelines, operators, contexts, and examples into a deployable unit. You’ll learn about package design principles and how the components fit together.

Help
Glossary

This page defines central terms in the Tenzir ecosystem.

FAQs

This page answers frequently asked questions about Tenzir.

Reference

Nitty-gritty technical descriptions of how Tenzir works. Start here when you need detailed information about building blocks.

Language (TQL)
Type System

This page explains TQL’s type system, which provides strong typing with automatic inference. You get type safety without requiring explicit declarations. Key characteristics include:

Expressions

Expressions form the computational core of TQL. They range from simple literals to complex evaluations.

Statements

TQL programs are a sequence of statements. Operator statements perform various actions on data streams. Each operator statement can be thought of as a modular unit that processes data and can be combined with other operators to create complex dataflows.

Programs

TQL programs compose statements into complete data processing workflows that can execute. Valid TQL programs adhere to the following rules:

Operators

Tenzir comes with a wide range of built-in pipeline operators.

Functions

Functions appear in expressions and take positional and/or named arguments, producing a value as a result of their computation.

Tools
Test Framework

The tenzir-test harness discovers and runs integration tests for pipelines, fixtures, and custom runners. Use this page as a reference for concepts, configuration, and CLI details. For step-by-step walkthroughs, see the guides for running tests, writing tests, creating fixtures, adding custom runners, and configuring project hooks.

Ship Framework

tenzir-ship helps you ship faster with automated release engineering. Manage changelogs, generate release notes, and publish GitHub releases. Use this page as a reference for concepts, configuration, and CLI details. For step-by-step walkthroughs, see the guide for maintaining a changelog.

Node Index
Node Configuration
Platform Index
Platform command line interface
Platform Configuration
Indexes

For the complete operator listing by category, read Operator Index.

For the complete function listing by category, read Function Index.

Integrations

Turn-key packages and native connectors for security tools. Start here to connect Tenzir with Splunk, Elastic, CrowdStrike, etc.

Cloud Providers
Amazon

Tenzir integrates with the services from Amazon Web Services (AWS) listed below.

MSK

Amazon Managed Streaming for Apache Kafka (Amazon MSK) is a managed Kafka service on AWS. It handles infrastructure and operations, making it easier to run Kafka applications and Kafka Connect connectors without becoming a Kafka expert.

S3

Amazon Simple Storage Service (S3) is an object storage service. Tenzir can treat it like a local filesystem to read and write files.

Security Lake

Amazon Security Lake is a managed security data lake on AWS. It collects and stores security data in the Open Cybersecurity Schema Framework (OCSF) format.

SQS

Amazon Simple Queuing Service (SQS) is a managed message queue on AWS. It supports microservices, distributed systems, and serverless applications.

Google
Cloud Logging

Google Cloud Logging is Google’s log management solution. Tenzir can send events to Google Cloud Logging.

Cloud Storage

Cloud Storage is Google’s object storage service. Tenzir can treat it like a local filesystem to read and write files.

Cloud Pub/Sub

Google Cloud Pub/Sub ingests events for streaming into BigQuery, data lakes, or operational databases. Tenzir can act as a publisher that sends messages to a topic, and as a subscriber that receives messages from a subscription.

SecOps

Google Security Operations (SecOps) is Google’s security operations platform. Tenzir can send events to Google SecOps using the unstructured logs ingestion API.

Microsoft
Azure Blob Storage

Azure Blob Storage is Azure’s object storage service. Tenzir can treat it like a local filesystem to read and write files.

Azure Event Hubs

Azure Event Hubs is a real-time event ingestion service. It can receive and process millions of events per second, and it provides a Kafka endpoint for streaming data from Microsoft services to Tenzir.

Defender

Microsoft Defender offers protection, detection, investigation, and response to threats. Defender comes in multiple editions, Defender for Office 365, Defender for Endpoint, Defender for IoT, Defender for Identity, and Defender for Cloud. All Defender products can stream events in real time to Tenzir using Azure Event Hubs.

Sentinel & Log Analytics

Send security logs and events from Tenzir to Microsoft’s Log Analytics platform. You can analyze them with Microsoft Sentinel, create alerts with Azure Monitor, or query them with KQL.

Windows Event Logs

Windows Event Logs record system, security, and application events on Windows. You can collect them into Tenzir for monitoring, troubleshooting, and analysis.

Messaging
AMQP

The Advanced Message Queuing Protocol (AMQP) is an open standard for message-oriented middleware. It defines how producers, exchanges, queues, and consumers route messages between systems.

Fluent Bit

Fluent Bit is a an open source observability pipeline. Tenzir embeds Fluent Bit, exposing all its inputs via from_fluent_bit and outputs via to_fluent_bit

Kafka

Apache Kafka is a distributed open-source message broker. The Tenzir integration can publish (send messages to a topic) or subscribe (receive) messages from a topic.

ZeroMQ

ZeroMQ (0mq) is a light-weight messaging framework with various socket types. Tenzir supports writing to PUB sockets and reading from SUB sockets, both in server (listening) and client (connect) mode.

Protocols
Email

Tenzir supports sending events as email using the save_email operator. To this end, the operator establishes a connection with an SMTP server that sends the message on behalf of Tenzir.

File

Tenzir can read from and write to files. This includes non-regular files such as Unix domain sockets, standard input, standard output, and standard error.

FTP

Tenzir supports the File Transfer Protocol (FTP), both downloading and uploading files.

HTTP

Tenzir supports HTTP and HTTPS, both as sender and receiver.

Network Interface

Tenzir supports reading packets from a network interface card (NIC).

Syslog

Tenzir supports parsing and emitting Syslog messages across multiple transport protocols, including both UDP and TCP. This enables seamless integration with Syslog-based systems for ingesting or exporting logs.

TCP

The Transmission Control Protocol (TCP) provides a bidirectional byte stream over IP. Tenzir supports reading from and writing to TCP sockets in both server (listening) and client (connect) mode.

UDP

The User Datagram Protocol (UDP) is a connection-less protocol to send messages on an IP network. Tenzir supports writing to and reading from UDP sockets, both in server (listening) and client (connect) mode.

Data Tools
ClickHouse

ClickHouse is an open-source analytical database. It lets you run real-time analytics with SQL queries.

Elasticsearch

Elasticsearch is a search and observability suite for unstructured data. Tenzir can send events to Elasticsearch and emulate and Elasticsearch Bulk API endpoint.

Graylog

Graylog is a log management solution based on top of OpenSearch. Tenzir can send data to and receive data from Graylog.1

OpenSearch

OpenSearch is a search and observability suite for unstructured data. Tenzir can send events to OpenSearch and emulate and OpenSearch Bulk API endpoint.

Snowflake

Snowflake is a multi-cloud data warehouse. Tenzir can send events from a pipeline to Snowflake databases.

Splunk

Splunk is a SIEM solution for storing and processing logs. Tenzir can send data to Splunk via HEC.

Security Tools
SentinelOne Data Lake

SentinelOne is a cybersecurity platform that provides endpoint protection and threat detection. The SentinelOne Singularity Data Lake allows you to store and analyze security events at scale. Tenzir provides bidirectional integration with the SentinelOne Data Lake via its REST API.

Suricata

Suricata is network monitor with a rule matching engine to detect threats. Use Tenzir to acquire, process, and store Suricata logs.

Velociraptor

Velociraptor is a digital forensics and incident response (DFIR) tool for interrogating endpoints.

Zeek

The Zeek network monitor translates raw packets into structured logs. Tenzir supports various Zeek use cases, such as continuous ingestion, ad-hoc log file processing, and even generating Zeek logs.

Zscaler

Zscaler’s Nanolog Streaming Service (NSS) streams Zscaler logs to external systems. You can use Zscaler’s Cloud NSS or deploy an on-prem NSS server, and Tenzir can receive logs in either case.

Weekly Installs
61
Repository
tenzir/skills
GitHub Stars
1
First Seen
Mar 11, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass