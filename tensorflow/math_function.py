# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 22:30:43 2021

@author: JLong
"""

import tensorflow as tf
import numpy as np
tf.compat.v1.disable_eager_execution()
# create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.9 + 0.3

### create tensorflow structure start ###
Weights = tf.Variable(tf.random.uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights*x_data + biases

loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.compat.v1.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)
### create tensorflow structure end ###

sess = tf.compat.v1.Session()
init=tf.compat.v1.global_variables_initializer()
sess.run(init)

for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(Weights), sess.run(biases))