---
title: epic-ui-guidelines
url: https://skills.sh/epicweb-dev/epic-stack/epic-ui-guidelines
---

# epic-ui-guidelines

skills/epicweb-dev/epic-stack/epic-ui-guidelines
epic-ui-guidelines
Installation
$ npx skills add https://github.com/epicweb-dev/epic-stack --skill epic-ui-guidelines
SKILL.md
Epic Stack: UI Guidelines
When to use this skill

Use this skill when you need to:

Create accessible UI components
Follow Epic Stack design patterns
Use Tailwind CSS effectively
Implement semantic HTML
Add ARIA attributes correctly
Create responsive layouts
Ensure proper form accessibility
Follow Epic Stack's UI component conventions
Patterns and conventions
UI Philosophy

Following Epic Web principles:

Software is built for people, by people - Accessibility isn't about checking boxes or meeting standards. It's about creating software that works for real people with diverse needs, abilities, and contexts. Every UI decision should prioritize the human experience over technical convenience.

Accessibility is not optional - it's how we ensure our software serves all users, not just some. When you make UI accessible, you're making it better for everyone: clearer labels help all users, keyboard navigation helps power users, and semantic HTML helps search engines.

Example - Human-centered approach:

// ✅ Good - Built for people
function NoteForm() {
	return (
		<Form method="POST">
			<Field
				labelProps={{
					htmlFor: fields.title.id,
					children: 'Note Title', // Clear, human-readable label
				}}
				inputProps={{
					...getInputProps(fields.title),
					placeholder: 'Enter a descriptive title', // Helpful guidance
					autoFocus: true, // Saves time for users
				}}
				errors={fields.title.errors} // Clear error messages
			/>
		</Form>
	)
}

// ❌ Avoid - Technical convenience over user experience
function NoteForm() {
	return (
		<Form method="POST">
			<input name="title" /> {/* No label, no guidance, no accessibility */}
		</Form>
	)
}

Semantic HTML

✅ Good - Use semantic elements:

function UserCard({ user }: { user: User }) {
	return (
		<article>
			<header>
				<h2>{user.name}</h2>
			</header>
			<p>{user.bio}</p>
			<footer>
				<time dateTime={user.createdAt}>{formatDate(user.createdAt)}</time>
			</footer>
		</article>
	)
}


❌ Avoid - Generic divs:

// ❌ Don't use divs for everything
<div>
	<div>{user.name}</div>
	<div>{user.bio}</div>
	<div>{formatDate(user.createdAt)}</div>
</div>

Form Accessibility

✅ Good - Always use labels:

import { Field } from '#app/components/forms.tsx'

<Field
	labelProps={{
		htmlFor: fields.email.id,
		children: 'Email',
	}}
	inputProps={{
		...getInputProps(fields.email, { type: 'email' }),
		autoFocus: true,
		autoComplete: 'email',
	}}
	errors={fields.email.errors}
/>


The Field component automatically:

Associates labels with inputs using htmlFor and id
Adds aria-invalid when there are errors
Adds aria-describedby pointing to error messages
Ensures proper error announcement

❌ Avoid - Unlabeled inputs:

// ❌ Don't forget labels
<input type="email" name="email" />

ARIA Attributes

✅ Good - Use ARIA appropriately:

// Epic Stack's Field component handles this automatically
<Field
	inputProps={{
		...getInputProps(fields.email, { type: 'email' }),
		// aria-invalid and aria-describedby are added automatically
	}}
	errors={fields.email.errors} // Error messages are linked via aria-describedby
/>


✅ Good - ARIA for custom components:

function LoadingButton({ isLoading, children }: { isLoading: boolean; children: React.ReactNode }) {
	return (
		<button aria-busy={isLoading} disabled={isLoading}>
			{isLoading ? 'Loading...' : children}
		</button>
	)
}

Using Radix UI Components

Epic Stack uses Radix UI for accessible, unstyled components.

✅ Good - Use Radix primitives:

import * as Dialog from '@radix-ui/react-dialog'
import { Button } from '#app/components/ui/button.tsx'

function MyDialog() {
	return (
		<Dialog.Root>
			<Dialog.Trigger asChild>
				<Button>Open Dialog</Button>
			</Dialog.Trigger>
			<Dialog.Portal>
				<Dialog.Overlay className="fixed inset-0 bg-black/50" />
				<Dialog.Content className="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-white p-6">
					<Dialog.Title>Dialog Title</Dialog.Title>
					<Dialog.Description>Dialog description</Dialog.Description>
					<Dialog.Close asChild>
						<Button>Close</Button>
					</Dialog.Close>
				</Dialog.Content>
			</Dialog.Portal>
		</Dialog.Root>
	)
}


Radix components automatically handle:

Keyboard navigation
Focus management
ARIA attributes
Screen reader announcements
Tailwind CSS Patterns

✅ Good - Use Tailwind utility classes:

function Card({ children }: { children: React.ReactNode }) {
	return (
		<div className="rounded-lg border border-gray-200 bg-white p-6 shadow-sm">
			{children}
		</div>
	)
}


✅ Good - Use Tailwind responsive utilities:

<div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
	{items.map(item => (
		<Card key={item.id}>{item.name}</Card>
	))}
</div>


✅ Good - Use Tailwind dark mode:

<div className="bg-white text-gray-900 dark:bg-gray-800 dark:text-gray-100">
	{content}
</div>

Error Handling in Forms

✅ Good - Display errors accessibly:

import { Field, ErrorList } from '#app/components/forms.tsx'

<Field
	labelProps={{ htmlFor: fields.email.id, children: 'Email' }}
	inputProps={getInputProps(fields.email, { type: 'email' })}
	errors={fields.email.errors} // Errors are displayed below input
/>

<ErrorList errors={form.errors} id={form.errorId} /> // Form-level errors


Errors are automatically:

Associated with inputs via aria-describedby
Announced to screen readers
Visually distinct with error styling
Focus Management

✅ Good - Visible focus indicators:

// Tailwind's default focus:ring handles this
<button className="focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">
	Click me
</button>


✅ Good - Focus on form errors:

import { useEffect, useRef } from 'react'

function FormWithErrorFocus() {
	const firstErrorRef = useRef<HTMLInputElement>(null)

	useEffect(() => {
		if (actionData?.errors && firstErrorRef.current) {
			firstErrorRef.current.focus()
		}
	}, [actionData?.errors])

	return <Field inputProps={{ ref: firstErrorRef, ... }} />
}

Keyboard Navigation

✅ Good - Keyboard accessible components:

// Radix components handle keyboard navigation automatically
<Dialog.Trigger asChild>
	<Button>Open</Button>
</Dialog.Trigger>

// Custom components should support keyboard
<button
	onKeyDown={(e) => {
		if (e.key === 'Enter' || e.key === ' ') {
			handleClick()
		}
	}}
>
	Custom Button
</button>

Color Contrast

✅ Good - Use accessible color combinations:

// Use Tailwind's semantic colors that meet WCAG AA
<div className="bg-white text-gray-900"> // High contrast
<div className="text-blue-600 hover:text-blue-700"> // Accessible links


❌ Avoid - Low contrast text:

// ❌ Don't use low contrast
<div className="bg-gray-100 text-gray-200"> // Very low contrast

Responsive Design

✅ Good - Mobile-first approach:

<div className="
	flex flex-col gap-4
	md:flex-row md:gap-8
	lg:gap-12
">
	{/* Content */}
</div>


✅ Good - Responsive typography:

<h1 className="text-2xl md:text-3xl lg:text-4xl">
	Responsive Heading
</h1>

Loading States

✅ Good - Accessible loading indicators:

import { useNavigation } from 'react-router'

function SubmitButton() {
	const navigation = useNavigation()
	const isSubmitting = navigation.state === 'submitting'

	return (
		<button
			type="submit"
			disabled={isSubmitting}
			aria-busy={isSubmitting}
		>
			{isSubmitting ? 'Saving...' : 'Save'}
		</button>
	)
}

Icon Usage

✅ Good - Decorative icons:

import { Icon } from '#app/components/ui/icon.tsx'

<button aria-label="Delete note">
	<Icon name="trash" />
	<span className="sr-only">Delete note</span>
</button>


✅ Good - Semantic icons:

<button>
	<Icon name="check" aria-hidden="true" />
	Save
</button>

Skip Links

✅ Good - Add skip to main content:

// In your root layout
<a href="#main-content" className="sr-only focus:not-sr-only focus:absolute focus:top-0 focus:left-0 focus:z-50 focus:p-4 focus:bg-blue-600 focus:text-white">
	Skip to main content
</a>

<main id="main-content">
	{/* Main content */}
</main>

Progressive Enhancement

✅ Good - Forms work without JavaScript:

// Conform forms work without JavaScript
<Form method="POST" {...getFormProps(form)}>
	<Field {...props} />
	<StatusButton type="submit">Submit</StatusButton>
</Form>


Forms automatically:

Submit via native HTML forms if JavaScript is disabled
Validate server-side
Show errors appropriately
Screen Reader Best Practices

✅ Good - Use semantic HTML first:

// ✅ Semantic HTML provides context automatically
<nav aria-label="Main navigation">
	<ul>
		<li><a href="/">Home</a></li>
		<li><a href="/about">About</a></li>
	</ul>
</nav>


✅ Good - Announce dynamic content:

import { useNavigation } from 'react-router'

function SearchResults({ results }: { results: Result[] }) {
	const navigation = useNavigation()
	const isSearching = navigation.state === 'loading'

	return (
		<div
			role="status"
			aria-live="polite"
			aria-atomic="true"
			className="sr-only"
		>
			{isSearching ? 'Searching...' : `${results.length} results found`}
		</div>
	)
}


✅ Good - Live regions for important updates:

function ToastContainer({ toasts }: { toasts: Toast[] }) {
	return (
		<div aria-live="assertive" aria-atomic="true" className="sr-only">
			{toasts.map(toast => (
				<div key={toast.id} role="alert">
					{toast.message}
				</div>
			))}
		</div>
	)
}


ARIA live region options:

aria-live="polite" - For non-critical updates (search results, status messages)
aria-live="assertive" - For critical updates (errors, confirmations)
aria-atomic="true" - Screen reader reads entire region on update
aria-atomic="false" - Screen reader reads only changed parts
Keyboard Navigation Patterns

✅ Good - Tab order follows visual order:

// Elements appear in logical tab order
<nav>
	<a href="/">Home</a>
	<a href="/about">About</a>
	<a href="/contact">Contact</a>
</nav>


✅ Good - Keyboard shortcuts:

import { useEffect } from 'react'

function SearchDialog({ onClose }: { onClose: () => void }) {
	useEffect(() => {
		function handleKeyDown(e: KeyboardEvent) {
			if (e.key === 'Escape') {
				onClose()
			}
		}

		window.addEventListener('keydown', handleKeyDown)
		return () => window.removeEventListener('keydown', handleKeyDown)
	}, [onClose])

	return <Dialog>{/* content */}</Dialog>
}


✅ Good - Focus trap in modals:

// Radix Dialog automatically handles focus trap
<Dialog.Root>
	<Dialog.Content>
		{/* Focus is trapped inside dialog */}
		<Dialog.Close>Close</Dialog.Close>
	</Dialog.Content>
</Dialog.Root>

Focus Management for React Router

✅ Good - Focus on route changes:

import { useEffect } from 'react'
import { useNavigation } from 'react-router'

function RouteComponent() {
	const navigation = useNavigation()
	const mainRef = useRef<HTMLElement>(null)

	useEffect(() => {
		if (navigation.state === 'idle' && mainRef.current) {
			mainRef.current.focus()
		}
	}, [navigation.state])

	return (
		<main ref={mainRef} tabIndex={-1}>
			{/* Content */}
		</main>
	)
}


✅ Good - Focus on errors:

import { useEffect, useRef } from 'react'

function FormWithErrorFocus({ actionData }: Route.ComponentProps) {
	const firstErrorRef = useRef<HTMLInputElement>(null)

	useEffect(() => {
		if (actionData?.errors && firstErrorRef.current) {
			// Focus first error field
			firstErrorRef.current.focus()
			// Announce error
			firstErrorRef.current.setAttribute('aria-invalid', 'true')
		}
	}, [actionData?.errors])

	return <Field inputProps={{ ref: firstErrorRef, ... }} />
}

Typography and Readability

✅ Good - Readable text sizes:

// Use Tailwind's text size scale
<p className="text-base md:text-lg">Readable body text</p>
<h1 className="text-2xl md:text-3xl lg:text-4xl">Clear headings</h1>


✅ Good - Sufficient line height:

// Tailwind defaults provide good line height
<p className="leading-relaxed">Comfortable reading</p>


❌ Avoid - Small or hard-to-read text:

// ❌ Don't use very small text
<p className="text-xs">Hard to read</p>

Touch Target Sizes

✅ Good - Sufficient touch targets:

// Buttons should be at least 44x44px (touch target size)
<button className="min-h-[44px] min-w-[44px] px-4 py-2">
	Click me
</button>


✅ Good - Spacing between interactive elements:

<div className="flex gap-4">
	<Button>Save</Button>
	<Button>Cancel</Button>
</div>

Internationalization (i18n) Considerations

✅ Good - Use semantic HTML for dates/times:

<time dateTime={note.createdAt.toISOString()}>
	{formatDate(note.createdAt)}
</time>


✅ Good - Use semantic HTML for numbers:

// Screen readers can pronounce numbers correctly
<p>Total: <span aria-label={`${count} items`}>{count}</span></p>


✅ Good - Language attributes:

// In root.tsx
<html lang="en">
	<body>
		{/* Content */}
	</body>
</html>

Dark Mode Accessibility

✅ Good - Maintain contrast in dark mode:

// Ensure sufficient contrast in both modes
<div className="bg-white text-gray-900 dark:bg-gray-900 dark:text-gray-100">
	{content}
</div>


✅ Good - Respect user preference:

// Epic Stack automatically handles theme preference
// Use semantic colors that work in both modes
<button className="bg-blue-600 text-white hover:bg-blue-700 dark:bg-blue-500 dark:hover:bg-blue-600">
	Button
</button>

Animation and Motion

✅ Good - Respect reduced motion:

// Tailwind automatically respects prefers-reduced-motion
<div className="transition-transform duration-200 hover:scale-105 motion-reduce:transition-none">
	{/* Animations disabled for users who prefer reduced motion */}
</div>


✅ Good - Use CSS for animations:

// ✅ CSS animations can be disabled via prefers-reduced-motion
<div className="animate-fade-in">
	{/* Content */}
</div>

// ❌ JavaScript animations may not respect user preferences

Common mistakes to avoid
❌ Treating accessibility as a checklist: Accessibility is about serving real people, not just meeting standards
❌ Missing form labels: Always use Field component which includes labels - helps all users, not just screen reader users
❌ Using divs for semantic elements: Use <article>, <header>, <nav>, etc. - helps all users understand content structure
❌ Ignoring keyboard navigation: Ensure all interactive elements are keyboard accessible - helps power users and those who can't use a mouse
❌ Low color contrast: Test color combinations for WCAG AA compliance - helps users with visual impairments and in bright sunlight
❌ Missing ARIA attributes: Use Epic Stack components which handle this automatically
❌ Breaking focus management: Let Radix components handle focus
❌ Not testing with screen readers: Test with VoiceOver, NVDA, or JAWS - understand how real users experience your UI
❌ Hiding content from screen readers: Use sr-only instead of display: none for screen reader only content
❌ Ignoring mobile users: Always test on mobile devices - many users only have mobile access
❌ Not using Tailwind's responsive utilities: Use mobile-first responsive design
❌ Not using live regions: Use aria-live for dynamic content announcements
❌ Small touch targets: Ensure interactive elements are at least 44x44px - helps users with motor impairments and on mobile
❌ Ignoring reduced motion: Respect prefers-reduced-motion media query - helps users with vestibular disorders
❌ Poor focus indicators: Ensure focus is always visible - helps keyboard users navigate
❌ Missing skip links: Add skip to main content links for keyboard users
References
Web Content Accessibility Guidelines (WCAG)
Epic Web Principles
Radix UI Documentation
Tailwind CSS Documentation
Epic Stack Forms Documentation
app/components/forms.tsx - Accessible form components
app/components/ui/ - Accessible UI components using Radix
app/styles/tailwind.css - Tailwind configuration
Weekly Installs
31
Repository
epicweb-dev/epic-stack
GitHub Stars
5.5K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass