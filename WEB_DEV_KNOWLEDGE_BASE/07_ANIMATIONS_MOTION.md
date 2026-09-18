# ✨ 07 — Animations & Motion Design
> **Use this file when**: Adding animations, transitions, scroll effects, or micro-interactions to a website.

---

## 🎬 Animation Library Comparison

| Library | Size | Learning | Best For | GitHub Stars |
|---------|------|----------|---------|-------------|
| **Framer Motion** | ~100KB | Low | React animations, gestures | ⭐ 25k+ |
| **GSAP** | ~60KB | Medium | Complex timelines, scroll, SVG | ⭐ 20k+ |
| **Anime.js** | ~17KB | Low | SVG, DOM, CSS animations | ⭐ 50k+ |
| **Motion One** | ~18KB | Low | Lightweight WAAPI-based | ⭐ 5k+ |
| **Auto Animate** | ~3KB | Very Low | Auto layout transitions | ⭐ 13k+ |
| **AOS** | ~13KB | Very Low | Scroll-triggered animations | ⭐ 26k+ |
| **Lottie** | ~50KB | Very Low | JSON-based vector animations | ⭐ 31k+ |
| **React Spring** | ~30KB | Medium | Physics-based spring animations | ⭐ 28k+ |
| **Three.js** | ~600KB | High | 3D canvas animations | ⭐ 102k+ |
| **Rive** | ~40KB | Medium | Interactive state machines | Growing |
| **CSS Animations** | 0KB | Low | Simple, performant transitions | Built-in |

---

## 🎯 Framer Motion (React)

GitHub: https://github.com/framer/motion ⭐ 25k+
```bash
npm i framer-motion
```

### Basic Animations
```jsx
import { motion, AnimatePresence } from 'framer-motion'

// Fade in on mount
<motion.div
  initial={{ opacity: 0, y: 20 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.5, ease: 'easeOut' }}
>
  Content
</motion.div>

// Hover & tap gestures
<motion.button
  whileHover={{ scale: 1.05 }}
  whileTap={{ scale: 0.95 }}
  transition={{ type: 'spring', stiffness: 400, damping: 17 }}
>
  Click me
</motion.button>

// Page transitions
<AnimatePresence mode="wait">
  <motion.div
    key={router.pathname}
    initial={{ opacity: 0, x: 20 }}
    animate={{ opacity: 1, x: 0 }}
    exit={{ opacity: 0, x: -20 }}
    transition={{ duration: 0.3 }}
  />
</AnimatePresence>
```

### Scroll Animations
```jsx
import { motion, useScroll, useTransform } from 'framer-motion'

// Parallax
const { scrollY } = useScroll()
const y = useTransform(scrollY, [0, 500], [0, 150])
<motion.div style={{ y }}>Parallax element</motion.div>

// Scroll-triggered reveal
import { useInView } from 'framer-motion'
const ref = useRef(null)
const isInView = useInView(ref, { once: true })

<motion.div
  ref={ref}
  animate={{ opacity: isInView ? 1 : 0, y: isInView ? 0 : 50 }}
  transition={{ duration: 0.6 }}
/>
```

### Stagger Children
```jsx
const container = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: { staggerChildren: 0.1 }
  }
}

const item = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0 }
}

<motion.ul variants={container} initial="hidden" animate="show">
  {items.map(i => (
    <motion.li key={i} variants={item}>{i}</motion.li>
  ))}
</motion.ul>
```

---

## 🎪 GSAP (Professional Grade)

GitHub: https://github.com/greensock/GSAP ⭐ 20k+
```bash
npm i gsap
```

### GSAP Basics
```javascript
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import { TextPlugin } from 'gsap/TextPlugin'

gsap.registerPlugin(ScrollTrigger, TextPlugin)

// Basic tween
gsap.to('.element', { 
  x: 100, opacity: 1, duration: 1, 
  ease: 'power2.out' 
})

// Timeline
const tl = gsap.timeline({ defaults: { ease: 'power2.out' } })
tl.from('.hero-title', { y: 100, opacity: 0, duration: 0.8 })
  .from('.hero-subtitle', { y: 50, opacity: 0, duration: 0.6 }, '-=0.4')
  .from('.hero-cta', { y: 30, opacity: 0, duration: 0.4 }, '-=0.3')

// ScrollTrigger
gsap.from('.card', {
  scrollTrigger: {
    trigger: '.card',
    start: 'top 80%',
    end: 'bottom 20%',
    toggleActions: 'play none none reverse'
  },
  y: 50, opacity: 0, stagger: 0.2
})
```

---

## 🍃 Auto Animate (Simplest Approach)

GitHub: https://github.com/formkit/auto-animate ⭐ 13k+
```bash
npm i @formkit/auto-animate
```
```jsx
import { useAutoAnimate } from '@formkit/auto-animate/react'

const [parent] = useAutoAnimate()
// Any add/remove/move within [parent] is animated automatically!
<ul ref={parent}>
  {items.map(item => <li key={item.id}>{item.text}</li>)}
</ul>
```

---

## 📜 AOS — Animate on Scroll

GitHub: https://github.com/michalsnik/aos ⭐ 26k+
```bash
npm i aos
```
```html
<!-- HTML attributes -->
<div data-aos="fade-up" data-aos-delay="100" data-aos-duration="800">
<div data-aos="slide-left" data-aos-once="true">
<div data-aos="zoom-in" data-aos-easing="ease-in-out">
```
```javascript
import AOS from 'aos'
import 'aos/dist/aos.css'
AOS.init({ duration: 800, once: true })
```

---

## 🌊 CSS-Only Animations (No JS!)

### Skeleton Loading
```css
.skeleton {
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
  border-radius: 4px;
}

@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}
```

### Infinite Marquee (CSS)
```css
.marquee-track {
  display: flex;
  gap: 2rem;
  animation: marquee 20s linear infinite;
}

@keyframes marquee {
  from { transform: translateX(0); }
  to { transform: translateX(-50%); }
}
```

### Floating Animation
```css
@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-20px); }
}
.float { animation: float 3s ease-in-out infinite; }
```

### Pulse/Ping
```css
@keyframes ping {
  75%, 100% { transform: scale(2); opacity: 0; }
}
.ping { animation: ping 1s cubic-bezier(0, 0, 0.2, 1) infinite; }
```

---

## 🎭 Micro-Interaction Patterns

### Button Hover States
```css
/* Lift effect */
.btn { transition: transform 150ms, box-shadow 150ms; }
.btn:hover { transform: translateY(-2px); box-shadow: 0 10px 25px -5px rgb(0 0 0 / 0.15); }

/* Fill effect */
.btn { background: white; color: blue; border: 2px solid blue; transition: all 200ms; }
.btn:hover { background: blue; color: white; }

/* Arrow slide */
.btn .arrow { transition: transform 200ms; }
.btn:hover .arrow { transform: translateX(4px); }
```

---

## 🔗 Animation Resources

| Resource | URL | Type |
|----------|-----|------|
| Cubic Bezier | cubic-bezier.com | Easing visualizer |
| Easing Functions | easings.net | Cheat sheet |
| CSS Animation | animate.style | Animate.css demo |
| Animista | animista.net | CSS animation generator |
| Transition.style | transition.style | Copy CSS transitions |
| GSAP Ease Visualizer | gsap.com/docs/v3/Eases | GSAP easing |
