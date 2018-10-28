# -*- coding: utf-8 -*-


import cv2
import os

# 파일의 directory리스트
files = os.listdir('C:\\Users\\Kim\\Desktop\\OpenCV_tutorial')

# 파일 안의 이미지 파일의 경로 리스트
imgfiles = []

for x in files:
    if x.endswith('png'):
        print(x)
        imgfile = 'C:\\Users\\Kim\\Desktop\\OpenCV_tutorial\\' + x
        imgfiles.append(imgfile)

gray = False
# gray 이면 1 아니면 0
k = 0
# f을 눌렀을 때, 다음 파일
# b을 눌렀을때, 뒷 파일


drawing = False
ix, iy = -1, -1
B = 256
G = 0
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


img = cv2.imread(imgfiles[k])
cv2.namedWindow(imgfiles[k], cv2.WINDOW_NORMAL)

while True:
    cv2.setMouseCallback(imgfiles[k], draw_rectangle, param=img)
    cv2.imshow(imgfiles[k], img)
    a = cv2.waitKey(0)

    print(k)
    print(imgfiles[k])

    if a == ord('f'):
        k = k + 1
        if k == 3:
            k = 0
        cv2.destroyAllWindows()
        img = cv2.imread(imgfiles[k])
        cv2.namedWindow(imgfiles[k], cv2.WINDOW_NORMAL)


    elif a == ord('b'):
        k = k - 1
        if k == -3:
            k = 2
        cv2.destroyAllWindows()
        img = cv2.imread(imgfiles[k])
        cv2.namedWindow(imgfiles[k], cv2.WINDOW_NORMAL)


    elif a == ord('g'):
        if gray == True:
            gray = False
            cv2.destroyAllWindows()
            img = cv2.imread(imgfiles[k])
            cv2.namedWindow(imgfiles[k], cv2.WINDOW_NORMAL)


        else:
            gray = True
            cv2.destroyAllWindows()
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.namedWindow(imgfiles[k], cv2.WINDOW_NORMAL)

    elif a == ord('r'):
        cv2.destroyAllWindows()
        img = cv2.imread(imgfiles[k])
        cv2.namedWindow(imgfiles[k], cv2.WINDOW_NORMAL)


    elif a == 27:
        break

cv2.destroyAllWindows()