---
title: tv-navigator
url: https://skills.sh/dbobkov245-source/pwa-torserve/tv-navigator
---

# tv-navigator

skills/dbobkov245-source/pwa-torserve/tv-navigator
tv-navigator
Installation
$ npx skills add https://github.com/dbobkov245-source/pwa-torserve --skill tv-navigator
SKILL.md
TV Navigator Skill

This skill provides expertise in creating "TV-First" interfaces using the useTVNavigation hook. Your goal is to ensure every component is accessible via D-Pad (Arrow Keys) and handles focus states correctly.

🧠 Core Concepts
1. useTVNavigation Hook

Located in: client/src/hooks/useTVNavigation.js

Signature:

const { 
  focusedIndex,    // Current active index (0..N)
  setFocusedIndex, // Manually set focus
  containerProps,  // { onKeyDown, tabIndex } - spreads to parent container
  isFocused        // Helper: (index) => boolean
} = useTVNavigation({
  itemCount: number,      // Total items
  columns: number,        // 1 for List, >1 for Grid
  itemRefs: React.RefObject, // { current: { [index]: HTMLElement } }
  onSelect: (index) => void, // Enter/OK press
  onBack: () => void,     // Escape/Back press
  loop: boolean,          // Default: false
  trapFocus: boolean,     // true = Isolated (Modals), false = Global (HomeRow)
  isActive: boolean       // External control. If false, ignores all input.
})

2. Focus Visualization
NEVER use :hover for TV interfaces.
ALWAYS use the .focused state logic or conditional rendering based on focusedIndex.
For focused items, apply: border, transform: scale(1.05), or box-shadow.
3. Scroll Management

The hook automatically handles scrolling using scrollIntoView({ behavior: 'smooth', block: 'center' }). You must attach refs to items:

<div ref={el => itemRefs.current[index] = el} ... >

4. Integration with activeArea

The hook must respect the isActive flag.

If isActive === false: The hook ignores ALL key presses.
This allows other UI areas (like the Sidebar) to take over control without unmounting the grid.
🛠 Common Patterns
Vertical List (Menu)
const { containerProps, isFocused } = useTVNavigation({ 
  itemCount: items.length, 
  columns: 1 
});

Grid (Posters)
const { containerProps } = useTVNavigation({ 
  itemCount: items.length, 
  columns: 4 // or dynamic based on width
});

⚠️ Anti-Patterns to Avoid
Hidden Overflow: Avoid overflow: hidden on containers that need to scroll, unless you are implementing virtualized scrolling.
Missing TabIndex: The container MUST have tabIndex={0} (provided by containerProps) to capture keyboard events.
Mouse Dependency: Do not rely on onClick. Always map onSelect (Enter key) to the same handler.
Weekly Installs
23
Repository
dbobkov245-sour…torserve
GitHub Stars
1
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass