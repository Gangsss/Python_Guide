# -*- coding: utf-8 -*-

import cv2
import os

# 파일의 directory리스트
files = os.listdir()

imgfiles = []
photo_name = []

# 파일 안의 이미지 파일의 경로 리스트
for photo in files:
    if photo.endswith('png'or'jpg'or'jpeg'):
        photo_name.append(photo)
        imgfile = 'C:\\Users\\Kim\\Desktop\\OpenCV_tutorial\\' + photo
        imgfiles.append(imgfile)

if imgfiles is False:
    print('no photo in this file')

else:
    print('there is photo in here')
    print(photo_name)

gray = False
# gray 이면 1 아니면 0
k = 0
# f을 눌렀을 때, 다음 파일
# b을 눌렀을때, 뒷 파일

drawing = False
B = 256
G = 0
R = 0


def draw_rectangle(event, x, y, flags, param):
    global drawing, left_point, right_point
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        left_point = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        right_point = (x, y)
        print('왼쪽 위 좌표 :' ,left_point, '오른쪽 아래 좌표 :',right_point)
        cv2.rectangle(param, left_point, right_point, (B, G, R), 1)
        cv2.imshow(imgfiles[k],img)

img = cv2.imread(imgfiles[k])
cv2.namedWindow(imgfiles[k], cv2.WINDOW_NORMAL)
print('f을 누르면 앞의 파일로 가고 \nb를 누르면 뒤의 파일로 갑니다.\ng를 누르면 gray화 됩니다.\nr을 누르면 reset \nESC를 눌러 나갈 수 있습니다.')

while True:
    print('현재 파일의 위치는', os.getcwd())
    print('현재 파일은 :', imgfiles[k])
    cv2.setMouseCallback(imgfiles[k], draw_rectangle, param=img)
    cv2.imshow(imgfiles[k], img)
    a = cv2.waitKey(0)

    if a == ord('f'):
        k = k + 1
        if k == 3:
            k = 0
        cv2.destroyAllWindows()
        img = cv2.imread(imgfiles[k])
        cv2.namedWindow(imgfiles[k], cv2.WINDOW_NORMAL)


    elif a ==ord('b'):
        k = k - 1
        if k == -3:
            k = 2
        cv2.destroyAllWindows()
        img = cv2.imread(imgfiles[k])
        cv2.namedWindow(imgfiles[k], cv2.WINDOW_NORMAL)


    elif a == ord('g'):
        if gray is True:
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
        left_point = ()
        right_point = ()
        cv2.destroyAllWindows()
        img = cv2.imread(imgfiles[k])
        cv2.namedWindow(imgfiles[k], cv2.WINDOW_NORMAL)

    elif a == ord('c'):
        cv2.destroyAllWindows()
        crop_img = img[left_point[1]:right_point[1],left_point[0]:right_point[0]]
        cv2.imshow('croped',crop_img)
        print('cropped image')
        print('아무 키나 누르면 뒤로 갑니다.')
        a = cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif a == 27:  # esc
        print('종료합니다')
        quit()