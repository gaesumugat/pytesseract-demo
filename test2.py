import cv2
import pytesseract

def ocr(img):
    text = pytesseract.image_to_string(img)
    return text

def get_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def remove_noise(img):
    return cv2.medianBlur(img, 5)

def thresholding(img):
    return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def processImg(img):
    readImg = cv2.imread(img)
    readImg = get_grayscale(readImg)
    readImg = thresholding(readImg)
    readImg = remove_noise(readImg)
    return [x.replace(' ','') for x in ocr(img).split('\n') if x != '']

for item in processImg("./input/multiplication.png"):
    item = item.replace('=', '')
    item = item.replace('x', '*')
    print(str(eval(item)))