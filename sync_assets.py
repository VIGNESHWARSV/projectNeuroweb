import os
import shutil
import subprocess
import sys

def check_pillow():
    try:
        from PIL import Image
        return True
    except ImportError:
        print("Pillow library is missing. Attempting to install...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
            from PIL import Image
            return True
        except Exception as e:
            print(f"Failed to install Pillow: {e}")
            print("Will fallback to standard XML icon configurations.")
            return False

def generate_icons(source_logo_path, res_dir):
    if not os.path.exists(source_logo_path):
        print(f"Warning: Source logo.png not found at {source_logo_path}. Cannot generate icons.")
        return False
        
    if not check_pillow():
        return False
        
    from PIL import Image, ImageDraw
    
    # Target densities and sizes for launcher icons
    icon_sizes = {
        "mipmap-mdpi": 48,
        "mipmap-hdpi": 72,
        "mipmap-xhdpi": 96,
        "mipmap-xxhdpi": 144,
        "mipmap-xxxhdpi": 192
    }
    
    try:
        img = Image.open(source_logo_path).convert("RGBA")
        
        for folder_name, size in icon_sizes.items():
            folder_path = os.path.join(res_dir, folder_name)
            os.makedirs(folder_path, exist_ok=True)
            
            # 1. Standard square/rectangular launcher icon
            resized_icon = img.resize((size, size), Image.Resampling.LANCZOS)
            icon_path = os.path.join(folder_path, "ic_launcher.png")
            resized_icon.save(icon_path, "PNG")
            
            # 2. Round launcher icon
            mask = Image.new("L", (size, size), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, size, size), fill=255)
            
            round_icon = Image.new("RGBA", (size, size), (0, 0, 0, 0))
            round_icon.paste(resized_icon, (0, 0), mask=mask)
            
            round_icon_path = os.path.join(folder_path, "ic_launcher_round.png")
            round_icon.save(round_icon_path, "PNG")
            
        print("Successfully generated launcher icons for all densities (MDPI to XXXHDPI).")
        return True
    except Exception as e:
        print(f"Error generating launcher icons: {e}")
        return False

def sync():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(base_dir, "android", "app", "src", "main", "assets")
    res_dir = os.path.join(base_dir, "android", "app", "src", "main", "res")
    
    # 1. Create assets directory if not exists
    os.makedirs(assets_dir, exist_ok=True)
    
    # 2. Files to synchronize
    files_to_sync = [
        "index.html",
        "style.css",
        "app.js",
        "authentication.js",
        "database.js",
        "firebase-config.js",
        "firebase-main.js",
        "logo.png"
    ]
    
    print("Synchronizing web assets to Android assets folder...")
    for filename in files_to_sync:
        src_path = os.path.join(base_dir, "frontend", filename)
        dest_path = os.path.join(assets_dir, filename)
        
        if os.path.exists(src_path):
            shutil.copy2(src_path, dest_path)
            print(f" -> Copied: {filename}")
        else:
            print(f" -> Warning: Source file not found: {filename}")
            
    # 3. Generate launcher icons from logo.png
    logo_path = os.path.join(base_dir, "frontend", "logo.png")
    generate_icons(logo_path, res_dir)

if __name__ == "__main__":
    sync()
