import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('test1.png')
rows, cols, channels = img.shape
bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_,thresh =  cv2.threshold(bw, 190,255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
min_x = 10000
max_x = 0
min_y = 10000
max_y = 0

for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        if x<min_x:
            min_x = x
        if y<min_y:
            min_y = y
        if x+w>max_x:
            max_x = x+w
        if y+h>max_y:
            max_y = y+h

avg_x = int((min_x+max_x)/2)

cv2.rectangle(img, (min_x,min_y), (max_x,max_y), (255,0,255), 2)
cv2.line(img, (avg_x, 0), (avg_x, cols), (0,0,255), 2)

cv2.imshow('window', img)
cv2.waitKey()
cv2.destroyAllWindows()