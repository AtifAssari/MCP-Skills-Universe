---
title: rbac-policy-tester
url: https://skills.sh/patricio0312rev/skills/rbac-policy-tester
---

# rbac-policy-tester

skills/patricio0312rev/skills/rbac-policy-tester
rbac-policy-tester
Installation
$ npx skills add https://github.com/patricio0312rev/skills --skill rbac-policy-tester
SKILL.md
RBAC/Policy Tester

Comprehensive testing for role-based access control.

Permission Test Matrix
type Role = 'ADMIN' | 'MANAGER' | 'USER' | 'GUEST';
type Action = 'create' | 'read' | 'update' | 'delete';
type Resource = 'users' | 'orders' | 'reports';

const permissionMatrix: Record<Role, Record<Resource, Action[]>> = {
  ADMIN: {
    users: ['create', 'read', 'update', 'delete'],
    orders: ['create', 'read', 'update', 'delete'],
    reports: ['create', 'read', 'update', 'delete'],
  },
  MANAGER: {
    users: ['read', 'update'],
    orders: ['create', 'read', 'update'],
    reports: ['read', 'update'],
  },
  USER: {
    users: ['read'], // Only own profile
    orders: ['create', 'read'], // Only own orders
    reports: ['read'],
  },
  GUEST: {
    users: [],
    orders: [],
    reports: ['read'],
  },
};

describe('RBAC Tests', () => {
  Object.entries(permissionMatrix).forEach(([role, resources]) => {
    describe(\`Role: \${role}\`, () => {
      Object.entries(resources).forEach(([resource, actions]) => {
        actions.forEach(action => {
          it(\`should allow \${action} on \${resource}\`, async () => {
            const token = generateToken({ role });
            await request(app)
              .post(\`/api/\${resource}/\${action}\`)
              .set('Authorization', \`Bearer \${token}\`)
              .expect(200);
          });
        });

        // Test forbidden actions
        const allActions: Action[] = ['create', 'read', 'update', 'delete'];
        const forbidden = allActions.filter(a => !actions.includes(a));

        forbidden.forEach(action => {
          it(\`should deny \${action} on \${resource}\`, async () => {
            const token = generateToken({ role });
            await request(app)
              .post(\`/api/\${resource}/\${action}\`)
              .set('Authorization', \`Bearer \${token}\`)
              .expect(403);
          });
        });
      });
    });
  });
});

Output Checklist
 Permission matrix defined
 Test suite for all roles
 Positive and negative tests
 CI gating enabled
 Coverage monitoring ENDFILE
Weekly Installs
91
Repository
patricio0312rev/skills
GitHub Stars
35
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass