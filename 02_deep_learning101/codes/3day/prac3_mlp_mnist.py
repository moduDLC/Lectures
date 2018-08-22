# -*- coding: utf-8 -*-

from __future__ import print_function

import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout

batch_size = 128
num_classes = 10
epochs = 20

# the data, shuffled and split between train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

model = Sequential()

#############################################
################## Code ##################
#############################################
#### 주석에 맡게 ? 부분을 채우세요.
# 512개의 뉴런, activation : 'relu'의 Dense Layer
model.add(Dense(?, activation='?', input_shape=(784,)))
# 512개의 뉴런, activation : 'relu'
model.add(Dense(?, activation='?'))
# Class의 수 많큼의 뉴런, activation : 'softmax'
model.add(Dense(?, activation='?'))

#############################################
################## End of your Code ##################
#############################################

model.summary()

# loss 는 크로스 엔트로피, Optimizer는 RMSprop(), metric : 학습이 아닌 평가할 때 사용하는 것.
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

# epoch : 모델이 학습데이터 젠체를 살펴본 횟수
history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1,
                    validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
