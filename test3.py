import cv2
import pytesseract
import os
from csv import writer
from pytesseract import Output
import numpy as np

def appendRow(fname, row):
    with open(fname, 'a+',newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(row)

image = cv2.imread('./input/tables/table-data2.png')

# scale_percent = 25 # percent of original size
# width = int(image.shape[1] * scale_percent / 100)
# height = int(image.shape[0] * scale_percent / 100)
# dim = (width, height)
# image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

result = image.copy()
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Remove horizontal lines
horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (40,1))
remove_horizontal = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
cnts = cv2.findContours(remove_horizontal, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    cv2.drawContours(result, [c], -1, (255,255,255), 5)

# Remove vertical lines
vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,40))
remove_vertical = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, vertical_kernel, iterations=2)
cnts = cv2.findContours(remove_vertical, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    cv2.drawContours(result, [c], -1, (255,255,255), 5)

text = pytesseract.image_to_data(result, lang='eng',config='--psm 4 --oem 3', output_type=Output.DATAFRAME)
boxes = pytesseract.image_to_data(result, config='--psm 4 --oem 3')
row = []

for i in text['text']:
    if str(i) != 'nan':
        row.append(i)
    else:
        if len(row) != 0:
            appendRow('table.csv', row)
            row = []

hImg, wImg, _ = image.shape
for x,box in enumerate(boxes.splitlines()):
    if x!=0:
        box = box.split()
        if len(box)==12:
            x,y,w,h = int(box[6]),int(box[7]),int(box[8]),int(box[9])
            cv2.rectangle(image, (x,y),(w+x,h+y), (0,0,255),1)

cv2.imshow('boxes', image)
cv2.waitKey()
