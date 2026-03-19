import numpy as np
import cv2 as cv
from PIL import Image

def preprocess(img_src):
    img = np.array(Image.open(img_src))
    img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    img = cv.convertScaleAbs(img, alpha=1.2)

    return img