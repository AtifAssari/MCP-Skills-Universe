---
title: swift-codable
url: https://skills.sh/dpearson2699/swift-ios-skills/swift-codable
---

# swift-codable

skills/dpearson2699/swift-ios-skills/swift-codable
swift-codable
Installation
$ npx skills add https://github.com/dpearson2699/swift-ios-skills --skill swift-codable
SKILL.md
Swift Codable

Encode and decode Swift types using Codable (Encodable & Decodable) with JSONEncoder, JSONDecoder, and related APIs. Targets Swift 6.3 / iOS 26+.

Contents
Basic Conformance
Custom CodingKeys
Custom Decoding and Encoding
Nested and Flattened Containers
Heterogeneous Arrays
Date Decoding Strategies
Data and Key Strategies
Lossy Array Decoding
Single Value Containers
Default Values for Missing Keys
Encoder and Decoder Configuration
Codable with URLSession
Codable with SwiftData
Codable with UserDefaults
Common Mistakes
Review Checklist
References
Basic Conformance

When all stored properties are themselves Codable, the compiler synthesizes conformance automatically:

struct User: Codable {
    let id: Int
    let name: String
    let email: String
    let isVerified: Bool
}

let user = try JSONDecoder().decode(User.self, from: jsonData)
let encoded = try JSONEncoder().encode(user)


Prefer Decodable for read-only API responses and Encodable for write-only. Use Codable only when both directions are required.

Custom CodingKeys

Rename JSON keys without writing a custom decoder by declaring a CodingKeys enum:

struct Product: Codable {
    let id: Int
    let displayName: String
    let imageURL: URL
    let priceInCents: Int

    enum CodingKeys: String, CodingKey {
        case id
        case displayName = "display_name"
        case imageURL = "image_url"
        case priceInCents = "price_in_cents"
    }
}


Every stored property must appear in the enum. Omitting a property from CodingKeys excludes it from encoding/decoding -- provide a default value or compute it separately.

Custom Decoding and Encoding

Override init(from:) and encode(to:) for transformations the synthesized conformance cannot handle:

struct Event: Codable {
    let name: String
    let timestamp: Date
    let tags: [String]

    enum CodingKeys: String, CodingKey {
        case name, timestamp, tags
    }

    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        name = try container.decode(String.self, forKey: .name)
        // Decode Unix timestamp as Double, convert to Date
        let epoch = try container.decode(Double.self, forKey: .timestamp)
        timestamp = Date(timeIntervalSince1970: epoch)
        // Default to empty array when key is missing
        tags = try container.decodeIfPresent([String].self, forKey: .tags) ?? []
    }

    func encode(to encoder: Encoder) throws {
        var container = encoder.container(keyedBy: CodingKeys.self)
        try container.encode(name, forKey: .name)
        try container.encode(timestamp.timeIntervalSince1970, forKey: .timestamp)
        try container.encode(tags, forKey: .tags)
    }
}

Nested and Flattened Containers

Use nestedContainer(keyedBy:forKey:) to navigate and flatten nested JSON:

// JSON: { "id": 1, "location": { "lat": 37.7749, "lng": -122.4194 } }
struct Place: Decodable {
    let id: Int
    let latitude: Double
    let longitude: Double

    enum CodingKeys: String, CodingKey { case id, location }
    enum LocationKeys: String, CodingKey { case lat, lng }

    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        id = try container.decode(Int.self, forKey: .id)
        let location = try container.nestedContainer(
            keyedBy: LocationKeys.self, forKey: .location)
        latitude = try location.decode(Double.self, forKey: .lat)
        longitude = try location.decode(Double.self, forKey: .lng)
    }
}


Chain multiple nestedContainer calls to flatten deeply nested structures. Also use nestedUnkeyedContainer(forKey:) for nested arrays.

Heterogeneous Arrays

Decode arrays of mixed types using a discriminator field:

// JSON: [{"type":"text","content":"Hello"},{"type":"image","url":"pic.jpg"}]
enum ContentBlock: Decodable {
    case text(String)
    case image(URL)

    enum CodingKeys: String, CodingKey { case type, content, url }

    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        let type = try container.decode(String.self, forKey: .type)
        switch type {
        case "text":
            let content = try container.decode(String.self, forKey: .content)
            self = .text(content)
        case "image":
            let url = try container.decode(URL.self, forKey: .url)
            self = .image(url)
        default:
            throw DecodingError.dataCorruptedError(
                forKey: .type, in: container,
                debugDescription: "Unknown type: \(type)")
        }
    }
}

let blocks = try JSONDecoder().decode([ContentBlock].self, from: jsonData)

Date Decoding Strategies

Configure JSONDecoder.dateDecodingStrategy to match your API:

let decoder = JSONDecoder()

// ISO 8601 (e.g., "2024-03-15T10:30:00Z")
decoder.dateDecodingStrategy = .iso8601

// Unix timestamp in seconds (e.g., 1710499800)
decoder.dateDecodingStrategy = .secondsSince1970

// Custom DateFormatter
let formatter = DateFormatter()
formatter.dateFormat = "yyyy-MM-dd"
formatter.locale = Locale(identifier: "en_US_POSIX")
formatter.timeZone = TimeZone(secondsFromGMT: 0)
decoder.dateDecodingStrategy = .formatted(formatter)

// Custom closure for multiple formats
decoder.dateDecodingStrategy = .custom { decoder in
    let container = try decoder.singleValueContainer()
    let string = try container.decode(String.self)
    if let date = ISO8601DateFormatter().date(from: string) { return date }
    throw DecodingError.dataCorruptedError(
        in: container, debugDescription: "Cannot decode date: \(string)")
}


Set the matching strategy on JSONEncoder: encoder.dateEncodingStrategy = .iso8601

Data and Key Strategies
let decoder = JSONDecoder()
decoder.dataDecodingStrategy = .base64           // Base64-encoded Data fields
decoder.keyDecodingStrategy = .convertFromSnakeCase  // snake_case -> camelCase
// {"user_name": "Alice"} maps to `var userName: String` -- no CodingKeys needed

let encoder = JSONEncoder()
encoder.dataEncodingStrategy = .base64
encoder.keyEncodingStrategy = .convertToSnakeCase

Lossy Array Decoding

By default, one invalid element fails the entire array. Use a wrapper to skip invalid elements:

struct LossyArray<Element: Decodable>: Decodable {
    let elements: [Element]

    init(from decoder: Decoder) throws {
        var container = try decoder.unkeyedContainer()
        var elements: [Element] = []
        while !container.isAtEnd {
            if let element = try? container.decode(Element.self) {
                elements.append(element)
            } else {
                _ = try? container.decode(AnyCodableValue.self) // advance past bad element
            }
        }
        self.elements = elements
    }
}
private struct AnyCodableValue: Decodable {}

Single Value Containers

Wrap primitives for type safety using singleValueContainer():

struct UserID: Codable, Hashable {
    let rawValue: String

    init(_ rawValue: String) { self.rawValue = rawValue }

    init(from decoder: Decoder) throws {
        let container = try decoder.singleValueContainer()
        rawValue = try container.decode(String.self)
    }

    func encode(to encoder: Encoder) throws {
        var container = encoder.singleValueContainer()
        try container.encode(rawValue)
    }
}
// JSON: "usr_abc123" decodes directly to UserID

Default Values for Missing Keys

Use decodeIfPresent with nil-coalescing to provide defaults:

struct Settings: Decodable {
    let theme: String
    let fontSize: Int
    let notificationsEnabled: Bool

    enum CodingKeys: String, CodingKey {
        case theme, fontSize = "font_size"
        case notificationsEnabled = "notifications_enabled"
    }

    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        theme = try container.decodeIfPresent(String.self, forKey: .theme) ?? "system"
        fontSize = try container.decodeIfPresent(Int.self, forKey: .fontSize) ?? 16
        notificationsEnabled = try container.decodeIfPresent(
            Bool.self, forKey: .notificationsEnabled) ?? true
    }
}

Encoder and Decoder Configuration
let encoder = JSONEncoder()
encoder.outputFormatting = [.prettyPrinted, .sortedKeys, .withoutEscapingSlashes]

// Non-conforming floats (NaN, Infinity are not valid JSON)
encoder.nonConformingFloatEncodingStrategy = .convertToString(
    positiveInfinity: "Infinity", negativeInfinity: "-Infinity", nan: "NaN")
decoder.nonConformingFloatDecodingStrategy = .convertFromString(
    positiveInfinity: "Infinity", negativeInfinity: "-Infinity", nan: "NaN")

PropertyListEncoder / PropertyListDecoder
let plistEncoder = PropertyListEncoder()
plistEncoder.outputFormat = .xml  // or .binary
let data = try plistEncoder.encode(settings)
let decoded = try PropertyListDecoder().decode(Settings.self, from: data)

Codable with URLSession
func fetchUser(id: Int) async throws -> User {
    let url = URL(string: "https://api.example.com/users/\(id)")!
    let (data, response) = try await URLSession.shared.data(from: url)
    guard let http = response as? HTTPURLResponse,
          (200...299).contains(http.statusCode) else {
        throw APIError.invalidResponse
    }
    let decoder = JSONDecoder()
    decoder.keyDecodingStrategy = .convertFromSnakeCase
    decoder.dateDecodingStrategy = .iso8601
    return try decoder.decode(User.self, from: data)
}

// Generic API envelope for wrapped responses
struct APIResponse<T: Decodable>: Decodable {
    let data: T
    let meta: Meta?
    struct Meta: Decodable { let page: Int; let totalPages: Int }
}
let users = try decoder.decode(APIResponse<[User]>.self, from: data).data

Codable with SwiftData

Codable structs work as composite attributes in SwiftData models. In iOS 18+, SwiftData natively supports them without explicit @Attribute(.transformable):

struct Address: Codable {
    var street: String
    var city: String
    var zipCode: String
}

@Model class Contact {
    var name: String
    var address: Address?  // Codable struct stored as composite attribute
    init(name: String, address: Address? = nil) {
        self.name = name; self.address = address
    }
}

Codable with UserDefaults

Store Codable values via RawRepresentable for @AppStorage:

struct UserPreferences: Codable {
    var showOnboarding: Bool = true
    var accentColor: String = "blue"
}

extension UserPreferences: RawRepresentable {
    init?(rawValue: String) {
        guard let data = rawValue.data(using: .utf8),
              let decoded = try? JSONDecoder().decode(Self.self, from: data)
        else { return nil }
        self = decoded
    }
    var rawValue: String {
        guard let data = try? JSONEncoder().encode(self),
              let string = String(data: data, encoding: .utf8)
        else { return "{}" }
        return string
    }
}

struct SettingsView: View {
    @AppStorage("userPrefs") private var prefs = UserPreferences()
    var body: some View {
        Toggle("Show Onboarding", isOn: $prefs.showOnboarding)
    }
}

Common Mistakes

1. Not handling missing optional keys:

// DON'T -- crashes if key is absent
let value = try container.decode(String.self, forKey: .bio)
// DO -- returns nil for missing keys
let value = try container.decodeIfPresent(String.self, forKey: .bio) ?? ""


2. Failing entire array when one element is invalid:

// DON'T -- one bad element kills the whole decode
let items = try container.decode([Item].self, forKey: .items)
// DO -- use LossyArray or decode elements individually
let items = try container.decode(LossyArray<Item>.self, forKey: .items).elements


3. Date strategy mismatch:

// DON'T -- default strategy expects Double, but API sends ISO string
let decoder = JSONDecoder()  // dateDecodingStrategy defaults to .deferredToDate
// DO -- set strategy to match your API format
decoder.dateDecodingStrategy = .iso8601


4. Force-unwrapping decoded optionals:

// DON'T
let user = try? decoder.decode(User.self, from: data)
print(user!.name)
// DO
guard let user = try? decoder.decode(User.self, from: data) else { return }


5. Using Codable when only Decodable is needed:

// DON'T -- unnecessarily constrains the type to also be Encodable
struct APIResponse: Codable { let id: Int; let message: String }
// DO -- use Decodable for read-only API responses
struct APIResponse: Decodable { let id: Int; let message: String }


6. Manual CodingKeys for simple snake_case APIs:

// DON'T -- verbose boilerplate for every model
enum CodingKeys: String, CodingKey {
    case userName = "user_name"
    case avatarUrl = "avatar_url"
}
// DO -- configure once on the decoder
decoder.keyDecodingStrategy = .convertFromSnakeCase

Review Checklist
 Types conform to Decodable only when encoding is not needed
 decodeIfPresent used with defaults for optional or missing keys
 keyDecodingStrategy = .convertFromSnakeCase used instead of manual CodingKeys for simple snake_case APIs
 dateDecodingStrategy matches the API date format
 Arrays of unreliable data use lossy decoding to skip invalid elements
 Custom init(from:) validates and transforms data instead of post-decode fixups
 JSONEncoder.outputFormatting includes .sortedKeys for deterministic test output
 Wrapper types (UserID, etc.) use singleValueContainer for clean JSON
 Generic APIResponse<T> wrapper used for consistent API envelope handling
 No force-unwrapping of decoded values
 @AppStorage Codable types conform to RawRepresentable
 SwiftData composite attributes use Codable structs
References
Codable -- protocol combining Encodable and Decodable
JSONDecoder -- decodes JSON data into Codable types
JSONEncoder -- encodes Codable types as JSON data
CodingKey -- protocol for encoding/decoding keys
Encoding and Decoding Custom Types -- Apple guide on custom Codable conformance
Using JSON with Custom Types -- Apple sample code for JSON patterns
Weekly Installs
887
Repository
dpearson2699/sw…s-skills
GitHub Stars
512
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass