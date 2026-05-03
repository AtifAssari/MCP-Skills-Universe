---
title: react-useref
url: https://skills.sh/b4r7x/agent-skills/react-useref
---

# react-useref

skills/b4r7x/agent-skills/react-useref
react-useref
Installation
$ npx skills add https://github.com/b4r7x/agent-skills --skill react-useref
SKILL.md
React useRef
Overview

useRef is a "box" for a value that survives between renders but doesn't trigger re-renders when changed. Two distinct use cases: DOM access and mutable instance values.

useState  → change = re-render
useRef    → change = NO re-render, React doesn't know

The Rule

If changing the value should update UI → useState. If not → useRef.

Case 1: DOM Access

The most common and cleanest use case — imperative DOM methods:

function SearchModal() {
  const inputRef = useRef(null);
  useEffect(() => { inputRef.current?.focus(); }, []);
  return <input ref={inputRef} placeholder="Search..." />;
}


Also: scrollIntoView, ResizeObserver, measuring element dimensions.

Case 2: Mutable Values Between Renders

Store values that shouldn't cause re-renders:

// Timer ID
const intervalRef = useRef(null);
const start = () => {
  intervalRef.current = setInterval(() => setTime(t => t + 1), 1000);
};
const stop = () => clearInterval(intervalRef.current);

// Previous value
const prevPriceRef = useRef(price);
useEffect(() => { prevPriceRef.current = price; });
const diff = price - prevPriceRef.current;

// First render flag
const isFirstRender = useRef(true);
useEffect(() => {
  if (isFirstRender.current) { isFirstRender.current = false; return; }
  fetchData(filters); // skip on mount, run on filter change
}, [filters]);

Case 3: Stable Callback in useEffect (React 19.2+)

Old workaround with useRef is replaced by useEffectEvent:

// ❌ Old workaround (before React 19.2)
const onSuccessRef = useRef(onSuccess);
useEffect(() => { onSuccessRef.current = onSuccess; });
useEffect(() => {
  fetchData().then(data => onSuccessRef.current(data));
}, []);

// ✅ Modern (React 19.2+)
import { useEffectEvent } from 'react';
const stableOnSuccess = useEffectEvent(onSuccess);
useEffect(() => {
  fetchData().then(data => stableOnSuccess(data));
}, []);


Note: useEffectEvent can only be called inside effects, not in UI event handlers.

Case 4: External Library Integration

Libraries outside React (D3, Chart.js, Google Maps) need direct DOM access:

function D3Chart({ data }) {
  const svgRef = useRef(null);
  useEffect(() => {
    if (!svgRef.current) return;
    const svg = d3.select(svgRef.current);
    svg.selectAll('*').remove();
    // D3 manipulates DOM directly
  }, [data]);
  return <svg ref={svgRef} width={600} height={400} />;
}

Decision Table
Question	Answer
Should change update UI?	useState
Need DOM node reference?	useRef
Storing timer/interval ID?	useRef
Tracking previous value?	useRef
First-render flag?	useRef
Integrating non-React library?	useRef
Value changes but doesn't affect render?	useRef
Anti-pattern
// ❌ useRef as "hidden useState" — UI won't update
const filtersRef = useRef([]);
const applyFilter = (filter) => {
  filtersRef.current.push(filter); // React doesn't know — UI stays stale
};

// ✅ If it affects UI, use useState
const [filters, setFilters] = useState([]);
const applyFilter = (filter) => {
  setFilters(prev => [...prev, filter]);
};

References
useRef — React docs — official API reference covering DOM access and mutable values
useEffectEvent — React docs — official reference for the hook that replaces the useRef callback workaround
Weekly Installs
15
Repository
b4r7x/agent-skills
First Seen
Mar 11, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass