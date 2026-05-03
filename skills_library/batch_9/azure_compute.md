---
title: azure-compute
url: https://skills.sh/microsoft/azure-skills/azure-compute
---

# azure-compute

skills/microsoft/azure-skills/azure-compute
azure-compute
Installation
$ npx skills add https://github.com/microsoft/azure-skills --skill azure-compute
Summary

Recommend Azure VM sizes, scale sets, and configurations based on workload requirements and budget.

Analyzes workload type, performance needs, scaling requirements, and cost to suggest 2–3 VM or VMSS options with trade-offs
Verifies recommendations against live Microsoft documentation; falls back to reference files if fetch fails
Queries the unauthenticated Azure Retail Prices API for current pricing without requiring an Azure subscription
Guides VM vs VMSS decision through a decision tree covering autoscaling, instance count, availability, and statefulness
Covers all VM families (general purpose, compute/memory optimized, GPU, confidential computing) and VMSS orchestration modes (Flexible vs Uniform)
SKILL.md
Azure Compute Skill

Routes Azure VM requests to the appropriate workflow based on user intent.

When to Use This Skill

Activate this skill when the user:

Asks about Azure Virtual Machines (VMs) or VM Scale Sets (VMSS)
Asks about choosing a VM, VM sizing, pricing, or cost estimates
Needs a workload-based recommendation for scenarios like database, GPU, deep learning, HPC, web tier, or dev/test
Mentions VM families, autoscale, load balancing, or Flexible versus Uniform orchestration
Wants to troubleshoot Azure VM connectivity issues such as unreachable VMs, RDP/SSH failures, black screens, NSG/firewall issues, or credential resets
Asks about Capacity Reservation Groups (CRGs), reserving VM capacity, associating/disassociating VMs with a CRG, or guaranteeing compute capacity
Uses prompts like "Help me choose a VM"
Routing
User intent?
├─ Recommend / choose / compare / price a VM or VMSS
│  └─ Route to [VM Recommender](workflows/vm-recommender/vm-recommender.md)
│
├─ Can't connect / RDP / SSH / troubleshoot a VM
│  └─ Route to [VM Troubleshooter](workflows/vm-troubleshooter/vm-troubleshooter.md)
│
├─ Capacity reservation / CRG / reserve capacity / associate VM with CRG
│  └─ Route to [Capacity Reservation](workflows/capacity-reservation/capacity-reservation.md)
│
└─ Unclear
   └─ Ask: "Are you looking for a VM recommendation, troubleshooting a connectivity issue, or managing capacity reservations?"

Signal	Workflow
"recommend VM", "which VM", "VM size", "VM pricing", "VMSS", "scale set"	VM Recommender
"can't connect", "RDP", "SSH", "NSG blocking", "reset password", "black screen"	VM Troubleshooter
"capacity reservation", "CRG", "reserve capacity", "guarantee capacity", "associate VM with CRG"	Capacity Reservation

Routing rule: Always read the matched workflow file before accessing any reference files. The workflow file contains the step-by-step guidance and the reference routing table for the user's request.

Workflows
Workflow	Purpose	References
VM Recommender	Recommend VM sizes, VMSS, pricing using public APIs/docs	vm-families, retail-prices-api, vmss-guide, vm-quotas
VM Troubleshooter	Diagnose and resolve VM connectivity failures (RDP/SSH)	cannot-connect-to-vm
Capacity Reservation	Create and manage Capacity Reservation Groups (CRGs)	capacity-reservation-overview, association-disassociation
Weekly Installs
275.9K
Repository
microsoft/azure-skills
GitHub Stars
796
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass