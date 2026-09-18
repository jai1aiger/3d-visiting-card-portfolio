# 🔐 10 — Authentication & Security
> **Use this file when**: Adding user authentication, managing sessions, or securing a web application.

---

## 🔑 Authentication Methods

| Method | Best For | Complexity |
|--------|---------|-----------|
| **Email/Password** | Most apps | Low |
| **OAuth / Social Login** | Consumer apps | Medium |
| **Magic Link** | Frictionless UX | Low |
| **Passkeys (WebAuthn)** | Secure, modern | Medium |
| **JWT Tokens** | Stateless APIs | Medium |
| **Session Cookies** | Traditional web apps | Low |
| **API Keys** | Server-to-server | Low |
| **SSO/SAML** | Enterprise | High |
| **2FA/MFA** | High security | Medium |

---

## ⭐ Auth.js / NextAuth.js (Best for Next.js)

GitHub: https://github.com/nextauthjs/next-auth ⭐ 25k+
```bash
npm i next-auth@beta
```

### Setup (Next.js App Router)
```typescript
// auth.ts
import NextAuth from "next-auth"
import GitHub from "next-auth/providers/github"
import Google from "next-auth/providers/google"
import Credentials from "next-auth/providers/credentials"
import { PrismaAdapter } from "@auth/prisma-adapter"

export const { handlers, signIn, signOut, auth } = NextAuth({
  adapter: PrismaAdapter(prisma),
  providers: [
    GitHub,
    Google,
    Credentials({
      credentials: { email: {}, password: {} },
      authorize: async (credentials) => {
        const user = await getUserByEmail(credentials.email)
        if (!user || !verifyPassword(credentials.password, user.hash)) return null
        return user
      }
    })
  ],
  callbacks: {
    jwt({ token, user }) {
      if (user) token.role = user.role
      return token
    },
    session({ session, token }) {
      session.user.role = token.role
      return session
    }
  }
})
```

```typescript
// app/api/auth/[...nextauth]/route.ts
export { GET, POST } from "@/auth"

// Usage in server component
const session = await auth()
if (!session) redirect('/login')
```

---

## 🔥 Supabase Auth (All-in-One)

```typescript
// Login with email/password
const { data, error } = await supabase.auth.signInWithPassword({ email, password })

// OAuth (Google, GitHub, etc.)
await supabase.auth.signInWithOAuth({ provider: 'google', options: { redirectTo: '/' } })

// Magic link
await supabase.auth.signInWithOtp({ email })

// Get current user
const { data: { user } } = await supabase.auth.getUser()

// Protect route in Next.js middleware
export async function middleware(request: NextRequest) {
  const { data: { session } } = await supabase.auth.getSession()
  if (!session) return NextResponse.redirect(new URL('/login', request.url))
}
```

---

## 🔐 Clerk (Fastest to Implement)

GitHub: https://github.com/clerk/javascript ⭐ 3k+
```bash
npm i @clerk/nextjs
```
```typescript
// middleware.ts
import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server'
const isProtectedRoute = createRouteMatcher(['/dashboard(.*)'])

export default clerkMiddleware((auth, req) => {
  if (isProtectedRoute(req)) auth().protect()
})

// Components
import { SignInButton, SignedIn, SignedOut, UserButton } from '@clerk/nextjs'

<SignedOut><SignInButton /></SignedOut>
<SignedIn><UserButton /></SignedIn>
```
- Pre-built UI components (sign in, sign up, user profile)
- Social logins, MFA, passkeys included
- Free tier: 10k MAU

---

## 🛡️ JWT (JSON Web Tokens)

```bash
npm i jsonwebtoken bcryptjs
npm i -D @types/jsonwebtoken @types/bcryptjs
```

```typescript
import jwt from 'jsonwebtoken'
import bcrypt from 'bcryptjs'

const SECRET = process.env.JWT_SECRET!

// Hash password
const hash = await bcrypt.hash(password, 12)
const valid = await bcrypt.compare(password, hash)

// Generate token
const token = jwt.sign(
  { userId: user.id, role: user.role },
  SECRET,
  { expiresIn: '7d' }
)

// Verify token
try {
  const payload = jwt.verify(token, SECRET) as { userId: string; role: string }
} catch (err) {
  // Token invalid or expired
}
```

### JWT Best Practices
- Short access token expiry (15min)
- Longer refresh token (7-30 days)
- Store in httpOnly cookies (NOT localStorage)
- Rotate refresh tokens on use

---

## 🔒 Security Headers & Best Practices

### Helmet.js (Express Security Headers)
```bash
npm i helmet
```
```javascript
import helmet from 'helmet'
app.use(helmet())
// Sets: Content-Security-Policy, X-Frame-Options, 
// X-Content-Type-Options, Referrer-Policy, etc.
```

### Next.js Security Headers
```javascript
// next.config.js
const securityHeaders = [
  { key: 'X-DNS-Prefetch-Control', value: 'on' },
  { key: 'Strict-Transport-Security', value: 'max-age=63072000; includeSubDomains; preload' },
  { key: 'X-Frame-Options', value: 'SAMEORIGIN' },
  { key: 'X-Content-Type-Options', value: 'nosniff' },
  { key: 'Referrer-Policy', value: 'origin-when-cross-origin' },
  { key: 'Permissions-Policy', value: 'camera=(), microphone=(), geolocation=()' },
]
```

---

## 🚦 Rate Limiting

```bash
npm i express-rate-limit   # Express
npm i @upstash/ratelimit   # Serverless (Redis-based)
```

```typescript
// @upstash/ratelimit with Redis (Vercel Edge)
import { Ratelimit } from "@upstash/ratelimit"
import { Redis } from "@upstash/redis"

const ratelimit = new Ratelimit({
  redis: Redis.fromEnv(),
  limiter: Ratelimit.slidingWindow(10, "10 s"), // 10 req per 10s
})

const { success, limit, reset, remaining } = await ratelimit.limit(identifier)
if (!success) return new Response('Too Many Requests', { status: 429 })
```

---

## 🛡️ Input Validation & Sanitization

```bash
npm i zod              # Type-safe schema validation
npm i validator        # String validators/sanitizers  
npm i dompurify        # XSS sanitization for HTML
npm i hpp              # HTTP Parameter Pollution prevention
```

```typescript
// Zod schema validation
import { z } from 'zod'

const UserSchema = z.object({
  email: z.string().email(),
  password: z.string().min(8).regex(/[A-Z]/).regex(/[0-9]/),
  age: z.number().int().min(13).max(120).optional(),
  role: z.enum(['admin', 'user', 'moderator']).default('user'),
})

const result = UserSchema.safeParse(req.body)
if (!result.success) {
  return res.status(400).json({ errors: result.error.flatten() })
}
```

---

## 🔐 Environment Variables Best Practices

```bash
# .env (local only, NEVER commit)
DATABASE_URL=postgresql://...
JWT_SECRET=your-super-secret-key-min-32-chars
NEXTAUTH_SECRET=another-random-secret
GOOGLE_CLIENT_ID=xxx
GOOGLE_CLIENT_SECRET=xxx

# Generate secrets
openssl rand -base64 32
node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"
```

### .gitignore must include:
```
.env
.env.local
.env.production
```

---

## 🔑 Auth Providers & Services

| Service | Free | Social | MFA | Passkeys |
|---------|------|--------|-----|---------|
| **Clerk** | 10k MAU | Yes | Yes | Yes |
| **Auth.js** | Free OSS | Yes | Plugin | Plugin |
| **Supabase Auth** | 50k MAU | Yes | Yes | Yes |
| **Auth0** | 7.5k MAU | Yes | Yes | Yes |
| **Firebase Auth** | Unlimited | Yes | Yes | No |
| **Lucia** | Free OSS | Manual | Manual | Manual |
| **Better Auth** | Free OSS | Yes | Yes | Yes |
