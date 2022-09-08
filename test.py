import cv2
import pytesseract

img = cv2.imread('./input/tables/table-data.png')
#word detection with filter
#wordFilter = 'text'
#wx, wy = 1000, 1000
hImg, wImg, _ = img.shape
boxes = pytesseract.image_to_data(img, config='--psm 6 --oem 3')
for x,box in enumerate(boxes.splitlines()):
    if x!=0:
        box = box.split()
        if len(box)==12:
            x,y,w,h = int(box[6]),int(box[7]),int(box[8]),int(box[9])
            cv2.rectangle(img, (x,y),(w+x,h+y), (0,0,255),1)

#resized = cv2.resize(img, (wx, wy))
cv2.imshow('Result', img)
cv2.waitKey(0)
