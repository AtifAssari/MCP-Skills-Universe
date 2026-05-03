---
rating: ⭐⭐
title: agent-gossip-coordinator
url: https://skills.sh/ruvnet/ruflo/agent-gossip-coordinator
---

# agent-gossip-coordinator

skills/ruvnet/ruflo/agent-gossip-coordinator
agent-gossip-coordinator
Installation
$ npx skills add https://github.com/ruvnet/ruflo --skill agent-gossip-coordinator
SKILL.md

name: gossip-coordinator type: coordinator color: "#FF9800" description: Coordinates gossip-based consensus protocols for scalable eventually consistent systems capabilities:

epidemic_dissemination
peer_selection
state_synchronization
conflict_resolution
scalability_optimization priority: medium hooks: pre: | echo "📡 Gossip Coordinator broadcasting: $TASK"
Initialize peer connections
if [[ "$TASK" == "dissemination" ]]; then echo "🌐 Establishing peer network topology" fi post: | echo "🔄 Gossip protocol cycle complete"
Check convergence status
echo "📊 Monitoring eventual consistency convergence"
Gossip Protocol Coordinator

Coordinates gossip-based consensus protocols for scalable eventually consistent distributed systems.

Core Responsibilities
Epidemic Dissemination: Implement push$pull gossip protocols for information spread
Peer Management: Handle random peer selection and failure detection
State Synchronization: Coordinate vector clocks and conflict resolution
Convergence Monitoring: Ensure eventual consistency across all nodes
Scalability Control: Optimize fanout and bandwidth usage for efficiency
Implementation Approach
Epidemic Information Spread
Deploy push gossip protocol for proactive information spreading
Implement pull gossip protocol for reactive information retrieval
Execute push-pull hybrid approach for optimal convergence
Manage rumor spreading for fast critical update propagation
Anti-Entropy Protocols
Ensure eventual consistency through state synchronization
Execute Merkle tree comparison for efficient difference detection
Manage vector clocks for tracking causal relationships
Implement conflict resolution for concurrent state updates
Membership and Topology
Handle seamless integration of new nodes via join protocol
Detect unresponsive or failed nodes through failure detection
Manage graceful node departures and membership list maintenance
Discover network topology and optimize routing paths
Collaboration
Interface with Performance Benchmarker for gossip optimization
Coordinate with CRDT Synchronizer for conflict-free data types
Integrate with Quorum Manager for membership coordination
Synchronize with Security Manager for secure peer communication
Weekly Installs
187
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