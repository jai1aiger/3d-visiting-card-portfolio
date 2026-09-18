# 💳 25 — E-Commerce, Payments & Billing
> **Use this file when**: Building checkout flows, subscriptions, carts, Stripe webhooks, or product showcases.

---

## 🛍️ Payment Gateway Comparison

| Provider | Best For | Recurring/Sub | Fees (Standard) | Developer Experience |
|----------|----------|---------------|-----------------|----------------------|
| **Stripe** | Global standard, developers | ⭐⭐⭐⭐⭐ | 2.9% + 30¢ | Industry benchmark |
| **Lemon Squeezy** | Merchant of Record (MoR) for SaaS/Digital | ⭐⭐⭐⭐⭐ | 5% + 50¢ | Handles global taxes |
| **Paddle** | MoR for SaaS / EU VAT | ⭐⭐⭐⭐ | 5% + 50¢ | Global tax compliance |
| **Razorpay** | India / South Asia | ⭐⭐⭐⭐ | 2% + GST | UPI, Cards, NetBanking |
| **PayPal** | Consumer fallback | ⭐⭐⭐ | 3.49% + 49¢ | High consumer trust |

---

## ⚡ Stripe Integration (Next.js App Router)

```bash
npm i stripe @stripe/stripe-js
```

### 1. Stripe Client Checkout Session (API Route)
```typescript
// app/api/checkout/route.ts
import { NextResponse } from 'next/server'
import Stripe from 'stripe'

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!, {
  apiVersion: '2024-06-20',
})

export async function POST(req: Request) {
  try {
    const { items, customerEmail } = await req.json()

    const session = await stripe.checkout.sessions.create({
      payment_method_types: ['card'],
      customer_email: customerEmail,
      line_items: items.map((item: any) => ({
        price_data: {
          currency: 'usd',
          product_data: { name: item.name, images: [item.image] },
          unit_amount: Math.round(item.price * 100), // cents
        },
        quantity: item.quantity,
      })),
      mode: 'payment',
      success_url: `${process.env.NEXT_PUBLIC_SITE_URL}/success?session_id={CHECKOUT_SESSION_ID}`,
      cancel_url: `${process.env.NEXT_PUBLIC_SITE_URL}/cart`,
    })

    return NextResponse.json({ url: session.url })
  } catch (error: any) {
    return NextResponse.json({ error: error.message }, { status: 500 })
  }
}
```

### 2. Stripe Secure Webhook Handler
```typescript
// app/api/webhooks/stripe/route.ts
import { headers } from 'next/headers'
import { NextResponse } from 'next/server'
import Stripe from 'stripe'

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!, {
  apiVersion: '2024-06-20',
})

export async function POST(req: Request) {
  const body = await req.text()
  const signature = headers().get('stripe-signature') as string

  let event: Stripe.Event

  try {
    event = stripe.webhooks.constructEvent(
      body,
      signature,
      process.env.STRIPE_WEBHOOK_SECRET!
    )
  } catch (err: any) {
    return new NextResponse(`Webhook Error: ${err.message}`, { status: 400 })
  }

  switch (event.type) {
    case 'checkout.session.completed': {
      const session = event.data.object as Stripe.Checkout.Session
      // Provision access, record order in database, trigger confirmation email
      console.log('Payment succeeded for session:', session.id)
      break
    }
    case 'customer.subscription.deleted': {
      // Handle subscription cancellation
      break
    }
  }

  return NextResponse.json({ received: true })
}
```

---

## 🛒 Shopping Cart State with Zustand

```typescript
// store/cartStore.ts
import { create } from 'zustand'
import { persist } from 'zustand/middleware'

export interface CartItem {
  id: string
  name: string
  price: number
  quantity: number
  image?: string
}

interface CartState {
  items: CartItem[]
  addItem: (item: CartItem) => void
  removeItem: (id: string) => void
  updateQuantity: (id: string, qty: number) => void
  clearCart: () => void
  totalAmount: () => number
}

export const useCartStore = create<CartState>()(
  persist(
    (set, get) => ({
      items: [],
      addItem: (item) => {
        const existing = get().items.find((i) => i.id === item.id)
        if (existing) {
          set({
            items: get().items.map((i) =>
              i.id === item.id ? { ...i, quantity: i.quantity + item.quantity } : i
            ),
          })
        } else {
          set({ items: [...get().items, item] })
        }
      },
      removeItem: (id) => set({ items: get().items.filter((i) => i.id !== id) }),
      updateQuantity: (id, qty) =>
        set({
          items: get().items.map((i) => (i.id === id ? { ...i, quantity: qty } : i)),
        }),
      clearCart: () => set({ items: [] }),
      totalAmount: () => get().items.reduce((sum, i) => sum + i.price * i.quantity, 0),
    }),
    { name: 'shopping-cart-storage' }
  )
)
```
