import cv2
import pytesseract

img = cv2.imread('input/arial.png')
cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#character detection
# hImg, wImg, _ = img.shape
# boxes = pytesseract.image_to_boxes(img, config = " -c tessedit_create_boxfile=1")
# for box in boxes.splitlines():
#     print(box)
#     box = box.split(' ')
#     x,y,w,h = int(box[1]),int(box[2]),int(box[3]),int(box[4])
#     cv2.rectangle(img, (x,hImg-y),(w,hImg-h), (0,0,255),2)
    
# cv2.imshow('Result', img)
# cv2.waitKey(0)

#word detection with filter
wordFilter = 'BOLD.'
hImg, wImg, _ = img.shape
boxes = pytesseract.image_to_data(img)
for x,box in enumerate(boxes.splitlines()):
    if x!=0:
        box = box.split()
        if len(box)==12 and box[11] == wordFilter:
            x,y,w,h = int(box[6]),int(box[7]),int(box[8]),int(box[9])
            cv2.rectangle(img, (x,y),(w+x,h+y), (0,0,255),2)
    
cv2.imshow('Result', img)
cv2.waitKey(0)
