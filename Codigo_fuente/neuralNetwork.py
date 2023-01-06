import pickle

import keras
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense,Dropout
from tensorflow.keras.utils import to_categorical
from keras.models import load_model



class RedNeuronal:

    def __init__(self):
        pass


    #Load database handwriting digit
    def reconocerNumero(self):

        model = load_model('My_model.h5')
        x_test=cv.imread('ImgNum28x28.bmp', 0)
        x_test = x_test.reshape(-1, 28 * 28)
        x_test = x_test / 255

        #eval = model.evaluate(x_test, to_categorical(y_test))
        predictions = model.predict(x_test)

        num=np.argmax(predictions[0])
        return num




