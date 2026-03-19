from pathlib import Path
from PIL import Image

def scan_gallery(folder_path: str) -> list[str]:
    res = []
    extensions = ("*.jpg", "*.jpeg", "*.png")

    for ext in extensions:
        for file in Path(folder_path).rglob(ext):
            try:
                width, height = Image.open(file).size
                if height / width >= 1.5:
                    res.append(str(file))
            except Exception:
                pass
    return res