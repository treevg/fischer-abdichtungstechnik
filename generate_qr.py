import qrcode
import qrcode.image.svg
import re

def generate_whatsapp_qr():
    # The exact WhatsApp Link to encode
    link = "https://wa.me/49216224716?text=Hallo%20Fischer-Team%2C%20ich%20habe%20ein%20Feuchtigkeitsproblem%20und%20interessiere%20mich%20f%C3%BCr%20die%20kostenlose%20Schadenanalyse."
    
    # Create QR Code instance
    # Box size is 10, border is 4 (standard parameters)
    qr = qrcode.QRCode(
        version=None,  # Automatically detect version (usually version 4-6 for this link length)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction to allow center logo masking!
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    
    # Generate SvgPathImage
    factory = qrcode.image.svg.SvgPathImage
    img = qr.make_image(image_factory=factory)
    
    # Render SVG as string
    svg_bytes = img.to_string()
    svg_str = svg_bytes.decode('utf-8')
    
    # We want to find the viewBox dimensions of the generated SVG
    # SvgPathImage output structure typically starts with:
    # <svg viewBox="0 0 370 370" ...
    match = re.search(r'viewBox="0 0 (\d+) (\d+)"', svg_str)
    if match:
        width = int(match.group(1))
        height = int(match.group(2))
    else:
        width = 370
        height = 370
        
    print(f"Generated QR SVG with dimensions: {width}x{height}")
    
    # Let's calculate the center coordinates for the WhatsApp logo overlay.
    # We want the logo to span about 18% of the total size.
    logo_size = int(width * 0.18)
    logo_x = (width - logo_size) // 2
    logo_y = (height - logo_size) // 2
    
    # We will insert a white background square to clear the QR code patterns in the center,
    # and then draw the official WhatsApp SVG logo inside that white square.
    overlay_html = f"""
    <!-- White background square behind central logo -->
    <rect x="{logo_x - 4}" y="{logo_y - 4}" width="{logo_size + 8}" height="{logo_size + 8}" fill="white" rx="6" ry="6"/>
    <!-- Official WhatsApp SVG icon -->
    <image href="images/icons8-whatsapp.svg" x="{logo_x}" y="{logo_y}" width="{logo_size}" height="{logo_size}"/>
</svg>"""
    
    # Replace the closing </svg> tag with our overlay and the closing tag
    modified_svg = svg_str.replace("</svg>", overlay_html)
    
    # Save the beautiful gebrandeten QR Code SVG
    with open("images/whatsapp_qr.svg", "w") as f:
        f.write(modified_svg)
        
    print("Successfully generated and saved gebrandeten QR Code to images/whatsapp_qr.svg")

if __name__ == "__main__":
    generate_whatsapp_qr()
