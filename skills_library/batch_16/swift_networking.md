---
title: swift-networking
url: https://skills.sh/johnrogers/claude-swift-engineering/swift-networking
---

# swift-networking

skills/johnrogers/claude-swift-engineering/swift-networking
swift-networking
Installation
$ npx skills add https://github.com/johnrogers/claude-swift-engineering --skill swift-networking
SKILL.md
Swift Networking

Network.framework is Apple's modern networking API for TCP/UDP connections, replacing BSD sockets with smart connection establishment, user-space networking, and seamless mobility handling.

Reference Loading Guide

ALWAYS load reference files if there is even a small chance the content may be required. It's better to have the context than to miss a pattern or make a mistake.

Reference	Load When
Getting Started	Setting up NWConnection for TCP/UDP, choosing between APIs
Connection States	Handling .waiting, .ready, .failed transitions
iOS 26+ Networking	Using NetworkConnection with async/await, TLV framing, Coder protocol
Migration Guide	Moving from sockets, CFSocket, SCNetworkReachability, URLSession
Troubleshooting	Debugging timeouts, TLS failures, connection issues
Core Workflow
Choose transport (TCP/UDP/QUIC) based on use case
Create NWConnection (iOS 12+) or NetworkConnection (iOS 26+)
Set up state handler for connection lifecycle
Start connection on appropriate queue
Send/receive data with proper error handling
Handle network transitions (WiFi to cellular)
When to Use Network.framework vs URLSession
URLSession: HTTP, HTTPS, WebSocket, simple TCP/TLS streams
Network.framework: UDP, custom protocols, low-level control, peer-to-peer, gaming
Common Mistakes

Ignoring state handlers — Creating an NWConnection without a state change handler means you never learn when it's ready or failed. Always implement the state handler first.

Blocking the main thread — Never call receive() on the main queue. Use a background DispatchQueue or Task for all network operations.

Wrong queue selection — Using the wrong queue (UI queue for network work, or serial queue for concurrent reads) causes deadlocks or silent failures. Always explicit your queue choice.

Not handling network transitions — WiFi/cellular switches or network loss aren't always detected automatically. Implement viability checks and state monitoring for robust apps.

Improper error recovery — Network errors need retry logic with backoff. Immediately failing on transient errors (timeouts, temporary loss) creates poor UX.

Weekly Installs
102
Repository
johnrogers/clau…ineering
GitHub Stars
201
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass