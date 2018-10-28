# -*- coding: utf-8 -*-

import cv2
import os

# 파일의 directory리스트
files = os.listdir('C:\\Users\\Kim\\Desktop\\OpenCV_tutorial')

imgfiles = []

for x in files:
    if x.endswith('png'):
        print(x)
        imgfile = 'C:\\Users\\Kim\\Desktop\\OpenCV_tutorial\\' + x
        imgfiles.append(imgfile)

drawing = False
ix, iy = -1, -1
B = 0
G = 256
R = 0


def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(param, (ix, iy), (x, y), (B, G, R), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(param, (ix, iy), (x, y), (B, G, R), -1)


# 파일 안의 이미지 파일의 경로 리스트
img = cv2.imread(imgfiles[0])
cv2.namedWindow('paint')
cv2.setMouseCallback('paint', draw_rectangle, param=img)

while True:
    cv2.imshow('paint', img)
    k = cv2.waitKey(1)
    if k == 27:
        cv2.destroyAllWindows()
        break