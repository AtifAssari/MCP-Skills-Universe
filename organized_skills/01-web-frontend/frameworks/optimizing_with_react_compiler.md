---
rating: ⭐⭐
title: optimizing-with-react-compiler
url: https://skills.sh/djankies/claude-configs/optimizing-with-react-compiler
---

# optimizing-with-react-compiler

skills/djankies/claude-configs/optimizing-with-react-compiler
optimizing-with-react-compiler
Installation
$ npx skills add https://github.com/djankies/claude-configs --skill optimizing-with-react-compiler
SKILL.md
React Compiler Awareness

React Compiler (available separately) automatically memoizes code, reducing need for manual optimization. (verify use in project before using this skill)

What React Compiler Handles

Automatically memoizes:

Component re-renders
Expensive calculations
Function references
Object/array creation

Before (Manual Memoization):

function Component({ items }) {
  const sortedItems = useMemo(() => {
    return [...items].sort((a, b) => a.name.localeCompare(b.name));
  }, [items]);

  const handleClick = useCallback(() => {
    console.log('Clicked');
  }, []);

  return <List items={sortedItems} onClick={handleClick} />;
}


After (React Compiler):

function Component({ items }) {
  const sortedItems = [...items].sort((a, b) => a.name.localeCompare(b.name));

  const handleClick = () => {
    console.log('Clicked');
  };

  return <List items={sortedItems} onClick={handleClick} />;
}

When Manual Memoization Still Needed

Keep useMemo when:

Extremely expensive calculations (> 100ms)
Third-party libraries require stable references
React Profiler shows specific performance issues

Keep React.memo when:

Component re-renders are very expensive
Props rarely change but parent re-renders often
Verified performance improvement with Profiler
Performance Best Practices

Do:

Trust React Compiler for most optimizations
Keep components small and focused
Keep state local
Use children prop pattern

Don't:

Add premature memoization
Over-engineer performance
Skip measuring actual impact

For comprehensive React Compiler information, see: research/react-19-comprehensive.md lines 1179-1223.

Weekly Installs
14
Repository
djankies/claude-configs
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass