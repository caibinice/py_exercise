# import tensorflow as tf

import tensorflow._api.v2.compat.v1 as tf

# 解决tf版本问题，2.0无法兼容1.0，所以需要禁用2.0功能
tf.disable_eager_execution()

# 在 Tensorflow 中需要定义 placeholder 的 type ，一般为 float32 形式
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

# mul = multiply 是将input1和input2 做乘法运算，并输出为 output
output = tf.multiply(input1, input2)

with tf.Session() as sess:
    print(sess.run(output, feed_dict={input1: [7.], input2: [2.]}))
# [ 14.]
