---
title: aws-ec2
url: https://skills.sh/alphaonedev/openclaw-graph/aws-ec2
---

# aws-ec2

skills/alphaonedev/openclaw-graph/aws-ec2
aws-ec2
Installation
$ npx skills add https://github.com/alphaonedev/openclaw-graph --skill aws-ec2
SKILL.md
aws-ec2
AWS Agent Plugin Integration

This skill delegates all AWS provisioning and operations to the official AWS agent plugin.

/plugin marketplace add awslabs/agent-plugins
/plugin install deploy-on-aws@agent-plugins-for-aws


Use the deploy-on-aws plugin for all AWS provisioning actions.

This skill covers: architecture decisions, cost modeling, IaC patterns, and pre-flight requirements — the plugin handles execution.

Architecture Guidance

Consult this skill for:

Service selection and trade-off analysis
Cost estimation and optimization strategy
Pre-flight IAM permission requirements
IaC approach (CDK vs CloudFormation vs Terraform)
Integration patterns with other AWS services
Reference
AWS Agent Plugins
deploy-on-aws plugin
AWS MCP Servers
Weekly Installs
19
Repository
alphaonedev/ope…aw-graph
GitHub Stars
4
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn