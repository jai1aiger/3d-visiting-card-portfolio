# 🔌 18 — API Design: REST, GraphQL & WebSockets
> **Use this file when**: Designing APIs, choosing between REST/GraphQL, or adding real-time features.

---

## 🔷 API Technology Comparison

| Technology | Best For | Pros | Cons |
|------------|---------|------|------|
| **REST** | CRUD apps, public APIs | Simple, cacheable, universal | Over/under-fetching |
| **GraphQL** | Complex UIs, mobile apps | Precise data fetching | Complex setup |
| **tRPC** | TypeScript full-stack | End-to-end type safety | TS only |
| **WebSockets** | Real-time, chat, games | Bidirectional, low latency | Connection overhead |
| **SSE** | Live feeds, notifications | Simple, one-way push | Uni-directional |
| **gRPC** | Microservices, high perf | Binary protocol, fast | Browser support limited |

---

## 🌐 REST API Best Practices

### URL Design
```
# Nouns, plural, hierarchical
GET    /api/v1/users              # List all users
POST   /api/v1/users              # Create user
GET    /api/v1/users/:id          # Get user
PATCH  /api/v1/users/:id          # Update partial
PUT    /api/v1/users/:id          # Replace full
DELETE /api/v1/users/:id          # Delete user

# Nested resources
GET    /api/v1/users/:id/posts    # User's posts
GET    /api/v1/users/:id/posts/:postId

# Query parameters
GET    /api/v1/posts?page=1&limit=20&sort=createdAt&order=desc&search=keyword&category=tech

# Actions (when CRUD doesn't fit)
POST   /api/v1/users/:id/activate
POST   /api/v1/orders/:id/cancel
POST   /api/v1/auth/login
POST   /api/v1/auth/logout
POST   /api/v1/auth/refresh
```

### HTTP Status Codes
```
200 OK             — Successful GET, PUT, PATCH
201 Created        — Successful POST
204 No Content     — Successful DELETE
400 Bad Request    — Invalid input/validation error
401 Unauthorized   — Not authenticated
403 Forbidden      — Authenticated but no permission
404 Not Found      — Resource doesn't exist
409 Conflict       — Resource already exists (duplicate email)
422 Unprocessable  — Validation errors with details
429 Too Many Req   — Rate limit exceeded
500 Internal Error — Server error (never expose details)
```

### Standard Response Format
```typescript
// Success
{ "data": {...}, "meta": { "page": 1, "total": 100 } }

// Error
{ "error": { "code": "VALIDATION_ERROR", "message": "...", "details": [...] } }

// Paginated list
{
  "data": [...],
  "meta": {
    "page": 1,
    "limit": 20,
    "total": 245,
    "totalPages": 13,
    "hasNext": true,
    "hasPrev": false
  }
}
```

---

## ⚡ tRPC (TypeScript Full-Stack)

GitHub: https://github.com/trpc/trpc ⭐ 35k+
```bash
npm i @trpc/server @trpc/client @trpc/react-query @trpc/next
```

### Server Setup
```typescript
// server/trpc.ts
import { initTRPC } from '@trpc/server'
import { z } from 'zod'

const t = initTRPC.create()
export const { router, procedure } = t

// router/users.ts
export const usersRouter = router({
  getAll: procedure.query(async () => {
    return await prisma.user.findMany()
  }),
  
  getById: procedure
    .input(z.object({ id: z.number() }))
    .query(async ({ input }) => {
      return await prisma.user.findUniqueOrThrow({ where: { id: input.id } })
    }),
  
  create: procedure
    .input(z.object({ name: z.string().min(1), email: z.string().email() }))
    .mutation(async ({ input }) => {
      return await prisma.user.create({ data: input })
    }),
})

// Root router
export const appRouter = router({ users: usersRouter })
export type AppRouter = typeof appRouter
```

### Client Usage
```typescript
// Client auto-complete from server types!
const { data: users } = trpc.users.getAll.useQuery()
const createUser = trpc.users.create.useMutation()

await createUser.mutateAsync({ name: 'John', email: 'john@example.com' })
```

---

## 🔮 GraphQL

### Apollo Server
```bash
npm i @apollo/server graphql
```

```typescript
import { ApolloServer } from '@apollo/server'
import { startStandaloneServer } from '@apollo/server/standalone'
import { gql } from 'graphql-tag'

const typeDefs = gql`
  type User {
    id: ID!
    name: String!
    email: String!
    posts: [Post!]!
  }
  
  type Post {
    id: ID!
    title: String!
    author: User!
  }
  
  type Query {
    users: [User!]!
    user(id: ID!): User
  }
  
  type Mutation {
    createUser(name: String!, email: String!): User!
    deleteUser(id: ID!): Boolean!
  }
`

const resolvers = {
  Query: {
    users: () => prisma.user.findMany(),
    user: (_, { id }) => prisma.user.findUnique({ where: { id: Number(id) } }),
  },
  Mutation: {
    createUser: (_, args) => prisma.user.create({ data: args }),
  },
  User: {
    posts: (parent) => prisma.post.findMany({ where: { authorId: parent.id } })
  }
}
```

### GraphQL on the Client (urql - Recommended)
```bash
npm i urql graphql
```
```typescript
import { useQuery, useMutation, gql } from 'urql'

const GetUsersQuery = gql`
  query GetUsers {
    users { id name email }
  }
`

function UserList() {
  const [result] = useQuery({ query: GetUsersQuery })
  const { data, fetching, error } = result
  if (fetching) return <Spinner />
  return <ul>{data.users.map(u => <li key={u.id}>{u.name}</li>)}</ul>
}
```

---

## 🔴 WebSockets & Real-Time

### Socket.io
```bash
# Server
npm i socket.io

# Client
npm i socket.io-client
```

```typescript
// Server
import { Server } from 'socket.io'

const io = new Server(httpServer, {
  cors: { origin: ['http://localhost:3000'], methods: ['GET', 'POST'] }
})

io.on('connection', (socket) => {
  console.log('User connected:', socket.id)
  
  socket.on('join-room', (roomId) => {
    socket.join(roomId)
    io.to(roomId).emit('user-joined', { userId: socket.id })
  })
  
  socket.on('message', ({ roomId, text }) => {
    io.to(roomId).emit('message', { userId: socket.id, text, timestamp: Date.now() })
  })
  
  socket.on('disconnect', () => {
    console.log('User disconnected')
  })
})

// Client
import { io } from 'socket.io-client'
const socket = io('http://localhost:3001')

socket.emit('join-room', 'room-123')
socket.on('message', (msg) => setMessages(prev => [...prev, msg]))
```

### Server-Sent Events (SSE) — Simpler, one-way
```typescript
// Next.js API Route
export async function GET(req: Request) {
  const encoder = new TextEncoder()
  const stream = new ReadableStream({
    async start(controller) {
      // Send events
      const sendEvent = (data: object) => {
        controller.enqueue(encoder.encode(`data: ${JSON.stringify(data)}\n\n`))
      }
      
      sendEvent({ message: 'Connected!' })
      // Keep alive / push more events
    }
  })
  
  return new Response(stream, {
    headers: {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',
      'Connection': 'keep-alive',
    }
  })
}

// Client
const eventSource = new EventSource('/api/events')
eventSource.onmessage = (e) => console.log(JSON.parse(e.data))
```

---

## 🔧 API Client Libraries

| Library | Install | Stars | Best For |
|---------|---------|-------|---------|
| **Axios** | `npm i axios` | ⭐ 105k+ | Universal HTTP client |
| **Ky** | `npm i ky` | ⭐ 13k+ | Modern, fetch-based |
| **ofetch** | `npm i ofetch` | ⭐ 4k+ | Next.js/Nuxt optimized |
| **SWR** | `npm i swr` | ⭐ 30k+ | React data fetching |
| **TanStack Query** | `npm i @tanstack/query` | ⭐ 43k+ | Full server state mgmt |
