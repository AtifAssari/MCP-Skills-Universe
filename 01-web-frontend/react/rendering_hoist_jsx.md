---
title: rendering-hoist-jsx
url: https://skills.sh/theorcdev/8bitcn-ui/rendering-hoist-jsx
---

# rendering-hoist-jsx

skills/theorcdev/8bitcn-ui/rendering-hoist-jsx
rendering-hoist-jsx
Installation
$ npx skills add https://github.com/theorcdev/8bitcn-ui --skill rendering-hoist-jsx
SKILL.md
Hoist Static JSX Elements

Extract static JSX outside components to avoid re-creation.

Incorrect (recreates element every render):

function LoadingSkeleton() {
  return <div className="animate-pulse h-20 bg-gray-200" />
}

function Container() {
  return (
    <div>
      {loading && <LoadingSkeleton />}
    </div>
  )
}


Correct (reuses same element):

const loadingSkeleton = (
  <div className="animate-pulse h-20 bg-gray-200" />
)

function Container() {
  return (
    <div>
      {loading && loadingSkeleton}
    </div>
  )
}


This is especially helpful for large and static SVG nodes, which can be expensive to recreate on every render.

Note: If your project has React Compiler enabled, the compiler automatically hoists static JSX elements and optimizes component re-renders, making manual hoisting unnecessary.

Weekly Installs
24
Repository
theorcdev/8bitcn-ui
GitHub Stars
1.8K
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass