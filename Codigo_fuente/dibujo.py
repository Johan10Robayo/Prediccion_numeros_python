
import numpy as np
import cv2 as cv

drawing = False # true if mouse is pressed

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global drawing
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
                cv.circle(img,(x,y),20,(255,255,255),-1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        cv.circle(img,(x,y),20,(255,255,255),-1)
img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
while(1):
    cv.imshow('image',img)
    k = cv.waitKey(10) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()


gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imwrite('ImgAprox1.bmp',gray_image)

img1 = cv.imread('ImgAprox1.bmp',0)
res = cv.resize(img1, dsize=(28,28), interpolation=cv.INTER_CUBIC)

cv.imwrite('ImgNum28x28.bmp',res)
img28=cv.imread('ImgNum28x28.bmp',0)

