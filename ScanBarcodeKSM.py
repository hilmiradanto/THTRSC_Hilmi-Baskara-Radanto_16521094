import cv2
import numpy as py
from pyzbar.pyzbar import decode

img = cv2.imread('QRKSM.jpg')

for code in decode(img):
    print(code.type)
    print(code.data.decode('utf-8'))