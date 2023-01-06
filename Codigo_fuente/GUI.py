from tkinter import *
from neuralNetwork import RedNeuronal
import PIL
import numpy as np
import cv2 as cv
from PIL import ImageTk


drawing = False # true si el mause es presionado

root= Tk()
root.title("MAIN WINDOW")
root.resizable(0,0)



miframe=Frame(root,width=800,height=400)
miframe.pack()

labelTitulo1=Label(miframe,text="Número")
labelTitulo2=Label(miframe,text="Aproximación")
labelImgAproxim=Label(miframe)
labelNum=Label(miframe)

labelTitulo1.grid(row=0,column=0,padx=5,pady=5)
labelTitulo2.grid(row=0,column=1,padx=5,pady=5)
labelImgAproxim.grid(row=1,column=1,sticky="e",padx=5,pady=5)

#----------------Funciones------------
def reconocer():
    global labelImgAproxim
    NN=RedNeuronal()
    numeropredict=NN.reconocerNumero()
    print(numeropredict)
    labelImgAproxim.config(text=numeropredict,font=("Helvetica", 250))

#-------------------Dibujar el número con el raton
def dibujar(event,x,y,flags,param):
    global drawing
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
                cv.circle(img,(x,y),11,(255,255,255),-1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        cv.circle(img,(x,y),11,(255,255,255),-1)

def dibujar1(event1,x1,y1,flags,param):
    global drawing
    global img1
    global auxarray

    if  event1 == cv.EVENT_LBUTTONDOWN:
        drawing = True

    elif  event1 == cv.EVENT_MOUSEMOVE:
        if drawing == True:
                cv.circle(img1,(x1,y1),11,(255,255,255),-1)

    elif  event1 == cv.EVENT_LBUTTONUP:
        drawing = False
        cv.circle(img1,(x1,y1),11,(255,255,255),-1)


def dibujarOtro():
    global auxarray
    global img1
    cv.namedWindow('Imagen Dibujada1')
    cv.setMouseCallback('Imagen Dibujada1', dibujar1)

    while (1):
        cv.imshow('Imagen Dibujada1', img1)
        k = cv.waitKey(10) & 0xFF
        if k == 27:
            break
    cv.destroyAllWindows()
    auxarray = img1
    img1 = np.zeros((280, 280, 3), np.uint8)

    # Guardar imagen creado con el raton
    gray_image = cv.cvtColor(auxarray, cv.COLOR_BGR2GRAY)
    cv.imwrite('ImgNum1.bmp', gray_image)

    # Redimensionar la imagen
    res = cv.resize(gray_image, dsize=(28, 28), interpolation=cv.INTER_CUBIC)
    cv.imwrite('ImgNum28x28.bmp', res)

    im = PIL.Image.open('ImgNum1.bmp')
    ph = ImageTk.PhotoImage(im)
    labelNum.image = ph
    labelNum.config(image=ph)
    labelNum.grid(row=1, column=0, sticky="e", padx=5, pady=5)


img = np.zeros((280,280,3), np.uint8)
img1=np.zeros((280,280,3), np.uint8)
auxarray=np.zeros((280,280,3), np.uint8)
cv.namedWindow('Imagen Dibujada')
cv.setMouseCallback('Imagen Dibujada',dibujar)
while(1):
    cv.imshow('Imagen Dibujada',img)
    k = cv.waitKey(10) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()

#Guardar imagen creado con el raton
gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imwrite('ImgNum.bmp',gray_image)

#Redimensionar la imagen
res = cv.resize(gray_image, dsize=(28,28), interpolation=cv.INTER_CUBIC)
cv.imwrite('ImgNum28x28.bmp',res)



im = PIL.Image.open('ImgNum.bmp')
ph = ImageTk.PhotoImage(im)
labelNum.image=ph
labelNum.config(image=ph)
labelNum.grid(row=1,column=0,sticky="e",padx=5,pady=5)

miframe1=Frame(root)
miframe1.pack()

botonReconocer=Button(miframe1,text = "Reconocer",command=reconocer)
botonReconocer.config(bg="black",fg="white")
botonReconocer.grid(row=0,column=0,sticky="e",padx=5,pady=5)

botonDib=Button(miframe1,text = "Nuevo Número",command=dibujarOtro)
botonDib.config(bg="black",fg="white")
botonDib.grid(row=0,column=1,sticky="e",padx=5,pady=5)

root.mainloop()
