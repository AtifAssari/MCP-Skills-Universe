---
title: react-use
url: https://skills.sh/hairyf/skills/react-use
---

# react-use

skills/hairyf/skills/react-use
react-use
Installation
$ npx skills add https://github.com/hairyf/skills --skill react-use
Summary

Essential React Hooks for sensors, UI, animations, side-effects, lifecycles, and state management.

30+ sensor hooks track browser APIs and device interfaces including geolocation, keyboard input, scroll position, network state, and device motion
9 UI hooks manage audio, video, fullscreen, drag-and-drop, speech synthesis, and click-away detection
8 animation hooks provide requestAnimationFrame loops, intervals, timeouts, spring dynamics, and tweening
16 side-effect hooks handle async operations, storage, clipboard, debouncing, throttling, and browser APIs like cookies and favicons
15 lifecycle hooks extend React's built-in hooks with mount/unmount callbacks, deep comparison effects, and mounted state tracking
25+ state hooks simplify management of booleans, arrays, maps, observables, and custom state patterns with history and validation support
SKILL.md
react-use

The skill is based on react-use v17.6.0, generated at 2026-01-29.

react-use is a collection of essential React Hooks that provide ready-to-use functionality for common patterns in React applications. It includes hooks for sensors, UI interactions, animations, side-effects, lifecycle management, and state management.

Core References
Topic	Description	Reference
Usage	Import patterns and tree-shaking recommendations	core-usage
Sensors

Sensor hooks listen to changes in browser APIs and device interfaces, forcing components to re-render with updated state.

Topic	Description	Reference
useBattery	Tracks device battery status	sensors-battery
useGeolocation	Tracks geo location state of user's device	sensors-geolocation
useHover	Tracks mouse hover state of an element	sensors-hover
useHash	Tracks location hash value	sensors-hash
useIdle	Tracks whether user is being inactive	sensors-idle
useIntersection	Tracks an HTML element's intersection	sensors-intersection
useKey	Tracks key presses	sensors-key
useKeyPress	Tracks key press state	sensors-key-press
useKeyPressEvent	Handles key press events	sensors-key-press-event
useKeyboardJs	Tracks keyboard key combinations	sensors-keyboard-js
useLocation	Tracks page navigation bar location state	sensors-location
useSearchParam	Tracks URL search parameters	sensors-search-param
useLongPress	Tracks long press gesture	sensors-long-press
useMedia	Tracks state of a CSS media query	sensors-media
useMediaDevices	Tracks state of connected hardware devices	sensors-media-devices
useMotion	Tracks state of device's motion sensor	sensors-motion
useMouse	Tracks state of mouse position	sensors-mouse
useMouseWheel	Tracks deltaY of scrolled mouse wheel	sensors-mouse-wheel
useNetworkState	Tracks browser's network connection state	sensors-network-state
useOrientation	Tracks device's screen orientation	sensors-orientation
usePageLeave	Triggers when mouse leaves page boundaries	sensors-page-leave
useScratch	Tracks mouse click-and-scrub state	sensors-scratch
useScroll	Tracks an HTML element's scroll position	sensors-scroll
useScrolling	Tracks whether HTML element is scrolling	sensors-scrolling
useStartTyping	Detects when user starts typing	sensors-start-typing
useWindowScroll	Tracks Window scroll position	sensors-window-scroll
useWindowSize	Tracks Window dimensions	sensors-window-size
useMeasure	Tracks an HTML element's dimensions	sensors-measure
useSize	Tracks element size	sensors-size
createBreakpoint	Tracks innerWidth with breakpoints	sensors-breakpoint
useScrollbarWidth	Detects browser's native scrollbars width	sensors-scrollbar-width
usePinchZoom	Tracks pointer events to detect pinch zoom	sensors-pinch-zoom
UI

UI hooks allow you to control and subscribe to state changes of UI elements.

Topic	Description	Reference
useAudio	Plays audio and exposes its controls	ui-audio
useClickAway	Triggers callback when user clicks outside target area	ui-click-away
useCss	Dynamically adjusts CSS	ui-css
useDrop	Tracks file, link and copy-paste drops	ui-drop
useFullscreen	Display an element or video full-screen	ui-fullscreen
useSlider	Provides slide behavior over any HTML element	ui-slider
useSpeech	Synthesizes speech from a text string	ui-speech
useVibrate	Provides physical feedback using Vibration API	ui-vibrate
useVideo	Plays video, tracks its state, and exposes playback controls	ui-video
Animations

Animation hooks usually interpolate numeric values over time.

Topic	Description	Reference
useRaf	Re-renders component on each requestAnimationFrame	animations-raf
useInterval	Re-renders component on a set interval	animations-interval
useHarmonicIntervalFn	Harmonic interval function	animations-harmonic-interval
useSpring	Interpolates number over time according to spring dynamics	animations-spring
useTimeout	Re-renders component after a timeout	animations-timeout
useTimeoutFn	Calls given function after a timeout	animations-timeout-fn
useTween	Re-renders component while tweening a number from 0 to 1	animations-tween
useUpdate	Returns a callback which re-renders component when called	animations-update
Side-effects

Side-effect hooks allow your app to trigger various side-effects using browser's API.

Topic	Description	Reference
useAsync	Resolves an async function	side-effects-async
useAsyncFn	Async function with manual execution	side-effects-async-fn
useAsyncRetry	Async function with retry capability	side-effects-async-retry
useBeforeUnload	Shows browser alert when user tries to reload or close the page	side-effects-before-unload
useCookie	Provides way to read, update and delete a cookie	side-effects-cookie
useCopyToClipboard	Copies text to clipboard	side-effects-copy-to-clipboard
useDebounce	Debounces a function	side-effects-debounce
useError	Error dispatcher	side-effects-error
useFavicon	Sets favicon of the page	side-effects-favicon
useLocalStorage	Manages a value in localStorage	side-effects-local-storage
useSessionStorage	Manages a value in sessionStorage	side-effects-session-storage
useLockBodyScroll	Locks scrolling of the body element	side-effects-lock-body-scroll
useRafLoop	Calls given function inside the RAF loop	side-effects-raf-loop
useThrottle	Throttles a function	side-effects-throttle
useThrottleFn	Throttle function variant	side-effects-throttle-fn
useTitle	Sets title of the page	side-effects-title
usePermission	Query permission status for browser APIs	side-effects-permission
Lifecycles

Lifecycle hooks modify and extend built-in React hooks or imitate React Class component lifecycle patterns.

Topic	Description	Reference
useEffectOnce	Modified useEffect that only runs once	lifecycles-effect-once
useEvent	Subscribe to events	lifecycles-event
useLifecycles	Calls mount and unmount callbacks	lifecycles-lifecycles
useMountedState	Tracks if component is mounted	lifecycles-mounted-state
useUnmountPromise	Track if component is mounted with promise support	lifecycles-unmount-promise
usePromise	Resolves promise only while component is mounted	lifecycles-promise
useLogger	Logs in console as component goes through life-cycles	lifecycles-logger
useMount	Calls mount callbacks	lifecycles-mount
useUnmount	Calls unmount callbacks	lifecycles-unmount
useUpdateEffect	Run an effect only on updates	lifecycles-update-effect
useIsomorphicLayoutEffect	useLayoutEffect that works on server	lifecycles-isomorphic-layout-effect
useDeepCompareEffect	useEffect with deep comparison	lifecycles-deep-compare-effect
useShallowCompareEffect	useEffect with shallow comparison	lifecycles-shallow-compare-effect
useCustomCompareEffect	useEffect with custom comparison function	lifecycles-custom-compare-effect
State

State hooks allow you to easily manage state of booleans, arrays, and maps.

Topic	Description	Reference
createMemo	Factory of memoized hooks	state-create-memo
createReducer	Factory of reducer hooks with custom middleware	state-create-reducer
createReducerContext	Factory of hooks for sharing state between components	state-create-reducer-context
createStateContext	Factory of hooks for sharing state between components	state-create-state-context
createGlobalState	Cross component shared state	state-create-global-state
useDefault	Returns the default value when state is null or undefined	state-default
useGetSet	Returns state getter get() instead of raw state	state-get-set
useGetSetState	Combination of useGetSet and useSetState	state-get-set-state
useLatest	Returns the latest state or props	state-latest
usePrevious	Returns the previous state or props	state-previous
usePreviousDistinct	Like usePrevious but with a predicate	state-previous-distinct
useObservable	Tracks latest value of an Observable	state-observable
useRafState	Creates setState method which only updates after requestAnimationFrame	state-raf-state
useSetState	Creates setState method which works like this.setState	state-set-state
useToggle	Tracks state of a boolean	state-toggle
useCounter	Tracks state of a number	state-counter
useList	Tracks state of an array	state-list
useMap	Tracks state of an object	state-map
useSet	Tracks state of a Set	state-set
useQueue	Implements simple queue	state-queue
useStateList	Circularly iterates over an array	state-state-list
useStateValidator	Validates state with a validator function	state-state-validator
useStateWithHistory	Stores previous state values and provides handles to travel through them	state-state-with-history
useMultiStateValidator	Alike useStateValidator but tracks multiple states	state-multi-state-validator
useMediatedState	Like regular useState but with mediation by custom function	state-mediated-state
useFirstMountState	Check if current render is first	state-first-mount-state
useRendersCount	Count component renders	state-renders-count
useMethods	Neat alternative to useReducer	state-methods
Miscellaneous
Topic	Description	Reference
useEnsuredForwardedRef	Use a React.forwardedRef safely	misc-ensured-forwarded-ref
Weekly Installs
658
Repository
hairyf/skills
GitHub Stars
15
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn