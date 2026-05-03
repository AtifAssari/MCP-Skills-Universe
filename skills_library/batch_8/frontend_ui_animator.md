---
title: frontend-ui-animator
url: https://skills.sh/julianromli/ai-skills/frontend-ui-animator
---

# frontend-ui-animator

skills/julianromli/ai-skills/frontend-ui-animator
frontend-ui-animator
Installation
$ npx skills add https://github.com/julianromli/ai-skills --skill frontend-ui-animator
SKILL.md
Frontend UI Animator

Implement purposeful, performant animations that enhance UX without overwhelming users. Focus on key moments: hero intros, hover feedback, content reveals, and navigation transitions.

Core Philosophy

"You don't need animations everywhere" - Prioritize:

Priority	Area	Purpose
1	Hero Intro	First impression, brand personality
2	Hover Interactions	Feedback, discoverability
3	Content Reveal	Guide attention, reduce cognitive load
4	Background Effects	Atmosphere, depth
5	Navigation Transitions	Spatial awareness, continuity
Workflow

Execute phases sequentially. Complete each before proceeding.

Phase 1: Analyze
Scan project structure - Identify all pages in app/ and components in components/
Check existing setup - Review tailwind.config.ts for existing animations/keyframes
Identify animation candidates - List components by priority category
Document constraints - Note installed animation libraries (framer-motion, etc.)

Output: Animation audit table. See references/component-checklist.md.

Phase 2: Plan
Map animations to components - Assign specific animation patterns
Determine triggers - Load, scroll (intersection), hover, click
Estimate effort - Low (CSS only), Medium (hooks needed), High (library required)
Propose phased rollout - Quick wins first

Output: Implementation plan with component → animation mapping.

Phase 3: Implement
Extend Tailwind config - Add keyframes and animation utilities
Add reduced-motion support - Accessibility first
Create reusable hooks - useScrollReveal, useMousePosition if needed
Apply animations per component - Follow patterns in references/animation-patterns.md

Performance rules:

// ✅ DO: Use transforms and opacity only
transform: translateY(20px);
opacity: 0.5;
filter: blur(4px);

// ❌ DON'T: Animate layout properties
margin-top: 20px;
height: 100px;
width: 200px;

Phase 4: Verify
Test in browser - Visual QA all animations
Test reduced-motion - Verify prefers-reduced-motion works
Check CLS - No layout shifts from animations
Performance audit - No jank on scroll animations
Quick Reference
Animation Triggers
Trigger	Implementation
Page load	CSS animation with animation-delay for stagger
Scroll into view	IntersectionObserver or react-intersection-observer
Hover	Tailwind hover: utilities or CSS :hover
Click/Tap	State-driven with useState
Common Patterns

Staggered children:

{items.map((item, i) => (
  <div 
    key={item.id}
    style={{ animationDelay: `${i * 100}ms` }}
    className="animate-fade-slide-in"
  />
))}


Scroll reveal hook:

const useScrollReveal = (threshold = 0.1) => {
  const ref = useRef<HTMLDivElement>(null);
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => entry.isIntersecting && setIsVisible(true),
      { threshold }
    );
    if (ref.current) observer.observe(ref.current);
    return () => observer.disconnect();
  }, [threshold]);

  return { ref, isVisible };
};


Usage:

const { ref, isVisible } = useScrollReveal();
<div ref={ref} className={isVisible ? 'animate-fade-in' : 'opacity-0'} />

Resources
Animation patterns: See references/animation-patterns.md
Audit template: See references/component-checklist.md
Tailwind presets: See references/tailwind-presets.md
Technical Stack
CSS animations: Default for simple effects
Tailwind utilities: For hover states and basic animations
Framer Motion: For complex orchestration, gestures, layout animations
GSAP: For timeline-based sequences (if already installed)
Accessibility (Required)

Always include in global CSS:

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
  }
}

Weekly Installs
335
Repository
julianromli/ai-skills
GitHub Stars
155
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass