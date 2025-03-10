from PIL import Image, ImageDraw, ImageFont
import os
from pathlib import Path

images_dir = Path("app/static/images")
images_dir.mkdir(parents=True, exist_ok=True)

img = Image.new('RGB', (800, 600), color=(240, 240, 240))
d = ImageDraw.Draw(img)

text = "Waiting for images..."
try:
    font = ImageFont.truetype("Arial", 40)
except IOError:

    font = ImageFont.load_default()

text_width, text_height = d.textsize(text, font=font) if hasattr(d, 'textsize') else (300, 40)
position = ((800 - text_width) // 2, (600 - text_height) // 2)

d.text(position, text, fill=(100, 100, 100), font=font)

placeholder_path = images_dir / "5.jpg"
img.save(placeholder_path)

print(f"Created placeholder image at {placeholder_path}")