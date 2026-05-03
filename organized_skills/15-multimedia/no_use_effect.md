---
rating: ⭐⭐
title: no-use-effect
url: https://skills.sh/alejandrobailo/no-use-effect/no-use-effect
---

# no-use-effect

skills/alejandrobailo/no-use-effect/no-use-effect
no-use-effect
Installation
$ npx skills add https://github.com/alejandrobailo/no-use-effect --skill no-use-effect
SKILL.md
No Direct useEffect

Never call useEffect directly. For the rare case of syncing with an external system on mount, use useMountEffect().

export function useMountEffect(effect: () => void | (() => void)) {
  /* eslint-disable react-hooks/exhaustive-deps, no-restricted-syntax */
  useEffect(effect, []);
}


The only place useEffect may appear directly is inside reusable custom hooks (like useMountEffect itself, or a useData hook when no fetching library is available). Components must never import or call useEffect.

The 6 Rules
Rule 1: Derive state, do not sync it

If you can calculate it from existing state/props, compute it inline.

// BAD: two render cycles
const [filteredProducts, setFilteredProducts] = useState([]);
useEffect(() => {
  setFilteredProducts(products.filter((p) => p.inStock));
}, [products]);

// GOOD: one render
const filteredProducts = products.filter((p) => p.inStock);


For expensive calculations, use useMemo:

const visibleTodos = useMemo(
  () => getFilteredTodos(todos, filter),
  [todos, filter]
);


Smell test: You're about to write useEffect(() => setX(f(y)), [y]) or state that only mirrors other state/props.

Rule 2: Use data-fetching libraries

Effect-based fetching creates race conditions and reinvents caching.

// BAD: race condition
useEffect(() => {
  fetchProduct(productId).then(setProduct);
}, [productId]);

// GOOD: library handles cancellation/caching/staleness
const { data: product } = useQuery(
  ['product', productId],
  () => fetchProduct(productId)
);


In React 19+, use the use() hook with <Suspense> to unwrap promises without useEffect or useState:

// GOOD: use() + Suspense (React 19+)
function UserProfile({ userPromise }: { userPromise: Promise<User> }) {
  const user = use(userPromise);
  return <h1>{user.name}</h1>;
}


Smell test: Your effect does fetch() then setState(), or you're reimplementing caching/retries/cancellation.

Rule 3: Event handlers, not effects

If a user action triggers it, do the work in the handler. Procedural logic (validate → transform → submit) belongs in handlers. Reconstructing procedural flow through ref+effect chains is a sign the logic was event-driven from the start.

// BAD: flag-relay through effect
const [liked, setLiked] = useState(false);
useEffect(() => {
  if (liked) { postLike(); setLiked(false); }
}, [liked]);

// GOOD: direct
<button onClick={() => postLike()}>Like</button>


For shared logic between handlers, extract a function — not an effect:

function buyProduct() {
  addToCart(product);
  showNotification(`Added ${product.name}`);
}


Smell test: State used as a flag so an effect can do the real action, or "set flag -> effect runs -> reset flag" mechanics.

Rule 4: useMountEffect for one-time external sync

Only for true mount-time external system setup: DOM integration, third-party widgets, browser API subscriptions.

// BAD: guard inside effect
useEffect(() => {
  if (!isLoading) playVideo();
}, [isLoading]);

// GOOD: conditional mounting
function VideoPlayerWrapper({ isLoading }) {
  if (isLoading) return <LoadingScreen />;
  return <VideoPlayer />;
}
function VideoPlayer() {
  useMountEffect(() => playVideo());
}


Smell test: Behavior is naturally "setup on mount, cleanup on unmount" with an external system.

Rule 5: Reset with key, not dependency choreography

If you need "start fresh when ID changes," use React's remount semantics.

// BAD: effect resets on ID change
useEffect(() => { loadVideo(videoId); }, [videoId]);

// GOOD: key forces clean remount
<VideoPlayer key={videoId} videoId={videoId} />

function VideoPlayer({ videoId }) {
  useMountEffect(() => { loadVideo(videoId); });
}


This also applies to resetting form state, clearing selections, etc. Use key on the component instead of an effect that sets state to initial values.

Smell test: Effect's only job is to reset local state when an ID/prop changes.

Rule 6: Never patch a broken effect with a ref

If you need a useRef to stop an effect from double-firing, looping, or accessing stale state, the effect itself is the problem. Eliminate the root effect — don't bandage it with a ref.

// BAD: ref guard hides the real problem
const hasRun = useRef(false);
useEffect(() => {
  if (hasRun.current) return;
  hasRun.current = true;
  showWelcomeToast(userId);
}, [userId]);

// GOOD: useMountEffect for true one-time setup
useMountEffect(() => {
  showWelcomeToast(userId);
});

// BAD: ref to capture latest callback, dodging the dependency array
const onMessageRef = useRef(onMessage);
onMessageRef.current = onMessage;
useEffect(() => {
  const conn = createConnection(roomId);
  conn.on('message', (msg) => onMessageRef.current(msg));
  return () => conn.disconnect();
}, [roomId]);

// GOOD: useEffectEvent (experimental) captures latest values automatically
const onMsg = useEffectEvent((msg) => {
  onMessage(msg);
});
useEffect(() => {
  const conn = createConnection(roomId);
  conn.on('message', onMsg);
  return () => conn.disconnect();
}, [roomId]);


The React docs explicitly warn: "The right question isn't 'how to run an Effect once', but 'how to fix my Effect so that it works after remounting'."

Smell test: You're adding hasRun.current, isMounted.current, or a ref whose sole purpose is controlling when/if an effect runs. Or you're storing a callback in a ref to avoid listing it as a dependency.

Additional Patterns
Notifying parents about state changes

Do not use an effect to call onChange — update both in the event handler, or lift state up:

// BAD
useEffect(() => { onChange(isOn); }, [isOn, onChange]);

// GOOD: update both during the event
function updateToggle(nextIsOn) {
  setIsOn(nextIsOn);
  onChange(nextIsOn);
}

useEffectEvent for latest values (experimental)

When an effect needs to read the latest value of a prop/state without re-running when it changes, use useEffectEvent instead of a ref workaround:

// BAD: ref to read latest theme without adding it as dependency
const themeRef = useRef(theme);
themeRef.current = theme;
useEffect(() => {
  logVisit(url, themeRef.current);
}, [url]);

// GOOD: useEffectEvent reads latest values automatically
const onVisit = useEffectEvent(() => {
  logVisit(url, theme);
});
useEffect(() => {
  onVisit();
}, [url]);


Until useEffectEvent is stable, prefer moving logic to event handlers or useMountEffect. If neither fits, isolate the ref workaround in a custom hook — never in a component.

Callback refs for DOM side effects

For DOM measurement or setup, a callback ref is more reliable than useRef + useMountEffect — it fires exactly when the node attaches or detaches:

// BAD: ref.current may be null on first render
const ref = useRef(null);
useMountEffect(() => {
  setHeight(ref.current.getBoundingClientRect().height);
});
return <div ref={ref}>Content</div>;

// GOOD: callback ref fires when node is attached
const measuredRef = useCallback((node: HTMLDivElement | null) => {
  if (node !== null) {
    setHeight(node.getBoundingClientRect().height);
  }
}, []);
return <div ref={measuredRef}>Content</div>;


In React 19+, callback refs support cleanup return values. For earlier versions, store cleanup logic in a ref inside a custom hook.

Subscribing to external stores

Use useSyncExternalStore instead of manual subscription effects:

const isOnline = useSyncExternalStore(
  subscribe,
  () => navigator.onLine,
  () => true
);

App initialization

Run once at module level, not in an effect:

if (typeof window !== 'undefined') {
  checkAuthToken();
  loadDataFromLocalStorage();
}

Chains of computations

Never chain effects that trigger each other. Derive values inline and batch state updates in the event handler:

// BAD: 3 effects chaining state -> 3 extra renders
useEffect(() => { if (card?.gold) setGoldCardCount(c => c + 1); }, [card]);
useEffect(() => { if (goldCardCount > 3) { setRound(r => r + 1); setGoldCardCount(0); } }, [goldCardCount]);
useEffect(() => { if (round > 5) setIsGameOver(true); }, [round]);

// GOOD: derive + handle in event
const isGameOver = round > 5;

function handlePlaceCard(nextCard) {
  setCard(nextCard);
  if (nextCard.gold) {
    if (goldCardCount < 3) setGoldCardCount(goldCardCount + 1);
    else { setGoldCardCount(0); setRound(round + 1); }
  }
}

Decision Checklist

Before writing any effect, answer these questions:

Can I compute it during render? -> Derive it inline or useMemo
Is it triggered by a user action? -> Event handler
Am I fetching data? -> Data-fetching library (React Query, SWR, etc.) or use() + Suspense in React 19+
Am I subscribing to an external store? -> useSyncExternalStore
Do I need to reset state when a prop changes? -> key prop
Is it true mount-time external system sync? -> useMountEffect
Am I using refs to control when/if an effect runs? -> Remove the refs; move logic to an event handler, derive it, or use useEffectEvent
Do I need a DOM side effect when a node mounts? -> Callback ref

If none of the above apply and you still think you need useEffect, see references/patterns.md for detailed examples.

Failure Modes
useMountEffect failures are binary and loud: it ran once, or not at all
Direct useEffect failures degrade gradually as flaky behavior, perf issues, or loops before a hard crash

Choose the bug that's easy to find.

Weekly Installs
222
Repository
alejandrobailo/…e-effect
GitHub Stars
61
First Seen
Mar 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass