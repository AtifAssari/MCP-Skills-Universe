---
title: android-kotlin-development
url: https://skills.sh/aj-geddes/useful-ai-prompts/android-kotlin-development
---

# android-kotlin-development

skills/aj-geddes/useful-ai-prompts/android-kotlin-development
android-kotlin-development
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill android-kotlin-development
Summary

Native Android development with Kotlin, MVVM architecture, Jetpack Compose, and modern libraries.

Covers MVVM pattern with Jetpack ViewModels, StateFlow for reactive state management, and Hilt for dependency injection
Includes Jetpack Compose for declarative UI, Retrofit for API integration, and Room for local SQLite persistence
Provides reference implementations for models, API services, ViewModels, and Compose UI components
Emphasizes coroutines for async operations, proper lifecycle management, and comprehensive error handling across network and storage layers
SKILL.md
Android Kotlin Development
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Build robust native Android applications using Kotlin with modern architecture patterns, Jetpack libraries, and Compose for declarative UI.

When to Use
Creating native Android applications with best practices
Using Kotlin for type-safe development
Implementing MVVM architecture with Jetpack
Building modern UIs with Jetpack Compose
Integrating with Android platform APIs
Quick Start

Minimal working example:

// Models
data class User(
  val id: String,
  val name: String,
  val email: String,
  val avatarUrl: String? = null
)

data class Item(
  val id: String,
  val title: String,
  val description: String,
  val imageUrl: String? = null,
  val price: Double
)

// API Service with Retrofit
interface ApiService {
  @GET("/users/{id}")
  suspend fun getUser(@Path("id") userId: String): User

  @PUT("/users/{id}")
  suspend fun updateUser(
    @Path("id") userId: String,
    @Body user: User
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Models & API Service	Models & API Service
MVVM ViewModels with Jetpack	MVVM ViewModels with Jetpack
Jetpack Compose UI	Jetpack Compose UI
Best Practices
✅ DO
Use Kotlin for all new Android code
Implement MVVM with Jetpack libraries
Use Jetpack Compose for UI development
Leverage coroutines for async operations
Use Room for local data persistence
Implement proper error handling
Use Hilt for dependency injection
Use StateFlow for reactive state
Test on multiple device types
Follow Android design guidelines
❌ DON'T
Store tokens in SharedPreferences
Make network calls on main thread
Ignore lifecycle management
Skip null safety checks
Hardcode strings and resources
Ignore configuration changes
Store passwords in code
Deploy without device testing
Use deprecated APIs
Accumulate memory leaks
Weekly Installs
832
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