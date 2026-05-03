---
title: vee-validate-skilld
url: https://skills.sh/harlan-zw/vue-ecosystem-skills/vee-validate-skilld
---

# vee-validate-skilld

skills/harlan-zw/vue-ecosystem-skills/vee-validate-skilld
vee-validate-skilld
Installation
$ npx skills add https://github.com/harlan-zw/vue-ecosystem-skills --skill vee-validate-skilld
SKILL.md
logaretm/vee-validate vee-validate@4.15.1

Tags: prev: 1.0.0-beta.10, next-edge: 4.5.0-alpha.2, edge: 4.5.0-alpha.6

References: Docs

API Changes

This section documents version-specific API changes for vee-validate v4.x — prioritize these over legacy patterns.

BREAKING: v-model support disabled by default in v4.10.0 for performance; enable via configure({ validateOnModelUpdate: true }) or per-field syncVModel source

NEW: defineField introduced in v4.9.0 — replaces defineComponentBinds and defineInputBinds for cleaner Composition API integration source

DEPRECATED: Reactive initial values deprecated in v4.12.0; use non-reactive objects or getters to prevent unintended sync source

NEW: useFormContext exposed in v4.14.0 for accessing form state in deeply nested components without manual injection source

NEW: setValue exposed on Field instances and slot props in v4.13.0 for manual value updates source

NEW: Composition setter hooks (useSetFieldValue, useSetFormValues, useSetFormErrors) added in v4.11.0 for external state management source

NEW: handleBlur accepts shouldValidate parameter since v4.10.0 to control validation triggers on blur events source

NEW: syncVModel accepts target model prop name as a string in v4.10.0 for custom model support source

NEW: isValidating state added to useForm and form slot props in v4.9.3 to track async validation status source

NEW: move(oldIdx, newIdx) added to FieldArray in v4.6.0 for reordering items within array fields source

NEW: Specialized state hooks (useIsFieldDirty, useIsFormValid, useFieldValue) added in v4.1.0 for granular state access source

DEPRECATED: handleInput deprecated in v4.4.0; use handleChange for both input and change events source

NEW: label support in defineField added in v4.12.0 for consistent error message generation source

NEW: ResetFormOpts with force flag added to useResetForm in v4.13.0 to clear values without merging source

Also changed: defineComponentBinds deprecated · defineInputBinds deprecated · useFieldModel deprecated · unsetValueOnUnmount config added · keepValuesOnUnmount reactivity improved · useForm validate returns object · useResetForm hook added · nested field meta querying new v4.12.3

Best Practices
Prefer defineField() for binding components and inputs — returns a v-model ref and a props object for clean, non-deprecated binding source
const [email, emailProps] = defineField('email', {
  validateOnBlur: true,
  props: state => ({ 'aria-invalid': !!state.errors.length })
});


Display errors conditionally using meta.touched — prevents "aggressive" validation where error messages appear before the user interacts with the field source

Use toTypedSchema() for comprehensive TypeScript safety — wraps Yup, Zod, or Valibot schemas to differentiate between input (UI) and output (submitted) types source

import { toTypedSchema } from '@vee-validate/zod';
import * as z from 'zod';

const { values } = useForm({
  validationSchema: toTypedSchema(z.object({ email: z.string().email() }))
});


Mark validation schemas as non-reactive — wrap schemas in markRaw or declare them outside of ref/reactive to avoid unnecessary deep reactivity overhead source

Tree-shake schema validator imports — only import the specific functions you need (e.g., import { string } from 'yup') to keep bundle sizes to a minimum source

Pass reactive field names as getters in useField — use a function (e.g., () => props.name) to ensure vee-validate tracks name changes in dynamic forms source

Enable keepValuesOnUnmount for multi-step forms — preserves field state when components are hidden via v-if or tab switching source

const { values } = useForm({
  keepValuesOnUnmount: true
});


Use field.key for stable iteration in v-for — useFieldArray provides unique identifiers that persist through array operations, unlike indices source

Escape field names with [] to disable automatic nesting — wrap names (e.g., [user.name]) to treat dots as literal characters rather than object paths source

Filter submission values with handleSubmit.withControlled() — ensures only fields explicitly registered via useField or defineField are included in the payload source

Weekly Installs
98
Repository
harlan-zw/vue-e…m-skills
GitHub Stars
158
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass