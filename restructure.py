import os
import shutil
import glob

base_dir = r"c:\Users\vigne\demo1neuro"

# Rename android to android_project
android_src = os.path.join(base_dir, "android")
android_dst = os.path.join(base_dir, "android_project")
if os.path.exists(android_src):
    try:
        os.rename(android_src, android_dst)
        print("Renamed android to android_project")
    except Exception as e:
        print(f"Error renaming android: {e}")

# Rename frontend to web_project
frontend_src = os.path.join(base_dir, "frontend")
frontend_dst = os.path.join(base_dir, "web_project")
if os.path.exists(frontend_src):
    try:
        os.rename(frontend_src, frontend_dst)
        print("Renamed frontend to web_project")
    except Exception as e:
        print(f"Error renaming frontend: {e}")

# Move items to web_project
items_to_move = [
    "backend",
    "selenium-tests",
    ".firebase",
    ".firebaseignore",
    ".firebaserc",
    "firebase.json",
    "firestore.rules",
    "local-auth.js"
]

for item in items_to_move:
    src = os.path.join(base_dir, item)
    if os.path.exists(src):
        try:
            shutil.move(src, os.path.join(frontend_dst, item))
            print(f"Moved {item}")
        except Exception as e:
            print(f"Error moving {item}: {e}")

# Move python scripts
py_files = glob.glob(os.path.join(base_dir, "*.py"))
for py_file in py_files:
    if os.path.basename(py_file) == "restructure.py":
        continue
    try:
        shutil.move(py_file, os.path.join(frontend_dst, os.path.basename(py_file)))
        print(f"Moved {os.path.basename(py_file)}")
    except Exception as e:
        print(f"Error moving {os.path.basename(py_file)}: {e}")
