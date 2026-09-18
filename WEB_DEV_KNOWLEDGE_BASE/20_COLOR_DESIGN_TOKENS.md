# 🎨 20 — Color Systems & Design Tokens
> **Use this file when**: Choosing colors, setting up a design token system, or building themes.

---

## 🌈 Color Theory Basics

| Concept | Definition | Web Example |
|---------|------------|-------------|
| **Hue** | The color family | Blue, Red, Green |
| **Saturation** | Intensity/purity | Vivid → Muted |
| **Lightness** | Light/dark value | White → Black |
| **Tint** | Color + White | Light blue |
| **Shade** | Color + Black | Dark blue |
| **Tone** | Color + Gray | Muted blue |
| **Complementary** | Opposite on wheel | Blue + Orange |
| **Analogous** | Adjacent on wheel | Blue + Blue-Green |
| **Triadic** | 3 equidistant | Blue + Red + Yellow |
| **Split-comp** | Color + two adjacent complements | Blue + Yellow-Orange + Red-Orange |

---

## 🎨 Color Palette Systems

### Tailwind CSS Color Scale (Most Popular)
Each color has 11 shades: 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950

```css
/* Example usage */
--color-primary-50:  #eff6ff;  /* Lightest */
--color-primary-100: #dbeafe;
--color-primary-200: #bfdbfe;
--color-primary-300: #93c5fd;
--color-primary-400: #60a5fa;
--color-primary-500: #3b82f6;  /* Base */
--color-primary-600: #2563eb;
--color-primary-700: #1d4ed8;
--color-primary-800: #1e40af;
--color-primary-900: #1e3a8a;
--color-primary-950: #172554;  /* Darkest */
```

### Tailwind Color Reference

#### Blues (Default: blue-600 for buttons)
- `blue-50` `blue-100`...`blue-600`#2563eb `blue-900`
- `sky-400` `indigo-500` `violet-600`

#### Greens (Success states)
- `green-500`#22c55e `emerald-500`#10b981 `teal-500`#14b8a6

#### Reds (Error states)
- `red-500`#ef4444 `rose-500`#f43f5e

#### Yellows/Oranges (Warning states)
- `yellow-400`#facc15 `amber-500`#f59e0b `orange-500`#f97316

#### Grays (Text, borders, backgrounds)
- `gray-50`bg `gray-100`borders `gray-500`muted-text `gray-900`body-text
- `slate-*` `zinc-*` `neutral-*` `stone-*` (alternatives)

---

## 🏗️ Design Token Architecture

### CSS Custom Properties (Modern Approach)
```css
/* tokens.css — Base design tokens */
:root {
  /* === COLOR === */
  /* Brand Palette */
  --brand-primary:    hsl(221, 83%, 53%);   /* blue-600 */
  --brand-secondary:  hsl(262, 83%, 58%);   /* violet-600 */
  --brand-accent:     hsl(171, 77%, 42%);   /* emerald-500 */
  
  /* Semantic Colors */
  --color-bg:         hsl(0, 0%, 100%);
  --color-bg-subtle:  hsl(220, 14%, 96%);   /* gray-100 */
  --color-surface:    hsl(0, 0%, 100%);
  --color-border:     hsl(220, 9%, 89%);    /* gray-200 */
  --color-text:       hsl(222, 47%, 11%);   /* gray-900 */
  --color-text-muted: hsl(215, 16%, 47%);   /* gray-500 */
  --color-text-subtle:hsl(217, 10%, 63%);   /* gray-400 */
  
  /* Status Colors */
  --color-success:    hsl(142, 76%, 36%);
  --color-warning:    hsl(38, 92%, 50%);
  --color-error:      hsl(0, 84%, 60%);
  --color-info:       hsl(204, 94%, 50%);
  
  /* === SPACING === */
  --space-1:  0.25rem;  /* 4px */
  --space-2:  0.5rem;   /* 8px */
  --space-3:  0.75rem;  /* 12px */
  --space-4:  1rem;     /* 16px */
  --space-6:  1.5rem;   /* 24px */
  --space-8:  2rem;     /* 32px */
  --space-12: 3rem;     /* 48px */
  --space-16: 4rem;     /* 64px */
  
  /* === TYPOGRAPHY === */
  --font-sans: 'Inter', system-ui, sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', monospace;
  --text-xs:   0.75rem;
  --text-sm:   0.875rem;
  --text-base: 1rem;
  --text-lg:   1.125rem;
  --text-xl:   1.25rem;
  --text-2xl:  1.5rem;
  --text-3xl:  1.875rem;
  --text-4xl:  2.25rem;
  
  /* === BORDER === */
  --radius-sm:  0.25rem;
  --radius:     0.5rem;
  --radius-md:  0.75rem;
  --radius-lg:  1rem;
  --radius-xl:  1.5rem;
  --radius-full:9999px;
  
  /* === SHADOW === */
  --shadow-sm:  0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow:     0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1);
  --shadow-md:  0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
  --shadow-lg:  0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
  --shadow-xl:  0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
  
  /* === TRANSITION === */
  --transition-fast: 100ms ease;
  --transition:      200ms ease;
  --transition-slow: 300ms ease;
  
  /* === Z-INDEX === */
  --z-base:    0;
  --z-raised:  1;
  --z-dropdown:1000;
  --z-sticky:  1100;
  --z-overlay: 1200;
  --z-modal:   1300;
  --z-toast:   1400;
  --z-tooltip: 1500;
}

/* Dark mode tokens */
[data-theme="dark"], .dark {
  --color-bg:          hsl(222, 47%, 7%);
  --color-bg-subtle:   hsl(222, 47%, 11%);
  --color-surface:     hsl(222, 47%, 11%);
  --color-border:      hsl(215, 28%, 20%);
  --color-text:        hsl(210, 40%, 98%);
  --color-text-muted:  hsl(215, 20%, 65%);
  --color-text-subtle: hsl(215, 16%, 47%);
}
```

---

## 🌟 Professional Color Palettes

### Startup / Modern SaaS
```css
/* Primary: Blue, Accent: Violet */
--primary: #3b82f6;    /* blue-500 */
--accent: #8b5cf6;     /* violet-500 */
--bg: #ffffff;
--surface: #f8fafc;    /* slate-50 */
```

### Dark / Developer / Tech
```css
/* Dark base with electric blue */
--primary: #60a5fa;    /* blue-400 */
--bg: #0f172a;         /* slate-900 */
--surface: #1e293b;    /* slate-800 */
--border: #334155;     /* slate-700 */
```

### Luxury / Premium
```css
/* Deep navy + gold */
--primary: #d4af37;    /* gold */
--bg: #0a0a0a;
--surface: #1a1a1a;
--text: #f5f5f0;
```

### Medical / Health
```css
/* Clean blue + white */
--primary: #0284c7;    /* sky-600 */
--accent: #059669;     /* emerald-600 */
--bg: #f0f9ff;         /* sky-50 */
```

---

## 🛠️ Color Tools

| Tool | URL | Purpose |
|------|-----|---------|
| **Coolors** | coolors.co | Palette generator |
| **Palettte** | palettte.app | Gradient palette builder |
| **Huemint** | huemint.com | AI brand palette |
| **Tailwind Palette** | tailwindcss.com/docs/customizing-colors | Official colors |
| **Radix Colors** | radix-ui.com/colors | Accessible palette |
| **Open Color** | yeun.github.io/open-color | Open-source palette |
| **ColorSpace** | mycolor.space | Similar color finder |
| **Oklch** | oklch.com | Modern color model |
| **contrast ratio** | contrast-ratio.com | WCAG contrast check |
| **WebAIM Contrast** | webaim.org/resources/contrastchecker | WCAG AA/AAA test |
| **Realtime Colors** | realtimecolors.com | See colors on real page |

---

## 🌙 Dark Mode Implementation

### Method 1: CSS class (Tailwind)
```typescript
// tailwind.config.js
{ darkMode: 'class' }

// In HTML/JSX
<html className="dark">

// Usage
<div className="bg-white dark:bg-gray-900 text-gray-900 dark:text-gray-100">
```

### Method 2: CSS attribute
```typescript
// tailwind.config.js
{ darkMode: ['attribute', 'data-theme'] }
<html data-theme="dark">
```

### Toggle Implementation
```typescript
import { useEffect, useState } from 'react'

function useDarkMode() {
  const [isDark, setIsDark] = useState(() => {
    if (typeof window === 'undefined') return false
    return localStorage.getItem('theme') === 'dark' ||
      (!localStorage.getItem('theme') && 
       window.matchMedia('(prefers-color-scheme: dark)').matches)
  })
  
  useEffect(() => {
    document.documentElement.classList.toggle('dark', isDark)
    localStorage.setItem('theme', isDark ? 'dark' : 'light')
  }, [isDark])
  
  return { isDark, toggle: () => setIsDark(d => !d) }
}
```
