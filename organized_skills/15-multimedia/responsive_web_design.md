---
rating: ⭐⭐
title: responsive-web-design
url: https://skills.sh/secondsky/claude-skills/responsive-web-design
---

# responsive-web-design

skills/secondsky/claude-skills/responsive-web-design
responsive-web-design
Installation
$ npx skills add https://github.com/secondsky/claude-skills --skill responsive-web-design
SKILL.md
Responsive Web Design

Build adaptive interfaces using modern CSS techniques for all screen sizes.

Mobile-First Media Queries
/* Base: Mobile (320px+) */
.container {
  padding: 1rem;
}

/* Tablet (640px+) */
@media (min-width: 640px) {
  .container {
    padding: 2rem;
    max-width: 640px;
    margin: 0 auto;
  }
}

/* Desktop (1024px+) */
@media (min-width: 1024px) {
  .container {
    max-width: 1024px;
  }
}

Flexible Grid
.grid {
  display: grid;
  gap: 1rem;
  grid-template-columns: 1fr; /* Mobile: single column */
}

@media (min-width: 640px) {
  .grid {
    grid-template-columns: repeat(2, 1fr); /* Tablet: 2 columns */
  }
}

@media (min-width: 1024px) {
  .grid {
    grid-template-columns: repeat(3, 1fr); /* Desktop: 3 columns */
  }
}

Fluid Typography
/* Scales smoothly between breakpoints */
h1 {
  font-size: clamp(1.5rem, 4vw, 3rem);
}

p {
  font-size: clamp(1rem, 2vw, 1.25rem);
}

Responsive Images
img {
  max-width: 100%;
  height: auto;
}

.hero-image {
  width: 100%;
  aspect-ratio: 16 / 9;
  object-fit: cover;
}

Flexbox Navigation
.nav {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

@media (min-width: 768px) {
  .nav {
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
  }
}

Best Practices
Start with mobile styles first
Use flexible units (%, rem, vw)
Test on real devices
Ensure minimum 48px touch targets
Maintain readable line lengths (45-75 chars)
Use CSS Grid for 2D layouts, Flexbox for 1D
Resources
MDN Flexbox Guide
MDN Grid Guide
Weekly Installs
203
Repository
secondsky/claude-skills
GitHub Stars
129
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass