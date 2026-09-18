# 🤖 27 — AI Integration & Generative UI (2025–2026)
> **Use this file when**: Integrating LLMs, streaming chats, AI assistants, or generative UI components.

---

## 🛠️ Essential AI Toolkits & SDKs

| Toolkit | Description | Stars | Install |
|---------|-------------|-------|---------|
| **Vercel AI SDK** | Unified TypeScript library for building AI-powered UIs | ⭐ 14k+ | `npm i ai @ai-sdk/openai @ai-sdk/google` |
| **LangChain.js** | Agent orchestration, memory, vector stores | ⭐ 13k+ | `npm i langchain` |
| **LlamaIndex.ts** | Data indexing and RAG for TypeScript | ⭐ 3k+ | `npm i llamaindex` |
| **Assistant UI** | Pre-built chat UI components for React | ⭐ 2k+ | `npm i @assistant-ui/react` |
| **CopilotKit** | Embedded AI assistants & copilots for apps | ⭐ 14k+ | `npm i @copilotkit/react-core` |

---

## ⚡ Streaming AI Chat with Vercel AI SDK

### 1. Backend Route Handler (Next.js)
```typescript
// app/api/chat/route.ts
import { streamText } from 'ai'
import { google } from '@ai-sdk/google'

export async function POST(req: Request) {
  const { messages } = await req.json()

  const result = streamText({
    model: google('gemini-1.5-pro-latest'),
    messages,
    system: 'You are an expert design and coding assistant.',
  })

  return result.toDataStreamResponse()
}
```

### 2. Frontend React Component (`useChat`)
```tsx
'use client'
import { useChat } from 'ai/react'

export function AIChat() {
  const { messages, input, handleInputChange, handleSubmit, isLoading } = useChat()

  return (
    <div className="flex flex-col h-[500px] max-w-xl mx-auto border rounded-xl shadow-lg bg-white overflow-hidden">
      <div className="flex-1 p-4 overflow-y-auto space-y-3">
        {messages.map((m) => (
          <div
            key={m.id}
            className={`p-3 rounded-xl max-w-[80%] text-sm ${
              m.role === 'user' ? 'ml-auto bg-blue-600 text-white' : 'mr-auto bg-gray-100 text-gray-800'
            }`}
          >
            {m.content}
          </div>
        ))}
        {isLoading && <div className="text-gray-400 text-xs italic">AI is thinking...</div>}
      </div>

      <form onSubmit={handleSubmit} className="p-3 border-t flex gap-2">
        <input
          value={input}
          onChange={handleInputChange}
          placeholder="Ask a question..."
          className="flex-1 px-3 py-2 border rounded-lg outline-none focus:ring-2 focus:ring-blue-500"
        />
        <button type="submit" className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700">
          Send
        </button>
      </form>
    </div>
  )
}
```
