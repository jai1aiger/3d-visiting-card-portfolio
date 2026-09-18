# 🎨 04 — CSS Frameworks, Styling & Preprocessors
> **Use this file when**: Styling any web project, choosing a CSS methodology, or setting up a styling system.

---

## ⚡ CSS Framework Comparison

| Framework | Approach | Bundle Size | Learning Curve | Best For |
|-----------|----------|------------|----------------|---------|
| **Tailwind CSS** | Utility-first | ~10KB (purged) | Medium | Rapid development, custom designs |
| **Bootstrap 5** | Component-first | ~22KB | Low | Quick prototypes, legacy projects |
| **Bulma** | Component-first | ~22KB | Low | Clean, no-JS framework |
| **Foundation** | Component-first | ~17KB | Medium | Enterprise, flexible grid |
| **UnoCSS** | Utility-first | ~0KB (on-demand) | Medium | Maximum performance |
| **Open Props** | Design tokens | ~7KB | Low | CSS custom properties system |
| **Pico CSS** | Semantic | ~10KB | Very Low | Minimal, no classes needed |
| **MVP.css** | Semantic | ~7KB | Very Low | Rapid prototyping |

---

## 🌊 Tailwind CSS (Most Popular Utility-First)

GitHub: https://github.com/tailwindlabs/tailwindcss ⭐ 83k+

### Setup with Vite
```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

```js
// tailwind.config.js
module.exports = {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx,vue,svelte}'],
  theme: {
    extend: {
      colors: {
        brand: { 50: '#f0f9ff', 500: '#0ea5e9', 900: '#0c4a6e' }
      },
      fontFamily: { sans: ['Inter', 'sans-serif'] }
    }
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/aspect-ratio'),
  ]
}
```

### Essential Tailwind Plugins
| Plugin | Install | Purpose |
|--------|---------|---------|
| `@tailwindcss/forms` | `npm i -D @tailwindcss/forms` | Beautiful form styles |
| `@tailwindcss/typography` | `npm i -D @tailwindcss/typography` | Prose/article styling (`prose` class) |
| `@tailwindcss/aspect-ratio` | `npm i -D @tailwindcss/aspect-ratio` | Aspect ratio utilities |
| `@tailwindcss/line-clamp` | Built-in v3.3+ | Text truncation |
| `tailwindcss-animate` | `npm i -D tailwindcss-animate` | Animation utilities |
| `daisyui` | `npm i -D daisyui` | Component plugin |
| `shadcn-ui` | `npx shadcn@latest init` | Copy-paste components |

### Tailwind Quick Reference
```html
<!-- Flexbox Layout -->
<div class="flex items-center justify-between gap-4">

<!-- Grid Layout -->
<div class="grid grid-cols-3 gap-6 md:grid-cols-2 sm:grid-cols-1">

<!-- Typography -->
<h1 class="text-4xl font-bold tracking-tight text-gray-900 dark:text-white">
<p class="text-base text-gray-600 leading-relaxed max-w-prose">

<!-- Card -->
<div class="rounded-xl border bg-white shadow-sm p-6 hover:shadow-md transition-shadow">

<!-- Button -->
<button class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 active:scale-95 transition-all">

<!-- Badge -->
<span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800">

<!-- Gradient Text -->
<span class="bg-gradient-to-r from-blue-600 to-violet-600 bg-clip-text text-transparent">

<!-- Glass effect -->
<div class="backdrop-blur-md bg-white/30 border border-white/20 rounded-xl shadow-xl">
```

---

## 🅱️ Bootstrap 5

GitHub: https://github.com/twbs/bootstrap ⭐ 171k+

```bash
npm i bootstrap @popperjs/core
# OR via CDN
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
```

### Key Bootstrap 5 Features
- Flexbox-based grid
- CSS custom properties (no jQuery!)
- Utility API (customize with Sass)
- RTL support
- Dark mode support

---

## 🔮 UnoCSS (Fastest Utility CSS)

GitHub: https://github.com/unocss/unocss ⭐ 17k+

```bash
npm i -D unocss
```

- On-demand atomic CSS (only generates used classes)
- Compatible with Tailwind, Windi CSS presets
- Fastest CSS engine available
- Icons preset (100k+ icons as CSS!)

---

## 🖌️ CSS Preprocessors

### Sass/SCSS (Most Popular)
```bash
npm i -D sass
```

```scss
// Variables
$primary: #3b82f6;
$border-radius: 0.5rem;

// Mixins
@mixin flex-center {
  display: flex;
  align-items: center;
  justify-content: center;
}

// Nesting
.card {
  border-radius: $border-radius;
  
  &:hover { transform: translateY(-2px); }
  
  &__header { @include flex-center; }
  &__body { padding: 1.5rem; }
}

// Maps for design tokens
$colors: (
  "primary": #3b82f6,
  "success": #10b981,
  "danger": #ef4444,
);
```

### PostCSS
```bash
npm i -D postcss autoprefixer postcss-nested postcss-custom-media
```
- Autoprefixer: adds vendor prefixes automatically
- Transform future CSS today

---

## ✨ CSS-in-JS Solutions

| Library | GitHub | Approach | Performance |
|---------|--------|---------|-------------|
| **Styled Components** | ⭐ 40k+ | Template literals | Good |
| **Emotion** | ⭐ 17k+ | Template literals / Object | Better |
| **Stitches** | ⭐ 8k+ | Near-zero runtime | Best |
| **Vanilla Extract** | ⭐ 10k+ | Zero-runtime, type-safe | Excellent |
| **Panda CSS** | ⭐ 6k+ | Compile-time, design tokens | Excellent |
| **StyleX** | ⭐ 9k+ | Facebook, atomic, zero-runtime | Excellent |

---

## 🎭 Modern CSS Techniques (No Framework Needed)

### CSS Custom Properties (Variables)
```css
:root {
  --color-primary: #3b82f6;
  --color-bg: #ffffff;
  --radius: 0.5rem;
  --shadow: 0 1px 3px rgb(0 0 0 / 0.1);
  --transition: 200ms ease;
}

[data-theme="dark"] {
  --color-bg: #0f172a;
  --color-text: #e2e8f0;
}
```

### Container Queries (Modern Responsive)
```css
.card-container {
  container-type: inline-size;
}

@container (min-width: 400px) {
  .card { flex-direction: row; }
}
```

### Fluid Typography with clamp()
```css
html {
  font-size: clamp(14px, 1.5vw, 18px);
}

h1 {
  font-size: clamp(1.8rem, 5vw, 4rem);
  line-height: 1.1;
}
```

### CSS Grid Patterns
```css
/* Holy Grail Layout */
.layout {
  display: grid;
  grid-template: auto 1fr auto / 250px 1fr;
  min-height: 100vh;
}

/* Masonry-like */
.masonry {
  columns: 3 200px;
  gap: 1.5rem;
}

/* Centering */
.center {
  display: grid;
  place-items: center;
}
```

---

## 🌈 CSS Animations & Transitions

```css
/* Smooth transitions */
.btn {
  transition: all 200ms cubic-bezier(0.4, 0, 0.2, 1);
}

/* Keyframe animation */
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(20px); }
  to   { opacity: 1; transform: translateY(0); }
}

.element { animation: fadeInUp 0.5s ease forwards; }

/* Scroll-driven animations (CSS-only) */
@keyframes reveal {
  from { opacity: 0; transform: scale(0.8); }
  to   { opacity: 1; transform: scale(1); }
}

.card {
  animation: reveal linear both;
  animation-timeline: view();
  animation-range: entry 0% entry 50%;
}
```

---

## 📚 CSS Methodology: BEM

```css
/* Block */
.card { }

/* Element */
.card__header { }
.card__body { }
.card__footer { }

/* Modifier */
.card--featured { }
.card--dark { }
.card__button--primary { }
```

---

## 🔗 Key CSS Resources on GitHub

| Resource | Stars | Link |
|----------|-------|------|
| Tailwind CSS | ⭐ 83k+ | https://github.com/tailwindlabs/tailwindcss |
| Bootstrap | ⭐ 171k+ | https://github.com/twbs/bootstrap |
| Sass | ⭐ 15k+ | https://github.com/sass/sass |
| Animate.css | ⭐ 81k+ | https://github.com/animate-css/animate.css |
| Normalize.css | ⭐ 52k+ | https://github.com/necolas/normalize.css |
| Open Props | ⭐ 5k+ | https://github.com/argyleink/open-props |
| CSS Tricks | — | https://css-tricks.com |
| Cssmatic | — | https://www.cssmatic.com |
