# 🧩 19 — Component Libraries & UI Kits
> **Use this file when**: Picking ready-made UI components, comparing UI kits, or finding specific component implementations.

---

## ⭐ Top Component Libraries (2025)

### 1. shadcn/ui — The Best Default Choice
GitHub: https://github.com/shadcn-ui/ui ⭐ 80k+
```bash
npx shadcn@latest init
npx shadcn@latest add button card dialog input
```
- Copy-paste components (you own the code)
- Built on Radix UI (accessible) + Tailwind
- TypeScript-first
- Customizable via CSS variables
- Not a npm package — directly in your project

### Available shadcn Components
```
Accordion          Alert            Alert Dialog     Avatar
Badge              Breadcrumb       Button           Calendar
Card               Carousel         Chart            Checkbox
Collapsible        Combobox         Command          Context Menu
Data Table         Date Picker      Dialog           Drawer
Dropdown Menu      Form             Hover Card       Input
Input OTP          Label            Menubar          Navigation Menu
Pagination         Popover          Progress         Radio Group
Resizable          Scroll Area      Select           Separator
Sheet              Skeleton         Slider           Sonner (Toasts)
Switch             Table            Tabs             Textarea
Toast              Toggle           Toggle Group     Tooltip
```

---

### 2. Material UI (MUI) — Google Material Design
GitHub: https://github.com/mui/material-ui ⭐ 94k+
```bash
npm i @mui/material @emotion/react @emotion/styled @mui/icons-material
```
```jsx
import { Button, TextField, Card, Typography, Stack } from '@mui/material'
import { Save } from '@mui/icons-material'

<Stack spacing={2}>
  <Typography variant="h4">Form Title</Typography>
  <TextField label="Email" type="email" fullWidth />
  <Button variant="contained" startIcon={<Save />}>Save</Button>
</Stack>
```

---

### 3. Mantine — Full-Featured, 100+ Components
GitHub: https://github.com/mantinedev/mantine ⭐ 28k+
```bash
npm i @mantine/core @mantine/hooks @mantine/dates
```
```jsx
import { Button, TextInput, Card, Group, Stack, Text } from '@mantine/core'
import { useDisclosure, useLocalStorage } from '@mantine/hooks'

// Hooks included: useDebounce, useLocalStorage, useForm, useDisclosure...
const [opened, { open, close }] = useDisclosure(false)
```
**Includes**: Rich text editor, date picker, notifications, charts, dropzone, spotlight, and more.

---

### 4. Chakra UI — Accessible & Themeable
GitHub: https://github.com/chakra-ui/chakra-ui ⭐ 38k+
```bash
npm i @chakra-ui/react @emotion/react
```
```jsx
import { Button, VStack, HStack, Text, Box, Badge } from '@chakra-ui/react'

<VStack spacing={4} align="start">
  <HStack>
    <Text fontWeight="bold">Status:</Text>
    <Badge colorScheme="green">Active</Badge>
  </HStack>
  <Button colorScheme="blue" size="lg" isLoading={loading}>
    Submit
  </Button>
</VStack>
```

---

### 5. DaisyUI — Tailwind Plugin, 56+ Components
GitHub: https://github.com/saadeghi/daisyui ⭐ 35k+
```bash
npm i -D daisyui
# In tailwind.config: plugins: [require('daisyui')]
```
```html
<button class="btn btn-primary">Primary</button>
<button class="btn btn-outline btn-secondary">Outline</button>

<div class="card bg-base-100 shadow-xl">
  <div class="card-body">
    <h2 class="card-title">Card Title</h2>
    <p>Card description here.</p>
    <div class="card-actions justify-end">
      <button class="btn btn-primary">Action</button>
    </div>
  </div>
</div>

<!-- Modal -->
<dialog class="modal" id="my_modal">
  <div class="modal-box">
    <h3 class="font-bold text-lg">Hello!</h3>
    <form method="dialog">
      <button class="btn">Close</button>
    </form>
  </div>
</dialog>
```
Themes: `light, dark, cupcake, bumblebee, emerald, corporate, synthwave, retro, cyberpunk, valentine, halloween, garden, forest, aqua, lofi, pastel, fantasy, wireframe, black, luxury, dracula, cmyk, autumn, business, acid, lemonade, night, coffee, winter, dim, nord, sunset`

---

### 6. NextUI — Modern, Framer Motion
GitHub: https://github.com/nextui-org/nextui ⭐ 23k+
```bash
npm i @nextui-org/react framer-motion
```
```jsx
import { Button, Card, CardBody, Input, Chip } from '@nextui-org/react'

<Card>
  <CardBody>
    <Input placeholder="Enter email" type="email" />
    <Button color="primary" variant="shadow">Subscribe</Button>
    <Chip color="success" variant="flat">Active</Chip>
  </CardBody>
</Card>
```

---

## 🎠 Specialized UI Components

### Data Tables
| Library | Install | Stars | Features |
|---------|---------|-------|---------|
| **TanStack Table** | `@tanstack/react-table` | ⭐ 25k+ | Headless, powerful |
| **AG Grid** | `ag-grid-react` | ⭐ 13k+ | Enterprise grade |
| **React Table** | `@tanstack/react-table` | ⭐ 25k+ | Same as TanStack |

### Date/Time
| Library | Install | Stars |
|---------|---------|-------|
| **react-day-picker** | `npm i react-day-picker` | ⭐ 6k+ |
| **react-datepicker** | `npm i react-datepicker` | ⭐ 8k+ |
| **Flatpickr** | `npm i flatpickr` | ⭐ 16k+ |

### Charts & Data Viz
| Library | Install | Stars | Type |
|---------|---------|-------|------|
| **Recharts** | `npm i recharts` | ⭐ 24k+ | React, D3-based |
| **Chart.js** | `npm i chart.js react-chartjs-2` | ⭐ 64k+ | Universal |
| **Tremor** | `npm i @tremor/react` | ⭐ 18k+ | Dashboard focused |
| **Visx** | `npm i @visx/group` | ⭐ 20k+ | D3 + React, Airbnb |
| **ApexCharts** | `npm i apexcharts react-apexcharts` | ⭐ 14k+ | Interactive |
| **ECharts** | `npm i echarts echarts-for-react` | ⭐ 60k+ | Apache, complex |
| **D3.js** | `npm i d3` | ⭐ 108k+ | Ultimate flexibility |

### Rich Text Editors
| Library | Install | Stars |
|---------|---------|-------|
| **Tiptap** | `npm i @tiptap/react` | ⭐ 27k+ |
| **Quill** | `npm i react-quill` | ⭐ 43k+ |
| **Slate.js** | `npm i slate slate-react` | ⭐ 30k+ |
| **Lexical** | `npm i lexical @lexical/react` | ⭐ 19k+ |

### Drag & Drop
| Library | Install | Stars |
|---------|---------|-------|
| **dnd-kit** | `npm i @dnd-kit/core` | ⭐ 13k+ |
| **react-beautiful-dnd** | `npm i react-beautiful-dnd` | ⭐ 32k+ |
| **Pragmatic DnD** | `npm i @atlaskit/pragmatic-drag-and-drop` | Atlassian |

### Toast / Notifications
| Library | Install | Stars |
|---------|---------|-------|
| **Sonner** | `npm i sonner` | ⭐ 8k+ |
| **React Hot Toast** | `npm i react-hot-toast` | ⭐ 9k+ |
| **React Toastify** | `npm i react-toastify` | ⭐ 13k+ |

### Carousels / Sliders
| Library | Install | Stars |
|---------|---------|-------|
| **Embla Carousel** | `npm i embla-carousel-react` | ⭐ 7k+ |
| **Swiper** | `npm i swiper` | ⭐ 39k+ |
| **Keen Slider** | `npm i keen-slider` | ⭐ 5k+ |

---

## 🎪 Headless Component Libraries (No Styling)

| Library | Stars | Description |
|---------|-------|-------------|
| **Radix UI** | ⭐ 16k+ | Accessible, unstyled primitives |
| **Headless UI** | ⭐ 26k+ | Tailwind team, React + Vue |
| **Ark UI** | ⭐ 4k+ | Chakra team, framework-agnostic |
| **React Aria** | ⭐ 13k+ | Adobe, WAI-ARIA compliant |
| **Base UI** | MUI | MUI-backed headless components |
