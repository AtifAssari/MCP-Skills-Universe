---
title: mantine-form
url: https://skills.sh/mantinedev/skills/mantine-form
---

# mantine-form

skills/mantinedev/skills/mantine-form
mantine-form
Installation
$ npx skills add https://github.com/mantinedev/skills --skill mantine-form
SKILL.md
Mantine Form Skill
Core Workflow
1. Set up the form
const form = useForm({
  mode: 'controlled',       // or 'uncontrolled' for large forms
  initialValues: {
    email: '',
    age: 0,
  },
  validate: {
    email: isEmail('Invalid email'),
    age: isInRange({ min: 18 }, 'Must be at least 18'),
  },
});

2. Wire inputs with getInputProps
<TextInput {...form.getInputProps('email')} label="Email" />
<NumberInput {...form.getInputProps('age')} label="Age" />


For checkboxes pass { type: 'checkbox' }:

<Checkbox {...form.getInputProps('agreed', { type: 'checkbox' })} label="I agree" />

3. Handle submission
<form onSubmit={form.onSubmit((values) => console.log(values))}>
  ...
  <Button type="submit">Submit</Button>
</form>


onSubmit only calls the handler when validation passes. To handle failures:

form.onSubmit(
  (values) => save(values),
  (errors) => console.log('Validation failed', errors)
)

Validation
Rules object (most common)
validate: {
  name: isNotEmpty('Required'),
  email: isEmail('Invalid email'),
  password: hasLength({ min: 8 }, 'Min 8 chars'),
  confirmPassword: matchesField('password', 'Passwords do not match'),
}

Function (for cross-field logic)
validate: (values) => ({
  endDate: values.endDate < values.startDate ? 'End must be after start' : null,
})

When to validate
validateInputOnChange: true,        // validate all fields on every change
validateInputOnChange: ['email'],    // validate specific fields only
validateInputOnBlur: true,          // validate on blur instead

Modes
Mode	State storage	Re-renders	Input props
'controlled' (default)	React state	On every change	value + onChange
'uncontrolled'	Refs	None	defaultValue + onChange

In uncontrolled mode, use form.key('fieldPath') as the React key prop when you need to force a re-render of an input.

References
references/api.md — Full API: useForm options, complete return value, useField, createFormContext, createFormActions, all built-in validators, key types
references/patterns.md — Code examples: nested objects, array fields, async validation, form context across components, transformValues, useField standalone
Weekly Installs
593
Repository
mantinedev/skills
GitHub Stars
40
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass