# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tensorflow as tf
from keras.models import Sequential
from keras.layers import MaxPooling2D

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# =============================================================================
# print(len(x_train))
# print(x_train[0].shape)
# =============================================================================

model = Sequential()
