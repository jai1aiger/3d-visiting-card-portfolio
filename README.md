# 📇 VTKRO 360° Interactive 3D Digital Visiting Card

> ### 🌐 [👉 CLICK HERE TO OPEN AND VIEW THE LIVE 3D CARD 👈](https://jai1aiger.github.io/vtkro-3d-digital-card/)
> **Live URL**: `https://jai1aiger.github.io/vtkro-3d-digital-card/`
> 
> **📥 Downloadable Standalone File**: [VTKRO-3D-Digital-Card.html](VTKRO-3D-Digital-Card.html) (Double-click to view offline anytime!)
> 
> **📇 1-Click Phone Contact**: [VTKRO-Contact.vcf](VTKRO-Contact.vcf) (Save to smartphone contacts)

[![Live Demo](https://img.shields.io/badge/Live%20Demo-View%20Card-00e5ff?style=for-the-badge&logo=github)](https://jai1aiger.github.io/vtkro-3d-digital-card/)
[![Download Card](https://img.shields.io/badge/Download-Standalone%20File-0284c7?style=for-the-badge&logo=html5)](https://jai1aiger.github.io/vtkro-3d-digital-card/VTKRO-3D-Digital-Card.html)
[![Platform](https://img.shields.io/badge/platform-Mobile%20%7C%20Tablet%20%7C%20Desktop-00e5ff?style=flat-square)](#)
[![Dependency](https://img.shields.io/badge/dependencies-Zero%20(100%25%20Offline)-10b981?style=flat-square)](#)

An executive, high-performance **360° Interactive 3D Digital Visiting Card** engineered for **VTKRO — Virtual Tour Kro**. Designed to deliver an immersive, tactile physical card feel with smooth multi-axis swipe gestures, momentum physics, and instant dual-face flipping.

---

## 📥 Download as a File & View Anytime

You can now download the 3D visiting card as a standalone file (`VTKRO-3D-Digital-Card.html`):
1. **Download the File**: Click **"Download Card File"** on the [Live Site](https://jai1aiger.github.io/vtkro-3d-digital-card/) or download [VTKRO-3D-Digital-Card.html](VTKRO-3D-Digital-Card.html).
2. **Click to Open**: Simply click or double-click the downloaded file in your file manager / Downloads on Windows, Mac, Android, or iOS.
3. **Pop-up Card Reveal**: The VTKRO 3D digital card instantly **pops up on your screen** with full 360° swipe rotation, specular sheen, and tap-to-flip.
4. **100% Offline**: Zero internet connection and zero external files needed. All visuals are 100% self-contained.

---

## ✨ Features

- **📱 Designed for Any Mobile Device**: Dynamically calibrated (`min(96vw, 680px)`) to fit comfortably on any smartphone screen (iPhone, Samsung Galaxy, Pixel, etc.) in both portrait and landscape.
- **🔄 360° Free Touch Swiping**: Drag or swipe anywhere on the screen in **any direction** (horizontal, vertical, diagonal) to freely tumble and spin the card in 3D space without clamp limits.
- **⚡ Physics Momentum & Inertia**: Releasing a swipe applies natural angular velocity that decelerates smoothly with friction physics.
- **👆 Tap to Flip**: Tapping or clicking anywhere on the screen triggers a smooth 180° flip between the Front (Logo & Contact) and Back (QR Code).
- **🎬 Pop-Up Entrance Animation**: On page load, the card smoothly rises from below the viewport into the center stage with an elastic spring easing curve.
- **✨ Subtle Hidden Specular Reflection**: A virtual hidden light source dynamically glides across the card surface as it tilts, producing a soft, realistic semi-gloss laminate glint without glare.
- **🖼️ Full Edge-to-Edge Artwork**: Both front and back images seamlessly cover the card with zero letterboxing or black margins.
- **📦 100% Offline & Standalone (`file:///`)**: Zero external dependencies, libraries, or build steps. Images are linked locally with embedded Base64 fallbacks, meaning the file opens and runs locally on any device even without internet.

---

## 🎨 Card Design & Faces

| Face | Artwork | Details |
| :--- | :--- | :--- |
| **Front** | **VTKRO Logo & Contact Hub** | Futuristic 3D chrome `VT` monogram, `VTKRO - VIRTUAL TOUR KRO` wordmark, direct voice & WhatsApp contact (`+91 9676700488`), website (`Vtkro.com`), email, and location. |
| **Back** | **QR Gateway & Value Guarantee** | High-contrast glowing QR Code connecting directly to the portfolio, *"SCAN TO CONNECT"*, and *"SAME SUPPORT AT EVERY LEVEL"*. |

---

## 🚀 Quick Start

### Option 1: Direct File Launch (No Server Needed)
Simply double-click [`index.html`](index.html) in your file manager (Windows Explorer, Mac Finder, Android Files). It opens and runs natively via the `file:///` protocol in any modern browser.

### Option 2: Run via Local Development Server
To preview or share across devices on the same Wi-Fi network:

```bash
# Using Python
python server.py

# Or one-line HTTP server
python -m http.server 3000
```

Then visit:
- **Local machine**: `http://localhost:3000/`
- **Mobile on same Wi-Fi**: `http://<your-local-ip>:3000/`

---

## 📁 Repository Structure

```
├── index.html                    # Main production standalone interactive 3D digital card
├── vtkro-digital-card.html        # Portable release build with embedded assets
├── card_front_normalized.png     # High-resolution front face graphic (1024x350)
├── card_back_normalized.png      # High-resolution back face graphic (1024x350, borderless)
├── 3d-lanyard-card-demo.html     # Bonus: Vercel-style 3D physics lanyard badge simulation
├── build_minimal_card.py         # Build pipeline script for compiling normalized assets
├── server.py                     # Multi-threaded local development server
├── launch_demo.bat               # 1-click Windows launcher
└── README.md                     # Documentation & specifications
```

---

## 📱 Device Compatibility

| Browser / Environment | Compatibility | Protocol Supported |
| :--- | :---: | :---: |
| **iOS Safari (iPhone / iPad)** | ✅ 100% | `http://`, `https://`, `file:///` |
| **Android Chrome / Samsung Internet** | ✅ 100% | `http://`, `https://`, `file:///` |
| **Google Chrome (macOS / Windows / Linux)** | ✅ 100% | `http://`, `https://`, `file:///` |
| **Microsoft Edge (Windows / macOS)** | ✅ 100% | `http://`, `https://`, `file:///` |
| **Mozilla Firefox** | ✅ 100% | `http://`, `https://`, `file:///` |

---

## 🏢 Corporate Identity

- **Entity**: VTKRO — Virtual Tour Kro
- **Primary Value**: India's Most Affordable Website Builder (Zero Subscriptions)
- **Headquarters**: Bhilai, Chhattisgarh, India
- **Support**: `+91 9676700488` | `Vtkro@gmail.com` | [Vtkro.com](https://vtkro.com)
