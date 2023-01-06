import keras
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense,Dropout
from tensorflow.keras.utils import to_categorical



(x_train,y_train),(x_test,y_test)=mnist.load_data()

img1 = cv.imread('ImgNum28x28.bmp',0)
#print(img1)
x_test[0]=img1
x_train[0]=img1
x_train=x_train.reshape(-1,28*28)
x_train=x_train/255
x_test=x_test.reshape(-1,28*28)
x_test=x_test/255

#trainig model
model=Sequential([
    Dense(1024,activation='relu',input_shape=(784,)),
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
    epochs=5,
    batch_size=16,
)

eval=model.evaluate(x_test,to_categorical(y_test))
predictions=model.predict(x_test[0:10])

plt.imshow(predictions)
print(np.argmax(predictions[0]))