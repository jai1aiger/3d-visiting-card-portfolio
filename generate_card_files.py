import base64
import os

# 1. Read base64 strings of the front and back card images
with open('card_front_normalized.png', 'rb') as f:
    front_b64 = base64.b64encode(f.read()).decode('ascii')

with open('card_back_normalized.png', 'rb') as f:
    back_b64 = base64.b64encode(f.read()).decode('ascii')

# Read vCard content for inline generation
with open('VTKRO-Contact.vcf', 'r', encoding='utf-8') as f:
    vcf_content = f.read().replace('\n', '\\n').replace('"', '\\"')

def build_html(is_standalone_offline=False):
    title_suffix = "Offline Interactive Edition" if is_standalone_offline else "3D Interactive Digital Visiting Card"
    badge_text = "💾 Offline 3D Edition • No Internet Needed" if is_standalone_offline else "✨ Official 3D Interactive Card"
    
    # Action buttons based on mode
    if is_standalone_offline:
        action_buttons = """
        <button class="btn btn-primary" onclick="toggleFlip()" title="Flip 180°">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"/></svg>
          <span>Flip Card</span>
        </button>
        <button class="btn btn-secondary" onclick="replayPopup()" title="Replay Pop-up">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/></svg>
          <span>Pop-up</span>
        </button>
        <button class="btn btn-secondary" onclick="downloadVCard()" title="Add to Contacts">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><line x1="19" y1="8" x2="19" y2="14"/><line x1="22" y1="11" x2="16" y2="11"/></svg>
          <span>Save Contact</span>
        </button>
        <a href="tel:+919676700488" class="btn btn-secondary" title="Call Now">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
          <span>Call</span>
        </a>
        <a href="https://wa.me/919676700488" target="_blank" rel="noopener" class="btn btn-secondary" title="WhatsApp Chat">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
          <span>WhatsApp</span>
        </a>
        <a href="https://www.vtkro.com/" target="_blank" rel="noopener" class="btn btn-secondary" title="Visit Website">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
          <span>vtkro.com</span>
        </a>
        """
    else:
        # Live website version
        action_buttons = """
        <button class="btn btn-primary" onclick="downloadCardFile()" title="Download Standalone 3D Card File">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          <span>Download Card File</span>
        </button>
        <button class="btn btn-secondary" onclick="toggleFlip()" title="Flip 180°">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"/></svg>
          <span>Flip Card</span>
        </button>
        <button class="btn btn-secondary" onclick="replayPopup()" title="Replay Pop-up">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/></svg>
          <span>Pop-up</span>
        </button>
        <button class="btn btn-secondary" onclick="downloadVCard()" title="Add to Contacts">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><line x1="19" y1="8" x2="19" y2="14"/><line x1="22" y1="11" x2="16" y2="11"/></svg>
          <span>Save Contact</span>
        </button>
        <a href="https://www.vtkro.com/" target="_blank" rel="noopener" class="btn btn-secondary" title="Visit Website">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
          <span>vtkro.com</span>
        </a>
        """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover" />
  <title>VTKRO | {title_suffix}</title>
  
  <meta name="description" content="VTKRO 3D Interactive Visiting Card. Authentic 360-degree rotation, dual front and encrypted QR back card. Built for local Indian businesses." />
  <meta property="og:title" content="VTKRO | 3D Interactive Digital Visiting Card" />
  <meta property="og:description" content="Click to view the 3D interactive VTKRO visiting card. 360-degree rotation, instant contact save, and encrypted QR gateway." />
  <meta property="og:type" content="website" />
  <meta name="theme-color" content="#020611" />

  <style>
    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
      user-select: none;
      -webkit-user-select: none;
    }}

    :root {{
      --bg-dark: #020611;
      --cyan-neon: #00e5ff;
      --cyan-glow: rgba(0, 229, 255, 0.45);
      --card-radius: 16px;
      --card-ratio: 1024 / 350; /* Authentic 1024x350 Business Card Proportion */
    }}

    html, body {{
      width: 100%;
      height: 100%;
      height: 100dvh;
      overflow: hidden;
      background-color: var(--bg-dark);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      position: relative;
      touch-action: none;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      background-image: 
        radial-gradient(circle at 50% 28%, rgba(0, 229, 255, 0.16) 0%, transparent 65%),
        radial-gradient(circle at 50% 80%, rgba(2, 132, 199, 0.14) 0%, transparent 60%),
        linear-gradient(180deg, #020611 0%, #060e22 50%, #02050e 100%);
    }}

    /* Subtle cyber background grid */
    .bg-grid {{
      position: absolute;
      inset: 0;
      background-size: 36px 36px;
      background-image: 
        linear-gradient(to right, rgba(255, 255, 255, 0.025) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255, 255, 255, 0.025) 1px, transparent 1px);
      pointer-events: none;
      z-index: 0;
    }}

    /* ─── TOP HEADER BAR ─── */
    .top-header {{
      position: absolute;
      top: 14px;
      left: 0;
      right: 0;
      z-index: 40;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0 20px;
      pointer-events: none;
    }}

    .brand-badge {{
      pointer-events: auto;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 14px;
      background: rgba(6, 16, 38, 0.75);
      border: 1px solid rgba(0, 229, 255, 0.3);
      border-radius: 999px;
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      color: #e2e8f0;
      font-size: 13px;
      font-weight: 500;
      letter-spacing: 0.3px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    }}

    .brand-dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background-color: var(--cyan-neon);
      box-shadow: 0 0 10px var(--cyan-neon);
      animation: pulseGlow 2s infinite ease-in-out;
    }}

    @keyframes pulseGlow {{
      0%, 100% {{ transform: scale(1); opacity: 0.85; }}
      50% {{ transform: scale(1.3); opacity: 1; box-shadow: 0 0 15px var(--cyan-neon); }}
    }}

    /* ─── 3D VIEWPORT ─── */
    .viewport-3d {{
      position: relative;
      z-index: 10;
      width: 100%;
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      perspective: 1100px;
      perspective-origin: 50% 50%;
      touch-action: none;
      cursor: grab;
    }}

    .viewport-3d:active {{
      cursor: grabbing;
    }}

    /* POP-UP ENTRANCE FROM BELOW TO ABOVE (ENLARGED FOR MOBILE COMFORT) */
    .stage-wrapper {{
      width: min(95vw, 660px);
      max-height: 52vh;
      display: flex;
      justify-content: center;
      align-items: center;
      transform-style: preserve-3d;
      -webkit-transform-style: preserve-3d;
      will-change: transform;
    }}

    .stage-wrapper.animating {{
      animation: popUpEntrance 1.25s cubic-bezier(0.16, 1.25, 0.3, 1) forwards;
    }}

    @keyframes popUpEntrance {{
      0% {{
        transform: translateY(115vh) rotateX(40deg) scale(0.65);
        opacity: 0;
      }}
      65% {{
        transform: translateY(-16px) rotateX(-5deg) scale(1.02);
        opacity: 1;
      }}
      85% {{
        transform: translateY(5px) rotateX(2deg) scale(0.995);
      }}
      100% {{
        transform: translateY(0) rotateX(0deg) scale(1);
        opacity: 1;
      }}
    }}

    /* ─── 3D CARD CONTAINER ─── */
    .card-3d {{
      width: 100%;
      aspect-ratio: var(--card-ratio);
      position: relative;
      transform-style: preserve-3d;
      -webkit-transform-style: preserve-3d;
      border-radius: var(--card-radius);
      will-change: transform;
    }}

    /* ─── CARD FACES (Front & Back - CLEAN BORDERLESS PROFESSIONAL DESIGN) ─── */
    .face {{
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      border-radius: var(--card-radius);
      backface-visibility: hidden;
      -webkit-backface-visibility: hidden;
      border: none;
      outline: none;
      background-color: transparent;
      box-shadow: 
        0 28px 55px rgba(0, 0, 0, 0.9),
        0 8px 22px rgba(0, 0, 0, 0.6);
      overflow: hidden;
    }}

    .face img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      border-radius: var(--card-radius);
      pointer-events: none;
      border: none;
      outline: none;
    }}

    /* FRONT FACE: Logo & Contact Image */
    .face-front {{
      transform: rotateY(0deg) translateZ(1.5px);
      -webkit-transform: rotateY(0deg) translateZ(1.5px);
    }}

    /* BACK FACE: QR Code Image */
    .face-back {{
      transform: rotateY(180deg) translateZ(1.5px);
      -webkit-transform: rotateY(180deg) translateZ(1.5px);
    }}

    /* ─── HIDDEN LIGHT SOURCE / SUBTLE SPECULAR REFLECTION ─── */
    .specular-sheen {{
      position: absolute;
      inset: 0;
      border-radius: var(--card-radius);
      pointer-events: none;
      z-index: 5;
      opacity: 0.16;
      mix-blend-mode: overlay;
      transition: opacity 0.25s ease;
      background: radial-gradient(
        circle at var(--light-x, 60%) var(--light-y, 35%),
        rgba(255, 255, 255, 0.95) 0%,
        rgba(0, 229, 255, 0.45) 25%,
        transparent 65%
      );
    }}

    .glint-band {{
      position: absolute;
      inset: 0;
      border-radius: var(--card-radius);
      pointer-events: none;
      z-index: 6;
      background: linear-gradient(
        var(--glint-angle, 125deg),
        transparent 35%,
        rgba(255, 255, 255, 0.2) 48%,
        rgba(0, 229, 255, 0.3) 50%,
        rgba(255, 255, 255, 0.15) 52%,
        transparent 65%
      );
      opacity: 0.12;
      transition: opacity 0.3s ease;
    }}

    /* Floor Reflection */
    .floor-reflection {{
      position: absolute;
      bottom: -45px;
      left: 10%;
      width: 80%;
      height: 30px;
      border-radius: 50%;
      background: radial-gradient(ellipse at center, rgba(0, 229, 255, 0.32) 0%, rgba(2, 132, 199, 0.08) 40%, transparent 75%);
      filter: blur(16px);
      transform: rotateX(80deg);
      pointer-events: none;
      transition: opacity 0.3s ease, transform 0.3s ease;
    }}

    /* ─── INTERACTION HINT PILL ─── */
    .hint-pill {{
      position: absolute;
      bottom: 84px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 30;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 14px;
      background: rgba(4, 12, 30, 0.65);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 999px;
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      color: rgba(226, 232, 240, 0.7);
      font-size: 12px;
      pointer-events: none;
      transition: opacity 0.6s ease, transform 0.6s ease;
    }}

    .hint-pill.hidden {{
      opacity: 0;
      transform: translateX(-50%) translateY(10px);
    }}

    /* ─── FLOATING ACTION BAR (CYBER GLASS DOCK) ─── */
    .action-dock {{
      position: absolute;
      bottom: 20px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 50;
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 8px 12px;
      background: rgba(4, 12, 30, 0.85);
      border: 1px solid rgba(0, 229, 255, 0.3);
      border-radius: 999px;
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      box-shadow: 
        0 10px 30px rgba(0, 0, 0, 0.8),
        0 0 20px rgba(0, 229, 255, 0.15);
      max-width: 95vw;
      overflow-x: auto;
      scrollbar-width: none;
    }}

    .action-dock::-webkit-scrollbar {{
      display: none;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 7px;
      padding: 9px 15px;
      border-radius: 999px;
      font-size: 13px;
      font-weight: 600;
      letter-spacing: 0.2px;
      text-decoration: none;
      cursor: pointer;
      border: none;
      outline: none;
      white-space: nowrap;
      transition: all 0.2s cubic-bezier(0.2, 0.8, 0.2, 1);
    }}

    .btn-primary {{
      background: linear-gradient(135deg, #00e5ff 0%, #0099ff 100%);
      color: #020611;
      box-shadow: 0 4px 14px rgba(0, 229, 255, 0.4);
    }}

    .btn-primary:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(0, 229, 255, 0.6);
      background: linear-gradient(135deg, #33ebff 0%, #1ab0ff 100%);
    }}

    .btn-primary:active {{
      transform: translateY(0);
      box-shadow: 0 2px 8px rgba(0, 229, 255, 0.4);
    }}

    .btn-secondary {{
      background: rgba(255, 255, 255, 0.07);
      color: #e2e8f0;
      border: 1px solid rgba(255, 255, 255, 0.12);
    }}

    .btn-secondary:hover {{
      background: rgba(255, 255, 255, 0.14);
      color: #ffffff;
      border-color: rgba(0, 229, 255, 0.4);
      transform: translateY(-2px);
    }}

    .btn-secondary:active {{
      transform: translateY(0);
    }}

    /* ─── TOAST NOTIFICATION ─── */
    .toast {{
      position: absolute;
      top: 65px;
      left: 50%;
      transform: translateX(-50%) translateY(-20px);
      z-index: 100;
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 10px 18px;
      background: rgba(6, 20, 48, 0.95);
      border: 1px solid var(--cyan-neon);
      border-radius: 12px;
      color: #ffffff;
      font-size: 13px;
      font-weight: 500;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.9), 0 0 15px var(--cyan-glow);
      opacity: 0;
      pointer-events: none;
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .toast.show {{
      opacity: 1;
      transform: translateX(-50%) translateY(0);
      pointer-events: auto;
    }}

    /* Mobile screens: Generous 100x70 proportions */
    @media (max-width: 600px) {{
      .stage-wrapper {{
        width: 92vw;
        max-width: 440px;
      }}
      :root {{
        --card-radius: 14px;
      }}
      .top-header {{
        padding: 0 12px;
      }}
      .brand-badge {{
        font-size: 11px;
        padding: 5px 10px;
      }}
      .action-dock {{
        bottom: 14px;
        padding: 6px 8px;
        gap: 6px;
      }}
      .btn {{
        padding: 8px 12px;
        font-size: 12px;
      }}
      .hint-pill {{
        bottom: 70px;
        font-size: 11px;
      }}
    }}

    /* Landscape mode on phones */
    @media (max-height: 500px) and (orientation: landscape) {{
      .stage-wrapper {{
        width: auto;
        height: 68vh;
        aspect-ratio: var(--card-ratio);
      }}
      .action-dock {{
        bottom: 8px;
        padding: 4px 8px;
      }}
      .hint-pill {{
        display: none;
      }}
    }}
  </style>
</head>
<body>

  <div class="bg-grid"></div>

  <!-- Top Brand Header -->
  <header class="top-header">
    <div class="brand-badge">
      <span class="brand-dot"></span>
      <strong>VTKRO</strong> &nbsp;|&nbsp; {badge_text}
    </div>
  </header>

  <!-- Notification Toast -->
  <div class="toast" id="toastBox">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#00e5ff" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
    <span id="toastMsg">VTKRO 3D Card downloaded successfully!</span>
  </div>

  <!-- 3D VIEWPORT (Captures swipes across the whole screen) -->
  <main class="viewport-3d" id="viewport3d">
    <!-- Pop-up Entrance Stage -->
    <div class="stage-wrapper animating" id="stageWrapper">
      <!-- 3D Card Object -->
      <div class="card-3d" id="card3d" role="region" aria-label="3D Interactive Visiting Card">

        <!-- FRONT FACE (Logo Image) -->
        <div class="face face-front">
          <img src="data:image/png;base64,{front_b64}" alt="VTKRO Visiting Card Front" draggable="false" />
          <div class="specular-sheen" id="sheenFront"></div>
          <div class="glint-band" id="glintFront"></div>
        </div>

        <!-- BACK FACE (QR Code Image) -->
        <div class="face face-back">
          <img src="data:image/png;base64,{back_b64}" alt="VTKRO Visiting Card Back QR" draggable="false" />
          <div class="specular-sheen" id="sheenBack"></div>
          <div class="glint-band" id="glintBack"></div>
        </div>

      </div>
    </div>

    <!-- Soft Ambient Floor Reflection -->
    <div class="floor-reflection" id="floorReflection"></div>
  </main>

  <!-- Interactive Gesture Guide Hint -->
  <div class="hint-pill" id="hintPill">
    <span>👆 Drag to rotate 360° • Tap to flip</span>
  </div>

  <!-- Floating Cyber Action Dock -->
  <nav class="action-dock" aria-label="Card Actions">
    {action_buttons}
  </nav>

  <script>
    /* ─────────────────────────────────────────────────────────────
       VTKRO 3D CARD PHYSICS, POP-UP ENTRANCE & INTERACTION ENGINE
       ───────────────────────────────────────────────────────────── */

    const viewport = document.getElementById('viewport3d');
    const card = document.getElementById('card3d');
    const stageWrapper = document.getElementById('stageWrapper');
    const floorReflect = document.getElementById('floorReflection');
    const hintPill = document.getElementById('hintPill');
    const toastBox = document.getElementById('toastBox');
    const toastMsg = document.getElementById('toastMsg');

    // 3D Euler rotation angles (degrees)
    let rotX = 0;
    let rotY = 0;
    
    // Inertia angular velocities
    let velX = 0;
    let velY = 0;
    let isDragging = false;
    let animationFrameId = null;
    let userHasInteracted = false;

    // Pointer gesture coordinates
    let pointerStartX = 0;
    let pointerStartY = 0;
    let lastPointerX = 0;
    let lastPointerY = 0;
    let lastTimestamp = 0;

    /* ─── 1. RENDER 3D TRANSFORM & HIDDEN LIGHT SPECULAR REFLECTION ─── */
    function updateCardTransform() {{
      card.style.transform = `rotateX(${{rotX.toFixed(2)}}deg) rotateY(${{rotY.toFixed(2)}}deg)`;

      // Dynamic floor shadow response
      const radX = (rotX * Math.PI) / 180;
      const shadowScale = Math.max(0.65, 1 - Math.abs(Math.sin(radX)) * 0.4);
      floorReflect.style.transform = `rotateX(80deg) scale(${{shadowScale.toFixed(2)}})`;

      // Hidden light source: virtual 3D point (upper right)
      const baseLightX = 65; // percentage
      const baseLightY = 30; // percentage

      // Specular highlight shifts across surface with tilt
      const shiftX = (rotY % 360) * 0.45;
      const shiftY = (rotX % 360) * 0.45;

      const currentLightX = Math.max(8, Math.min(92, baseLightX - shiftX));
      const currentLightY = Math.max(8, Math.min(92, baseLightY + shiftY));

      card.style.setProperty('--light-x', `${{currentLightX.toFixed(1)}}%`);
      card.style.setProperty('--light-y', `${{currentLightY.toFixed(1)}}%`);

      // Shimmer angle calculation
      const glintAngle = 120 + shiftX * 0.5;
      card.style.setProperty('--glint-angle', `${{glintAngle.toFixed(1)}}deg`);
    }}

    /* ─── 2. SCREEN-WIDE SWIPE IN ANY DIRECTION (TOUCH & MOUSE) ─── */
    viewport.addEventListener('pointerdown', (e) => {{
      isDragging = true;
      viewport.setPointerCapture(e.pointerId);
      card.style.transition = 'none';

      pointerStartX = e.clientX;
      pointerStartY = e.clientY;
      lastPointerX = e.clientX;
      lastPointerY = e.clientY;
      lastTimestamp = performance.now();
      velX = 0;
      velY = 0;

      if (!userHasInteracted) {{
        userHasInteracted = true;
        hintPill.classList.add('hidden');
      }}

      if (animationFrameId) {{
        cancelAnimationFrame(animationFrameId);
        animationFrameId = null;
      }}
    }});

    viewport.addEventListener('pointermove', (e) => {{
      if (!isDragging) return;

      const now = performance.now();
      const dt = Math.max(1, now - lastTimestamp);

      const deltaX = e.clientX - lastPointerX;
      const deltaY = e.clientY - lastPointerY;

      // Sensitivity factor tuned for comfortable mobile swiping
      const sensitivity = 0.55;

      rotY += deltaX * sensitivity;
      rotX -= deltaY * sensitivity;

      // Inertia velocity calculation
      velY = (deltaX / dt) * 9.0;
      velX = -(deltaY / dt) * 9.0;

      lastPointerX = e.clientX;
      lastPointerY = e.clientY;
      lastTimestamp = now;

      updateCardTransform();
    }});

    function handlePointerUp(e) {{
      if (!isDragging) return;
      isDragging = false;
      try {{
        viewport.releasePointerCapture(e.pointerId);
      }} catch (err) {{}}

      // Detect Tap (< 7px movement): Tap flips the card 180° smoothly
      const totalDist = Math.hypot(e.clientX - pointerStartX, e.clientY - pointerStartY);
      if (totalDist < 7) {{
        toggleFlip();
        return;
      }}

      // Otherwise, continue with momentum glide
      startMomentumLoop();
    }}

    viewport.addEventListener('pointerup', handlePointerUp);
    viewport.addEventListener('pointercancel', handlePointerUp);

    /* ─── 3. MOMENTUM / INERTIA PHYSICS LOOP ─── */
    function startMomentumLoop() {{
      const friction = 0.94; // Deceleration damping factor

      function step() {{
        if (isDragging) return;

        if (Math.abs(velX) > 0.04 || Math.abs(velY) > 0.04) {{
          rotX += velX;
          rotY += velY;

          velX *= friction;
          velY *= friction;

          updateCardTransform();
          animationFrameId = requestAnimationFrame(step);
        }} else {{
          velX = 0;
          velY = 0;
          animationFrameId = null;
        }}
      }}

      if (animationFrameId) cancelAnimationFrame(animationFrameId);
      animationFrameId = requestAnimationFrame(step);
    }}

    /* ─── 4. FLIP 180° (FRONT LOGO <-> BACK QR) ─── */
    function toggleFlip() {{
      if (!userHasInteracted) {{
        userHasInteracted = true;
        hintPill.classList.add('hidden');
      }}

      const normalizedY = ((rotY % 360) + 360) % 360;
      const isBackFacing = normalizedY > 90 && normalizedY < 270;
      const targetY = isBackFacing ? Math.round(rotY / 360) * 360 : (Math.floor(rotY / 360) * 360) + 180;

      animateToAngles(0, targetY, 600);
    }}

    function animateToAngles(targetX, targetY, duration = 600) {{
      if (animationFrameId) cancelAnimationFrame(animationFrameId);

      const startX = rotX;
      const startY = rotY;
      const startTime = performance.now();

      function ease(t) {{
        return 1 - Math.pow(1 - t, 3); // Cubic ease-out
      }}

      function animate(time) {{
        const elapsed = time - startTime;
        const progress = Math.min(1, elapsed / duration);
        const eased = ease(progress);

        rotX = startX + (targetX - startX) * eased;
        rotY = startY + (targetY - startY) * eased;

        updateCardTransform();

        if (progress < 1) {{
          animationFrameId = requestAnimationFrame(animate);
        }} else {{
          rotX = targetX;
          rotY = targetY;
          updateCardTransform();
          animationFrameId = null;
        }}
      }}

      animationFrameId = requestAnimationFrame(animate);
    }}

    /* ─── 5. REPLAY POP-UP ENTRANCE ANIMATION ─── */
    function replayPopup() {{
      rotX = 0;
      rotY = 0;
      updateCardTransform();

      stageWrapper.classList.remove('animating');
      void stageWrapper.offsetWidth; // Force CSS reflow
      stageWrapper.classList.add('animating');

      showToast("✨ Pop-up Animation triggered!");
    }}

    /* ─── 6. TOAST NOTIFICATION UTILITY ─── */
    let toastTimeout = null;
    function showToast(msg) {{
      if (!toastBox) return;
      toastMsg.textContent = msg;
      toastBox.classList.add('show');
      if (toastTimeout) clearTimeout(toastTimeout);
      toastTimeout = setTimeout(() => {{
        toastBox.classList.remove('show');
      }}, 3500);
    }}

    /* ─── 7. DOWNLOAD STANDALONE CARD FILE (.HTML) ─── */
    function downloadCardFile() {{
      showToast("📥 Downloading VTKRO-3D-Digital-Card.html...");

      // Attempt direct download link first
      const link = document.createElement('a');
      link.href = 'VTKRO-3D-Digital-Card.html';
      link.download = 'VTKRO-3D-Digital-Card.html';
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }}

    /* ─── 8. SAVE CONTACT VCARD (.VCF) ─── */
    function downloadVCard() {{
      showToast("📇 Downloading VTKRO Contact Card...");
      const vcfData = "{vcf_content}";
      const blob = new Blob([vcfData], {{ type: 'text/vcard;charset=utf-8' }});
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.download = 'VTKRO-Website-Builder.vcf';
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      setTimeout(() => URL.revokeObjectURL(url), 1000);
    }}

    /* ─── 9. CHECK URL PARAMETERS (?download=true) ─── */
    window.addEventListener('DOMContentLoaded', () => {{
      const params = new URLSearchParams(window.location.search);
      if (params.get('download') === 'true' || params.get('dl') === '1') {{
        setTimeout(downloadCardFile, 600);
      }}
    }});

    // Initial render
    updateCardTransform();
  </script>
</body>
</html>
"""
    return html

# Generate the standalone offline card
print("Building VTKRO-3D-Digital-Card.html (Standalone Offline Edition)...")
standalone_content = build_html(is_standalone_offline=True)
with open('VTKRO-3D-Digital-Card.html', 'w', encoding='utf-8') as f:
    f.write(standalone_content)
print(f"VTKRO-3D-Digital-Card.html generated! Size: {os.path.getsize('VTKRO-3D-Digital-Card.html')} bytes")

# Generate the live website index.html
print("Building index.html (Live Website Edition with Download action)...")
live_content = build_html(is_standalone_offline=False)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(live_content)
print(f"index.html generated! Size: {os.path.getsize('index.html')} bytes")

# Also mirror to vtkro-digital-card.html
with open('vtkro-digital-card.html', 'w', encoding='utf-8') as f:
    f.write(standalone_content)
print(f"vtkro-digital-card.html mirrored! Size: {os.path.getsize('vtkro-digital-card.html')} bytes")

print("All card files generated successfully!")
