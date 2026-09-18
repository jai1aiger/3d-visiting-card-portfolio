# 🎭 06 — Icons & Illustrations
> **Use this file when**: Adding icons to any web project or selecting illustration styles.

---

## 🔷 Icon Libraries Comparison

| Library | Icons | License | Format | Size | Install |
|---------|-------|---------|--------|------|---------|
| **Lucide** | 1500+ | ISC | SVG | tiny | `npm i lucide-react` |
| **Heroicons** | 292 | MIT | SVG | tiny | `npm i @heroicons/react` |
| **Radix Icons** | 318 | MIT | SVG | tiny | `npm i @radix-ui/react-icons` |
| **Phosphor Icons** | 9000+ | MIT | SVG | flexible | `npm i phosphor-react` |
| **Tabler Icons** | 5700+ | MIT | SVG | small | `npm i @tabler/icons-react` |
| **Feather Icons** | 286 | MIT | SVG | tiny | `npm i feather-icons` |
| **React Icons** | 60k+ | Various | SVG | varies | `npm i react-icons` |
| **Iconify** | 200k+ | Various | SVG | on-demand | `npm i @iconify/react` |
| **Font Awesome** | 2000+ free | Free+Pro | Font/SVG | medium | CDN or npm |
| **Material Icons** | 2100+ | Apache | SVG/Font | medium | Google CDN |
| **Bootstrap Icons** | 2000+ | MIT | SVG | small | `npm i bootstrap-icons` |
| **Remix Icons** | 2800+ | Apache | SVG | small | `npm i remixicon` |
| **Simple Icons** | 3000+ | CC0 | SVG | tiny | Brand icons only |

---

## ⭐ Top Recommended Icon Libraries

### 1. Lucide React (Best Default Choice)
GitHub: https://github.com/lucide-icons/lucide ⭐ 12k+
```bash
npm i lucide-react
```
```jsx
import { Search, User, Settings, ChevronRight } from 'lucide-react'

<Search size={20} strokeWidth={1.5} className="text-gray-500" />
<User className="w-5 h-5 text-blue-600" />
```

### 2. Heroicons (Tailwind Team)
GitHub: https://github.com/tailwindlabs/heroicons ⭐ 21k+
```bash
npm i @heroicons/react
```
```jsx
import { MagnifyingGlassIcon } from '@heroicons/react/24/outline'
import { StarIcon } from '@heroicons/react/24/solid'

<MagnifyingGlassIcon className="h-5 w-5" />
```

### 3. Phosphor Icons (Most Variants)
GitHub: https://github.com/phosphor-icons/react ⭐ 1.5k+
```bash
npm i @phosphor-icons/react
```
```jsx
import { Horse, Heart, Cube } from '@phosphor-icons/react'
// Variants: Regular, Thin, Light, Bold, Fill, Duotone
<Heart weight="fill" size={32} color="#ef4444" />
```

### 4. React Icons (Meta-library, 60k+ icons)
GitHub: https://github.com/react-icons/react-icons ⭐ 12k+
```bash
npm i react-icons
```
```jsx
import { FaGithub, FaTwitter } from 'react-icons/fa'      // FontAwesome
import { SiReact, SiNextdotjs } from 'react-icons/si'     // Simple Icons (brands)
import { MdEmail, MdPhone } from 'react-icons/md'          // Material Design
import { IoLogoVercel } from 'react-icons/io5'             // Ionicons
```

### 5. Iconify (200k+ from all libraries)
GitHub: https://github.com/iconify/iconify ⭐ 4k+
```bash
npm i @iconify/react
```
```jsx
import { Icon } from '@iconify/react'
<Icon icon="mdi:github" width="24" height="24" />
<Icon icon="logos:react" />
<Icon icon="twemoji:flag-india" />
```

---

## 🎨 SVG Icon Best Practices

```jsx
// Component pattern for custom SVG icons
const StarIcon = ({ size = 24, color = 'currentColor', ...props }) => (
  <svg 
    width={size} 
    height={size} 
    viewBox="0 0 24 24" 
    fill="none"
    stroke={color}
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
    {...props}
  >
    <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2" />
  </svg>
)
```

---

## 🖼️ Illustration Libraries

### Free Illustration Sets
| Library | URL | Style | License |
|---------|-----|-------|---------|
| **unDraw** | undraw.co | Flat, customizable | MIT |
| **Storyset** | storyset.com | Diverse styles | Free with attribution |
| **Illustrations.co** | illlustrations.co | 3D isometric | Free |
| **DrawKit** | drawkit.com | Various | Free + Premium |
| **Blush** | blush.design | Diverse, AI | Freemium |
| **Humaaans** | humaaans.com | Customizable people | CC-BY |
| **Open Doodles** | opendoodles.com | Hand-drawn | CC0 |
| **Streamline** | streamlinehq.com | 80k+ illustrations | Freemium |
| **Popsy** | popsy.co | Notion-style | Free |
| **Control.rocks** | control.rocks | Abstract people | Free |

### Paid Illustration Libraries
| Library | Price | Notes |
|---------|-------|-------|
| **Icons8** | ~$13/mo | Illustrations + icons + photos |
| **Envato Elements** | ~$16/mo | All creative assets |
| **Creative Market** | Per item | Premium collections |

---

## 🌟 Lottie Animations (JSON-based)

GitHub: https://github.com/airbnb/lottie-web ⭐ 31k+
```bash
npm i lottie-react  # React
npm i @lottiefiles/dotlottie-react  # Lightweight version
```
```jsx
import Lottie from 'lottie-react'
import animationData from './animation.json'

<Lottie animationData={animationData} loop={true} style={{width: 200}} />
```

### Where to Get Lottie Animations
- **LottieFiles**: lottiefiles.com — Free & premium
- **IconScout**: iconscout.com
- **Lordicon**: lordicon.com

---

## 🔧 Icon Tools & Generators

| Tool | URL | Purpose |
|------|-----|---------|
| **SVGR** | github.com/gregberge/svgr ⭐ 10k+ | Convert SVG to React component |
| **SVGO** | github.com/svg/svgo ⭐ 21k+ | Optimize SVG files |
| **Icomoon** | icomoon.io | Custom icon font generator |
| **Fontello** | fontello.com | Icon font builder |
| **RealFaviconGenerator** | realfavicongenerator.net | Favicon generator |
| **SVG Crop** | svgcrop.com | Remove whitespace from SVG |
| **SVG Path Editor** | yqnn.github.io/svg-path-editor | Edit SVG paths |

---

## 📱 Favicon Setup

```html
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/manifest.webmanifest">
```

### Recommended Favicon Sizes
- 16×16 px — Browser tab
- 32×32 px — Taskbar shortcuts
- 180×180 px — Apple touch icon
- 192×192 px — Android
- 512×512 px — PWA splash screen
