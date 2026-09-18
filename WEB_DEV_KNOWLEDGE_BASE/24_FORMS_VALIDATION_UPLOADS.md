# 📝 24 — Forms, Validation & File Uploads
> **Use this file when**: Building user forms, validation pipelines, multi-step wizards, or file upload systems.

---

## 📋 Form Library Comparison (React & Modern Web)

| Library | Type | Performance | Learning Curve | GitHub Stars |
|---------|------|-------------|----------------|--------------|
| **React Hook Form** | Uncontrolled | ⚡⚡⚡⚡⚡ | Low | ⭐ 41k+ |
| **Formik** | Controlled | ⚡⚡⚡ | Low | ⭐ 33k+ |
| **TanStack Form** | Headless/Agnostic | ⚡⚡⚡⚡⚡ | Medium | ⭐ 4k+ |
| **VeeValidate** | Vue 3 | ⚡⚡⚡⚡ | Low | ⭐ 10k+ |
| **Conform** | Remix/Next Server Actions | ⚡⚡⚡⚡⚡ | Medium | ⭐ 3k+ |
| **Native HTML5** | Browser Built-in | ⚡⚡⚡⚡⚡ | Zero | Built-in |

---

## ⚡ React Hook Form + Zod (Industry Standard 2025)

```bash
npm i react-hook-form @hookform/resolvers zod
```

### Complete Production Example
```tsx
import React from 'react'
import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import * as z from 'zod'

const formSchema = z.object({
  fullName: z.string().min(2, 'Name must be at least 2 characters'),
  email: z.string().email('Please enter a valid email address'),
  password: z
    .string()
    .min(8, 'Password must be at least 8 characters')
    .regex(/[A-Z]/, 'Must contain at least 1 uppercase letter')
    .regex(/[0-9]/, 'Must contain at least 1 number'),
  terms: z.literal(true, {
    errorMap: () => ({ message: 'You must accept the terms and conditions' }),
  }),
})

type FormValues = z.infer<typeof formSchema>

export function SignupForm() {
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
    reset,
  } = useForm<FormValues>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      fullName: '',
      email: '',
      password: '',
    },
  })

  const onSubmit = async (data: FormValues) => {
    try {
      const res = await fetch('/api/auth/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      })
      if (!res.ok) throw new Error('Registration failed')
      reset()
      alert('Account created!')
    } catch (err: any) {
      alert(err.message)
    }
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4 max-w-md mx-auto p-6 bg-white rounded-xl shadow">
      <div>
        <label className="block text-sm font-medium mb-1">Full Name</label>
        <input
          {...register('fullName')}
          className="w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
          placeholder="Jane Doe"
        />
        {errors.fullName && <p className="text-red-500 text-xs mt-1">{errors.fullName.message}</p>}
      </div>

      <div>
        <label className="block text-sm font-medium mb-1">Email</label>
        <input
          type="email"
          {...register('email')}
          className="w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
          placeholder="jane@example.com"
        />
        {errors.email && <p className="text-red-500 text-xs mt-1">{errors.email.message}</p>}
      </div>

      <div>
        <label className="block text-sm font-medium mb-1">Password</label>
        <input
          type="password"
          {...register('password')}
          className="w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
        />
        {errors.password && <p className="text-red-500 text-xs mt-1">{errors.password.message}</p>}
      </div>

      <div className="flex items-center gap-2">
        <input type="checkbox" {...register('terms')} id="terms" className="rounded" />
        <label htmlFor="terms" className="text-xs text-gray-600">I agree to the Terms of Service</label>
      </div>
      {errors.terms && <p className="text-red-500 text-xs">{errors.terms.message}</p>}

      <button
        type="submit"
        disabled={isSubmitting}
        className="w-full py-2.5 px-4 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg disabled:opacity-50 transition"
      >
        {isSubmitting ? 'Creating Account...' : 'Sign Up'}
      </button>
    </form>
  )
}
```

---

## 📁 File Upload Libraries & Solutions

| Tool | Type | Best For | GitHub Stars |
|------|------|----------|--------------|
| **UploadThing** | Full-Stack SDK | Next.js / React serverless file uploads | ⭐ 4.5k+ |
| **Uppy** | Frontend UI | Drag & drop, webcam, multi-source | ⭐ 29k+ |
| **Dropzone.js** | Frontend Drop | Drag-and-drop file uploads | ⭐ 18k+ |
| **FilePond** | Frontend Drop | Smooth UI, image preview, cropping | ⭐ 15k+ |
| **Multer** | Node Middleware | Express multipart/form-data | ⭐ 11k+ |
| **S3 Presigned URLs**| Cloud Architecture| Direct-to-storage without server load | AWS Standard |

### Direct Cloud Upload Pattern (S3 / Cloudflare R2)
1. Frontend requests a pre-signed PUT URL from backend: `POST /api/upload/presign`
2. Backend generates signed URL with expiry (e.g. 5 minutes) via AWS SDK or Supabase Storage.
3. Frontend uploads directly to S3/R2 using `fetch(signedUrl, { method: 'PUT', body: file })`.
4. Result: Zero backend bandwidth consumption, supports multi-GB files.

---

## 🧙‍♂️ Multi-Step Wizard Pattern
- Keep step state in URL query parameters (`?step=1`, `?step=2`) for browser back-button support.
- Persist draft state in `sessionStorage` or Zustand persist store.
- Validate only current step fields before progressing to the next step.
