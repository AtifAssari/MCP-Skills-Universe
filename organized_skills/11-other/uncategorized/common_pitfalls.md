---
rating: ⭐⭐
title: common-pitfalls
url: https://skills.sh/bwl21/bwl-flyer-generator/common-pitfalls
---

# common-pitfalls

skills/bwl21/bwl-flyer-generator/common-pitfalls
common-pitfalls
Installation
$ npx skills add https://github.com/bwl21/bwl-flyer-generator --skill common-pitfalls
SKILL.md
Common Pitfalls
ChurchTools API
Pitfall	Wrong	Correct
Nested params	{ params: { key: 'val' } }	{ key: 'val' }
Delete method	churchtoolsClient.delete()	churchtoolsClient.deleteApi()
Tags response	response.data	response (direct array)
Tag domains	'appointment'	'person' | 'song' | 'group'
Vue Components
Pitfall	Wrong	Correct
Button type	<button>	<button type="button">
BaseCard import	Absolute path	Relative: ../common/BaseCard.vue
Reactivity	Plain objects	ref() or reactive()
TypeScript
Check src/ct-types.d.ts for ChurchTools types
Always define interfaces for API responses
Use strict typing for all data
Build Issues
Verify import paths after moving components
Check for missing dependencies in package.json
Ensure all required fields in API requests
Safari-specific
Blocks Secure; SameSite=None cookies on http://localhost
Blocks third-party cookies from different domains
Solution: Use Vite proxy + HTTPS
Form Submission

Buttons without type="button" will submit forms and cause page reloads:

<!-- Wrong - triggers form submission -->
<button @click="handleClick">Click</button>

<!-- Correct -->
<button type="button" @click="handleClick">Click</button>

API Error Handling

Always wrap API calls in try-catch with loading states:

try {
  loading.value = true
  // API call
} catch (err) {
  error.value = 'User-friendly message'
  console.error('Debug info:', err)
} finally {
  loading.value = false
}

Weekly Installs
8
Repository
bwl21/bwl-flyer…enerator
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass