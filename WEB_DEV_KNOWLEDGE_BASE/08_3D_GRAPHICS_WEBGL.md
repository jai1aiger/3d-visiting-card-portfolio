# 🌐 08 — 3D Graphics & WebGL
> **Use this file when**: Adding 3D elements, WebGL effects, or immersive experiences to a website.

---

## 🔺 3D/WebGL Library Comparison

| Library | Learning | Performance | Best For | Stars |
|---------|----------|-------------|---------|-------|
| **Three.js** | Medium-High | Excellent | General 3D, scenes | ⭐ 102k+ |
| **React Three Fiber** | Medium | Excellent | React + Three.js | ⭐ 27k+ |
| **Babylon.js** | High | Excellent | Games, complex scenes | ⭐ 24k+ |
| **Spline** | Very Low | Good | 3D design without code | SaaS |
| **GSAP + SVG** | Medium | Great | 2D→3D transitions | ⭐ 20k+ |
| **Lottie 3D** | Very Low | Good | JSON-based 3D | — |
| **Model Viewer** | Very Low | Good | Display GLTF models | ⭐ 7k+ |
| **Vanta.js** | Very Low | Good | Animated 3D backgrounds | ⭐ 8k+ |
| **Particles.js** | Very Low | Good | Particle effects | ⭐ 29k+ |
| **tsParticles** | Very Low | Better | Modern particles.js fork | ⭐ 8k+ |
| **WebGPU** | Very High | Maximum | Next-gen GPU access | Native API |

---

## ⚡ React Three Fiber (R3F) — Recommended

GitHub: https://github.com/pmndrs/react-three-fiber ⭐ 27k+
```bash
npm i three @react-three/fiber @react-three/drei
npm i -D @types/three
```

### Basic Scene Setup
```jsx
import { Canvas } from '@react-three/fiber'
import { OrbitControls, Environment, Stars } from '@react-three/drei'

function Box() {
  const meshRef = useRef()
  useFrame((state, delta) => {
    meshRef.current.rotation.x += delta
    meshRef.current.rotation.y += delta * 0.5
  })
  
  return (
    <mesh ref={meshRef} castShadow>
      <boxGeometry args={[1, 1, 1]} />
      <meshStandardMaterial color="#3b82f6" roughness={0.2} metalness={0.8} />
    </mesh>
  )
}

export default function Scene() {
  return (
    <Canvas camera={{ position: [0, 0, 5], fov: 75 }} shadows>
      <ambientLight intensity={0.3} />
      <directionalLight position={[10, 10, 5]} castShadow />
      <Box />
      <OrbitControls enableZoom={false} autoRotate />
      <Environment preset="city" />
      <Stars radius={100} depth={50} count={5000} />
    </Canvas>
  )
}
```

### Drei Helpers (100+ utilities)
```jsx
import {
  OrbitControls,    // Mouse-controlled camera
  Environment,      // HDR environment lighting
  Stars,            // Starfield
  Float,            // Floating animation
  Text,             // 3D text
  Text3D,           // Extruded 3D text
  Html,             // HTML in 3D space
  useGLTF,          // Load GLTF/GLB models
  useTexture,       // Load textures
  Sparkles,         // Particle sparkles
  MeshReflectorMaterial,  // Reflective floor
  MeshTransmissionMaterial,  // Glass/crystal
  MeshWobbleMaterial,  // Wobbly mesh
  ContactShadows,   // Fake soft shadows
  BakeShadows,      // Bake shadow performance
  Loader,           // Loading bar
  useProgress,      // Loading progress
  Scroll,           // Scroll-linked 3D
  ScrollControls,   // 3D scroll scenes
  PresentationControls,  // Touch/mouse drag
} from '@react-three/drei'
```

### Loading GLTF Models
```jsx
import { useGLTF } from '@react-three/drei'

function Model({ url }) {
  const { scene } = useGLTF(url)
  return <primitive object={scene} />
}

// Preload for performance
useGLTF.preload('/models/laptop.glb')
```

---

## 🌌 Three.js Basics (Without React)

GitHub: https://github.com/mrdoob/three.js ⭐ 102k+
```bash
npm i three
```

```javascript
import * as THREE from 'three'
import { OrbitControls } from 'three/addons/controls/OrbitControls.js'

// Scene setup
const scene = new THREE.Scene()
const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000)
const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true })

renderer.setSize(window.innerWidth, window.innerHeight)
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
document.body.appendChild(renderer.domElement)

// Add geometry
const geometry = new THREE.IcosahedronGeometry(1, 0)
const material = new THREE.MeshStandardMaterial({ 
  color: 0x3b82f6, 
  wireframe: false,
  roughness: 0.3,
  metalness: 0.7
})
const mesh = new THREE.Mesh(geometry, material)
scene.add(mesh)

// Lights
scene.add(new THREE.AmbientLight(0xffffff, 0.3))
const light = new THREE.DirectionalLight(0xffffff, 1)
light.position.set(5, 5, 5)
scene.add(light)

// Controls
const controls = new OrbitControls(camera, renderer.domElement)
camera.position.z = 3

// Animation loop
function animate() {
  requestAnimationFrame(animate)
  mesh.rotation.y += 0.005
  controls.update()
  renderer.render(scene, camera)
}
animate()
```

---

## 🎆 Particle Effects

### tsParticles (Modern)
GitHub: https://github.com/tsparticles/tsparticles ⭐ 8k+
```bash
npm i @tsparticles/react @tsparticles/slim
```

### Particles.js (Classic)
GitHub: https://github.com/VincentGarreau/particles.js ⭐ 29k+
CDN-based, simple config

---

## 🖼️ Vanta.js Backgrounds

GitHub: https://github.com/tengbao/vanta ⭐ 8k+
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r134/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vanta/dist/vanta.waves.min.js"></script>
<script>
VANTA.WAVES({
  el: "#hero",
  mouseControls: true,
  touchControls: true,
  gyroControls: false,
  minHeight: 200.00,
  minWidth: 200.00,
  scale: 1.00,
  scaleMobile: 1.00,
  color: 0x3b5f82
})
</script>
```
Effects: WAVES, BIRDS, CELLS, FOG, GLOBE, HALO, NET, RINGS, TOPOLOGY

---

## 🎮 Spline (No Code 3D)

URL: https://spline.design
```bash
npm i @splinetool/react-spline @splinetool/runtime
```
```jsx
import Spline from '@splinetool/react-spline'
<Spline scene="https://prod.spline.design/YOUR_SCENE_URL/scene.splinecode" />
```
- Visual 3D editor (like Figma for 3D)
- Interactive, scrollable 3D scenes
- Great for landing page heroes

---

## 🎯 Use Cases for 3D on Websites

| Use Case | Recommended Tool |
|----------|-----------------|
| Hero section with 3D object | Spline or R3F + drei |
| Particle background | tsParticles or Vanta.js |
| Product 3D viewer | `<model-viewer>` or R3F |
| Data visualization | Three.js |
| Game/interactive experience | Babylon.js |
| Animated background | Vanta.js |
| Logo animation | GSAP + SVG |
| Scroll-linked 3D | R3F + ScrollControls |
