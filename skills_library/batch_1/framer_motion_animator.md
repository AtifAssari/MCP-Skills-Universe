---
title: framer-motion-animator
url: https://skills.sh/patricio0312rev/skills/framer-motion-animator
---

# framer-motion-animator

skills/patricio0312rev/skills/framer-motion-animator
framer-motion-animator
Installation
$ npx skills add https://github.com/patricio0312rev/skills --skill framer-motion-animator
Summary

Smooth animations and micro-interactions using Framer Motion's declarative API.

Supports entrance/exit animations, hover states, gesture-driven interactions (drag, swipe), and scroll-triggered effects with useInView and useScroll
Includes variants pattern for orchestrating staggered sequences, shared layout animations with LayoutGroup, and imperative control via useAnimate
Provides page transitions for Next.js, parallax effects, and scroll progress tracking through motion values and transforms
Built-in accessibility support via useReducedMotion hook; emphasizes GPU-accelerated properties (opacity, transform) and spring physics for natural motion
SKILL.md
Framer Motion Animator

Build delightful animations and interactions with Framer Motion's declarative API.

Core Workflow
Identify animation needs: Entrance, exit, hover, gestures
Choose animation type: Simple, variants, gestures, layout
Define motion values: Opacity, scale, position, rotation
Add transitions: Duration, easing, spring physics
Orchestrate sequences: Stagger, delay, parent-child
Optimize performance: GPU-accelerated properties
Installation
npm install framer-motion

Basic Animations
Simple Animation
import { motion } from 'framer-motion';

// Animate on mount
export function FadeIn({ children }: { children: React.ReactNode }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    >
      {children}
    </motion.div>
  );
}

// Animate on hover
export function ScaleOnHover({ children }: { children: React.ReactNode }) {
  return (
    <motion.div
      whileHover={{ scale: 1.05 }}
      whileTap={{ scale: 0.95 }}
      transition={{ type: 'spring', stiffness: 400, damping: 17 }}
    >
      {children}
    </motion.div>
  );
}

Exit Animations with AnimatePresence
import { motion, AnimatePresence } from 'framer-motion';

export function Modal({ isOpen, onClose, children }: ModalProps) {
  return (
    <AnimatePresence>
      {isOpen && (
        <>
          {/* Backdrop */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={onClose}
            className="fixed inset-0 bg-black/50 z-40"
          />

          {/* Modal */}
          <motion.div
            initial={{ opacity: 0, scale: 0.95, y: 20 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.95, y: 20 }}
            transition={{ type: 'spring', damping: 25, stiffness: 300 }}
            className="fixed inset-0 z-50 flex items-center justify-center"
          >
            <div className="bg-white rounded-xl p-6 max-w-md w-full">
              {children}
            </div>
          </motion.div>
        </>
      )}
    </AnimatePresence>
  );
}

Variants Pattern
Staggered Children
const containerVariants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      staggerChildren: 0.1,
      delayChildren: 0.2,
    },
  },
};

const itemVariants = {
  hidden: { opacity: 0, y: 20 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { type: 'spring', stiffness: 300, damping: 24 },
  },
};

export function StaggeredList({ items }: { items: string[] }) {
  return (
    <motion.ul
      variants={containerVariants}
      initial="hidden"
      animate="visible"
    >
      {items.map((item, index) => (
        <motion.li key={index} variants={itemVariants}>
          {item}
        </motion.li>
      ))}
    </motion.ul>
  );
}

Interactive Variants
const buttonVariants = {
  initial: { scale: 1 },
  hover: { scale: 1.05 },
  tap: { scale: 0.95 },
  disabled: { opacity: 0.5, scale: 1 },
};

export function AnimatedButton({
  children,
  disabled,
  onClick,
}: ButtonProps) {
  return (
    <motion.button
      variants={buttonVariants}
      initial="initial"
      whileHover={disabled ? 'disabled' : 'hover'}
      whileTap={disabled ? 'disabled' : 'tap'}
      animate={disabled ? 'disabled' : 'initial'}
      onClick={onClick}
      disabled={disabled}
      className="px-4 py-2 bg-blue-500 text-white rounded-lg"
    >
      {children}
    </motion.button>
  );
}

Page Transitions
Next.js App Router
// app/template.tsx
'use client';

import { motion } from 'framer-motion';

export default function Template({ children }: { children: React.ReactNode }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: 20 }}
      transition={{ duration: 0.3 }}
    >
      {children}
    </motion.div>
  );
}

Shared Layout Animations
import { motion, LayoutGroup } from 'framer-motion';

export function Tabs({ tabs, activeTab, onTabChange }: TabsProps) {
  return (
    <LayoutGroup>
      <div className="flex gap-2">
        {tabs.map((tab) => (
          <button
            key={tab.id}
            onClick={() => onTabChange(tab.id)}
            className="relative px-4 py-2"
          >
            {activeTab === tab.id && (
              <motion.div
                layoutId="activeTab"
                className="absolute inset-0 bg-blue-500 rounded-lg"
                transition={{ type: 'spring', stiffness: 500, damping: 30 }}
              />
            )}
            <span className="relative z-10">{tab.label}</span>
          </button>
        ))}
      </div>
    </LayoutGroup>
  );
}

Gesture Animations
Drag
export function DraggableCard() {
  return (
    <motion.div
      drag
      dragConstraints={{ left: -100, right: 100, top: -100, bottom: 100 }}
      dragElastic={0.2}
      dragTransition={{ bounceStiffness: 600, bounceDamping: 20 }}
      whileDrag={{ scale: 1.1, cursor: 'grabbing' }}
      className="w-32 h-32 bg-blue-500 rounded-lg cursor-grab"
    />
  );
}

Swipe to Dismiss
export function SwipeToDelete({ onDelete, children }: SwipeProps) {
  return (
    <motion.div
      drag="x"
      dragConstraints={{ left: 0, right: 0 }}
      onDragEnd={(_, info) => {
        if (info.offset.x < -100) {
          onDelete();
        }
      }}
      className="relative"
    >
      {children}
      <motion.div
        className="absolute right-0 inset-y-0 bg-red-500 flex items-center px-4"
        style={{ opacity: 0 }}
        animate={{ opacity: 1 }}
      >
        Delete
      </motion.div>
    </motion.div>
  );
}

Scroll Animations
Scroll-Triggered
import { motion, useInView } from 'framer-motion';
import { useRef } from 'react';

export function FadeInWhenVisible({ children }: { children: React.ReactNode }) {
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true, margin: '-100px' });

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, y: 50 }}
      animate={isInView ? { opacity: 1, y: 0 } : { opacity: 0, y: 50 }}
      transition={{ duration: 0.6, ease: 'easeOut' }}
    >
      {children}
    </motion.div>
  );
}

Scroll Progress
import { motion, useScroll, useTransform } from 'framer-motion';

export function ParallaxHero() {
  const { scrollY } = useScroll();
  const y = useTransform(scrollY, [0, 500], [0, 150]);
  const opacity = useTransform(scrollY, [0, 300], [1, 0]);

  return (
    <motion.div
      style={{ y, opacity }}
      className="h-screen flex items-center justify-center"
    >
      <h1 className="text-6xl font-bold">Parallax Hero</h1>
    </motion.div>
  );
}

export function ScrollProgress() {
  const { scrollYProgress } = useScroll();

  return (
    <motion.div
      style={{ scaleX: scrollYProgress }}
      className="fixed top-0 left-0 right-0 h-1 bg-blue-500 origin-left z-50"
    />
  );
}

Animation Hooks
useAnimate (Imperative)
import { useAnimate } from 'framer-motion';

export function SubmitButton() {
  const [scope, animate] = useAnimate();

  const handleClick = async () => {
    // Sequence of animations
    await animate(scope.current, { scale: 0.95 }, { duration: 0.1 });
    await animate(scope.current, { scale: 1 }, { type: 'spring' });

    // Success animation
    await animate(
      scope.current,
      { backgroundColor: '#22c55e' },
      { duration: 0.2 }
    );
  };

  return (
    <motion.button ref={scope} onClick={handleClick} className="px-4 py-2">
      Submit
    </motion.button>
  );
}

useMotionValue & useTransform
import { motion, useMotionValue, useTransform } from 'framer-motion';

export function RotatingCard() {
  const x = useMotionValue(0);
  const rotateY = useTransform(x, [-200, 200], [-45, 45]);
  const opacity = useTransform(x, [-200, 0, 200], [0.5, 1, 0.5]);

  return (
    <motion.div
      drag="x"
      dragConstraints={{ left: -200, right: 200 }}
      style={{ x, rotateY, opacity }}
      className="w-64 h-96 bg-gradient-to-br from-purple-500 to-pink-500 rounded-xl"
    />
  );
}

Reusable Animation Components
AnimatedContainer
// components/AnimatedContainer.tsx
import { motion, Variants } from 'framer-motion';

const animations: Record<string, Variants> = {
  fadeIn: {
    hidden: { opacity: 0 },
    visible: { opacity: 1 },
  },
  fadeInUp: {
    hidden: { opacity: 0, y: 20 },
    visible: { opacity: 1, y: 0 },
  },
  fadeInDown: {
    hidden: { opacity: 0, y: -20 },
    visible: { opacity: 1, y: 0 },
  },
  scaleIn: {
    hidden: { opacity: 0, scale: 0.8 },
    visible: { opacity: 1, scale: 1 },
  },
  slideInLeft: {
    hidden: { opacity: 0, x: -50 },
    visible: { opacity: 1, x: 0 },
  },
  slideInRight: {
    hidden: { opacity: 0, x: 50 },
    visible: { opacity: 1, x: 0 },
  },
};

interface AnimatedContainerProps {
  children: React.ReactNode;
  animation?: keyof typeof animations;
  delay?: number;
  duration?: number;
  className?: string;
}

export function AnimatedContainer({
  children,
  animation = 'fadeInUp',
  delay = 0,
  duration = 0.5,
  className,
}: AnimatedContainerProps) {
  return (
    <motion.div
      variants={animations[animation]}
      initial="hidden"
      animate="visible"
      transition={{ duration, delay, ease: 'easeOut' }}
      className={className}
    >
      {children}
    </motion.div>
  );
}

AnimatedList
// components/AnimatedList.tsx
import { motion } from 'framer-motion';

const containerVariants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      staggerChildren: 0.05,
    },
  },
};

const itemVariants = {
  hidden: { opacity: 0, x: -20 },
  visible: { opacity: 1, x: 0 },
};

interface AnimatedListProps<T> {
  items: T[];
  renderItem: (item: T, index: number) => React.ReactNode;
  keyExtractor: (item: T, index: number) => string;
  className?: string;
}

export function AnimatedList<T>({
  items,
  renderItem,
  keyExtractor,
  className,
}: AnimatedListProps<T>) {
  return (
    <motion.ul
      variants={containerVariants}
      initial="hidden"
      animate="visible"
      className={className}
    >
      {items.map((item, index) => (
        <motion.li key={keyExtractor(item, index)} variants={itemVariants}>
          {renderItem(item, index)}
        </motion.li>
      ))}
    </motion.ul>
  );
}

Transition Presets
// lib/transitions.ts
export const transitions = {
  spring: {
    type: 'spring',
    stiffness: 300,
    damping: 24,
  },
  springBouncy: {
    type: 'spring',
    stiffness: 500,
    damping: 15,
  },
  springStiff: {
    type: 'spring',
    stiffness: 700,
    damping: 30,
  },
  smooth: {
    type: 'tween',
    duration: 0.3,
    ease: 'easeInOut',
  },
  snappy: {
    type: 'tween',
    duration: 0.15,
    ease: [0.25, 0.1, 0.25, 1],
  },
} as const;

// Usage
<motion.div transition={transitions.spring} />

Reduced Motion Support
import { useReducedMotion } from 'framer-motion';

export function AccessibleAnimation({ children }: { children: React.ReactNode }) {
  const shouldReduceMotion = useReducedMotion();

  return (
    <motion.div
      initial={{ opacity: 0, y: shouldReduceMotion ? 0 : 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: shouldReduceMotion ? 0 : 0.5 }}
    >
      {children}
    </motion.div>
  );
}

Best Practices
Use GPU-accelerated properties: opacity, transform (not width, height)
Add layout for smooth resizing: Automatic layout animations
Use AnimatePresence: For exit animations
Prefer springs: More natural than tween for UI
Respect reduced motion: Use useReducedMotion hook
Avoid animating layout thrashing: Don't animate top, left, width
Use layoutId: For shared element transitions
Stagger children: For list animations
Output Checklist

Every animation implementation should include:

 Appropriate animation type (simple, variants, gestures)
 Smooth transitions with proper easing
 Exit animations with AnimatePresence
 Reduced motion support
 GPU-accelerated properties only
 Spring physics for natural feel
 Staggered children for lists
 Performance tested on low-end devices
Weekly Installs
3.9K
Repository
patricio0312rev/skills
GitHub Stars
35
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass