# 🌐 Web Development Knowledge Base & Database

> **Curated from top GitHub repositories, awesome lists, and industry standards (2025–2026)**
> Stored directly in a high-performance **SQLite FTS5 Full-Text Search Database** (`web_dev_knowledge.db`).
> Queryable on demand via CLI or local REST API while designing any website!

---

## 🗄️ Database Quick Start

The knowledge base is indexed in SQLite at `web_dev_knowledge.db` with full-text search capability.

```bash
# 1. List all 28+ topics in the database
python db_manager.py list

# 2. Search anything instantly (FTS5 relevance ranking)
python db_manager.py search "framer motion"
python db_manager.py search "stripe webhook"
python db_manager.py search "auth clerk"

# 3. Search specific headings & code blocks
python db_manager.py section "glassmorphism"

# 4. View a full document
python db_manager.py get 01_UI_UX_DESIGN.md

# 5. Get tool recommendation for your project
python db_manager.py recommend "saas"
python db_manager.py recommend "portfolio"
python db_manager.py recommend "ecommerce"

# 6. Launch local Search Web UI & REST API
python db_manager.py serve 5050
# Open http://localhost:5050 in browser to search while coding!
```

---

## 📁 Complete Knowledge Base Files

| # | File | Category | Key Highlights |
|---|------|----------|----------------|
| **00** | [`00_MASTER_INDEX.md`](00_MASTER_INDEX.md) | Master Index | GitHub stars comparison, decision flowchart |
| **01** | [`01_UI_UX_DESIGN.md`](01_UI_UX_DESIGN.md) | UI/UX & Design Systems | Principles, Figma/Penpot, Bento grid, Glassmorphism |
| **02** | [`02_FRONTEND_FRAMEWORKS.md`](02_FRONTEND_FRAMEWORKS.md) | Frontend Frameworks | React, Next.js 15, Vue 3, Nuxt, SvelteKit, Astro |
| **03** | [`03_BACKEND_FRAMEWORKS.md`](03_BACKEND_FRAMEWORKS.md) | Backend Frameworks | Express, Fastify, NestJS, Hono, FastAPI, Gin, Laravel |
| **04** | [`04_CSS_STYLING.md`](04_CSS_STYLING.md) | CSS & Styling | Tailwind CSS v4, UnoCSS, Bootstrap, CSS Variables |
| **05** | [`05_TYPOGRAPHY_FONTS.md`](05_TYPOGRAPHY_FONTS.md) | Typography & Fonts | Top 10 Font pairings, Variable fonts, Fontsource |
| **06** | [`06_ICONS_ILLUSTRATIONS.md`](06_ICONS_ILLUSTRATIONS.md) | Icons & Illustrations | Lucide, Heroicons, Phosphor, unDraw, Lottie |
| **07** | [`07_ANIMATIONS_MOTION.md`](07_ANIMATIONS_MOTION.md) | Animations & Motion | Framer Motion, GSAP, Lenis, Auto Animate |
| **08** | [`08_3D_GRAPHICS_WEBGL.md`](08_3D_GRAPHICS_WEBGL.md) | 3D Graphics & WebGL | Three.js, React Three Fiber (R3F), Drei, Spline |
| **09** | [`09_DATABASE_ORM.md`](09_DATABASE_ORM.md) | Databases & ORM | PostgreSQL, Prisma, Drizzle, MongoDB, Supabase |
| **10** | [`10_AUTH_SECURITY.md`](10_AUTH_SECURITY.md) | Authentication & Security | Auth.js, Clerk, Passkeys, JWT, Helmet, Rate limiting |
| **11** | [`11_STATE_MANAGEMENT.md`](11_STATE_MANAGEMENT.md) | State Management | Zustand, Jotai, Redux Toolkit, TanStack Query |
| **12** | [`12_TESTING_QA.md`](12_TESTING_QA.md) | Testing & QA | Vitest, Playwright, React Testing Library, Cypress |
| **13** | [`13_BUILD_TOOLS.md`](13_BUILD_TOOLS.md) | Build Tools & Bundlers | Vite, Turbopack, Webpack 5, TypeScript configs |
| **14** | [`14_PERFORMANCE.md`](14_PERFORMANCE.md) | Performance & CWV | Core Web Vitals, Sharp image compression, code split |
| **15** | [`15_ACCESSIBILITY.md`](15_ACCESSIBILITY.md) | Accessibility (A11y) | WCAG 2.2 AA, ARIA patterns, keyboard navigation |
| **16** | [`16_SEO_ANALYTICS.md`](16_SEO_ANALYTICS.md) | SEO & Analytics | Next.js Metadata, sitemaps, JSON-LD, GA4, Plausible |
| **17** | [`17_DEPLOYMENT_DEVOPS.md`](17_DEPLOYMENT_DEVOPS.md) | Deployment & DevOps | Vercel, Docker multi-stage, GitHub Actions CI/CD |
| **18** | [`18_API_REST_GRAPHQL.md`](18_API_REST_GRAPHQL.md) | APIs & WebSockets | REST standards, tRPC, GraphQL (urql), Socket.io |
| **19** | [`19_COMPONENT_LIBRARIES.md`](19_COMPONENT_LIBRARIES.md) | Component Libraries | shadcn/ui, MUI, Mantine, DaisyUI, NextUI |
| **20** | [`20_COLOR_DESIGN_TOKENS.md`](20_COLOR_DESIGN_TOKENS.md) | Color & Design Tokens | OKLCH, Tailwind scale, dark mode tokens |
| **21** | [`21_ENHANCED_UI_COMPONENTS.md`](21_ENHANCED_UI_COMPONENTS.md) | UI Components Deep-Dive | Aceternity UI, Magic UI, Tiptap, TanStack Table |
| **22** | [`22_ANIMATION_SCROLL_LIBS.md`](22_ANIMATION_SCROLL_LIBS.md) | Scroll & Motion Libs | GSAP ScrollTrigger, Lenis smooth scroll, Confetti |
| **23** | [`23_ICON_FONT_TOOLS.md`](23_ICON_FONT_TOOLS.md) | Icons & Fonts Exhaustive | Full directory of icon sets, font tools & patterns |
| **24** | [`24_FORMS_VALIDATION_UPLOADS.md`](24_FORMS_VALIDATION_UPLOADS.md) | Forms & File Uploads | React Hook Form + Zod, S3 Presigned URLs |
| **25** | [`25_ECOMMERCE_PAYMENTS.md`](25_ECOMMERCE_PAYMENTS.md) | E-Commerce & Payments | Stripe checkout, webhooks, Zustand cart state |
| **26** | [`26_I18N_LOCALIZATION_RTL.md`](26_I18N_LOCALIZATION_RTL.md) | i18n & Localization & RTL | `next-intl`, RTL Tailwind logical styling |
| **27** | [`27_AI_INTEGRATION_LLM_UI.md`](27_AI_INTEGRATION_LLM_UI.md) | AI & Generative UI | Vercel AI SDK, streaming chat UI, CopilotKit |

---

## 🎯 Architecture Decision Matrix

```
START NEW WEBSITE
 ├── Marketing / Portfolio / Creative?
 │    └── Next.js / Astro → Tailwind CSS → Framer Motion / GSAP → Spline/R3F → Vercel
 ├── Full-Stack SaaS / Web Application?
 │    └── Next.js 15 → Tailwind + shadcn/ui → Prisma + PostgreSQL → Clerk / Auth.js → Vercel
 ├── High-Traffic E-Commerce?
 │    └── Next.js Storefront → Stripe Checkout → PostgreSQL → Zustand Cart → Cloudflare CDN
 └── Content / Documentation / Blog?
      └── Astro / Next.js Contentlayer → Tailwind Typography → Plausible Analytics
```
