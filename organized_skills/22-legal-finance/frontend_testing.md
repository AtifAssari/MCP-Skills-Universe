---
rating: ⭐⭐
title: frontend testing
url: https://skills.sh/exceptionless/exceptionless/frontend-testing
---

# frontend testing

skills/exceptionless/exceptionless/frontend-testing
frontend-testing
Installation
$ npx skills add https://github.com/exceptionless/exceptionless --skill frontend-testing
SKILL.md
Frontend Testing

Documentation: vitest.dev | testing-library.com

Framework & Location
Framework: Vitest + @testing-library/svelte
Location: Co-locate with code as .test.ts or .spec.ts
TDD workflow: When fixing bugs or adding features, write a failing test first
AAA Pattern

Use explicit Arrange, Act, Assert regions:

import { describe, expect, it } from "vitest";

describe("Calculator", () => {
    it("should add two numbers correctly", () => {
        // Arrange
        const a = 5;
        const b = 3;

        // Act
        const result = add(a, b);

        // Assert
        expect(result).toBe(8);
    });
});

Testing with Spies
import { beforeEach, describe, expect, it, vi } from "vitest";
import { CachedPersistedState } from "./cached-persisted-state.svelte";

describe("CachedPersistedState", () => {
    beforeEach(() => {
        vi.clearAllMocks();
    });

    it("should return cached value without reading storage repeatedly", () => {
        // Arrange
        const getItemSpy = vi.spyOn(Storage.prototype, "getItem");
        localStorage.setItem("test-key", "value1");
        const state = new CachedPersistedState("test-key", "default");
        getItemSpy.mockClear();

        // Act
        const val1 = state.current;
        const val2 = state.current;

        // Assert
        expect(val1).toBe("value1");
        expect(val2).toBe("value1");
        expect(getItemSpy).not.toHaveBeenCalled();
    });
});

Query Selection Priority

Use accessible queries (not implementation details):

screen.getByRole("button", { name: /submit/i }) — Role-based (preferred)
screen.getByLabelText("Email address") — Label-based
screen.getByText("Welcome back") — Text-based
screen.getByTestId("complex-chart") — Test ID (fallback)
❌ screen.getByClassName("btn-primary") — Never use implementation details
Mocking Modules
import { vi, describe, it, beforeEach, expect } from "vitest";
import { render, screen } from "@testing-library/svelte";

vi.mock("$lib/api/organizations", () => ({
    getOrganizations: vi.fn(),
}));

import { getOrganizations } from "$lib/api/organizations";
import OrganizationList from "./organization-list.svelte";

describe("OrganizationList", () => {
    beforeEach(() => {
        vi.clearAllMocks();
    });

    it("displays organizations from API", async () => {
        // Arrange
        vi.mocked(getOrganizations).mockResolvedValue([{ id: "1", name: "Org One" }]);

        // Act
        render(OrganizationList);

        // Assert
        expect(await screen.findByText("Org One")).toBeInTheDocument();
    });
});

Weekly Installs
18
Repository
exceptionless/e…tionless
GitHub Stars
2.5K
First Seen
Mar 15, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass