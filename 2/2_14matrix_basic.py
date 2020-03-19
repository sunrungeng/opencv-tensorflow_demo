# -*- coding: utf-8 -*-

import tensorflow as tf

# data1 = tf.placeholder(tf.float32)
# data2 = tf.placeholder(tf.float32)
# dataAdd = tf.add(data1, data2)
# with tf.Session() as sess:
#     print(sess.run(dataAdd, feed_dict={data1: 6, data2: 2}))

d1 = tf.constant([[6, 6]])
d2 = tf.constant([[6],
                  [6]])
d3 = tf.constant([[2, 3],
                  [3, 4],
                  [4, 5]])
with tf.Session() as sess:
    print(sess.run(d3[0]))
    print(sess.run(d3[:, 1]))
