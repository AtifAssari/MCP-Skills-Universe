---
title: anime-js
url: https://skills.sh/dylantarre/animation-principles/anime-js
---

# anime-js

skills/dylantarre/animation-principles/anime-js
anime-js
Installation
$ npx skills add https://github.com/dylantarre/animation-principles --skill anime-js
SKILL.md
Anime.js Animation Principles

Implement all 12 Disney animation principles using Anime.js's flexible animation engine.

1. Squash and Stretch
anime({
  targets: '.ball',
  scaleX: [1, 1.2, 1],
  scaleY: [1, 0.8, 1],
  duration: 300,
  easing: 'easeInOutQuad'
});

2. Anticipation
anime.timeline()
  .add({
    targets: '.character',
    translateY: 10,
    scaleY: 0.9,
    duration: 200
  })
  .add({
    targets: '.character',
    translateY: -200,
    duration: 400,
    easing: 'easeOutQuad'
  });

3. Staging
anime({
  targets: '.background',
  filter: 'blur(3px)',
  opacity: 0.6,
  duration: 500
});
anime({
  targets: '.hero',
  scale: 1.1,
  duration: 500
});

4. Straight Ahead / Pose to Pose
anime({
  targets: '.element',
  keyframes: [
    { translateX: 0, translateY: 0 },
    { translateX: 100, translateY: -50 },
    { translateX: 200, translateY: 0 },
    { translateX: 300, translateY: -30 }
  ],
  duration: 1000
});

5. Follow Through and Overlapping Action
anime.timeline()
  .add({ targets: '.body', translateX: 200, duration: 500 })
  .add({ targets: '.hair', translateX: 200, duration: 500 }, '-=450')
  .add({ targets: '.cape', translateX: 200, duration: 600 }, '-=500');

6. Slow In and Slow Out
anime({
  targets: '.element',
  translateX: 300,
  duration: 600,
  easing: 'easeInOutCubic'
});
// Options: easeInQuad, easeOutQuad, easeInOutQuad
// easeInCubic, easeOutCubic, easeInOutCubic
// spring(mass, stiffness, damping, velocity)

7. Arc
anime({
  targets: '.ball',
  translateX: 200,
  translateY: [
    { value: -100, duration: 500 },
    { value: 0, duration: 500 }
  ],
  easing: 'easeOutQuad',
  duration: 1000
});

// Or use SVG path
anime({
  targets: '.element',
  translateX: anime.path('.motion-path')('x'),
  translateY: anime.path('.motion-path')('y'),
  duration: 1000
});

8. Secondary Action
const tl = anime.timeline();
tl.add({
  targets: '.button',
  scale: 1.1,
  duration: 200
})
.add({
  targets: '.icon',
  rotate: 15,
  duration: 150
}, '-=150')
.add({
  targets: '.particles',
  opacity: [0, 1],
  delay: anime.stagger(50)
}, '-=100');

9. Timing
// Fast - snappy
anime({ targets: '.fast', translateX: 100, duration: 150 });

// Normal
anime({ targets: '.normal', translateX: 100, duration: 300 });

// Slow - dramatic
anime({ targets: '.slow', translateX: 100, duration: 600 });

// Spring physics
anime({ targets: '.spring', translateX: 100, easing: 'spring(1, 80, 10, 0)' });

10. Exaggeration
anime({
  targets: '.element',
  scale: 1.5,
  rotate: '2turn',
  duration: 800,
  easing: 'easeOutElastic(1, 0.5)' // overshoot
});

11. Solid Drawing
anime({
  targets: '.box',
  rotateX: 45,
  rotateY: 30,
  perspective: 1000,
  duration: 500
});

12. Appeal
anime({
  targets: '.card',
  scale: 1.02,
  boxShadow: '0 20px 40px rgba(0,0,0,0.2)',
  duration: 300,
  easing: 'easeOutQuad'
});

Stagger Animation
anime({
  targets: '.item',
  translateY: [20, 0],
  opacity: [0, 1],
  delay: anime.stagger(100), // 100ms between each
  easing: 'easeOutQuad'
});

Key Anime.js Features
anime.timeline() - Sequence animations
keyframes - Multiple poses
anime.stagger() - Offset delays
anime.path() - SVG motion paths
Built-in easings + spring() + elastic()
'-=200' - Relative offset timing
anime.set() - Instant property set
Weekly Installs
197
Repository
dylantarre/anim…inciples
GitHub Stars
35
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass