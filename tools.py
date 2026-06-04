import os
import re
import base64

# Ensure the output directory exists
os.makedirs("img", exist_ok=True)

# Read the HTML document
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Pattern to locate base64 images inside data URIs
pattern = r'data:image/(png|jpeg|jpg|gif);base64,([A-Za-z0-9+/={}\s\n\r]+)'

count = 0

def replacement_callback(match):
    global count
    ext = match.group(1)
    base64_data = match.group(2).strip().replace("\n", "").replace("\r", "")
    
    # Generate meaningful names based on appearance order or index
    filename = f"hero-bg.{ext}" if count == 0 else f"logo.{ext}"
    filepath = f"img/{filename}"
    
    # Decode and save the image file
    try:
        with open(filepath, "wb") as img_file:
            img_file.write(base64.b64decode(base64_data))
        print(f"Extracted: {filepath}")
    except Exception as e:
        print(f"Failed to decode image {count}: {e}")
        return match.group(0)  # Return original if it fails
        
    count += 1
    return filepath

# Replace data URIs with the new local asset relative paths
new_html_content = re.sub(pattern, replacement_callback, html_content)

# Write out the modernized index.html file
with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_html_content)

print("Finished processing index.html and updating references.")