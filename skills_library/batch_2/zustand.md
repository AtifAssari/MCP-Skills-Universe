---
title: zustand
url: https://skills.sh/lobehub/lobehub/zustand
---

# zustand

skills/lobehub/lobehub/zustand
zustand
Installation
$ npx skills add https://github.com/lobehub/lobehub --skill zustand
Summary

Zustand state management patterns and conventions for LobeHub store development.

Three-tier action hierarchy: public actions for UI, internal actions for business logic, and dispatch methods for state updates; use reducer pattern for complex state and simple set for primitives
Optimistic update pattern for non-destructive operations: update frontend immediately, call backend service, then refresh for consistency
Class-based action implementation using private fields and flattenActions for composition; migrate away from plain StateCreator objects toward encapsulated, type-safe action classes
Naming conventions for actions (verb form for public, internal_ prefix for logic, internal_dispatch* for updates) and state (ID arrays, maps, active flags, init flags)
SKILL.md
LobeHub Zustand State Management
Action Type Hierarchy
1. Public Actions

Main interfaces for UI components:

Naming: Verb form (createTopic, sendMessage)
Responsibilities: Parameter validation, flow orchestration
2. Internal Actions (internal_*)

Core business logic implementation:

Naming: internal_ prefix (internal_createTopic)
Responsibilities: Optimistic updates, service calls, error handling
Should not be called directly by UI
3. Dispatch Methods (internal_dispatch*)

State update handlers:

Naming: internal_dispatch + entity (internal_dispatchTopic)
Responsibilities: Calling reducers, updating store
When to Use Reducer vs Simple set

Use Reducer Pattern:

Managing object lists/maps (messagesMap, topicMaps)
Optimistic updates
Complex state transitions

Use Simple set:

Toggling booleans
Updating simple values
Setting single state fields
Optimistic Update Pattern
internal_createTopic: async (params) => {
  const tmpId = Date.now().toString();

  // 1. Immediately update frontend (optimistic)
  get().internal_dispatchTopic(
    { type: 'addTopic', value: { ...params, id: tmpId } },
    'internal_createTopic'
  );

  // 2. Call backend service
  const topicId = await topicService.createTopic(params);

  // 3. Refresh for consistency
  await get().refreshTopic();
  return topicId;
},


Delete operations: Don't use optimistic updates (destructive, complex recovery)

Naming Conventions

Actions:

Public: createTopic, sendMessage

Internal: internal_createTopic, internal_updateMessageContent

Dispatch: internal_dispatchTopic State:

ID arrays: topicEditingIds

Maps: topicMaps, messagesMap

Active: activeTopicId

Init flags: topicsInit

Detailed Guides
Action patterns: references/action-patterns.md
Slice organization: references/slice-organization.md
Class-Based Action Implementation

We are migrating slices from plain StateCreator objects to class-based actions.

Pattern
Define a class that encapsulates actions and receives (set, get, api) in the constructor.
Use #private fields (e.g., #set, #get) to avoid leaking internals.
Prefer shared typing helpers:
StoreSetter<T> from @/store/types for set.
Pick<ActionImpl, keyof ActionImpl> to expose only public methods.
Export a create*Slice helper that returns a class instance.
type Setter = StoreSetter<HomeStore>;
export const createRecentSlice = (set: Setter, get: () => HomeStore, _api?: unknown) =>
  new RecentActionImpl(set, get, _api);

export class RecentActionImpl {
  readonly #get: () => HomeStore;
  readonly #set: Setter;

  constructor(set: Setter, get: () => HomeStore, _api?: unknown) {
    void _api;
    this.#set = set;
    this.#get = get;
  }

  useFetchRecentTopics = () => {
    // ...
  };
}

export type RecentAction = Pick<RecentActionImpl, keyof RecentActionImpl>;

Composition
In store files, merge class instances with flattenActions (do not spread class instances).
flattenActions binds methods to the original class instance and supports prototype methods and class fields.
const createStore: StateCreator<HomeStore, [['zustand/devtools', never]]> = (...params) => ({
  ...initialState,
  ...flattenActions<HomeStoreAction>([
    createRecentSlice(...params),
    createHomeInputSlice(...params),
  ]),
});

Multi-Class Slices
For large slices that need multiple action classes, compose them in the slice entry using flattenActions.
Use a local PublicActions<T> helper if you need to combine multiple classes and hide private fields.
type PublicActions<T> = { [K in keyof T]: T[K] };

export type ChatGroupAction = PublicActions<
  ChatGroupInternalAction & ChatGroupLifecycleAction & ChatGroupMemberAction & ChatGroupCurdAction
>;

export const chatGroupAction: StateCreator<
  ChatGroupStore,
  [['zustand/devtools', never]],
  [],
  ChatGroupAction
> = (...params) =>
  flattenActions<ChatGroupAction>([
    new ChatGroupInternalAction(...params),
    new ChatGroupLifecycleAction(...params),
    new ChatGroupMemberAction(...params),
    new ChatGroupCurdAction(...params),
  ]);

Store-Access Types
For class methods that depend on actions in other classes, define explicit store augmentations:
ChatGroupStoreWithSwitchTopic for lifecycle switchTopic
ChatGroupStoreWithRefresh for member refresh
ChatGroupStoreWithInternal for curd internal_dispatchChatGroup
Slices That Don't Currently Need set

When a slice doesn't write local state at the moment — e.g. it reads context from #get() and forwards calls to another store, or just runs hooks — drop the #set field. Otherwise ESLint's no-unused-vars flags the unused private field.

Mark the constructor's set param as _set and void _set it to keep the (set, get, api) shape aligned with StateCreator. This is a snapshot of the current need, not a permanent contract — if a later change needs set, restore the #set field and use it; do not invent a workaround to keep the "unused" form.

type Setter = StoreSetter<ConversationStore>;

export const toolSlice = (set: Setter, get: () => ConversationStore, _api?: unknown) =>
  new ToolActionImpl(set, get, _api);

export class ToolActionImpl {
  readonly #get: () => ConversationStore;

  // Mark unused params with `_` prefix and `void _x` so the constructor still
  // matches StateCreator's `(set, get, api)` shape without triggering unused
  // diagnostics.
  constructor(_set: Setter, get: () => ConversationStore, _api?: unknown) {
    void _set;
    void _api;
    this.#get = get;
  }

  approveToolCall = async (id: string) => {
    const { context, hooks } = this.#get();
    await useChatStore.getState().approveToolCalling(id, '', context);
    hooks.onToolCallComplete?.(id, undefined);
  };
}

export type ToolAction = Pick<ToolActionImpl, keyof ToolActionImpl>;


Rules of thumb:

If a slice doesn't currently call set, drop #set (use _set + void _set in the constructor). When a later edit needs set, restore #set and use it.
Don't add setNamespace for slices that don't write state. Add it when the slice starts writing state.
Never leave #set declared but unused "for future use" — lint will fail and re-adding it later costs nothing.
Do / Don't
Do: keep constructor signature aligned with StateCreator params (set, get, api).
Do: use #private to avoid set/get being exposed.
Do: use flattenActions instead of spreading class instances.
Do: drop #set (and use _set + void _set in the constructor) for delegate-only slices that never write state — keeps lint green without breaking the (set, get, api) shape.
Don't: keep both old slice objects and class actions active at the same time.
Don't: keep an unused #set field "for future use" — it fails ESLint and re-adding it later costs nothing.
Weekly Installs
1.4K
Repository
lobehub/lobehub
GitHub Stars
75.9K
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass