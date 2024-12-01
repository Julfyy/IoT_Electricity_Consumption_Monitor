import cv2
import numpy as np
import pytesseract

def preprocess_image(image_data):
    np_img = np.frombuffer(image_data, np.uint8)
    image = cv2.imdecode(np_img, cv2.IMREAD_GRAYSCALE)
    _, binary = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    kernel = np.ones((2, 2), np.uint8)
    processed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel, iterations=1)
    return processed

def recognize_text(image):
    config = "--psm 6"
    text = pytesseract.image_to_string(image, lang='lets', config=config)
    digits = ''.join(filter(lambda x: x.isdigit() or x == '.', text))
    return digits
