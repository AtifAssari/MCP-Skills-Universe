---
title: axiom-storekit-ref
url: https://skills.sh/charleswiltgen/axiom/axiom-storekit-ref
---

# axiom-storekit-ref

skills/charleswiltgen/axiom/axiom-storekit-ref
axiom-storekit-ref
Installation
$ npx skills add https://github.com/charleswiltgen/axiom --skill axiom-storekit-ref
SKILL.md
StoreKit 2 — Complete API Reference
Overview

StoreKit 2 is Apple's modern in-app purchase framework with async/await APIs, automatic receipt validation, and SwiftUI integration. This reference covers every API, iOS 18.4 enhancements, and comprehensive WWDC 2025 code examples.

Product Types Supported

Consumable:

Products that can be purchased multiple times
Examples: coins, hints, temporary boosts
Do NOT restore on new devices

Non-Consumable:

Products purchased once, owned forever
Examples: premium features, level packs, remove ads
MUST restore on new devices

Auto-Renewable Subscription:

Subscriptions that renew automatically
Organized into subscription groups
MUST restore on new devices
Support: free trials, intro offers, promotional offers, win-back offers

Non-Renewing Subscription:

Fixed duration subscriptions (no auto-renewal)
Examples: seasonal passes
MUST restore on new devices
Key Improvements Over StoreKit 1
Async/Await: Modern concurrency instead of delegates/closures
Automatic Verification: JSON Web Signature (JWS) verification built-in
Transaction Types: Strong Swift types instead of SKPaymentTransaction
Testing: StoreKit configuration files for local testing
SwiftUI Views: Pre-built purchase UIs (ProductView, SubscriptionStoreView)
Server APIs: App Store Server API and Server Notifications
When to Use This Reference

Use this reference when:

Implementing in-app purchases with StoreKit 2
Understanding new iOS 18.4 fields (appTransactionID, offerPeriod, etc.)
Looking up specific API signatures and parameters
Planning subscription architecture
Debugging transaction issues
Implementing StoreKit Views
Integrating with App Store Server APIs

Related Skills:

axiom-in-app-purchases — Discipline skill with testing-first workflow, architecture patterns
(Future: iap-auditor agent for auditing existing IAP code)
(Future: iap-implementation agent for implementing IAP from scratch)
Product
Overview

Product represents an in-app purchase item configured in App Store Connect or StoreKit configuration file.

Loading Products

Basic Loading:

import StoreKit

let productIDs = [
    "com.app.coins_100",
    "com.app.premium",
    "com.app.pro_monthly"
]

let products = try await Product.products(for: productIDs)

From WWDC 2021-10114

Handling Missing Products:

let products = try await Product.products(for: productIDs)

// Check what loaded
let loadedIDs = Set(products.map { $0.id })
let missingIDs = Set(productIDs).subtracting(loadedIDs)

if !missingIDs.isEmpty {
    print("Missing products: \(missingIDs)")
    // Products not configured in App Store Connect or .storekit file
}

Product Properties

Basic Properties:

let product: Product

product.id // "com.app.premium"
product.displayName // "Premium Upgrade"
product.description // "Unlock all features"
product.displayPrice // "$4.99"
product.price // Decimal(4.99)
product.type // .nonConsumable


Product Type Enum:

switch product.type {
case .consumable:
    // Coins, hints, boosts
case .nonConsumable:
    // Premium features, level packs
case .autoRenewable:
    // Monthly/annual subscriptions
case .nonRenewing:
    // Seasonal passes
@unknown default:
    break
}

Subscription-Specific Properties

Check if Product is Subscription:

if let subscriptionInfo = product.subscription {
    // Product is auto-renewable subscription
    let groupID = subscriptionInfo.subscriptionGroupID
    let period = subscriptionInfo.subscriptionPeriod
}


Subscription Period:

let period = product.subscription?.subscriptionPeriod

switch period?.unit {
case .day:
    print("\(period?.value ?? 0) days")
case .week:
    print("\(period?.value ?? 0) weeks")
case .month:
    print("\(period?.value ?? 0) months")
case .year:
    print("\(period?.value ?? 0) years")
default:
    break
}


Introductory Offer:

if let introOffer = product.subscription?.introductoryOffer {
    print("Free trial: \(introOffer.period.value) \(introOffer.period.unit)")
    print("Price: \(introOffer.displayPrice)")

    switch introOffer.paymentMode {
    case .freeTrial:
        print("Free trial - no charge")
    case .payAsYouGo:
        print("Discounted price per period")
    case .payUpFront:
        print("One-time discounted price")
    @unknown default:
        break
    }
}


Promotional Offers:

let offers = product.subscription?.promotionalOffers ?? []

for offer in offers {
    print("Offer ID: \(offer.id)")
    print("Price: \(offer.displayPrice)")
    print("Period: \(offer.period.value) \(offer.period.unit)")
}

Purchase Methods

Purchase with UI Context (iOS 18.2+):

let product: Product
let scene: UIWindowScene

let result = try await product.purchase(confirmIn: scene)

From WWDC 2025-241:9:32

Purchase with Options:

let accountToken = UUID()

let result = try await product.purchase(
    confirmIn: scene,
    options: [
        .appAccountToken(accountToken)
    ]
)

From WWDC 2025-241:11:01

Purchase with Promotional Offer (JWS Format):

let jwsSignature: String // From your server

let result = try await product.purchase(
    confirmIn: scene,
    options: [
        .promotionalOffer(offerID: "promo_winback", signature: jwsSignature)
    ]
)

From WWDC 2025-241:10:55

Purchase with Custom Intro Eligibility:

let jwsSignature: String // From your server

let result = try await product.purchase(
    confirmIn: scene,
    options: [
        .introductoryOfferEligibility(signature: jwsSignature)
    ]
)

From WWDC 2025-241:10:42

SwiftUI Purchase (Using Environment):

struct ProductView: View {
    let product: Product
    @Environment(\.purchase) private var purchase

    var body: some View {
        Button("Buy \(product.displayPrice)") {
            Task {
                do {
                    let result = try await purchase(product)
                    // Handle result
                } catch {
                    print("Purchase failed: \(error)")
                }
            }
        }
    }
}

From WWDC 2025-241:9:50
PurchaseResult

Handling Purchase Results:

let result = try await product.purchase(confirmIn: scene)

switch result {
case .success(let verificationResult):
    // Purchase succeeded - verify transaction
    guard let transaction = try? verificationResult.payloadValue else {
        print("Transaction verification failed")
        return
    }

    // Grant entitlement
    await grantEntitlement(for: transaction)
    await transaction.finish()

case .userCancelled:
    // User tapped "Cancel" in payment sheet
    print("User cancelled purchase")

case .pending:
    // Purchase requires action (Ask to Buy, payment issue)
    // Transaction will arrive via Transaction.updates when approved
    print("Purchase pending approval")

@unknown default:
    break
}

From WWDC 2025-241
Transaction
Overview

Transaction represents a successful in-app purchase. Contains purchase metadata, product ID, purchase date, and for subscriptions, expiration date.

New Fields (iOS 18.4)

appTransactionID:

let transaction: Transaction
let appTransactionID = transaction.appTransactionID
// Unique ID for app download (same across all purchases by same Apple Account)

From WWDC 2025-241:4:13

offerPeriod:

if let offerPeriod = transaction.offer?.period {
    print("Offer duration: \(offerPeriod)")
    // ISO 8601 duration format (e.g., "P1M" for 1 month)
}

From WWDC 2025-249:3:11

advancedCommerceInfo:

if let advancedInfo = transaction.advancedCommerceInfo {
    // Only present for Advanced Commerce API purchases
    // nil for standard IAP
}

From WWDC 2025-241:4:42
Essential Properties

Basic Fields:

let transaction: Transaction

transaction.id // Unique transaction ID
transaction.originalID // Original transaction ID (consistent across renewals)
transaction.productID // "com.app.pro_monthly"
transaction.productType // .autoRenewable
transaction.purchaseDate // Date of purchase
transaction.appAccountToken // UUID set at purchase time (if provided)


Subscription Fields:

transaction.expirationDate // When subscription expires
transaction.isUpgraded // true if user upgraded to higher tier
transaction.revocationDate // Date of refund (nil if not refunded)
transaction.revocationReason // .developerIssue or .other


Offer Fields:

if let offer = transaction.offer {
    offer.type // .introductory or .promotional or .code
    offer.id // Offer identifier from App Store Connect
    offer.paymentMode // .freeTrial, .payAsYouGo, .payUpFront, .oneTime
}

From WWDC 2025-241:8:00
Current Entitlements

Get All Current Entitlements:

var purchasedProductIDs: Set<String> = []

for await result in Transaction.currentEntitlements {
    guard let transaction = try? result.payloadValue else {
        continue
    }

    // Only include non-refunded transactions
    if transaction.revocationDate == nil {
        purchasedProductIDs.insert(transaction.productID)
    }
}

From WWDC 2025-241

Get Entitlements for Specific Product (iOS 18.4+):

let productID = "com.app.premium"

for await result in Transaction.currentEntitlements(for: productID) {
    if let transaction = try? result.payloadValue,
       transaction.revocationDate == nil {
        // User owns this product
        return true
    }
}

From WWDC 2025-241:3:31

Deprecated API (iOS 18.4):

// ❌ Deprecated in iOS 18.4
let entitlement = await Transaction.currentEntitlement(for: productID)

// ✅ Use this instead (returns sequence, handles Family Sharing)
for await result in Transaction.currentEntitlements(for: productID) {
    // ...
}

From WWDC 2025-241:3:31
Transaction History

Get All Transactions:

for await result in Transaction.all {
    guard let transaction = try? result.payloadValue else {
        continue
    }

    print("Transaction: \(transaction.productID) on \(transaction.purchaseDate)")
}


Get Transactions for Product:

for await result in Transaction.all(matching: productID) {
    guard let transaction = try? result.payloadValue else {
        continue
    }

    // All transactions for this product
}

Transaction Listener

Listen for Real-Time Updates (REQUIRED):

func listenForTransactions() -> Task<Void, Never> {
    Task.detached {
        for await verificationResult in Transaction.updates {
            await handleTransaction(verificationResult)
        }
    }
}

func handleTransaction(_ result: VerificationResult<Transaction>) async {
    guard let transaction = try? result.payloadValue else {
        return
    }

    // Grant or revoke entitlement
    if transaction.revocationDate != nil {
        await revokeEntitlement(for: transaction.productID)
    } else {
        await grantEntitlement(for: transaction)
    }

    // CRITICAL: Always finish transaction
    await transaction.finish()
}

From WWDC 2021-10114

Transaction Sources:

In-app purchases
Purchases from App Store (promoted IAP)
Offer code redemptions
Subscription renewals
Family Sharing transactions
Pending purchases (Ask to Buy) that complete
Refund notifications
Verification

VerificationResult:

let result: VerificationResult<Transaction>

switch result {
case .verified(let transaction):
    // ✅ Transaction signed by App Store
    await grantEntitlement(for: transaction)
    await transaction.finish()

case .unverified(let transaction, let error):
    // ❌ Transaction signature invalid
    print("Unverified: \(error)")
    // DO NOT grant entitlement
    await transaction.finish() // Still finish to clear queue
}


What Verification Checks:

Transaction signed by App Store (not fraudulent)
Transaction belongs to this app (bundle ID match)
Transaction belongs to this device
Finishing Transactions

Always Call finish():

await transaction.finish()


When to finish:

✅ After granting entitlement to user
✅ After storing transaction receipt/ID
✅ Even for unverified transactions (to clear queue)
✅ Even for refunded transactions

What happens if you don't finish:

Transaction redelivered on next app launch
Transaction.updates re-emits transaction
Queue builds up over time
AppTransaction
Overview

AppTransaction represents the original app download. Available via AppTransaction.shared.

New Fields (iOS 18.4)

appTransactionID:

let appTransaction = try await AppTransaction.shared

switch appTransaction {
case .verified(let transaction):
    let appTransactionID = transaction.appTransactionID
    // Globally unique ID for this Apple Account + app
    // Same value appears in Transaction and RenewalInfo

case .unverified(_, let error):
    print("AppTransaction verification failed: \(error)")
}

From WWDC 2025-241:1:42

originalPlatform:

if let appTransaction = try? await AppTransaction.shared.payloadValue {
    let platform = appTransaction.originalPlatform

    switch platform {
    case .iOS:
        print("Originally downloaded on iPhone/iPad")
    case .macOS:
        print("Originally downloaded on Mac")
    case .tvOS:
        print("Originally downloaded on Apple TV")
    case .visionOS:
        print("Originally downloaded on Vision Pro")
    @unknown default:
        break
    }
}

From WWDC 2025-241:2:11

Note: Apps downloaded on watchOS show originalPlatform = .iOS

Essential Properties
let appTransaction: AppTransaction

appTransaction.appVersion // "1.2.3"
appTransaction.originalAppVersion // "1.0.0"
appTransaction.originalPurchaseDate // First download date
appTransaction.bundleID // "com.company.app"
appTransaction.deviceVerification // UUID for device
appTransaction.deviceVerificationNonce // Nonce for verification

Use Cases

Check App Version:

if let appTransaction = try? await AppTransaction.shared.payloadValue {
    if appTransaction.appVersion != currentVersion {
        // Prompt user to update
    }
}

From WWDC 2025-241:0:51

Business Model Migration:

// Moving from paid app to free app with IAP
if appTransaction.originalPlatform == .iOS,
   appTransaction.originalPurchaseDate < migrationDate {
    // User paid for app before migration - grant premium
    await grantPremiumAccess()
}

From WWDC 2025-241:2:32
Product.SubscriptionInfo.RenewalInfo
Overview

RenewalInfo provides information about auto-renewable subscription renewal state, including whether it will renew, expiration reason, and upcoming offers.

New Fields (iOS 18.4)

appTransactionID:

let renewalInfo: RenewalInfo
let appTransactionID = renewalInfo.appTransactionID

From WWDC 2025-241:6:40

offerPeriod:

if let offerPeriod = renewalInfo.offerPeriod {
    print("Next renewal offer period: \(offerPeriod)")
    // ISO 8601 duration (applies at next renewal)
}

From WWDC 2025-249:3:11

appAccountToken:

if let token = renewalInfo.appAccountToken {
    // UUID associating subscription with your server account
}

From WWDC 2025-241:6:56

advancedCommerceInfo:

if let advancedInfo = renewalInfo.advancedCommerceInfo {
    // Only for Advanced Commerce API subscriptions
}

From WWDC 2025-241:6:50
Essential Properties

Renewal State:

let renewalInfo: RenewalInfo

renewalInfo.willAutoRenew // true if subscription will renew
renewalInfo.autoRenewPreference // Product ID customer will renew to
renewalInfo.expirationReason // Why subscription expired (if expired)


Expiration Reasons:

switch renewalInfo.expirationReason {
case .autoRenewDisabled:
    // User turned off auto-renewal
case .billingError:
    // Payment method issue
case .didNotConsentToPriceIncrease:
    // User didn't accept price increase - show win-back offer!
case .productUnavailable:
    // Product no longer available
case .unknown:
    // Unknown reason
@unknown default:
    break
}

From WWDC 2025-241:5:38

Grace Period:

if let gracePeriodExpiration = renewalInfo.gracePeriodExpirationDate {
    // Subscription in grace period - billing issue
    // Show update payment method UI
}


Price Increase Consent:

if let consentStatus = renewalInfo.priceIncreaseStatus {
    switch consentStatus {
    case .agreed:
        // User accepted price increase
    case .notYetResponded:
        // User hasn't responded - show consent UI
    @unknown default:
        break
    }
}

Accessing RenewalInfo

From SubscriptionStatus:

let statuses = try await Product.SubscriptionInfo.status(for: groupID)

for status in statuses {
    switch status.renewalInfo {
    case .verified(let renewalInfo):
        print("Will renew: \(renewalInfo.willAutoRenew)")
    case .unverified(_, let error):
        print("Renewal info verification failed: \(error)")
    }
}

Product.SubscriptionInfo.Status
Overview

SubscriptionStatus represents the current state of an auto-renewable subscription, including whether it's active, expired, in grace period, or in billing retry.

Subscription States

State Enum:

let status: Product.SubscriptionInfo.Status

switch status.state {
case .subscribed:
    // User has active subscription - full access

case .expired:
    // Subscription expired - show resubscribe/win-back offer

case .inGracePeriod:
    // Billing issue but access maintained - show update payment UI

case .inBillingRetryPeriod:
    // Apple retrying payment - maintain access

case .revoked:
    // Family Sharing access removed - revoke access

@unknown default:
    break
}

From WWDC 2025-241
Getting Subscription Status

For Subscription Group:

let groupID = "pro_tier"

let statuses = try await Product.SubscriptionInfo.status(for: groupID)

// Find highest service level
let activeStatus = statuses
    .filter { $0.state == .subscribed }
    .max { $0.transaction.productID < $1.transaction.productID }

From WWDC 2025-241:6:22

For Specific Transaction (iOS 18.4+):

let transactionID = transaction.id

let status = try await Product.SubscriptionInfo.status(for: transactionID)

From WWDC 2025-241:6:40

Listen for Status Updates:

for await statuses in Product.SubscriptionInfo.Status.updates(for: groupID) {
    // Process updated statuses
    for status in statuses {
        print("Status: \(status.state)")
    }
}

Status Properties
let status: Product.SubscriptionInfo.Status

status.state // .subscribed, .expired, etc.
status.transaction // VerificationResult<Transaction>
status.renewalInfo // VerificationResult<RenewalInfo>

StoreKit Views
ProductView (iOS 17+)

Basic Usage:

import StoreKit

struct ContentView: View {
    let productID = "com.app.premium"

    var body: some View {
        ProductView(id: productID)
    }
}

From WWDC 2023-10013

With Loaded Product:

struct ContentView: View {
    let product: Product

    var body: some View {
        ProductView(for: product)
    }
}


Custom Icon:

ProductView(id: productID) {
    Image(systemName: "star.fill")
        .foregroundStyle(.yellow)
}


Control Styles:

ProductView(id: productID)
    .productViewStyle(.regular)  // Default

ProductView(id: productID)
    .productViewStyle(.compact)  // Smaller

ProductView(id: productID)
    .productViewStyle(.large)  // Prominent

StoreView (iOS 17+)

Basic Store:

struct ContentView: View {
    let productIDs = [
        "com.app.coins_100",
        "com.app.coins_500",
        "com.app.coins_1000"
    ]

    var body: some View {
        StoreView(ids: productIDs)
    }
}

From WWDC 2023-10013

With Loaded Products:

struct ContentView: View {
    let products: [Product]

    var body: some View {
        StoreView(products: products)
    }
}

SubscriptionStoreView (iOS 17+)

Basic Subscription Store:

struct SubscriptionView: View {
    let groupID = "pro_tier"

    var body: some View {
        SubscriptionStoreView(groupID: groupID) {
            // Marketing content above subscription options
            VStack {
                Image("app-icon")
                Text("Go Pro")
                    .font(.largeTitle.bold())
                Text("Unlock all features")
            }
        }
    }
}

From WWDC 2023-10013

Control Style:

SubscriptionStoreView(groupID: groupID) {
    // Marketing content
}
.subscriptionStoreControlStyle(.automatic)    // Default
.subscriptionStoreControlStyle(.picker)       // Horizontal picker
.subscriptionStoreControlStyle(.buttons)      // Stacked buttons
.subscriptionStoreControlStyle(.prominentPicker) // Large picker (iOS 18.4+)

From WWDC 2025-241
SubscriptionOfferView (iOS 18.4+)

Basic Offer View:

struct ContentView: View {
    let productID = "com.app.pro_monthly"

    var body: some View {
        SubscriptionOfferView(id: productID)
    }
}

From WWDC 2025-241:14:27

With Loaded Product:

let product: Product // Already loaded via Product.products(for:)

SubscriptionOfferView(product: product)


With Promotional Icon:

SubscriptionOfferView(
    id: productID,
    prefersPromotionalIcon: true
)

// Also available as modifier
SubscriptionOfferView(id: productID)
    .prefersPromotionalIcon(true)


With Custom Icon:

SubscriptionOfferView(id: productID) {
    Image("custom-icon")
        .resizable()
        .frame(width: 60, height: 60)
} placeholder: {
    Image(systemName: "photo")
        .foregroundStyle(.gray)
}

From WWDC 2025-241:15:14

With Detail Action:

@State private var showStore = false

var body: some View {
    SubscriptionOfferView(id: productID)
        .subscriptionOfferViewDetailAction {
            showStore = true
        }
        .sheet(isPresented: $showStore) {
            SubscriptionStoreView(groupID: "pro_tier")
        }
}

From WWDC 2025-241:15:38

Visible Relationship:

// Only show if customer can upgrade
SubscriptionOfferView(
    groupID: "pro_tier",
    visibleRelationship: .upgrade
)

// Only show if customer can downgrade
SubscriptionOfferView(
    groupID: "pro_tier",
    visibleRelationship: .downgrade
)

// Show crossgrade options (same tier, different billing period)
SubscriptionOfferView(
    groupID: "pro_tier",
    visibleRelationship: .crossgrade
)

// Show current subscription (only if offer available)
SubscriptionOfferView(
    groupID: "pro_tier",
    visibleRelationship: .current
)

// Show any plan in group
SubscriptionOfferView(
    groupID: "pro_tier",
    visibleRelationship: .all
)

From WWDC 2025-241:17:44

With App Icon:

SubscriptionOfferView(
    groupID: groupID,
    visibleRelationship: .all,
    useAppIcon: true
)

From WWDC 2025-241:19:06
Offer Modifiers

Promotional Offer (JWS):

SubscriptionStoreView(groupID: groupID)
    .subscriptionPromotionalOffer(
        for: { subscription in
            // Return offer for this subscription
            return subscription.promotionalOffers.first
        },
        signature: { subscription, offer in
            // Get JWS signature from server
            let signature = try await server.signOffer(
                productID: subscription.id,
                offerID: offer.id
            )
            return signature
        }
    )

From WWDC 2025-241:12:17
subscriptionStatusTask Modifier (iOS 18.4+)

Track subscription status at the app level with a SwiftUI modifier. Eliminates manual polling by reacting to status changes automatically.

Basic Usage:

@main
struct MyApp: App {
    @State private var customerStatus: CustomerStatus = .unknown

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(\.customerSubscriptionStatus, customerStatus)
                .subscriptionStatusTask(for: "your.group.id") { statuses in
                    if statuses.contains(where: { $0.state == .subscribed }) {
                        customerStatus = .subscribed
                    } else if statuses.contains(where: { $0.state == .expired }) {
                        customerStatus = .expired
                    } else {
                        customerStatus = .notSubscribed
                    }
                }
        }
    }
}


Key behavior:

Fires on app launch with current statuses
Fires again when subscription status changes (renewal, expiration, upgrade)
Translate StoreKit statuses to your app's model — keep your domain model simple
Attach at the top of your view hierarchy (App or root WindowGroup)
Offer Codes (iOS 18.2+)
Overview

Offer codes now support all product types (previously subscription-only):

Consumables
Non-consumables
Non-renewing subscriptions
Auto-renewable subscriptions
Redeem in App

UIKit:

func showOfferCodeSheet() {
    guard let scene = view.window?.windowScene else { return }

    StoreKit.AppStore.presentOfferCodeRedeemSheet(in: scene)
}

From WWDC 2025-241:7:38

SwiftUI:

.offerCodeRedemption(isPresented: $showRedeemSheet)

Payment Mode

New: .oneTime:

let transaction: Transaction

if let offer = transaction.offer {
    switch offer.paymentMode {
    case .freeTrial:
        // No charge during offer period
    case .payAsYouGo:
        // Discounted price per billing period
    case .payUpFront:
        // One-time discounted price for entire duration
    case .oneTime:
        // ✨ New: One-time offer code redemption (iOS 17.2+)
    @unknown default:
        break
    }
}

From WWDC 2025-241:8:17

Legacy Access (iOS 15-17.1):

if let offerMode = transaction.offerPaymentModeStringRepresentation {
    // String representation for older OS versions
    print(offerMode) // "oneTime"
}

From WWDC 2025-241:8:49
App Store Server Library
Overview

Open-source library for signing IAP requests and decoding server API responses. Available in Swift, Java, Python, Node.js.

Create Promotional Offer Signature

Swift Example:

import AppStoreServerLibrary

// Configure signing
let signingKey = "YOUR_PRIVATE_KEY"
let keyID = "YOUR_KEY_ID"
let issuerID = "YOUR_ISSUER_ID"
let bundleID = "com.app.bundle"

let creator = PromotionalOfferV2SignatureCreator(
    privateKey: signingKey,
    keyID: keyID,
    issuerID: issuerID,
    bundleID: bundleID
)

// Create signature
let productID = "com.app.pro_monthly"
let offerID = "promo_winback"
let transactionID = transaction.id // Optional but recommended

let signature = try creator.createSignature(
    productIdentifier: productID,
    subscriptionOfferIdentifier: offerID,
    applicationUsername: nil,
    nonce: UUID(),
    timestamp: Date().timeIntervalSince1970,
    transactionIdentifier: transactionID
)

// Send signature to app
return signature // Compact JWS string

From WWDC 2025-241:12:44, 2025-249

Server Endpoint Example:

app.get("promo-offer") { req async throws -> String in
    let productID = try req.query.get(String.self, at: "productID")
    let offerID = try req.query.get(String.self, at: "offerID")

    let signature = try creator.createSignature(
        productIdentifier: productID,
        subscriptionOfferIdentifier: offerID,
        transactionIdentifier: nil
    )

    return signature
}

From WWDC 2025-241:12:52
App Store Server API
Set App Account Token

Endpoint:

PATCH /inApps/v1/transactions/{originalTransactionId}


Request Body:

{
  "appAccountToken": "550e8400-e29b-41d4-a716-446655440000"
}


Usage:

Set appAccountToken for purchases made outside your app (offer codes, App Store)
Update appAccountToken when account ownership changes
Associates transaction with customer account on your server
From WWDC 2025-249:5:19
Get App Transaction Info

Endpoint:

GET /inApps/v2/appTransaction/{transactionId}


Response:

{
  "signedAppTransactionInfo": "eyJhbGc..."
}


Usage:

Get app download information on server
Check app version, platform, environment
Available later in 2025
From WWDC 2025-249:10:48
Send Consumption Information V2

Endpoint:

PUT /inApps/v2/transactions/consumption/{transactionId}


Request Body:

{
  "customerConsented": true,
  "sampleContentProvided": false,
  "deliveryStatus": "DELIVERED",
  "refundPreference": "GRANT_PRORATED",
  "consumptionPercentage": 25000
}


Fields:

customerConsented (required): User consented to send consumption data
sampleContentProvided (optional): Sample provided before purchase
deliveryStatus (required): "DELIVERED" or various UNDELIVERED statuses
refundPreference (optional): "NO_REFUND", "GRANT_REFUND", "GRANT_PRORATED"
consumptionPercentage (optional): 0-100000 (millipercent, e.g., 25000 = 25%)

Prorated Refund:

New in 2025
Supports partial consumption (consumables, non-consumables, non-renewing)
For auto-renewable subscriptions, App Store calculates based on time remaining
From WWDC 2025-249:16:09
Refund Notifications

REFUND Notification:

{
  "notificationType": "REFUND",
  "data": {
    "signedTransactionInfo": "...",
    "refundPercentage": 75,
    "revocationType": "REFUND_PRORATED"
  }
}


revocationType Values:

REFUND_FULL: 100% refund - revoke all access
REFUND_PRORATED: Partial refund - revoke proportional access
FAMILY_REVOKE: Family Sharing removed - revoke access
From WWDC 2025-249:20:17
Edge Cases
Family Sharing

Detect Family Shared Transactions:

// appAccountToken is NOT available for family shared transactions
let transaction: Transaction

if transaction.appAccountToken == nil {
    // Might be family shared (or appAccountToken not set)
    // Check ownershipType (if available)
}


Subscription Status for Family Sharing:

// Each family member has unique appTransactionID
// Use appTransactionID to identify individual family members

From WWDC 2025-241:1:54
Refunds

Handle Refund:

func handleTransaction(_ transaction: Transaction) async {
    if let revocationDate = transaction.revocationDate {
        // Transaction was refunded
        print("Refunded on \(revocationDate)")

        switch transaction.revocationReason {
        case .developerIssue:
            // Refund due to app issue
        case .other:
            // Other refund reason
        @unknown default:
            break
        }

        // Revoke entitlement
        await revokeEntitlement(for: transaction.productID)
    }
}

Advanced Commerce API

The Advanced Commerce API enables support for:

In-app purchases for large content catalogs
Creator experiences (tipping, patronage)
Subscriptions with optional add-ons

Check if Transaction Uses Advanced Commerce:

if transaction.advancedCommerceInfo != nil {
    // Transaction from Advanced Commerce API
    // Large catalogs, creator experiences, subscriptions with add-ons
}


Accessible through the advancedCommerceInfo field on both Transaction and RenewalInfo. Returns nil for standard IAP transactions.

From WWDC 2025-241:4:51
Win-Back Offers

Show Win-Back for Expired Subscription:

let renewalInfo: RenewalInfo

if renewalInfo.expirationReason == .didNotConsentToPriceIncrease {
    // Perfect time for win-back offer!
    SubscriptionOfferView(
        groupID: groupID,
        visibleRelationship: .current
    )
    .preferredSubscriptionOffer(offer: winBackOffer)
}

From WWDC 2025-241:5:38
Testing
StoreKit Configuration File

Create:

Xcode → File → New → StoreKit Configuration File
Add products (consumables, non-consumables, subscriptions)
Configure prices, images, descriptions

Enable in Scheme:

Scheme → Edit Scheme → Run → Options
StoreKit Configuration: Select .storekit file

Test Scenarios:

Successful purchases
Cancelled purchases
Subscription renewals (accelerated time)
Subscription expirations
Upgrades/downgrades
Offer code redemptions
Family Sharing (enable in config file)
Transaction Manager

Use the Transaction Manager window in Xcode to inspect and manipulate transactions during testing:

Create transactions manually (test specific purchase flows)
Modify transaction properties (expiration, renewal state)
Test subscription offer scenarios
Inspect transaction details and verification status

Open: Debug → StoreKit → Manage Transactions (while running with StoreKit configuration)

Sandbox Testing

Create Sandbox Account:

App Store Connect → Users and Access → Sandbox Testers
Create test Apple ID
Sign in on device Settings → App Store → Sandbox Account

Clear Purchase History:

Settings → App Store → Sandbox Account → Clear Purchase History
Migration from StoreKit 1
Key Changes

Delegates → Async/Await:

// StoreKit 1
class StoreObserver: NSObject, SKPaymentTransactionObserver {
    func paymentQueue(_ queue: SKPaymentQueue, updatedTransactions transactions: [SKPaymentTransaction]) {
        // Handle transactions
    }
}

// StoreKit 2
for await result in Transaction.updates {
    // Handle transactions
}


Receipt → Transaction:

// StoreKit 1
let receiptURL = Bundle.main.appStoreReceiptURL
let receipt = try Data(contentsOf: receiptURL!)

// StoreKit 2
let transaction: Transaction // Automatically verified!


Products → Product.products(for:):

// StoreKit 1
let request = SKProductsRequest(productIdentifiers: Set(productIDs))
request.delegate = self
request.start()

// StoreKit 2
let products = try await Product.products(for: productIDs)

Resources

WWDC: 2025-241, 2025-249, 2024-10061, 2024-10062, 2024-10110, 2023-10013, 2023-10140, 2022-10007, 2022-110404, 2021-10114

Docs: /storekit

Skills: axiom-in-app-purchases

Quick Reference
Product Types
.consumable - Can purchase multiple times (coins, boosts)
.nonConsumable - Purchase once, own forever (premium, level packs)
.autoRenewable - Auto-renewing subscriptions
.nonRenewing - Fixed duration subscriptions
Transaction States
success - Purchase completed
userCancelled - User tapped cancel
pending - Requires action (Ask to Buy)
Subscription States
.subscribed - Active subscription
.expired - Subscription ended
.inGracePeriod - Billing issue, access maintained
.inBillingRetryPeriod - Apple retrying payment
.revoked - Family Sharing removed
Essential Calls
// Load products
try await Product.products(for: productIDs)

// Purchase
try await product.purchase(confirmIn: scene)

// Current entitlements
Transaction.currentEntitlements(for: productID)

// Transaction listener
Transaction.updates

// Subscription status
Product.SubscriptionInfo.status(for: groupID)

// Restore purchases
try await AppStore.sync()

// Finish transaction (REQUIRED)
await transaction.finish()

Weekly Installs
183
Repository
charleswiltgen/axiom
GitHub Stars
881
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn