import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

w, h = 1024, 571
img = Image.new('RGBA', (w, h), (255, 255, 255, 255))
draw = ImageDraw.Draw(img)

# Luxury white card border
draw.rounded_rectangle([16, 16, w-16, h-16], radius=24, outline=(226, 232, 240, 255), width=2)
draw.rounded_rectangle([22, 22, w-22, h-22], radius=20, outline=(241, 245, 249, 255), width=1)

# Subtle metallic cyan accent line at top
draw.line([(60, 20), (w-60, 20)], fill=(0, 180, 255, 200), width=3)

# Load logo
if os.path.exists('vtkro-official-logo.png'):
    logo = Image.open('vtkro-official-logo.png').convert('RGBA')
    lw = 240
    lh = int(lw * logo.size[1] / logo.size[0])
    logo = logo.resize((lw, lh), Image.Resampling.LANCZOS)
    img.paste(logo, (55, 50), logo)
    logo_bottom = 50 + lh
else:
    logo_bottom = 120

# Load fonts
try:
    font_bold = ImageFont.truetype('Poppins-Bold.ttf', 23)
    font_semi = ImageFont.truetype('Poppins-SemiBold.ttf', 16)
    font_med = ImageFont.truetype('Poppins-Medium.ttf', 14)
    font_small = ImageFont.truetype('Poppins-Medium.ttf', 12)
    font_tagline = ImageFont.truetype('Montserrat.ttf', 12)
except Exception as e:
    font_bold = font_semi = font_med = font_small = font_tagline = ImageFont.load_default()

# Slogan / headline
draw.text((60, logo_bottom + 18), "INDIA'S MOST AFFORDABLE WEBSITE BUILDER", fill=(15, 23, 42), font=font_bold)
draw.text((60, logo_bottom + 52), "Flat Rs 5,000 One-Time  |  Zero Subscriptions  |  Lifetime Hosting", fill=(2, 132, 199), font=font_semi)

# Feature bullet badges
badges = ['* 100% Mobile Responsive', '* 3D Interactive Digital Card', '* Google SEO & Ultra-Fast Speed', '* Free Domain & SSL Included']
bx = 60
by = logo_bottom + 92
for i, badge in enumerate(badges):
    col = i % 2
    row = i // 2
    draw.text((bx + col * 240, by + row * 28), badge, fill=(71, 85, 105), font=font_med)

# Generate QR code for back
qr = qrcode.QRCode(version=1, box_size=5, border=2)
qr.add_data('https://portfolio.vtkro.com/')
qr.make(fit=True)
qr_img = qr.make_image(fill_color='#0f172a', back_color='white').convert('RGBA')
qr_w, qr_h = 165, 165
qr_img = qr_img.resize((qr_w, qr_h), Image.Resampling.LANCZOS)

# Paste QR on right
qrx = w - qr_w - 75
qry = 60
draw.rounded_rectangle([qrx - 10, qry - 10, qrx + qr_w + 10, qry + qr_h + 38], radius=14, fill=(248, 250, 252, 255), outline=(226, 232, 240, 255), width=2)
img.paste(qr_img, (qrx, qry), qr_img)
draw.text((qrx + 15, qry + qr_h + 8), "SCAN TO CONNECT", fill=(14, 165, 233), font=font_bold)

# Contact info below QR
cy = qry + qr_h + 55
draw.text((qrx - 15, cy), "Phone: +91 9676700488", fill=(15, 23, 42), font=font_semi)
draw.text((qrx - 15, cy + 28), "Web: Vtkro.com", fill=(2, 132, 199), font=font_semi)
draw.text((qrx - 15, cy + 56), "Email: Vtkro@gmail.com", fill=(71, 85, 105), font=font_semi)
draw.text((qrx - 15, cy + 84), "Location: Chattisgarh, India", fill=(100, 116, 139), font=font_med)

# Bottom footer bar
draw.line([(50, h - 55), (w - 50, h - 55)], fill=(226, 232, 240, 255), width=1)
draw.text((60, h - 42), "EXPLORE   |   EXPERIENCE   |   VIRTUALLY", fill=(100, 116, 139), font=font_tagline)
draw.text((w - 240, h - 42), "VTKRO DIGITAL ID #9050", fill=(148, 163, 184), font=font_tagline)

img.convert('RGB').save('vtkro-card-back-white.png', 'PNG', quality=95)
print('Successfully generated vtkro-card-back-white.png')
