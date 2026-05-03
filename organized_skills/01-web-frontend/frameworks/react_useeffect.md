---
rating: ⭐⭐
title: react-useeffect
url: https://skills.sh/b4r7x/agent-skills/react-useeffect
---

# react-useeffect

skills/b4r7x/agent-skills/react-useeffect
react-useeffect
Installation
$ npx skills add https://github.com/b4r7x/agent-skills --skill react-useeffect
SKILL.md
React useEffect
Overview

useEffect is an escape hatch — it synchronizes a component with an external system. If there's no external system involved, you probably don't need an effect.

"Code that runs because a component was displayed should be in Effects. The rest should be in events." — React docs

Decision Tree
Code you want to run...
  ├─ User clicked / submitted / performed action?
  │         → Event handler
  ├─ Derivable from existing state/props?
  │         → Compute during render (or useMemo)
  ├─ Need to reset state when a prop changes?
  │         → key on the component
  ├─ Need to notify parent about state change?
  │         → Call callback in the same event handler
  └─ Component is visible and must sync with something
     OUTSIDE React (DOM, network, timer, library)?
              → useEffect ✅

Valid Use Cases
1. External system connection
useEffect(() => {
  const conn = createConnection(serverUrl, roomId);
  conn.connect();
  return () => conn.disconnect(); // always cleanup
}, [serverUrl, roomId]);

2. Browser event subscription
useEffect(() => {
  const handler = () => setIsOnline(navigator.onLine);
  window.addEventListener('online', handler);
  window.addEventListener('offline', handler);
  return () => {
    window.removeEventListener('online', handler);
    window.removeEventListener('offline', handler);
  };
}, []);


Consider useSyncExternalStore as a less error-prone alternative.

3. Data fetch (without framework)
// Option A: ignore flag
useEffect(() => {
  let ignore = false;
  fetchUser(userId).then(data => {
    if (!ignore) setUser(data);
  });
  return () => { ignore = true; };
}, [userId]);

// Option B: AbortController (preferred — actually cancels the request)
useEffect(() => {
  const controller = new AbortController();
  fetch(`/api/users/${userId}`, { signal: controller.signal })
    .then(r => r.json())
    .then(setUser)
    .catch(err => {
      if (err.name !== 'AbortError') setError(err);
    });
  return () => controller.abort();
}, [userId]);


If using a framework (Next.js, Remix) — use its data fetching mechanism instead.

4. Non-React library integration (D3, maps, video)
5. Analytics (logging page views)
6. Server/client rendering differences
function ClientOnlyComponent() {
  const [isClient, setIsClient] = useState(false);
  useEffect(() => { setIsClient(true); }, []);
  if (!isClient) return <ServerFallback />;
  return <div>{localStorage.getItem('theme')}</div>;
}

Anti-patterns
1. Derived state (most common mistake)
// ❌ Two unnecessary renders
const [total, setTotal] = useState(0);
useEffect(() => {
  setTotal(items.reduce((sum, i) => sum + i.price, 0));
}, [items]);

// ✅ Compute during render
const total = items.reduce((sum, i) => sum + i.price, 0);

2. Event-specific logic
// ❌ Notification fires on every page refresh
useEffect(() => {
  if (product.isInCart) showNotification(`Added ${product.name}!`);
}, [product]);

// ✅ Logic in event handler — only when user clicks
function handleBuyClick() {
  addToCart(product);
  showNotification(`Added ${product.name}!`);
}

3. Chains of effects
// ❌ 3 effects, each triggering the next = 3 unnecessary renders
useEffect(() => { if (card?.gold) setGoldCount(c => c + 1); }, [card]);
useEffect(() => { if (goldCount > 3) { setRound(r => r + 1); setGoldCount(0); } }, [goldCount]);
useEffect(() => { if (round > 5) setIsGameOver(true); }, [round]);

// ✅ All logic in one event handler — single render
function handlePlaceCard(nextCard) {
  setCard(nextCard);
  if (nextCard.gold) {
    if (goldCount < 3) setGoldCount(goldCount + 1);
    else { setGoldCount(0); setRound(round + 1); }
  }
}
const isGameOver = round > 5; // derived, not state

4. Notifying parent via effect
// ❌ Double render
useEffect(() => { onChange(isOn); }, [isOn, onChange]);

// ✅ Both states in one interaction
function handleClick() {
  const next = !isOn;
  setIsOn(next);
  onChange(next); // immediately, in same event
}

5. Resetting state via effect
// ❌ Renders with stale state first, then resets
useEffect(() => { setComment(''); }, [userId]);

// ✅ key forces React to reset all state
<Profile key={userId} userId={userId} />

6. Adjusting state when props/state change via effect
// ❌ Extra render cycle — renders stale UI, commits to DOM, then re-renders
useEffect(() => {
  if (error) setOtpValue("");
}, [error]);

// ✅ Adjust state during render (documented React pattern)
// React skips the stale commit — clears value before painting
const [prevState, setPrevState] = useState(state);
if (state !== prevState) {
  setPrevState(state);
  if (error) setOtpValue("");
}


This is the "Storing information from previous renders" pattern from the official React useState docs. Key rules:

Use useState (not useRef) to store the previous value — ref mutation during render is a side effect
Guard with an if condition to avoid infinite loops
Prefer deriving values or using key when possible — this is a last resort
See: useState — Storing information from previous renders
7. App initialization
// ❌ Runs twice in Strict Mode
useEffect(() => { checkAuthToken(); }, []);

// ✅ Module-level (runs once on import)
if (typeof window !== 'undefined') { checkAuthToken(); }

Dependency Pitfalls
Object as dependency
// ❌ New object every render = effect runs every render
const options = { serverUrl, roomId };
useEffect(() => { /* ... */ }, [options]);

// ✅ Create object inside effect
useEffect(() => {
  const options = { serverUrl, roomId };
  // ...
}, [roomId]); // only primitive deps

Functional updater to avoid deps
// ❌ count in deps = reset interval on every change
useEffect(() => {
  const id = setInterval(() => setCount(count + 1), 1000);
  return () => clearInterval(id);
}, [count]);

// ✅ Functional update — no count in deps
useEffect(() => {
  const id = setInterval(() => setCount(c => c + 1), 1000);
  return () => clearInterval(id);
}, []);

Cleanup Checklist

Every effect that subscribes, connects, or sets a timer must return a cleanup function:

setInterval → clearInterval
addEventListener → removeEventListener
WebSocket connect → disconnect
fetch → AbortController.abort() or ignore flag
References
Synchronizing with Effects — React docs — official guide on when useEffect is needed
You Might Not Need an Effect — React docs — official decision tree for avoiding unnecessary effects
Weekly Installs
18
Repository
b4r7x/agent-skills
First Seen
Mar 11, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass