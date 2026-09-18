import base64
import os

# Read front and back images and encode to base64
front_path = 'vtkro-card-front.jpg'
back_path = 'vtkro-card-back-white.png'

with open(front_path, 'rb') as f:
    front_b64 = 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode('ascii')

with open(back_path, 'rb') as f:
    back_b64 = 'data:image/png;base64,' + base64.b64encode(f.read()).decode('ascii')

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <title>VTKRO | 360° Interactive 3D Digital Visiting Card</title>
  <meta name="description" content="Official 3D Interactive Digital Visiting Card for VTKRO - Virtual Tour Kro. 360° free rotation from any direction, smooth pop-up entrance, subtle hidden light reflection, and executive white back." />

  <style>
    /* ─── RESET & ROOT THEME TOKENS ─── */
    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }}

    :root {{
      --bg-dark: #030712;
      --cyan-neon: #00e5ff;
      --cyan-glow: rgba(0, 229, 255, 0.4);
      --card-radius: 18px;
      --card-ratio: 90 / 50; /* 1.8 : 1 ISO/Indian Standard Aspect Ratio */
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
    }}

    body {{
      background-color: var(--bg-dark);
      color: var(--text-main);
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
      min-height: 100vh;
      min-height: 100dvh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: space-between;
      overflow-x: hidden;
      padding: 16px 12px;
      position: relative;
      touch-action: pan-y;
      background-image: 
        radial-gradient(circle at 50% 15%, rgba(0, 229, 255, 0.09) 0%, transparent 60%),
        radial-gradient(circle at 80% 85%, rgba(2, 132, 199, 0.08) 0%, transparent 55%),
        linear-gradient(180deg, #030712 0%, #081024 50%, #02050f 100%);
    }}

    /* Subtle background cyber grid */
    .bg-grid {{
      position: fixed;
      inset: 0;
      background-size: 36px 36px;
      background-image: 
        linear-gradient(to right, rgba(255, 255, 255, 0.02) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
      pointer-events: none;
      z-index: 0;
    }}

    /* ─── HEADER BAR ─── */
    .header {{
      position: relative;
      z-index: 10;
      text-align: center;
      max-width: 600px;
      margin-bottom: 8px;
    }}

    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 13px;
      border-radius: 999px;
      background: rgba(0, 229, 255, 0.1);
      border: 1px solid rgba(0, 229, 255, 0.35);
      color: var(--cyan-neon);
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      margin-bottom: 6px;
      box-shadow: 0 0 14px rgba(0, 229, 255, 0.2);
    }}

    .badge-dot {{
      width: 6px;
      height: 6px;
      background: var(--cyan-neon);
      border-radius: 50%;
      box-shadow: 0 0 8px var(--cyan-neon);
      animation: pulseDot 2s infinite ease-in-out;
    }}

    @keyframes pulseDot {{
      0%, 100% {{ opacity: 1; transform: scale(1); }}
      50% {{ opacity: 0.35; transform: scale(0.75); }}
    }}

    .title {{
      font-size: clamp(22px, 5vw, 32px);
      font-weight: 800;
      letter-spacing: -0.02em;
      background: linear-gradient(135deg, #ffffff 40%, #7dd3fc 75%, #00e5ff 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 3px;
    }}

    .subtitle {{
      color: var(--text-muted);
      font-size: clamp(12px, 2.5vw, 13px);
      line-height: 1.4;
    }}

    /* ─── 3D VIEWPORT & STAGE ─── */
    .viewport-3d {{
      position: relative;
      z-index: 10;
      width: 100%;
      max-width: 580px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      perspective: 1400px;
      perspective-origin: 50% 50%;
      margin: 12px 0 20px 0;
      user-select: none;
      -webkit-user-select: none;
    }}

    /* POP-UP FROM BELOW TO ABOVE ENTRANCE ANIMATION */
    .stage-wrapper {{
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      transform-style: preserve-3d;
      will-change: transform, opacity;
      animation: popUpEntrance 1.25s cubic-bezier(0.16, 1.25, 0.3, 1) forwards;
    }}

    @keyframes popUpEntrance {{
      0% {{
        transform: translateY(115vh) rotateX(45deg) scale(0.65);
        opacity: 0;
      }}
      65% {{
        transform: translateY(-15px) rotateX(-5deg) scale(1.02);
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

    /* ─── 3D CARD OBJECT ─── */
    .card-3d {{
      width: 100%;
      aspect-ratio: var(--card-ratio);
      position: relative;
      transform-style: preserve-3d;
      cursor: grab;
      touch-action: none;
      border-radius: var(--card-radius);
      will-change: transform;
      filter: drop-shadow(0 25px 35px rgba(0, 0, 0, 0.88)) drop-shadow(0 0 20px rgba(0, 229, 255, 0.15));
    }}

    .card-3d:active {{
      cursor: grabbing;
    }}

    /* ─── CARD FACES (Front & Back) ─── */
    .face {{
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      border-radius: var(--card-radius);
      backface-visibility: hidden;
      -webkit-backface-visibility: hidden;
      overflow: hidden;
      transform-style: preserve-3d;
    }}

    /* FRONT FACE: Cyber Blue VTKRO (Uploaded Image) */
    .face-front {{
      transform: translateZ(2px);
      background: #020712;
      border: 1.5px solid rgba(0, 229, 255, 0.45);
      box-shadow: inset 0 0 20px rgba(0, 229, 255, 0.2);
    }}

    .face-front img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      border-radius: inherit;
    }}

    /* BACK FACE: Pure Luxury Executive White */
    .face-back {{
      transform: rotateY(180deg) translateZ(2px);
      background: #ffffff;
      border: 1.5px solid rgba(203, 213, 225, 0.85);
      box-shadow: 
        inset 0 0 25px rgba(0, 0, 0, 0.03),
        0 10px 25px rgba(0, 0, 0, 0.12);
    }}

    .face-back img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      border-radius: inherit;
    }}

    /* ─── 3D CARD THICKNESS / CORE DEPTH ─── */
    .card-edge {{
      position: absolute;
      inset: 0;
      border-radius: var(--card-radius);
      pointer-events: none;
      backface-visibility: hidden;
    }}
    .edge-layer-1 {{
      transform: translateZ(1px);
      background: rgba(255, 255, 255, 0.4);
      border: 1px solid rgba(0, 229, 255, 0.3);
    }}
    .edge-layer-2 {{
      transform: translateZ(0px);
      background: #e2e8f0;
      border: 1.5px solid #cbd5e1;
    }}
    .edge-layer-3 {{
      transform: translateZ(-1px);
      background: rgba(255, 255, 255, 0.5);
      border: 1px solid rgba(0, 229, 255, 0.2);
    }}

    /* ─── HIDDEN LIGHT SOURCE / SUBTLE SPECULAR SHEEN ─── */
    .specular-sheen {{
      position: absolute;
      inset: 0;
      border-radius: inherit;
      pointer-events: none;
      z-index: 5;
      opacity: 0.15; /* Subtle reflection only */
      mix-blend-mode: overlay;
      transition: opacity 0.25s ease;
      background: radial-gradient(
        circle at var(--light-x, 60%) var(--light-y, 35%),
        rgba(255, 255, 255, 0.95) 0%,
        rgba(0, 229, 255, 0.45) 25%,
        transparent 65%
      );
    }}

    .face-back .specular-sheen {{
      mix-blend-mode: soft-light;
      opacity: 0.18; /* Subtle glossy pearlescent sheen on white back */
      background: radial-gradient(
        circle at var(--light-x, 60%) var(--light-y, 35%),
        rgba(255, 255, 255, 1) 0%,
        rgba(2, 132, 199, 0.25) 30%,
        transparent 65%
      );
    }}

    /* Subtle glint band */
    .glint-band {{
      position: absolute;
      inset: 0;
      border-radius: inherit;
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
      bottom: -40px;
      left: 10%;
      width: 80%;
      height: 25px;
      border-radius: 50%;
      background: radial-gradient(ellipse at center, rgba(0, 229, 255, 0.26) 0%, rgba(2, 132, 199, 0.08) 40%, transparent 75%);
      filter: blur(12px);
      transform: rotateX(80deg);
      pointer-events: none;
      transition: opacity 0.3s ease, transform 0.3s ease;
    }}

    /* Mini gesture helper tag */
    .gesture-indicator {{
      display: inline-flex;
      align-items: center;
      gap: 7px;
      margin-top: 14px;
      padding: 5px 14px;
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid rgba(0, 229, 255, 0.25);
      border-radius: 20px;
      font-size: 11.5px;
      color: var(--text-muted);
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
      backdrop-filter: blur(8px);
    }}

    .gesture-indicator span {{
      color: var(--cyan-neon);
      font-weight: 600;
    }}

    /* ─── ACTION TOOLBAR ─── */
    .toolbar {{
      position: relative;
      z-index: 10;
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      justify-content: center;
      max-width: 620px;
      width: 100%;
      margin-top: 6px;
      margin-bottom: 12px;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 7px;
      padding: 9px 16px;
      border-radius: 30px;
      font-size: 12.5px;
      font-weight: 600;
      color: #ffffff;
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid rgba(0, 229, 255, 0.35);
      backdrop-filter: blur(12px);
      cursor: pointer;
      text-decoration: none;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
      user-select: none;
    }}

    .btn:hover {{
      background: rgba(0, 229, 255, 0.15);
      border-color: var(--cyan-neon);
      box-shadow: 0 0 16px rgba(0, 229, 255, 0.4);
      transform: translateY(-2px);
      color: #ffffff;
    }}

    .btn:active {{
      transform: translateY(0);
    }}

    .btn-primary {{
      background: linear-gradient(135deg, #0284c7 0%, #00e5ff 100%);
      border: none;
      color: #030712;
      font-weight: 700;
      box-shadow: 0 0 20px rgba(0, 229, 255, 0.4);
    }}

    .btn-primary:hover {{
      box-shadow: 0 0 28px rgba(0, 229, 255, 0.7);
      transform: translateY(-2px);
      color: #030712;
    }}

    .btn-icon {{
      font-size: 14px;
      line-height: 1;
    }}

    /* ─── QUICK SPECS SUMMARY PILL ─── */
    .specs-pill {{
      position: relative;
      z-index: 10;
      display: flex;
      align-items: center;
      justify-content: space-around;
      width: 100%;
      max-width: 580px;
      background: rgba(10, 18, 36, 0.65);
      border: 1px solid rgba(0, 229, 255, 0.18);
      border-radius: 12px;
      padding: 10px 16px;
      margin-top: 4px;
      font-size: 11.5px;
      color: var(--text-muted);
      backdrop-filter: blur(10px);
    }}

    .spec-item {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .spec-item b {{
      color: #e2e8f0;
    }}

    /* Mobile adjustments */
    @media (max-width: 480px) {{
      body {{
        padding: 12px 8px;
      }}
      .btn {{
        padding: 8px 12px;
        font-size: 11.5px;
      }}
      .specs-pill {{
        flex-direction: column;
        gap: 5px;
        text-align: center;
      }}
    }}
  </style>
</head>
<body>

  <div class="bg-grid"></div>

  <!-- HEADER -->
  <header class="header">
    <div class="badge">
      <span class="badge-dot"></span>
      360° Interactive 3D Card
    </div>
    <h1 class="title">VTKRO Visiting Card</h1>
    <p class="subtitle">Drag in any direction to spin 360° • Tap or click to flip front & white back</p>
  </header>

  <!-- 3D VIEWPORT -->
  <main class="viewport-3d" id="viewport3d">
    <!-- Pop-up Entrance Stage Wrapper -->
    <div class="stage-wrapper" id="stageWrapper">
      <!-- 3D Card Object -->
      <div class="card-3d" id="card3d" role="region" aria-label="3D Interactive Visiting Card">
        
        <!-- Physical 3D Thickness Edge Layers -->
        <div class="card-edge edge-layer-1"></div>
        <div class="card-edge edge-layer-2"></div>
        <div class="card-edge edge-layer-3"></div>

        <!-- FRONT FACE: Cyber Dark VTKRO (Uploaded Card Graphic) -->
        <div class="face face-front">
          <div class="specular-sheen" id="sheenFront"></div>
          <div class="glint-band" id="glintFront"></div>
          <img src="vtkro-card-front.jpg" onerror="this.src='{front_b64}'" alt="VTKRO Visiting Card Front" draggable="false" />
        </div>

        <!-- BACK FACE: Pristine Executive White -->
        <div class="face face-back">
          <div class="specular-sheen" id="sheenBack"></div>
          <div class="glint-band" id="glintBack"></div>
          <img src="vtkro-card-back-white.png" onerror="this.src='{back_b64}'" alt="VTKRO Visiting Card White Back" draggable="false" />
        </div>

      </div>
    </div>

    <!-- Dynamic Soft Floor Shadow & Reflection -->
    <div class="floor-reflection" id="floorReflection"></div>

    <!-- Quick Interaction Guide -->
    <div class="gesture-indicator">
      <span>✋ Drag:</span> 360° In Any Direction &nbsp;|&nbsp; <span>👆 Tap:</span> Flip Front / White Back
    </div>
  </main>

  <!-- ACTION CONTROLS TOOLBAR -->
  <nav class="toolbar" aria-label="Card Controls">
    <button class="btn btn-primary" id="btnFlip" onclick="toggleFlip()">
      <span class="btn-icon">🔄</span> Flip 180°
    </button>
    <button class="btn" id="btnOrbit" onclick="toggleAutoOrbit()">
      <span class="btn-icon">✨</span> <span id="orbitText">Auto 360°</span>
    </button>
    <button class="btn" onclick="resetOrientation()">
      <span class="btn-icon">🎯</span> Reset View
    </button>
    <button class="btn" onclick="triggerPopUp()">
      <span class="btn-icon">🎬</span> Replay Pop-Up
    </button>
    <a class="btn" href="https://wa.me/919676700488?text=Hi%20VTKRO,%20I%20am%20interested%20in%20building%20a%20website" target="_blank" rel="noopener noreferrer">
      <span class="btn-icon">💬</span> WhatsApp
    </a>
    <a class="btn" href="tel:+919676700488">
      <span class="btn-icon">📞</span> Call
    </a>
    <button class="btn" onclick="downloadVCard()">
      <span class="btn-icon">📲</span> Save vCard
    </button>
    <button class="btn" onclick="shareCard()">
      <span class="btn-icon">🔗</span> Share
    </button>
  </nav>

  <!-- SPECIFICATIONS FOOTER -->
  <footer class="specs-pill">
    <div class="spec-item">Standard: <b>90 × 50 mm (1.80 : 1)</b></div>
    <div class="spec-item">Front: <b>Cybernetic Glow</b></div>
    <div class="spec-item">Back: <b>Pristine White</b></div>
    <div class="spec-item">Light: <b>Subtle Hidden Specular</b></div>
  </footer>

  <script>
    /* ─────────────────────────────────────────────────────────────
       360° MULTI-AXIS ROTATION & PHYSICS ENGINE
       Runs 100% offline on any browser and device without dependencies
       ───────────────────────────────────────────────────────────── */

    const card = document.getElementById('card3d');
    const stage = document.getElementById('stageWrapper');
    const floorReflect = document.getElementById('floorReflection');
    const orbitText = document.getElementById('orbitText');

    // 3D Euler angles (degrees)
    let rotX = 0;
    let rotY = 0;
    
    // Angular velocities for momentum gliding
    let velX = 0;
    let velY = 0;
    let isDragging = false;
    let isOrbiting = false;
    let animationFrameId = null;

    // Pointer coordinates & tap tracking
    let pointerStartX = 0;
    let pointerStartY = 0;
    let lastPointerX = 0;
    let lastPointerY = 0;
    let lastTimestamp = 0;

    /* ─── 1. POP-UP ENTRANCE ANIMATION ─── */
    function triggerPopUp() {{
      stage.style.animation = 'none';
      void stage.offsetWidth; // Force CSS reflow
      stage.style.animation = 'popUpEntrance 1.25s cubic-bezier(0.16, 1.25, 0.3, 1) forwards';
    }}

    /* ─── 2. 3D TRANSFORM & HIDDEN LIGHT SPECULAR REFLECTION ─── */
    function updateCardTransform() {{
      // Update 3D orientation
      card.style.transform = `rotateX(${{rotX.toFixed(2)}}deg) rotateY(${{rotY.toFixed(2)}}deg)`;

      // Dynamic floor shadow response
      const radX = (rotX * Math.PI) / 180;
      const shadowScale = Math.max(0.65, 1 - Math.abs(Math.sin(radX)) * 0.4);
      floorReflect.style.transform = `rotateX(80deg) scale(${{shadowScale.toFixed(2)}})`;

      // Hidden light source: virtual position in 3D upper-right
      const baseLightX = 65; // percentage
      const baseLightY = 30; // percentage

      // Specular highlight shifts across the surface as the card rotates
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

    /* ─── 3. POINTER DRAG & 360° ROTATION (TOUCH & MOUSE) ─── */
    card.addEventListener('pointerdown', (e) => {{
      isDragging = true;
      isOrbiting = false;
      orbitText.textContent = 'Auto 360°';
      
      card.setPointerCapture(e.pointerId);
      card.style.transition = 'none';

      pointerStartX = e.clientX;
      pointerStartY = e.clientY;
      lastPointerX = e.clientX;
      lastPointerY = e.clientY;
      lastTimestamp = performance.now();
      velX = 0;
      velY = 0;

      if (animationFrameId) {{
        cancelAnimationFrame(animationFrameId);
        animationFrameId = null;
      }}
    }});

    card.addEventListener('pointermove', (e) => {{
      if (!isDragging) return;

      const now = performance.now();
      const dt = Math.max(1, now - lastTimestamp);

      const deltaX = e.clientX - lastPointerX;
      const deltaY = e.clientY - lastPointerY;

      // Sensitivity factor for fluid 360-degree rotation in any direction
      const sensitivity = 0.52;

      rotY += deltaX * sensitivity;
      rotX -= deltaY * sensitivity;

      // Angular velocity calculation for inertia
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
        card.releasePointerCapture(e.pointerId);
      }} catch (err) {{}}

      // Detect Tap / Click (< 7px movement): Tap flips the card!
      const totalDist = Math.hypot(e.clientX - pointerStartX, e.clientY - pointerStartY);
      if (totalDist < 7) {{
        toggleFlip();
        return;
      }}

      // Otherwise, start momentum inertia glide
      startMomentumLoop();
    }}

    card.addEventListener('pointerup', handlePointerUp);
    card.addEventListener('pointercancel', handlePointerUp);

    /* ─── 4. MOMENTUM / INERTIA PHYSICS LOOP ─── */
    function startMomentumLoop() {{
      const friction = 0.94; // Deceleration damping factor

      function step() {{
        if (isDragging) return;

        if (isOrbiting) {{
          rotY += 0.85; // Continuous auto showcase rotation
          updateCardTransform();
          animationFrameId = requestAnimationFrame(step);
          return;
        }}

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

    /* ─── 5. FLIP 180° BETWEEN FRONT & WHITE BACK ─── */
    function toggleFlip() {{
      isOrbiting = false;
      orbitText.textContent = 'Auto 360°';

      // Find current side and calculate closest opposite side
      const normalizedY = ((rotY % 360) + 360) % 360;
      const isBackFacing = normalizedY > 90 && normalizedY < 270;

      const targetY = isBackFacing ? Math.round(rotY / 360) * 360 : (Math.floor(rotY / 360) * 360) + 180;
      
      animateToAngles(0, targetY, 650);
    }}

    /* ─── 6. AUTO 360° SHOWCASE ORBIT ─── */
    function toggleAutoOrbit() {{
      isOrbiting = !isOrbiting;
      orbitText.textContent = isOrbiting ? 'Stop Orbit' : 'Auto 360°';

      if (isOrbiting) {{
        velX = 0;
        velY = 0;
        startMomentumLoop();
      }}
    }}

    /* ─── 7. RESET ORIENTATION ─── */
    function resetOrientation() {{
      isOrbiting = false;
      orbitText.textContent = 'Auto 360°';
      animateToAngles(0, 0, 700);
    }}

    function animateToAngles(targetX, targetY, duration = 650) {{
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

    /* ─── 8. VCARD GENERATION & DIRECT DOWNLOAD ─── */
    function downloadVCard() {{
      const vcardData = 
`BEGIN:VCARD
VERSION:3.0
N:Support;VTKRO;;;
FN:VTKRO Support
ORG:VTKRO - Virtual Tour Kro
TITLE:Virtual Tour Kro & Affordable Web Solutions
TEL;TYPE=CELL,VOICE,PREF:+919676700488
EMAIL;TYPE=INTERNET,WORK:Vtkro@gmail.com
URL:https://vtkro.com
URL;TYPE=PORTFOLIO:https://portfolio.vtkro.com/
ADR;TYPE=WORK:;;Chattisgarh;;;;India
NOTE:India's Most Affordable Website Builder. Flat ₹5,000 One-Time • Zero Subscriptions • Lifetime Hosting.
END:VCARD`;

      const blob = new Blob([vcardData], {{ type: 'text/vcard;charset=utf-8;' }});
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.download = 'VTKRO_Contact.vcf';
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      URL.revokeObjectURL(url);
    }}

    /* ─── 9. WEB SHARE / CLIPBOARD LINK ─── */
    function shareCard() {{
      if (navigator.share) {{
        navigator.share({{
          title: 'VTKRO 3D Visiting Card',
          text: 'VTKRO - Virtual Tour Kro: India\\'s Most Affordable Website Builder (Zero Subscriptions).',
          url: window.location.href
        }}).catch(() => {{}});
      }} else {{
        navigator.clipboard.writeText(window.location.href);
        alert('Visiting Card link copied to clipboard!');
      }}
    }}

    // Initial render
    updateCardTransform();
  </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

with open('vtkro-digital-card.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Successfully generated finalized index.html and vtkro-digital-card.html!")
