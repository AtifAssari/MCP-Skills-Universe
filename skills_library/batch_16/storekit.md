---
title: storekit
url: https://skills.sh/johnrogers/claude-swift-engineering/storekit
---

# storekit

skills/johnrogers/claude-swift-engineering/storekit
storekit
Installation
$ npx skills add https://github.com/johnrogers/claude-swift-engineering --skill storekit
SKILL.md
StoreKit

StoreKit 2 patterns for implementing in-app purchases with async/await APIs, automatic verification, and SwiftUI integration.

Reference Loading Guide

ALWAYS load reference files if there is even a small chance the content may be required. It's better to have the context than to miss a pattern or make a mistake.

Reference	Load When
Getting Started	Setting up .storekit configuration file, testing-first workflow
Products	Loading products, product types, purchasing with Product.purchase()
Subscriptions	Auto-renewable subscriptions, subscription groups, offers, renewal tracking
Transactions	Transaction listener, verification, finishing transactions, restore purchases
StoreKit Views	ProductView, SubscriptionStoreView, SubscriptionOfferView in SwiftUI
Core Workflow
Create .storekit configuration file first (before any code)
Test purchases locally in Xcode simulator
Implement centralized StoreManager with @MainActor
Set up Transaction.updates listener at app launch
Display products with ProductView or custom UI
Always call transaction.finish() after granting entitlements
Essential Architecture
@MainActor
final class StoreManager: ObservableObject {
    @Published private(set) var products: [Product] = []
    @Published private(set) var purchasedProductIDs: Set<String> = []
    private var transactionListener: Task<Void, Never>?

    init() {
        transactionListener = listenForTransactions()
        Task { await loadProducts() }
    }
}

Common Mistakes

Missing .finish() calls on transactions — Forgetting to call transaction.finish() after granting entitlements causes transactions to never complete. The user won't see their purchase reflected. Always call finish().

Unsafe StoreManager state — Shared StoreManager without @MainActor can have race conditions. Multiple async tasks can update @Published properties concurrently, corrupting state. Use @MainActor for thread safety.

No transaction listener at app launch — Not setting up Transaction.updates listener means app crashes or misses refunded/canceled purchases. Listen for transactions immediately in @main, not when user taps purchase button.

Hardcoded product IDs — Hardcoded IDs make testing and localization hard. Use configuration files or environment variables for product IDs. Same applies to prices (fetch from App Store, don't hardcode).

Ignoring verification failures — App Store verification fails silently sometimes. Not checking verification status means accepting unverified transactions (security risk). Always verify before granting entitlements.

Weekly Installs
101
Repository
johnrogers/clau…ineering
GitHub Stars
201
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn