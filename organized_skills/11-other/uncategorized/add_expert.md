---
rating: ⭐⭐
title: add-expert
url: https://skills.sh/remotion-dev/remotion/add-expert
---

# add-expert

skills/remotion-dev/remotion/add-expert
add-expert
Installation
$ npx skills add https://github.com/remotion-dev/remotion --skill add-expert
SKILL.md
Steps

Add the expert's photo to both:

packages/docs/static/img/freelancers/<firstname>.png
packages/promo-pages/public/img/freelancers/<firstname>.png

The image should be a square headshot (PNG format). Both paths must have the same file.

Add an entry to the experts array in packages/promo-pages/src/components/experts/experts-data.tsx:

{
    slug: 'firstname-lastname',
    name: 'First Last',
    image: '/img/freelancers/<firstname>.png',
    website: 'https://example.com' | null,
    x: 'twitter_handle' | null,
    github: 'github_username' | null,
    linkedin: 'in/linkedin-slug/' | null,
    email: 'email@example.com' | null,
    videocall: 'https://cal.com/...' | null,
    since: new Date('YYYY-MM-DD').getTime(),
    description: (
        <div>
            A short description of the expert's work and specialties.
            Links to projects can be included with <a> tags.
        </div>
    ),
},

since should be set to today's date
slug must be lowercase, hyphenated version of the name
Set unused social fields to null
The entry goes at the end of the experts array (before the closing ])

Render the expert card by running in packages/docs:

bun render-cards


This generates packages/docs/static/generated/experts-<slug>.png. Verify it says "Rendered experts-<slug>" (not "Existed").

Weekly Installs
521
Repository
remotion-dev/remotion
GitHub Stars
45.4K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass