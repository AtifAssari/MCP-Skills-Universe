---
title: tanstack-form
url: https://skills.sh/tanstack-skills/tanstack-skills/tanstack-form
---

# tanstack-form

skills/tanstack-skills/tanstack-skills/tanstack-form
tanstack-form
Installation
$ npx skills add https://github.com/tanstack-skills/tanstack-skills --skill tanstack-form
SKILL.md
Overview

TanStack Form is a headless form library with deep TypeScript integration. It provides field-level and form-level validation (sync/async), array fields, linked/dependent fields, fine-grained reactivity, and schema validation adapter support (Zod, Valibot, Yup).

Package: @tanstack/react-form Adapters: @tanstack/zod-form-adapter, @tanstack/valibot-form-adapter Status: Stable (v1)

Installation
npm install @tanstack/react-form
# Optional schema adapters:
npm install @tanstack/zod-form-adapter zod
npm install @tanstack/valibot-form-adapter valibot

Core: useForm
import { useForm } from '@tanstack/react-form'

function MyForm() {
  const form = useForm({
    defaultValues: {
      firstName: '',
      lastName: '',
      email: '',
      age: 0,
    },
    onSubmit: async ({ value }) => {
      // value is fully typed
      await submitToServer(value)
    },
    onSubmitInvalid: ({ value, formApi }) => {
      console.log('Validation failed:', formApi.state.errors)
    },
  })

  return (
    <form
      onSubmit={(e) => {
        e.preventDefault()
        e.stopPropagation()
        form.handleSubmit()
      }}
    >
      {/* Fields */}
      <form.Subscribe
        selector={(state) => ({ canSubmit: state.canSubmit, isSubmitting: state.isSubmitting })}
        children={({ canSubmit, isSubmitting }) => (
          <button type="submit" disabled={!canSubmit}>
            {isSubmitting ? 'Submitting...' : 'Submit'}
          </button>
        )}
      />
    </form>
  )
}

Fields (form.Field)
<form.Field
  name="firstName"
  validators={{
    onChange: ({ value }) =>
      value.length < 3 ? 'Must be at least 3 characters' : undefined,
  }}
  children={(field) => (
    <div>
      <label htmlFor={field.name}>First Name</label>
      <input
        id={field.name}
        name={field.name}
        value={field.state.value}
        onBlur={field.handleBlur}
        onChange={(e) => field.handleChange(e.target.value)}
      />
      {field.state.meta.isTouched && field.state.meta.errors.length > 0 && (
        <em>{field.state.meta.errors.join(', ')}</em>
      )}
    </div>
  )}
/>

<!-- Nested fields use dot notation -->
<form.Field name="address.city">
  {(field) => (
    <input
      value={field.state.value}
      onChange={(e) => field.handleChange(e.target.value)}
      onBlur={field.handleBlur}
    />
  )}
</form.Field>

Validation
Validation Timing
Cause	When
onChange	After every value change
onBlur	When field loses focus
onSubmit	During submission
onMount	When field mounts
Synchronous Validation
<form.Field
  name="age"
  validators={{
    onChange: ({ value }) => {
      if (value < 18) return 'Must be 18 or older'
      return undefined // undefined = valid
    },
    onBlur: ({ value }) => {
      if (!value) return 'Required'
      return undefined
    },
  }}
/>

Asynchronous Validation
<form.Field
  name="username"
  asyncDebounceMs={500}
  validators={{
    onChangeAsync: async ({ value }) => {
      const res = await fetch(`/api/check-username?q=${value}`)
      const { available } = await res.json()
      if (!available) return 'Username taken'
      return undefined
    },
  }}
>
  {(field) => (
    <>
      <input value={field.state.value} onChange={(e) => field.handleChange(e.target.value)} />
      {field.state.meta.isValidating && <span>Checking...</span>}
    </>
  )}
</form.Field>

Schema Validation (Zod)
import { zodValidator } from '@tanstack/zod-form-adapter'
import { z } from 'zod'

const form = useForm({
  defaultValues: { email: '', age: 0 },
  validatorAdapter: zodValidator(),
  onSubmit: async ({ value }) => { /* ... */ },
})

<form.Field
  name="email"
  validators={{
    onChange: z.string().email('Invalid email'),
    onBlur: z.string().min(1, 'Required'),
  }}
/>

<form.Field
  name="age"
  validators={{
    onChange: z.number().min(18, 'Must be 18+'),
  }}
/>

Form-Level Validation
const form = useForm({
  defaultValues: { password: '', confirmPassword: '' },
  validators: {
    onChange: ({ value }) => {
      if (value.password !== value.confirmPassword) {
        return 'Passwords do not match'
      }
      return undefined
    },
  },
})

Linked/Dependent Fields
<form.Field
  name="confirmPassword"
  validators={{
    onChangeListenTo: ['password'], // Re-validate when password changes
    onChange: ({ value, fieldApi }) => {
      const password = fieldApi.form.getFieldValue('password')
      if (value !== password) return 'Passwords do not match'
      return undefined
    },
  }}
/>

Array Fields
<form.Field name="people" mode="array">
  {(field) => (
    <div>
      {field.state.value.map((_, index) => (
        <div key={index}>
          <form.Field name={`people[${index}].name`}>
            {(subField) => (
              <input
                value={subField.state.value}
                onChange={(e) => subField.handleChange(e.target.value)}
              />
            )}
          </form.Field>
          <button type="button" onClick={() => field.removeValue(index)}>
            Remove
          </button>
        </div>
      ))}
      <button type="button" onClick={() => field.pushValue({ name: '', age: 0 })}>
        Add Person
      </button>
    </div>
  )}
</form.Field>

Array Methods
field.pushValue(item)              // Add to end
field.insertValue(index, item)     // Insert at index
field.replaceValue(index, item)    // Replace at index
field.removeValue(index)           // Remove at index
field.swapValues(indexA, indexB)    // Swap positions
field.moveValue(from, to)          // Move position

Listeners (Side Effects)
<form.Field
  name="country"
  listeners={{
    onChange: ({ value }) => {
      // Side effect: reset dependent fields
      form.setFieldValue('state', '')
      form.setFieldValue('postalCode', '')
    },
  }}
/>

Reactivity (form.Subscribe & useStore)
// Render-prop subscription (fine-grained)
<form.Subscribe
  selector={(state) => ({ canSubmit: state.canSubmit, isDirty: state.isDirty })}
  children={({ canSubmit, isDirty }) => (
    <div>
      {isDirty && <span>Unsaved changes</span>}
      <button disabled={!canSubmit}>Save</button>
    </div>
  )}
/>

// Hook-based subscription
function FormStatus() {
  const isValid = form.useStore((s) => s.isValid)
  return isValid ? null : <p>Fix errors</p>
}

Form State
interface FormState {
  values: TFormData
  errors: ValidationError[]
  errorMap: Record<string, ValidationError>
  isFormValid: boolean
  isFieldsValid: boolean
  isValid: boolean               // isFormValid && isFieldsValid
  isTouched: boolean
  isPristine: boolean
  isDirty: boolean
  isSubmitting: boolean
  isSubmitted: boolean
  isSubmitSuccessful: boolean
  submissionAttempts: number
  canSubmit: boolean             // isValid && !isSubmitting
}

Field State
interface FieldState<TData> {
  value: TData
  meta: {
    isTouched: boolean
    isDirty: boolean
    isPristine: boolean
    isValidating: boolean
    errors: ValidationError[]
    errorMap: Record<ValidationCause, ValidationError>
  }
}

FormApi Methods
form.handleSubmit()
form.reset()
form.getFieldValue(field)
form.setFieldValue(field, value)
form.getFieldMeta(field)
form.setFieldMeta(field, updater)
form.validateAllFields(cause)
form.validateField(field, cause)
form.deleteField(field)

Shared Form Options (formOptions)
import { formOptions } from '@tanstack/react-form'

const sharedOpts = formOptions({
  defaultValues: { firstName: '', lastName: '' },
})

// Reuse across components
const form = useForm({
  ...sharedOpts,
  onSubmit: async ({ value }) => { /* ... */ },
})

Server-Side Validation
// TanStack Start / Next.js server action
import { ServerValidateError } from '@tanstack/react-form/nextjs'

export async function validateForm(data: FormData) {
  const email = data.get('email') as string
  if (await checkEmailExists(email)) {
    throw new ServerValidateError({
      form: 'Submission failed',
      fields: { email: 'Email already registered' },
    })
  }
}

TypeScript Integration
// Type-safe field paths with DeepKeys
interface UserForm {
  name: string
  address: { street: string; city: string }
  tags: string[]
  contacts: Array<{ name: string; phone: string }>
}

// TypeScript auto-completes all valid paths:
// 'name', 'address', 'address.street', 'address.city', 'tags', 'contacts'
<form.Field name="address.city" />     // OK
<form.Field name="nonexistent" />       // Type Error!

Best Practices
Always call e.preventDefault() and e.stopPropagation() on form submit
Always attach onBlur={field.handleBlur} for blur validation and isTouched tracking
Use mode="array" for array fields to get array methods
Return undefined (not null/false) for valid validators
Use asyncDebounceMs for async validators to prevent API spam
Check isTouched before showing errors for better UX
Use form.Subscribe with selectors to minimize re-renders
Use formOptions for shared configuration across components
Use schema validators (Zod/Valibot) for complex validation rules
Use onChangeListenTo for cross-field validation dependencies
Common Pitfalls
Forgetting e.preventDefault() on form submit (causes page reload)
Not attaching onBlur to inputs (breaks blur validation and isTouched)
Returning null or false instead of undefined for valid fields
Using mode="array" incorrectly (only needed on the array field itself, not sub-fields)
Subscribing to entire form state instead of using selectors (unnecessary re-renders)
Not using asyncDebounceMs with async validators (fires on every keystroke)
Weekly Installs
1.0K
Repository
tanstack-skills…k-skills
GitHub Stars
14
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass