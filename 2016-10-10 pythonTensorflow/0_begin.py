import numpy as np
import tensorflow as tf

print("\n")
print("\n")
print("*****Start! Ndarray library : numpy vs tensorflow*****")

a = tf.zeros((2,2)); b = tf.ones((2,2))

show_a = tf.reduce_sum(b, reduction_indices=1).eval #syntactic sugar
show_b = a.get_shape
show_c = tf.reshape(a, (1,4)).eval
show_d = b*5+1
show_e = tf.matmul(a, b)
show_f = a[0,0], a[:,0], a[0,:]

print(show_a)
print(show_b)
print(show_c)
print(show_d)
print(show_e)
print(show_f)

# [note] be careful about computation graph!
# TensorFlow computations define a computation graph that has no numerical value until evaluated!
# Tensor is a multidimensional array of numbers

print("\n")
print("\n")
print("*****First graph!*****")

matrix1 = tf.constant([[3., 3.]])
matrix2 = tf.constant([[2.], [2.]])
matrix3 = tf.ones((2,2))
matrix4 = tf.random_normal((2,2))

matrix_buf = tf.Variable(tf.zeros((2,2)))

product_a = tf.matmul(matrix1, matrix2)
add = tf.assign_add(matrix_buf, matrix3)
assign = tf.assign(matrix_buf, matrix4)

init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    print(product_a.eval(),"\n")

    for _ in range(3):
        sess.run(add)
        print(matrix_buf.eval())

    sess.run(assign)
    print("\n",matrix_buf.eval(),"\n")

# [note] other modification
# tf.InteractiveSession
# with tf.device("/gpu:1"):


print("\n")
print("\n")


# References
# http://blog.moebigdata.com/2016/01/tensorflow.html?m=1
# http://blog.bryanbigdata.com/2016/02/python-google-deep-learning-tensorflow.html?m=1
# http://ntudavid.blogspot.tw/2016/01/deep-learning-tensorflowpython33.html?m=1
# http://blog.twman.org/2016/06/tensorflow.html?m=1




