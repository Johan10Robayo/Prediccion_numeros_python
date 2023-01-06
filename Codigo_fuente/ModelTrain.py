import keras
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense,Dropout
from tensorflow.keras.utils import to_categorical
import pickle



(x_train, y_train) = mnist.load_data()


fichero = open("ArraysTrain", "rb")
ArrayTrain = pickle.load(fichero)

for i in range(0,200):
    x_train[i]=ArrayTrain[i]

n=0
for j in range(0,200):
    if j%20==0 and j!=0:
        n+=1
    y_train[j]=n

y_train[180]=9


x_train = x_train.reshape(-1, 28 * 28)
x_train = x_train / 255


# trainig model
model = Sequential([
    Dense(1024, activation='relu', input_shape=(784,)),
    Dense(256, activation='relu'),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
        ])

model.compile(
    optimizer='Adam',
    loss='categorical_crossentropy',
    metrics='accuracy'
)

model.fit(
    x=x_train,
    y=to_categorical(y_train),
    epochs=20,
    batch_size=16,
)

model.save('My_model.h5')

'''listElments=[x_test,y_test]
fichero_binario=open("DataSets","wb")
pickle.dump(listElments,fichero_binario)
fichero_binario.close()'''
