# 🧪 12 — Testing & QA
> **Use this file when**: Setting up tests, writing test cases, or ensuring code quality.

---

## 🔷 Testing Strategy Pyramid

```
         /\
        /E2E\         <- Few, slow, expensive (Playwright, Cypress)
       /------\
      /Integration\   <- Some, medium speed (Supertest, MSW)
     /------------\
    /  Unit Tests  \  <- Many, fast, cheap (Vitest, Jest)
   /--------------\
```

---

## ⚡ Vitest (Recommended — Fast, Vite-native)

GitHub: https://github.com/vitest-dev/vitest ⭐ 14k+
```bash
npm i -D vitest @vitest/ui @vitest/coverage-v8
```

```typescript
// vitest.config.ts
import { defineConfig } from 'vitest/config'
export default defineConfig({
  test: {
    globals: true,
    environment: 'jsdom',
    setupFiles: ['./src/test/setup.ts'],
    coverage: { provider: 'v8', reporter: ['text', 'html'] }
  }
})
```

```typescript
// sum.test.ts
import { describe, it, expect, vi, beforeEach } from 'vitest'
import { add, fetchUser } from './utils'

describe('math utils', () => {
  it('adds two numbers', () => {
    expect(add(1, 2)).toBe(3)
  })
  
  it('handles edge cases', () => {
    expect(add(-1, 1)).toBe(0)
    expect(add(0, 0)).toBe(0)
  })
})

// Mocking
describe('fetchUser', () => {
  it('returns user data', async () => {
    vi.mocked(fetch).mockResolvedValueOnce({
      json: () => Promise.resolve({ id: 1, name: 'John' })
    } as Response)
    
    const user = await fetchUser(1)
    expect(user.name).toBe('John')
  })
})
```

---

## 🧩 React Testing Library

GitHub: https://github.com/testing-library/react-testing-library ⭐ 19k+
```bash
npm i -D @testing-library/react @testing-library/user-event @testing-library/jest-dom
```

```typescript
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { Button } from './Button'

describe('Button', () => {
  it('renders correctly', () => {
    render(<Button>Click me</Button>)
    expect(screen.getByRole('button', { name: /click me/i })).toBeInTheDocument()
  })
  
  it('calls onClick when clicked', async () => {
    const user = userEvent.setup()
    const handleClick = vi.fn()
    
    render(<Button onClick={handleClick}>Click me</Button>)
    await user.click(screen.getByRole('button'))
    
    expect(handleClick).toHaveBeenCalledTimes(1)
  })
  
  it('is disabled when loading', () => {
    render(<Button isLoading>Submit</Button>)
    expect(screen.getByRole('button')).toBeDisabled()
  })
})
```

---

## 🎭 Playwright (E2E Testing — Recommended)

GitHub: https://github.com/microsoft/playwright ⭐ 68k+
```bash
npm i -D @playwright/test
npx playwright install
```

```typescript
// tests/home.spec.ts
import { test, expect } from '@playwright/test'

test.describe('Home page', () => {
  test('has correct title', async ({ page }) => {
    await page.goto('http://localhost:3000')
    await expect(page).toHaveTitle(/My App/)
  })
  
  test('user can sign up', async ({ page }) => {
    await page.goto('/signup')
    await page.fill('[name=email]', 'test@example.com')
    await page.fill('[name=password]', 'SecurePass123!')
    await page.click('button[type=submit]')
    await expect(page).toHaveURL('/dashboard')
  })
  
  test('mobile view', async ({ page }) => {
    await page.setViewportSize({ width: 375, height: 812 })
    await page.goto('/')
    await expect(page.locator('.mobile-menu')).toBeVisible()
  })
})
```

```bash
npx playwright test
npx playwright test --ui    # Interactive UI mode
npx playwright test --headed # Show browser
npx playwright codegen http://localhost:3000  # Record tests
```

---

## 🌲 Cypress (E2E Alternative)

GitHub: https://github.com/cypress-io/cypress ⭐ 47k+
```bash
npm i -D cypress
npx cypress open
```

```javascript
// cypress/e2e/auth.cy.js
describe('Authentication', () => {
  it('logs in successfully', () => {
    cy.visit('/login')
    cy.get('[data-cy=email]').type('user@example.com')
    cy.get('[data-cy=password]').type('password123')
    cy.get('[data-cy=submit]').click()
    cy.url().should('include', '/dashboard')
    cy.contains('Welcome back').should('be.visible')
  })
})
```

---

## 🔧 Jest (Classic Testing)

GitHub: https://github.com/jestjs/jest ⭐ 44k+
```bash
npm i -D jest @types/jest ts-jest
```

```javascript
// jest.config.js
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  collectCoverageFrom: ['src/**/*.ts'],
}
```

---

## 🌐 API Testing

### Supertest (Express API Testing)
```bash
npm i -D supertest @types/supertest
```
```typescript
import request from 'supertest'
import app from '../app'

describe('GET /api/users', () => {
  it('returns 200 with users array', async () => {
    const res = await request(app).get('/api/users').set('Authorization', 'Bearer token')
    expect(res.status).toBe(200)
    expect(res.body).toBeInstanceOf(Array)
  })
})
```

### MSW (Mock Service Worker) — Mock APIs
```bash
npm i -D msw
```
```typescript
import { http, HttpResponse } from 'msw'
import { setupServer } from 'msw/node'

const server = setupServer(
  http.get('/api/users', () => HttpResponse.json([{ id: 1, name: 'John' }])),
  http.post('/api/users', async ({ request }) => {
    const body = await request.json()
    return HttpResponse.json({ id: 2, ...body }, { status: 201 })
  })
)

beforeAll(() => server.listen())
afterEach(() => server.resetHandlers())
afterAll(() => server.close())
```

---

## 📊 Code Quality Tools

### ESLint
```bash
npm i -D eslint @eslint/js typescript-eslint eslint-plugin-react
```

### Prettier
```bash
npm i -D prettier eslint-config-prettier
echo '{ "semi": false, "singleQuote": true, "tabWidth": 2 }' > .prettierrc
```

### Husky (Git Hooks)
```bash
npm i -D husky lint-staged
npx husky init
echo "npx lint-staged" > .husky/pre-commit
```

```json
// package.json
"lint-staged": {
  "*.{ts,tsx}": ["eslint --fix", "prettier --write"],
  "*.{css,md}": "prettier --write"
}
```

---

## 🏆 Testing Coverage Targets

| Type | Minimum | Recommended |
|------|---------|-------------|
| Business logic | 80% | 95% |
| UI components | 60% | 80% |
| API endpoints | 90% | 100% |
| Utilities | 90% | 100% |

```bash
npx vitest run --coverage   # Check coverage
```
