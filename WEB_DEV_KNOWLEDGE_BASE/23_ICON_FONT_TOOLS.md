# 🎭 23 — Icons, Fonts & Visual Assets (Complete Index)
> Source: bradtraversy/design-resources-for-developers, GitHub awesome lists

---

## 🔷 Icon Libraries — Complete Reference

### SVG Icon Libraries

| Library | Stars | Count | Style | License | Install |
|---------|-------|-------|-------|---------|---------|
| **Lucide** | ⭐ 15k+ | 1,500+ | Stroke | ISC | `npm i lucide-react` |
| **Heroicons** | ⭐ 22k+ | 300+ | Stroke/Solid | MIT | `npm i @heroicons/react` |
| **Phosphor** | ⭐ 5k+ | 9,000+ | 6 weights | MIT | `npm i @phosphor-icons/react` |
| **Tabler** | ⭐ 18k+ | 5,700+ | Stroke | MIT | `npm i @tabler/icons-react` |
| **Iconify** | ⭐ 4k+ | 200,000+ | All | Various | `npm i @iconify/react` |
| **React Icons** | ⭐ 12k+ | 60,000+ | Mixed | Various | `npm i react-icons` |
| **Bootstrap Icons** | ⭐ 7k+ | 2,000+ | Stroke/Fill | MIT | `npm i bootstrap-icons` |
| **Radix Icons** | ⭐ 3k+ | 318 | Balanced | MIT | `npm i @radix-ui/react-icons` |
| **Feather** | ⭐ 24k+ | 286 | Stroke | MIT | `npm i feather-icons` |
| **Remix Icons** | ⭐ 6k+ | 2,800+ | Balanced | Apache | `npm i remixicon` |
| **Font Awesome** | ⭐ 73k+ | 2,000+ free | Mixed | CC+MIT | CDN or `npm i @fortawesome/fontawesome-free` |
| **Material Icons** | ⭐ 5k+ | 2,500+ | 5 styles | Apache | `npm i @mui/icons-material` |
| **Simple Icons** | ⭐ 20k+ | 3,000+ | Brand logos | CC0 | `npm i simple-icons` |
| **Ionicons** | ⭐ 17k+ | 1,300+ | Stroke/Fill | MIT | via React Icons `io5` |
| **Carbon** | IBM-made | 2,100+ | IBM Design | Apache | `npm i @carbon/icons-react` |

---

## Icon Usage Code Examples

### Lucide (Recommended)
```jsx
import { Search, Heart, Star, Home, Settings, User, Bell, X } from 'lucide-react'

// Size and color
<Search size={20} color="currentColor" strokeWidth={1.5} />

// With Tailwind
<Heart className="w-5 h-5 text-red-500" />
<Bell className="w-6 h-6 text-gray-600 hover:text-gray-900 cursor-pointer" />
```

### Heroicons
```jsx
import { MagnifyingGlassIcon, HeartIcon } from '@heroicons/react/24/outline'  // Stroke
import { HeartIcon as HeartSolid } from '@heroicons/react/24/solid'            // Filled
import { HeartIcon as HeartMini } from '@heroicons/react/20/solid'             // 20px

<MagnifyingGlassIcon className="h-6 w-6" />
```

### React Icons (Meta-library)
```jsx
import { FaGithub, FaTwitter, FaLinkedin } from 'react-icons/fa'   // Font Awesome
import { FaXTwitter } from 'react-icons/fa6'                        // FA6 (X/Twitter)
import { SiReact, SiNextdotjs, SiTailwindcss } from 'react-icons/si'  // Tech logos
import { IoLogoVercel } from 'react-icons/io5'                      // Ionicons 5
import { MdEmail, MdPhone } from 'react-icons/md'                   // Material
import { AiOutlineMail } from 'react-icons/ai'                      // Ant Design
import { BiHome } from 'react-icons/bi'                             // Boxicons

// All with same API
<FaGithub className="w-5 h-5" />
<SiReact color="#61DAFB" size={24} />
```

### Iconify (Access any icon set)
```jsx
import { Icon } from '@iconify/react'

// Format: "collection:icon-name"
<Icon icon="mdi:github" width="24" height="24" />
<Icon icon="logos:react" />                        // Colored brand logos
<Icon icon="twemoji:flag-india" />                // Emoji flags
<Icon icon="game-icons:dragon" />                  // Game icons
<Icon icon="noto:sparkles" />                     // Noto emoji
```

---

## 🎨 Illustration Libraries

### Free Illustration Packs
| Library | URL | Style | License |
|---------|-----|-------|---------|
| **unDraw** | https://undraw.co/ | Flat, SVG, customizable color | MIT |
| **Storyset** | https://storyset.com/ | Multiple styles, animate-able | Free with attribution |
| **Illustrations.co** | https://illlustrations.co/ | 3D isometric | Free |
| **DrawKit** | https://www.drawkit.com/ | Various, professional | Free + premium |
| **Blush** | https://blush.design/ | Diverse people, customizable | Freemium |
| **Humaaans** | https://www.humaaans.com/ | Mix-and-match people | CC-BY |
| **Open Doodles** | https://www.opendoodles.com/ | Hand-drawn, relaxed | CC0 |
| **Popsy** | https://popsy.co/ | Notion-style illustrations | Free |
| **Control.rocks** | https://control.rocks/ | Abstract people | Free |
| **Abstrakt** | https://abstrakt.design/ | Abstract/geometric | Free |
| **Skribbl** | https://weareskribbl.com/ | Rough sketch style | Free with attribution |
| **Woobro** | https://woobro.design/ | Clean, modern | Free |
| **Delesign** | https://delesign.com/free-designs/graphics/ | Various | Free |

### Paid Illustration Services
| Service | Price | Notes |
|---------|-------|-------|
| **Icons8 Illustrations** | ~$13/mo | 3D, flat, cartoon styles |
| **Envato Elements** | ~$16/mo | All creative assets |
| **Streamline** | Freemium | 80,000+ illustrations |
| **Craftwork** | Per pack | Premium design resources |

---

## 🔤 Font Resources — Complete List

### Free Font Platforms
| Platform | URL | Count | Notes |
|----------|-----|-------|-------|
| **Google Fonts** | https://fonts.google.com/ | 1,500+ | Most popular, free |
| **Fontsource** | https://fontsource.org/ | 1,500+ | Self-host Google Fonts |
| **Fontshare** | https://www.fontshare.com/ | 100+ | High-quality free fonts |
| **Bunny Fonts** | https://fonts.bunny.net/ | 1,500+ | GDPR-compliant CDN |
| **DaFont** | https://www.dafont.com/ | 60,000+ | Mostly display/decorative |
| **Font Squirrel** | https://www.fontsquirrel.com/ | 5,000+ | Commercial-use free |
| **1001 Fonts** | https://www.1001fonts.com/ | 15,000+ | Mixed licenses |
| **Befonts** | https://befonts.com/ | — | Curated quality free fonts |

### Premium Font Services
| Service | URL | Notes |
|---------|-----|-------|
| **Adobe Fonts** | https://fonts.adobe.com/ | Included with CC subscription |
| **Fonts.com** | https://www.fonts.com/ | Professional library |
| **Lineto** | https://lineto.com/ | Swiss premium fonts |
| **TypeType** | https://typetype.org/ | Modern premium typefaces |
| **Grilli Type** | https://www.grillitype.com/ | Swiss quality fonts |

---

## Font Tools

| Tool | URL | Purpose |
|------|-----|---------|
| **Wakamai Fondue** | https://wakamaifondue.com/ | Inspect variable font axes |
| **Fonts Ninja** | https://www.fonts.ninja/ | Chrome extension — identify fonts |
| **FontDrop** | https://fontdrop.info/ | Analyze font files |
| **V-Fonts** | https://v-fonts.com/ | Variable font explorer |
| **Google Fonts Pairings** | fonts.google.com/pairings | Official pairing suggestions |
| **Fontjoy** | https://fontjoy.com/ | AI font pairing generator |
| **FontPair** | https://fontpair.co/ | Curated Google Fonts pairings |
| **Typescale** | https://typescale.com/ | Visual type scale generator |
| **Modular Scale** | https://www.modularscale.com/ | Mathematical type scale |
| **Type Scale** | https://type-scale.com/ | Interactive scale builder |
| **Word-O-Mat** | — | Font testing tool |

---

## 🖼️ Free Photography & Media

| Source | URL | License |
|--------|-----|---------|
| **Unsplash** | https://unsplash.com/ | Free commercial use |
| **Pexels** | https://www.pexels.com/ | Free commercial use |
| **Pixabay** | https://pixabay.com/ | Free commercial use |
| **Freepik** | https://www.freepik.com/ | Free with attribution (or paid) |
| **StockSnap** | https://stocksnap.io/ | CC0 |
| **Burst (Shopify)** | https://burst.shopify.com/ | Free commercial |
| **Picography** | https://picography.co/ | Free |
| **Gratisography** | https://gratisography.com/ | Free, quirky |
| **SplitShire** | https://www.splitshire.com/ | Free commercial |
| **Life of Pix** | https://www.lifeofpix.com/ | Free |

---

## 🎬 Free Video Resources

| Source | URL | Type |
|--------|-----|------|
| **Pexels Videos** | https://www.pexels.com/videos/ | Free stock video |
| **Pixabay Videos** | https://pixabay.com/videos/ | Free stock video |
| **Videvo** | https://www.videvo.net/ | Stock video + motion graphics |
| **Mixkit** | https://mixkit.co/ | Free video, music, templates |
| **Coverr** | https://coverr.co/ | Free website background videos |

---

## 🎨 Background Pattern & Texture Generators

| Tool | URL | Output |
|------|-----|--------|
| **fffuel** | https://www.fffuel.co/ | SVG generators, patterns, textures |
| **Haikei** | https://app.haikei.app/ | Wave, blob, SVG shapes |
| **SVGBackgrounds** | https://www.svgbackgrounds.com/ | CSS SVG patterns |
| **Heropatterns** | https://heropatterns.com/ | Repeating SVG patterns (Tailwind team) |
| **PatternPad** | https://patternpad.com/ | Abstract patterns |
| **Noise & Texture** | https://www.noiseandtexture.com/ | Noise overlays |
| **CSS Background Patterns** | https://www.magicpattern.design/ | CSS + SVG patterns |
| **Glassmorphism Gen** | https://glassgenerator.netlify.app/ | Glassmorphism CSS generator |
| **Neumorphism.io** | https://neumorphism.io/ | Neumorphic shadow generator |
| **CSS Grid Generator** | https://cssgrid-generator.netlify.app/ | Visual grid builder |
| **Clip Path Maker** | https://bennettfeely.com/clippy/ | CSS clip-path generator |
| **CSS Mesh Gradients** | https://meshgradient.com/ | Beautiful mesh gradients |
| **UI Gradients** | https://uigradients.com/ | 200+ gradients |
| **Hypercolor** | https://hypercolor.dev/ | Tailwind gradient collection |
