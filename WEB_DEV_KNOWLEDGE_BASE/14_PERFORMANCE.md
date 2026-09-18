# ⚡ 14 — Performance Optimization
> **Use this file when**: Improving website speed, Core Web Vitals, or optimizing assets.

---

## 📊 Core Web Vitals Targets

| Metric | Good | Needs Improvement | Poor | Measures |
|--------|------|-------------------|------|---------|
| **LCP** (Largest Contentful Paint) | < 2.5s | 2.5s–4s | > 4s | Loading speed |
| **INP** (Interaction to Next Paint) | < 200ms | 200–500ms | > 500ms | Interactivity |
| **CLS** (Cumulative Layout Shift) | < 0.1 | 0.1–0.25 | > 0.25 | Visual stability |
| **FCP** (First Contentful Paint) | < 1.8s | 1.8–3s | > 3s | First paint |
| **TTFB** (Time to First Byte) | < 800ms | 800ms–1.8s | > 1.8s | Server response |

---

## 🖼️ Image Optimization

### Next.js Image Component (Best Practice)
```jsx
import Image from 'next/image'

// Next.js automatically: WebP conversion, lazy loading, size optimization
<Image
  src="/hero.jpg"
  alt="Hero image"
  width={1200}
  height={600}
  priority={true}      // LCP image — load eagerly
  quality={85}
  placeholder="blur"
  blurDataURL="data:image/jpeg;base64,/9j/..."
/>
```

### Sharp (Node.js Image Processing)
```bash
npm i sharp
```
```javascript
import sharp from 'sharp'

// Convert and optimize
await sharp('input.jpg')
  .resize(1200, 630, { fit: 'cover' })
  .webp({ quality: 85 })
  .toFile('output.webp')

// Generate responsive sizes
const sizes = [320, 640, 960, 1280]
for (const size of sizes) {
  await sharp('hero.jpg')
    .resize(size)
    .webp({ quality: 80 })
    .toFile(`hero-${size}.webp`)
}
```

### Modern Image Formats
```html
<!-- Use picture element for format fallback -->
<picture>
  <source srcset="image.avif" type="image/avif">
  <source srcset="image.webp" type="image/webp">
  <img src="image.jpg" alt="..." loading="lazy" decoding="async">
</picture>
```

### CSS for Images
```css
/* Always specify dimensions to prevent CLS */
img {
  width: 100%;
  height: auto;
  aspect-ratio: 16 / 9;
}

/* Lazy loading */
img { loading: lazy; decoding: async; }

/* LCP image — eager load */
.hero img { loading: eager; fetchpriority: high; }
```

---

## 🔤 Font Performance

```html
<!-- Critical: Preconnect + Preload -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="font" href="/fonts/inter.woff2" 
      type="font/woff2" crossorigin>
```

```css
@font-face {
  font-family: 'Inter';
  src: url('/fonts/inter.woff2') format('woff2');
  font-weight: 400 700;
  font-display: swap;     /* Prevents FOIT */
  size-adjust: 100%;      /* Reduce CLS from font swap */
  ascent-override: 90%;   /* Match fallback metrics */
}
```

---

## 📦 Code Splitting & Lazy Loading

### React Lazy + Suspense
```tsx
import { lazy, Suspense } from 'react'

// Lazy load heavy components
const HeavyChart = lazy(() => import('./HeavyChart'))
const Map = lazy(() => import('./Map'))

function App() {
  return (
    <Suspense fallback={<div className="skeleton h-64" />}>
      <HeavyChart />
    </Suspense>
  )
}
```

### Next.js Dynamic Import
```typescript
import dynamic from 'next/dynamic'

// No SSR (client-only component)
const MapComponent = dynamic(() => import('./Map'), { 
  ssr: false,
  loading: () => <Skeleton />
})

// With named export
const HeavyEditor = dynamic(() => 
  import('./Editor').then(m => m.Editor), { ssr: false }
)
```

### Route-Based Code Splitting (React Router)
```typescript
const HomePage = lazy(() => import('./pages/Home'))
const AboutPage = lazy(() => import('./pages/About'))

<Suspense fallback={<PageLoader />}>
  <Routes>
    <Route path="/" element={<HomePage />} />
    <Route path="/about" element={<AboutPage />} />
  </Routes>
</Suspense>
```

---

## 🚀 Caching Strategies

### HTTP Cache Headers
```javascript
// Express
app.use('/static', express.static('public', {
  maxAge: '1y',   // 1 year for hashed assets
  etag: false
}))

// Next.js API Route
res.setHeader('Cache-Control', 'public, s-maxage=60, stale-while-revalidate=300')
```

### Service Worker Caching (PWA)
```bash
npm i -D vite-plugin-pwa   # Vite
npm i workbox-webpack-plugin  # Webpack
# OR use Workbox directly
```

---

## ♻️ React Performance Patterns

```typescript
// 1. Memoize expensive computations
const expensiveValue = useMemo(() => computeExpensive(items), [items])

// 2. Stable callback references
const handleClick = useCallback((id: number) => {
  setSelected(id)
}, [])

// 3. Prevent unnecessary re-renders
const MemoizedCard = memo(Card, (prev, next) => prev.id === next.id)

// 4. Virtualize long lists
import { FixedSizeList } from 'react-window'
<FixedSizeList height={600} itemCount={10000} itemSize={50} width="100%">
  {({ index, style }) => <div style={style}>Row {index}</div>}
</FixedSizeList>

// 5. Defer non-critical state updates
import { startTransition } from 'react'
startTransition(() => setSearchQuery(value))
```

---

## 🔍 Performance Measurement Tools

| Tool | URL | Type |
|------|-----|------|
| **Google PageSpeed** | pagespeed.web.dev | CWV analysis |
| **Lighthouse** | Chrome DevTools | Full audit |
| **WebPageTest** | webpagetest.org | Deep analysis |
| **GTmetrix** | gtmetrix.com | Performance grading |
| **BundlePhobia** | bundlephobia.com | npm package size |
| **Import Cost** | VS Code extension | Show import sizes |
| **React DevTools Profiler** | Browser extension | React rendering |
| **Chrome Coverage** | DevTools → Coverage | Unused code |
| **web-vitals** | npm i web-vitals | Measure in production |

### Measuring CWV in Code
```typescript
import { onCLS, onINP, onLCP, onFCP, onTTFB } from 'web-vitals'

function sendToAnalytics({ name, value, id }) {
  console.log(`${name}: ${value}`)
  // Send to your analytics...
}

onCLS(sendToAnalytics)
onINP(sendToAnalytics)
onLCP(sendToAnalytics)
onFCP(sendToAnalytics)
onTTFB(sendToAnalytics)
```

---

## 📋 Performance Checklist

- [ ] Images: WebP/AVIF format, correct dimensions, lazy loading
- [ ] LCP image: `fetchpriority="high"` or `priority` in Next.js
- [ ] Fonts: `font-display: swap`, self-hosted or preloaded
- [ ] Critical CSS: inline above-the-fold styles
- [ ] JavaScript: code split, lazy loaded routes
- [ ] No layout shift: explicit dimensions on images/embeds
- [ ] Compress: Brotli/Gzip for HTML/CSS/JS
- [ ] CDN: static assets served from CDN
- [ ] Prefetch: `<link rel="prefetch">` for next likely page
- [ ] Resource hints: `<link rel="preconnect">` for third parties
- [ ] HTTP/2: multiple assets in parallel
- [ ] Cache: long TTL for hashed static assets
