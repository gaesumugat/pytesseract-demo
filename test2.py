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
    scale_percent = 40# percent of original size
    width = int(readImg.shape[1] * scale_percent / 100)
    height = int(readImg.shape[0] * scale_percent / 100)
    dim = (width, height)
    image = cv2.resize(readImg, dim, interpolation = cv2.INTER_AREA)
    return image


img = 'input/phone_texts/arial_phone.jpg'
text = ocr(processImg(img))
print(text)
cv2.imshow('Output', processImg(img))
cv2.waitKey()
