---
title: qe-visual-accessibility
url: https://skills.sh/proffesor-for-testing/agentic-qe/qe-visual-accessibility
---

# qe-visual-accessibility

skills/proffesor-for-testing/agentic-qe/qe-visual-accessibility
qe-visual-accessibility
Installation
$ npx skills add https://github.com/proffesor-for-testing/agentic-qe --skill qe-visual-accessibility
SKILL.md
QE Visual Accessibility
Purpose

Guide the use of v3's visual and accessibility testing capabilities including screenshot comparison, responsive design validation, and WCAG 2.2 compliance verification.

Activation
When testing visual appearance
When validating responsive design
When checking accessibility compliance
When detecting visual regressions
When testing cross-browser rendering
Quick Start
# Visual regression test
aqe visual test --baseline production --current staging

# Responsive design test
aqe visual responsive --url https://example.com --viewports all

# Accessibility audit
aqe a11y audit --url https://example.com --standard wcag22-aa

# Cross-browser test
aqe visual cross-browser --url https://example.com --browsers chrome,firefox,safari

Agent Workflow
// Visual regression testing
Task("Run visual regression", `
  Compare staging against production:
  - Capture screenshots of key pages
  - Detect pixel differences
  - Flag significant visual changes
  - Generate visual diff report
`, "qe-visual-tester")

// Accessibility audit
Task("Audit accessibility", `
  Run WCAG 2.2 AA compliance audit:
  - Check color contrast ratios
  - Verify keyboard navigation
  - Test screen reader compatibility
  - Validate ARIA labels
  Generate compliance report with fix suggestions.
`, "qe-accessibility-agent")

Browser engine

All browser automation in this skill uses the qe-browser fleet skill (Vibium engine). See .claude/skills/qe-browser/SKILL.md. The vibium binary is installed by aqe init.

Visual Testing Operations
1. Visual Regression (via qe-browser)
# Establish baselines for the pages we care about
for path in / /login /dashboard /settings; do
  slug=$(echo "$path" | tr '/' '_' | sed 's/^_//' || echo root)
  vibium go "https://production.example.com$path" && vibium wait load
  node .claude/skills/qe-browser/scripts/visual-diff.js --name "baseline_${slug:-root}"
done

# Compare staging against those baselines
for path in / /login /dashboard /settings; do
  slug=$(echo "$path" | tr '/' '_' | sed 's/^_//' || echo root)
  vibium go "https://staging.example.com$path" && vibium wait load
  node .claude/skills/qe-browser/scripts/visual-diff.js \
    --name "baseline_${slug:-root}" --threshold 0.001  # 0.1% pixel diff
done


Ignore dynamic regions (timestamps, live counts) by scoping the diff to a selector that excludes them:

node .claude/skills/qe-browser/scripts/visual-diff.js \
  --name hero --selector "main > .content"


Legacy programmatic TypeScript API (still available for tests that prefer it over shelling out):

await visualTester.compareScreenshots({
  baseline: {
    source: 'production',
    pages: ['/', '/login', '/dashboard', '/settings']
  },
  current: {
    source: 'staging',
    pages: ['/', '/login', '/dashboard', '/settings']
  },
  comparison: {
    threshold: 0.1,  // 0.1% pixel difference
    antialiasing: true,
    ignoreRegions: ['#dynamic-content', '.timestamp']
  }
});

2. Responsive Testing
await responsiveTester.test({
  url: 'https://example.com',
  viewports: [
    { name: 'mobile', width: 375, height: 667 },
    { name: 'tablet', width: 768, height: 1024 },
    { name: 'desktop', width: 1920, height: 1080 }
  ],
  checks: {
    layoutShift: true,
    contentOverflow: true,
    touchTargets: true,
    fontScaling: true
  }
});

3. Accessibility Audit
await accessibilityAgent.audit({
  url: 'https://example.com',
  standard: 'WCAG22-AA',
  checks: {
    perceivable: {
      colorContrast: true,
      textAlternatives: true,
      captions: true
    },
    operable: {
      keyboardAccessible: true,
      noTimingIssues: true,
      navigable: true
    },
    understandable: {
      readable: true,
      predictable: true,
      inputAssistance: true
    },
    robust: {
      compatible: true,
      parseErrors: true
    }
  }
});

4. Cross-Browser Testing
await visualTester.crossBrowser({
  url: 'https://example.com',
  browsers: ['chrome', 'firefox', 'safari', 'edge'],
  versions: 'latest-2',
  comparisons: {
    betweenBrowsers: true,
    betweenVersions: true,
    againstBaseline: true
  }
});

WCAG 2.2 Checklist
Level	Criteria	Auto-Testable
A	Non-text Content	✅
A	Info and Relationships	Partial
A	Color Contrast (4.5:1)	✅
A	Keyboard Accessible	✅
A	Focus Visible	✅
AA	Reflow	✅
AA	Text Spacing	✅
AAA	Enhanced Contrast (7:1)	✅
Visual Test Report
interface VisualReport {
  summary: {
    pagesCompared: number;
    differencesFound: number;
    passRate: number;
  };
  comparisons: {
    page: string;
    viewport: string;
    baseline: string;
    current: string;
    diff: string;
    diffPercentage: number;
    status: 'pass' | 'fail' | 'review';
  }[];
  accessibility: {
    violations: A11yViolation[];
    passes: number;
    incomplete: number;
    score: number;
  };
  responsive: {
    viewport: string;
    issues: ResponsiveIssue[];
  }[];
}

Accessibility Report
interface AccessibilityReport {
  summary: {
    score: number;
    violations: number;
    warnings: number;
    passes: number;
  };
  violations: {
    id: string;
    impact: 'critical' | 'serious' | 'moderate' | 'minor';
    description: string;
    wcag: string[];
    elements: {
      selector: string;
      html: string;
      issue: string;
      fix: string;
    }[];
  }[];
  compliance: {
    wcagLevel: 'A' | 'AA' | 'AAA';
    criteriasMet: number;
    criteriasTotal: number;
  };
}

CI/CD Integration
visual_testing:
  on_pr:
    - capture_screenshots
    - compare_to_baseline
    - run_a11y_audit

  thresholds:
    visual_diff: 0.1
    a11y_violations: 0

  artifacts:
    - screenshots/
    - diffs/
    - a11y-report.html

Coordination

Primary Agents: qe-visual-tester, qe-accessibility-agent, qe-responsive-tester Coordinator: qe-visual-coordinator Related Skills: qe-test-execution, qe-quality-assessment

Weekly Installs
43
Repository
proffesor-for-t…entic-qe
GitHub Stars
334
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn