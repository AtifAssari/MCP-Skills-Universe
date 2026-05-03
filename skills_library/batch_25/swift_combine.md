---
title: swift_combine
url: https://skills.sh/swiftzilla/skills/swift_combine
---

# swift_combine

skills/swiftzilla/skills/swift_combine
swift_combine
Installation
$ npx skills add https://github.com/swiftzilla/skills --skill swift_combine
SKILL.md
Swift Combine

This skill covers Apple's Combine framework for reactive programming and handling asynchronous events.

Overview

Combine is a declarative Swift API for processing values over time. It provides a unified approach to handling asynchronous events, user interface updates, and data streams.

Available References
Publishers & Subscribers - Core concepts and lifecycle
Operators - Transforming, filtering, and combining streams
Integration - Using Combine with UIKit, SwiftUI, and Foundation
Quick Reference
Basic Publisher
import Combine

// Published property
@Published var username: String = ""

// CurrentValueSubject
let subject = CurrentValueSubject<String, Never>("initial")

// PassthroughSubject
let passthrough = PassthroughSubject<Int, Never>()

// Just publisher
let just = Just("value")

// Future publisher
let future = Future<String, Error> { promise in
    promise(.success("result"))
}

Subscribing
// Sink
let cancellable = publisher.sink(
    receiveCompletion: { completion in
        switch completion {
        case .finished:
            print("Completed")
        case .failure(let error):
            print("Error: \(error)")
        }
    },
    receiveValue: { value in
        print("Value: \(value)")
    }
)

// Assign
let cancellable = publisher
    .assign(to: \.text, on: label)

Storing Subscriptions
private var cancellables = Set<AnyCancellable>()

publisher
    .sink { value in
        print(value)
    }
    .store(in: &cancellables)

Common Operators
publisher
    .filter { $0 > 0 }
    .map { $0 * 2 }
    .debounce(for: .seconds(0.5), scheduler: RunLoop.main)
    .removeDuplicates()
    .sink { value in
        print(value)
    }

Combine vs Async/Await
Use Case	Combine	Async/Await
Event streams	✅ Excellent	⚠️ Complex
UI bindings	✅ Perfect	⚠️ Verbose
Chaining operations	✅ Great	✅ Good
Simple async calls	⚠️ Overkill	✅ Simple
Error handling	✅ Rich	✅ Good
Best Practices
Store cancellables - Prevent memory leaks
Use weak self - Avoid retain cycles
Handle errors - Always handle completion
Thread safety - Use receive(on:) for UI
Cancel properly - Clean up subscriptions
Avoid overuse - Combine is powerful but not for everything
Test pipelines - Use expectations for async
For More Information

Visit https://swiftzilla.dev for comprehensive Combine documentation.

Weekly Installs
32
Repository
swiftzilla/skills
GitHub Stars
6
First Seen
Today