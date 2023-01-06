import numpy as np
import cv2 as cv
import pickle

NumArrays=np.zeros((200,28,28))
for i in range(0,200):
    drawing = False  # true if mouse is pressed
    # mouse callback function
    def draw_circle(event, x, y, flags, param):
        global drawing
        if event == cv.EVENT_LBUTTONDOWN:
            drawing = True
        elif event == cv.EVENT_MOUSEMOVE:
            if drawing == True:
                cv.circle(img, (x, y),11,255,-1)
        elif event == cv.EVENT_LBUTTONUP:
            drawing = False
            cv.circle(img, (x, y),11,255,-1)


    img = np.zeros((280,280), np.uint8)
    cv.namedWindow('image')
    cv.setMouseCallback('image', draw_circle)
    while (1):
        cv.imshow('image', img)
        k = cv.waitKey(10) & 0xFF
        if k == 27:
            break
    cv.destroyAllWindows()

    res = cv.resize(img, dsize=(28, 28), interpolation=cv.INTER_CUBIC)
    NumArrays[i]=res
    print("Van ",i+1," números")

"""
fichero_binario=open("ArraysTrain","wb")
pickle.dump(NumArrays,fichero_binario)
fichero_binario.close()"""



"""
fichero=open("ArraysTrain","rb")
lista=pickle.load(fichero)


print(lista[1])
cv.imwrite('Imgprueba.bmp',lista[1])"""
#print(len(NumArrays[0]))
#cv.imwrite('Imgprueba.bmp',NumArrays[0])

