# 🏪 11 — State Management
> **Use this file when**: Managing global state in frontend applications.

---

## 🔷 State Management Comparison

| Library | Size | Complexity | Best For | Stars |
|---------|------|-----------|---------|-------|
| **Zustand** | 1KB | Very Low | Small-large apps | ⭐ 47k+ |
| **Jotai** | 13KB | Low | Atomic state, React | ⭐ 18k+ |
| **Redux Toolkit** | ~40KB | High | Large teams, complex | ⭐ 10k+ |
| **Pinia** | 28KB | Low | Vue 3 apps | ⭐ 13k+ |
| **Valtio** | 4KB | Very Low | Proxy-based | ⭐ 9k+ |
| **Recoil** | Large | Medium | Facebook-style atomic | ⭐ 19k+ |
| **XState** | 20KB | High | State machines | ⭐ 27k+ |
| **TanStack Query** | 50KB | Medium | Server state | ⭐ 43k+ |
| **SWR** | 25KB | Low | Server state (Next) | ⭐ 30k+ |
| **Nanostores** | 1KB | Very Low | Framework-agnostic | ⭐ 5k+ |
| **Context API** | 0KB | Low | Simple, built-in React | Built-in |

---

## ⭐ Zustand (Recommended for Most)

GitHub: https://github.com/pmndrs/zustand ⭐ 47k+
```bash
npm i zustand
```

### Basic Store
```typescript
import { create } from 'zustand'

interface CounterState {
  count: number
  increment: () => void
  decrement: () => void
  reset: () => void
}

const useCounterStore = create<CounterState>((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 })),
  decrement: () => set((state) => ({ count: state.count - 1 })),
  reset: () => set({ count: 0 }),
}))

// Usage
function Counter() {
  const { count, increment } = useCounterStore()
  return <button onClick={increment}>{count}</button>
}
```

### Zustand with Persistence
```typescript
import { create } from 'zustand'
import { persist, createJSONStorage } from 'zustand/middleware'

const useThemeStore = create(
  persist(
    (set) => ({
      theme: 'light',
      setTheme: (theme) => set({ theme }),
    }),
    { name: 'theme-storage', storage: createJSONStorage(() => localStorage) }
  )
)
```

### Zustand with Immer (Immutable updates)
```typescript
import { produce } from 'immer'
import { create } from 'zustand'

const useStore = create((set) => ({
  todos: [],
  addTodo: (text) => set(produce((state) => {
    state.todos.push({ id: Date.now(), text, done: false })
  })),
  toggleTodo: (id) => set(produce((state) => {
    const todo = state.todos.find(t => t.id === id)
    if (todo) todo.done = !todo.done
  }))
}))
```

---

## ⚛️ Jotai (Atomic State)

GitHub: https://github.com/pmndrs/jotai ⭐ 18k+
```bash
npm i jotai
```

```typescript
import { atom, useAtom, useAtomValue, useSetAtom } from 'jotai'

// Atoms (like useState but global)
const countAtom = atom(0)
const doubleAtom = atom((get) => get(countAtom) * 2) // derived atom

// Usage
function Counter() {
  const [count, setCount] = useAtom(countAtom)
  const double = useAtomValue(doubleAtom)
  
  return (
    <>
      <p>Count: {count}, Double: {double}</p>
      <button onClick={() => setCount(c => c + 1)}>+</button>
    </>
  )
}

// async atom
const userAtom = atom(async (get) => {
  const id = get(userIdAtom)
  const res = await fetch(`/api/users/${id}`)
  return res.json()
})
```

---

## 🗃️ Redux Toolkit (RTK)

GitHub: https://github.com/reduxjs/redux-toolkit ⭐ 10k+
```bash
npm i @reduxjs/toolkit react-redux
```

```typescript
// store/counterSlice.ts
import { createSlice, PayloadAction } from '@reduxjs/toolkit'

const counterSlice = createSlice({
  name: 'counter',
  initialState: { value: 0 },
  reducers: {
    increment: (state) => { state.value += 1 },
    decrement: (state) => { state.value -= 1 },
    incrementByAmount: (state, action: PayloadAction<number>) => {
      state.value += action.payload
    }
  }
})

export const { increment, decrement, incrementByAmount } = counterSlice.actions
export default counterSlice.reducer

// store/index.ts
import { configureStore } from '@reduxjs/toolkit'
export const store = configureStore({
  reducer: { counter: counterSlice.reducer }
})
export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch

// Usage
import { useSelector, useDispatch } from 'react-redux'
const count = useSelector((state: RootState) => state.counter.value)
const dispatch = useDispatch()
dispatch(increment())
```

### RTK Query (API Data Fetching)
```typescript
import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'

export const usersApi = createApi({
  reducerPath: 'usersApi',
  baseQuery: fetchBaseQuery({ baseUrl: '/api' }),
  tagTypes: ['User'],
  endpoints: (builder) => ({
    getUsers: builder.query<User[], void>({ query: () => '/users' }),
    getUserById: builder.query<User, number>({ query: (id) => `/users/${id}` }),
    createUser: builder.mutation<User, Partial<User>>({
      query: (body) => ({ url: '/users', method: 'POST', body }),
      invalidatesTags: ['User']
    })
  })
})

export const { useGetUsersQuery, useCreateUserMutation } = usersApi
```

---

## 🌿 Pinia (Vue 3)

GitHub: https://github.com/vuejs/pinia ⭐ 13k+
```bash
npm i pinia
```

```typescript
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const doubleCount = computed(() => count.value * 2)
  
  function increment() { count.value++ }
  async function fetchData() { /* ... */ }
  
  return { count, doubleCount, increment, fetchData }
})

// In component
const store = useCounterStore()
store.increment()
```

---

## 🌐 TanStack Query (Server State)

GitHub: https://github.com/TanStack/query ⭐ 43k+
```bash
npm i @tanstack/react-query @tanstack/react-query-devtools
```

```typescript
import { QueryClient, QueryClientProvider, useQuery, useMutation } from '@tanstack/react-query'

const queryClient = new QueryClient({
  defaultOptions: { queries: { staleTime: 5 * 60 * 1000 } }
})

// Fetch data
function Users() {
  const { data, isLoading, error } = useQuery({
    queryKey: ['users'],
    queryFn: () => fetch('/api/users').then(r => r.json()),
  })
  
  if (isLoading) return <Skeleton />
  if (error) return <Error />
  return <UserList users={data} />
}

// Mutate data
function CreateUser() {
  const mutation = useMutation({
    mutationFn: (user) => fetch('/api/users', { method: 'POST', body: JSON.stringify(user) }),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['users'] })
  })
  
  return <button onClick={() => mutation.mutate({ name: 'John' })}>
    {mutation.isPending ? 'Creating...' : 'Create User'}
  </button>
}
```
