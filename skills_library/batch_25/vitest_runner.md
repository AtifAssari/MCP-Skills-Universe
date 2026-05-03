---
title: vitest_runner
url: https://skills.sh/vuralserhat86/antigravity-agentic-skills/vitest_runner
---

# vitest_runner

skills/vuralserhat86/antigravity-agentic-skills/vitest_runner
vitest_runner
Installation
$ npx skills add https://github.com/vuralserhat86/antigravity-agentic-skills --skill vitest_runner
SKILL.md
Vitest
Description

Modern JavaScript/TypeScript testing with Vitest including mocking and coverage.

When to Use
Testing JavaScript/TypeScript
React component testing
Unit and integration tests
Core Patterns
Basic Tests
import { describe, it, expect } from 'vitest';

describe('math', () => {
  it('should add numbers', () => {
    expect(1 + 1).toBe(2);
  });

  it('should throw on invalid input', () => {
    expect(() => divide(1, 0)).toThrow('Division by zero');
  });
});

Mocking
import { vi, describe, it, expect } from 'vitest';

// Mock module
vi.mock('./api', () => ({
  fetchUser: vi.fn().mockResolvedValue({ id: 1 })
}));

// Mock function
const callback = vi.fn();
callback('arg');
expect(callback).toHaveBeenCalledWith('arg');

Async Tests
it('should fetch data', async () => {
  const data = await fetchData();
  expect(data).toEqual({ id: 1 });
});

it('should reject on error', async () => {
  await expect(fetchData()).rejects.toThrow('Error');
});

React Testing
import { render, screen } from '@testing-library/react';
import { userEvent } from '@testing-library/user-event';

it('should handle click', async () => {
  const onClick = vi.fn();
  render(<Button onClick={onClick}>Click</Button>);

  await userEvent.click(screen.getByRole('button'));
  expect(onClick).toHaveBeenCalled();
});

🔄 Workflow

Kaynak: Vitest Official Documentation & Vite + Testing Best Practices

Aşama 1: Environment & Setup
 Vite Integration: vitest.config.ts dosyasının Vite ayarlarıyla senkronize olduğunu doğrula.
 Environment Choice: Web projeleri için jsdom veya happy-dom, backend için node environment'ı seç.
 Global Mocks: Sık kullanılan harici servisler (API, LocalStorage) için setup.ts içinde global mock'ları tanımla.
Aşama 2: Unit & Component Testing
 Isolation Layer: Bağımlılıkları vi.mock() ile izole ederek sadece hedef üniteyi test et.
 Assertion Strategy: expect metodlarını kullanarak beklenen sonuçları (be.truthy, toEqual, toBeCalled) doğrula.
 Snapshot Testing: UI bileşenlerindeki (Component) beklenmedik arayüz değişikliklerini toMatchSnapshot() ile yakala.
Aşama 3: Performance & Coverage
 Watch Mode: Geliştirme sürecinde testleri watch modunda tutarak anlık geri bildirim al.
 Coverage Analysis: v8 veya istanbul provider kullanarak test kapsamını raporla.
 Dependency Cleanup: vi.clearAllMocks() ile testler arası veri kirliliğini (Pollution) önle.
Kontrol Noktaları
Aşama	Doğrulama
1	Test dosyaları *.test.ts veya *.spec.ts formatında mı?
2	Asenkron kodlar (async/await) doğru handle ediliyor mu?
3	Karmaşık nesne karşılaştırmalarında toBe (referans) yerine toEqual (değer) mi kullanıldı?

Vitest Runner v1.5 - With Workflow

Weekly Installs
13
Repository
vuralserhat86/a…c-skills
GitHub Stars
42
First Seen
Jan 24, 2026