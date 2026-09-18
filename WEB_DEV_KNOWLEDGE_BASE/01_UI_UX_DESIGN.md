# 🎨 01 — UI/UX Design Tools & Resources
> **Source**: Curated from GitHub awesome lists, top-starred repositories, and professional design communities.
> **Use this file when**: Starting any website design, building design systems, or choosing UI libraries.

---

## 📐 Design Systems & Principles

### What Makes Great UI/UX?
| Principle | Description |
|-----------|-------------|
| **Consistency** | Use the same patterns, colors, and components throughout |
| **Hierarchy** | Guide users with visual weight — size, color, spacing |
| **Feedback** | Every interaction should have a visual/audio response |
| **Accessibility** | Design for all users including those with disabilities |
| **Performance** | Fast UI is good UX — target < 100ms interaction response |
| **Mobile-First** | Design for small screens first, then scale up |
| **Whitespace** | Breathing room improves readability and focus |

---

## 🖌️ Design Tools (Software)

### Prototyping & Wireframing
| Tool | Type | GitHub/URL | Use Case |
|------|------|-----------|---------|
| **Figma** | SaaS | https://figma.com | Industry standard UI design & prototyping |
| **Penpot** | Open Source | https://github.com/penpot/penpot ⭐ 35k+ | Free Figma alternative, self-hostable |
| **Excalidraw** | Open Source | https://github.com/excalidraw/excalidraw ⭐ 90k+ | Hand-drawn style wireframes |
| **Draw.io / Diagrams.net** | Free | https://github.com/jgraph/drawio ⭐ 40k+ | Flowcharts, wireframes |
| **Quant-UX** | Open Source | https://github.com/KlausSchaefers/quant-ux | Prototyping with user testing |
| **Plasmic** | SaaS/OS | https://github.com/plasmicapp/plasmic ⭐ 5k+ | Visual page builder for React |

### Design Handoff
| Tool | Description |
|------|-------------|
| **Zeplin** | Design-to-code specs |
| **Avocode** | Inspect Figma/Sketch files in code |
| **Supernova** | Design tokens to code generation |
| **Story Book** | UI component documentation |

---

## 🧩 Component Library Ecosystems

### React-Based
| Library | GitHub Stars | Install | Best For |
|---------|-------------|---------|---------|
| **shadcn/ui** | ⭐ 80k+ | `npx shadcn@latest init` | Tailwind + Radix, customizable, copy-paste |
| **Material UI (MUI)** | ⭐ 94k+ | `npm i @mui/material` | Google Material Design, enterprise apps |
| **Ant Design** | ⭐ 92k+ | `npm i antd` | Chinese-first enterprise design system |
| **Chakra UI** | ⭐ 38k+ | `npm i @chakra-ui/react` | Accessible, themeable, great DX |
| **Mantine** | ⭐ 28k+ | `npm i @mantine/core` | Full-featured, 100+ components |
| **NextUI** | ⭐ 23k+ | `npm i @nextui-org/react` | Modern, beautiful, Tailwind-based |
| **Radix UI** | ⭐ 16k+ | `npm i @radix-ui/react-*` | Headless, accessible primitives |
| **Headless UI** | ⭐ 26k+ | `npm i @headlessui/react` | Tailwind-compatible headless components |
| **DaisyUI** | ⭐ 35k+ | `npm i daisyui` | Tailwind CSS plugin, 56+ components |
| **Tremor** | ⭐ 18k+ | `npm i @tremor/react` | React dashboard components |
| **Park UI** | Growing | `npx @park-ui/cli init` | Panda CSS + Ark UI components |

### Vue-Based
| Library | GitHub Stars | Install |
|---------|-------------|---------|
| **Vuetify** | ⭐ 40k+ | `npm i vuetify` |
| **PrimeVue** | ⭐ 11k+ | `npm i primevue` |
| **Naive UI** | ⭐ 16k+ | `npm i naive-ui` |
| **Element Plus** | ⭐ 25k+ | `npm i element-plus` |
| **Quasar** | ⭐ 26k+ | `npm i -g @quasar/cli` |

### Angular-Based
| Library | GitHub Stars | Install |
|---------|-------------|---------|
| **Angular Material** | ⭐ 24k+ | `ng add @angular/material` |
| **NG-ZORRO** | ⭐ 9k+ | `ng add ng-zorro-antd` |
| **PrimeNG** | ⭐ 10k+ | `npm i primeng` |

---

## 🎭 Design System Tools

### Storybook (Component Documentation)
```bash
npx storybook@latest init
```
- GitHub: https://github.com/storybookjs/storybook ⭐ 85k+
- Supports React, Vue, Angular, Svelte, Ember
- Visual testing, accessibility addon, interaction tests

### Design Tokens
| Tool | GitHub | Purpose |
|------|--------|---------|
| **Style Dictionary** | https://github.com/amzn/style-dictionary ⭐ 4k+ | Transform design tokens for all platforms |
| **Theo** | https://github.com/salesforce-ux/theo | Salesforce design token transformer |
| **Token Transformer** | npm package | Convert Figma Tokens to Style Dictionary |
| **Panda CSS** | https://github.com/chakra-ui/panda ⭐ 6k+ | CSS-in-JS with design tokens |

---

## 📱 Responsive Design Patterns

### Grid Systems
```css
/* Modern CSS Grid — No framework needed */
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}
```

### Breakpoints (Tailwind Standard)
| Name | Min Width | Use Case |
|------|----------|---------|
| `sm` | 640px | Small tablets |
| `md` | 768px | Tablets |
| `lg` | 1024px | Small laptops |
| `xl` | 1280px | Desktops |
| `2xl` | 1536px | Large screens |

---

## 🔮 Trending UI Patterns (2025)

| Pattern | Description | Example Libraries |
|---------|-------------|------------------|
| **Glassmorphism** | Frosted glass effect | `backdrop-filter: blur()` |
| **Neumorphism** | Soft UI, extruded from bg | CSS box-shadow technique |
| **Bento Grid** | Magazine-style card grids | CSS Grid |
| **Dark Mode First** | Default to dark, offer light | CSS `prefers-color-scheme` |
| **Fluid Typography** | Font sizes that scale with viewport | `clamp()` function |
| **Skeleton Loading** | Placeholder while content loads | `react-loading-skeleton` |
| **Scroll Animations** | Elements animate as you scroll | GSAP ScrollTrigger, AOS |
| **Micro-interactions** | Tiny delightful animations | Framer Motion |
| **AI-generated UI** | v0.dev, Galileo AI, Uizard | AI tools |

---

## 🧪 UX Research Tools (Open Source)

| Tool | GitHub | Purpose |
|------|--------|---------|
| **Hotjar** (free tier) | hotjar.com | Heatmaps, session recording |
| **Microsoft Clarity** | clarity.microsoft.com | Free heatmaps & session replay |
| **PostHog** | https://github.com/PostHog/posthog ⭐ 25k+ | Open source analytics & session recording |
| **Uxwizard** | Community tools | User flow testing |

---

## 📏 Spacing & Layout Systems

### The 8-Point Grid System
- All spacing/sizing values are multiples of 8px
- Common values: 4, 8, 12, 16, 24, 32, 48, 64, 96, 128px

### Tailwind Spacing Reference
```
p-1  = 4px   p-2  = 8px   p-4  = 16px  p-6  = 24px
p-8  = 32px  p-12 = 48px  p-16 = 64px  p-24 = 96px
```

---

## 🎯 UI/UX Checklists

### Before Launch
- [ ] All text passes WCAG AA contrast ratio (4.5:1 for body)
- [ ] Site is usable with keyboard only
- [ ] Mobile viewport tested on real devices
- [ ] Loading states for all async operations
- [ ] Error states for all form inputs
- [ ] 404 and 500 pages designed
- [ ] Favicon and Open Graph images set
- [ ] Page titles and meta descriptions written
- [ ] No placeholder "Lorem Ipsum" text remains
- [ ] All images have `alt` attributes

---

## 🔗 Best GitHub Repositories to Explore

| Repo | Stars | Description |
|------|-------|-------------|
| https://github.com/bradtraversy/design-resources-for-developers | ⭐ 60k+ | Massive design resources list |
| https://github.com/nicehash/NiceHashUI | Various | Design inspiration |
| https://github.com/goabstract/Awesome-Design-Tools | ⭐ 32k+ | Design tools curated list |
| https://github.com/alexpate/awesome-design-systems | ⭐ 16k+ | Design systems collection |
| https://github.com/MoAlyousef/ui-examples | Various | UI examples |
| https://ui.aceternity.com | Source: GitHub | Modern animated components |
| https://ui.shadcn.com | ⭐ 80k+ | Best copy-paste components |
| https://www.radix-ui.com | ⭐ 16k+ | Accessible headless primitives |
