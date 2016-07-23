import tensorflow as tf
import numpy as np


W = tf.Variable(
      tf.random_uniform([10, 5], -1.0, 1.0),
       name="W")

sess = tf.Session()
sess.run(tf.initialize_all_variables())
#print( sess.run( tf.nn.embedding_lookup ( tf.random_uniform([10, 5], -1.0, 1.0), 2)))

print( sess.run(W))

embedded_chars = tf.nn.embedding_lookup(W, 2)
print( sess.run(embedded_chars))
embedded_chars_expanded = tf.expand_dims(W, -1)
print( sess.run(embedded_chars_expanded))
