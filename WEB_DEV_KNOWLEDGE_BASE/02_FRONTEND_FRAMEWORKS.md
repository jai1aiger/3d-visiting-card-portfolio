# 🖥️ 02 — Frontend Frameworks & Libraries
> **Use this file when**: Choosing a frontend framework for a new project, or understanding the ecosystem.

---

## ⚡ Framework Comparison Matrix

| Framework | Language | Learning Curve | Performance | Ecosystem | Best For |
|-----------|----------|---------------|-------------|-----------|---------|
| **React** | JS/TS | Medium | ⭐⭐⭐⭐ | Huge | SPAs, complex apps, large teams |
| **Next.js** | JS/TS | Medium | ⭐⭐⭐⭐⭐ | Very Large | SSR, SSG, full-stack apps |
| **Vue 3** | JS/TS | Low-Medium | ⭐⭐⭐⭐ | Large | Progressive enhancement, startups |
| **Nuxt 3** | JS/TS | Medium | ⭐⭐⭐⭐⭐ | Growing | Vue SSR, full-stack |
| **Angular** | TypeScript | High | ⭐⭐⭐⭐ | Large | Enterprise, large teams |
| **Svelte** | JS/TS | Low | ⭐⭐⭐⭐⭐ | Medium | High performance, simple apps |
| **SvelteKit** | JS/TS | Low-Medium | ⭐⭐⭐⭐⭐ | Growing | Full-stack Svelte |
| **Solid.js** | JS/TS | Medium | ⭐⭐⭐⭐⭐ | Small-Med | Maximum runtime performance |
| **Astro** | JS/TS | Low | ⭐⭐⭐⭐⭐ | Growing | Content sites, static sites, MPA |
| **Qwik** | JS/TS | High | ⭐⭐⭐⭐⭐ | Small | Instant load, resumability |
| **Remix** | JS/TS | Medium | ⭐⭐⭐⭐ | Growing | Web standards, full-stack React |
| **HTMX** | HTML | Very Low | ⭐⭐⭐⭐ | Growing | Hypermedia, minimal JS |

---

## ⚛️ React Ecosystem

### Core
```bash
# Create React App (legacy)
npx create-react-app my-app

# Vite (recommended)
npm create vite@latest my-app -- --template react-ts

# Next.js (recommended for production)
npx create-next-app@latest my-app
```

GitHub: https://github.com/facebook/react ⭐ 230k+

### Essential React Libraries
| Category | Library | Install | Description |
|----------|---------|---------|-------------|
| **Routing** | React Router v7 | `npm i react-router` | Client-side routing |
| **Routing** | TanStack Router | `npm i @tanstack/router` | Type-safe routing |
| **State** | Zustand | `npm i zustand` | Simple global state |
| **State** | Jotai | `npm i jotai` | Atomic state |
| **State** | Redux Toolkit | `npm i @reduxjs/toolkit react-redux` | Redux with DX |
| **Data Fetching** | TanStack Query | `npm i @tanstack/query` | Server state management |
| **Data Fetching** | SWR | `npm i swr` | Stale-while-revalidate |
| **Forms** | React Hook Form | `npm i react-hook-form` | Performant forms |
| **Forms** | Formik | `npm i formik` | Form management |
| **Validation** | Zod | `npm i zod` | TypeScript schema validation |
| **Animation** | Framer Motion | `npm i framer-motion` | Production-ready animations |
| **Styling** | Styled Components | `npm i styled-components` | CSS-in-JS |
| **Styling** | Emotion | `npm i @emotion/react` | CSS-in-JS, faster |
| **Testing** | React Testing Library | `npm i @testing-library/react` | Component testing |
| **Dev Tools** | React DevTools | Browser Extension | Debug React apps |

---

## 💚 Vue 3 Ecosystem

### Core Setup
```bash
npm create vue@latest my-app
# Select: TypeScript, Vue Router, Pinia, Vitest
```

GitHub: https://github.com/vuejs/core ⭐ 48k+

### Essential Vue Libraries
| Category | Library | Install |
|----------|---------|---------|
| **Routing** | Vue Router | Included in setup |
| **State** | Pinia | `npm i pinia` |
| **Composition** | VueUse | `npm i @vueuse/core` |
| **Forms** | VeeValidate | `npm i vee-validate` |
| **Animation** | @vueuse/motion | `npm i @vueuse/motion` |
| **HTTP** | Axios | `npm i axios` |

---

## 🔴 Angular Ecosystem

### Core Setup
```bash
npm install -g @angular/cli
ng new my-app --standalone
```

GitHub: https://github.com/angular/angular ⭐ 96k+

### Essential Angular Libraries
| Category | Library | Command |
|----------|---------|---------|
| **UI Components** | Angular Material | `ng add @angular/material` |
| **State** | NgRx | `ng add @ngrx/store` |
| **HTTP** | Angular HttpClient | Built-in |
| **Forms** | Reactive Forms | Built-in |
| **PWA** | Angular PWA | `ng add @angular/pwa` |
| **SSR** | Angular Universal | `ng add @angular/ssr` |

---

## 🌟 Next.js (Full-Stack React)

### Why Next.js?
- File-based routing (App Router with Server Components)
- SSR, SSG, ISR, CSR — all in one
- API Routes built-in
- Image optimization, font optimization
- Edge Runtime support
- Vercel deployment optimized

```bash
npx create-next-app@latest my-app --typescript --tailwind --app
```

GitHub: https://github.com/vercel/next.js ⭐ 128k+

### Next.js App Router Structure
```
app/
├── layout.tsx          ← Root layout (HTML shell)
├── page.tsx            ← Home page (/)
├── globals.css         ← Global styles
├── about/
│   └── page.tsx        ← /about route
├── blog/
│   ├── page.tsx        ← /blog listing
│   └── [slug]/
│       └── page.tsx    ← /blog/[slug] dynamic route
└── api/
    └── route.ts        ← API endpoint
```

---

## 🚀 Astro (Content-First)

```bash
npm create astro@latest
```

GitHub: https://github.com/withastro/astro ⭐ 48k+

- **Islands Architecture**: Interactive components only where needed
- Zero JS by default
- Can use React, Vue, Svelte components together
- Perfect for blogs, marketing sites, portfolios
- Extremely fast Lighthouse scores

---

## ⚡ Svelte & SvelteKit

```bash
npm create svelte@latest my-app
```

GitHub: https://github.com/sveltejs/svelte ⭐ 80k+

- No Virtual DOM — compiles to vanilla JS
- Incredibly small bundle sizes
- Built-in animations and transitions
- SvelteKit = Next.js equivalent for Svelte

---

## 🧰 Universal/Meta-Framework Tools

| Tool | Purpose | GitHub |
|------|---------|--------|
| **Vite** | Ultra-fast dev server & bundler | https://github.com/vitejs/vite ⭐ 70k+ |
| **Turbopack** | Rust-based bundler (Next.js) | Built into Next.js |
| **Nx** | Monorepo tooling | https://github.com/nrwl/nx ⭐ 24k+ |
| **Turborepo** | Monorepo build system | https://github.com/vercel/turborepo ⭐ 27k+ |
| **Bun** | JS runtime + bundler | https://github.com/oven-sh/bun ⭐ 75k+ |

---

## 🎯 How to Choose a Frontend Framework

```
Is it a content/marketing/blog site?
  → Astro (fastest, best SEO)
  → Next.js (if dynamic content needed)

Is it a complex SPA/web app?
  → Next.js (React, SSR, best ecosystem)
  → Nuxt 3 (Vue, if team prefers Vue)
  → SvelteKit (if bundle size matters)
  → Angular (if enterprise Java-like structure needed)

Is it a simple site with minimal JS?
  → Astro + HTMX
  → Vanilla HTML + Alpine.js

Is maximum runtime performance critical?
  → Solid.js
  → Svelte
```

---

## 📦 Package Managers

| Manager | Install | Best For |
|---------|---------|---------|
| **npm** | Built-in with Node | Standard, universal |
| **pnpm** | `npm i -g pnpm` | Fast, efficient disk usage |
| **yarn** | `npm i -g yarn` | Workspace support |
| **bun** | OS-specific | Fastest, but newer |
