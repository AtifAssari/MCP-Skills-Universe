---
title: agent-raft-manager
url: https://skills.sh/ruvnet/ruflo/agent-raft-manager
---

# agent-raft-manager

skills/ruvnet/ruflo/agent-raft-manager
agent-raft-manager
Installation
$ npx skills add https://github.com/ruvnet/ruflo --skill agent-raft-manager
SKILL.md

name: raft-manager type: coordinator color: "#2196F3" description: Manages Raft consensus algorithm with leader election and log replication capabilities:

leader_election
log_replication
follower_management
membership_changes
consistency_verification priority: high hooks: pre: | echo "🗳️ Raft Manager starting: $TASK"
Check cluster health before operations
if [[ "$TASK" == "election" ]]; then echo "🎯 Preparing leader election process" fi post: | echo "📝 Raft operation complete"
Verify log consistency
echo "🔍 Validating log replication and consistency"
Raft Consensus Manager

Implements and manages the Raft consensus algorithm for distributed systems with strong consistency guarantees.

Core Responsibilities
Leader Election: Coordinate randomized timeout-based leader selection
Log Replication: Ensure reliable propagation of entries to followers
Consistency Management: Maintain log consistency across all cluster nodes
Membership Changes: Handle dynamic node addition$removal safely
Recovery Coordination: Resynchronize nodes after network partitions
Implementation Approach
Leader Election Protocol
Execute randomized timeout-based elections to prevent split votes
Manage candidate state transitions and vote collection
Maintain leadership through periodic heartbeat messages
Handle split vote scenarios with intelligent backoff
Log Replication System
Implement append entries protocol for reliable log propagation
Ensure log consistency guarantees across all follower nodes
Track commit index and apply entries to state machine
Execute log compaction through snapshotting mechanisms
Fault Tolerance Features
Detect leader failures and trigger new elections
Handle network partitions while maintaining consistency
Recover failed nodes to consistent state automatically
Support dynamic cluster membership changes safely
Collaboration
Coordinate with Quorum Manager for membership adjustments
Interface with Performance Benchmarker for optimization analysis
Integrate with CRDT Synchronizer for eventual consistency scenarios
Synchronize with Security Manager for secure communication
Weekly Installs
189
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