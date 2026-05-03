---
rating: ⭐⭐
title: react-usecontext
url: https://skills.sh/b4r7x/agent-skills/react-usecontext
---

# react-usecontext

skills/b4r7x/agent-skills/react-usecontext
react-usecontext
Installation
$ npx skills add https://github.com/b4r7x/agent-skills --skill react-usecontext
SKILL.md
React useContext
Overview

Context provides "global" data to a component tree without prop drilling. The key insight: context is overused the same way Redux once was — consider simpler alternatives first.

When to Use Context
Truly global, stable data — auth/user, theme, i18n, permissions
Deep prop drilling (3+ levels) — props passing through components that don't use them
Compound components — local, isolated context for tightly coupled UI (best use case)
When NOT to Use
Scenario	Use instead
1-2 levels of props	Normal props — it's not "drilling"
Frequently changing state	Zustand / Jotai
Server data (fetch, cache)	React Query / TanStack Query
Single-branch data	Local useState
Deep but simple structure	Component composition
Component Composition (often overlooked)
// ❌ Prop drilling through 3 levels
<Layout user={user}>
  <Sidebar user={user}>
    <UserAvatar user={user} />
  </Sidebar>
</Layout>

// ✅ Composition — Layout knows nothing about user
<Layout sidebar={<Sidebar><UserAvatar user={user} /></Sidebar>}>

Key Nuance

Only components that directly call useContext re-render when context value changes. Deeply nested components that don't consume the context are unaffected — don't over-optimize with memo() on components that don't use the context.

Context Value Optimization

Two orthogonal problems require separate solutions:

Problem	Solution
Context consumers re-render on every provider render	useMemo on value
Children re-render because parent re-renders	memo() on child component
Full protection pattern
function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const logout = useCallback(() => setUser(null), []);
  // ✅ Stable value — consumers only re-render when user changes
  const value = useMemo(() => ({ user, logout }), [user, logout]);
  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

// ✅ memo prevents re-renders from parent, useMemo prevents re-renders from context
const UserAvatar = memo(function UserAvatar() {
  const { user } = useContext(AuthContext);
  return <img src={user.avatar} />;
});


Without memo on children: useMemo on value protects consumers from unnecessary context changes, but children still re-render when the provider's parent re-renders — these are different mechanisms.

Compound Components (Best Context Use Case)

Local, isolated context for tightly coupled UI — no risk of "too many consumers":

const TabsContext = createContext(null);

function useTabs() {
  const ctx = useContext(TabsContext);
  if (!ctx) throw new Error('Tabs.* must be used inside <Tabs>');
  return ctx;
}

function Tabs({ children, defaultTab }) {
  const [activeTab, setActiveTab] = useState(defaultTab);
  const value = useMemo(() => ({ activeTab, setActiveTab }), [activeTab]);
  return (
    <TabsContext.Provider value={value}>
      <div className="tabs">{children}</div>
    </TabsContext.Provider>
  );
}

Tabs.Tab = function Tab({ id, children }) {
  const { activeTab, setActiveTab } = useTabs();
  return (
    <button className={activeTab === id ? 'active' : ''} onClick={() => setActiveTab(id)}>
      {children}
    </button>
  );
};

Tabs.Panel = function TabPanel({ id, children }) {
  const { activeTab } = useTabs();
  if (activeTab !== id) return null;
  return <div className="tab-panel">{children}</div>;
};


Every major component library (Radix UI, Headless UI, React Aria) uses this pattern.

Anti-pattern: Mega-Context
// ❌ One context for everything — any change re-renders ALL consumers
<AppContext.Provider value={{ user, cart, theme, notifications }}>

// ✅ Separate, isolated contexts
<ThemeProvider>
  <AuthProvider>
    <CartProvider>
      {children}
    </CartProvider>
  </AuthProvider>
</ThemeProvider>

References
useContext — React docs — official API reference with provider patterns
Compound Components with React Hooks — Kent C. Dodds on compound components with context
Compound Pattern — patterns.dev — visual walkthrough of compound components
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