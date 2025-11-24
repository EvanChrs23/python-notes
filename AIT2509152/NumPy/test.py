import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'
import tensorflow as tf

a = tf.constant([1, 2, 3])
b = tf.constant([4, 5, 6])
print(a * b)