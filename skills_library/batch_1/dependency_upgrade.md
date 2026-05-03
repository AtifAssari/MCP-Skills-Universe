---
title: dependency-upgrade
url: https://skills.sh/wshobson/agents/dependency-upgrade
---

# dependency-upgrade

skills/wshobson/agents/dependency-upgrade
dependency-upgrade
Installation
$ npx skills add https://github.com/wshobson/agents --skill dependency-upgrade
Summary

Manage major dependency version upgrades with compatibility analysis, staged rollout, and comprehensive testing.

Provides semantic versioning review, dependency auditing tools, and compatibility matrix validation across framework versions
Includes staged upgrade strategies with phase-based planning, incremental updates, and validation workflows to minimize breaking changes
Covers breaking change identification, automated codemods for API migrations, and custom migration scripts for large codebases
Offers comprehensive testing approaches including unit, integration, visual regression, and E2E test strategies
Supports automated dependency management via Renovate and Dependabot configurations, with rollback procedures and workspace upgrade patterns
SKILL.md
Dependency Upgrade

Master major dependency version upgrades, compatibility analysis, staged upgrade strategies, and comprehensive testing approaches.

When to Use This Skill
Upgrading major framework versions
Updating security-vulnerable dependencies
Modernizing legacy dependencies
Resolving dependency conflicts
Planning incremental upgrade paths
Testing compatibility matrices
Automating dependency updates
Semantic Versioning Review
MAJOR.MINOR.PATCH (e.g., 2.3.1)

MAJOR: Breaking changes
MINOR: New features, backward compatible
PATCH: Bug fixes, backward compatible

^2.3.1 = >=2.3.1 <3.0.0 (minor updates)
~2.3.1 = >=2.3.1 <2.4.0 (patch updates)
2.3.1 = exact version

Dependency Analysis
Audit Dependencies
# npm
npm outdated
npm audit
npm audit fix

# yarn
yarn outdated
yarn audit

# Check for major updates
npx npm-check-updates
npx npm-check-updates -u  # Update package.json

Analyze Dependency Tree
# See why a package is installed
npm ls package-name
yarn why package-name

# Find duplicate packages
npm dedupe
yarn dedupe

# Visualize dependencies
npx madge --image graph.png src/

Compatibility Matrix
// compatibility-matrix.js
const compatibilityMatrix = {
  react: {
    "16.x": {
      "react-dom": "^16.0.0",
      "react-router-dom": "^5.0.0",
      "@testing-library/react": "^11.0.0",
    },
    "17.x": {
      "react-dom": "^17.0.0",
      "react-router-dom": "^5.0.0 || ^6.0.0",
      "@testing-library/react": "^12.0.0",
    },
    "18.x": {
      "react-dom": "^18.0.0",
      "react-router-dom": "^6.0.0",
      "@testing-library/react": "^13.0.0",
    },
  },
};

function checkCompatibility(packages) {
  // Validate package versions against matrix
}

Staged Upgrade Strategy
Phase 1: Planning
# 1. Identify current versions
npm list --depth=0

# 2. Check for breaking changes
# Read CHANGELOG.md and MIGRATION.md

# 3. Create upgrade plan
echo "Upgrade order:
1. TypeScript
2. React
3. React Router
4. Testing libraries
5. Build tools" > UPGRADE_PLAN.md

Phase 2: Incremental Updates
# Don't upgrade everything at once!

# Step 1: Update TypeScript
npm install typescript@latest

# Test
npm run test
npm run build

# Step 2: Update React (one major version at a time)
npm install react@17 react-dom@17

# Test again
npm run test

# Step 3: Continue with other packages
npm install react-router-dom@6

# And so on...

Phase 3: Validation
// tests/compatibility.test.js
describe("Dependency Compatibility", () => {
  it("should have compatible React versions", () => {
    const reactVersion = require("react/package.json").version;
    const reactDomVersion = require("react-dom/package.json").version;

    expect(reactVersion).toBe(reactDomVersion);
  });

  it("should not have peer dependency warnings", () => {
    // Run npm ls and check for warnings
  });
});

Breaking Change Handling
Identifying Breaking Changes
# Check the changelog directly
curl https://raw.githubusercontent.com/facebook/react/master/CHANGELOG.md

Codemod for Automated Fixes
# Run jscodeshift with transform URL
npx jscodeshift -t <transform-url> <path>

# Example: Rename unsafe lifecycle methods
npx jscodeshift -t https://raw.githubusercontent.com/reactjs/react-codemod/master/transforms/rename-unsafe-lifecycles.js src/

# For TypeScript files
npx jscodeshift -t https://raw.githubusercontent.com/reactjs/react-codemod/master/transforms/rename-unsafe-lifecycles.js --parser=tsx src/

# Dry run to preview changes
npx jscodeshift -t https://raw.githubusercontent.com/reactjs/react-codemod/master/transforms/rename-unsafe-lifecycles.js --dry src/

Custom Migration Script
// migration-script.js
const fs = require("fs");
const glob = require("glob");

glob("src/**/*.tsx", (err, files) => {
  files.forEach((file) => {
    let content = fs.readFileSync(file, "utf8");

    // Replace old API with new API
    content = content.replace(
      /componentWillMount/g,
      "UNSAFE_componentWillMount",
    );

    // Update imports
    content = content.replace(
      /import { Component } from 'react'/g,
      "import React, { Component } from 'react'",
    );

    fs.writeFileSync(file, content);
  });
});

Testing Strategy
Unit Tests
// Ensure tests pass before and after upgrade
npm run test

// Update test utilities if needed
npm install @testing-library/react@latest

Integration Tests
// tests/integration/app.test.js
describe("App Integration", () => {
  it("should render without crashing", () => {
    render(<App />);
  });

  it("should handle navigation", () => {
    const { getByText } = render(<App />);
    fireEvent.click(getByText("Navigate"));
    expect(screen.getByText("New Page")).toBeInTheDocument();
  });
});

Visual Regression Tests
// visual-regression.test.js
describe("Visual Regression", () => {
  it("should match snapshot", () => {
    const { container } = render(<App />);
    expect(container.firstChild).toMatchSnapshot();
  });
});

E2E Tests
// cypress/e2e/app.cy.js
describe("E2E Tests", () => {
  it("should complete user flow", () => {
    cy.visit("/");
    cy.get('[data-testid="login"]').click();
    cy.get('input[name="email"]').type("user@example.com");
    cy.get('button[type="submit"]').click();
    cy.url().should("include", "/dashboard");
  });
});

Automated Dependency Updates
Renovate Configuration
// renovate.json
{
  "extends": ["config:base"],
  "packageRules": [
    {
      "matchUpdateTypes": ["minor", "patch"],
      "automerge": true
    },
    {
      "matchUpdateTypes": ["major"],
      "automerge": false,
      "labels": ["major-update"]
    }
  ],
  "schedule": ["before 3am on Monday"],
  "timezone": "America/New_York"
}

Dependabot Configuration
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 5
    reviewers:
      - "team-leads"
    commit-message:
      prefix: "chore"
      include: "scope"

Rollback Plan
// rollback.sh
#!/bin/bash

# Save current state
git stash
git checkout -b upgrade-branch

# Attempt upgrade
npm install package@latest

# Run tests
if npm run test; then
  echo "Upgrade successful"
  git add package.json package-lock.json
  git commit -m "chore: upgrade package"
else
  echo "Upgrade failed, rolling back"
  git checkout main
  git branch -D upgrade-branch
  npm install  # Restore from package-lock.json
fi

Common Upgrade Patterns
Lock File Management
# npm
npm install --package-lock-only  # Update lock file only
npm ci  # Clean install from lock file

# yarn
yarn install --frozen-lockfile  # CI mode
yarn upgrade-interactive  # Interactive upgrades

Peer Dependency Resolution
# npm 7+: strict peer dependencies
npm install --legacy-peer-deps  # Ignore peer deps

# npm 8+: override peer dependencies
npm install --force

Workspace Upgrades
# Update all workspace packages
npm install --workspaces

# Update specific workspace
npm install package@latest --workspace=packages/app

Weekly Installs
5.8K
Repository
wshobson/agents
GitHub Stars
34.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn