---
rating: ⭐⭐
title: unit-test-vue-pinia
url: https://skills.sh/github/awesome-copilot/unit-test-vue-pinia
---

# unit-test-vue-pinia

skills/github/awesome-copilot/unit-test-vue-pinia
unit-test-vue-pinia
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill unit-test-vue-pinia
SKILL.md
unit-test-vue-pinia

Use this skill to create or review unit tests for Vue components, composables, and Pinia stores. Keep tests small, deterministic, and behavior-first.

Workflow
Identify the behavior boundary first: component UI behavior, composable behavior, or store behavior.
Choose the narrowest test style that can prove that behavior.
Set up Pinia with the least powerful option that still covers the scenario.
Drive the test through public inputs such as props, form updates, button clicks, emitted child events, and store APIs.
Assert observable outputs and side effects before considering any instance-level assertion.
Return or review tests with clear behavior-oriented names and note any remaining coverage gaps.
Core Rules
Test one behavior per test.
Assert observable input/output behavior first (rendered text, emitted events, callback calls, store state changes).
Avoid implementation-coupled assertions.
Access wrapper.vm only in exceptional cases when there is no reasonable DOM, prop, emit, or store-level assertion.
Prefer explicit setup in beforeEach() and reset mocks every test.
Use checked-in reference material in references/pinia-patterns.md as the local source of truth for standard Pinia test setups.
Pinia Testing Approach

Use references/pinia-patterns.md first, then fall back to Pinia's testing cookbook when the checked-in examples do not cover the case.

Default pattern for component tests

Use createTestingPinia as a global plugin while mounting. Prefer createSpy: vi.fn as the default for consistency and easier action-spy assertions.

const wrapper = mount(ComponentUnderTest, {
	global: {
		plugins: [
			createTestingPinia({
				createSpy: vi.fn,
			}),
		],
	},
});


By default, actions are stubbed and spied. Use stubActions: true (default) when the test only needs to verify whether an action was called (or not called).

Accepted minimal Pinia setups

The following are also valid and should not be flagged as incorrect:

createTestingPinia({}) when the test does not assert Pinia action spy behavior.
createTestingPinia({ initialState: ... }) or createTestingPinia({ stubActions: ... }) without createSpy, when the test only needs state seeding or action stubbing behavior and does not inspect generated spies.
setActivePinia(createTestingPinia(...)) in store/composable-focused tests (without mounting a component) when mocking/seeding dependent stores is needed.

Use createSpy: vi.fn when action spy assertions are part of the test intent.

Execute real actions only when needed

Use stubActions: false only when the test must validate the action's real behavior and side effects. Do not switch it on by default for simple "was called" assertions.

const wrapper = mount(ComponentUnderTest, {
	global: {
		plugins: [
			createTestingPinia({
				createSpy: vi.fn,
				stubActions: false,
			}),
		],
	},
});

Seed store state with initialState
const wrapper = mount(ComponentUnderTest, {
	global: {
		plugins: [
			createTestingPinia({
				createSpy: vi.fn,
				initialState: {
					counter: { n: 20 },
					user: { name: "Leia Organa" },
				},
			}),
		],
	},
});

Add Pinia plugins through createTestingPinia
const wrapper = mount(ComponentUnderTest, {
	global: {
		plugins: [
			createTestingPinia({
				createSpy: vi.fn,
				plugins: [myPiniaPlugin],
			}),
		],
	},
});

Getter override pattern for edge cases
const pinia = createTestingPinia({ createSpy: vi.fn });
const store = useCounterStore(pinia);

store.double = 999;
// @ts-expect-error test-only reset of overridden getter
store.double = undefined;

Pure store unit tests

Prefer pure store tests with createPinia() when the goal is to validate store state transitions and action behavior without component rendering. Use createTestingPinia() only when you need stubbed dependent stores, seeded test doubles, or action spies.

beforeEach(() => {
	setActivePinia(createPinia());
});

it("increments", () => {
	const counter = useCounterStore();
	counter.increment();
	expect(counter.n).toBe(1);
});

Vue Test Utils Approach

Follow Vue Test Utils guidance: https://test-utils.vuejs.org/guide/

Mount shallow by default for focused unit tests.
Mount full component trees only when integration behavior is the subject.
Drive behavior through props, user-like interactions, and emitted events.
Prefer findComponent(...).vm.$emit(...) for child stub events instead of touching parent internals.
Use nextTick only when updates are async.
Assert emitted events and payloads with wrapper.emitted(...).
Access wrapper.vm only when no DOM assertion, emitted event assertion, prop assertion, or store-level assertion can express the behavior. Treat it as an exception and keep the assertion narrowly scoped.
Key Testing Snippets

Emit and assert payload:

await wrapper.find("button").trigger("click");
expect(wrapper.emitted("submit")?.[0]?.[0]).toBe("Mango Mission");


Update input and assert output:

await wrapper.find("input").setValue("Agent Violet");
await wrapper.find("form").trigger("submit");
expect(wrapper.emitted("save")?.[0]?.[0]).toBe("Agent Violet");

Test Writing Workflow
Identify the behavior boundary to test.
Build minimal fixture data (only fields needed by that behavior).
Configure Pinia and required test doubles.
Trigger behavior through public inputs.
Assert public outputs and side effects.
Refactor test names to describe behavior, not implementation.
Constraints and Safety
Do not test private/internal implementation details.
Do not overuse snapshots for dynamic UI behavior.
Do not assert every field in large objects if only one behavior matters.
Keep fake data deterministic; avoid random values.
Do not claim a Pinia setup is wrong when it is one of the accepted minimal setups above.
Do not rewrite working tests toward deeper mounting or real actions unless the behavior under test requires that extra surface area.
Flag missing test coverage, brittle selectors, and implementation-coupled assertions explicitly during review.
Output Contract
For create or update, return the finished test code plus a short note describing the selected Pinia strategy.
For review, return concrete findings first, then missing coverage or brittleness risks.
When the safest choice is ambiguous, state the assumption that drove the chosen test setup.
References
references/pinia-patterns.md
Pinia testing cookbook: https://pinia.vuejs.org/cookbook/testing.html
Vue Test Utils guide: https://test-utils.vuejs.org/guide/
Weekly Installs
1.4K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Mar 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass