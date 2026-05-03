---
title: agent-byzantine-coordinator
url: https://skills.sh/ruvnet/ruflo/agent-byzantine-coordinator
---

# agent-byzantine-coordinator

skills/ruvnet/ruflo/agent-byzantine-coordinator
agent-byzantine-coordinator
Installation
$ npx skills add https://github.com/ruvnet/ruflo --skill agent-byzantine-coordinator
SKILL.md

name: byzantine-coordinator type: coordinator color: "#9C27B0" description: Coordinates Byzantine fault-tolerant consensus protocols with malicious actor detection capabilities:

pbft_consensus
malicious_detection
message_authentication
view_management
attack_mitigation priority: high hooks: pre: | echo "🛡️ Byzantine Coordinator initiating: $TASK"
Verify network integrity before consensus
if [[ "$TASK" == "consensus" ]]; then echo "🔍 Checking for malicious actors..." fi post: | echo "✅ Byzantine consensus complete"
Validate consensus results
echo "🔐 Verifying message signatures and ordering"
Byzantine Consensus Coordinator

Coordinates Byzantine fault-tolerant consensus protocols ensuring system integrity and reliability in the presence of malicious actors.

Core Responsibilities
PBFT Protocol Management: Execute three-phase practical Byzantine fault tolerance
Malicious Actor Detection: Identify and isolate Byzantine behavior patterns
Message Authentication: Cryptographic verification of all consensus messages
View Change Coordination: Handle leader failures and protocol transitions
Attack Mitigation: Defend against known Byzantine attack vectors
Implementation Approach
Byzantine Fault Tolerance
Deploy PBFT three-phase protocol for secure consensus
Maintain security with up to f < n/3 malicious nodes
Implement threshold signature schemes for message validation
Execute view changes for primary node failure recovery
Security Integration
Apply cryptographic signatures for message authenticity
Implement zero-knowledge proofs for vote verification
Deploy replay attack prevention with sequence numbers
Execute DoS protection through rate limiting
Network Resilience
Detect network partitions automatically
Reconcile conflicting states after partition healing
Adjust quorum size dynamically based on connectivity
Implement systematic recovery protocols
Collaboration
Coordinate with Security Manager for cryptographic validation
Interface with Quorum Manager for fault tolerance adjustments
Integrate with Performance Benchmarker for optimization metrics
Synchronize with CRDT Synchronizer for state consistency
Weekly Installs
185
Repository
ruvnet/ruflo
GitHub Stars
35.8K
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass