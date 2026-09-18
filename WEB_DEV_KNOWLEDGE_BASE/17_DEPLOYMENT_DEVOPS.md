# 🚀 17 — Deployment & DevOps
> **Use this file when**: Deploying a website, setting up CI/CD, or configuring hosting infrastructure.

---

## 🌍 Hosting Platform Comparison

| Platform | Type | Free Tier | Best For |
|----------|------|-----------|---------|
| **Vercel** | Serverless | Generous | Next.js, React, static |
| **Netlify** | Serverless | 100GB/mo | JAMstack, forms, functions |
| **Cloudflare Pages** | Edge | Unlimited | Global edge performance |
| **Railway** | Container | ~$5/mo credit | Full-stack, databases |
| **Render** | Container | Limited | Node.js, web services |
| **Fly.io** | Container | 3 VMs free | Global distributed apps |
| **AWS Amplify** | Serverless | 12 months | AWS ecosystem |
| **Google Cloud Run** | Container | 180k req/month | Containerized apps |
| **DigitalOcean** | VPS | No | Full control, affordable |
| **Hetzner** | VPS | No | Cheapest quality VPS |
| **GitHub Pages** | Static | Unlimited | Documentation, static sites |

---

## ▲ Vercel (Recommended for Next.js)

```bash
npm i -g vercel
vercel login
vercel       # Deploy with guided setup
vercel --prod  # Deploy to production
```

### vercel.json Configuration
```json
{
  "framework": "nextjs",
  "buildCommand": "next build",
  "devCommand": "next dev",
  "installCommand": "pnpm install",
  "regions": ["iad1", "sfo1"],
  "functions": {
    "app/api/**/*.ts": { "maxDuration": 30 }
  },
  "headers": [
    {
      "source": "/api/(.*)",
      "headers": [
        { "key": "Access-Control-Allow-Origin", "value": "*" }
      ]
    }
  ],
  "rewrites": [
    { "source": "/old-path", "destination": "/new-path" }
  ],
  "redirects": [
    { "source": "/old", "destination": "/new", "permanent": true }
  ]
}
```

### Environment Variables in Vercel
```
NEXT_PUBLIC_API_URL=https://api.example.com  # Public (client-side)
DATABASE_URL=postgresql://...                  # Private (server only)
```

---

## 🐳 Docker

### Dockerfile (Node.js / Next.js)
```dockerfile
# Multi-stage build for production
FROM node:20-alpine AS base

# Install dependencies
FROM base AS deps
WORKDIR /app
COPY package.json pnpm-lock.yaml ./
RUN npm install -g pnpm && pnpm install --frozen-lockfile

# Build
FROM base AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
ENV NEXT_TELEMETRY_DISABLED 1
RUN pnpm build

# Production runner
FROM base AS runner
WORKDIR /app
ENV NODE_ENV production
ENV NEXT_TELEMETRY_DISABLED 1

# Non-root user for security
RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs
USER nextjs

COPY --from=builder /app/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

EXPOSE 3000
ENV PORT 3000
CMD ["node", "server.js"]
```

### docker-compose.yml (Full Stack)
```yaml
version: '3.8'

services:
  web:
    build: .
    ports: ["3000:3000"]
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/myapp
      - REDIS_URL=redis://redis:6379
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
    restart: unless-stopped

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
      POSTGRES_DB: myapp
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    volumes: [redis_data:/data]

volumes:
  postgres_data:
  redis_data:
```

---

## ⚙️ GitHub Actions CI/CD

### Next.js Deploy to Vercel
```yaml
# .github/workflows/deploy.yml
name: Deploy

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '20', cache: 'npm' }
      - run: npm ci
      - run: npm run lint
      - run: npm run type-check
      - run: npm test
      
  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4
      - uses: amondnet/vercel-action@v25
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.ORG_ID }}
          vercel-project-id: ${{ secrets.PROJECT_ID }}
          vercel-args: '--prod'
```

### Docker Build & Push
```yaml
name: Build & Deploy

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
      - name: Login to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_TOKEN }}
      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: username/myapp:latest,username/myapp:${{ github.sha }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

---

## 🌐 CDN & Edge

### Cloudflare Setup
1. Add domain to Cloudflare
2. Enable Proxy (orange cloud)
3. Set SSL/TLS to Full (Strict)
4. Enable Auto Minify (HTML, CSS, JS)
5. Enable Brotli compression
6. Add Page Rules or Transform Rules for redirects
7. Enable HTTP/3

### Cloudflare Workers (Edge Functions)
```javascript
export default {
  async fetch(request, env) {
    const url = new URL(request.url)
    
    if (url.pathname.startsWith('/api/')) {
      return await handleAPI(request, env)
    }
    
    return fetch(request) // Pass through to origin
  }
}
```

---

## 🔒 SSL/TLS Setup

```bash
# Let's Encrypt with Certbot (free SSL)
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d example.com -d www.example.com

# Auto-renewal
sudo systemctl enable certbot.timer
```

---

## 📋 Deployment Checklist

- [ ] Environment variables set in hosting platform
- [ ] `.env` files not committed to git
- [ ] Database migrations run before deploy
- [ ] Health check endpoint `/api/health` working
- [ ] Custom domain configured with HTTPS
- [ ] Error tracking set up (Sentry)
- [ ] Logging configured
- [ ] Backups scheduled for database
- [ ] CDN configured for static assets
- [ ] Rate limiting enabled on API routes
- [ ] Security headers configured
- [ ] Monitoring/uptime check set up (UptimeRobot, Better Uptime)
