# ⚙️ 03 — Backend Frameworks & Server Technologies
> **Use this file when**: Choosing a backend technology, building APIs, or architecting server-side logic.

---

## 🏗️ Backend Framework Comparison

| Framework | Language | Performance | Learning Curve | Best For |
|-----------|----------|-------------|----------------|---------|
| **Express.js** | Node.js | ⭐⭐⭐⭐ | Very Low | REST APIs, microservices |
| **Fastify** | Node.js | ⭐⭐⭐⭐⭐ | Low | High-perf Node APIs |
| **NestJS** | TypeScript | ⭐⭐⭐⭐ | High | Enterprise Node.js |
| **Hono** | JS/TS | ⭐⭐⭐⭐⭐ | Very Low | Edge/lightweight APIs |
| **Django** | Python | ⭐⭐⭐ | Medium | Batteries-included |
| **FastAPI** | Python | ⭐⭐⭐⭐⭐ | Low | Modern Python APIs |
| **Flask** | Python | ⭐⭐⭐ | Very Low | Simple Python APIs |
| **Gin** | Go | ⭐⭐⭐⭐⭐ | Medium | High-perf Go APIs |
| **Fiber** | Go | ⭐⭐⭐⭐⭐ | Low | Express-like Go |
| **Axum** | Rust | ⭐⭐⭐⭐⭐ | High | Maximum performance |
| **Laravel** | PHP | ⭐⭐⭐ | Medium | PHP full-stack |
| **Spring Boot** | Java | ⭐⭐⭐⭐ | High | Enterprise Java |

---

## 🟢 Node.js Backends

### Express.js
GitHub: https://github.com/expressjs/express ⭐ 65k+
```bash
npm i express
npm i -D @types/express typescript ts-node nodemon
```

```typescript
import express from 'express'
const app = express()
app.use(express.json())

app.get('/api/users', (req, res) => {
  res.json({ users: [] })
})

app.listen(3000, () => console.log('Server on port 3000'))
```

### Fastify (2x faster than Express)
GitHub: https://github.com/fastify/fastify ⭐ 32k+
```bash
npm i fastify @fastify/cors @fastify/jwt
```

```typescript
import Fastify from 'fastify'
const app = Fastify({ logger: true })

app.get('/api/users', async (request, reply) => {
  return { users: [] }
})

await app.listen({ port: 3000 })
```

### NestJS (Enterprise Node.js)
GitHub: https://github.com/nestjs/nest ⭐ 68k+
```bash
npm i -g @nestjs/cli
nest new my-api
```
- Modular architecture (Angular-inspired)
- Built-in DI, decorators, validation
- OpenAPI/Swagger auto-generation
- Supports REST, GraphQL, WebSockets, microservices

### Hono (Ultra-lightweight, Edge-ready)
GitHub: https://github.com/honojs/hono ⭐ 22k+
```bash
npm i hono
```
- Works on Cloudflare Workers, Deno, Bun, Node
- 14kb bundle size
- TypeScript-first

---

## 🐍 Python Backends

### FastAPI (Modern Python)
GitHub: https://github.com/fastapi/fastapi ⭐ 80k+
```bash
pip install fastapi uvicorn[standard]
uvicorn main:app --reload
```

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    email: str

@app.get("/users")
async def get_users():
    return {"users": []}

@app.post("/users")
async def create_user(user: User):
    return user
```
- Auto-generates OpenAPI/Swagger docs
- Async by default
- Pydantic validation
- One of fastest Python frameworks

### Django (Batteries Included)
GitHub: https://github.com/django/django ⭐ 80k+
```bash
pip install django djangorestframework
django-admin startproject myproject
python manage.py runserver
```
- ORM included
- Admin panel out of the box
- Auth system built-in
- Perfect for complex web apps

### Flask (Micro-framework)
GitHub: https://github.com/pallets/flask ⭐ 68k+
```bash
pip install flask flask-restful
```
- Simple, minimal, flexible
- Great for prototypes and simple APIs

---

## 🐹 Go Backends

### Gin
GitHub: https://github.com/gin-gonic/gin ⭐ 79k+
```bash
go get github.com/gin-gonic/gin
```

```go
package main
import "github.com/gin-gonic/gin"

func main() {
    r := gin.Default()
    r.GET("/users", func(c *gin.Context) {
        c.JSON(200, gin.H{"users": []string{}})
    })
    r.Run(":3000")
}
```

### Fiber (Express-like Go)
GitHub: https://github.com/gofiber/fiber ⭐ 34k+
```bash
go get github.com/gofiber/fiber/v2
```

---

## 🦀 Rust Backends

### Axum
GitHub: https://github.com/tokio-rs/axum ⭐ 20k+
```bash
cargo add axum tokio serde_json
```
- Ergonomic async API
- Built on Tokio + Hyper
- Type-safe routing

### Actix-web
GitHub: https://github.com/actix/actix-web ⭐ 22k+
- One of fastest web frameworks ever benchmarked
- Actor-based concurrency

---

## 🐘 PHP Backends

### Laravel
GitHub: https://github.com/laravel/laravel ⭐ 79k+
```bash
composer create-project laravel/laravel my-app
php artisan serve
```
- Eloquent ORM
- Blade templating
- Built-in queue, scheduling, broadcasting
- Livewire for reactive UIs without JS

---

## 🗄️ Backend Architecture Patterns

### REST API Structure
```
/api/v1/
├── /users          GET (list), POST (create)
├── /users/:id      GET, PUT, PATCH, DELETE
├── /posts          GET, POST
├── /posts/:id      GET, PUT, DELETE
└── /auth
    ├── /login      POST
    ├── /logout     POST
    └── /refresh    POST
```

### Project Structure (Node.js/Express)
```
src/
├── controllers/    ← Request handlers
├── services/       ← Business logic
├── repositories/   ← Database queries
├── models/         ← Data models/schemas
├── middleware/     ← Auth, logging, validation
├── routes/         ← Route definitions
├── utils/          ← Helper functions
├── config/         ← App configuration
└── app.ts          ← App entry point
```

---

## 🌐 BaaS (Backend as a Service)

| Service | GitHub/URL | Features |
|---------|-----------|---------|
| **Supabase** | https://github.com/supabase/supabase ⭐ 74k+ | Postgres, Auth, Storage, Realtime |
| **Appwrite** | https://github.com/appwrite/appwrite ⭐ 45k+ | Self-hostable Firebase alternative |
| **PocketBase** | https://github.com/pocketbase/pocketbase ⭐ 40k+ | Single binary BaaS |
| **Firebase** | google/firebase | Real-time DB, Auth, Hosting |
| **Neon** | neon.tech | Serverless Postgres |
| **PlanetScale** | planetscale.com | Serverless MySQL |
| **Convex** | convex.dev | Real-time backend platform |

---

## 🔌 Essential Backend Middleware

### Node.js Middleware
```bash
npm i cors helmet morgan express-rate-limit compression
npm i express-validator joi    # Validation
npm i multer                   # File uploads
npm i socket.io                # WebSockets
```

| Package | Purpose |
|---------|---------|
| `cors` | Cross-Origin Resource Sharing |
| `helmet` | Security headers |
| `morgan` | HTTP request logger |
| `express-rate-limit` | Rate limiting |
| `compression` | Gzip compression |
| `multer` | File upload handling |
| `socket.io` | Real-time WebSocket communication |

---

## 📧 Email Services (Backend)

| Service | Package | Free Tier |
|---------|---------|-----------|
| **Resend** | `npm i resend` | 3k emails/mo |
| **SendGrid** | `npm i @sendgrid/mail` | 100/day |
| **Nodemailer** | `npm i nodemailer` | Self-managed |
| **Mailgun** | `npm i mailgun.js` | 5k/mo trial |
| **Brevo (Sendinblue)** | SDK | 300/day |
