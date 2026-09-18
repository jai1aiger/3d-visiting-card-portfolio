# ♿ 15 — Accessibility (A11y)
> **Use this file when**: Ensuring your website is accessible to all users. WCAG compliance is required in many regions.

---

## 🎯 WCAG 2.2 Compliance Levels

| Level | Requirement | Criteria |
|-------|-------------|---------|
| **A** | Minimum | 30 criteria — basic access |
| **AA** | Standard (legal in most countries) | 50 criteria — most users |
| **AAA** | Enhanced | 78 criteria — most accessible |

> Most websites should target **WCAG 2.2 AA**

---

## 🎨 Color Contrast Requirements

| Text Size | AA Ratio | AAA Ratio |
|-----------|---------|----------|
| Normal text (< 18pt) | **4.5:1** | 7:1 |
| Large text (≥ 18pt or 14pt bold) | **3:1** | 4.5:1 |
| UI components & graphics | **3:1** | — |

### Contrast Check Tools
```bash
# Check in CSS
# Use WebAIM contrast checker: https://webaim.org/resources/contrastchecker/
```

Approved Tailwind color combos:
- `bg-white text-gray-900` ✅ (21:1)
- `bg-blue-600 text-white` ✅ (4.6:1)
- `bg-yellow-400 text-black` ✅ (10.7:1)
- `bg-gray-100 text-gray-400` ❌ (2.9:1 — fail!)

---

## 📝 Semantic HTML

```html
<!-- WRONG: divs only -->
<div class="header">
  <div class="logo">Brand</div>
  <div class="nav">
    <div>Home</div>
    <div>About</div>
  </div>
</div>
<div class="content">
  <div class="article">
    <div class="heading">Title</div>
    <div>Content...</div>
  </div>
</div>
<div class="footer">Footer</div>

<!-- RIGHT: semantic HTML -->
<header>
  <a href="/" aria-label="Brand homepage">Brand</a>
  <nav aria-label="Main navigation">
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/about">About</a></li>
    </ul>
  </nav>
</header>
<main>
  <article>
    <h1>Title</h1>
    <p>Content...</p>
  </article>
</main>
<footer>Footer content</footer>
```

---

## ⌨️ Keyboard Navigation

```css
/* NEVER remove focus visible styles */
:focus-visible {
  outline: 3px solid #3b82f6;
  outline-offset: 2px;
  border-radius: 4px;
}

/* Custom focus style */
.btn:focus-visible {
  box-shadow: 0 0 0 3px rgb(59 130 246 / 0.5);
  outline: none;
}
```

### Keyboard Trap for Modals
```typescript
// Use Radix UI Dialog — keyboard trap built-in
import * as Dialog from '@radix-ui/react-dialog'

// Or focus-trap-react
import FocusTrap from 'focus-trap-react'
<FocusTrap active={isOpen}>
  <div role="dialog" aria-modal="true">...</div>
</FocusTrap>
```

---

## 🏷️ ARIA Attributes

```html
<!-- Buttons -->
<button aria-label="Close dialog">
  <XIcon aria-hidden="true" />
</button>

<!-- Loading states -->
<button aria-busy="true" aria-live="polite">
  <Spinner aria-hidden="true" />
  <span>Saving...</span>
</button>

<!-- Error messages -->
<input
  id="email"
  type="email"
  aria-describedby="email-error"
  aria-invalid="true"
/>
<p id="email-error" role="alert">Please enter a valid email address</p>

<!-- Expandable sections -->
<button aria-expanded={isOpen} aria-controls="panel-content">
  Toggle section
</button>
<div id="panel-content" hidden={!isOpen}>Content</div>

<!-- Navigation landmarks -->
<nav aria-label="Main">
<nav aria-label="Breadcrumb">
<nav aria-label="Pagination">

<!-- Live regions -->
<div role="status" aria-live="polite">Items loaded: {count}</div>
<div role="alert" aria-live="assertive">Error: {error}</div>
```

---

## 🖼️ Images & Media Accessibility

```html
<!-- Informative image -->
<img src="chart.png" alt="Sales increased 40% from Q1 to Q2 2024">

<!-- Decorative image -->
<img src="decoration.svg" alt="" role="presentation">

<!-- Complex image -->
<figure>
  <img src="complex-chart.png" alt="Complex chart - see description below" 
       aria-describedby="chart-desc">
  <figcaption id="chart-desc">
    Detailed description of the chart data...
  </figcaption>
</figure>

<!-- Video -->
<video controls>
  <source src="video.mp4" type="video/mp4">
  <track kind="captions" src="captions.vtt" srclang="en" label="English" default>
  Your browser doesn't support video.
</video>
```

---

## 🛠️ Accessibility Testing Tools

### Automated Tools
| Tool | Type | Install/URL |
|------|------|------------|
| **axe DevTools** | Browser extension | Chrome/Firefox extension |
| **WAVE** | Browser extension | wave.webaim.org |
| **Lighthouse** | Built-in Chrome | DevTools → Lighthouse |
| **jest-axe** | Unit testing | `npm i -D jest-axe axe-core` |
| **@testing-library/jest-dom** | Unit testing | includes a11y matchers |
| **eslint-plugin-jsx-a11y** | Linting | `npm i -D eslint-plugin-jsx-a11y` |
| **Storybook a11y addon** | Dev | `npx storybook add @storybook/addon-a11y` |

### jest-axe Example
```typescript
import { axe, toHaveNoViolations } from 'jest-axe'
expect.extend(toHaveNoViolations)

test('has no accessibility violations', async () => {
  const { container } = render(<Button>Click me</Button>)
  const results = await axe(container)
  expect(results).toHaveNoViolations()
})
```

### eslint-plugin-jsx-a11y Rules
```json
{
  "plugins": ["jsx-a11y"],
  "rules": {
    "jsx-a11y/alt-text": "error",
    "jsx-a11y/anchor-is-valid": "error",
    "jsx-a11y/click-events-have-key-events": "error",
    "jsx-a11y/no-noninteractive-element-interactions": "error",
    "jsx-a11y/label-has-associated-control": "error"
  }
}
```

---

## 📋 Accessibility Checklist

### Perceivable
- [ ] All images have alt text (or `alt=""` for decorative)
- [ ] Color is not the only way to convey info
- [ ] Text contrast ≥ 4.5:1 (normal), 3:1 (large)
- [ ] Videos have captions
- [ ] Content can be resized to 200% without loss

### Operable
- [ ] All functionality works with keyboard alone
- [ ] No keyboard traps (unless intentional like modal)
- [ ] Skip navigation link at top of page
- [ ] Proper focus management on modals/dialogs
- [ ] No content flashes more than 3 times/second

### Understandable
- [ ] `lang` attribute set on `<html>`
- [ ] Form inputs have associated labels
- [ ] Error messages are descriptive
- [ ] Clear and consistent navigation

### Robust
- [ ] Valid HTML (use W3C validator)
- [ ] ARIA used correctly
- [ ] Components have semantic roles
- [ ] All interactive elements have accessible names
