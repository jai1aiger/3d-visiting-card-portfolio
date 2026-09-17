import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import io
import re
import resvg_py
import qrcode

# 1. Load the original full image (1536 x 1024)
full_img = cv2.imread('WhatsApp Image 2026-09-15 at 8.58.29 PM.jpeg')

# 2. Extract and clean the Front card (y: 52 to 522, x: 216 to 1324)
front_card = full_img[52:522, 216:1324].copy()

# Seamless clone to erase "NMAE :-" cleanly
strip_source = front_card[75:115, 835:1015].copy()
mask = np.ones((40, 180), dtype=np.uint8) * 255
center = (655 + 90, 75 + 20)
front_card_clean = cv2.seamlessClone(strip_source, front_card, mask, center, cv2.NORMAL_CLONE)

# 3. Dual Call + WhatsApp glowing icon
def get_dual_call_wa_icon(size=(60, 40)):
    scale = 4
    w, h = size[0] * scale, size[1] * scale
    svg_dual = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="-4 -4 46 28" width="{w}" height="{h}" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <g transform="translate(0, 0)">
        <path d="M4 3h3.5l1.8 4.2l-2.2 1.3a9.5 9.5 0 0 0 4.3 4.3l1.3 -2.2l4.2 1.8v3.5a1.8 1.8 0 0 1 -1.8 1.8a14 14 0 0 1 -13 -13a1.8 1.8 0 0 1 1.8 -1.8" />
      </g>
      <g transform="translate(19, 0)">
        <path d="M2.5 17.5l1.4 -3.2a7.5 7.5 0 1 1 2.8 2.4l-4.2 .8" />
        <path d="M7.5 8.5a.4 .4 0 0 0 .8 0v-.8a.4 .4 0 0 0 -.8 0v.8a4 4 0 0 0 4 4h.8a.4 .4 0 0 0 0 -.8h-.8a.4 .4 0 0 0 0 .8" />
      </g>
    </svg>""".format(w=w, h=h)
    
    sg2 = re.sub(r'stroke="[^"]*"', 'stroke="#0055ff"', svg_dual)
    sg2 = re.sub(r'stroke-width="[^"]*"', 'stroke-width="7.0"', sg2)
    im_g2 = Image.open(io.BytesIO(resvg_py.svg_to_bytes(sg2))).convert('RGBA').filter(ImageFilter.GaussianBlur(radius=5))
    
    sg1 = re.sub(r'stroke="[^"]*"', 'stroke="#00b4d8"', svg_dual)
    sg1 = re.sub(r'stroke-width="[^"]*"', 'stroke-width="3.5"', sg1)
    im_g1 = Image.open(io.BytesIO(resvg_py.svg_to_bytes(sg1))).convert('RGBA').filter(ImageFilter.GaussianBlur(radius=2.5))
    
    sc = re.sub(r'stroke="[^"]*"', 'stroke="#00e5ff"', svg_dual)
    sc = re.sub(r'stroke-width="[^"]*"', 'stroke-width="1.8"', sc)
    im_c = Image.open(io.BytesIO(resvg_py.svg_to_bytes(sc))).convert('RGBA')

    sh = re.sub(r'stroke="[^"]*"', 'stroke="#e0ffff"', svg_dual)
    sh = re.sub(r'stroke-width="[^"]*"', 'stroke-width="0.7"', sh)
    im_h = Image.open(io.BytesIO(resvg_py.svg_to_bytes(sh))).convert('RGBA')

    comp = Image.alpha_composite(im_g2, im_g1)
    comp = Image.alpha_composite(comp, im_c)
    comp = Image.alpha_composite(comp, im_h)
    return comp.resize(size, Image.Resampling.LANCZOS)

icon_dual = get_dual_call_wa_icon((60, 40))

# 4. Build Front Card Image
front_pil = Image.fromarray(cv2.cvtColor(front_card_clean, cv2.COLOR_BGR2RGB))
draw_front = ImageDraw.Draw(front_pil)
font_phone = ImageFont.truetype('Poppins-Medium.ttf', 26)

# Paste icon and render "+91 9676700488"
front_pil.paste(icon_dual, (675, 76), icon_dual)
draw_front.text((751, 80), '+91 9676700488', fill=(255, 255, 255), font=font_phone)

# Save Front Card standalone
front_pil.save('VTKRO_Card_Front.png', quality=95)
front_pil.save('VTKRO_Card_Front.jpg', quality=95)

# Also generate variant with 9676700488 (without +91)
front_pil_local = Image.fromarray(cv2.cvtColor(front_card_clean, cv2.COLOR_BGR2RGB))
draw_front_local = ImageDraw.Draw(front_pil_local)
front_pil_local.paste(icon_dual, (675, 76), icon_dual)
draw_front_local.text((751, 80), '9676700488', fill=(255, 255, 255), font=font_phone)
front_pil_local.save('VTKRO_Card_Front_LocalNum.png', quality=95)

# 5. Build Back Card with scannable QR
back_card = full_img[548:968, 216:1324].copy()

# Generate real scannable QR code for WhatsApp & Direct Contact
qr_wa = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=1,
)
qr_wa.add_data("https://wa.me/919676700488")
qr_wa.make(fit=True)
qr_wa_img = qr_wa.make_image(fill_color="black", back_color="white").convert('RGB')
qr_wa_resized = qr_wa_img.resize((275, 275), Image.Resampling.LANCZOS)

back_pil = Image.fromarray(cv2.cvtColor(back_card, cv2.COLOR_BGR2RGB))
# Center QR box in card: x center = 656, y center = 196
top_left_x = 656 - 275//2
top_left_y = 196 - 275//2
back_pil.paste(qr_wa_resized, (top_left_x, top_left_y))

# Save Back Card standalone
back_pil.save('VTKRO_Card_Back.png', quality=95)
back_pil.save('VTKRO_Card_Back.jpg', quality=95)

# Also generate a vCard version of the back card
vcard_data = """BEGIN:VCARD\nVERSION:3.0\nFN:VTKRO - Virtual Tour Kro\nORG:VTKRO\nTEL;TYPE=CELL,VOICE,PREF:+919676700488\nEMAIL:Vtkro@gmail.com\nURL:https://vtkro.com\nADR;TYPE=WORK:;;Chattisgarh;;;;\nEND:VCARD"""
qr_vc = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=10, border=1)
qr_vc.add_data(vcard_data)
qr_vc.make(fit=True)
qr_vc_img = qr_vc.make_image(fill_color="black", back_color="white").convert('RGB').resize((275, 275), Image.Resampling.LANCZOS)
back_pil_vc = Image.fromarray(cv2.cvtColor(back_card, cv2.COLOR_BGR2RGB))
back_pil_vc.paste(qr_vc_img, (top_left_x, top_left_y))
back_pil_vc.save('VTKRO_Card_Back_vCard.png', quality=95)

# 6. Composite into the Full Showcase Image (1536 x 1024)
showcase_pil = Image.fromarray(cv2.cvtColor(full_img, cv2.COLOR_BGR2RGB))
# Paste updated front card
showcase_pil.paste(front_pil, (216, 52))
# Paste updated back card (with scannable WhatsApp QR)
showcase_pil.paste(back_pil, (216, 548))

showcase_pil.save('VTKRO_Visiting_Card_Showcase.png', quality=95)
showcase_pil.save('VTKRO_Visiting_Card_Showcase.jpg', quality=95)

# Also copy to artifact directory for presentation
import shutil
artifact_dir = r'C:\Users\pedin\.gemini\antigravity\brain\0cf0f430-9f01-4a49-a663-42e700cf275d'
shutil.copy('VTKRO_Visiting_Card_Showcase.png', f'{artifact_dir}/VTKRO_Visiting_Card_Showcase.png')
shutil.copy('VTKRO_Card_Front.png', f'{artifact_dir}/VTKRO_Card_Front.png')
shutil.copy('VTKRO_Card_Back.png', f'{artifact_dir}/VTKRO_Card_Back.png')

print('All deliverables created successfully!')
