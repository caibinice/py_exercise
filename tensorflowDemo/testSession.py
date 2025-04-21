import tensorflow as tf

# 解决tf版本问题，2.0无法兼容1.0，所以需要禁用2.0功能
tf.compat.v1.disable_eager_execution()

# create two matrixes
matrix1 = tf.compat.v1.constant([[3,3]])
matrix2 = tf.compat.v1.constant([[2],
                       [2]])
product = tf.compat.v1.matmul(matrix1, matrix2)
sess = tf.compat.v1.Session()
result = sess.run(product)
print(result)
sess.close()
# [[12]]

# method 2
with tf.compat.v1.Session() as sess:
    result2 = sess.run(product)
    print(result2)
# [[12]]