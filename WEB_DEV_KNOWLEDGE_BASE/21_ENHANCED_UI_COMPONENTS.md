# 🧩 21 — Enhanced UI Component Libraries (Research-Verified 2025)
> Source: bradtraversy/design-resources-for-developers, enaqx/awesome-react, vuejs/awesome-vue

---

## ⭐ React Component Libraries — Full Reference

### shadcn/ui ⭐ 84k+
```bash
npx shadcn@latest init
npx shadcn@latest add button card dialog input table
```
- Copy-paste (you own the code, full control)
- Built on Radix UI (accessibility) + Tailwind CSS
- 50+ components: Accordion, Alert, Avatar, Badge, Button, Calendar, Card, Carousel, Chart, Checkbox, Combobox, Command, Context Menu, Data Table, Date Picker, Dialog, Drawer, Dropdown, Form, Hover Card, Input, Label, Menubar, Navigation Menu, Pagination, Popover, Progress, Radio, Select, Separator, Sheet, Skeleton, Slider, Switch, Table, Tabs, Textarea, Toast, Toggle, Tooltip

### Material UI (MUI) ⭐ 94k+
```bash
npm i @mui/material @emotion/react @emotion/styled @mui/icons-material
```
- 100+ components following Google Material Design 2/3
- MUI X: advanced data grid, date pickers, charts
- Extensive theming with `createTheme()`

### Ant Design ⭐ 93k+
```bash
npm install antd
```
- Enterprise-class React UI: 60+ high-quality components
- Design language for complex B2B products
- Built-in TypeScript, internationalization (i18n), RTL

### Mantine ⭐ 28k+
```bash
npm i @mantine/core @mantine/hooks @mantine/dates @mantine/form
```
- 100+ components + 50+ hooks
- Rich text editor (tiptap-based), Carousel, Dropzone, Spotlight (⌘K)
- Full dark mode, accessibility, zero config

### Chakra UI ⭐ 38k+
```bash
npm i @chakra-ui/react @emotion/react
```
- Responsive style props (`mt={{ base: 2, md: 4 }}`)
- Color mode (dark/light) via CSS variables
- Accessible by default

### DaisyUI ⭐ 35k+
```bash
npm i -D daisyui
# in tailwind.config: plugins: [require('daisyui')]
```
- 56+ components, 30+ themes
- Pure CSS — no JS dependency
- Themes: `light, dark, cupcake, cyberpunk, retro, synthwave, dracula, ...`

### HeroUI (formerly NextUI) ⭐ 23k+
```bash
npm i @heroui/react framer-motion
```
- Modern, beautiful React + Tailwind + Framer Motion
- Compound component pattern

### Flowbite ⭐ 8k+
```bash
npm i flowbite flowbite-react
```
- 400+ Tailwind UI blocks, React components
- Official React, Vue, Svelte, Angular support

### Aceternity UI (Trending 2025)
- Website: https://ui.aceternity.com/
- Premium animated components: Sticky Scroll, Spotlight, Lamp, Tabs, Background Beams, Meteors, Typewriter Effect, etc.
- Copy-paste pattern, uses Tailwind + Framer Motion

### Magic UI (Trending 2025)
- Website: https://magicui.design/
- Marketing and landing page components with animations
- Components: Globe, Terminal, Confetti, Ripple, Shine Border, Animated Gradient, Word Rotate

### PrimeReact ⭐ 6k+
```bash
npm i primereact primeicons
```
- 90+ open-source components
- Multiple built-in themes
- DataTable with sorting, filtering, pagination, virtual scroll

### Ariakit ⭐ 7k+
```bash
npm i @ariakit/react
```
- Toolkit for building accessible React apps
- Strict WAI-ARIA compliance

---

## 🟢 Vue Component Libraries — Full Reference

### Vuetify ⭐ 40k+
```bash
npm i vuetify
```
- 80+ Material Design 3 components
- A11y, RTL support, tree-shakeable

### Quasar ⭐ 27k+
```bash
npm i -g @quasar/cli
quasar create my-app
```
- Build for Web, Mobile (Cordova/Capacitor), Desktop (Electron), SSR, PWA from ONE codebase
- 70+ high-quality components

### PrimeVue ⭐ 14k+
```bash
npm i primevue
```
- 90+ components, design agnostic, unstyled mode

### Element Plus ⭐ 24k+
```bash
npm i element-plus
```
- Vue 3 successor to Element UI
- Popular for Vue 3 admin panels

### Nuxt UI ⭐ 6k+
```bash
npx nuxi@latest module add ui
```
- Official Nuxt-optimized UI library

### shadcn-vue ⭐ 5k+
```bash
npx shadcn-vue@latest init
```
- shadcn/ui ported to Vue 3

---

## 🅰️ Angular Component Libraries — Full Reference

### Angular Material ⭐ 24k+
```bash
ng add @angular/material
```
- Official Google-maintained Material Design components

### PrimeNG ⭐ 10k+
```bash
npm i primeng
```
- 90+ rich Angular UI components

### NG-ZORRO ⭐ 9k+
```bash
ng add ng-zorro-antd
```
- Ant Design for Angular — enterprise grade

### Nebular ⭐ 8k+
```bash
npm i @nebular/theme
```
- 40+ customizable Angular UI components

---

## 🎪 Headless / Unstyled Libraries

| Library | Stars | Approach | Install |
|---------|-------|---------|---------|
| **Radix UI** | ⭐ 16k+ | React primitives | `npm i @radix-ui/react-*` |
| **Headless UI** | ⭐ 26k+ | React + Vue | `npm i @headlessui/react` |
| **Ark UI** | ⭐ 4k+ | Framework-agnostic | `npm i @ark-ui/react` |
| **React Aria** | ⭐ 13k+ | Adobe, WAI-ARIA strict | `npm i @react-aria/*` |
| **Base UI** | MUI-backed | Next-gen headless | `npm i @base-ui-components/react` |

---

## 📊 Specialized Components — Exhaustive List

### Data Tables
| Library | Install | Stars | Highlights |
|---------|---------|-------|------------|
| **TanStack Table** | `@tanstack/react-table` | ⭐ 25k+ | Headless, supports React/Vue/Svelte |
| **AG Grid** | `ag-grid-react` | ⭐ 13k+ | Enterprise, Excel-like features |

### Charts & Data Visualization
| Library | Install | Stars | Best For |
|---------|---------|-------|---------|
| **D3.js** | `d3` | ⭐ 108k+ | Ultimate flexibility |
| **Chart.js** | `chart.js` | ⭐ 64k+ | Simple, universal |
| **ECharts** | `echarts` | ⭐ 60k+ | Complex charts |
| **Recharts** | `recharts` | ⭐ 24k+ | React-native |
| **Tremor** | `@tremor/react` | ⭐ 18k+ | Dashboard components |
| **Visx** | `@visx/group` | ⭐ 20k+ | D3 + React, Airbnb |
| **ApexCharts** | `apexcharts` | ⭐ 14k+ | Interactive |
| **Nivo** | `@nivo/core` | ⭐ 13k+ | React + D3, great docs |
| **Victory** | `victory` | ⭐ 11k+ | Composable React charts |

### Rich Text Editors
| Library | Install | Stars | Notes |
|---------|---------|-------|-------|
| **Tiptap** | `@tiptap/react` | ⭐ 27k+ | Extension-based, best DX |
| **Quill** | `react-quill` | ⭐ 43k+ | Classic, widely used |
| **Lexical** | `lexical` | ⭐ 19k+ | Facebook-built, React |
| **Slate.js** | `slate slate-react` | ⭐ 30k+ | Fully customizable |
| **CKEditor 5** | `npm i ckeditor5` | ⭐ 9k+ | Enterprise-grade |
| **Milkdown** | `@milkdown/core` | ⭐ 8k+ | Plugin-based, markdown |

### Drag & Drop
| Library | Install | Stars |
|---------|---------|-------|
| **dnd-kit** | `@dnd-kit/core` | ⭐ 13k+ |
| **react-beautiful-dnd** | `react-beautiful-dnd` | ⭐ 32k+ |
| **Atlassian Pragmatic DnD** | `@atlaskit/pragmatic-drag-and-drop` | By Atlassian |

### Carousels / Sliders
| Library | Install | Stars |
|---------|---------|-------|
| **Swiper** | `swiper` | ⭐ 39k+ |
| **Embla Carousel** | `embla-carousel-react` | ⭐ 7k+ |
| **Keen Slider** | `keen-slider` | ⭐ 5k+ |
| **Splide** | `@splidejs/splide` | ⭐ 4k+ |

### Toast / Notifications
| Library | Install | Stars |
|---------|---------|-------|
| **Sonner** | `sonner` | ⭐ 8k+ |
| **React Hot Toast** | `react-hot-toast` | ⭐ 9k+ |
| **React Toastify** | `react-toastify` | ⭐ 13k+ |
| **Notistack** | `notistack` | ⭐ 4k+ |

### Modal / Dialog
| Library | Stars | Notes |
|---------|-------|-------|
| **Radix Dialog** | ⭐ 16k+ | Built into shadcn/ui |
| **Headless UI Dialog** | ⭐ 26k+ | Tailwind Labs |
| **react-modal** | ⭐ 7k+ | Simple, standalone |

### Date Pickers
| Library | Install | Stars |
|---------|---------|-------|
| **react-day-picker** | `react-day-picker` | ⭐ 6k+ |
| **react-datepicker** | `react-datepicker` | ⭐ 8k+ |
| **Flatpickr** | `flatpickr` | ⭐ 16k+ |
| **Pikaday** | `pikaday` | ⭐ 8k+ |

### Form Libraries
| Library | Install | Stars | Notes |
|---------|---------|-------|-------|
| **React Hook Form** | `react-hook-form` | ⭐ 40k+ | Best performance |
| **Formik** | `formik` | ⭐ 33k+ | Classic, popular |
| **VeeValidate** | `vee-validate` | ⭐ 10k+ | Vue-first |
| **Zod** | `zod` | ⭐ 35k+ | TypeScript schema validation |
| **Yup** | `yup` | ⭐ 22k+ | Schema validation |

### Map Libraries
| Library | Install | Stars |
|---------|---------|-------|
| **Leaflet** | `react-leaflet` | ⭐ 41k+ |
| **Mapbox GL** | `mapbox-gl` | ⭐ 11k+ |
| **Google Maps** | `@react-google-maps/api` | Popular |
| **Pigeon Maps** | `pigeon-maps` | ⭐ 3k+ |

### Virtual Scroll / Infinite List
| Library | Install | Stars |
|---------|---------|-------|
| **react-window** | `react-window` | ⭐ 16k+ |
| **react-virtuoso** | `react-virtuoso` | ⭐ 5k+ |
| **@tanstack/virtual** | `@tanstack/react-virtual` | ⭐ 5k+ |

### Command Palette / Search
| Library | Install | Stars |
|---------|---------|-------|
| **cmdk** | `cmdk` | ⭐ 9k+ | shadcn Command component |
| **kbar** | `kbar` | ⭐ 4k+ | Keyboard shortcut UI |
| **Spotlight (Mantine)** | `@mantine/spotlight` | Part of Mantine |
