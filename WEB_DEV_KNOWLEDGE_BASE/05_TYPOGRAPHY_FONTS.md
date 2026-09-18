# 🔤 05 — Typography & Fonts
> **Use this file when**: Choosing fonts, setting up type scales, or optimizing font loading.

---

## 🎯 Typography Principles

| Principle | Rule |
|-----------|------|
| **Readability** | Body text: 16–18px, line-height 1.5–1.7 |
| **Contrast** | Minimum 4.5:1 contrast ratio for body text |
| **Hierarchy** | 3–4 type sizes maximum per design |
| **Width** | Optimal line length: 60–80 characters (45–75 chars for narrow) |
| **Pairing** | Combine a serif/display font + clean sans-serif |
| **Loading** | Subset fonts, use `font-display: swap` |
| **System Fonts** | Use system stack for performance-critical sites |

---

## 🔤 Google Fonts (Free, 1500+ fonts)

```html
<!-- In <head> — Optimized loading -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
```

```css
/* Usage */
body { font-family: 'Inter', sans-serif; }
```

### Top Professional Font Pairings

| Heading Font | Body Font | Vibe |
|-------------|-----------|------|
| **Playfair Display** | **Source Sans 3** | Elegant, editorial |
| **Merriweather** | **Open Sans** | Classic, trustworthy |
| **Montserrat** | **Lato** | Modern, corporate |
| **Raleway** | **Roboto** | Clean, tech |
| **DM Serif Display** | **DM Sans** | Contemporary, startup |
| **Fraunces** | **Inter** | Bold, premium |
| **Space Grotesk** | **Space Mono** | Developer, techy |
| **Syne** | **Epilogue** | Creative, agency |
| **Cabinet Grotesk** | **Satoshi** | Boutique, luxury |
| **Clash Display** | **General Sans** | Fashion, design |

---

## 💎 Premium & Variable Fonts

### Variable Fonts (Single file, all weights)
```css
/* Variable font — supports any weight 100-900 */
@font-face {
  font-family: 'Inter';
  src: url('/fonts/Inter-Variable.woff2') format('woff2');
  font-weight: 100 900;
  font-display: swap;
}
```

### Top Variable Fonts (Free)
| Font | Where | Weights |
|------|-------|---------|
| **Inter** | fontsource.org / Google | 100-900 |
| **Plus Jakarta Sans** | Google Fonts | 200-800 |
| **Nunito** | Google Fonts | 200-900 |
| **DM Sans** | Google Fonts | 100-900 |
| **Bricolage Grotesque** | Google Fonts | 200-800 |
| **Geist** | vercel/geist-font ⭐ | 100-900 |
| **Cal Sans** | calcom/cal-sans | Display |
| **Outfit** | Google Fonts | 100-900 |

---

## 📦 Font Loading Libraries

### Fontsource (Self-host Google Fonts)
GitHub: https://github.com/fontsource/fontsource ⭐ 5k+
```bash
npm i @fontsource/inter @fontsource-variable/inter
```
```js
// In your entry file
import '@fontsource-variable/inter'
```
Benefits: No external request, GDPR-compliant, works offline

### Next.js Font Optimization
```typescript
import { Inter, Playfair_Display } from 'next/font/google'

const inter = Inter({ 
  subsets: ['latin'],
  variable: '--font-inter',
  display: 'swap'
})

const playfair = Playfair_Display({
  subsets: ['latin'],
  variable: '--font-playfair',
  weight: ['400', '700', '900']
})

// In layout.tsx
<body className={`${inter.variable} ${playfair.variable}`}>
```

---

## 📏 Type Scale Systems

### Major Third Scale (1.25x ratio)
```css
:root {
  --text-xs:   0.64rem;   /* ~10px */
  --text-sm:   0.8rem;    /* ~13px */
  --text-base: 1rem;      /* 16px  */
  --text-lg:   1.25rem;   /* 20px  */
  --text-xl:   1.563rem;  /* 25px  */
  --text-2xl:  1.953rem;  /* 31px  */
  --text-3xl:  2.441rem;  /* 39px  */
  --text-4xl:  3.052rem;  /* 49px  */
}
```

### Tailwind Type Scale Reference
```
text-xs    = 12px    text-xl    = 20px
text-sm    = 14px    text-2xl   = 24px
text-base  = 16px    text-3xl   = 30px
text-lg    = 18px    text-4xl   = 36px
                     text-5xl   = 48px
                     text-6xl   = 60px
                     text-7xl   = 72px
                     text-8xl   = 96px
                     text-9xl   = 128px
```

---

## 🛠️ Typography Tools

| Tool | URL | Purpose |
|------|-----|---------|
| **Typescale** | typescale.com | Visual type scale generator |
| **Type-Scale** | type-scale.com | Modular scale calculator |
| **Fontjoy** | fontjoy.com | AI font pairing generator |
| **Google Fonts** | fonts.google.com | Free web fonts |
| **Adobe Fonts** | fonts.adobe.com | Premium (with CC subscription) |
| **Font Squirrel** | fontsquirrel.com | Free for commercial use |
| **DaFont** | dafont.com | Free fonts |
| **Font Brief** | fontbrief.com | Find fonts by description |
| **Wordmark.it** | wordmark.it | Preview text in installed fonts |

---

## 💻 System Font Stacks

```css
/* Modern System UI Stack */
body {
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 
    'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 
    'Open Sans', 'Helvetica Neue', sans-serif;
}

/* Monospace */
code {
  font-family: 'JetBrains Mono', 'Fira Code', 'Cascadia Code',
    'Source Code Pro', Consolas, 'Courier New', monospace;
}

/* Readable serif */
article {
  font-family: 'Georgia', 'Times New Roman', 
    'Noto Serif', serif;
}
```

---

## 🌐 Font Performance Best Practices

```html
<!-- 1. Preconnect to font origin -->
<link rel="preconnect" href="https://fonts.googleapis.com">

<!-- 2. Preload critical fonts -->
<link rel="preload" as="font" href="/fonts/inter.woff2" 
      type="font/woff2" crossorigin>
```

```css
/* 3. Always use font-display: swap */
@font-face {
  font-family: 'MyFont';
  src: url('/fonts/myfont.woff2') format('woff2');
  font-display: swap;  /* Show fallback while loading */
}

/* 4. Subset fonts to needed characters */
/* Use tools: glyphhanger, subfont, pyftsubset */

/* 5. Avoid FOIT (Flash of Invisible Text) */
/* font-display: swap prevents this */
```

---

## 📝 Markdown Typography (Prose Styling)

```bash
npm i -D @tailwindcss/typography
```

```html
<article class="prose prose-lg prose-gray dark:prose-invert max-w-none">
  <!-- Your markdown/HTML content here -->
</article>
```

Customization:
```js
// tailwind.config.js
typography: {
  DEFAULT: {
    css: {
      color: '#374151',
      a: { color: '#3b82f6', '&:hover': { color: '#2563eb' } },
      h1: { fontFamily: 'Playfair Display, serif' },
    }
  }
}
```
