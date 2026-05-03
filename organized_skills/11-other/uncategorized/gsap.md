---
rating: ⭐⭐⭐
title: gsap
url: https://skills.sh/mindrally/skills/gsap
---

# gsap

skills/mindrally/skills/gsap
gsap
Installation
$ npx skills add https://github.com/mindrally/skills --skill gsap
SKILL.md
GSAP Animation Guidelines

You are an expert in GSAP (GreenSock Animation Platform), JavaScript, and web animation performance. Follow these guidelines when creating animations.

Core Principles
Import and Setup
// Modern ES Module import
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

// Register plugins
gsap.registerPlugin(ScrollTrigger);

Use gsap.to(), gsap.from(), and gsap.fromTo()
// Animate TO a state
gsap.to(".element", { x: 100, duration: 1 });

// Animate FROM a state
gsap.from(".element", { opacity: 0, y: 50, duration: 0.5 });

// Animate FROM one state TO another
gsap.fromTo(".element",
  { opacity: 0 },
  { opacity: 1, duration: 0.5 }
);

Performance Optimization
Leverage Hardware Acceleration
// Use transforms instead of positional properties
gsap.to(".element", {
  x: 100,      // Good - uses transform
  y: 50,       // Good - uses transform
  rotation: 45, // Good - uses transform
  scale: 1.2,  // Good - uses transform
  // Avoid: left, top, width, height when possible
});

// Enable force3D for GPU acceleration
gsap.to(".element", {
  x: 100,
  force3D: true // Ensures GPU acceleration
});

Use will-change Wisely
// Apply will-change before animation
element.style.willChange = "transform";

gsap.to(element, {
  x: 100,
  onComplete: () => {
    element.style.willChange = "auto"; // Remove after animation
  }
});

Stagger for Multiple Elements
// Always use stagger for multiple elements
gsap.to(".items", {
  opacity: 1,
  y: 0,
  stagger: 0.1, // Prevents all elements animating at once
  duration: 0.5
});

// Advanced stagger options
gsap.to(".grid-items", {
  scale: 1,
  stagger: {
    each: 0.1,
    from: "center",
    grid: "auto"
  }
});

Use Lag Smoothing
// Prevent animation stuttering during CPU spikes
gsap.ticker.lagSmoothing(1000, 16);

Timeline Best Practices
Use Timelines for Complex Sequences
const tl = gsap.timeline({
  defaults: { duration: 0.5, ease: "power2.out" }
});

tl.to(".header", { y: 0, opacity: 1 })
  .to(".content", { y: 0, opacity: 1 }, "-=0.3") // Overlap
  .to(".footer", { y: 0, opacity: 1 }, "-=0.3");

Use Labels for Organization
const tl = gsap.timeline();

tl.addLabel("start")
  .to(".intro", { opacity: 1 })
  .addLabel("middle")
  .to(".main", { x: 100 })
  .addLabel("end")
  .to(".outro", { opacity: 0 });

// Jump to label
tl.play("middle");

Control Timelines
const tl = gsap.timeline({ paused: true });

// Methods
tl.play();
tl.pause();
tl.reverse();
tl.restart();
tl.seek(1.5); // Go to 1.5 seconds
tl.progress(0.5); // Go to 50%

ScrollTrigger Best Practices
Basic ScrollTrigger Setup
gsap.to(".element", {
  x: 500,
  scrollTrigger: {
    trigger: ".element",
    start: "top center",
    end: "bottom center",
    scrub: true,
    markers: false // Enable for debugging only
  }
});

Pin Elements Properly
ScrollTrigger.create({
  trigger: ".panel",
  pin: true,
  start: "top top",
  end: "+=500",
  pinSpacing: true
});

Batch ScrollTriggers for Performance
ScrollTrigger.batch(".items", {
  onEnter: (elements) => {
    gsap.to(elements, {
      opacity: 1,
      y: 0,
      stagger: 0.1
    });
  }
});

React Integration
Use useGSAP Hook
import { useGSAP } from "@gsap/react";

function Component() {
  const containerRef = useRef(null);

  useGSAP(() => {
    gsap.to(".box", { x: 100 });
  }, { scope: containerRef }); // Scopes selectors to container

  return <div ref={containerRef}>...</div>;
}

Cleanup Animations
useGSAP(() => {
  const tl = gsap.timeline();
  tl.to(".element", { x: 100 });

  return () => {
    tl.kill(); // Clean up on unmount
  };
}, []);

Selector Optimization
Cache DOM Selectors
// Bad - queries DOM on every call
gsap.to(".element", { x: 100 });
gsap.to(".element", { y: 50 });

// Good - cache the reference
const element = document.querySelector(".element");
gsap.to(element, { x: 100 });
gsap.to(element, { y: 50 });

Use gsap.utils for Efficiency
// Convert NodeList to Array
const items = gsap.utils.toArray(".items");

// Create reusable selector
const select = gsap.utils.selector(container);
gsap.to(select(".box"), { x: 100 });

Easing
Use Appropriate Eases
// Common eases for UI
gsap.to(".element", { x: 100, ease: "power2.out" }); // Decelerate
gsap.to(".element", { x: 100, ease: "power2.in" });  // Accelerate
gsap.to(".element", { x: 100, ease: "power2.inOut" }); // Both

// Bounce and elastic for playful UI
gsap.to(".element", { y: 0, ease: "bounce.out" });
gsap.to(".element", { scale: 1, ease: "elastic.out(1, 0.3)" });

SVG Animation
Animate SVG Properties
gsap.to("path", {
  strokeDashoffset: 0,
  duration: 2,
  ease: "none"
});

gsap.to("circle", {
  attr: { r: 50, cx: 200 },
  duration: 1
});

Complex Animations
Use MotionPath for Path Animation
import { MotionPathPlugin } from "gsap/MotionPathPlugin";
gsap.registerPlugin(MotionPathPlugin);

gsap.to(".element", {
  motionPath: {
    path: "#path",
    align: "#path",
    autoRotate: true
  },
  duration: 5
});

Debugging
Use Markers During Development
ScrollTrigger.defaults({
  markers: process.env.NODE_ENV === "development"
});

Debug Timeline Progress
tl.eventCallback("onUpdate", () => {
  console.log(tl.progress());
});

Best Practices Summary
Always use transforms over positional properties
Use stagger for animating multiple elements
Leverage timelines for complex sequences
Cache DOM selectors
Use useGSAP hook in React
Clean up animations on component unmount
Enable lag smoothing for smooth playback
Test on actual devices, especially mobile
Weekly Installs
294
Repository
mindrally/skills
GitHub Stars
88
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass