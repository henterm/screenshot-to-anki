import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import easyocr
import numpy as np

reader = easyocr.Reader(['ru', 'en'])
def extract_text(img: np.ndarray) -> list:
    return reader.readtext(img)