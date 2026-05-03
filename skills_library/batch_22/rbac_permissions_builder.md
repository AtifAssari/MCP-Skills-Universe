---
title: rbac-permissions-builder
url: https://skills.sh/patricio0312rev/skills/rbac-permissions-builder
---

# rbac-permissions-builder

skills/patricio0312rev/skills/rbac-permissions-builder
rbac-permissions-builder
Installation
$ npx skills add https://github.com/patricio0312rev/skills --skill rbac-permissions-builder
SKILL.md
RBAC/Permissions Builder

Implement flexible role-based access control systems.

Permission Matrix
// Define permissions
export enum Permission {
  USER_READ = "user:read",
  USER_WRITE = "user:write",
  USER_DELETE = "user:delete",
  POST_READ = "post:read",
  POST_WRITE = "post:write",
  ADMIN_ACCESS = "admin:access",
}

// Define roles
export const ROLE_PERMISSIONS = {
  user: [Permission.USER_READ, Permission.POST_READ, Permission.POST_WRITE],
  moderator: [...userPermissions, Permission.POST_DELETE],
  admin: Object.values(Permission), // All permissions
};

// Check permission
export const hasPermission = (user: User, permission: Permission): boolean => {
  return ROLE_PERMISSIONS[user.role]?.includes(permission) ?? false;
};

Route Guards (Express)
export const requirePermission = (...permissions: Permission[]) => {
  return (req: Request, res: Response, next: NextFunction) => {
    if (!req.user) {
      return res.status(401).json({ error: "Unauthorized" });
    }

    const hasAllPermissions = permissions.every((p) =>
      hasPermission(req.user, p)
    );

    if (!hasAllPermissions) {
      return res.status(403).json({ error: "Forbidden" });
    }

    next();
  };
};

// Usage
router.delete(
  "/users/:id",
  authenticate,
  requirePermission(Permission.USER_DELETE),
  controller.delete
);

Policy Pattern
// policies/user.policy.ts
export class UserPolicy {
  static canUpdate(currentUser: User, targetUser: User): boolean {
    // Users can update themselves
    if (currentUser.id === targetUser.id) return true;

    // Admins can update anyone
    if (hasPermission(currentUser, Permission.USER_WRITE)) return true;

    return false;
  }

  static canDelete(currentUser: User, targetUser: User): boolean {
    // Can't delete yourself
    if (currentUser.id === targetUser.id) return false;

    // Only admins can delete
    return hasPermission(currentUser, Permission.USER_DELETE);
  }
}

// Usage in controller
if (!UserPolicy.canUpdate(req.user, targetUser)) {
  return res.status(403).json({ error: "Cannot update this user" });
}

Resource Ownership
export const requireOwnership = (
  getResourceUserId: (req: Request) => Promise<string>
) => {
  return async (req: Request, res: Response, next: NextFunction) => {
    const resourceUserId = await getResourceUserId(req);

    // Owner can access
    if (req.user.id === resourceUserId) {
      return next();
    }

    // Admin can access anything
    if (hasPermission(req.user, Permission.ADMIN_ACCESS)) {
      return next();
    }

    return res.status(403).json({ error: "Forbidden" });
  };
};

UI Permission Hints
// Return permissions with user
GET /api/me
{
  "user": { ... },
  "permissions": ["user:read", "post:write"]
}

// Frontend helper
export const usePermission = (permission: Permission): boolean => {
  const { user } = useAuth();
  return user?.permissions?.includes(permission) ?? false;
};

// Usage
{usePermission('user:delete') && <DeleteButton />}

Best Practices
Define permissions granularly (resource:action)
Check at multiple layers (route, controller, UI)
Use policies for complex rules
Cache permission checks
Log permission denials
Test all permission paths
Output Checklist
 Permission enum/constants
 Role-to-permission mapping
 Route guard middleware
 Policy classes for complex rules
 Ownership checking utilities
 Permission checking helpers
 UI permission hints endpoint
 Test cases for all permission paths
Weekly Installs
115
Repository
patricio0312rev/skills
GitHub Stars
35
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass