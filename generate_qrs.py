import os
import qrcode
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

products = [
    {"name": "SOIL RICH", "slug": "SOIL-RICH"},
    {"name": "Red Gram", "slug": "Red-Gram"},
    {"name": "Flower", "slug": "Flower"},
    {"name": "Pushpak Gold", "slug": "Pushpak-Gold"},
    {"name": "Chinna", "slug": "Chinna"},
    {"name": "Advin", "slug": "Advin"},
    {"name": "Swarna", "slug": "Swarna"},
    {"name": "Kavacha", "slug": "Kavacha"},
    {"name": "Red Mite", "slug": "Red-Mite"},
    {"name": "Green Max", "slug": "Green-Max"}
]

domain = "https://greech-chi.vercel.app"
output_dir = r"c:\Users\jashw\OneDrive\Desktop\green\qr cods"
os.makedirs(output_dir, exist_ok=True)

print("Starting QR PDF generation...")
for p in products:
    url = f"{domain}/{p['slug']}"
    name = p["name"]
    print(f"Generating for {name} ({url})...")
    
    # 1. Generate QR Code image
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    temp_img_path = f"temp_{p['slug']}.png"
    img.save(temp_img_path)
    
    # 2. Generate PDF with ReportLab
    pdf_filename = f"{name.replace(' ', '_')}.pdf"
    pdf_path = os.path.join(output_dir, pdf_filename)
    
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter
    
    # Draw nice header
    c.setFont("Helvetica-Bold", 28)
    c.setFillColorRGB(0.1, 0.4, 0.2) # Deep green brand color
    c.drawCentredString(width / 2.0, height - 100, name.upper())
    
    c.setFont("Helvetica-Bold", 16)
    c.setFillColorRGB(0.3, 0.3, 0.3)
    c.drawCentredString(width / 2.0, height - 130, "Scan to View Product Registration & Details")
    
    # Draw QR code image
    qr_size = 320
    x_pos = (width - qr_size) / 2.0
    y_pos = (height - qr_size) / 2.0 - 20
    c.drawImage(temp_img_path, x_pos, y_pos, width=qr_size, height=qr_size)
    
    # Draw line separator
    c.setStrokeColorRGB(0.8, 0.8, 0.8)
    c.setLineWidth(1)
    c.line(100, 150, width - 100, 150)
    
    # Draw footer
    c.setFont("Helvetica-Oblique", 11)
    c.setFillColorRGB(0.4, 0.4, 0.4)
    c.drawCentredString(width / 2.0, 120, f"URL: {url}")
    
    c.setFont("Helvetica-Bold", 12)
    c.setFillColorRGB(0.1, 0.4, 0.2)
    c.drawCentredString(width / 2.0, 90, "GREEN CHEMICAL")
    
    c.save()
    
    # Clean up temp image
    if os.path.exists(temp_img_path):
        os.remove(temp_img_path)

print("Done! All QR Codes generated in 'qr cods' folder.")
