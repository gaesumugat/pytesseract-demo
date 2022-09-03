import cv2
import pytesseract

def ocr(img):
    text = pytesseract.image_to_string(img)
    return text

img = cv2.imread('lorem.png')

def get_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def remove_noise(img):
    return cv2.medianBlur(img, 5)

def thresholding(img):
    return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

img = get_grayscale(img)
img = thresholding(img)
img = remove_noise(img)

data = ocr(img).split('\n')

with open('output.txt', 'w') as f:
    for line in data:
        f.write(line)
        f.write('\n')