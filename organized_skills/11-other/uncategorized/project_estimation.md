---
rating: ⭐⭐
title: project-estimation
url: https://skills.sh/aj-geddes/useful-ai-prompts/project-estimation
---

# project-estimation

skills/aj-geddes/useful-ai-prompts/project-estimation
project-estimation
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill project-estimation
SKILL.md
Project Estimation
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Accurate project estimation determines realistic timelines, budgets, and resource allocation. Effective estimation combines historical data, expert judgment, and structured techniques to minimize surprises.

When to Use
Defining project scope and deliverables
Creating project budgets and timelines
Allocating team resources
Managing stakeholder expectations
Assessing project feasibility
Planning for contingencies
Updating estimates during project execution
Quick Start

Minimal working example:

# Three-point estimation technique for uncertainty

class ThreePointEstimation:
    @staticmethod
    def calculate_pert_estimate(optimistic, most_likely, pessimistic):
        """
        PERT formula: (O + 4M + P) / 6
        Weighted toward most likely estimate
        """
        pert = (optimistic + 4 * most_likely + pessimistic) / 6
        return round(pert, 2)

    @staticmethod
    def calculate_standard_deviation(optimistic, pessimistic):
        """Standard deviation for risk analysis"""
        sigma = (pessimistic - optimistic) / 6
        return round(sigma, 2)

    @staticmethod
    def calculate_confidence_interval(pert_estimate, std_dev, confidence=0.95):
        """
        Calculate confidence interval for estimate
        95% confidence ≈ ±2 sigma
        """
        z_score = 1.96 if confidence == 0.95 else 2.576
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Three-Point Estimation (PERT)	Three-Point Estimation (PERT)
Bottom-Up Estimation	Bottom-Up Estimation
Analogous Estimation	Analogous Estimation
Resource Estimation	Resource Estimation
Estimation Templates	Estimation Templates
Best Practices
✅ DO
Use multiple estimation techniques and compare results
Include contingency buffers (15-25% for new projects)
Base estimates on historical data from similar projects
Break down large efforts into smaller components
Get input from team members doing the actual work
Document assumptions and exclusions clearly
Review and adjust estimates regularly
Track actual vs. estimated metrics for improvement
Include non-development tasks (planning, testing, deployment)
Account for learning curve on unfamiliar technologies
❌ DON'T
Estimate without clear scope definition
Use unrealistic best-case scenarios
Ignore historical project data
Estimate under pressure to hit arbitrary targets
Forget to include non-coding activities
Use estimates as performance metrics for individuals
Change estimates mid-project without clear reason
Estimate without team input
Ignore risks and contingencies
Use one technique exclusively
Weekly Installs
358
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass