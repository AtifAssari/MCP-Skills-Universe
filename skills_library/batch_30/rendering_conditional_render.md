---
title: rendering-conditional-render
url: https://skills.sh/theorcdev/8bitcn-ui/rendering-conditional-render
---

# rendering-conditional-render

skills/theorcdev/8bitcn-ui/rendering-conditional-render
rendering-conditional-render
Installation
$ npx skills add https://github.com/theorcdev/8bitcn-ui --skill rendering-conditional-render
SKILL.md
Use Explicit Conditional Rendering

Use explicit ternary operators (? :) instead of && for conditional rendering when the condition can be 0, NaN, or other falsy values that render.

Incorrect (renders "0" when count is 0):

function Badge({ count }: { count: number }) {
  return (
    <div>
      {count && <span className="badge">{count}</span>}
    </div>
  )
}

// When count = 0, renders: <div>0</div>
// When count = 5, renders: <div><span class="badge">5</span></div>


Correct (renders nothing when count is 0):

function Badge({ count }: { count: number }) {
  return (
    <div>
      {count > 0 ? <span className="badge">{count}</span> : null}
    </div>
  )
}

// When count = 0, renders: <div></div>
// When count = 5, renders: <div><span class="badge">5</span></div>

Weekly Installs
22
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