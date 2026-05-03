---
rating: ⭐⭐⭐
title: playwright-recording
url: https://skills.sh/digitalsamba/claude-code-video-toolkit/playwright-recording
---

# playwright-recording

skills/digitalsamba/claude-code-video-toolkit/playwright-recording
playwright-recording
Installation
$ npx skills add https://github.com/digitalsamba/claude-code-video-toolkit --skill playwright-recording
SKILL.md
Playwright Video Recording

Playwright can record browser interactions as video - perfect for demo footage in Remotion compositions.

Quick Start
Installation
# In your video project
npm init -y
npm install -D playwright @playwright/test
npx playwright install chromium

Basic Recording Script
// scripts/record-demo.ts
import { chromium } from 'playwright';

async function recordDemo() {
  const browser = await chromium.launch();
  const context = await browser.newContext({
    viewport: { width: 1920, height: 1080 },
    recordVideo: {
      dir: './recordings',
      size: { width: 1920, height: 1080 }
    }
  });

  const page = await context.newPage();

  // Your recording actions
  await page.goto('https://example.com');
  await page.waitForTimeout(2000);
  await page.click('button.demo');
  await page.waitForTimeout(3000);

  // Close to save video
  await context.close();
  await browser.close();

  console.log('Recording saved to ./recordings/');
}

recordDemo();


Run with:

npx ts-node scripts/record-demo.ts
# or
npx tsx scripts/record-demo.ts

Recording Configuration
Viewport Sizes
// Standard 1080p (recommended for Remotion)
viewport: { width: 1920, height: 1080 }

// 720p (smaller files)
viewport: { width: 1280, height: 720 }

// Square (social media)
viewport: { width: 1080, height: 1080 }

// Mobile
viewport: { width: 390, height: 844 } // iPhone 14

Video Quality Settings
const context = await browser.newContext({
  viewport: { width: 1920, height: 1080 },
  recordVideo: {
    dir: './recordings',
    size: { width: 1920, height: 1080 } // Match viewport for crisp output
  },
  // Slow down for visibility
  // Note: slowMo is on browser launch, not context
});

// For slow motion, launch browser with slowMo
const browser = await chromium.launch({
  slowMo: 100 // 100ms delay between actions
});

Recording Patterns
Form Submission Demo
import { chromium } from 'playwright';

async function recordFormDemo() {
  const browser = await chromium.launch({ slowMo: 50 });
  const context = await browser.newContext({
    viewport: { width: 1920, height: 1080 },
    recordVideo: { dir: './recordings', size: { width: 1920, height: 1080 } }
  });
  const page = await context.newPage();

  await page.goto('https://myapp.com/form');
  await page.waitForTimeout(1000);

  // Type with realistic speed
  await page.fill('#name', 'John Smith', { timeout: 5000 });
  await page.waitForTimeout(500);

  await page.fill('#email', 'john@example.com');
  await page.waitForTimeout(500);

  // Click submit
  await page.click('button[type="submit"]');

  // Wait for result
  await page.waitForSelector('.success-message');
  await page.waitForTimeout(2000);

  await context.close();
  await browser.close();
}

Multi-Page Navigation
async function recordNavDemo() {
  const browser = await chromium.launch({ slowMo: 100 });
  const context = await browser.newContext({
    viewport: { width: 1920, height: 1080 },
    recordVideo: { dir: './recordings', size: { width: 1920, height: 1080 } }
  });
  const page = await context.newPage();

  // Page 1
  await page.goto('https://myapp.com');
  await page.waitForTimeout(2000);

  // Navigate to page 2
  await page.click('nav a[href="/features"]');
  await page.waitForLoadState('networkidle');
  await page.waitForTimeout(2000);

  // Navigate to page 3
  await page.click('nav a[href="/pricing"]');
  await page.waitForLoadState('networkidle');
  await page.waitForTimeout(2000);

  await context.close();
  await browser.close();
}

Scroll Demo
async function recordScrollDemo() {
  const browser = await chromium.launch();
  const context = await browser.newContext({
    viewport: { width: 1920, height: 1080 },
    recordVideo: { dir: './recordings', size: { width: 1920, height: 1080 } }
  });
  const page = await context.newPage();

  await page.goto('https://myapp.com/long-page');
  await page.waitForTimeout(1000);

  // Smooth scroll
  await page.evaluate(async () => {
    const delay = (ms: number) => new Promise(r => setTimeout(r, ms));
    for (let i = 0; i < 10; i++) {
      window.scrollBy({ top: 200, behavior: 'smooth' });
      await delay(300);
    }
  });

  await page.waitForTimeout(1000);
  await context.close();
  await browser.close();
}

Login Flow
async function recordLoginDemo() {
  const browser = await chromium.launch({ slowMo: 75 });
  const context = await browser.newContext({
    viewport: { width: 1920, height: 1080 },
    recordVideo: { dir: './recordings', size: { width: 1920, height: 1080 } }
  });
  const page = await context.newPage();

  await page.goto('https://myapp.com/login');
  await page.waitForTimeout(1000);

  await page.fill('#email', 'demo@example.com');
  await page.waitForTimeout(300);

  await page.fill('#password', '••••••••');
  await page.waitForTimeout(500);

  await page.click('button[type="submit"]');

  // Wait for dashboard
  await page.waitForURL('**/dashboard');
  await page.waitForTimeout(3000);

  await context.close();
  await browser.close();
}

Cursor Highlighting

Playwright doesn't show cursor by default. Add visual indicators:

CSS Cursor Highlight
// Inject cursor visualization
await page.addStyleTag({
  content: `
    * { cursor: none !important; }
    .playwright-cursor {
      position: fixed;
      width: 24px;
      height: 24px;
      background: rgba(255, 100, 100, 0.5);
      border: 2px solid rgba(255, 50, 50, 0.8);
      border-radius: 50%;
      pointer-events: none;
      z-index: 999999;
      transform: translate(-50%, -50%);
      transition: transform 0.1s ease;
    }
    .playwright-cursor.clicking {
      transform: translate(-50%, -50%) scale(0.8);
      background: rgba(255, 50, 50, 0.8);
    }
  `
});

// Add cursor element
await page.evaluate(() => {
  const cursor = document.createElement('div');
  cursor.className = 'playwright-cursor';
  document.body.appendChild(cursor);

  document.addEventListener('mousemove', (e) => {
    cursor.style.left = e.clientX + 'px';
    cursor.style.top = e.clientY + 'px';
  });

  document.addEventListener('mousedown', () => cursor.classList.add('clicking'));
  document.addEventListener('mouseup', () => cursor.classList.remove('clicking'));
});

Click Ripple Effect
// Add click ripple visualization
await page.addStyleTag({
  content: `
    .click-ripple {
      position: fixed;
      width: 40px;
      height: 40px;
      border-radius: 50%;
      background: rgba(234, 88, 12, 0.4);
      pointer-events: none;
      z-index: 999998;
      transform: translate(-50%, -50%) scale(0);
      animation: ripple 0.4s ease-out forwards;
    }
    @keyframes ripple {
      to {
        transform: translate(-50%, -50%) scale(2);
        opacity: 0;
      }
    }
  `
});

// Custom click function with ripple
async function clickWithRipple(page, selector) {
  const element = await page.locator(selector);
  const box = await element.boundingBox();

  await page.evaluate(({ x, y }) => {
    const ripple = document.createElement('div');
    ripple.className = 'click-ripple';
    ripple.style.left = x + 'px';
    ripple.style.top = y + 'px';
    document.body.appendChild(ripple);
    setTimeout(() => ripple.remove(), 400);
  }, { x: box.x + box.width / 2, y: box.y + box.height / 2 });

  await element.click();
}

Output for Remotion
Move Recording to public/demos/
import { chromium } from 'playwright';
import * as fs from 'fs';
import * as path from 'path';

async function recordForRemotion(outputName: string) {
  const browser = await chromium.launch({ slowMo: 50 });
  const context = await browser.newContext({
    viewport: { width: 1920, height: 1080 },
    recordVideo: { dir: './temp-recordings', size: { width: 1920, height: 1080 } }
  });
  const page = await context.newPage();

  // ... recording actions ...

  await context.close();

  // Get the video path
  const video = page.video();
  const videoPath = await video?.path();

  if (videoPath) {
    const destPath = `./public/demos/${outputName}.webm`;
    fs.mkdirSync(path.dirname(destPath), { recursive: true });
    fs.renameSync(videoPath, destPath);
    console.log(`Recording saved to: ${destPath}`);

    // Get duration for config
    // Use ffprobe: ffprobe -v error -show_entries format=duration -of csv=p=0 file.webm
  }

  await browser.close();
}

Convert WebM to MP4

Playwright outputs WebM. Convert for better Remotion compatibility:

ffmpeg -i recording.webm -c:v libx264 -crf 20 -preset medium -movflags faststart public/demos/demo.mp4

Interactive Recording

For user-driven recordings where you manually perform actions:

// Inject ESC key listener to stop recording
async function injectStopListener(page: Page): Promise<void> {
  await page.evaluate(() => {
    if ((window as any).__escListenerAdded) return;
    (window as any).__escListenerAdded = true;
    (window as any).__stopRecording = false;
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        e.preventDefault();
        (window as any).__stopRecording = true;
      }
    });
  });
}

// Poll for stop signal - handle navigation errors gracefully
while (!stopped) {
  try {
    const shouldStop = await page.evaluate(() => (window as any).__stopRecording === true);
    if (shouldStop) break;
  } catch {
    // Page navigating - continue recording
  }
  await new Promise(r => setTimeout(r, 200));
}


Key insight: page.evaluate() throws during navigation. Use try/catch and continue - don't treat errors as stop signals.

Window Scaling for Laptops

Record at full 1080p while showing a smaller window:

const scale = 0.75; // 75% window size
const context = await browser.newContext({
  viewport: { width: 1920 * scale, height: 1080 * scale },
  deviceScaleFactor: 1 / scale,
  recordVideo: { dir: './recordings', size: { width: 1920, height: 1080 } },
});

Cookie Banner Dismissal

Comprehensive selector list for common consent platforms:

const COOKIE_SELECTORS = [
  '#onetrust-accept-btn-handler',           // OneTrust
  '#CybotCookiebotDialogBodyButtonAccept',  // Cookiebot
  '.cc-btn.cc-dismiss',                      // Cookie Consent by Insites
  '[class*="cookie"] button[class*="accept"]',
  '[class*="consent"] button[class*="accept"]',
  'button:has-text("Accept all")',
  'button:has-text("Accept cookies")',
  'button:has-text("Got it")',
];

async function dismissCookieBanners(page: Page): Promise<void> {
  await page.waitForTimeout(500);
  for (const selector of COOKIE_SELECTORS) {
    try {
      const btn = page.locator(selector).first();
      if (await btn.isVisible({ timeout: 100 })) {
        await btn.click({ timeout: 500 });
        return;
      }
    } catch { /* try next */ }
  }
}


Call after page.goto() and on page.on('load') for navigation.

Important: Injected Elements Appear in Video

Warning: Any DOM elements you inject (cursors, control panels, overlays) will be recorded. For UI-free recordings, use terminal-based controls only (Ctrl+C, max duration timer).

Tips for Good Demo Recordings
Use slowMo - 50-100ms makes actions visible
Add waitForTimeout - Pause between actions for comprehension
Wait for animations - Use waitForLoadState('networkidle')
Match Remotion dimensions - 1920x1080 at 30fps typical
Test without recording first - Debug before final capture
Clear browser state - Use fresh context for clean demos
Dismiss cookie banners - Use comprehensive selector list above
Re-inject on navigation - Cursor/listeners reset on page load
Feedback & Contributions

If this skill is missing information or could be improved:

Missing a pattern? Describe what you needed
Found an error? Let me know what's wrong
Want to contribute? I can help you:
Update this skill with improvements
Create a PR to github.com/digitalsamba/claude-code-video-toolkit

Just say "improve this skill" and I'll guide you through updating .claude/skills/playwright-recording/SKILL.md.

Weekly Installs
385
Repository
digitalsamba/cl…-toolkit
GitHub Stars
1.0K
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn