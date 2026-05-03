---
title: visual-regression-tester
url: https://skills.sh/patricio0312rev/skills/visual-regression-tester
---

# visual-regression-tester

skills/patricio0312rev/skills/visual-regression-tester
visual-regression-tester
Installation
$ npx skills add https://github.com/patricio0312rev/skills --skill visual-regression-tester
SKILL.md
Visual Regression Tester

Catch unintended UI changes with automated visual regression testing.

Core Workflow
Choose tool: Playwright, Chromatic, Percy
Setup baseline: Capture initial screenshots
Configure thresholds: Define acceptable diff
Integrate CI: Automated testing
Review changes: Approve or reject
Update baselines: Accept intentional changes
Playwright Visual Testing
Installation
npm install -D @playwright/test
npx playwright install

Configuration
// playwright.config.ts
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests/visual',
  testMatch: '**/*.visual.ts',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: [
    ['html', { open: 'never' }],
    ['json', { outputFile: 'test-results/results.json' }],
  ],

  // Snapshot configuration
  snapshotDir: './tests/visual/__snapshots__',
  snapshotPathTemplate: '{snapshotDir}/{testFilePath}/{arg}{ext}',

  expect: {
    toHaveScreenshot: {
      maxDiffPixels: 100,
      maxDiffPixelRatio: 0.01,
      threshold: 0.2,
      animations: 'disabled',
    },
    toMatchSnapshot: {
      maxDiffPixelRatio: 0.01,
    },
  },

  use: {
    baseURL: 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },

  projects: [
    {
      name: 'Desktop Chrome',
      use: {
        ...devices['Desktop Chrome'],
        viewport: { width: 1280, height: 720 },
      },
    },
    {
      name: 'Desktop Firefox',
      use: {
        ...devices['Desktop Firefox'],
        viewport: { width: 1280, height: 720 },
      },
    },
    {
      name: 'Mobile Safari',
      use: {
        ...devices['iPhone 13'],
      },
    },
    {
      name: 'Tablet',
      use: {
        viewport: { width: 768, height: 1024 },
      },
    },
  ],

  webServer: {
    command: 'npm run start',
    url: 'http://localhost:3000',
    reuseExistingServer: !process.env.CI,
    timeout: 120 * 1000,
  },
});

Visual Test Examples
// tests/visual/homepage.visual.ts
import { test, expect } from '@playwright/test';

test.describe('Homepage Visual Tests', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
    // Wait for fonts and images to load
    await page.waitForLoadState('networkidle');
    // Disable animations for consistent screenshots
    await page.addStyleTag({
      content: `
        *, *::before, *::after {
          animation-duration: 0s !important;
          animation-delay: 0s !important;
          transition-duration: 0s !important;
        }
      `,
    });
  });

  test('full page screenshot', async ({ page }) => {
    await expect(page).toHaveScreenshot('homepage-full.png', {
      fullPage: true,
    });
  });

  test('hero section', async ({ page }) => {
    const hero = page.locator('[data-testid="hero-section"]');
    await expect(hero).toHaveScreenshot('hero-section.png');
  });

  test('navigation bar', async ({ page }) => {
    const nav = page.locator('nav');
    await expect(nav).toHaveScreenshot('navigation.png');
  });

  test('footer', async ({ page }) => {
    const footer = page.locator('footer');
    await footer.scrollIntoViewIfNeeded();
    await expect(footer).toHaveScreenshot('footer.png');
  });
});

Component Visual Tests
// tests/visual/components.visual.ts
import { test, expect } from '@playwright/test';

test.describe('Button Component', () => {
  test('all variants', async ({ page }) => {
    await page.goto('/storybook/button');

    // Primary button
    const primary = page.locator('[data-testid="button-primary"]');
    await expect(primary).toHaveScreenshot('button-primary.png');

    // Secondary button
    const secondary = page.locator('[data-testid="button-secondary"]');
    await expect(secondary).toHaveScreenshot('button-secondary.png');

    // Hover state
    await primary.hover();
    await expect(primary).toHaveScreenshot('button-primary-hover.png');

    // Focus state
    await primary.focus();
    await expect(primary).toHaveScreenshot('button-primary-focus.png');

    // Disabled state
    const disabled = page.locator('[data-testid="button-disabled"]');
    await expect(disabled).toHaveScreenshot('button-disabled.png');
  });
});

test.describe('Form Components', () => {
  test('input states', async ({ page }) => {
    await page.goto('/storybook/input');

    const input = page.locator('[data-testid="input-default"]');

    // Default state
    await expect(input).toHaveScreenshot('input-default.png');

    // Focused state
    await input.focus();
    await expect(input).toHaveScreenshot('input-focused.png');

    // With value
    await input.fill('Test value');
    await expect(input).toHaveScreenshot('input-with-value.png');

    // Error state
    const errorInput = page.locator('[data-testid="input-error"]');
    await expect(errorInput).toHaveScreenshot('input-error.png');
  });
});

Responsive Testing
// tests/visual/responsive.visual.ts
import { test, expect, devices } from '@playwright/test';

const viewports = [
  { name: 'mobile', width: 375, height: 667 },
  { name: 'tablet', width: 768, height: 1024 },
  { name: 'desktop', width: 1280, height: 720 },
  { name: 'wide', width: 1920, height: 1080 },
];

for (const viewport of viewports) {
  test.describe(`${viewport.name} viewport`, () => {
    test.use({ viewport: { width: viewport.width, height: viewport.height } });

    test('homepage layout', async ({ page }) => {
      await page.goto('/');
      await page.waitForLoadState('networkidle');

      await expect(page).toHaveScreenshot(`homepage-${viewport.name}.png`, {
        fullPage: true,
      });
    });

    test('navigation menu', async ({ page }) => {
      await page.goto('/');

      if (viewport.width < 768) {
        // Mobile: test hamburger menu
        const menuButton = page.locator('[data-testid="mobile-menu-button"]');
        await menuButton.click();
        await expect(page.locator('[data-testid="mobile-menu"]')).toHaveScreenshot(
          `mobile-menu-${viewport.name}.png`
        );
      } else {
        // Desktop: test full nav
        await expect(page.locator('nav')).toHaveScreenshot(
          `nav-${viewport.name}.png`
        );
      }
    });
  });
}

Dark Mode Testing
// tests/visual/dark-mode.visual.ts
import { test, expect } from '@playwright/test';

test.describe('Dark Mode', () => {
  test('homepage in dark mode', async ({ page }) => {
    await page.goto('/');

    // Enable dark mode via color scheme
    await page.emulateMedia({ colorScheme: 'dark' });

    await expect(page).toHaveScreenshot('homepage-dark.png', {
      fullPage: true,
    });
  });

  test('homepage in light mode', async ({ page }) => {
    await page.goto('/');

    await page.emulateMedia({ colorScheme: 'light' });

    await expect(page).toHaveScreenshot('homepage-light.png', {
      fullPage: true,
    });
  });

  test('theme toggle', async ({ page }) => {
    await page.goto('/');

    // Toggle theme via button
    const themeToggle = page.locator('[data-testid="theme-toggle"]');
    await themeToggle.click();

    // Wait for transition
    await page.waitForTimeout(300);

    await expect(page).toHaveScreenshot('homepage-toggled-theme.png');
  });
});

Chromatic Integration
Setup
npm install -D chromatic

Configuration
// .storybook/main.ts
export default {
  stories: ['../src/**/*.stories.@(js|jsx|ts|tsx)'],
  addons: ['@chromatic-com/storybook'],
};

CI Configuration
# .github/workflows/chromatic.yml
name: Chromatic

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  chromatic:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'

      - run: npm ci

      - name: Publish to Chromatic
        uses: chromaui/action@latest
        with:
          projectToken: ${{ secrets.CHROMATIC_PROJECT_TOKEN }}
          exitZeroOnChanges: true
          exitOnceUploaded: true
          onlyChanged: true

Chromatic Story Configuration
// Button.stories.tsx
import type { Meta, StoryObj } from '@storybook/react';
import { Button } from './Button';

const meta: Meta<typeof Button> = {
  component: Button,
  parameters: {
    chromatic: {
      // Capture multiple viewports
      viewports: [375, 768, 1280],
      // Delay for animations
      delay: 300,
      // Disable animations
      pauseAnimationAtEnd: true,
    },
  },
};

export default meta;

export const Primary: StoryObj<typeof Button> = {
  args: { variant: 'primary', children: 'Button' },
};

export const AllStates: StoryObj<typeof Button> = {
  parameters: {
    chromatic: {
      // Test interaction states
      modes: {
        hover: { pseudo: { hover: true } },
        focus: { pseudo: { focus: true } },
        active: { pseudo: { active: true } },
      },
    },
  },
  render: () => (
    <div style={{ display: 'flex', gap: '1rem' }}>
      <Button variant="primary">Primary</Button>
      <Button variant="secondary">Secondary</Button>
      <Button disabled>Disabled</Button>
    </div>
  ),
};

CI Integration
# .github/workflows/visual-tests.yml
name: Visual Regression Tests

on:
  pull_request:
    branches: [main]

jobs:
  visual-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'

      - run: npm ci

      - name: Install Playwright Browsers
        run: npx playwright install --with-deps chromium

      - name: Build application
        run: npm run build

      - name: Run visual tests
        run: npx playwright test --project="Desktop Chrome"

      - name: Upload test results
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: playwright-report
          path: |
            playwright-report/
            test-results/
          retention-days: 30

      - name: Upload diff images
        if: failure()
        uses: actions/upload-artifact@v4
        with:
          name: visual-diffs
          path: tests/visual/__snapshots__/*-diff.png
          retention-days: 7

Update Baselines Script
// package.json
{
  "scripts": {
    "test:visual": "playwright test --project='Desktop Chrome'",
    "test:visual:update": "playwright test --update-snapshots",
    "test:visual:ui": "playwright test --ui",
    "test:visual:report": "playwright show-report"
  }
}

Best Practices
Disable animations: Consistent screenshots
Wait for network: Ensure content loaded
Use stable selectors: data-testid attributes
Test multiple viewports: Responsive coverage
Set thresholds: Allow minor pixel differences
Review in CI: Block merges on failures
Organize snapshots: Clear naming convention
Update intentionally: Review all baseline changes
Output Checklist

Every visual testing setup should include:

 Playwright/Chromatic configuration
 Baseline screenshots
 Multi-viewport testing
 Dark mode coverage
 Component state testing
 Animation disabling
 CI integration
 Diff threshold configuration
 Baseline update workflow
 Artifact storage
Weekly Installs
125
Repository
patricio0312rev/skills
GitHub Stars
35
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass