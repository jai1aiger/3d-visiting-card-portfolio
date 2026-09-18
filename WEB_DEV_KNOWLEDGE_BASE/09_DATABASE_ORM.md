# 🗄️ 09 — Databases & ORM
> **Use this file when**: Choosing a database, setting up ORM, or designing data models.

---

## 🔷 Database Types Overview

| Type | Examples | Best For |
|------|---------|---------|
| **Relational (SQL)** | PostgreSQL, MySQL, SQLite | Structured data, complex queries |
| **Document (NoSQL)** | MongoDB, CouchDB | Flexible schema, JSON data |
| **Key-Value** | Redis, DynamoDB | Caching, sessions, counters |
| **Column-Wide** | Cassandra, Bigtable | Time-series, IoT, high write |
| **Graph** | Neo4j, ArangoDB | Social networks, recommendations |
| **Vector** | Pinecone, Weaviate | AI/ML, semantic search |
| **Time Series** | InfluxDB, TimescaleDB | Metrics, monitoring |
| **Search Engine** | Elasticsearch, Meilisearch | Full-text search |

---

## 🐘 PostgreSQL (Recommended SQL DB)

### Why PostgreSQL?
- ACID compliant, extremely reliable
- JSON/JSONB support (SQL + NoSQL)
- Full-text search built-in
- Extensions (PostGIS, TimescaleDB, pgvector for AI)
- Free and open source

### Setup with Docker
```bash
docker run -d \
  --name postgres \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=myapp \
  -p 5432:5432 \
  postgres:16-alpine
```

### Connection
```javascript
// Node.js with pg
const { Pool } = require('pg')
const pool = new Pool({ connectionString: process.env.DATABASE_URL })

// Prisma (recommended ORM)
DATABASE_URL="postgresql://user:password@localhost:5432/myapp"
```

---

## ⚡ Prisma ORM (Best Node.js ORM)

GitHub: https://github.com/prisma/prisma ⭐ 40k+
```bash
npm i prisma @prisma/client
npx prisma init
npx prisma migrate dev --name init
npx prisma generate
```

### Schema Example
```prisma
// prisma/schema.prisma
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model User {
  id        Int      @id @default(autoincrement())
  email     String   @unique
  name      String?
  createdAt DateTime @default(now())
  posts     Post[]
}

model Post {
  id        Int      @id @default(autoincrement())
  title     String
  content   String?
  published Boolean  @default(false)
  author    User     @relation(fields: [authorId], references: [id])
  authorId  Int
  createdAt DateTime @default(now())
}
```

### CRUD Operations
```typescript
import { PrismaClient } from '@prisma/client'
const prisma = new PrismaClient()

// Create
const user = await prisma.user.create({
  data: { email: 'test@example.com', name: 'John' }
})

// Read with relations
const users = await prisma.user.findMany({
  include: { posts: { where: { published: true } } },
  orderBy: { createdAt: 'desc' },
  take: 10,
  skip: 0
})

// Update
await prisma.user.update({
  where: { id: 1 },
  data: { name: 'Jane' }
})

// Delete
await prisma.user.delete({ where: { id: 1 } })

// Upsert
await prisma.user.upsert({
  where: { email: 'test@example.com' },
  create: { email: 'test@example.com', name: 'John' },
  update: { name: 'John Updated' }
})
```

---

## 🗃️ Drizzle ORM (TypeScript-First, Lightweight)

GitHub: https://github.com/drizzle-team/drizzle-orm ⭐ 25k+
```bash
npm i drizzle-orm @libsql/client
npm i -D drizzle-kit
```

```typescript
// schema.ts
import { sqliteTable, text, integer } from 'drizzle-orm/sqlite-core'

export const users = sqliteTable('users', {
  id: integer('id').primaryKey({ autoIncrement: true }),
  name: text('name').notNull(),
  email: text('email').unique().notNull(),
})

// Queries
const allUsers = await db.select().from(users)
await db.insert(users).values({ name: 'John', email: 'john@example.com' })
```

---

## 🍃 MongoDB (NoSQL)

GitHub: https://github.com/mongodb/node-mongodb-native ⭐ 10k+

### With Mongoose (ODM)
```bash
npm i mongoose
```
```javascript
const mongoose = require('mongoose')

const userSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, unique: true, required: true },
  createdAt: { type: Date, default: Date.now }
})

const User = mongoose.model('User', userSchema)

// CRUD
const user = new User({ name: 'John', email: 'john@example.com' })
await user.save()

const users = await User.find({}).sort({ createdAt: -1 }).limit(10)
await User.findByIdAndUpdate(id, { name: 'Jane' })
await User.findByIdAndDelete(id)
```

---

## ⚡ Redis (Caching & Sessions)

GitHub: https://github.com/redis/ioredis ⭐ 14k+
```bash
npm i ioredis
```
```javascript
const Redis = require('ioredis')
const redis = new Redis(process.env.REDIS_URL)

// Cache
await redis.set('key', JSON.stringify(data), 'EX', 3600) // 1hr TTL
const cached = await redis.get('key')

// Rate limiting
await redis.incr('requests:user:123')
await redis.expire('requests:user:123', 60) // reset per minute

// Sessions
await redis.hset('session:abc123', { userId: 1, role: 'admin' })
const session = await redis.hgetall('session:abc123')
```

---

## 🔥 Supabase (Postgres + BaaS)

GitHub: https://github.com/supabase/supabase ⭐ 74k+
```bash
npm i @supabase/supabase-js
```
```javascript
import { createClient } from '@supabase/supabase-js'

const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_ANON_KEY)

// Auth
const { data, error } = await supabase.auth.signUp({ email, password })
await supabase.auth.signInWithPassword({ email, password })
await supabase.auth.signOut()

// Database (PostgreSQL via PostgREST)
const { data: users } = await supabase.from('users').select('*').eq('role', 'admin')
await supabase.from('posts').insert({ title: 'Hello', content: '...' })
await supabase.from('posts').update({ title: 'Updated' }).eq('id', 1)

// Real-time subscriptions
supabase.channel('posts').on('postgres_changes',
  { event: '*', schema: 'public', table: 'posts' },
  (payload) => console.log(payload)
).subscribe()

// File storage
await supabase.storage.from('avatars').upload('user123.jpg', file)
const { data: { publicUrl } } = supabase.storage.from('avatars').getPublicUrl('user123.jpg')
```

---

## 🌩️ Cloud Database Services

| Service | Type | Free Tier | Best For |
|---------|------|-----------|---------|
| **Supabase** | PostgreSQL | 500MB, 2 projects | Full-stack apps |
| **PlanetScale** | MySQL | 5GB | Serverless MySQL |
| **Neon** | PostgreSQL | 512MB | Serverless Postgres |
| **MongoDB Atlas** | MongoDB | 512MB | Document DB |
| **Turso** | SQLite/LibSQL | 8GB | Edge SQLite |
| **Railway** | PostgreSQL/MySQL | ~$5/mo | Simple deploy |
| **Upstash** | Redis | 10k req/day | Redis serverless |
| **FaunaDB** | Document/Graph | 100k reads | Serverless |
| **Xata** | PostgreSQL+Search | Free | Search-first DB |

---

## 📊 Database Design Best Practices

```sql
-- Always use these patterns:
-- 1. UUID primary keys for distributed systems
id UUID PRIMARY KEY DEFAULT gen_random_uuid()

-- 2. Timestamps on every table
created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()

-- 3. Soft deletes
deleted_at TIMESTAMPTZ

-- 4. Indexes on frequently queried columns
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_posts_author ON posts(author_id);

-- 5. Foreign key constraints
FOREIGN KEY (author_id) REFERENCES users(id) ON DELETE CASCADE
```
