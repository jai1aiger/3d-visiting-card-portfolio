# 🎬 22 — Animation, Scroll & Motion Libraries (Complete Reference)
> Source: bradtraversy/design-resources-for-developers, GitHub Trending 2025

---

## JavaScript Animation Libraries — Full Index

| Library | Stars | Size | Best For | Install |
|---------|-------|------|---------|---------|
| **GSAP** | ⭐ 20k+ | ~60KB | Professional timelines, SVG, scroll | `npm i gsap` |
| **Framer Motion** | ⭐ 30k+ | ~100KB | React animations, gestures, layout | `npm i framer-motion` |
| **Anime.js** | ⭐ 50k+ | ~17KB | SVG, DOM, multi-step | `npm i animejs` |
| **Motion One** | ⭐ 5k+ | ~3KB | WAAPI, off-main-thread | `npm i motion` |
| **React Spring** | ⭐ 28k+ | ~30KB | Physics-based spring animations | `npm i @react-spring/web` |
| **Auto Animate** | ⭐ 12k+ | ~3KB | Zero-config list transitions | `npm i @formkit/auto-animate` |
| **Lottie** | ⭐ 28k+ | ~50KB | After Effects JSON animations | `npm i lottie-web` |
| **Three.js** | ⭐ 102k+ | — | 3D animations | see 08 |

---

## CSS Animation Libraries

| Library | Stars | Install | Description |
|---------|-------|---------|-------------|
| **Animate.css** | ⭐ 80k+ | `npm i animate.css` | Most popular — just add a class |
| **Hover.css** | ⭐ 29k+ | CDN | CSS hover effects only |
| **AnimXYZ** | ⭐ 3k+ | `npm i @animxyz/core` | Composable CSS animations |
| **Magic Animations** | ⭐ 8k+ | CDN | Impressive effect library |
| **CSShake** | ⭐ 5k+ | CDN | Shake/wiggle effects |
| **Whirl** | ⭐ 4k+ | CDN | CSS loading spinners |
| **Hamburgers** | ⭐ 8k+ | `npm i hamburgers` | CSS hamburger icon animations |

---

## Scroll Animation Libraries

| Library | Stars | Install | Description |
|---------|-------|---------|-------------|
| **AOS** | ⭐ 25k+ | `npm i aos` | Animate on scroll — easiest |
| **ScrollReveal** | ⭐ 21k+ | `npm i scrollreveal` | Scroll animation |
| **Locomotive Scroll** | ⭐ 8k+ | `npm i locomotive-scroll` | Smooth scroll + parallax |
| **Lenis** | ⭐ 8k+ | `npm i @studio-freight/lenis` | Ultra-smooth native scroll feel |
| **GSAP ScrollTrigger** | Part of GSAP | — | Professional scroll animations |
| **Rellax.js** | ⭐ 7k+ | `npm i rellax` | Simple parallax |
| **Splitting.js** | ⭐ 5k+ | `npm i splitting` | Text splitting for reveal effects |

### AOS Usage
```html
<div data-aos="fade-up" data-aos-duration="800" data-aos-delay="100">Content</div>
<div data-aos="slide-left">Content</div>
<div data-aos="zoom-in" data-aos-once="true">Content</div>
```
```js
import AOS from 'aos'
import 'aos/dist/aos.css'
AOS.init({ duration: 800, once: true, easing: 'ease-out-cubic' })
```

### Lenis (Smooth Scroll)
```js
import Lenis from '@studio-freight/lenis'
const lenis = new Lenis({ lerp: 0.1, smoothWheel: true })

function raf(time) {
  lenis.raf(time)
  requestAnimationFrame(raf)
}
requestAnimationFrame(raf)

// With GSAP ScrollTrigger
lenis.on('scroll', ScrollTrigger.update)
gsap.ticker.add((time) => lenis.raf(time * 1000))
```

---

## Background Animation Libraries

| Library | Stars | Install | Effects |
|---------|-------|---------|---------|
| **Vanta.js** | ⭐ 4k+ | `npm i vanta` | WAVES, BIRDS, FOG, GLOBE, NET, RINGS |
| **tsParticles** | ⭐ 8k+ | `npm i tsparticles` | Particles, confetti, fireworks |
| **Particles.js** | ⭐ 28k+ | `npm i particles.js` | Classic particles |
| **Nice Waves** | ⭐ 1k+ | CDN | Animated wave SVG backgrounds |
| **Canvas Confetti** | ⭐ 8k+ | `npm i canvas-confetti` | Confetti bursts |

### Canvas Confetti
```js
import confetti from 'canvas-confetti'
// Trigger on button click
confetti({ particleCount: 100, spread: 70, origin: { y: 0.6 } })
```

---

## GSAP Complete Guide

```js
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import { TextPlugin } from 'gsap/TextPlugin'
import { SplitText } from 'gsap/SplitText'   // Club plugin
import { Flip } from 'gsap/Flip'             // Layout flip
import { Draggable } from 'gsap/Draggable'

gsap.registerPlugin(ScrollTrigger, TextPlugin, Flip, Draggable)

// === BASIC TWEENS ===
gsap.to('.element', { x: 100, opacity: 1, duration: 1, ease: 'power2.out' })
gsap.from('.element', { opacity: 0, y: 50, duration: 0.8 })
gsap.fromTo('.element', { opacity: 0 }, { opacity: 1, duration: 1 })
gsap.set('.element', { opacity: 0 })  // Instant set

// === TIMELINES ===
const tl = gsap.timeline({
  defaults: { ease: 'power2.out', duration: 0.8 },
  delay: 0.3,
  onComplete: () => console.log('Done!')
})

tl.from('.hero-title', { y: 100, opacity: 0 })
  .from('.hero-subtitle', { y: 60, opacity: 0 }, '-=0.5')
  .from('.hero-cta', { y: 30, opacity: 0 }, '-=0.3')
  .from('.hero-image', { scale: 0.8, opacity: 0 }, '-=0.4')

// === SCROLL TRIGGER ===
gsap.from('.card', {
  scrollTrigger: {
    trigger: '.card',
    start: 'top 80%',           // When top of element hits 80% down viewport
    end: 'bottom 20%',
    scrub: 1,                   // Smooth scrub effect
    pin: true,                  // Pin element while scrolling
    markers: false,             // Debug markers
    toggleActions: 'play none none reverse'
  },
  y: 100,
  opacity: 0,
  stagger: 0.15
})

// === GSAP EASES ===
// Power: none, power1, power2, power3, power4
// Direction: .in, .out, .inOut
// Special: elastic, bounce, back, circ, expo, sine

// === STAGGER ===
gsap.from('.item', {
  opacity: 0,
  y: 20,
  stagger: {
    amount: 0.8,        // Total stagger time
    from: 'start',      // 'start', 'end', 'center', 'random', or index
    grid: 'auto',       // For grid layouts
    ease: 'power1.in'
  }
})
```

---

## Framer Motion Advanced Patterns

```jsx
import { motion, AnimatePresence, useScroll, useTransform, useInView } from 'framer-motion'

// === LAYOUT ANIMATIONS (magic motion) ===
<motion.div layout>
  {/* Automatically animates size/position changes */}
</motion.div>

// === SHARED LAYOUT ANIMATIONS ===
<AnimatePresence>
  {isOpen && (
    <motion.div
      layoutId="modal-card"
      className="modal"
      initial={{ borderRadius: 12 }}
    >
      Content
    </motion.div>
  )}
</AnimatePresence>

// === DRAG ===
<motion.div
  drag="x"
  dragConstraints={{ left: -100, right: 100 }}
  dragElastic={0.2}
  whileDrag={{ scale: 1.1 }}
>
  Drag me
</motion.div>

// === SCROLL-LINKED ===
function ParallaxHero() {
  const { scrollY } = useScroll()
  const y = useTransform(scrollY, [0, 500], [0, 200])
  const opacity = useTransform(scrollY, [0, 300], [1, 0])
  
  return <motion.div style={{ y, opacity }}>Hero</motion.div>
}

// === VIEW-TRIGGERED ===
function Card() {
  const ref = useRef(null)
  const isInView = useInView(ref, { once: true, margin: '-100px' })
  
  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, y: 50 }}
      animate={isInView ? { opacity: 1, y: 0 } : {}}
      transition={{ duration: 0.6, ease: 'easeOut' }}
    />
  )
}
```

---

## CSS-Only Animation Reference

```css
/* === ALL ESSENTIAL KEYFRAMES === */

/* Fade In */
@keyframes fadeIn { from { opacity: 0 } to { opacity: 1 } }

/* Slide Up */
@keyframes slideUp { from { opacity: 0; transform: translateY(20px) } to { opacity: 1; transform: translateY(0) } }

/* Scale In */
@keyframes scaleIn { from { opacity: 0; transform: scale(0.9) } to { opacity: 1; transform: scale(1) } }

/* Bounce */
@keyframes bounce { 0%, 100% { transform: translateY(0) } 50% { transform: translateY(-10px) } }

/* Float */
@keyframes float { 0%, 100% { transform: translateY(0) } 50% { transform: translateY(-15px) } }

/* Pulse */
@keyframes pulse { 0%, 100% { opacity: 1 } 50% { opacity: 0.5 } }

/* Spin */
@keyframes spin { from { transform: rotate(0deg) } to { transform: rotate(360deg) } }

/* Shimmer (skeleton) */
@keyframes shimmer {
  0% { background-position: -200% 0 }
  100% { background-position: 200% 0 }
}

/* Marquee */
@keyframes marquee { from { transform: translateX(0) } to { transform: translateX(-50%) } }

/* Ping */
@keyframes ping { 75%, 100% { transform: scale(2); opacity: 0 } }

/* Gradient shift */
@keyframes gradientShift {
  0% { background-position: 0% 50% }
  50% { background-position: 100% 50% }
  100% { background-position: 0% 50% }
}

/* Typewriter */
@keyframes typewriter { from { width: 0 } to { width: 100% } }
@keyframes blink { 0%, 100% { border-color: transparent } 50% { border-color: currentColor } }

/* Gradient text animation */
.animated-gradient-text {
  background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
  background-size: 400% 400%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gradientShift 8s ease infinite;
}
```

---

## Lottie Animations (JSON-based)

```bash
npm i lottie-react
# or lightweight: npm i @dotlottie/react-player
```

```jsx
import Lottie from 'lottie-react'

function SuccessAnimation() {
  const options = {
    animationData: animationData,  // JSON imported
    loop: false,
    autoplay: true,
    style: { width: 200, height: 200 }
  }
  return <Lottie {...options} />
}
```

### Free Lottie Resources
- **LottieFiles**: https://lottiefiles.com/ — Largest free collection
- **IconScout**: https://iconscout.com/lotties
- **LordIcon**: https://lordicon.com/ — 3,500+ animated icons
- **UseAnimations**: https://useanimations.com/
