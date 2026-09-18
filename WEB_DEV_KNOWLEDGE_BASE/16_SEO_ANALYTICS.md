# 📈 16 — SEO & Analytics
> **Use this file when**: Optimizing for search engines, setting up analytics, or improving discoverability.

---

## 🔍 SEO Fundamentals

### HTML Meta Tags
```html
<head>
  <!-- Basic SEO -->
  <title>Page Title — Brand Name (50-60 chars)</title>
  <meta name="description" content="Compelling description 120-160 chars that explains page value">
  <link rel="canonical" href="https://example.com/page">
  
  <!-- Open Graph (Social Sharing) -->
  <meta property="og:title" content="Page Title">
  <meta property="og:description" content="Description for social shares">
  <meta property="og:image" content="https://example.com/og-image.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:url" content="https://example.com/page">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Brand Name">
  
  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="@brandhandle">
  <meta name="twitter:title" content="Page Title">
  <meta name="twitter:description" content="Description">
  <meta name="twitter:image" content="https://example.com/twitter-image.jpg">
  
  <!-- Additional -->
  <meta name="robots" content="index, follow">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#3b82f6">
  <link rel="icon" href="/favicon.ico">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
</head>
```

---

## 📊 Next.js Metadata API

```typescript
// app/layout.tsx — Base metadata
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: {
    default: 'My App',
    template: '%s | My App'   // Each page: "Page Title | My App"
  },
  description: 'My app description',
  keywords: ['keyword1', 'keyword2'],
  authors: [{ name: 'Author Name' }],
  creator: 'Brand Name',
  metadataBase: new URL('https://myapp.com'),
  openGraph: {
    title: 'My App',
    description: 'Description',
    url: 'https://myapp.com',
    siteName: 'My App',
    images: [{
      url: '/og-image.jpg',
      width: 1200,
      height: 630,
      alt: 'My App',
    }],
    locale: 'en_US',
    type: 'website',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'My App',
    description: 'Description',
    creator: '@handle',
    images: ['/twitter-image.jpg'],
  },
  robots: {
    index: true,
    follow: true,
    googleBot: { index: true, follow: true, 'max-image-preview': 'large' }
  }
}

// app/blog/[slug]/page.tsx — Dynamic metadata
export async function generateMetadata({ params }): Promise<Metadata> {
  const post = await getPost(params.slug)
  return {
    title: post.title,
    description: post.excerpt,
    openGraph: { images: [{ url: post.coverImage }] }
  }
}
```

---

## 🗺️ Sitemap & Robots.txt

### Next.js Sitemap (app/sitemap.ts)
```typescript
import { MetadataRoute } from 'next'

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const posts = await getPosts()
  
  return [
    { url: 'https://myapp.com', lastModified: new Date(), changeFrequency: 'daily', priority: 1 },
    { url: 'https://myapp.com/about', lastModified: new Date(), changeFrequency: 'monthly', priority: 0.8 },
    ...posts.map(post => ({
      url: `https://myapp.com/blog/${post.slug}`,
      lastModified: post.updatedAt,
      changeFrequency: 'weekly' as const,
      priority: 0.7
    }))
  ]
}
```

### robots.txt (app/robots.ts)
```typescript
import { MetadataRoute } from 'next'

export default function robots(): MetadataRoute.Robots {
  return {
    rules: [
      { userAgent: '*', allow: '/', disallow: ['/private/', '/admin/'] }
    ],
    sitemap: 'https://myapp.com/sitemap.xml'
  }
}
```

---

## 📋 Structured Data (JSON-LD)

```typescript
// Organization
const jsonLd = {
  '@context': 'https://schema.org',
  '@type': 'Organization',
  name: 'Company Name',
  url: 'https://company.com',
  logo: 'https://company.com/logo.png',
  contactPoint: {
    '@type': 'ContactPoint',
    telephone: '+1-555-000-0000',
    contactType: 'Customer Service'
  }
}

// Article
const articleSchema = {
  '@context': 'https://schema.org',
  '@type': 'Article',
  headline: post.title,
  description: post.excerpt,
  image: post.coverImage,
  author: { '@type': 'Person', name: post.author },
  datePublished: post.publishedAt,
  dateModified: post.updatedAt,
}

// In Next.js
<script type="application/ld+json" 
        dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />
```

---

## 📊 Analytics Platforms

| Platform | Type | Cost | Best For |
|----------|------|------|---------|
| **Google Analytics 4** | SaaS | Free | Most comprehensive |
| **Plausible** | SaaS/OSS | Paid | Privacy-first, GDPR |
| **Fathom** | SaaS | Paid | Simple, privacy-first |
| **PostHog** | OSS | Free tier | Full analytics + events |
| **Umami** | OSS | Free/Self-host | Lightweight, GDPR |
| **Matomo** | OSS | Free/SaaS | Full-featured, self-host |
| **Mixpanel** | SaaS | Free tier | Product analytics |
| **Amplitude** | SaaS | Free tier | Product analytics |
| **Heap** | SaaS | Paid | Auto event capture |

### Google Analytics 4 Setup
```html
<!-- In <head> -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXX');
</script>
```

```bash
# Next.js with next/script
npm i @next/third-parties
```
```typescript
import { GoogleAnalytics } from '@next/third-parties/google'
<GoogleAnalytics gaId="G-XXXXXXXX" />
```

### Plausible (Privacy-First)
```typescript
import { usePlausible } from 'next-plausible'
const plausible = usePlausible()

// Track custom events
plausible('Purchase', { props: { plan: 'pro', amount: 49 } })
plausible('Signup', { props: { method: 'google' } })
```

---

## 🔍 SEO Tools & Resources

| Tool | URL | Purpose |
|------|-----|---------|
| **Google Search Console** | search.google.com/search-console | Index status, queries |
| **Google PageSpeed** | pagespeed.web.dev | CWV, performance |
| **Ahrefs Webmaster** | ahrefs.com/webmaster-tools | Backlinks, SEO audit |
| **Semrush** | semrush.com | Keywords, competitor |
| **Screaming Frog** | screamingfrog.co.uk | Site crawl/audit |
| **Schema Markup Validator** | validator.schema.org | Validate JSON-LD |
| **Rich Results Test** | search.google.com/test/rich-results | Test structured data |
| **Open Graph Debugger** | developers.facebook.com/tools/debug | Test OG tags |
| **Twitter Card Validator** | cards-dev.twitter.com/validator | Test Twitter cards |

---

## 📋 SEO Checklist

### Technical SEO
- [ ] HTTPS enabled
- [ ] Mobile-friendly (Google mobile-first indexing)
- [ ] Page speed: LCP < 2.5s, CLS < 0.1
- [ ] Sitemap.xml submitted to Google Search Console
- [ ] robots.txt configured correctly
- [ ] No broken links (404s)
- [ ] Canonical URLs set
- [ ] Structured data (JSON-LD) for main content types

### On-Page SEO
- [ ] Title tags: 50-60 characters, unique per page
- [ ] Meta descriptions: 120-160 characters, compelling
- [ ] One H1 per page
- [ ] Heading hierarchy (H1 → H2 → H3)
- [ ] Alt text on all images
- [ ] Internal linking strategy
- [ ] Keyword in URL slug (lowercase, hyphens)
- [ ] Open Graph and Twitter Card images (1200×630px)
