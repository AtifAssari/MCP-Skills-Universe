---
title: frontend-development
url: https://skills.sh/gemini960114/skills/frontend-development
---

# frontend-development

skills/gemini960114/skills/frontend-development
frontend-development
Installation
$ npx skills add https://github.com/gemini960114/skills --skill frontend-development
SKILL.md
Frontend Development Instructions

This skill provides general guidance for frontend development across various projects. Use this when working with web-based user interfaces, regardless of the specific framework or library.

General Principles
Code Organization
Separate concerns: HTML for structure, CSS for styling, JavaScript for behavior
Use semantic HTML elements for accessibility
Keep CSS modular and maintainable
Avoid global variable pollution using modules or IIFEs
Performance
Minimize DOM manipulations
Use CSS animations over JavaScript when possible
Lazy load images and resources
Debounce/throttle event handlers
Use requestAnimationFrame for animations
Accessibility
Use proper ARIA labels
Ensure keyboard navigation works
Maintain sufficient color contrast
Provide alt text for images
Common Patterns
Event Handling
// Event delegation for multiple elements
document.querySelector('.container').addEventListener('click', (e) => {
  if (e.target.matches('.btn')) {
    handleButtonClick(e);
  }
});

// Debounced input handler
function debounce(fn, delay) {
  let timeout;
  return (...args) => {
    clearTimeout(timeout);
    timeout = setTimeout(() => fn(...args), delay);
  };
}

DOM Manipulation
// Efficient DOM updates
const fragment = document.createDocumentFragment();
items.forEach(item => {
  const li = document.createElement('li');
  li.textContent = item.name;
  fragment.appendChild(li);
});
document.querySelector('#list').appendChild(fragment);

// Template literals for dynamic HTML
const html = `<div class="card">
  <h3>${title}</h3>
  <p>${description}</p>
</div>`;

State Management
// Simple state management
class StateManager {
  constructor() {
    this.state = {};
    this.listeners = [];
  }

  getState(key) {
    return this.state[key];
  }

  setState(key, value) {
    this.state[key] = value;
    this.listeners.forEach(fn => fn(this.state));
  }

  subscribe(fn) {
    this.listeners.push(fn);
    return () => {
      this.listeners = this.listeners.filter(f => f !== fn);
    };
  }
}

Fetch API
// GET request
async function fetchData(url) {
  try {
    const response = await fetch(url);
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    return await response.json();
  } catch (error) {
    console.error('Fetch failed:', error);
    throw error;
  }
}

// POST request with JSON
async function postData(url, data) {
  const response = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
  return response.json();
}

CSS Best Practices
/* Use CSS custom properties */
:root {
  --primary-color: #007bff;
  --spacing: 1rem;
}

/* Mobile-first responsive */
.container {
  padding: var(--spacing);
}

@media (min-width: 768px) {
  .container {
    max-width: 1200px;
    margin: 0 auto;
  }
}

/* Efficient selectors */
.card { /* Avoid overly specific selectors */ }
.card__title { }
.card__title--highlighted { }

Framework-Specific Notes
React
Use functional components with hooks
Keep components small and focused
Use useMemo/useCallback for expensive operations
Follow ESLint rules for React
Vue
Use Composition API for better code organization
Leverage computed properties for derived state
Use v-for with :key for list rendering
Vanilla JavaScript
Use ES6+ features (const/let, arrow functions, destructuring)
Prefer modules over script tags
Use modern APIs (fetch, IntersectionObserver, etc.)
Debugging
Browser DevTools
Use Console API effectively: console.log, console.warn, console.error
Use breakpoints for step-through debugging
Inspect network requests in Network tab
Check Application tab for localStorage/sessionStorage
Common Issues
CORS errors: Check server headers
Memory leaks: Monitor in Performance tab
Layout shifts: Check for dynamic content loading
Event listener issues: Verify cleanup in useEffect/destroy
Build Tools
Vite
npm create vite@latest my-app -- --template vanilla
npm install
npm run dev

Webpack
Configure loaders for different file types
Use code splitting for large apps
Enable production optimizations
Testing
Unit Testing
// Simple test example
function sum(a, b) {
  return a + b;
}

// Test
function testSum() {
  const result = sum(2, 3);
  console.assert(result === 5, 'Expected sum to be 5');
}

E2E Testing
Use Playwright or Cypress for end-to-end tests
Test critical user flows
Mock external APIs when needed
Performance Optimization
Core Web Vitals
LCP (Largest Contentful Paint): < 2.5s
FID (First Input Delay): < 100ms
CLS (Cumulative Layout Shift): < 0.1
Techniques
Optimize images (WebP, compression)
Minify CSS/JS
Use CDN for static assets
Implement caching strategies
Weekly Installs
10
Repository
gemini960114/skills
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass