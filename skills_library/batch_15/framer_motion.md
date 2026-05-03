---
title: framer-motion
url: https://skills.sh/huynhsang2005/blog-tanstack/framer-motion
---

# framer-motion

skills/huynhsang2005/blog-tanstack/framer-motion
framer-motion
Installation
$ npx skills add https://github.com/huynhsang2005/blog-tanstack --skill framer-motion
SKILL.md
Framer Motion Skill
When to use
Adding page transitions or route animations.
Creating component enter/exit animations.
Building gesture interactions (drag, hover, tap).
Animating lists with stagger effects.
Guardrails
Keep animations under 300ms for snappiness.
Always respect prefers-reduced-motion.
Use variants for complex, coordinated animations (not inline).
Animate transform/opacity only (avoid layout thrash).
Workflow checklist
Identify what should animate and when (mount, route change, user interaction).
Define variants for multi-state animations (initial, animate, exit).
Use motion components (motion.div, motion.span) for animated elements.
Coordinate children with staggerChildren in parent variants.
Test with reduced motion to ensure accessible fallbacks.
Common patterns
Page transitions
import { motion } from 'framer-motion'

export function PageTransition({ children }: { children: React.ReactNode }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -20 }}
      transition={{ duration: 0.3 }}
    >
      {children}
    </motion.div>
  )
}

Stagger children
const container = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: {
      staggerChildren: 0.1
    }
  }
}

const item = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0 }
}

<motion.div variants={container} initial="hidden" animate="show">
  {items.map(item => (
    <motion.div key={item.id} variants={item}>
      {item.content}
    </motion.div>
  ))}
</motion.div>

Best practices
✅ Use variants for readability and reusability
✅ Keep duration under 300ms for UI responsiveness
✅ Animate transform/opacity (GPU-accelerated)
✅ Add layout prop for automatic layout animations
❌ Don't animate width/height directly (causes layout thrash)
❌ Don't nest many motion components (performance)
References
Library patterns: docs/dev-1/docs/16-library-patterns.md#framer-motion
Design system: docs/dev-1/docs/13-unified-design-system.md (animation tokens)
Tooling
Use Context7 or web search for framer-motion API details when needed.
Weekly Installs
18
Repository
huynhsang2005/b…tanstack
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass