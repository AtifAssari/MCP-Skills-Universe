---
title: ios-swift-development
url: https://skills.sh/aj-geddes/useful-ai-prompts/ios-swift-development
---

# ios-swift-development

skills/aj-geddes/useful-ai-prompts/ios-swift-development
ios-swift-development
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill ios-swift-development
Summary

Native iOS app development with Swift, SwiftUI, and modern async patterns.

Covers MVVM architecture, SwiftUI declarative UI, URLSession networking, and Combine reactive programming
Includes async/await patterns, Core Data persistence, and Keychain for secure storage
Best practices emphasize dependency injection, proper error handling, @StateObject for ViewModels, and testing across iOS versions
Reference guides provided for network services, MVVM setup, and SwiftUI view implementation
SKILL.md
iOS Swift Development
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Build high-performance native iOS applications using Swift with modern frameworks including SwiftUI, Combine, and async/await patterns.

When to Use
Creating native iOS applications with optimal performance
Leveraging iOS-specific features and APIs
Building apps that require tight hardware integration
Using SwiftUI for declarative UI development
Implementing complex animations and transitions
Quick Start

Minimal working example:

import Foundation
import Combine

struct User: Codable, Identifiable {
  let id: UUID
  var name: String
  var email: String
}

class UserViewModel: ObservableObject {
  @Published var user: User?
  @Published var isLoading = false
  @Published var errorMessage: String?

  private let networkService: NetworkService

  init(networkService: NetworkService = .shared) {
    self.networkService = networkService
  }

  @MainActor
  func fetchUser(id: UUID) async {
    isLoading = true
    errorMessage = nil

// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
MVVM Architecture Setup	MVVM Architecture Setup
Network Service with URLSession	Network Service with URLSession
SwiftUI Views	SwiftUI Views
Best Practices
✅ DO
Use SwiftUI for modern UI development
Implement MVVM architecture
Use async/await patterns
Store sensitive data in Keychain
Handle errors gracefully
Use @StateObject for ViewModels
Validate API responses properly
Implement Core Data for persistence
Test on multiple iOS versions
Use dependency injection
Follow Swift style guidelines
❌ DON'T
Store tokens in UserDefaults
Make network calls on main thread
Use deprecated UIKit patterns
Ignore memory leaks
Skip error handling
Use force unwrapping (!)
Store passwords in code
Ignore accessibility
Deploy untested code
Use hardcoded API URLs
Weekly Installs
1.2K
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass