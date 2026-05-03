---
title: churchtools-api
url: https://skills.sh/bwl21/bwl-flyer-generator/churchtools-api
---

# churchtools-api

skills/bwl21/bwl-flyer-generator/churchtools-api
churchtools-api
Installation
$ npx skills add https://github.com/bwl21/bwl-flyer-generator --skill churchtools-api
SKILL.md
ChurchTools API Patterns
Client HTTP Methods

Use the correct method names - delete is NOT available:

churchtoolsClient.get()       // GET requests
churchtoolsClient.post()      // POST requests  
churchtoolsClient.put()       // PUT requests
churchtoolsClient.deleteApi() // DELETE requests - NOT .delete()!
churchtoolsClient.patch()     // PATCH requests

Parameter Structure

Pass parameters directly as the second argument, NOT nested in a "params" object:

// Correct
churchtoolsClient.get('/api/endpoint', { param1: 'value1', param2: 'value2' })

// Wrong - will fail
churchtoolsClient.get('/api/endpoint', { params: { param1: 'value1' } })

Tags API

The Tags API returns data directly as an array, not nested in a "data" property:

// Correct
const response = await churchtoolsClient.get<Tag[]>('/tags/person')
const tags = Array.isArray(response) ? response : []

// Wrong - response.data is undefined
const tags = response.data


Supported tag domains: 'person' | 'song' | 'group' (NOT 'appointment')

Tag updates require ALL fields:

const tagData = {
  name: tag.name,
  description: tag.description || '',  // Required, use empty string
  color: tag.color || 'basic'          // Required, use default color
}
await churchtoolsClient.put(`/tags/${tagId}`, tagData)

API Documentation

Check your ChurchTools instance OpenAPI spec at /system/runtime/swagger/openapi.json for correct endpoints, methods, and schemas.

Standard API Pattern
try {
  loading.value = true
  const response = await churchtoolsClient.get('/api/endpoint', {
    param1: 'value1',
    param2: 'value2'
  })
  // Handle response
} catch (err) {
  error.value = 'Error message'
  console.error('API Error:', err)
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