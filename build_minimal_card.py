import base64
from PIL import Image

# Read 100x70 normalized images for base64 offline embedding
with open('card_front_normalized.png', 'rb') as f:
    front_b64 = 'data:image/png;base64,' + base64.b64encode(f.read()).decode('ascii')

with open('card_back_normalized.png', 'rb') as f:
    back_b64 = 'data:image/png;base64,' + base64.b64encode(f.read()).decode('ascii')

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover" />
  <title>VTKRO | 3D Interactive Digital Visiting Card</title>
  
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
      align-items: center;
      justify-content: center;
      position: relative;
      touch-action: none;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background-image: 
        radial-gradient(circle at 50% 30%, rgba(0, 229, 255, 0.14) 0%, transparent 65%),
        radial-gradient(circle at 50% 80%, rgba(2, 132, 199, 0.12) 0%, transparent 60%),
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

    /* Mobile screens: Generous 100x70 proportions */
    @media (max-width: 600px) {{
      .stage-wrapper {{
        width: 90vw;
        max-width: 420px;
      }}
      :root {{
        --card-radius: 16px;
      }}
    }}

    /* Landscape mode on phones */
    @media (max-height: 500px) and (orientation: landscape) {{
      .stage-wrapper {{
        width: auto;
        height: 75vh;
        aspect-ratio: var(--card-ratio);
      }}
    }}
  </style>
</head>
<body>

  <div class="bg-grid"></div>

  <!-- 3D VIEWPORT (Captures swipes across the whole screen) -->
  <main class="viewport-3d" id="viewport3d">
    <!-- Pop-up Entrance Stage -->
    <div class="stage-wrapper" id="stageWrapper">
      <!-- 3D Card Object -->
      <div class="card-3d" id="card3d" role="region" aria-label="3D Interactive Visiting Card">

        <!-- FRONT FACE (Logo Image) -->
        <div class="face face-front">
          <img src="card_front_normalized.png" onerror="this.src='{front_b64}'" alt="VTKRO Visiting Card Front" draggable="false" />
          <div class="specular-sheen" id="sheenFront"></div>
          <div class="glint-band" id="glintFront"></div>
        </div>

        <!-- BACK FACE (QR Code Image) -->
        <div class="face face-back">
          <img src="card_back_normalized.png" onerror="this.src='{back_b64}'" alt="VTKRO Visiting Card Back QR" draggable="false" />
          <div class="specular-sheen" id="sheenBack"></div>
          <div class="glint-band" id="glintBack"></div>
        </div>

      </div>
    </div>

    <!-- Soft Ambient Floor Reflection -->
    <div class="floor-reflection" id="floorReflection"></div>
  </main>

  <script>
    /* ─────────────────────────────────────────────────────────────
       360° MULTI-AXIS MOBILE SWIPE & ROTATION PHYSICS ENGINE
       Clean, comfortable swipe interaction designed for any mobile
       ───────────────────────────────────────────────────────────── */

    const viewport = document.getElementById('viewport3d');
    const card = document.getElementById('card3d');
    const floorReflect = document.getElementById('floorReflection');

    // 3D Euler rotation angles (degrees)
    let rotX = 0;
    let rotY = 0;
    
    // Inertia angular velocities
    let velX = 0;
    let velY = 0;
    let isDragging = false;
    let animationFrameId = null;

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

print("Successfully updated with 100x70 proportion!")
