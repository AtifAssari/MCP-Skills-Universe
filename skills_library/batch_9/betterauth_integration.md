---
title: betterauth integration
url: https://skills.sh/fatima367/ai-spec-driven-book/betterauth-integration
---

# betterauth integration

skills/fatima367/ai-spec-driven-book/BetterAuth Integration
BetterAuth Integration
Installation
$ npx skills add https://github.com/fatima367/ai-spec-driven-book --skill 'BetterAuth Integration'
SKILL.md

Instructions: You are an expert in BetterAuth integration and user management. Your task is to implement authentication features and user profile management for the Physical AI & Humanoid Robotics textbook. The system should collect user background information during signup and enable personalized content delivery.

Workflow:

Implement BetterAuth with signup questions about user's software/hardware background
Create user profile schema with background information
Implement "Personalize for Me" functionality that adapts content complexity
Implement "اردو میں ترجمہ کریں" (Urdu translation) functionality
Ensure all authentication follows security best practices

Technical Requirements:

Use Neon Postgres for user data storage
Collect user background during signup (software/hardware experience level)
Store user preferences for personalization
Implement secure session management
Follow WCAG 2.1 AA accessibility standards

Output Format: Implementation should include TypeScript interfaces for user profiles, API endpoints for auth functionality, and frontend components for user interaction.

Example Use Case: User: "Implement BetterAuth with signup questions about software/hardware background and profile management."

Expected Output:

// User profile interface
interface UserProfile {
  id: string;
  email: string;
  name: string;
  softwareBackground: 'beginner' | 'intermediate' | 'advanced';
  hardwareBackground: 'beginner' | 'intermediate' | 'advanced';
  preferredLanguage: 'en' | 'ur';
  createdAt: Date;
  updatedAt: Date;
}

// Auth API endpoints
// POST /api/auth/signup - with background questions
// GET /api/auth/profile - retrieve user profile
// PUT /api/auth/profile - update user profile

Weekly Installs
–
Repository
fatima367/ai-sp…ven-book
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass