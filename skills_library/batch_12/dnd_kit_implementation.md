---
title: dnd-kit-implementation
url: https://skills.sh/atman-33/skills/dnd-kit-implementation
---

# dnd-kit-implementation

skills/atman-33/skills/dnd-kit-implementation
dnd-kit-implementation
Installation
$ npx skills add https://github.com/atman-33/skills --skill dnd-kit-implementation
SKILL.md
dnd-kit Implementation Guide
Overview

This skill provides patterns for implementing drag-and-drop functionality using dnd-kit library that supports both sortable containers and droppable targets simultaneously.

Core Concept

The key to combining useSortable and useDroppable is conditional logic based on drag context:

When dragging items → containers act as drop-only targets
When dragging containers → containers act as sortable elements

This is achieved by detecting what's currently being dragged and enabling only the appropriate functionality.

Implementation Pattern
Container Component Structure
const SortableDroppableContainer = ({ container }) => {
  // useSortable for container reordering
  const {
    attributes,
    listeners,
    setNodeRef: setSortableRef,
    transform,
    transition,
    isDragging,
  } = useSortable({ id: container.id });

  // useDroppable for receiving items
  const { setNodeRef: setDroppableRef, isOver } = useDroppable({
    id: container.id,
  });

  // Active element from context
  const { active } = useDndContext();

  // Determine behavior based on what's being dragged
  const isItem = active?.id?.toString().startsWith('item-');
  const isContainer = active?.id?.toString().startsWith('container-');

  // Apply conditional refs
  const setNodeRef = isItem ? setDroppableRef : setSortableRef;

  return (
    <div ref={setNodeRef} {...(isContainer ? attributes : {})} style={style}>
      <div {...(isContainer ? listeners : {})}>{/* Drag handle */}</div>
      {/* Container content */}
    </div>
  );
};

Key Implementation Points
Dual Hook Usage: Use both useSortable and useDroppable in the same component
Context Detection: Use useDndContext() to check what's being dragged
Conditional Refs: Apply the appropriate ref based on drag state
ID Naming Convention: Use prefixes like container-* and item-* to distinguish types
ID Naming Convention
// Containers
const containerId = `container-${id}`;

// Items
const itemId = `item-${id}`;


This convention makes conditional logic clean and maintainable.

State Management Critical Point

When updating container items, always create new objects:

// ❌ Won't trigger re-render
containers.items.push(newItem);

// ✅ Correct - creates new reference
setContainers(prev => prev.map(c =>
  c.id === targetId
    ? { ...c, items: [...c.items, newItem] }
    : c
));

Common Use Cases
Kanban Boards: Reorder columns and move cards between columns
File Management: Reorganize folders and move files into folders
Playlist Editors: Reorder playlists and add songs to playlists
Task Managers: Reorder task lists and move tasks between lists
References

For detailed implementation examples and code patterns, see:

implementation-patterns.md - Complete component examples with TypeScript
state-management.md - State update patterns and common pitfalls
Weekly Installs
24
Repository
atman-33/skills
First Seen
Feb 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass