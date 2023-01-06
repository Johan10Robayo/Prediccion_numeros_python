import pickle
import cv2 as cv
fichero=open("ArraysTrain","rb")
lista=pickle.load(fichero)


print(lista[179])
cv.imwrite('Imgprueba.bmp',lista[180])