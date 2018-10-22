import cv2
import os

# 파일의 directory 리스트
files = os.listdir('C:\\Users\\Kim\\Desktop\\OpenCV_tutorial')

# 파일 안의 이미지 파일의 경로 리시트
imgfiles = []

for x in files:
    if x.endswith('png'):
        print(x)
        imgfile = 'C:\\Users\\Kim\\Desktop\\OpenCV_tutorial\\' + x
        imgfiles.append(imgfile)

k = 0
# f을 눌렀을 때, 다음 파일로
# b을 눌렀을때, 뒷 파일로
# k=3, k=-4이 되서 indexError을 피하기 위해

while True:
    if k == 3:
        k = 0
    elif k == -4:
        k = 2
    img = cv2.imread(imgfiles[k])
    cv2.imshow('abc', img)
    print(imgfiles[k])
    a = cv2.waitKey(0)
    if a == ord('f'):
        k = k + 1
        cv2.destroyAllWindows()
    elif a == ord('b'):
        k = k - 1
        cv2.destroyAllWindows()
    elif a == 27:
        cv2.destroyAllWindows()
        break