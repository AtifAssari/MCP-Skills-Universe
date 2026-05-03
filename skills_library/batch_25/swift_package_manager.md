---
title: swift_package_manager
url: https://skills.sh/swiftzilla/skills/swift_package_manager
---

# swift_package_manager

skills/swiftzilla/skills/swift_package_manager
swift_package_manager
Installation
$ npx skills add https://github.com/swiftzilla/skills --skill swift_package_manager
SKILL.md
Swift Package Manager

This skill covers Swift Package Manager for managing dependencies, creating reusable packages, and organizing code into modular components.

Overview

Swift Package Manager (SPM) is Apple's official tool for distributing and managing Swift code. It handles dependency resolution, building, and packaging with a simple declarative format.

Available References
Package Structure - Package.swift, targets, products, and dependencies
Dependencies - Version constraints, local packages, and resolution
Publishing - Publishing packages to GitHub and registries
Quick Reference
Basic Package.swift
// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "MyLibrary",
    platforms: [.iOS(.v15), .macOS(.v12)],
    products: [
        .library(
            name: "MyLibrary",
            targets: ["MyLibrary"]
        ),
    ],
    dependencies: [
        .package(url: "https://github.com/Alamofire/Alamofire.git", from: "5.8.0"),
    ],
    targets: [
        .target(
            name: "MyLibrary",
            dependencies: [
                .product(name: "Alamofire", package: "Alamofire")
            ]
        ),
        .testTarget(
            name: "MyLibraryTests",
            dependencies: ["MyLibrary"]
        ),
    ]
)

Adding Dependencies
// Version ranges
.package(url: "...", from: "1.0.0")           // >= 1.0.0, < 2.0.0
.package(url: "...", .upToNextMajor(from: "1.0.0"))
.package(url: "...", .upToNextMinor(from: "1.0.0"))
.package(url: "...", .exact("1.0.0"))
.package(url: "...", branch: "main")
.package(url: "...", revision: "abc123")

// Local packages
.package(path: "../LocalPackage")

Command Line
# Initialize new package
swift package init --type library
swift package init --type executable

# Resolve dependencies
swift package resolve

# Update dependencies
swift package update

# Build
swift build

# Test
swift test

# Generate Xcode project
swift package generate-xcodeproj

Package Structure
MyPackage/
├── Package.swift          # Package manifest
├── Sources/
│   └── MyLibrary/
│       └── MyLibrary.swift
├── Tests/
│   └── MyLibraryTests/
│       └── MyLibraryTests.swift
└── README.md

Best Practices
Use semantic versioning - Follow SemVer for version tags
Specify platform requirements - Declare minimum OS versions
Create explicit products - Control what you expose
Separate test targets - Keep tests isolated
Use resource bundles - For non-code assets
Commit Package.resolved - For reproducible builds
Document public API - Use Swift documentation comments
Add LICENSE file - Essential for open source
For More Information

Visit https://swiftzilla.dev for comprehensive Swift Package Manager documentation.

Weekly Installs
24
Repository
swiftzilla/skills
GitHub Stars
6
First Seen
Jan 28, 2026