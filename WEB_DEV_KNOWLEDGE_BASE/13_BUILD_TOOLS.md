# 🔧 13 — Build Tools & Bundlers
> **Use this file when**: Configuring build pipelines, optimizing bundles, or setting up dev environments.

---

## ⚡ Build Tool Comparison

| Tool | Speed | Config | Best For | Stars |
|------|-------|--------|---------|-------|
| **Vite** | ⚡⚡⚡⚡⚡ | Minimal | All modern frameworks | ⭐ 70k+ |
| **Turbopack** | ⚡⚡⚡⚡⚡ | Auto | Next.js 13+ | Built-in |
| **esbuild** | ⚡⚡⚡⚡⚡ | Minimal | Libraries, CLIs | ⭐ 38k+ |
| **Webpack 5** | ⚡⚡ | Complex | Legacy/complex apps | ⭐ 65k+ |
| **Rollup** | ⚡⚡⚡ | Medium | Libraries | ⭐ 25k+ |
| **Parcel** | ⚡⚡⚡ | Zero-config | Beginners | ⭐ 43k+ |
| **Rspack** | ⚡⚡⚡⚡ | Webpack-compat | Webpack migration | ⭐ 10k+ |
| **Bun** | ⚡⚡⚡⚡⚡ | Minimal | Full-stack JS | ⭐ 75k+ |

---

## ⚡ Vite (Recommended)

GitHub: https://github.com/vitejs/vite ⭐ 70k+
```bash
npm create vite@latest my-app -- --template react-ts
```

### vite.config.ts
```typescript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

export default defineConfig({
  plugins: [
    react(),
    // tsconfigPaths(), // path aliases from tsconfig
  ],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
      '@components': path.resolve(__dirname, './src/components'),
      '@hooks': path.resolve(__dirname, './src/hooks'),
    }
  },
  build: {
    outDir: 'dist',
    minify: 'terser',
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
          ui: ['@radix-ui/react-dialog', 'framer-motion'],
        }
      }
    }
  },
  server: {
    port: 3000,
    proxy: {
      '/api': { target: 'http://localhost:8000', changeOrigin: true }
    }
  }
})
```

### Vite Plugins
| Plugin | Install | Purpose |
|--------|---------|---------|
| `@vitejs/plugin-react` | Built-in | React support |
| `@vitejs/plugin-vue` | Built-in | Vue support |
| `vite-plugin-svgr` | npm | Import SVG as React components |
| `vite-tsconfig-paths` | npm | TypeScript path aliases |
| `@vite-pwa/vite-plugin` | npm | PWA support |
| `vite-plugin-checker` | npm | Type checking in dev |
| `rollup-plugin-visualizer` | npm | Bundle analyzer |
| `vite-plugin-compression` | npm | Gzip/Brotli compression |

---

## 📦 Webpack 5 (Legacy but Powerful)

GitHub: https://github.com/webpack/webpack ⭐ 65k+

### webpack.config.js
```javascript
const path = require('path')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')

module.exports = {
  entry: './src/index.tsx',
  output: { path: path.resolve(__dirname, 'dist'), filename: '[name].[contenthash].js' },
  resolve: { extensions: ['.tsx', '.ts', '.js'], alias: { '@': path.resolve(__dirname, 'src') } },
  module: {
    rules: [
      { test: /\.tsx?$/, use: 'ts-loader', exclude: /node_modules/ },
      { test: /\.css$/, use: [MiniCssExtractPlugin.loader, 'css-loader', 'postcss-loader'] },
      { test: /\.(png|svg|jpg|gif)$/, type: 'asset/resource' },
    ]
  },
  plugins: [
    new HtmlWebpackPlugin({ template: './public/index.html' }),
    new MiniCssExtractPlugin({ filename: '[name].[contenthash].css' }),
  ],
  optimization: {
    splitChunks: { chunks: 'all' }
  }
}
```

---

## 📐 TypeScript Configuration

```json
// tsconfig.json (Next.js/Vite)
{
  "compilerOptions": {
    "target": "ES2020",
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "moduleResolution": "bundler",
    "jsx": "react-jsx",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noImplicitAny": true,
    "exactOptionalPropertyTypes": true,
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"],
      "@components/*": ["./src/components/*"],
      "@hooks/*": ["./src/hooks/*"],
      "@utils/*": ["./src/utils/*"],
    },
    "outDir": "dist",
    "skipLibCheck": true
  },
  "include": ["src"],
  "exclude": ["node_modules"]
}
```

---

## 🌈 PostCSS Configuration

```javascript
// postcss.config.js
module.exports = {
  plugins: {
    'tailwindcss': {},
    'autoprefixer': {},
    'postcss-nesting': {},         // CSS nesting (native CSS spec)
    'postcss-custom-media': {},    // Custom media queries
    'cssnano': { preset: 'default' }  // CSS minification (production)
  }
}
```

---

## 📊 Bundle Analysis

```bash
# Vite bundle analyzer
npm i -D rollup-plugin-visualizer
# In vite.config.ts:
visualizer({ open: true, gzipSize: true, brotliSize: true })

# Webpack bundle analyzer
npm i -D webpack-bundle-analyzer
npx webpack-bundle-analyzer dist/stats.json

# Next.js bundle analyzer
npm i -D @next/bundle-analyzer
```

---

## 🚀 Package Scripts Template

```json
{
  "scripts": {
    "dev": "vite",
    "build": "tsc -b && vite build",
    "preview": "vite preview",
    "lint": "eslint . --ext ts,tsx --report-unused-disable-directives",
    "lint:fix": "eslint . --fix",
    "format": "prettier --write \"src/**/*.{ts,tsx,css,md}\"",
    "test": "vitest",
    "test:ui": "vitest --ui",
    "test:coverage": "vitest run --coverage",
    "test:e2e": "playwright test",
    "type-check": "tsc --noEmit",
    "clean": "rm -rf dist node_modules .turbo",
    "analyze": "vite build --mode analyze"
  }
}
```

---

## 🔄 Monorepo Tools

| Tool | Purpose | Install |
|------|---------|---------|
| **Turborepo** | Monorepo build orchestration | `npx create-turbo@latest` |
| **Nx** | Monorepo + code generation | `npx create-nx-workspace` |
| **pnpm Workspaces** | Package management | `pnpm-workspace.yaml` |
| **Yarn Workspaces** | Package management | `workspaces` in package.json |
| **Lerna** | Package publishing | `npx lerna init` |
| **Changesets** | Version management | `npm i -D @changesets/cli` |

```yaml
# pnpm-workspace.yaml
packages:
  - 'apps/*'
  - 'packages/*'
```
