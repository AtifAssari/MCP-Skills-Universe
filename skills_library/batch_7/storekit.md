---
title: storekit
url: https://skills.sh/dpearson2699/swift-ios-skills/storekit
---

# storekit

skills/dpearson2699/swift-ios-skills/storekit
storekit
Installation
$ npx skills add https://github.com/dpearson2699/swift-ios-skills --skill storekit
Summary

Modern StoreKit 2 implementation for in-app purchases, subscriptions, and paywalls on iOS 16+.

Covers all product types (consumable, non-consumable, auto-renewable, non-renewing) with purchase flows, transaction verification, and entitlement checking
Provides SubscriptionStoreView and StoreView for building paywalls with automatic product loading, localized pricing, and purchase UI
Includes Transaction.updates listener pattern for handling mid-session changes, Family Sharing, Ask to Buy approvals, refunds, and subscription renewals
Details subscription status checking, renewal states, restore purchases, and app transaction verification for detecting tampered installations
Contains 10 common mistakes (missing listeners, unfinished transactions, unverified data, deprecated APIs) with corrected code examples and a pre-submission review checklist
SKILL.md
StoreKit 2 In-App Purchases and Subscriptions

Implement in-app purchases, subscriptions, and paywalls using StoreKit 2 on iOS 26+. Use the modern Product, Transaction, StoreView, and SubscriptionStoreView APIs. Avoid the older original StoreKit APIs (SKProduct, SKPaymentQueue, SKStoreReviewController).

Contents
Product Types
Loading Products
Purchase Flow
Transaction.updates Listener
Entitlement Checking
SubscriptionStoreView (iOS 17+)
StoreView (iOS 17+)
Subscription Status Checking
Restore Purchases
App Transaction (App Purchase Verification)
Purchase Options
SwiftUI Purchase Callbacks
Common Mistakes
Review Checklist
References
Product Types
Type	Enum Case	Behavior
Consumable	.consumable	Used once, can be repurchased (gems, coins)
Non-consumable	.nonConsumable	Purchased once permanently (premium unlock)
Auto-renewable	.autoRenewable	Recurring billing with automatic renewal
Non-renewing	.nonRenewing	Time-limited access without automatic renewal
Loading Products

Define product IDs as constants. Fetch products with Product.products(for:).

import StoreKit

enum ProductID {
    static let premium = "com.myapp.premium"
    static let gems100 = "com.myapp.gems100"
    static let monthlyPlan = "com.myapp.monthly"
    static let yearlyPlan = "com.myapp.yearly"
    static let all: [String] = [premium, gems100, monthlyPlan, yearlyPlan]
}

let products = try await Product.products(for: ProductID.all)
for product in products {
    print("\(product.displayName): \(product.displayPrice)")
}

Purchase Flow

Call product.purchase(options:) and handle all three PurchaseResult cases. Always verify and finish transactions.

func purchase(_ product: Product) async throws {
    let result = try await product.purchase(options: [
        .appAccountToken(userAccountToken)
    ])
    switch result {
    case .success(let verification):
        let transaction = try checkVerified(verification)
        await deliverContent(for: transaction)
        await transaction.finish()
    case .userCancelled:
        break
    case .pending:
        // Ask to Buy or deferred approval -- do not unlock content yet
        break
    @unknown default:
        break
    }
}

func checkVerified<T>(_ result: VerificationResult<T>) throws -> T {
    switch result {
    case .verified(let value): return value
    case .unverified(_, let error): throw error
    }
}

Transaction.updates Listener

Start at app launch. Catches purchases from other devices, Family Sharing changes, renewals, Ask to Buy approvals, refunds, and revocations.

@main
struct MyApp: App {
    private var transactionListener: Task<Void, Error>?

    init() {
        transactionListener = listenForTransactions()
    }

    var body: some Scene {
        WindowGroup { ContentView() }
    }

    func listenForTransactions() -> Task<Void, Error> {
        Task.detached {
            for await result in Transaction.updates {
                guard case .verified(let transaction) = result else { continue }
                await StoreManager.shared.updateEntitlements()
                await transaction.finish()
            }
        }
    }
}

Entitlement Checking

Use Transaction.currentEntitlements for non-consumable purchases and active subscriptions. Always check revocationDate.

@Observable
@MainActor
class StoreManager {
    static let shared = StoreManager()
    var purchasedProductIDs: Set<String> = []
    var isPremium: Bool { purchasedProductIDs.contains(ProductID.premium) }

    func updateEntitlements() async {
        var purchased = Set<String>()
        for await result in Transaction.currentEntitlements {
            if case .verified(let transaction) = result,
               transaction.revocationDate == nil {
                purchased.insert(transaction.productID)
            }
        }
        purchasedProductIDs = purchased
    }
}

SwiftUI .currentEntitlementTask Modifier
struct PremiumGatedView: View {
    @State private var state: EntitlementTaskState<VerificationResult<Transaction>?> = .loading

    var body: some View {
        Group {
            switch state {
            case .loading: ProgressView()
            case .failure: PaywallView()
            case .success(let transaction):
                if transaction != nil { PremiumContentView() }
                else { PaywallView() }
            }
        }
        .currentEntitlementTask(for: ProductID.premium) { state in
            self.state = state
        }
    }
}

SubscriptionStoreView (iOS 17+)

Built-in SwiftUI view for subscription paywalls. Handles product loading, purchase UI, and restore purchases automatically.

SubscriptionStoreView(groupID: "YOUR_GROUP_ID")
    .subscriptionStoreControlStyle(.prominentPicker)
    .subscriptionStoreButtonLabel(.multiline)
    .storeButton(.visible, for: .restorePurchases)
    .storeButton(.visible, for: .redeemCode)
    .subscriptionStorePolicyDestination(url: termsURL, for: .termsOfService)
    .subscriptionStorePolicyDestination(url: privacyURL, for: .privacyPolicy)
    .onInAppPurchaseCompletion { product, result in
        if case .success(.verified(let transaction)) = result {
            await transaction.finish()
        }
    }

Custom Marketing Content
SubscriptionStoreView(groupID: "YOUR_GROUP_ID") {
    VStack {
        Image(systemName: "crown.fill").font(.system(size: 60)).foregroundStyle(.yellow)
        Text("Unlock Premium").font(.largeTitle.bold())
        Text("Access all features").foregroundStyle(.secondary)
    }
}
.containerBackground(.blue.gradient, for: .subscriptionStore)

Hierarchical Layout
SubscriptionStoreView(groupID: "YOUR_GROUP_ID") {
    SubscriptionPeriodGroupSet()
}
.subscriptionStoreControlStyle(.picker)

StoreView (iOS 17+)

Merchandises multiple products with localized names, prices, and purchase buttons.

StoreView(ids: [ProductID.gems100, ProductID.premium], prefersPromotionalIcon: true)
    .productViewStyle(.large)
    .storeButton(.visible, for: .restorePurchases)
    .onInAppPurchaseCompletion { product, result in
        if case .success(.verified(let transaction)) = result {
            await transaction.finish()
        }
    }

ProductView for Individual Products
ProductView(id: ProductID.premium) { iconPhase in
    switch iconPhase {
    case .success(let image): image.resizable().scaledToFit()
    case .loading: ProgressView()
    default: Image(systemName: "star.fill")
    }
}
.productViewStyle(.large)

Subscription Status Checking
func checkSubscriptionActive(groupID: String) async throws -> Bool {
    let statuses = try await Product.SubscriptionInfo.Status.status(for: groupID)
    for status in statuses {
        guard case .verified = status.renewalInfo,
              case .verified = status.transaction else { continue }
        if status.state == .subscribed || status.state == .inGracePeriod {
            return true
        }
    }
    return false
}

Renewal States
State	Meaning
.subscribed	Active subscription
.expired	Subscription has expired
.inBillingRetryPeriod	Payment failed, Apple is retrying
.inGracePeriod	Payment failed but access continues during grace period
.revoked	Apple refunded or revoked the subscription
Restore Purchases

StoreKit 2 handles restoration via Transaction.currentEntitlements. Add a restore button or call AppStore.sync() explicitly.

func restorePurchases() async throws {
    try await AppStore.sync()
    await StoreManager.shared.updateEntitlements()
}


On store views: .storeButton(.visible, for: .restorePurchases)

App Transaction (App Purchase Verification)

Verify the legitimacy of the app installation. Use for business model changes or detecting tampered installations (iOS 16+).

func verifyAppPurchase() async {
    do {
        let result = try await AppTransaction.shared
        switch result {
        case .verified(let appTransaction):
            let originalVersion = appTransaction.originalAppVersion
            let purchaseDate = appTransaction.originalPurchaseDate
            // Migration logic for users who paid before subscription model
        case .unverified:
            // Potentially tampered -- restrict features as appropriate
            break
        }
    } catch { /* Could not retrieve app transaction */ }
}

Purchase Options
// App account token for server-side reconciliation
try await product.purchase(options: [.appAccountToken(UUID())])

// Consumable quantity
try await product.purchase(options: [.quantity(5)])

// Simulate Ask to Buy in sandbox
try await product.purchase(options: [.simulatesAskToBuyInSandbox(true)])

SwiftUI Purchase Callbacks
.onInAppPurchaseStart { product in
    return true  // Return false to cancel
}
.onInAppPurchaseCompletion { product, result in
    if case .success(.verified(let transaction)) = result {
        await transaction.finish()
    }
}
.inAppPurchaseOptions { product in
    [.appAccountToken(userAccountToken)]
}

Common Mistakes
1. Not starting Transaction.updates at app launch
// WRONG: No listener -- misses renewals, refunds, Ask to Buy approvals
@main struct MyApp: App {
    var body: some Scene { WindowGroup { ContentView() } }
}
// CORRECT: Start listener in App init (see Transaction.updates section above)

2. Forgetting transaction.finish()
// WRONG: Never finished -- reappears in unfinished queue forever
let transaction = try checkVerified(verification)
unlockFeature(transaction.productID)

// CORRECT: Always finish after delivering content
let transaction = try checkVerified(verification)
unlockFeature(transaction.productID)
await transaction.finish()

3. Ignoring verification result
// WRONG: Using unverified transaction -- security risk
let transaction = verification.unsafePayloadValue

// CORRECT: Verify before using
let transaction = try checkVerified(verification)

4. Using legacy original StoreKit APIs
// AVOID: Original StoreKit (legacy)
let request = SKProductsRequest(productIdentifiers: ["com.app.premium"])
SKPaymentQueue.default().add(payment)
SKStoreReviewController.requestReview()

// PREFERRED: StoreKit 2
let products = try await Product.products(for: ["com.app.premium"])
let result = try await product.purchase()
try await AppStore.requestReview(in: windowScene)

5. Not checking revocationDate
// WRONG: Grants access to refunded purchases
if case .verified(let transaction) = result {
    purchased.insert(transaction.productID)
}

// CORRECT: Skip revoked transactions
if case .verified(let transaction) = result, transaction.revocationDate == nil {
    purchased.insert(transaction.productID)
}

6. Hardcoding prices
// WRONG: Wrong for other currencies and regions
Text("Buy Premium for $4.99")

// CORRECT: Localized price from Product
Text("Buy \(product.displayName) for \(product.displayPrice)")

7. Not handling .pending purchase result
// WRONG: Silently drops pending Ask to Buy
default: break

// CORRECT: Inform user purchase is awaiting approval
case .pending:
    showPendingApprovalMessage()

8. Checking entitlements only once at launch
// WRONG: Check once, never update
func appDidFinish() { Task { await updateEntitlements() } }

// CORRECT: Re-check on Transaction.updates AND on foreground return
// Transaction.updates listener handles mid-session changes.
// Also use .task { await storeManager.updateEntitlements() } on content views.

9. Missing restore purchases button
// WRONG: No restore option -- App Store rejection risk
SubscriptionStoreView(groupID: "group_id")

// CORRECT
SubscriptionStoreView(groupID: "group_id")
    .storeButton(.visible, for: .restorePurchases)

10. Subscription views without policy links
// WRONG: No terms or privacy policy
SubscriptionStoreView(groupID: "group_id")

// CORRECT
SubscriptionStoreView(groupID: "group_id")
    .subscriptionStorePolicyDestination(url: termsURL, for: .termsOfService)
    .subscriptionStorePolicyDestination(url: privacyURL, for: .privacyPolicy)

Review Checklist
 Transaction.updates listener starts at app launch in App init
 All transactions verified before granting access
 transaction.finish() called after content delivery
 Revoked transactions excluded from entitlements
 .pending purchase result handled for Ask to Buy
 Restore purchases button visible on paywall and store views
 Terms of Service and Privacy Policy links on subscription views
 Prices shown using product.displayPrice, never hardcoded
 Subscription terms (price, duration, renewal) clearly displayed
 Free trial states post-trial pricing clearly
 No original StoreKit APIs (SKProduct, SKPaymentQueue)
 Product IDs defined as constants, not scattered strings
 StoreKit configuration file set up for testing
 Entitlements re-checked on Transaction.updates and app foreground
 Server-side validation uses jwsRepresentation if applicable
 Consumables delivered and finished promptly
 Transaction observer types and product model types are Sendable when shared across concurrency boundaries
References
See references/app-review-guidelines.md for IAP rules (Guideline 3.1.1), subscription display requirements, and rejection prevention.
See references/storekit-advanced.md for subscription control styles, offer management, testing patterns, and advanced subscription handling.
Weekly Installs
1.2K
Repository
dpearson2699/sw…s-skills
GitHub Stars
512
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn