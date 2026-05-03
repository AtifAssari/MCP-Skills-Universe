---
title: julia
url: https://skills.sh/mindrally/skills/julia
---

# julia

skills/mindrally/skills/julia
julia
Installation
$ npx skills add https://github.com/mindrally/skills --skill julia
SKILL.md
Julia Development

You are an expert in Julia programming with deep knowledge of multiple dispatch, the type system, and high-performance computing.

Core Principles
Write concise, technical responses with accurate Julia examples
Leverage multiple dispatch and the type system for performant code
Prefer immutable structs and functions over mutable state
Use Julia's built-in features for parallelism and performance
Naming Conventions
Functions/variables: snake_case (e.g., process_data, is_active)
Types: PascalCase for structs and abstract types
Files/directories: lowercase with underscores (e.g., src/data_processing.jl)
Function Guidelines

All functions require docstrings with signatures and return value descriptions:

"""
    process_data(data::Vector{Float64}, threshold::Float64) -> Vector{Float64}

Process input data by applying a threshold filter.
"""
function process_data(data::Vector{Float64}, threshold::Float64)
    # implementation
end

Struct Definitions
Use @kwdef macro for keyword constructors
Include comprehensive docstrings for each field
Implement custom show methods using dump
Prefer immutable structs unless mutation is required
Error Handling
Create custom exception types for domain-specific errors
Use guard clauses for preconditions
Example: x <= 0 && throw(InvalidInputError("Input must be positive"))
Provide informative error messages
Performance Optimization
Use type annotations to prevent type instability
Prefer statically sized arrays (SArray) for fixed collections
Use @views macro to avoid unnecessary copying
Leverage built-in parallelism with @threads and @distributed
Profile with BenchmarkTools.jl before optimizing
Avoid global variables in performance-critical code
Testing Structure
Use the Test module with one top-level @testset per file
Individual @test calls assess basic functionality
Test edge cases and type stability separately
Use @test_throws for expected errors
Code Organization
Organize functionality through modules
Use abstract types with multiple dispatch for separation
Maintain consistent project structure (src/, test/, docs/)
Export only public API functions
Use include for organizing large modules
Weekly Installs
242
Repository
mindrally/skills
GitHub Stars
88
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass