---
title: api-testing
url: https://skills.sh/sgcarstrends/sgcarstrends/api-testing
---

# api-testing

skills/sgcarstrends/sgcarstrends/api-testing
api-testing
Installation
$ npx skills add https://github.com/sgcarstrends/sgcarstrends --skill api-testing
SKILL.md
API Testing Skill
Running Tests
pnpm test                  # Run all tests
pnpm test:watch            # Watch mode
pnpm test:coverage         # With coverage
pnpm -F @sgcarstrends/web test              # Run web tests
pnpm -F @sgcarstrends/web test:watch        # Watch mode for web

Test Structure
apps/web/__tests__/
├── setup.ts              # Test setup
├── helpers.ts            # Test utilities
├── queries/              # Query tests
├── components/           # Component tests
└── utils/                # Utility tests

Testing API Routes
Basic Endpoint Test
import { describe, it, expect } from "vitest";

describe("GET /api/health", () => {
  it("returns 200 OK", async () => {
    const res = await fetch("http://localhost:3000/api/health");
    expect(res.status).toBe(200);
    expect(await res.json()).toEqual({ status: "ok" });
  });
});

Testing with Query Params
describe("GET /api/cars", () => {
  it("filters by month", async () => {
    const res = await fetch("http://localhost:3000/api/cars?month=2024-01");
    expect(res.status).toBe(200);
  });

  it("returns 400 for invalid month", async () => {
    const res = await fetch("http://localhost:3000/api/cars?month=invalid");
    expect(res.status).toBe(400);
  });
});

Testing POST Endpoints
describe("POST /api/posts", () => {
  it("creates a new post", async () => {
    const res = await fetch("http://localhost:3000/api/posts", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title: "Test", content: "Content" }),
    });
    expect(res.status).toBe(201);
  });
});

Mocking
Mock Database
import { vi } from "vitest";
import { db } from "../src/config/database";

vi.spyOn(db.query.cars, "findMany").mockResolvedValue([
  { make: "Toyota", model: "Corolla", number: 100 },
]);

Mock External APIs
const mockFetch = vi.fn().mockResolvedValue({
  ok: true,
  json: async () => ({ records: [] }),
});
global.fetch = mockFetch;

Mock Redis
vi.mock("@sgcarstrends/utils", () => ({
  redis: {
    get: vi.fn(),
    set: vi.fn(),
    del: vi.fn(),
  },
}));

Test Helpers
// apps/web/__tests__/helpers.ts
export const createAuthHeader = (token: string) => ({
  Authorization: `Bearer ${token}`,
});

export const seedDatabase = async (data: any[]) => {
  await db.insert(cars).values(data);
};

export const clearDatabase = async () => {
  await db.delete(cars);
};

Best Practices
Isolate tests - Each test should be independent
Test error cases - Test both happy and error paths
Use mocks - Mock external dependencies
Clean up - Reset state in afterEach
Descriptive names - Clear test descriptions
Coverage goals - Aim for 80%+ coverage
Coverage Configuration
// vitest.config.ts
export default defineConfig({
  test: {
    coverage: {
      provider: "v8",
      thresholds: { lines: 80, functions: 80, branches: 80 },
    },
  },
});

References
Vitest: https://vitest.dev
Next.js Testing: https://nextjs.org/docs/app/building-your-application/testing
Weekly Installs
73
Repository
sgcarstrends/sg…rstrends
GitHub Stars
20
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass