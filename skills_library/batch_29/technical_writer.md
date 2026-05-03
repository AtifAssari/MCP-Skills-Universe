---
title: technical writer
url: https://skills.sh/daffy0208/ai-dev-standards/technical-writer
---

# technical writer

skills/daffy0208/ai-dev-standards/Technical Writer
Technical Writer
Installation
$ npx skills add https://github.com/daffy0208/ai-dev-standards --skill 'Technical Writer'
SKILL.md
Technical Writer

Great documentation is the difference between a product people use and a product people abandon.

Core Principle

Write for your audience, not yourself.

Good documentation:

Answers questions before they're asked
Gets users to success quickly
Reduces support burden
Scales knowledge across teams
Documentation Types
1. API Documentation

Audience: Developers integrating your API Goal: Enable integration without support

2. User Guides

Audience: End users Goal: Help users accomplish tasks

3. Tutorials

Audience: Learners Goal: Teach concepts through practice

4. Reference Documentation

Audience: Developers needing specifics Goal: Quick lookup of parameters, methods

5. Architecture Documentation

Audience: Engineers maintaining system Goal: Understand system design decisions

Phase 1: API Documentation
OpenAPI / Swagger Specification
# openapi.yaml
openapi: 3.0.0
info:
  title: User API
  version: 1.0.0
  description: API for managing users

servers:
  - url: https://api.example.com/v1
    description: Production server

paths:
  /users:
    get:
      summary: List all users
      description: Returns a paginated list of users
      parameters:
        - name: page
          in: query
          description: Page number
          schema:
            type: integer
            default: 1
        - name: limit
          in: query
          description: Items per page
          schema:
            type: integer
            default: 20
            maximum: 100
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/User'
                  pagination:
                    $ref: '#/components/schemas/Pagination'
        '401':
          $ref: '#/components/responses/Unauthorized'

    post:
      summary: Create a user
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - email
                - name
              properties:
                email:
                  type: string
                  format: email
                  example: john@example.com
                name:
                  type: string
                  example: John Doe
      responses:
        '201':
          description: User created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '400':
          $ref: '#/components/responses/BadRequest'

components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: string
          format: uuid
        email:
          type: string
          format: email
        name:
          type: string
        createdAt:
          type: string
          format: date-time

    Pagination:
      type: object
      properties:
        page:
          type: integer
        limit:
          type: integer
        total:
          type: integer

  responses:
    Unauthorized:
      description: Authentication required
      content:
        application/json:
          schema:
            type: object
            properties:
              error:
                type: string
                example: Unauthorized

    BadRequest:
      description: Invalid request
      content:
        application/json:
          schema:
            type: object
            properties:
              error:
                type: string
              details:
                type: array
                items:
                  type: string

  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

security:
  - bearerAuth: []

API Documentation Structure
# User API

## Authentication

All API requests require authentication using a Bearer token:


Authorization: Bearer YOUR_API_KEY


Get your API key from the [dashboard](https://dashboard.example.com).

## Base URL



https://api.example.com/v1


## Rate Limiting

- 100 requests per minute per API key
- 1000 requests per hour per API key

Rate limit headers:


X-RateLimit-Limit: 100 X-RateLimit-Remaining: 99 X-RateLimit-Reset: 1640000000


## Errors

Standard HTTP status codes:

| Code | Meaning |
|------|---------|
| 200 | Success |
| 201 | Created |
| 400 | Bad Request - Invalid parameters |
| 401 | Unauthorized - Missing or invalid API key |
| 403 | Forbidden - Insufficient permissions |
| 404 | Not Found |
| 429 | Too Many Requests - Rate limit exceeded |
| 500 | Internal Server Error |

Error response format:
```json
{
  "error": "Invalid email format",
  "code": "VALIDATION_ERROR",
  "details": {
    "field": "email",
    "message": "Must be a valid email address"
  }
}

Endpoints
List Users
GET /users


Returns a paginated list of users.

Query Parameters:

Parameter	Type	Default	Description
page	integer	1	Page number
limit	integer	20	Items per page (max 100)
sort	string	created_at	Sort field
order	string	desc	Sort order (asc/desc)

Example Request:

curl -X GET "https://api.example.com/v1/users?page=1&limit=20" \
  -H "Authorization: Bearer YOUR_API_KEY"


Example Response:

{
  "data": [
    {
      "id": "usr_123",
      "email": "john@example.com",
      "name": "John Doe",
      "createdAt": "2024-01-22T10:30:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 100,
    "pages": 5
  }
}

Create User
POST /users


Creates a new user.

Request Body:

{
  "email": "john@example.com",
  "name": "John Doe",
  "role": "user"
}


Parameters:

Field	Type	Required	Description
email	string	Yes	User email address
name	string	Yes	User full name
role	string	No	User role (default: user)

Example Request:

curl -X POST "https://api.example.com/v1/users" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "name": "John Doe"
  }'


Example Response:

{
  "id": "usr_123",
  "email": "john@example.com",
  "name": "John Doe",
  "role": "user",
  "createdAt": "2024-01-22T10:30:00Z"
}

SDKs
JavaScript / TypeScript
npm install @example/api-client

import { ExampleAPI } from '@example/api-client'

const client = new ExampleAPI('YOUR_API_KEY')

// List users
const users = await client.users.list({ page: 1, limit: 20 })

// Create user
const user = await client.users.create({
  email: 'john@example.com',
  name: 'John Doe'
})

Python
pip install example-api

from example_api import Client

client = Client('YOUR_API_KEY')

# List users
users = client.users.list(page=1, limit=20)

# Create user
user = client.users.create(
    email='john@example.com',
    name='John Doe'
)

Webhooks

Subscribe to events via webhooks:

{
  "url": "https://yourdomain.com/webhook",
  "events": ["user.created", "user.updated", "user.deleted"]
}


Webhook payload:

{
  "event": "user.created",
  "timestamp": "2024-01-22T10:30:00Z",
  "data": {
    "id": "usr_123",
    "email": "john@example.com"
  }
}

Changelog
v1.1.0 (2024-01-22)
Added sort and order parameters to list endpoints
Improved error messages
v1.0.0 (2024-01-01)
Initial release

---

## Phase 2: User Guides

### Structure

```markdown
# Getting Started Guide

## What You'll Learn

In this guide, you'll learn how to:
- Set up your account
- Create your first project
- Invite team members
- Deploy to production

**Time required:** 15 minutes

## Prerequisites

Before you begin, make sure you have:
- [ ] An account (sign up at example.com)
- [ ] Node.js 18+ installed
- [ ] Basic command line knowledge

## Step 1: Create a Project

1. Log in to your [dashboard](https://dashboard.example.com)
2. Click **New Project**
3. Enter your project name
4. Select a region (choose the one closest to your users)
5. Click **Create**

![Create Project Screenshot](./images/create-project.png)

**Tip:** You can create up to 5 projects on the free plan.

## Step 2: Install the CLI

Open your terminal and run:

```bash
npm install -g @example/cli


Verify installation:

example --version


You should see: example CLI v1.0.0

Step 3: Authenticate

Log in to your account:

example login


This will open your browser. Click Authorize to continue.

Step 4: Deploy Your App

Navigate to your app directory:

cd my-app


Deploy:

example deploy


Your app will be live at https://your-app.example.com

Next Steps
Configure custom domains
Set up environment variables
Add team members
Troubleshooting
"Command not found: example"

Solution: Make sure npm's global bin directory is in your PATH.

Run:

npm config get prefix


Add /bin to your PATH.

"Authentication failed"

Solution:

Log out: example logout
Log in again: example login
Make sure you're using the correct account
Need Help?
Documentation
Community Forum
Support

---

## Phase 3: Tutorials

### Tutorial Structure

```markdown
# Build a Todo App with Example Framework

## What You'll Build

In this tutorial, you'll build a fully functional todo app with:
- ✅ Add, edit, and delete todos
- ✅ Mark todos as complete
- ✅ Filter by status
- ✅ Persist data to database

**Final result:** [Live Demo](https://todo-demo.example.com)

## Prerequisites

- Node.js 18+
- Basic JavaScript knowledge
- 30 minutes

## Step 1: Set Up Project

Create a new project:

```bash
npx create-example-app my-todo-app
cd my-todo-app
npm install


Start the dev server:

npm run dev


Open http://localhost:3000. You should see a welcome page.

Step 2: Create Todo Component

Create components/Todo.jsx:

export function Todo({ todo, onToggle, onDelete }) {
  return (
    <div className="todo">
      <input type="checkbox" checked={todo.completed} onChange={() => onToggle(todo.id)} />
      <span className={todo.completed ? 'completed' : ''}>{todo.text}</span>
      <button onClick={() => onDelete(todo.id)}>Delete</button>
    </div>
  )
}


What's happening here:

onToggle marks the todo as complete/incomplete
onDelete removes the todo
CSS class completed styles finished todos
Step 3: Create TodoList Component

Create components/TodoList.jsx:

import { useState } from 'react'
import { Todo } from './Todo'

export function TodoList() {
  const [todos, setTodos] = useState([])
  const [newTodo, setNewTodo] = useState('')

  const addTodo = () => {
    if (!newTodo.trim()) return

    setTodos([
      ...todos,
      {
        id: Date.now(),
        text: newTodo,
        completed: false
      }
    ])

    setNewTodo('')
  }

  const toggleTodo = id => {
    setTodos(todos.map(todo => (todo.id === id ? { ...todo, completed: !todo.completed } : todo)))
  }

  const deleteTodo = id => {
    setTodos(todos.filter(todo => todo.id !== id))
  }

  return (
    <div>
      <h1>My Todos</h1>

      <div className="add-todo">
        <input
          value={newTodo}
          onChange={e => setNewTodo(e.target.value)}
          placeholder="What needs to be done?"
          onKeyPress={e => e.key === 'Enter' && addTodo()}
        />
        <button onClick={addTodo}>Add</button>
      </div>

      <div className="todo-list">
        {todos.map(todo => (
          <Todo key={todo.id} todo={todo} onToggle={toggleTodo} onDelete={deleteTodo} />
        ))}
      </div>
    </div>
  )
}


Key concepts:

useState manages the list of todos
map renders each todo
filter removes deleted todos
Step 4: Add Filtering

Update TodoList.jsx:

const [filter, setFilter] = useState('all') // 'all', 'active', 'completed'

const filteredTodos = todos.filter(todo => {
  if (filter === 'active') return !todo.completed
  if (filter === 'completed') return todo.completed
  return true
})

// In JSX:
<div className="filters">
  <button onClick={() => setFilter('all')}>All</button>
  <button onClick={() => setFilter('active')}>Active</button>
  <button onClick={() => setFilter('completed')}>Completed</button>
</div>

<div className="todo-list">
  {filteredTodos.map(todo => (
    <Todo key={todo.id} todo={todo} onToggle={toggleTodo} onDelete={deleteTodo} />
  ))}
</div>

Step 5: Persist to Database

Install Prisma:

npm install @prisma/client
npm install -D prisma
npx prisma init


Define schema in prisma/schema.prisma:

model Todo {
  id        String   @id @default(uuid())
  text      String
  completed Boolean  @default(false)
  createdAt DateTime @default(now())
}


Run migration:

npx prisma migrate dev --name init


Create API route app/api/todos/route.ts:

import { prisma } from '@/lib/db'

export async function GET() {
  const todos = await prisma.todo.findMany()
  return Response.json(todos)
}

export async function POST(request: Request) {
  const { text } = await request.json()

  const todo = await prisma.todo.create({
    data: { text }
  })

  return Response.json(todo)
}


Update TodoList.jsx to use API:

useEffect(() => {
  fetch('/api/todos')
    .then(res => res.json())
    .then(data => setTodos(data))
}, [])

const addTodo = async () => {
  if (!newTodo.trim()) return

  const response = await fetch('/api/todos', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text: newTodo })
  })

  const todo = await response.json()
  setTodos([...todos, todo])
  setNewTodo('')
}

What You Learned
✅ Component composition
✅ State management with useState
✅ Event handling
✅ Conditional rendering
✅ API integration
✅ Database persistence
Next Steps
Add due dates to todos
Implement drag-and-drop reordering
Add user authentication
Deploy to production
Full Code

View on GitHub


---

## Phase 4: Reference Documentation

### Component Documentation

```markdown
# Button Component

## Import

```typescript
import { Button } from '@/components/Button'

Usage
<Button variant="primary" size="md" onClick={handleClick}>
  Click me
</Button>

Props
Prop	Type	Default	Description
children	ReactNode	required	Button content
variant	'primary' | 'secondary' | 'danger'	'primary'	Visual style
size	'sm' | 'md' | 'lg'	'md'	Button size
onClick	() => void	-	Click handler
disabled	boolean	false	Disabled state
loading	boolean	false	Shows loading spinner
type	'button' | 'submit' | 'reset'	'button'	HTML button type
fullWidth	boolean	false	Full width button
Examples
Primary Button
<Button variant="primary">Save</Button>

Secondary Button
<Button variant="secondary">Cancel</Button>

Danger Button
<Button variant="danger" onClick={handleDelete}>
  Delete
</Button>

Loading State
<Button loading disabled>
  Processing...
</Button>

Full Width
<Button fullWidth>Submit</Button>

Accessibility
Uses semantic <button> element
Supports keyboard navigation (Enter, Space)
Includes proper ARIA attributes when loading
Meets WCAG AA contrast requirements
Related Components
IconButton
LinkButton

---

## Documentation Tools

### Docusaurus (Recommended)

```bash
npx create-docusaurus@latest my-docs classic

cd my-docs
npm start


Structure:

my-docs/
├── docs/              # Documentation markdown files
│   ├── intro.md
│   ├── api/
│   └── guides/
├── blog/              # Blog posts
├── src/
│   └── pages/         # Custom React pages
├── static/            # Images, assets
├── docusaurus.config.js
└── sidebars.js        # Sidebar navigation

Other Tools
GitBook - Beautiful, easy
MkDocs - Python, simple
Mintlify - AI-powered, modern
ReadMe.io - API-focused
Notion - Internal docs
Writing Best Practices
✅ DO

Use Active Voice:

✅ "Click the button to save"
❌ "The button should be clicked to save"


Be Concise:

✅ "Returns user data"
❌ "This endpoint will return the data associated with the user"


Use Examples:

✅ "Set `timeout` to 5000 (5 seconds)"
❌ "Set the timeout parameter"


Break Up Long Content:

✅ Use headings, lists, code blocks
❌ Long paragraphs of text


Include Error Handling:

✅ Show common errors and solutions
❌ Only show happy path

❌ DON'T
Use jargon without explanation
Assume knowledge
Write from your perspective ("we", "our")
Skip error cases
Let docs get stale
Documentation Checklist
Getting Started
 Installation instructions
 Quick start guide
 Hello World example
 Next steps
API Documentation
 Authentication explained
 All endpoints documented
 Request/response examples
 Error codes listed
 Rate limits explained
 SDKs documented
Guides
 Common use cases covered
 Step-by-step tutorials
 Screenshots/videos included
 Troubleshooting section
Reference
 All parameters documented
 Types specified
 Default values listed
 Examples provided
Maintenance
 Versioned
 Changelog maintained
 Broken links checked
 Reviewed quarterly
Related Resources

Skills:

api-designer - API documentation
frontend-builder - Component documentation
ux-designer - User guides

Tools:

Docusaurus
Swagger/OpenAPI
GitBook
Mintlify

Great docs = happy developers = successful product. 📖

Weekly Installs
–
Repository
daffy0208/ai-de…tandards
GitHub Stars
27
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass