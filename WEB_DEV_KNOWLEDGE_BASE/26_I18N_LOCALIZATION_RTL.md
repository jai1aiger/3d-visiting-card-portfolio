# 🌍 26 — Internationalization (i18n), Localization & RTL
> **Use this file when**: Translating websites, handling multi-currency/dates, or building right-to-left (Arabic/Hebrew) UIs.

---

## 🌐 Top i18n Libraries

| Framework | Library | Install | GitHub Stars |
|-----------|---------|---------|--------------|
| **Next.js (App Router)** | `next-intl` | `npm i next-intl` | ⭐ 5k+ |
| **React** | `react-i18next` | `npm i react-i18next i18next` | ⭐ 9k+ |
| **Vue 3** | `vue-i18n` | `npm i vue-i18n@9` | ⭐ 4k+ |
| **Lightweight** | `typesafe-i18n` | `npm i typesafe-i18n` | ⭐ 2k+ |
| **FormatJS / Intl** | `@formatjs/intl` | `npm i @formatjs/intl` | ⭐ 14k+ |

---

## ⚡ Next.js App Router i18n with `next-intl`

### Folder Structure
```
app/
└── [locale]/
    ├── layout.tsx
    ├── page.tsx
    └── about/
        └── page.tsx
messages/
├── en.json
├── fr.json
└── ar.json (RTL)
```

### RTL (Right-to-Left) Support with Tailwind CSS
```html
<html lang="ar" dir="rtl">
```

Tailwind has native logical properties and RTL support:
- Use `ps-4` (padding-inline-start) instead of `pl-4`
- Use `pe-4` (padding-inline-end) instead of `pr-4`
- Use `ms-auto` instead of `ml-auto`
- Use `start-0` / `end-0` instead of `left-0` / `right-0`
- Conditional RTL styling: `rtl:rotate-180`, `ltr:text-left rtl:text-right`

### Number, Currency & Date Formatting (Native Web API)
```typescript
// Currency
new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(1249.99) // "$1,249.99"
new Intl.NumberFormat('de-DE', { style: 'currency', currency: 'EUR' }).format(1249.99) // "1.249,99 €"

// Dates
new Intl.DateTimeFormat('en-US', { dateStyle: 'full' }).format(new Date())
new Intl.RelativeTimeFormat('en', { numeric: 'auto' }).format(-1, 'day') // "yesterday"
```
