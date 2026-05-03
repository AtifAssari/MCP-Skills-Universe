---
title: rapid-prototyper
url: https://skills.sh/jackspace/claudeskillz/rapid-prototyper
---

# rapid-prototyper

skills/jackspace/claudeskillz/rapid-prototyper
rapid-prototyper
Installation
$ npx skills add https://github.com/jackspace/claudeskillz --skill rapid-prototyper
SKILL.md
Rapid Prototyper
Purpose

Fast validation through working prototypes. Creates complete, runnable code to test ideas before committing to full implementation:

Recalls your preferred tech stack from memory
Generates minimal but complete code
Makes it runnable immediately
Gets you visual feedback fast
Saves validated patterns for production

For ADHD users: Immediate gratification - working prototype in minutes, not hours. For aphantasia: Concrete, visual results instead of abstract descriptions. For all users: Validate before investing - fail fast, learn fast.

Activation Triggers
User says: "prototype this", "quick demo", "proof of concept", "MVP"
User asks: "can we build", "is it possible to", "how would we"
User mentions: "try out", "experiment with", "test the idea"
Before major feature: proactive offer to prototype first
Core Workflow
1. Understand Requirements

Extract key information:

{
  feature: "User authentication",
  purpose: "Validate JWT flow works",
  constraints: ["Must work offline", "No external dependencies"],
  success_criteria: ["Login form", "Token storage", "Protected route"]
}

2. Recall Tech Stack

Query context-manager:

search memories:
- Type: DECISION, PREFERENCE
- Tags: tech-stack, framework, library
- Project: current project


Example recall:

Found preferences:
- Frontend: React + Vite
- Styling: Tailwind CSS
- State: Zustand
- Backend: Node.js + Express
- Database: PostgreSQL (but skip for prototype)

3. Design Minimal Implementation

Prototype scope:

✅ Core feature working
✅ Visual interface (if UI feature)
✅ Basic validation
✅ Happy path functional
❌ Error handling (minimal)
❌ Edge cases (skip for speed)
❌ Styling polish (functional only)
❌ Optimization (prototype first)

Example: Auth prototype scope

✅ Include:
- Login form
- Token storage in localStorage
- Protected route example
- Basic validation

❌ Skip:
- Password hashing (use fake tokens)
- Refresh tokens
- Remember me
- Password reset
- Email verification

4. Generate Prototype

Structure:

prototype-{feature}-{timestamp}/
├── README.md              # How to run
├── package.json           # Dependencies
├── index.html             # Entry point
├── src/
│   ├── App.jsx           # Main component
│   ├── components/       # Feature components
│   └── utils/            # Helper functions
└── server.js             # If backend needed


Example: Auth Prototype

package.json:

{
  "name": "auth-prototype",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.20.0",
    "zustand": "^4.4.7"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.2.1",
    "vite": "^5.0.8"
  }
}


src/App.jsx:

import { useState } from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { useAuthStore } from './store';

function LoginForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const login = useAuthStore(state => state.login);

  const handleSubmit = (e) => {
    e.preventDefault();
    // Prototype: Accept any credentials
    if (email && password) {
      login({ email, token: 'fake-jwt-token' });
    }
  };

  return (
    <div style={{ maxWidth: 400, margin: '100px auto' }}>
      <h1>Login</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Email"
          style={{ display: 'block', width: '100%', margin: '10px 0', padding: 8 }}
        />
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="Password"
          style={{ display: 'block', width: '100%', margin: '10px 0', padding: 8 }}
        />
        <button type="submit" style={{ padding: '10px 20px' }}>
          Login
        </button>
      </form>
    </div>
  );
}

function Dashboard() {
  const { user, logout } = useAuthStore();

  return (
    <div style={{ maxWidth: 800, margin: '50px auto' }}>
      <h1>Dashboard</h1>
      <p>Welcome, {user.email}!</p>
      <p>Token: {user.token}</p>
      <button onClick={logout} style={{ padding: '10px 20px' }}>
        Logout
      </button>
    </div>
  );
}

function ProtectedRoute({ children }) {
  const isAuthenticated = useAuthStore(state => state.isAuthenticated);
  return isAuthenticated ? children : <Navigate to="/login" />;
}

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<LoginForm />} />
        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          }
        />
        <Route path="/" element={<Navigate to="/dashboard" />} />
      </Routes>
    </BrowserRouter>
  );
}


src/store.js:

import { create } from 'zustand';
import { persist } from 'zustand/middleware';

export const useAuthStore = create(
  persist(
    (set) => ({
      user: null,
      isAuthenticated: false,
      login: (user) => set({ user, isAuthenticated: true }),
      logout: () => set({ user: null, isAuthenticated: false }),
    }),
    {
      name: 'auth-storage',
    }
  )
);


README.md:

# Auth Prototype

Quick prototype to validate JWT authentication flow.

## Run

```bash
npm install
npm run dev


Open http://localhost:5173

Test
Go to /login
Enter any email and password
Click Login
Should redirect to /dashboard
Refresh page - should stay logged in
Click Logout - should return to /login
Notes
Uses fake tokens (no real JWT validation)
No password hashing
Minimal styling
No error handling
Next Steps if Validated
Implement real JWT signing/verification
Add password hashing with bcrypt
Add proper error handling
Add refresh token flow
Add validation and security measures

### 5. Save to Artifacts

```bash
# Save complete prototype
# Linux/macOS: ~/.claude-artifacts/prototypes/auth-{timestamp}/
# Windows: %USERPROFILE%\.claude-artifacts\prototypes\auth-{timestamp}\
~/.claude-artifacts/prototypes/auth-{timestamp}/

6. Present to User
✅ Auth prototype ready!

📁 Location (Linux/macOS): ~/.claude-artifacts/prototypes/auth-20251017/
📁 Location (Windows): %USERPROFILE%\.claude-artifacts\prototypes\auth-20251017\

🚀 To run:
cd ~/.claude-artifacts/prototypes/auth-20251017
# Windows: cd %USERPROFILE%\.claude-artifacts\prototypes\auth-20251017
npm install
npm run dev

🎯 Test flow:
1. Visit http://localhost:5173/login
2. Enter any email/password
3. Click Login → Redirects to Dashboard
4. Refresh → Stays logged in
5. Click Logout → Returns to Login

✅ Validates:
- JWT token flow works
- Protected routes work
- State persistence works
- React Router integration works

❌ Not included (yet):
- Real JWT validation
- Password hashing
- Error handling
- Production security

**Does this validate what you needed?**
- If yes: I'll build production version
- If no: What needs adjusting?

Prototype Templates
Single-File HTML App

For quick UI demos:

<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Prototype</title>
  <script src="https://unpkg.com/vue@3"></script>
  <style>
    body { font-family: sans-serif; max-width: 800px; margin: 50px auto; }
  </style>
</head>
<body>
  <div id="app">
    <h1>{{ title }}</h1>
    <button @click="count++">Count: {{ count }}</button>
  </div>

  <script>
    const { createApp } = Vue;
    createApp({
      data() {
        return {
          title: 'Quick Prototype',
          count: 0
        }
      }
    }).mount('#app');
  </script>
</body>
</html>


When to use: UI-only features, visual concepts, no build step needed

React + Vite

For complex UI with state management:

npm create vite@latest prototype-name -- --template react
cd prototype-name
npm install
# Add feature code
npm run dev


When to use: Multi-component features, routing, state management

Node.js Script

For backend/API prototypes:

// prototype.js
import express from 'express';

const app = express();
app.use(express.json());

app.post('/api/users', (req, res) => {
  // Prototype logic
  res.json({ success: true, user: req.body });
});

app.listen(3000, () => {
  console.log('Prototype running on http://localhost:3000');
});


When to use: API endpoints, data processing, backend logic

Python Script

For data analysis/processing:

# prototype.py
def process_data(data):
    # Prototype logic
    return [item * 2 for item in data]

if __name__ == '__main__':
    sample = [1, 2, 3, 4, 5]
    result = process_data(sample)
    print(f"Input: {sample}")
    print(f"Output: {result}")


When to use: Data processing, algorithms, automation

Context Integration
Recall Preferences

Before creating prototype:

// Query context-manager
const techStack = searchMemories({
  type: 'DECISION',
  tags: ['tech-stack', 'framework'],
  project: currentProject
});

const preferences = searchMemories({
  type: 'PREFERENCE',
  tags: ['coding-style', 'libraries'],
  project: currentProject
});

// Apply to prototype
const config = {
  framework: techStack.frontend || 'React',
  styling: techStack.styling || 'inline-styles',
  state: techStack.state || 'useState',
  build: techStack.build || 'Vite'
};

Save Validated Patterns

After user validates prototype:

User: "This works perfectly! Build the production version"

# Save pattern as PROCEDURE
remember: Authentication flow pattern
Type: PROCEDURE
Tags: auth, jwt, react-router, zustand
Content: Validated pattern for JWT auth:
- Zustand store with persist middleware
- React Router protected routes
- Token in localStorage
- Login/logout flow
Works well, use for production

Learn from Iterations

Track what gets changed:

// If user asks for modifications
"Can you add password validation?"
"Make the form prettier"
"Add loading state"

// Track patterns
if (commonRequest) {
  saveMemory({
    type: 'PREFERENCE',
    content: 'User commonly requests password validation in prototypes',
    tags: ['prototyping', 'validation']
  });

  // Auto-include in future prototypes
}

Integration with Other Skills
Context Manager

Recalls tech stack:

Query for DECISION with tags: [tech-stack, framework]
Query for PREFERENCE with tags: [libraries, tools]
Apply to prototype generation


Saves validated patterns:

After user validates prototype
Save pattern as PROCEDURE
Tag with feature name and tech stack

Rapid Production Build

After validation:

User: "Build it properly"
→ Use validated prototype as reference
→ Add error handling
→ Add tests (via testing-builder)
→ Add proper styling
→ Add security measures
→ Create production version

Browser App Creator

For standalone tools:

If prototype should be standalone tool:
→ Invoke browser-app-creator
→ Convert prototype to polished single-file app
→ Save to artifacts/browser-apps/

Success Patterns
Quick Validation (5 minutes)

Scope: Single feature, visual feedback Deliverable: Working demo Example: "Does this button style work?"

<!DOCTYPE html>
<html>
<body>
  <button style="background: #3b82f6; color: white; padding: 12px 24px; border: none; border-radius: 8px; font-size: 16px; cursor: pointer;">
    Click Me
  </button>
</body>
</html>

Feature Prototype (15-30 minutes)

Scope: Complete feature with interactions Deliverable: Multi-file app Example: "User authentication flow"

See full auth prototype above.

Architecture Validation (30-60 minutes)

Scope: System design, integration points Deliverable: Working system with multiple components Example: "Microservices communication pattern"

// api-gateway.js
// orchestrator.js
// user-service.js
// Complete working system

Prototype Checklist

Before generating: ✅ Requirements clear ✅ Tech stack recalled ✅ Scope defined (minimal but complete) ✅ Success criteria established

While generating: ✅ Focus on happy path ✅ Make it runnable immediately ✅ Include clear instructions ✅ Use simple, obvious code

After generating: ✅ Test that it runs ✅ Verify success criteria met ✅ Provide clear next steps ✅ Ask for validation

Quick Reference
When to Prototype
Situation	Prototype?
New feature idea	✅ Yes - validate before building
Bug fix	❌ No - fix directly
Refactoring	✅ Yes - test new pattern
UI tweak	✅ Yes - visual confirmation
Performance optimization	❌ No - measure first
New technology	✅ Yes - learn by doing
Trigger Phrases
"prototype this"
"quick demo"
"proof of concept"
"can we build"
"how would we"
"test the idea"
File Locations
Prototypes: ~/.claude-artifacts/prototypes/ (Linux/macOS) or %USERPROFILE%\.claude-artifacts\prototypes\ (Windows)
Validated patterns: ~/.claude-memories/procedures/ (Linux/macOS) or %USERPROFILE%\.claude-memories\procedures\ (Windows) - tagged "prototype-validated"
Success Criteria

✅ Prototype runs immediately (no setup friction) ✅ Visually demonstrates the concept ✅ Tests core functionality ✅ Takes <30 minutes to create ✅ Clear README with instructions ✅ User can validate yes/no quickly

Weekly Installs
176
Repository
jackspace/claudeskillz
GitHub Stars
14
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass