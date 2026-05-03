---
rating: ⭐⭐⭐
title: capacitor-performance
url: https://skills.sh/cap-go/capgo-skills/capacitor-performance
---

# capacitor-performance

skills/cap-go/capgo-skills/capacitor-performance
capacitor-performance
Installation
$ npx skills add https://github.com/cap-go/capgo-skills --skill capacitor-performance
SKILL.md
Performance Optimization for Capacitor

Make your Capacitor apps fast and responsive.

When to Use This Skill
User has slow app
User wants to optimize
User has memory issues
User needs profiling
User has janky animations
Quick Wins
1. Lazy Load Plugins
// BAD - All plugins loaded at startup
import { Camera } from '@capacitor/camera';
import { Filesystem } from '@capacitor/filesystem';
import { Geolocation } from '@capacitor/geolocation';

// GOOD - Load when needed
async function takePhoto() {
  const { Camera } = await import('@capacitor/camera');
  return Camera.getPhoto({ quality: 90 });
}

2. Reduce Bundle Size
# Analyze bundle
npx vite-bundle-visualizer

# Tree-shake imports
import { specific } from 'large-library';  // Good
import * as everything from 'large-library'; // Bad

3. Optimize Images
// Use appropriate quality
const photo = await Camera.getPhoto({
  quality: 80,        // Not 100
  width: 1024,        // Limit size
  resultType: CameraResultType.Uri,  // Not Base64
});

// Lazy load images
<img loading="lazy" src={url} />

4. Minimize Bridge Calls
// BAD - Multiple bridge calls
for (const item of items) {
  await Storage.set({ key: item.id, value: item.data });
}

// GOOD - Single call with batch
await Storage.set({
  key: 'items',
  value: JSON.stringify(items),
});

Rendering Performance
Use CSS Transforms
/* GPU accelerated */
.animated {
  transform: translateX(100px);
  will-change: transform;
}

/* Avoid - triggers layout */
.animated {
  left: 100px;
}

Virtual Scrolling
// Use virtual list for long lists
import { VirtualScroller } from 'your-framework';

<VirtualScroller
  items={items}
  itemHeight={60}
  renderItem={(item) => <ListItem item={item} />}
/>

Debounce Events
import { debounce } from 'lodash-es';

const handleScroll = debounce((e) => {
  // Handle scroll
}, 16); // ~60fps

Memory Management
Cleanup Listeners
import { App } from '@capacitor/app';

// Store listener handle
const handle = await App.addListener('appStateChange', callback);

// Cleanup on unmount
onUnmount(() => {
  handle.remove();
});

Avoid Memory Leaks
// Clear large data when done
let largeData = await fetchLargeData();
processData(largeData);
largeData = null; // Allow GC

Profiling
Chrome DevTools
Connect via chrome://inspect
Performance tab > Record
Analyze flame chart
Xcode Instruments
Product > Profile
Choose Time Profiler
Analyze hot paths
Android Profiler
View > Tool Windows > Profiler
Select CPU/Memory/Network
Record and analyze
Metrics to Track
Metric	Target
First Paint	< 1s
Time to Interactive	< 3s
Frame Rate	60fps
Memory	Stable, no growth
Bundle Size	< 500KB gzipped
Resources
Chrome DevTools: https://developer.chrome.com/docs/devtools
Xcode Instruments: https://developer.apple.com/instruments
Weekly Installs
254
Repository
cap-go/capgo-skills
GitHub Stars
31
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass