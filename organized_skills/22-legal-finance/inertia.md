---
rating: ⭐⭐
title: inertia
url: https://skills.sh/markhamsquareventures/essentials/inertia
---

# inertia

skills/markhamsquareventures/essentials/inertia
inertia
Installation
$ npx skills add https://github.com/markhamsquareventures/essentials --skill inertia
SKILL.md
Inertia
Instructions
Inertia + React
Use router.visit() or <Link> for navigation instead of traditional links.

import { Link } from '@inertiajs/react'

Inertia + React Forms

import { Form } from '@inertiajs/react'

export default () => (

    {errors.name && <div>{errors.name}</div>}

    <button type="submit" disabled={processing}>
        {processing ? 'Creating...' : 'Create User'}
    </button>

    {wasSuccessful && <div>User created successfully!</div>}
    </>
)}
</Form>


)

Weekly Installs
21
Repository
markhamsquareve…sentials
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass